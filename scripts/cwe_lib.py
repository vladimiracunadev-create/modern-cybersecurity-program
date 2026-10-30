# -*- coding: utf-8 -*-
"""Núcleo de la base de conocimiento local de MITRE CWE.

Este módulo hace tres cosas, y las separa a propósito porque cada una cambia
por motivos distintos:

  1. IMPORTAR: lee el catálogo oficial (XML dentro de un ZIP), lo valida y lo
     convierte a JSON Lines. Es la única parte que toca el formato de MITRE.
  2. INDEXAR: construye tablas pequeñas (índice por identificador, índice
     invertido por palabra, jerarquía) para consultar sin cargar todo el
     catálogo en memoria ni releerlo entero.
  3. CONSULTAR: carga lo normalizado y responde preguntas (una ficha, una
     búsqueda, los padres de una debilidad). No sabe nada del XML.

Capas de datos bajo `knowledge/cwe/` (ninguna se mezcla con otra):

  original/      ZIP descargado. NO se versiona (pesa ~2 MB comprimido, ~19 MB
                 descomprimido); se recupera con `cwe_kb.py importar --descargar`
                 y su SHA-256 queda registrado en PROCEDENCIA.json.
  normalizado/   cwe.jsonl, vistas.json, referencias.json: el catálogo con
                 nombres de campo en español pero texto de MITRE sin reescribir.
  pedagogico/    mapa-curricular.json: lo que ESTE programa enseña de cada CWE.
                 Es contenido propio, no de MITRE, y vive aparte para que una
                 actualización del catálogo nunca pise decisiones didácticas.
  indices/       Derivados reproducibles de normalizado/. Se pueden borrar y
                 regenerar; existen para consultar rápido y para que un agente
                 o un sistema RAG pueda leer una entrada sin cargar el resto.
  PROCEDENCIA.json  Origen, versión, huellas y fechas. Es lo que permite
                 saber de dónde salió cada dato y detectar manipulación.

Solo biblioteca estándar: el programa básico no exige claves ni dependencias.
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
KB = RAIZ / "knowledge" / "cwe"
ORIGINAL = KB / "original"
NORMALIZADO = KB / "normalizado"
PEDAGOGICO = KB / "pedagogico"
INDICES = KB / "indices"
PROCEDENCIA = KB / "PROCEDENCIA.json"

URL_CATALOGO = "https://cwe.mitre.org/data/xml/cwec_latest.xml.zip"
URL_TERMINOS = "https://cwe.mitre.org/about/termsofuse.html"
URL_TOP25 = "https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html"
TOP25_JSON = NORMALIZADO / "top25-2025.json"
NS = "{http://cwe.mitre.org/cwe-8}"

# Versión del formato que ESTE repositorio escribe (no la de MITRE). Si cambia
# el esquema de salida hay que subirla: `validar` rechaza datos de otra versión
# en vez de interpretarlos mal.
ESQUEMA = 1

# Vista de MITRE que representa la jerarquía «Research Concepts»: la única que
# cubre todo el catálogo con una relación ChildOf por entrada. Para enseñar
# padres e hijos usamos esta, y la consulta indica de qué vista procede cada
# relación porque otras vistas (p. ej. 699, desarrollo de software) difieren.
VISTA_JERARQUIA = "1000"

# Límites defensivos al leer datos descargados: el ZIP y el XML son entrada no
# confiable hasta que se validan, así que no se descomprime sin tope.
MAX_ZIP = 50 * 1024 * 1024
MAX_XML = 120 * 1024 * 1024

ID_RE = re.compile(r"^(?:CWE)?[-_ ]?(\d{1,5})$", re.IGNORECASE)


# --------------------------------------------------------------------------
# Identificadores y texto
# --------------------------------------------------------------------------
def normalizar_id(valor: str | int) -> str:
    """Devuelve 'CWE-89' para 89, '89', 'cwe89' o 'CWE-89'. ValueError si no es un CWE."""
    m = ID_RE.match(str(valor).strip())
    if not m:
        raise ValueError(f"Identificador CWE no válido: {valor!r}")
    return f"CWE-{int(m.group(1))}"


def numero(cwe_id: str) -> int:
    return int(cwe_id.split("-", 1)[1])


def sin_acentos(texto: str) -> str:
    """Minúsculas y sin diacríticos: así «Inyección» y «inyeccion» se encuentran."""
    base = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in base if not unicodedata.combining(c)).lower()


def tokens(texto: str) -> list[str]:
    """Palabras de búsqueda: alfanuméricas, de 3 o más caracteres, sin acentos."""
    return [t for t in re.findall(r"[a-z0-9]+", sin_acentos(texto)) if len(t) >= 3]


_BLOQUES = {"p", "li", "br", "div", "ul", "ol", "table", "tr", "pre"}


def texto_plano(elem: ET.Element | None) -> str:
    """Aplana el XHTML incrustado en las descripciones de MITRE a texto con párrafos.

    Las descripciones llevan etiquetas como <xhtml:p> o <xhtml:li>. Para
    estudiar o buscar nos basta el texto; conservamos solo los saltos de
    línea entre bloques para no pegar párrafos distintos en una sola frase.
    """
    if elem is None:
        return ""
    partes: list[str] = []

    def visitar(e: ET.Element) -> None:
        etiqueta = e.tag.rsplit("}", 1)[-1]
        if etiqueta in _BLOQUES:
            partes.append("\n")
        if e.text:
            partes.append(e.text)
        for hijo in e:
            visitar(hijo)
            if hijo.tail:
                partes.append(hijo.tail)

    visitar(elem)
    lineas = (re.sub(r"[ \t\r\f\v]+", " ", ln).strip() for ln in "".join(partes).split("\n"))
    return "\n".join(ln for ln in lineas if ln)


def _t(padre: ET.Element, etiqueta: str) -> str:
    return texto_plano(padre.find(NS + etiqueta))


def _lista(padre: ET.Element | None, etiqueta: str) -> list[str]:
    if padre is None:
        return []
    return [texto_plano(e) for e in padre.findall(NS + etiqueta) if texto_plano(e)]


def _cwe_ref(valor: str | None) -> str | None:
    """Los atributos CWE_ID del XML son números sueltos; los pasamos a 'CWE-n'."""
    if valor is None or not valor.isdigit():
        return None
    return f"CWE-{int(valor)}"


def huella(objeto: object) -> str:
    """SHA-256 del JSON canónico: sirve para detectar qué entradas cambiaron entre versiones."""
    return hashlib.sha256(serializar(objeto).encode("utf-8")).hexdigest()


def serializar(objeto: object) -> str:
    return json.dumps(objeto, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_archivo(ruta: Path) -> str:
    """SHA-256 de un archivo binario (el ZIP descargado): bytes tal cual."""
    h = hashlib.sha256()
    with open(ruta, "rb") as fh:
        for bloque in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def sha256_texto(ruta: Path) -> str:
    """SHA-256 de un archivo de texto ignorando el fin de línea.

    Git con `core.autocrlf=true` (el valor por defecto en Windows) convierte LF
    en CRLF al extraer. Si el hash dependiera de eso, la misma base de datos
    «fallaría» su verificación según el sistema operativo. Se normaliza a LF.
    """
    return hashlib.sha256(ruta.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


# --------------------------------------------------------------------------
# 1. Importar
# --------------------------------------------------------------------------
def descargar(url: str, destino: Path, timeout: int = 120) -> str:
    """Descarga `url` a `destino` y devuelve su SHA-256. Sin credenciales ni cookies."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    peticion = urllib.request.Request(url, headers={"User-Agent": "modern-cybersecurity-program/cwe-kb"})
    try:
        with urllib.request.urlopen(peticion, timeout=timeout) as resp, open(destino, "wb") as out:
            total = 0
            while True:
                bloque = resp.read(1 << 20)
                if not bloque:
                    break
                total += len(bloque)
                if total > MAX_ZIP:
                    raise ValueError(f"La descarga supera el límite de {MAX_ZIP} bytes")
                out.write(bloque)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        destino.unlink(missing_ok=True)
        raise RuntimeError(f"No se pudo descargar {url}: {exc}") from exc
    return sha256_archivo(destino)


def leer_xml_de_zip(ruta_zip: Path) -> tuple[str, bytes]:
    """Extrae en memoria el único XML del ZIP (nunca a disco ni con rutas del archivo)."""
    with zipfile.ZipFile(ruta_zip) as z:
        xmls = [i for i in z.infolist() if i.filename.lower().endswith(".xml") and not i.is_dir()]
        if len(xmls) != 1:
            raise ValueError(f"Se esperaba 1 XML en el ZIP y hay {len(xmls)}")
        info = xmls[0]
        if info.file_size > MAX_XML:
            raise ValueError(f"El XML descomprimido ({info.file_size} B) supera el límite {MAX_XML}")
        return Path(info.filename).name, z.read(info)


def parsear_xml(datos: bytes) -> ET.Element:
    """Parsea el XML rechazando DTD y entidades.

    ElementTree no resuelve entidades externas, pero sí expande las internas, y
    una definición recursiva puede agotar la memoria («billion laughs»). El
    catálogo oficial no usa DTD, así que basta con negarse a procesar uno.
    """
    cabecera = datos[:4096].lower()
    if b"<!doctype" in cabecera or b"<!entity" in cabecera:
        raise ValueError("El XML declara DTD/entidades; se rechaza por seguridad")
    return ET.fromstring(datos)


def _historial(e: ET.Element) -> dict:
    hist = e.find(NS + "Content_History")
    salida: dict = {}
    if hist is None:
        return salida
    envio = hist.find(NS + "Submission")
    if envio is not None:
        salida["envio_fecha"] = _t(envio, "Submission_Date")
    mods = hist.findall(NS + "Modification")
    if mods:
        ultima = mods[-1]
        salida["modificado_fecha"] = _t(ultima, "Modification_Date")
        salida["modificado_version"] = _t(ultima, "Modification_Version")
    return salida


def _notas_mapeo(e: ET.Element) -> dict:
    nm = e.find(NS + "Mapping_Notes")
    if nm is None:
        return {}
    return {
        "uso": _t(nm, "Usage"),
        "razon": _t(nm, "Rationale"),
        "comentarios": _t(nm, "Comments"),
    }


def _relaciones(e: ET.Element) -> list[dict]:
    rel = e.find(NS + "Related_Weaknesses")
    salida = []
    if rel is not None:
        for r in rel.findall(NS + "Related_Weakness"):
            destino = _cwe_ref(r.get("CWE_ID"))
            if destino:
                salida.append(
                    {
                        "naturaleza": r.get("Nature", ""),
                        "id": destino,
                        "vista": r.get("View_ID", ""),
                        "orden": r.get("Ordinal", ""),
                    }
                )
    salida.sort(key=lambda x: (x["vista"], x["naturaleza"], numero(x["id"]), x["orden"]))
    return salida


def _ordinalidad(w: ET.Element) -> list[str]:
    """Primary (causa raíz en sí misma), Resultant (efecto de otra) o Indirect."""
    cont = w.find(NS + "Weakness_Ordinalities")
    if cont is None:
        return []
    return [o for o in (_t(x, "Ordinality") for x in cont.findall(NS + "Weakness_Ordinality")) if o]


def normalizar_debilidad(w: ET.Element) -> dict:
    """Convierte un <Weakness> en un registro plano. El texto de MITRE no se reescribe."""
    consecuencias = []
    cc = w.find(NS + "Common_Consequences")
    if cc is not None:
        for c in cc.findall(NS + "Consequence"):
            consecuencias.append(
                {
                    "ambitos": _lista(c, "Scope"),
                    "impactos": _lista(c, "Impact"),
                    "probabilidad": _t(c, "Likelihood"),
                    "nota": _t(c, "Note"),
                }
            )

    mitigaciones = []
    pm = w.find(NS + "Potential_Mitigations")
    if pm is not None:
        for m in pm.findall(NS + "Mitigation"):
            mitigaciones.append(
                {
                    "id": m.get("Mitigation_ID", ""),
                    "fases": _lista(m, "Phase"),
                    "estrategia": _t(m, "Strategy"),
                    "descripcion": _t(m, "Description"),
                    "efectividad": _t(m, "Effectiveness"),
                    "efectividad_notas": _t(m, "Effectiveness_Notes"),
                }
            )

    deteccion = []
    dm = w.find(NS + "Detection_Methods")
    if dm is not None:
        for d in dm.findall(NS + "Detection_Method"):
            deteccion.append(
                {
                    "metodo": _t(d, "Method"),
                    "descripcion": _t(d, "Description"),
                    "efectividad": _t(d, "Effectiveness"),
                    "efectividad_notas": _t(d, "Effectiveness_Notes"),
                }
            )

    introduccion = []
    mi = w.find(NS + "Modes_Of_Introduction")
    if mi is not None:
        for i in mi.findall(NS + "Introduction"):
            introduccion.append({"fase": _t(i, "Phase"), "nota": _t(i, "Note")})

    plataformas = []
    ap = w.find(NS + "Applicable_Platforms")
    if ap is not None:
        for p in ap:
            tipo = p.tag.rsplit("}", 1)[-1]
            plataformas.append(
                {
                    "tipo": tipo,
                    "clase": p.get("Class", ""),
                    "nombre": p.get("Name", ""),
                    "prevalencia": p.get("Prevalence", ""),
                }
            )

    ejemplos = []
    oe = w.find(NS + "Observed_Examples")
    if oe is not None:
        for o in oe.findall(NS + "Observed_Example"):
            ejemplos.append({"referencia": _t(o, "Reference"), "descripcion": _t(o, "Description")})

    taxonomias = []
    tm = w.find(NS + "Taxonomy_Mappings")
    if tm is not None:
        for t in tm.findall(NS + "Taxonomy_Mapping"):
            taxonomias.append(
                {
                    "taxonomia": t.get("Taxonomy_Name", ""),
                    "id": _t(t, "Entry_ID"),
                    "nombre": _t(t, "Entry_Name"),
                    "ajuste": _t(t, "Mapping_Fit"),
                }
            )

    capec = []
    ra = w.find(NS + "Related_Attack_Patterns")
    if ra is not None:
        capec = sorted(f"CAPEC-{p.get('CAPEC_ID')}" for p in ra.findall(NS + "Related_Attack_Pattern") if p.get("CAPEC_ID"))

    alternos = []
    at = w.find(NS + "Alternate_Terms")
    if at is not None:
        for a in at.findall(NS + "Alternate_Term"):
            alternos.append({"termino": _t(a, "Term"), "rol": _t(a, "Role")})

    referencias = []
    refs = w.find(NS + "References")
    if refs is not None:
        referencias = sorted(r.get("External_Reference_ID", "") for r in refs.findall(NS + "Reference") if r.get("External_Reference_ID"))

    registro = {
        "id": f"CWE-{int(w.get('ID'))}",
        "tipo": "weakness",
        "nombre": w.get("Name", ""),
        "abstraccion": w.get("Abstraction", ""),
        "estructura": w.get("Structure", ""),
        "estado": w.get("Status", ""),
        "descripcion": _t(w, "Description"),
        "descripcion_extendida": _t(w, "Extended_Description"),
        "contexto": _lista(w.find(NS + "Background_Details"), "Background_Detail"),
        "relaciones": _relaciones(w),
        "ordinalidad": _ordinalidad(w),
        "alternos": alternos,
        "introduccion": introduccion,
        "plataformas": plataformas,
        "consecuencias": consecuencias,
        "probabilidad_explotacion": _t(w, "Likelihood_Of_Exploit"),
        "deteccion": deteccion,
        "mitigaciones": mitigaciones,
        "ejemplos_observados": ejemplos,
        "taxonomias": taxonomias,
        "capec": capec,
        "areas_funcionales": _lista(w.find(NS + "Functional_Areas"), "Functional_Area"),
        "recursos_afectados": _lista(w.find(NS + "Affected_Resources"), "Affected_Resource"),
        "notas_mapeo": _notas_mapeo(w),
        "referencias": referencias,
    }
    registro.update(_historial(w))
    return registro


def normalizar_agrupacion(g: ET.Element) -> dict:
    """<Grouping> (antes <Category>): agrupa entradas por un criterio, no es una debilidad."""
    miembros = []
    rel = g.find(NS + "Relationships")
    if rel is not None:
        for r in rel:
            destino = _cwe_ref(r.get("CWE_ID"))
            if destino:
                miembros.append(
                    {"naturaleza": r.tag.rsplit("}", 1)[-1], "id": destino, "vista": r.get("View_ID", "")}
                )
    miembros.sort(key=lambda x: (x["vista"], x["naturaleza"], numero(x["id"])))
    registro = {
        "id": f"CWE-{int(g.get('ID'))}",
        "tipo": "grouping",
        "nombre": g.get("Name", ""),
        "abstraccion": "",
        "estructura": "",
        "estado": g.get("Status", ""),
        "descripcion": _t(g, "Summary"),
        "relaciones": miembros,
        "taxonomias": [],
        "notas_mapeo": _notas_mapeo(g),
    }
    registro.update(_historial(g))
    return registro


def normalizar_vista(v: ET.Element) -> dict:
    miembros = []
    mm = v.find(NS + "Members")
    if mm is not None:
        miembros = [m for m in (_cwe_ref(h.get("CWE_ID")) for h in mm.findall(NS + "Has_Member")) if m]
    filtro = v.find(NS + "Filter")
    registro = {
        "id": v.get("ID", ""),
        "nombre": v.get("Name", ""),
        "tipo": v.get("Type", ""),
        "estado": v.get("Status", ""),
        "objetivo": _t(v, "Objective"),
        "miembros": miembros,
        "filtro": (filtro.text or "").strip() if filtro is not None else "",
    }
    registro.update(_historial(v))
    return registro


def normalizar_referencias(root: ET.Element) -> dict[str, dict]:
    salida: dict[str, dict] = {}
    ext = root.find(NS + "External_References")
    if ext is None:
        return salida
    for r in ext.findall(NS + "External_Reference"):
        rid = r.get("Reference_ID", "")
        if not rid:
            continue
        salida[rid] = {
            "titulo": _t(r, "Title"),
            "autores": _lista(r, "Author"),
            "url": _t(r, "URL"),
            "fecha_publicacion": "-".join(
                p for p in (_t(r, "Publication_Year"), _t(r, "Publication_Month"), _t(r, "Publication_Day")) if p
            ),
            "editorial": _t(r, "Publisher"),
        }
    return dict(sorted(salida.items()))


def normalizar_catalogo(root: ET.Element) -> dict:
    """Devuelve {'entradas', 'vistas', 'referencias', 'meta'} a partir de la raíz del XML."""
    entradas: list[dict] = []
    deb = root.find(NS + "Weaknesses")
    if deb is not None:
        entradas += [normalizar_debilidad(w) for w in deb.findall(NS + "Weakness")]
    agr = root.find(NS + "Groupings")
    if agr is not None:
        entradas += [normalizar_agrupacion(g) for g in agr.findall(NS + "Grouping")]
    entradas.sort(key=lambda e: numero(e["id"]))

    vistas_el = root.find(NS + "Views")
    vistas = [normalizar_vista(v) for v in vistas_el.findall(NS + "View")] if vistas_el is not None else []
    vistas.sort(key=lambda v: int(v["id"]))

    miembro_de: dict[str, list[str]] = {}
    for v in vistas:
        for m in v["miembros"]:
            miembro_de.setdefault(m, []).append(v["id"])
    for e in entradas:
        e["vistas"] = sorted(miembro_de.get(e["id"], []), key=int)

    return {
        "entradas": entradas,
        "vistas": vistas,
        "referencias": normalizar_referencias(root),
        "meta": {"catalogo_version": root.get("Version", ""), "catalogo_fecha": root.get("Date", "")},
    }


# --------------------------------------------------------------------------
# 2. Escribir capas e índices
# --------------------------------------------------------------------------
def _escribir(ruta: Path, texto: str) -> None:
    """Escribe en UTF-8 con LF en todas las plataformas: los hashes deben coincidir en Windows y Linux."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)


def escribir_normalizado(datos: dict) -> dict[str, str]:
    """Escribe la capa normalizada y devuelve {archivo: sha256}."""
    lineas = [serializar(e) for e in datos["entradas"]]
    _escribir(NORMALIZADO / "cwe.jsonl", "\n".join(lineas) + "\n")
    _escribir(NORMALIZADO / "vistas.json", json.dumps(datos["vistas"], ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    _escribir(NORMALIZADO / "referencias.json", json.dumps(datos["referencias"], ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    return {f"normalizado/{n}": sha256_texto(NORMALIZADO / n) for n in ("cwe.jsonl", "vistas.json", "referencias.json")}


def construir_indices(entradas: list[dict], jsonl: Path | None = None) -> dict[str, str]:
    """Genera los índices a partir de las entradas. Devuelve {archivo: sha256}.

    - indice.json     id -> metadatos mínimos + posición (offset, longitud) en
                      cwe.jsonl, para leer UNA entrada sin cargar las demás.
    - invertido.json  palabra -> ids, sobre nombre, términos alternos e id.
    - jerarquia.json  padre -> hijos según la vista 1000 (ChildOf), y raíces.
    """
    jsonl = jsonl or NORMALIZADO / "cwe.jsonl"
    posiciones: dict[str, tuple[int, int]] = {}
    with open(jsonl, "rb") as fh:
        desplazamiento = 0
        for linea in fh:
            reg = json.loads(linea)
            posiciones[reg["id"]] = (desplazamiento, len(linea))
            desplazamiento += len(linea)

    indice = {}
    invertido: dict[str, set[str]] = {}
    hijos: dict[str, list[str]] = {}
    con_padre: set[str] = set()
    for e in entradas:
        off, ln = posiciones[e["id"]]
        indice[e["id"]] = {
            "nombre": e["nombre"],
            "tipo": e["tipo"],
            "abstraccion": e["abstraccion"],
            "estado": e["estado"],
            "offset": off,
            "longitud": ln,
        }
        textos = [e["nombre"], e["id"]] + [a["termino"] for a in e.get("alternos", [])]
        for t in textos:
            for tk in tokens(t):
                invertido.setdefault(tk, set()).add(e["id"])
        for r in e.get("relaciones", []):
            if r["vista"] == VISTA_JERARQUIA and r["naturaleza"] == "ChildOf":
                hijos.setdefault(r["id"], []).append(e["id"])
                con_padre.add(e["id"])

    for lista in hijos.values():
        lista.sort(key=numero)
    raices = sorted((i for i, e in indice.items() if e["tipo"] == "weakness" and i not in con_padre), key=numero)
    ordenar = lambda ids: sorted(ids, key=numero)  # noqa: E731
    inv = {k: ordenar(v) for k, v in sorted(invertido.items())}
    jer = {"vista": VISTA_JERARQUIA, "raices": raices, "hijos": dict(sorted(hijos.items(), key=lambda kv: numero(kv[0])))}

    _escribir(INDICES / "indice.json", json.dumps(indice, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
    _escribir(INDICES / "invertido.json", json.dumps(inv, ensure_ascii=False, separators=(",", ":")) + "\n")
    _escribir(INDICES / "jerarquia.json", json.dumps(jer, ensure_ascii=False, separators=(",", ":")) + "\n")
    return {f"indices/{n}": sha256_texto(INDICES / n) for n in ("indice.json", "invertido.json", "jerarquia.json")}


def texto_de_html(html_crudo: str) -> str:
    """HTML -> texto con una línea por elemento (suficiente para leer las tablas de MITRE)."""
    import html as _html
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", html_crudo, flags=re.S)
    t = _html.unescape(re.sub(r"<[^>]+>", "\n", t))
    return "\n".join(ln.strip() for ln in t.splitlines() if ln.strip())


def parsear_top25(texto: str) -> list[dict]:
    """Extrae la tabla «Rank, ID, Name, Score, CVEs in KEV, Rank Change» de la página del CWE Top 25.

    En el texto de la página cada fila ocupa seis líneas seguidas. Se exige que sean 25,
    consecutivas y con identificadores válidos: si MITRE cambia el formato, falla en voz alta
    en lugar de guardar una lista mal leída.
    """
    lineas = texto.splitlines()
    try:
        ini = next(i for i, ln in enumerate(lineas) if ln.startswith("Rank Change"))
    except StopIteration:
        raise ValueError("No se encontró la cabecera de la tabla del Top 25") from None
    filas = []
    i = ini + 1
    while i + 5 < len(lineas) and lineas[i].isdigit() and re.fullmatch(r"CWE-\d+", lineas[i + 1]):
        rank, cid, nombre, score, kev, cambio = lineas[i:i + 6]
        filas.append({"rango": int(rank), "id": cid, "nombre": nombre, "puntuacion": float(score),
                      "cves_en_kev": int(kev), "cambio_vs_anterior": cambio})
        i += 6
    if [f["rango"] for f in filas] != list(range(1, 26)):
        raise ValueError(f"Se esperaban 25 filas consecutivas y se leyeron {len(filas)}")
    return filas


def importar_top25(texto_html: str, hoy: str | None = None) -> dict:
    """Guarda el Top 25 oficial (rango, puntuación y CVE en KEV) junto a su procedencia."""
    texto = texto_de_html(texto_html)
    entradas = parsear_top25(texto)
    lineas = texto.splitlines()
    actualizada = next((lineas[i + 1] for i, ln in enumerate(lineas) if ln.startswith("Page Last Updated") and i + 1 < len(lineas)), "")
    doc = {
        "lista": "2025 CWE Top 25 Most Dangerous Software Weaknesses",
        "fuente": URL_TOP25,
        "metodologia": "https://cwe.mitre.org/top25/archive/2025/2025_methodology.html",
        "pagina_actualizada": actualizada,
        "fecha_consulta": hoy or date.today().isoformat(),
        "nota": "puntuacion = frecuencia normalizada x severidad CVSS media normalizada x 100 (CVSS v3.0/3.1); ver la metodologia.",
        "entradas": entradas,
    }
    _escribir(TOP25_JSON, json.dumps(doc, ensure_ascii=False, indent=1) + "\n")
    return doc


def leer_procedencia() -> dict:
    if PROCEDENCIA.is_file():
        return json.loads(PROCEDENCIA.read_text(encoding="utf-8"))
    return {}


def importar(ruta_zip: Path, *, url: str = URL_CATALOGO, hoy: str | None = None, forzar: bool = False) -> dict:
    """Importa el catálogo desde un ZIP local y actualiza las capas normalizada e índices.

    Es incremental en dos sentidos. Si el SHA-256 del ZIP coincide con el ya
    importado y los archivos siguen íntegros, no se reescribe nada. Si cambió,
    se compara entrada por entrada (huella del JSON canónico) y se informa de
    cuántas se añadieron, eliminaron o modificaron, sin reimportar a ciegas.
    """
    hoy = hoy or date.today().isoformat()
    sha_zip = sha256_archivo(ruta_zip)
    previa = leer_procedencia()
    if not forzar and previa.get("origen", {}).get("sha256_zip") == sha_zip and (NORMALIZADO / "cwe.jsonl").is_file():
        return {"estado": "sin_cambios", "sha256_zip": sha_zip, "version": previa["catalogo"]["version"]}

    nombre_xml, datos_xml = leer_xml_de_zip(ruta_zip)
    datos = normalizar_catalogo(parsear_xml(datos_xml))
    if not datos["entradas"]:
        raise ValueError("El catálogo no contiene entradas: se aborta sin tocar los datos existentes")

    # Comparación con la importación anterior, antes de sobrescribirla.
    cambios = {"anadidas": 0, "eliminadas": 0, "modificadas": 0}
    ruta_prev = NORMALIZADO / "cwe.jsonl"
    if ruta_prev.is_file():
        anterior = {r["id"]: huella(r) for r in (json.loads(x) for x in ruta_prev.read_text(encoding="utf-8").splitlines() if x)}
        nuevo = {e["id"]: huella(e) for e in datos["entradas"]}
        cambios["anadidas"] = len(nuevo.keys() - anterior.keys())
        cambios["eliminadas"] = len(anterior.keys() - nuevo.keys())
        cambios["modificadas"] = sum(1 for i in nuevo.keys() & anterior.keys() if nuevo[i] != anterior[i])

    huellas = escribir_normalizado(datos)
    huellas.update(construir_indices(datos["entradas"]))

    tipos: dict[str, int] = {}
    for e in datos["entradas"]:
        clave = e["abstraccion"] if e["tipo"] == "weakness" else e["tipo"]
        tipos[clave] = tipos.get(clave, 0) + 1

    proc = {
        "esquema": ESQUEMA,
        "origen": {
            "url": url,
            "terminos_de_uso": URL_TERMINOS,
            "archivo_xml": nombre_xml,
            "sha256_zip": sha_zip,
            "fecha_consulta": hoy,
        },
        "catalogo": {
            "version": datos["meta"]["catalogo_version"],
            "fecha": datos["meta"]["catalogo_fecha"],
            "entradas": len(datos["entradas"]),
            "vistas": len(datos["vistas"]),
            "referencias_externas": len(datos["referencias"]),
            "por_tipo": dict(sorted(tipos.items())),
        },
        "ultima_actualizacion": cambios,
        "huellas": dict(sorted(huellas.items())),
        "licencia": "Ver LICENCIA-MITRE.md. CWE es © The MITRE Corporation; uso libre con la condición de reproducir su aviso de copyright y licencia.",
    }
    _escribir(PROCEDENCIA, json.dumps(proc, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    return {"estado": "importado", "sha256_zip": sha_zip, "version": proc["catalogo"]["version"], "cambios": cambios, "catalogo": proc["catalogo"]}


# --------------------------------------------------------------------------
# 3. Consultar
# --------------------------------------------------------------------------
class BaseCWE:
    """Catálogo cargado en memoria. Se construye una vez y se consulta muchas."""

    def __init__(self, entradas: list[dict], vistas: list[dict], referencias: dict[str, dict] | None = None):
        self.entradas = {e["id"]: e for e in entradas}
        self.vistas = {v["id"]: v for v in vistas}
        self.referencias = referencias or {}
        self._hijos: dict[str, list[str]] | None = None

    @classmethod
    def cargar(cls, base: Path | None = None) -> "BaseCWE":
        base = base or NORMALIZADO
        ruta = base / "cwe.jsonl"
        if not ruta.is_file():
            raise FileNotFoundError(
                f"No hay catálogo local en {ruta}. Ejecuta `python scripts/cwe_kb.py importar --descargar` "
                "(requiere red una sola vez) o `importar --zip RUTA` con un ZIP ya descargado."
            )
        entradas = [json.loads(ln) for ln in ruta.read_text(encoding="utf-8").splitlines() if ln]
        vistas = json.loads((base / "vistas.json").read_text(encoding="utf-8"))
        refs_ruta = base / "referencias.json"
        refs = json.loads(refs_ruta.read_text(encoding="utf-8")) if refs_ruta.is_file() else {}
        return cls(entradas, vistas, refs)

    def __contains__(self, cwe_id: str) -> bool:
        return cwe_id in self.entradas

    def obtener(self, valor: str | int) -> dict:
        cid = normalizar_id(valor)
        try:
            return self.entradas[cid]
        except KeyError:
            raise KeyError(f"{cid} no existe en el catálogo cargado") from None

    def _mapa_hijos(self) -> dict[str, list[str]]:
        if self._hijos is None:
            h: dict[str, list[str]] = {}
            for e in self.entradas.values():
                for r in e.get("relaciones", []):
                    if r["vista"] == VISTA_JERARQUIA and r["naturaleza"] == "ChildOf":
                        h.setdefault(r["id"], []).append(e["id"])
            self._hijos = {k: sorted(v, key=numero) for k, v in h.items()}
        return self._hijos

    def padres(self, valor: str | int, vista: str = VISTA_JERARQUIA) -> list[str]:
        e = self.obtener(valor)
        return [r["id"] for r in e.get("relaciones", []) if r["naturaleza"] == "ChildOf" and r["vista"] == vista]

    def hijos(self, valor: str | int) -> list[str]:
        return list(self._mapa_hijos().get(normalizar_id(valor), []))

    def ancestros(self, valor: str | int) -> list[list[str]]:
        """Todos los caminos desde la entrada hasta una raíz (un CWE puede tener varios padres)."""
        caminos: list[list[str]] = []

        def subir(cid: str, ruta: list[str]) -> None:
            ps = self.padres(cid) if cid in self.entradas else []
            ps = [p for p in ps if p not in ruta]  # corta ciclos defensivamente
            if not ps:
                caminos.append(ruta)
                return
            for p in ps:
                subir(p, ruta + [p])

        cid = normalizar_id(valor)
        subir(cid, [cid])
        return caminos

    def descendientes(self, valor: str | int, profundidad: int = 1) -> dict[str, int]:
        """{id: nivel} de los descendientes hasta `profundidad` niveles."""
        salida: dict[str, int] = {}
        frontera = [normalizar_id(valor)]
        for nivel in range(1, profundidad + 1):
            siguiente = []
            for cid in frontera:
                for h in self.hijos(cid):
                    if h not in salida:
                        salida[h] = nivel
                        siguiente.append(h)
            frontera = siguiente
        return salida

    def relaciones(self, valor: str | int) -> list[dict]:
        return list(self.obtener(valor).get("relaciones", []))

    def buscar(self, consulta: str, *, tipo: str | None = None, abstraccion: str | None = None,
               incluir_obsoletas: bool = False, limite: int = 25) -> list[tuple[int, dict]]:
        """Búsqueda por palabras con puntuación simple y explicable.

        Cada palabra de la consulta puntúa por dónde aparece: en el nombre
        (3 puntos), en un término alterno (2) o en la descripción (1). Se exige
        que TODAS las palabras aparezcan en alguna parte. Si la consulta es un
        identificador, devuelve esa entrada directamente.
        """
        try:
            return [(100, self.obtener(consulta))]
        except (ValueError, KeyError):
            pass
        palabras = tokens(consulta)
        if not palabras:
            return []
        resultados = []
        for e in self.entradas.values():
            if tipo and e["tipo"] != tipo:
                continue
            if abstraccion and e["abstraccion"].lower() != abstraccion.lower():
                continue
            if not incluir_obsoletas and e["estado"] == "Deprecated":
                continue
            nombre = sin_acentos(e["nombre"])
            alt = sin_acentos(" ".join(a["termino"] for a in e.get("alternos", [])))
            desc = sin_acentos(e["descripcion"])
            puntos = 0
            for p in palabras:
                if p in nombre:
                    puntos += 3
                elif p in alt:
                    puntos += 2
                elif p in desc:
                    puntos += 1
                else:
                    puntos = 0
                    break
            if puntos:
                resultados.append((puntos, e))
        resultados.sort(key=lambda x: (-x[0], numero(x[1]["id"])))
        return resultados[:limite]

    def vista(self, vista_id: str) -> dict:
        return self.vistas[str(vista_id)]

    def miembros_de_vista(self, vista_id: str) -> list[dict]:
        return [self.entradas[m] for m in self.vista(vista_id)["miembros"] if m in self.entradas]


def configurar_salida() -> None:
    """La consola de Windows usa cp1252 por defecto y rompería con acentos y símbolos."""
    for flujo in (sys.stdout, sys.stderr):
        if hasattr(flujo, "reconfigure"):
            flujo.reconfigure(encoding="utf-8")
