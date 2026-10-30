# -*- coding: utf-8 -*-
"""Análisis sobre la base CWE local: validar datos, auditar referencias del
temario, traducir hallazgos de herramientas SAST a CWE y medir la cobertura
curricular.

Separado de `cwe_lib.py` (que solo sabe importar y consultar) porque estas
funciones miran el REPOSITORIO —clases, laboratorios, soluciones— y cambian
cada vez que se escribe una clase; el catálogo cambia solo cuando MITRE publica.

Principio que rige la cobertura: que el identificador «CWE-89» aparezca en un
archivo no significa que la debilidad se enseñe. Por eso la cobertura se mide
en niveles, y los niveles altos exigen una declaración explícita en el mapa
curricular que el programa VERIFICA contra los archivos reales:

  mencionado        el identificador aparece en algún documento (automático)
  explicado         una clase declarada lo desarrolla (verificado: el archivo
                    existe y trata el tema)
  ejercicio         una clase declarada lo practica (misma verificación)
  laboratorio       un laboratorio declarado lo reproduce (el directorio existe)
  correccion_prueba el laboratorio incluye corrección y una prueba que existe

Un nivel nunca se concede por inferencia: si la declaración apunta a un archivo
que no existe o que ya no trata el tema, la cobertura baja y se informa.
"""
from __future__ import annotations

import csv
import io
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import cwe_lib as L

# Árboles que no son fuente curricular: salida generada o datos de terceros.
EXCLUIR_DIRS = {
    ".git", ".venv", ".vendor", "node_modules", "site", "mobile", "knowledge",
    "__pycache__", "diagramas", "dist", "dist-web", ".github", "salida",
    "scripts",  # herramientas, no temario: sus docstrings citan CWE solo como ejemplo
}
# Informes del propio trabajo CWE y documentos derivados: contarlos como
# «cobertura» sería circular (el informe cita lo que la cobertura mide).
EXCLUIR_ARCHIVOS = {
    "docs/matriz-cobertura-cwe.md",
    "docs/auditoria-cobertura-cwe-cve-cvss.md",
    "docs/implementacion-cwe-progreso.md",
    "docs/GLOSARIO-GLOBAL.md",
}
EXTENSIONES = {".md", ".py", ".sh", ".json", ".yml", ".yaml", ".c", ".txt"}
CWE_RE = re.compile(r"\bCWE-(\d{1,5})\b")
# Las herramientas SAST escriben etiquetas como «external/cwe/cwe-089» (minúsculas,
# con ceros a la izquierda); en los documentos del temario solo valen las mayúsculas.
CWE_ETIQUETA_RE = re.compile(r"\bcwe-(\d{1,5})\b", re.IGNORECASE)
NIVELES_COBERTURA = ("pendiente", "mencionado", "explicado", "ejercicio", "laboratorio", "correccion_prueba")


# --------------------------------------------------------------------------
# Escaneo del repositorio
# --------------------------------------------------------------------------
@dataclass
class Mencion:
    archivo: str      # ruta relativa con '/'
    linea: int
    cwe: str          # 'CWE-89'
    seccion: str      # encabezado '##' más cercano, sin emoji
    texto: str        # inicio de la línea (recortado)
    contexto: str = ""  # ventana alrededor de la mención: la palabra clave puede estar lejos del inicio de un párrafo largo


def _limpiar_encabezado(txt: str) -> str:
    # Quita los emoji y símbolos iniciales de «## 🧪 Laboratorio guiado».
    return re.sub(r"^[^\w¿¡]+", "", txt.strip(), flags=re.UNICODE).strip()


def iter_archivos(raiz: Path = L.RAIZ):
    for ruta in sorted(raiz.rglob("*")):
        if not ruta.is_file() or ruta.suffix.lower() not in EXTENSIONES:
            continue
        partes = ruta.relative_to(raiz).parts
        if any(p in EXCLUIR_DIRS for p in partes[:-1]):
            continue
        rel = "/".join(partes)
        if rel in EXCLUIR_ARCHIVOS:
            continue
        yield ruta, rel


def escanear_menciones(raiz: Path = L.RAIZ) -> list[Mencion]:
    """Todas las apariciones de «CWE-n» en clases, laboratorios, soluciones, rutas y docs."""
    menciones: list[Mencion] = []
    for ruta, rel in iter_archivos(raiz):
        try:
            texto = ruta.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue  # binario o ilegible: no es contenido curricular
        if "CWE-" not in texto:
            continue
        seccion = ""
        for n, linea in enumerate(texto.splitlines(), 1):
            if rel.endswith(".md") and linea.startswith("## "):
                seccion = _limpiar_encabezado(linea[3:])
            for m in CWE_RE.finditer(linea):
                ventana = linea[max(0, m.start() - 160): m.end() + 160]
                menciones.append(Mencion(rel, n, f"CWE-{int(m.group(1))}", seccion, linea.strip()[:240], ventana))
    return menciones


def clase_de_ruta(rel: str) -> int | None:
    m = re.search(r"classes/parte-[^/]+/(\d{3})-[^/]+/", rel)
    return int(m.group(1)) if m else None


def directorio_clase(n: int, raiz: Path = L.RAIZ) -> Path | None:
    hallados = sorted((raiz / "classes").glob(f"parte-*/{n:03d}-*"))
    return hallados[0] if hallados else None


def parte_de_clase(n: int, raiz: Path = L.RAIZ) -> str:
    d = directorio_clase(n, raiz)
    if not d:
        return ""
    m = re.match(r"parte-(\d+)-", d.parent.name)
    return m.group(1) if m else ""


# --------------------------------------------------------------------------
# Mapa curricular (capa pedagógica)
# --------------------------------------------------------------------------
def cargar_mapa(ruta: Path | None = None) -> dict:
    ruta = ruta or (L.PEDAGOGICO / "mapa-curricular.json")
    if not ruta.is_file():
        return {"esquema": L.ESQUEMA, "familias": {}, "entradas": {}}
    return json.loads(ruta.read_text(encoding="utf-8"))


def _texto_norm(ruta: Path) -> str:
    try:
        return L.sin_acentos(ruta.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, OSError):
        return ""


def _trata_tema(texto_norm: str, cwe_id: str, claves: list[str]) -> bool:
    """¿El texto menciona el identificador o alguna palabra clave del tema?"""
    if cwe_id.lower() in texto_norm:
        return True
    return any(L.sin_acentos(k) in texto_norm for k in claves)


# --------------------------------------------------------------------------
# Validación de la base de conocimiento
# --------------------------------------------------------------------------
@dataclass
class Resultado:
    errores: list[str] = field(default_factory=list)
    avisos: list[str] = field(default_factory=list)
    comprobaciones: list[tuple[str, bool, str]] = field(default_factory=list)

    def comprobar(self, nombre: str, ok: bool, detalle: str = "") -> None:
        self.comprobaciones.append((nombre, ok, detalle))
        if not ok:
            self.errores.append(f"{nombre}: {detalle}" if detalle else nombre)

    @property
    def correcto(self) -> bool:
        return not self.errores


CAMPOS_OBLIGATORIOS = ("id", "tipo", "nombre", "abstraccion", "estado", "descripcion", "relaciones")
TIPOS = {"weakness", "grouping"}


def validar_base(raiz_kb: Path | None = None, completo: bool = True) -> Resultado:
    """Comprueba los datos importados: esquema, unicidad, referencias, huellas e índices.

    `completo=False` omite las comprobaciones que solo tienen sentido sobre el
    catálogo entero (p. ej. que el Top 25 tenga 25 miembros); las pruebas
    automáticas lo usan con un extracto.
    """
    kb = raiz_kb or L.KB
    norm, ind = kb / "normalizado", kb / "indices"
    r = Resultado()

    ruta_jsonl = norm / "cwe.jsonl"
    r.comprobar("existe normalizado/cwe.jsonl", ruta_jsonl.is_file(), str(ruta_jsonl))
    if not ruta_jsonl.is_file():
        return r

    entradas, mal_json = [], 0
    for n, ln in enumerate(ruta_jsonl.read_text(encoding="utf-8").splitlines(), 1):
        if not ln.strip():
            continue
        try:
            entradas.append(json.loads(ln))
        except json.JSONDecodeError:
            mal_json += 1
    r.comprobar("todas las líneas de cwe.jsonl son JSON válido", mal_json == 0, f"{mal_json} línea(s) corruptas")

    ids = [e.get("id") for e in entradas]
    dup = sorted({i for i in ids if ids.count(i) > 1})
    r.comprobar("identificadores únicos", not dup, f"duplicados: {dup[:5]}")
    r.comprobar("formato de identificador CWE-n", all(isinstance(i, str) and re.fullmatch(r"CWE-\d+", i) for i in ids))

    faltan = [(e.get("id"), c) for e in entradas for c in CAMPOS_OBLIGATORIOS if c not in e]
    r.comprobar("campos obligatorios presentes", not faltan, f"{faltan[:3]}")
    r.comprobar("tipo de entrada reconocido", all(e.get("tipo") in TIPOS for e in entradas),
                str(sorted({e.get('tipo') for e in entradas} - TIPOS)))
    r.comprobar("nombre y descripción no vacíos (salvo obsoletas)",
                all(e["nombre"] and (e["descripcion"] or e["estado"] == "Deprecated") for e in entradas if "nombre" in e),
                "")

    conocidos = set(ids)
    # Referencias rotas: una relación hacia un CWE que no está en el catálogo.
    # MITRE puede referir entradas retiradas; se cuentan como aviso, no error,
    # salvo que superen un umbral que delataría un catálogo truncado.
    rotas = [(e["id"], rel["id"]) for e in entradas for rel in e.get("relaciones", []) if rel["id"] not in conocidos]
    r.comprobar("integridad de relaciones (destinos existentes)", len(rotas) <= max(5, len(entradas) // 200),
                f"{len(rotas)} destinos ausentes, p. ej. {rotas[:3]}")
    if rotas:
        r.avisos.append(f"{len(rotas)} relaciones apuntan a entradas ausentes del catálogo (p. ej. {rotas[:2]})")

    # Coherencia jerárquica: en la vista 1000 nadie es su propio padre ni hay ciclos.
    padres = {}
    for e in entradas:
        padres[e["id"]] = [x["id"] for x in e.get("relaciones", []) if x["vista"] == L.VISTA_JERARQUIA and x["naturaleza"] == "ChildOf"]
    autopadre = [i for i, ps in padres.items() if i in ps]
    r.comprobar("ninguna entrada es hija de sí misma (vista 1000)", not autopadre, str(autopadre[:3]))

    def hay_ciclo() -> str:
        estado: dict[str, int] = {}
        for ini in padres:
            pila = [(ini, iter(padres.get(ini, [])))]
            estado[ini] = 1
            while pila:
                nodo, it = pila[-1]
                try:
                    p = next(it)
                except StopIteration:
                    estado[nodo] = 2
                    pila.pop()
                    continue
                if estado.get(p) == 1:
                    return f"{nodo} -> {p}"
                if p not in estado and p in padres:
                    estado[p] = 1
                    pila.append((p, iter(padres[p])))
        return ""

    ciclo = hay_ciclo()
    r.comprobar("jerarquía sin ciclos (vista 1000)", not ciclo, ciclo)

    # Vistas
    ruta_v = norm / "vistas.json"
    r.comprobar("existe normalizado/vistas.json", ruta_v.is_file())
    if ruta_v.is_file():
        vistas = json.loads(ruta_v.read_text(encoding="utf-8"))
        vids = [v["id"] for v in vistas]
        r.comprobar("identificadores de vista únicos", len(vids) == len(set(vids)))
        ausentes = [(v["id"], m) for v in vistas for m in v["miembros"] if m not in conocidos]
        r.comprobar("miembros de vistas existentes en el catálogo", not ausentes, f"{ausentes[:3]}")
        if completo:
            top = next((v for v in vistas if "Top 25 Most Dangerous Software Weaknesses" in v["nombre"] and "2025" in v["nombre"]), None)
            r.comprobar("vista Top 25 de 2025 con 25 miembros", bool(top) and len(top["miembros"]) == 25,
                        f"{len(top['miembros']) if top else 'no hallada'}")

    # Procedencia y huellas
    proc = L.leer_procedencia()
    r.comprobar("existe PROCEDENCIA.json", bool(proc))
    if proc:
        r.comprobar("esquema compatible", proc.get("esquema") == L.ESQUEMA, f"{proc.get('esquema')} != {L.ESQUEMA}")
        r.comprobar("catálogo declara versión y fecha", bool(proc["catalogo"]["version"]) and bool(proc["catalogo"]["fecha"]))
        r.comprobar("recuento declarado = entradas reales", proc["catalogo"]["entradas"] == len(entradas),
                    f"{proc['catalogo']['entradas']} != {len(entradas)}")
        alterados = []
        for rel, esperado in proc["huellas"].items():
            ruta = kb / rel
            if not ruta.is_file() or L.sha256_texto(ruta) != esperado:
                alterados.append(rel)
        r.comprobar("huellas SHA-256 de datos e índices coinciden", not alterados,
                    f"modificados o ausentes: {alterados} (¿edición manual? regenera con `cwe_kb.py importar`)")
    r.comprobar("aviso de licencia de MITRE presente", (kb / "LICENCIA-MITRE.md").is_file())

    # El Top 25 guardado debe coincidir, en identificadores y orden, con la vista 1435 del catálogo.
    ruta_t = norm / "top25-2025.json"
    if ruta_t.is_file() and ruta_v.is_file() and completo:
        top25 = json.loads(ruta_t.read_text(encoding="utf-8"))["entradas"]
        vista = next((v for v in vistas if v["id"] == "1435"), None)
        if vista:
            r.comprobar("Top 25 guardado coincide con la vista 1435 (mismos CWE)",
                        {t["id"] for t in top25} == set(vista["miembros"]),
                        f"difieren: {sorted({t['id'] for t in top25} ^ set(vista['miembros']))}")
            r.comprobar("el orden de la vista 1435 es el del ranking oficial",
                        [t["id"] for t in top25] == vista["miembros"],
                        "el orden de miembros de la vista ya no coincide con el ranking")

    # Índices
    ruta_i = ind / "indice.json"
    if ruta_i.is_file() and entradas:
        indice = json.loads(ruta_i.read_text(encoding="utf-8"))
        r.comprobar("índice cubre todas las entradas", set(indice) == conocidos,
                    f"faltan {len(conocidos - set(indice))}, sobran {len(set(indice) - conocidos)}")
        malos = []
        with open(ruta_jsonl, "rb") as fh:
            for cid in sorted(indice, key=L.numero)[:: max(1, len(indice) // 60)]:  # muestra ~60 repartidas
                fh.seek(indice[cid]["offset"])
                bloque = fh.read(indice[cid]["longitud"])
                try:
                    if json.loads(bloque)["id"] != cid:
                        malos.append(cid)
                except (json.JSONDecodeError, KeyError):
                    malos.append(cid)
        r.comprobar("desplazamientos del índice leen la entrada correcta", not malos, f"{malos[:3]}")
        inv = json.loads((ind / "invertido.json").read_text(encoding="utf-8"))
        r.comprobar("índice invertido solo apunta a entradas existentes",
                    all(i in conocidos for ids_ in inv.values() for i in ids_))
        jer = json.loads((ind / "jerarquia.json").read_text(encoding="utf-8"))
        r.comprobar("jerarquía solo contiene entradas existentes",
                    all(p in conocidos and all(h in conocidos for h in hs) for p, hs in jer["hijos"].items()))
    else:
        r.comprobar("existen los índices", False, "ejecuta `python scripts/cwe_kb.py indices`")
    return r


def _cita_id(ruta: Path, cid: str) -> bool:
    """¿El archivo de evidencia cita el identificador (como palabra completa: CWE-78 no es CWE-780)?"""
    try:
        return re.search(rf"(?<![\w-]){re.escape(cid)}(?!\d)", ruta.read_text(encoding="utf-8")) is not None
    except OSError:
        return False


def validar_mapa(base: L.BaseCWE, raiz: Path = L.RAIZ, mapa: dict | None = None) -> Resultado:
    """Comprueba el mapa curricular contra el catálogo y contra los archivos del repositorio."""
    r = Resultado()
    mapa = mapa if mapa is not None else cargar_mapa()
    entradas = mapa.get("entradas", {})
    r.comprobar("el mapa tiene el esquema esperado", mapa.get("esquema") == L.ESQUEMA)
    familias = set(mapa.get("familias", {}))
    for cid, d in sorted(entradas.items(), key=lambda kv: L.numero(kv[0])):
        if cid not in base:
            r.errores.append(f"{cid}: no existe en el catálogo")
            continue
        e = base.obtener(cid)
        if e["estado"] == "Deprecated":
            r.errores.append(f"{cid}: está obsoleto en el catálogo; sustituir por la entrada vigente")
        if d.get("familia") not in familias:
            r.errores.append(f"{cid}: familia desconocida {d.get('familia')!r}")
        if d.get("nivel") not in ("basico", "intermedio", "avanzado"):
            r.errores.append(f"{cid}: nivel inválido {d.get('nivel')!r}")
        for clave in ("teoria", "ejercicio"):
            for n in d.get(clave, []):
                dc = directorio_clase(n, raiz)
                if not dc:
                    r.errores.append(f"{cid}: {clave} cita la clase {n:03d}, que no existe")
                    continue
                if not _trata_tema(_texto_norm(dc / "README.md"), cid, d.get("palabras_clave", [])):
                    r.errores.append(f"{cid}: la clase {n:03d} declarada en «{clave}» no menciona el identificador ni ninguna palabra clave")
        for lab in d.get("laboratorio", []):
            if not (raiz / lab).is_dir():
                r.errores.append(f"{cid}: laboratorio inexistente {lab}")
        for p in d.get("prueba", []):
            ruta, _, nombre = p.partition("::")
            f = raiz / ruta
            if not f.is_file():
                r.errores.append(f"{cid}: archivo de prueba inexistente {ruta}")
            elif nombre and not re.search(rf"def\s+{re.escape(nombre)}\b", f.read_text(encoding="utf-8")):
                r.errores.append(f"{cid}: la prueba {nombre} no está definida en {ruta}")
        for ev in d.get("evaluacion", []):
            if not (raiz / ev).is_file():
                r.errores.append(f"{cid}: evidencia de evaluación inexistente {ev}")
            elif not _cita_id(raiz / ev, cid):
                r.errores.append(f"{cid}: la evidencia de evaluación {ev} no cita el identificador")
    r.comprobaciones.append(("mapa curricular verificado contra catálogo y archivos", not r.errores, f"{len(entradas)} entradas"))
    return r


# --------------------------------------------------------------------------
# Auditoría de referencias del temario
# --------------------------------------------------------------------------
@dataclass
class Hallazgo:
    gravedad: str     # 'error' | 'aviso'
    archivo: str
    linea: int
    mensaje: str


# El nombre oficial solo se contrasta en viñetas o filas de tabla de Markdown («- CWE-190: Integer Overflow…»),
# que es donde se escriben las listas de referencias. En un comentario de código o en prosa, lo que sigue a los
# dos puntos es una explicación en español, no un nombre, y compararlo daría falsos positivos.
NOMBRE_RE = re.compile(r"^\s*(?:[-*]|\|)\s*CWE-(\d{1,5})\s*:\s*([A-Za-z][^—–<>\[\]|`\n]{3,120}?)\s*(?:—|–|<|\(|\[|$)")
URL_RE = re.compile(r"cwe\.mitre\.org/data/definitions/(\d+)(?:\.html)?")
# «CWE-284, 285, 287 y 862»: el prefijo solo aparece en el primero y los demás van como números sueltos.
LISTA_CWE_RE = re.compile(r"CWE-(\d{1,5})((?:\s*(?:,|y|e|and)\s*\d{1,5}\b)*)", re.IGNORECASE)
EXPLICA_OBSOLETO_RE = re.compile(r"(obsole|deprecat|retirad|sustitu|reemplaz|supers)", re.IGNORECASE)


def ids_de_linea(texto: str) -> set[int]:
    """Todos los identificadores citados en una línea, incluidas las listas «CWE-284, 285 y 862»."""
    ids: set[int] = set()
    for m in LISTA_CWE_RE.finditer(texto):
        ids.add(int(m.group(1)))
        ids.update(int(n) for n in re.findall(r"\d{1,5}", m.group(2)))
    return ids


def _norm_nombre(s: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", L.sin_acentos(s)))


def auditar_referencias(base: L.BaseCWE, menciones: list[Mencion]) -> list[Hallazgo]:
    """Detecta referencias CWE inválidas, obsoletas o con nombre/URL incongruente.

    Un enlace a `definitions/79.html` junto a «CWE-89» o «CWE-89: Cross-site
    Scripting» son errores reales y silenciosos: nadie los nota al leer, pero
    llevan al estudiante a estudiar otra debilidad.
    """
    h: list[Hallazgo] = []
    for m in menciones:
        if m.cwe not in base:
            if str(L.numero(m.cwe)) in base.vistas:
                # Vistas y entradas comparten la numeración: «CWE-1435» no es una entrada sino la vista del Top 25.
                h.append(Hallazgo("aviso", m.archivo, m.linea,
                                  f"{m.cwe} es una VISTA, no una entrada del catálogo: escríbela como «vista {L.numero(m.cwe)}»"))
            else:
                h.append(Hallazgo("error", m.archivo, m.linea, f"{m.cwe} no existe en el catálogo CWE {_version(base)}"))
            continue
        e = base.obtener(m.cwe)
        if e["estado"] == "Deprecated":
            # Si la propia línea lo reconoce («está obsoleta, usa CWE-1462»), es una explicación, no un uso indebido.
            if not EXPLICA_OBSOLETO_RE.search(m.contexto or m.texto):
                h.append(Hallazgo("error", m.archivo, m.linea, f"{m.cwe} está obsoleto («{e['nombre']}»); usar la entrada vigente"))
        elif (e["notas_mapeo"].get("uso") == "Prohibited"
              and re.search(r"(mapea|clasific|asign|CWE principal)", m.contexto or m.texto, re.I)
              # Si el propio contexto ya advierte de la prohibición, es una explicación, no un uso indebido.
              and not re.search(r"(prohib|agrupaci|categor|grouping|desaconsej|discouraged|vista)", m.contexto or m.texto, re.I)):
            h.append(Hallazgo("aviso", m.archivo, m.linea,
                              f"{m.cwe} ({e['abstraccion'] or e['tipo']}) tiene uso de mapeo «Prohibited»: no debería usarse para clasificar una vulnerabilidad concreta"))
    # Texto de la misma línea: nombre y URL deben corresponder al identificador.
    vistos: set[tuple[str, int]] = set()
    for m in menciones:
        clave = (m.archivo, m.linea)
        if clave in vistos:
            continue
        vistos.add(clave)
        for mm in NOMBRE_RE.finditer(m.texto):
            cid = f"CWE-{int(mm.group(1))}"
            if cid not in base:
                continue
            oficial = _norm_nombre(base.obtener(cid)["nombre"])
            citado = _norm_nombre(mm.group(2))
            if citado and not (oficial.startswith(citado) or citado.startswith(oficial) or oficial in citado):
                h.append(Hallazgo("error", m.archivo, m.linea,
                                  f"{cid} se cita como «{mm.group(2).strip()}» pero su nombre oficial es «{base.obtener(cid)['nombre']}»"))
        ids_linea = ids_de_linea(m.texto)
        for um in URL_RE.finditer(m.texto):
            if ids_linea and int(um.group(1)) not in ids_linea:
                h.append(Hallazgo("error", m.archivo, m.linea,
                                  f"la URL apunta a CWE-{um.group(1)} pero el texto de la línea cita {sorted('CWE-%d' % i for i in ids_linea)}"))
    return h


def auditar_urls(base: L.BaseCWE, raiz: Path = L.RAIZ) -> list[Hallazgo]:
    """URLs de definitions/N.html en cualquier documento: que N exista y esté vigente (sin red)."""
    h: list[Hallazgo] = []
    for ruta, rel in iter_archivos(raiz):
        if ruta.suffix != ".md":
            continue
        try:
            texto = ruta.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for n, linea in enumerate(texto.splitlines(), 1):
            for um in URL_RE.finditer(linea):
                cid = f"CWE-{int(um.group(1))}"
                if cid not in base:
                    h.append(Hallazgo("error", rel, n, f"enlace a {cid}, que no existe en el catálogo"))
                elif base.obtener(cid)["estado"] == "Deprecated":
                    h.append(Hallazgo("error", rel, n, f"enlace a {cid}, obsoleto"))
    return h


def _version(base: L.BaseCWE) -> str:
    p = L.leer_procedencia()
    return p.get("catalogo", {}).get("version", "?")


# --------------------------------------------------------------------------
# Hallazgos de herramientas SAST -> CWE
# --------------------------------------------------------------------------
@dataclass
class HallazgoSAST:
    herramienta: str
    regla: str
    archivo: str
    linea: int
    severidad: str
    mensaje: str
    cwes: list[str]


def _cwes_de_texto(valor) -> list[str]:
    """Extrae identificadores de «CWE-89: Improper…», de una lista de ellos o de un entero."""
    if valor is None:
        return []
    if isinstance(valor, (int, float)):
        return [f"CWE-{int(valor)}"]
    if isinstance(valor, str):
        return sorted({f"CWE-{int(x)}" for x in CWE_ETIQUETA_RE.findall(valor)}, key=L.numero)
    if isinstance(valor, (list, tuple)):
        out: list[str] = []
        for v in valor:
            out += _cwes_de_texto(v)
        return sorted(set(out), key=L.numero)
    return []


def leer_hallazgos_sast(datos: dict) -> list[HallazgoSAST]:
    """Detecta el formato (Bandit, Semgrep o SARIF) y devuelve hallazgos uniformes."""
    salida: list[HallazgoSAST] = []
    if "runs" in datos and datos.get("version", "").startswith("2."):  # SARIF 2.x
        for run in datos["runs"]:
            herr = run.get("tool", {}).get("driver", {}).get("name", "sarif")
            reglas = {r.get("id"): r for r in run.get("tool", {}).get("driver", {}).get("rules", [])}
            for res in run.get("results", []):
                regla = reglas.get(res.get("ruleId"), {})
                etiquetas = regla.get("properties", {}).get("tags", [])
                cwes = _cwes_de_texto([etiquetas, regla.get("properties", {}).get("cwe"),
                                       regla.get("relationships", [])])
                loc = (res.get("locations") or [{}])[0].get("physicalLocation", {})
                salida.append(HallazgoSAST(
                    herr, str(res.get("ruleId", "")), loc.get("artifactLocation", {}).get("uri", ""),
                    int(loc.get("region", {}).get("startLine", 0)), str(res.get("level", "")),
                    res.get("message", {}).get("text", ""), cwes))
    elif "results" in datos and datos["results"] and "issue_cwe" in datos["results"][0]:  # Bandit
        for res in datos["results"]:
            salida.append(HallazgoSAST(
                "bandit", res.get("test_id", ""), res.get("filename", ""), int(res.get("line_number", 0)),
                str(res.get("issue_severity", "")).lower(), res.get("issue_text", ""),
                _cwes_de_texto(res.get("issue_cwe", {}).get("id"))))
    elif "results" in datos:  # Semgrep
        for res in datos["results"]:
            extra = res.get("extra", {})
            salida.append(HallazgoSAST(
                "semgrep", res.get("check_id", ""), res.get("path", ""), int(res.get("start", {}).get("line", 0)),
                str(extra.get("severity", "")).lower(), extra.get("message", ""),
                _cwes_de_texto(extra.get("metadata", {}).get("cwe"))))
    else:
        raise ValueError("Formato no reconocido: se esperaba JSON de Bandit, Semgrep o SARIF 2.x")
    return salida


def anotar_hallazgos(base: L.BaseCWE, hallazgos: list[HallazgoSAST]) -> list[dict]:
    """Cruza cada hallazgo con el catálogo y marca lo que exige criterio humano."""
    filas = []
    for hz in hallazgos:
        info = []
        avisos = []
        for cid in hz.cwes:
            if cid not in base:
                avisos.append(f"{cid} no existe en el catálogo")
                continue
            e = base.obtener(cid)
            info.append({"id": cid, "nombre": e["nombre"], "abstraccion": e["abstraccion"] or e["tipo"], "estado": e["estado"]})
            if e["estado"] == "Deprecated":
                avisos.append(f"{cid} obsoleto")
            if e["notas_mapeo"].get("uso") in ("Prohibited", "Discouraged"):
                avisos.append(f"{cid}: uso de mapeo {e['notas_mapeo']['uso']}")
        if not hz.cwes:
            avisos.append("la herramienta no declara CWE: clasificar a mano")
        elif len(hz.cwes) > 1:
            avisos.append("varias CWE: elegir la causa raíz (la más específica que describa el defecto)")
        filas.append({"herramienta": hz.herramienta, "regla": hz.regla, "archivo": hz.archivo, "linea": hz.linea,
                      "severidad": hz.severidad, "mensaje": hz.mensaje, "cwe": info, "avisos": avisos})
    return filas


def contrastar_con_mapa(filas: list[dict], mapa_lab: dict, raiz: Path = L.RAIZ) -> list[dict]:
    """Añade a cada hallazgo el CWE que recomienda el mapa de un laboratorio, si encuentra el defecto.

    La herramienta SAST propone un CWE; el mapa del laboratorio recoge el que se considera
    correcto tras analizar la causa raíz. Cuando difieren se anota `contraste`, que es justo
    el ejercicio que el laboratorio quiere provocar: no copiar la etiqueta de la herramienta.
    """
    cache: dict[str, list[str]] = {}

    def lineas_de(archivo: str) -> list[str]:
        ruta = (raiz / archivo.replace("\\", "/")).resolve()
        clave = str(ruta)
        if clave not in cache:
            try:
                cache[clave] = ruta.read_text(encoding="utf-8").splitlines()
            except OSError:
                cache[clave] = []
        return cache[clave]

    for f in filas:
        texto = lineas_de(f["archivo"])
        linea = texto[f["linea"] - 1] if 0 < f["linea"] <= len(texto) else ""
        defecto = next((v for v in mapa_lab.get("vulnerabilidades", []) if v["marcador"] in linea), None)
        f["contraste"] = None
        if not defecto:
            continue
        reportados = [c["id"] for c in f["cwe"]]
        principal = defecto["cwe_principal"]
        alternativas = {a["id"]: a["motivo"] for a in defecto.get("cwe_alternativas", [])}
        if principal in reportados:
            f["contraste"] = {"vulnerabilidad": defecto["titulo"], "estado": "coincide", "recomendado": principal, "motivo": ""}
        elif any(r in alternativas for r in reportados):
            motivo = next(alternativas[r] for r in reportados if r in alternativas)
            f["contraste"] = {"vulnerabilidad": defecto["titulo"], "estado": "valido_pero_no_el_mas_especifico",
                              "recomendado": principal, "motivo": motivo}
        else:
            f["contraste"] = {"vulnerabilidad": defecto["titulo"], "estado": "difiere", "recomendado": principal,
                              "motivo": defecto.get("bandit", {}).get("nota", "")}
    return filas


# --------------------------------------------------------------------------
# Cobertura
# --------------------------------------------------------------------------
def cobertura(base: L.BaseCWE, raiz: Path = L.RAIZ, mapa: dict | None = None,
              menciones: list[Mencion] | None = None) -> list[dict]:
    """Calcula el nivel de cobertura de cada CWE objetivo (Top 25 vigente + mapa curricular)."""
    mapa = mapa if mapa is not None else cargar_mapa()
    menciones = menciones if menciones is not None else escanear_menciones(raiz)
    por_cwe: dict[str, list[Mencion]] = {}
    for m in menciones:
        por_cwe.setdefault(m.cwe, []).append(m)

    top = {e["id"] for e in base.miembros_de_vista(TOP25_VISTA)} if TOP25_VISTA in base.vistas else set()
    objetivo = set(mapa.get("entradas", {})) | top
    filas = []
    for cid in sorted(objetivo, key=L.numero):
        d = mapa.get("entradas", {}).get(cid, {})
        e = base.entradas.get(cid)
        problemas: list[str] = []
        claves = d.get("palabras_clave", [])

        def clases_validas(clave: str) -> list[int]:
            ok = []
            for n in d.get(clave, []):
                dc = directorio_clase(n, raiz)
                if dc and _trata_tema(_texto_norm(dc / "README.md"), cid, claves):
                    ok.append(n)
                else:
                    problemas.append(f"{clave}: clase {n:03d} no verificable")
            return ok

        teoria = clases_validas("teoria")
        ejercicio = clases_validas("ejercicio")
        labs = [lab for lab in d.get("laboratorio", []) if (raiz / lab).is_dir()]
        for lab in d.get("laboratorio", []):
            if lab not in labs:
                problemas.append(f"laboratorio {lab} inexistente")
        pruebas = []
        for p in d.get("prueba", []):
            ruta, _, nombre = p.partition("::")
            f = raiz / ruta
            if f.is_file() and (not nombre or re.search(rf"def\s+{re.escape(nombre)}\b", f.read_text(encoding="utf-8"))):
                pruebas.append(p)
            else:
                problemas.append(f"prueba {p} no encontrada")
        evals = [ev for ev in d.get("evaluacion", []) if (raiz / ev).is_file() and _cita_id(raiz / ev, cid)]
        for ev in d.get("evaluacion", []):
            if ev not in evals:
                problemas.append(f"evaluación {ev} inexistente o sin citar {cid}")

        nivel = "pendiente"
        if cid in por_cwe:
            nivel = "mencionado"
        if teoria:
            nivel = "explicado"
        if ejercicio:
            nivel = "ejercicio"
        if labs:
            nivel = "laboratorio"
        if labs and pruebas and d.get("correccion"):
            nivel = "correccion_prueba"

        mitigacion = d.get("mitigacion", "")
        practica = bool(ejercicio or labs)
        verificacion = bool(pruebas or evals)
        if teoria and practica and mitigacion and verificacion:
            estado = "Completo"
        elif teoria or practica:
            estado = "Parcial"
        else:
            estado = "Pendiente"

        todas_clases = sorted(set(teoria) | set(ejercicio))
        partes = sorted({parte_de_clase(n, raiz) for n in todas_clases}, key=lambda x: int(x or 0))
        filas.append({
            "id": cid,
            "nombre": e["nombre"] if e else "(no existe en el catálogo)",
            "abstraccion": (e["abstraccion"] or e["tipo"]) if e else "",
            "familia": d.get("familia", ""),
            "nivel": d.get("nivel", ""),
            "top25": cid in top,
            "menciones": len(por_cwe.get(cid, [])),
            "archivos_mencion": sorted({m.archivo for m in por_cwe.get(cid, [])}),
            "teoria": teoria, "ejercicio": ejercicio, "laboratorio": labs, "prueba": pruebas, "evaluacion": evals,
            "correccion": d.get("correccion", ""), "mitigacion": mitigacion,
            "partes": partes, "nivel_cobertura": nivel, "estado": estado, "problemas": problemas,
        })
    return filas


TOP25_VISTA = "1435"


def cwe_mencionados_fuera_de_objetivo(base: L.BaseCWE, filas: list[dict], menciones: list[Mencion]) -> dict[str, int]:
    objetivo = {f["id"] for f in filas}
    cuenta: dict[str, int] = {}
    for m in menciones:
        if m.cwe not in objetivo:
            cuenta[m.cwe] = cuenta.get(m.cwe, 0) + 1
    return dict(sorted(cuenta.items(), key=lambda kv: L.numero(kv[0])))


def clases_sin_cwe(partes: tuple[int, ...], menciones: list[Mencion], raiz: Path = L.RAIZ) -> list[str]:
    """Clases de las partes dadas cuyo README no cita ningún CWE (huecos de integración)."""
    con = {clase_de_ruta(m.archivo) for m in menciones if clase_de_ruta(m.archivo)}
    huecos = []
    for p in sorted((raiz / "classes").glob("parte-*")):
        mm = re.match(r"parte-(\d+)-", p.name)
        if not mm or int(mm.group(1)) not in partes:
            continue
        for c in sorted(p.glob("[0-9][0-9][0-9]-*")):
            n = int(c.name[:3])
            if n not in con:
                huecos.append(f"{n:03d} {c.name[4:]}")
    return huecos


# --------------------------------------------------------------------------
# Matriz de cobertura en Markdown (reproducible: sin fechas ni rutas absolutas)
# --------------------------------------------------------------------------
ETIQUETA_NIVEL = {
    "pendiente": "—", "mencionado": "mencionado", "explicado": "explicado",
    "ejercicio": "con ejercicio", "laboratorio": "con laboratorio", "correccion_prueba": "con corrección y prueba",
}
NOMBRE_NIVEL = {"basico": "Básico", "intermedio": "Intermedio", "avanzado": "Avanzado", "": "—"}


def _enlaces_clases(nums: list[int], raiz: Path) -> str:
    out = []
    for n in nums:
        dc = directorio_clase(n, raiz)
        if dc:
            rel = dc.relative_to(raiz).as_posix()
            out.append(f"[{n:03d}](../{rel}/README.md)")
        else:
            out.append(f"{n:03d}")
    return ", ".join(out) or "—"


def render_matriz(base: L.BaseCWE, filas: list[dict], fuera: dict[str, int], huecos: list[str], raiz: Path = L.RAIZ) -> str:
    proc = L.leer_procedencia()
    cat = proc.get("catalogo", {})
    n = len(filas)
    resumen = {est: sum(1 for f in filas if f["estado"] == est) for est in ("Completo", "Parcial", "Pendiente")}
    niveles = {nv: sum(1 for f in filas if f["nivel_cobertura"] == nv) for nv in NIVELES_COBERTURA}

    L_ = []
    a = L_.append
    a("# Matriz de cobertura CWE")
    a("")
    a("> **Archivo generado.** No se edita a mano: se regenera con `python scripts/cwe_kb.py cobertura --escribir`.")
    a("> La fuente de verdad es [`knowledge/cwe/pedagogico/mapa-curricular.json`](../knowledge/cwe/pedagogico/mapa-curricular.json)")
    a("> más los archivos reales del repositorio; cada declaración se verifica contra ellos en cada ejecución.")
    a("")
    a(f"Catálogo de referencia: **CWE {cat.get('version', '?')}** (publicado el {cat.get('fecha', '?')}). "
      f"Objetivo de la matriz: las **25 debilidades del CWE Top 25 de 2025** (vista 1435) más las familias que el programa se comprometió a cubrir.")
    a("")
    a("## Qué significa cada nivel")
    a("")
    a("Que el identificador «CWE-89» aparezca en un archivo **no** cuenta como cobertura. Los niveles son acumulativos y los tres últimos exigen un archivo que exista y que trate el tema.")
    a("")
    a("| Nivel | Qué prueba |")
    a("|---|---|")
    a("| mencionado | El identificador aparece en algún documento. No se afirma que se enseñe. |")
    a("| explicado | Una clase declarada desarrolla la debilidad (causa, mecanismo, consecuencia). |")
    a("| con ejercicio | Una clase declarada la practica con un ejercicio, laboratorio guiado o reto. |")
    a("| con laboratorio | Un laboratorio ejecutable la reproduce en un entorno local. |")
    a("| con corrección y prueba | El laboratorio incluye la corrección y una prueba automática que la verifica. |")
    a("")
    a("**Estado.** *Completo*: explicado + práctica + mitigación enseñada + verificación (prueba o evaluación). "
      "*Parcial*: tiene teoría o práctica pero le falta alguna otra pieza. *Pendiente*: como mucho se menciona.")
    a("")
    a("## Resumen")
    a("")
    a(f"- CWE objetivo: **{n}** — Completo **{resumen['Completo']}**, Parcial **{resumen['Parcial']}**, Pendiente **{resumen['Pendiente']}**.")
    a("- Por nivel más alto alcanzado: " + ", ".join(f"{ETIQUETA_NIVEL[k] if k != 'pendiente' else 'sin mención'} {v}" for k, v in niveles.items()) + ".")
    a("")
    a("## Matriz")
    a("")
    a("| CWE ID | Nombre | Top 25 2025 | Parte | Clase | Nivel | Teoría | Práctica | Laboratorio | Mitigación | Evaluación | Cobertura | Estado |")
    a("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for f in sorted(filas, key=lambda x: (x["familia"], L.numero(x["id"]))):
        practica = _enlaces_clases(f["ejercicio"], raiz)
        lab = ", ".join(f"[`{p.split('/')[-1]}`](../{p}/README.md)" for p in f["laboratorio"]) or "—"
        ev = ", ".join(f"[{p.split('/')[-1]}](../{p})" for p in f["evaluacion"]) or "—"
        if f["prueba"] and not f["evaluacion"]:
            ev = "prueba automática"
        elif f["prueba"]:
            ev += " + prueba automática"
        a("| " + " | ".join([
            f"[{f['id']}](https://cwe.mitre.org/data/definitions/{L.numero(f['id'])}.html)",
            f["nombre"].replace("|", "\\|"),
            "sí" if f["top25"] else "no",
            ", ".join(f["partes"]) or "—",
            _enlaces_clases(sorted(set(f["teoria"]) | set(f["ejercicio"])), raiz),
            NOMBRE_NIVEL.get(f["nivel"], "—"),
            "sí" if f["teoria"] else "no",
            practica if f["ejercicio"] else ("sí (lab)" if f["laboratorio"] else "no"),
            lab,
            (f["mitigacion"] or "—").replace("|", "\\|"),
            ev,
            ETIQUETA_NIVEL[f["nivel_cobertura"]] if f["nivel_cobertura"] != "pendiente" else "sin mención",
            f["estado"],
        ]) + " |")
    a("")
    problemas = [(f["id"], p) for f in filas for p in f["problemas"]]
    a("## Declaraciones que no se pudieron verificar")
    a("")
    if problemas:
        for cid, p in problemas:
            a(f"- {cid}: {p}")
    else:
        a("Ninguna: todo lo declarado en el mapa curricular existe y trata el tema.")
    a("")
    a("## CWE citados en el temario fuera de la matriz")
    a("")
    if fuera:
        a("Aparecen como **mencionados** (no se afirma que se enseñen). Si alguno debe cubrirse, se añade al mapa curricular.")
        a("")
        a("| CWE | Nombre | Apariciones |")
        a("|---|---|---|")
        for cid, c in fuera.items():
            nombre = base.entradas[cid]["nombre"].replace("|", "\\|") if cid in base else "(no existe en el catálogo)"
            a(f"| {cid} | {nombre} | {c} |")
    else:
        a("Ninguno.")
    a("")
    a("## Clases de las partes de desarrollo seguro y explotación que no citan ningún CWE")
    a("")
    if huecos:
        a("Son huecos de integración: el tema probablemente se enseña, pero sin vincularlo a su debilidad.")
        a("")
        for h in huecos:
            a(f"- {h}")
    else:
        a("Ninguna.")
    a("")
    a("## Cómo actualizar esta matriz")
    a("")
    a("1. Si cambió el catálogo de MITRE: `python scripts/cwe_kb.py importar --descargar` (una vez, con red).")
    a("2. Si cambió el temario: editar `knowledge/cwe/pedagogico/mapa-curricular.json` (declarar qué clase explica, practica o prueba cada CWE).")
    a("3. `python scripts/cwe_kb.py validar` — comprueba datos, mapa y referencias.")
    a("4. `python scripts/cwe_kb.py cobertura --escribir` — regenera este archivo; con `--check` falla si está desactualizado (lo usa el CI).")
    a("")
    return "\n".join(L_) + "\n"


def exportar_csv(entradas: list[dict]) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["id", "tipo", "abstraccion", "estado", "nombre", "padres_vista_1000", "vistas"])
    for e in entradas:
        padres = [r["id"] for r in e.get("relaciones", []) if r["vista"] == L.VISTA_JERARQUIA and r["naturaleza"] == "ChildOf"]
        w.writerow([e["id"], e["tipo"], e["abstraccion"], e["estado"], e["nombre"], " ".join(padres), " ".join(e.get("vistas", []))])
    return buf.getvalue()
