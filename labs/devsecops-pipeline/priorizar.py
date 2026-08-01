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
herramienta puede calcular: la exposición real (--exposicion).

Sin dependencias externas: solo biblioteca estándar.

Uso:
    python priorizar.py --hallazgos hallazgos-ejemplo.json
    python priorizar.py --hallazgos salida/mis-hallazgos.json --salida informe.md
    python priorizar.py --hallazgos hallazgos-ejemplo.json --sin-red
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
def render(hallazgos: list[dict], kev_ok: bool, epss_ok: bool) -> str:
    lineas: list[str] = []
    ap = lineas.append

    ap("# Plan de remediación priorizado")
    ap("")
    ap("Orden aplicado: **CISA KEV → EPSS → CVSS ajustado por exposición**.")
    ap("")

    # --- Cobertura: lo primero, siempre ---
    ap("## Cobertura de las señales")
    ap("")
    ap("| Señal | Estado |")
    ap("|---|---|")
    ap(f"| CISA KEV | {'consultada' if kev_ok else '**NO DISPONIBLE** — sin dato de explotación activa'} |")
    ap(f"| EPSS | {'consultada' if epss_ok else '**NO DISPONIBLE** — sin probabilidad de explotación'} |")
    ap("| CVSS | tomada de los hallazgos de entrada |")
    ap("")
    if not (kev_ok and epss_ok):
        ap("> ⚠️ Faltan señales: este orden es **provisional**. Una señal no consultada")
        ap("> no equivale a una señal en cero — repite la priorización con conectividad")
        ap("> antes de dar el plan por bueno.")
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

        paquete = f"`{h.get('paquete', '?')}=={h.get('version', '?')}`"
        ap(f"- [ ] **{etiqueta}** · {cve} · {paquete}")
        ap(f"  - {' · '.join(insignias)}")
        if h.get("_fix"):
            ap(f"  - **Acción:** subir a `{h['_fix']}` "
               f"_(versión mínima que corrige, no la más reciente)_")
        else:
            ap("  - **Acción:** sin versión corregida publicada → mitigar, aislar o "
               "sustituir la dependencia, y **documentarlo**")
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
    parser = argparse.ArgumentParser(
        description="Prioriza hallazgos por KEV -> EPSS -> CVSS ajustado por exposición.",
    )
    parser.add_argument("--hallazgos", default=os.path.join(AQUI, "hallazgos-ejemplo.json"),
                        help="JSON con los hallazgos a priorizar.")
    parser.add_argument("--salida", help="Archivo Markdown de salida (por defecto, stdout).")
    parser.add_argument("--sin-red", action="store_true",
                        help="No consultar KEV ni EPSS (usa caché si existe).")
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

    kev, kev_ok = descargar_kev(args.sin_red)
    cves = [h["cve"] for h in hallazgos if h.get("cve")]
    epss, epss_ok = consultar_epss(cves, args.sin_red)

    for h in hallazgos:
        cve = h.get("cve")
        h["_kev"] = bool(cve and cve in kev)
        h["_epss"] = epss.get(cve) if cve else None
        h["_fix"] = version_minima_que_corrige(h.get("versiones_corregidas") or [])

    hallazgos.sort(key=prioridad)
    informe = render(hallazgos, kev_ok, epss_ok)

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
