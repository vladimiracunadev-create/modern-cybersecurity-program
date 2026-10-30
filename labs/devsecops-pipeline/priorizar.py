#!/usr/bin/env python3
"""Prioriza hallazgos de vulnerabilidades con las tres señales: KEV, EPSS y CVSS.

Este script es la **implementación** de lo que el laboratorio enseña en la
sección "El problema difícil: priorizar". Un escáner te entrega una lista; esto
la convierte en un orden de trabajo defendible.

Las tres señales responden preguntas distintas:

  CISA KEV  ¿se está explotando YA, de forma documentada?   -> binaria
  EPSS      ¿qué probabilidad hay de que se explote pronto?  -> 0.0 a 1.0
  CVSS      ¿cuán grave sería si se explotara?               -> 0.0 a 10.0

El orden es KEV -> EPSS -> CVSS, y no al revés: una vulnerabilidad con
explotación activa confirmada y CVSS 7.5 es más urgente que una CVSS 9.8 que
nadie ha explotado nunca. Sobre ese orden se aplica el factor que ninguna
herramienta puede calcular: la exposición real (campo `exposicion` de cada
hallazgo).

Qué NO decide este script: la causa raíz. Un hallazgo puede llevar además la
debilidad que lo origina (`cwe`) y el vector CVSS (`cvss_vector`); se muestran en
el informe y el vector se recalcula para detectar notas mal copiadas, pero el
orden sigue siendo KEV → EPSS → CVSS ajustado. Las clases 368 y 369 explican por qué.

Sin dependencias externas: solo biblioteca estándar.

Uso:
    python priorizar.py --hallazgos hallazgos-ejemplo.json
    python priorizar.py --hallazgos salida/mis-hallazgos.json --salida informe.md
    python priorizar.py --hallazgos hallazgos-ejemplo.json --sin-red
    python priorizar.py --hallazgos hallazgos-cwe-ejemplo.json --instantanea datos/casos-cwe-cve.json

`--instantanea` usa KEV y EPSS de una foto guardada (la de `actualizar_casos.py`)
en vez de consultar la red: reproducible y sin conexión, pero con la fecha de la
foto, no la de hoy. El informe lo declara.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

KEV_URL = (
    "https://www.cisa.gov/sites/default/files/feeds/"
    "known_exploited_vulnerabilities.json"
)
EPSS_URL = "https://api.first.org/data/v1/epss?cve={}"
TIMEOUT = 30

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(AQUI, "salida", ".cache")
# Índice de la base de conocimiento CWE del programa (opcional): solo se lee para
# poner nombre a los identificadores; si no está, el informe muestra el número.
INDICE_CWE = os.path.join(AQUI, "..", "..", "knowledge", "cwe", "indices", "indice.json")


# --------------------------------------------------------------------------
# Consulta de las fuentes
# --------------------------------------------------------------------------
def _get_json(url: str) -> dict | None:
    """Descarga JSON. Devuelve None si falla: la ausencia de dato NO es un 0."""
    try:
        peticion = urllib.request.Request(url, headers={"User-Agent": "lab-devsecops"})
        with urllib.request.urlopen(peticion, timeout=TIMEOUT) as respuesta:
            return json.loads(respuesta.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
        print(f"  [!] No se pudo consultar {url.split('?')[0]}: {exc}", file=sys.stderr)
        return None


def descargar_kev(sin_red: bool = False) -> tuple[set[str], bool]:
    """Catálogo CISA KEV. Devuelve (conjunto de CVE, se_pudo_consultar)."""
    ruta_cache = os.path.join(CACHE, "cisa_kev.json")

    if not sin_red:
        datos = _get_json(KEV_URL)
        if datos:
            cves = {v["cveID"] for v in datos.get("vulnerabilities", []) if v.get("cveID")}
            os.makedirs(CACHE, exist_ok=True)
            with open(ruta_cache, "w", encoding="utf-8") as fh:
                json.dump(sorted(cves), fh)
            return cves, True

    if os.path.isfile(ruta_cache):
        with open(ruta_cache, encoding="utf-8") as fh:
            print("  [i] Usando la copia en caché del catálogo KEV.", file=sys.stderr)
            return set(json.load(fh)), True

    return set(), False


def consultar_epss(cves: list[str], sin_red: bool = False) -> tuple[dict[str, float], bool]:
    """Puntuaciones EPSS. Devuelve ({cve: score}, se_pudo_consultar)."""
    if sin_red or not cves:
        return {}, False

    puntuaciones: dict[str, float] = {}
    # La API acepta varios CVE separados por coma; se trocea para no exceder la URL.
    for i in range(0, len(cves), 50):
        lote = cves[i:i + 50]
        datos = _get_json(EPSS_URL.format(",".join(lote)))
        if datos is None:
            return puntuaciones, False
        for fila in datos.get("data", []):
            try:
                puntuaciones[fila["cve"]] = float(fila["epss"])
            except (KeyError, TypeError, ValueError):
                continue
    return puntuaciones, True


# --------------------------------------------------------------------------
# Instantánea, CWE y vector CVSS (extensiones opcionales)
# --------------------------------------------------------------------------
def cargar_instantanea(ruta: str) -> tuple[set[str], dict[str, float], set[str], dict]:
    """KEV y EPSS desde una foto guardada. Devuelve (kev, epss, cves_conocidos, procedencia).

    `cves_conocidos` importa: un CVE que NO está en la foto no es «sin explotación»,
    es «no sabemos». Por eso el informe distingue ambos casos.
    """
    with open(ruta, encoding="utf-8") as fh:
        doc = json.load(fh)
    kev, epss, conocidos = set(), {}, set()
    for caso in doc.get("casos", []):
        conocidos.add(caso["cve"])
        if caso.get("kev"):
            kev.add(caso["cve"])
        if caso.get("epss"):
            epss[caso["cve"]] = float(caso["epss"]["puntuacion"])
    return kev, epss, conocidos, doc.get("procedencia", {})


def cargar_ssvc(ruta: str) -> dict[str, dict]:
    """{cve: puntos de decisión SSVC de CISA} desde la instantánea (para el plazo de BOD 26-04)."""
    with open(ruta, encoding="utf-8") as fh:
        doc = json.load(fh)
    return {c["cve"]: c["ssvc_cisa"] for c in doc.get("casos", []) if c.get("ssvc_cisa")}


def extraer_cwes(valor) -> list[str]:
    """Acepta «CWE-79», 79, una lista de ellos o texto libre, y devuelve ['CWE-79', ...]."""
    if valor is None:
        return []
    if isinstance(valor, (list, tuple)):
        salida: list[str] = []
        for v in valor:
            salida += extraer_cwes(v)
        return list(dict.fromkeys(salida))
    if isinstance(valor, int):
        return [f"CWE-{valor}"]
    return list(dict.fromkeys(f"CWE-{int(n)}" for n in re.findall(r"CWE-(\d{1,5})", str(valor), re.IGNORECASE)))


def nombres_cwe() -> dict[str, str]:
    """{'CWE-89': 'Improper Neutralization...'} desde el índice local; vacío si no existe."""
    try:
        with open(INDICE_CWE, encoding="utf-8") as fh:
            return {k: v["nombre"] for k, v in json.load(fh).items()}
    except (OSError, ValueError, KeyError):
        return {}


def verificar_vector(h: dict) -> None:
    """Si el hallazgo trae `cvss_vector`, recalcula la nota y anota discrepancias.

    Dos fallos reales que esto atrapa: copiar mal el número desde el escáner y
    dar por válida una nota que corresponde a OTRO vector (p. ej. la del CNA en
    lugar de la de NVD). No decide nada; solo avisa.
    """
    vector = h.get("cvss_vector")
    if not vector:
        return
    try:
        from cvss import VectorInvalido, puntuar
    except ImportError:  # el módulo vive junto a este script; si falta, no hay verificación
        h["_aviso_vector"] = "no se pudo cargar cvss.py: el vector no se verificó"
        return
    try:
        calculada = puntuar(vector)["puntuacion"]
    except VectorInvalido as exc:
        h["_aviso_vector"] = f"vector CVSS inválido ({exc}); se usa la nota declarada"
        return
    h["_cvss_calculado"] = calculada
    if not h.get("cvss"):
        h["cvss"] = calculada
    elif abs(float(h["cvss"]) - calculada) > 0.05:
        h["_aviso_vector"] = f"la nota declarada ({h['cvss']}) no coincide con la del vector ({calculada})"


# --------------------------------------------------------------------------
# Minimal blast radius
# --------------------------------------------------------------------------
def _clave_version(version: str) -> tuple:
    """Clave de orden numérica y tolerante para comparar versiones."""
    partes = [p for p in re.split(r"[.\-+_]", version) if p]
    clave = []
    for parte in partes:
        if parte.isdigit():
            clave.append((0, int(parte), ""))
        else:
            numero = re.match(r"^(\d+)(.*)$", parte)
            if numero:
                clave.append((0, int(numero.group(1)), numero.group(2)))
            else:
                # Los sufijos alfabéticos (rc, beta) ordenan ANTES que el final.
                clave.append((-1, 0, parte))
    return tuple(clave)


def version_minima_que_corrige(corregidas: list[str]) -> str | None:
    """La versión más BAJA que corrige el fallo, no la más reciente.

    Se llama *minimal blast radius*: subir a la última disponible arrastra
    cambios de API y funcionalidad que nadie pidió y que rompen builds. Se sube
    lo mínimo imprescindible para cerrar la vulnerabilidad; modernizar es otra
    tarea, con otro calendario y otro riesgo.
    """
    validas = [v for v in corregidas if v]
    if not validas:
        return None
    return sorted(validas, key=_clave_version)[0]


# --------------------------------------------------------------------------
# Priorización
# --------------------------------------------------------------------------
FACTOR_EXPOSICION = {
    "publica": 1.0,      # alcanzable desde Internet
    "interna": 0.6,      # solo desde la red corporativa
    "no-alcanzable": 0.2,  # el código afectado no se ejecuta
    "desconocida": 0.8,  # sin analizar: no se asume lo mejor
}


def prioridad(h: dict) -> tuple:
    """Clave de orden: KEV primero, luego EPSS, luego CVSS ajustado."""
    factor = FACTOR_EXPOSICION.get(h.get("exposicion", "desconocida"), 0.8)
    cvss = float(h.get("cvss") or 0.0)
    epss = float(h.get("_epss") or 0.0)
    return (
        not h.get("_kev", False),   # False (0) primero => los KEV arriba
        -epss,
        -(cvss * factor),
    )


def etiqueta_prioridad(h: dict) -> str:
    """Etiqueta legible, coherente con el MISMO criterio que ordena la lista.

    Usa el CVSS **ajustado por exposición**, no el crudo: si el orden baja un
    hallazgo por no ser alcanzable, su etiqueta tiene que bajar también. Una
    etiqueta que contradice el orden destruye la confianza en el informe.
    """
    if h.get("_kev"):
        return "P1"
    if (h.get("_epss") or 0) >= 0.10:
        return "P1"
    factor = FACTOR_EXPOSICION.get(h.get("exposicion", "desconocida"), 0.8)
    cvss_ajustado = float(h.get("cvss") or 0.0) * factor
    if cvss_ajustado >= 7.0:
        return "P2"
    if cvss_ajustado >= 4.0:
        return "P3"
    return "P4"


# --------------------------------------------------------------------------
# Informe
# --------------------------------------------------------------------------
def render(hallazgos: list[dict], kev_ok: bool, epss_ok: bool, instantanea: dict | None = None,
           nombres: dict[str, str] | None = None, con_bod: bool = False) -> str:
    lineas: list[str] = []
    ap = lineas.append
    nombres = nombres or {}

    ap("# Plan de remediación priorizado")
    ap("")
    ap("Orden aplicado: **CISA KEV → EPSS → CVSS ajustado por exposición**.")
    ap("")

    # --- Cobertura: lo primero, siempre ---
    ap("## Cobertura de las señales")
    ap("")
    ap("| Señal | Estado |")
    ap("|---|---|")
    if instantanea:
        fecha = instantanea.get("fecha_consulta", "?")
        kev_v = instantanea.get("kev_version_catalogo", "?")
        ap(f"| CISA KEV | **instantánea** del {fecha} (catálogo {kev_v}), no el estado de hoy |")
        ap(f"| EPSS | **instantánea** del {fecha}, no el valor de hoy |")
    else:
        ap(f"| CISA KEV | {'consultada' if kev_ok else '**NO DISPONIBLE** — sin dato de explotación activa'} |")
        ap(f"| EPSS | {'consultada' if epss_ok else '**NO DISPONIBLE** — sin probabilidad de explotación'} |")
    ap("| CVSS | tomada de los hallazgos de entrada |")
    ap("")
    if not (kev_ok and epss_ok):
        ap("> ⚠️ Faltan señales: este orden es **provisional**. Una señal no consultada")
        ap("> no equivale a una señal en cero — repite la priorización con conectividad")
        ap("> antes de dar el plan por bueno.")
        ap("")

    fuera = [h.get("cve") for h in hallazgos if h.get("_fuera_instantanea")]
    if fuera:
        ap(f"> ⚠️ {len(fuera)} CVE no figuran en la instantánea ({', '.join(fuera)}): para ellos")
        ap("> «sin KEV / sin EPSS» significa **no sabemos**, no «no se explota».")
        ap("")

    if con_bod:
        ap("> ℹ️ **BOD 26-04** es obligatoria solo para agencias civiles federales de EE. UU. Aquí se usa como")
        ap("> **referencia** de cómo combinar exposición, KEV, automatización e impacto técnico; los plazos de")
        ap("> tu organización los fijas tú. Los datos SSVC son los de CISA Vulnrichment en la fecha de la instantánea.")
        ap("")

    sin_exposicion = [h for h in hallazgos if h.get("exposicion", "desconocida") == "desconocida"]
    if sin_exposicion:
        ap(f"> ℹ️ {len(sin_exposicion)} hallazgo(s) sin exposición declarada: se les aplica el")
        ap("> factor conservador (0.8). La exposición real la determina una persona; es el")
        ap("> único ajuste que ninguna herramienta puede calcular por ti.")
        ap("")

    # --- Resumen ---
    n_kev = sum(1 for h in hallazgos if h.get("_kev"))
    ap("## Resumen")
    ap("")
    ap(f"- Hallazgos priorizados: **{len(hallazgos)}**")
    ap(f"- Con explotación activa (CISA KEV): **{n_kev}**")
    ap(f"- Sin versión corregida disponible: **{sum(1 for h in hallazgos if not h.get('_fix'))}**")
    ap("")

    # --- Checklist ---
    ap("## Checklist")
    ap("")
    for h in hallazgos:
        cve = h.get("cve") or h.get("id") or "(sin id)"
        etiqueta = etiqueta_prioridad(h)
        insignias = []
        if h.get("_kev"):
            insignias.append("**[CISA KEV]**")
        if h.get("_epss") is not None:
            insignias.append(f"EPSS {h['_epss'] * 100:.1f}%")
        if h.get("cvss"):
            insignias.append(f"CVSS {h['cvss']}")
        insignias.append(f"exposición: {h.get('exposicion', 'desconocida')}")
        cwes = extraer_cwes(h.get("cwe"))
        if cwes:
            insignias.append("causa raíz: " + ", ".join(f"{c} {nombres[c]}" if c in nombres else c for c in cwes))

        paquete = f"`{h.get('paquete', '?')}=={h.get('version', '?')}`"
        ap(f"- [ ] **{etiqueta}** · {cve} · {paquete}")
        ap(f"  - {' · '.join(insignias)}")
        if h.get("_fix"):
            ap(f"  - **Acción:** subir a `{h['_fix']}` "
               f"_(versión mínima que corrige, no la más reciente)_")
        else:
            ap("  - **Acción:** sin versión corregida publicada → mitigar, aislar o "
               "sustituir la dependencia, y **documentarlo**")
        if con_bod:
            pz = h.get("_plazo")
            if pz:
                supuesto = " (exposición desconocida: se asumió expuesto)" if pz.get("supuesto_de_exposicion") else ""
                ap(f"  - Plazo de referencia BOD 26-04: **{pz['texto']}**{supuesto}")
            else:
                ap("  - Plazo de referencia BOD 26-04: sin datos SSVC de CISA para este CVE")
        if h.get("_aviso_vector"):
            ap(f"  - ⚠️ {h['_aviso_vector']}")
        if h.get("nota"):
            ap(f"  - Nota: {h['nota']}")
    ap("")

    ap("## Después de aplicar")
    ap("")
    ap("Cada subida de versión se verifica por separado: aplicar → instalar → pasar los")
    ap("tests. Si los tests fallan, **revertir** y registrar el hallazgo como")
    ap("*remediación bloqueada*, con el motivo. Una subida bloqueada no es un fracaso:")
    ap("es un hallazgo con contexto que alguien tiene que decidir.")
    ap("")
    return "\n".join(lineas)


# --------------------------------------------------------------------------
def main() -> int:
    # El informe lleva flechas y emojis; la consola de Windows usa cp1252 por defecto y
    # `print()` fallaba con UnicodeEncodeError cuando no se pasaba --salida.
    for flujo in (sys.stdout, sys.stderr):
        if hasattr(flujo, "reconfigure"):
            flujo.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(
        description="Prioriza hallazgos por KEV -> EPSS -> CVSS ajustado por exposición.",
    )
    parser.add_argument("--hallazgos", default=os.path.join(AQUI, "hallazgos-ejemplo.json"),
                        help="JSON con los hallazgos a priorizar.")
    parser.add_argument("--salida", help="Archivo Markdown de salida (por defecto, stdout).")
    parser.add_argument("--sin-red", action="store_true",
                        help="No consultar KEV ni EPSS (usa caché si existe).")
    parser.add_argument("--instantanea", help="JSON de datos/casos-cwe-cve.json: usa su KEV y EPSS en vez de la red.")
    parser.add_argument("--bod-26-04", action="store_true", dest="bod",
                        help="Añade el plazo de referencia de CISA BOD 26-04 (requiere --instantanea, de donde salen los datos SSVC).")
    args = parser.parse_args()

    if not os.path.isfile(args.hallazgos):
        print(f"ERROR: no existe {args.hallazgos}", file=sys.stderr)
        return 1

    with open(args.hallazgos, encoding="utf-8") as fh:
        hallazgos = json.load(fh)
    if not isinstance(hallazgos, list):
        print("ERROR: el JSON debe ser una lista de hallazgos.", file=sys.stderr)
        return 1

    print(f"Priorizando {len(hallazgos)} hallazgo(s)...", file=sys.stderr)

    instantanea = None
    conocidos: set[str] = set()
    if args.instantanea:
        try:
            kev, epss, conocidos, instantanea = cargar_instantanea(args.instantanea)
        except (OSError, ValueError, KeyError) as exc:
            print(f"ERROR: no se pudo leer la instantánea: {exc}", file=sys.stderr)
            return 1
        kev_ok = epss_ok = True
    else:
        kev, kev_ok = descargar_kev(args.sin_red)
        cves = [h["cve"] for h in hallazgos if h.get("cve")]
        epss, epss_ok = consultar_epss(cves, args.sin_red)

    ssvc: dict[str, dict] = {}
    if args.bod:
        if not args.instantanea:
            print("ERROR: --bod-26-04 necesita --instantanea (los datos SSVC de CISA vienen de ahí).", file=sys.stderr)
            return 1
        ssvc = cargar_ssvc(args.instantanea)

    for h in hallazgos:
        cve = h.get("cve")
        h["_kev"] = bool(cve and cve in kev)
        h["_epss"] = epss.get(cve) if cve else None
        h["_fix"] = version_minima_que_corrige(h.get("versiones_corregidas") or [])
        h["_fuera_instantanea"] = bool(instantanea is not None and cve and cve not in conocidos)
        verificar_vector(h)
        if args.bod:
            from bod2604 import plazo_de_hallazgo
            h["_plazo"] = plazo_de_hallazgo(h.get("exposicion", "desconocida"), h["_kev"], ssvc.get(cve or ""))

    hallazgos.sort(key=prioridad)
    informe = render(hallazgos, kev_ok, epss_ok, instantanea, nombres_cwe(), con_bod=args.bod)

    if args.salida:
        os.makedirs(os.path.dirname(os.path.abspath(args.salida)), exist_ok=True)
        with open(args.salida, "w", encoding="utf-8") as fh:
            fh.write(informe)
        print(f"Informe escrito en {args.salida}", file=sys.stderr)
    else:
        print(informe)
    return 0


if __name__ == "__main__":
    sys.exit(main())
