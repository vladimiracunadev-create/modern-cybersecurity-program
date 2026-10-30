#!/usr/bin/env python3
"""Mide cuántos CVE publicados en una ventana de fechas ha enriquecido NVD, y con qué datos.

Por qué existe
--------------
Es habitual suponer que cada CVE trae su CVSS y su CWE «de NVD». No es así: NVD enriquece
solo parte de los registros (estado `Analyzed`), y deja otros en `Deferred` («no programado
para enriquecimiento»), `Awaiting Analysis` o `Received`. Las puntuaciones y los CWE de un CVE
pueden venir del CNA que lo asignó, de un ADP como CISA-ADP, de NVD, o de nadie. Este script
cuenta, para una ventana de publicación, en qué estado está cada CVE y cuántos llevan datos
de cada fuente, para que decidas con datos de qué fuentes depende tu proceso.

Es una FOTO del momento de la consulta: los estados cambian cada día.

Sin dependencias ni claves obligatorias. La API pública de NVD limita las consultas anónimas;
el script espera entre páginas (con NVD_API_KEY, variable opcional, va más rápido).

Uso:
    python nvd_estados.py --desde 2026-09-01 --hasta 2026-09-10 --salida datos/nvd-estados.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from collections import Counter

URL = ("https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate={d}T00:00:00.000"
       "&pubEndDate={h}T23:59:59.000&resultsPerPage=2000&startIndex={i}")
AQUI = os.path.dirname(os.path.abspath(__file__))

# Estado de la API de NVD -> estado en la web (según https://nvd.nist.gov/vuln/vulnerability-status).
NOMBRE_WEB = {
    "Received": "Received",
    "Awaiting Analysis": "Awaiting Enrichment",
    "Undergoing Analysis": "Undergoing Enrichment",
    "Analyzed": "Enriched",
    "Modified": "Modified After Enrichment",
    "Deferred": "Not Scheduled",
    "Rejected": "Rejected",
}


def contar(vulnerabilidades: list[dict]) -> dict:
    """Cuenta estados y cuántos CVE traen cada dato, y de quién. Función pura: se prueba sin red."""
    estados: Counter[str] = Counter()
    con_v31_nvd = con_v40_algun = con_cwe_nvd = con_cwe_cualquiera = con_v31_cualquiera = 0
    for v in vulnerabilidades:
        c = v["cve"]
        estados[c.get("vulnStatus", "?")] += 1
        m = c.get("metrics", {})
        if any(x.get("source") == "nvd@nist.gov" for x in m.get("cvssMetricV31", [])):
            con_v31_nvd += 1
        if m.get("cvssMetricV31"):
            con_v31_cualquiera += 1
        if m.get("cvssMetricV40"):
            con_v40_algun += 1
        pesos = c.get("weaknesses", [])
        if any(w.get("source") == "nvd@nist.gov" for w in pesos):
            con_cwe_nvd += 1
        if pesos:
            con_cwe_cualquiera += 1
    return {
        "leidos": len(vulnerabilidades),
        "estados": dict(sorted(estados.items())),
        "con_cvss31_publicado_por_nvd": con_v31_nvd,
        "con_cvss31_de_cualquier_fuente": con_v31_cualquiera,
        "con_cvss40_de_alguna_fuente": con_v40_algun,
        "con_cwe_asignado_por_nvd": con_cwe_nvd,
        "con_cwe_de_cualquier_fuente": con_cwe_cualquiera,
    }


def porcentajes(conteo: dict) -> dict[str, float]:
    total = conteo["leidos"] or 1
    return {k: round(100 * v / total, 1) for k, v in conteo["estados"].items()}


def _get(url: str) -> dict:
    cab = {"User-Agent": "modern-cybersecurity-program/nvd-estados"}
    if os.environ.get("NVD_API_KEY"):
        cab["apiKey"] = os.environ["NVD_API_KEY"]
    with urllib.request.urlopen(urllib.request.Request(url, headers=cab), timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def descargar(desde: str, hasta: str, pausa: float) -> tuple[list[dict], int]:
    todas: list[dict] = []
    total = None
    i = 0
    while total is None or i < total:
        d = _get(URL.format(d=desde, h=hasta, i=i))
        total = d["totalResults"]
        todas += d["vulnerabilities"]
        i += d["resultsPerPage"]
        if i < total:
            time.sleep(pausa)
    return todas, total


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Estado de enriquecimiento de NVD para una ventana de publicación.")
    ap.add_argument("--desde", required=True, help="AAAA-MM-DD (publicación)")
    ap.add_argument("--hasta", required=True, help="AAAA-MM-DD (publicación, máximo 120 días de ventana en la API)")
    ap.add_argument("--salida", default=os.path.join(AQUI, "datos", "nvd-estados.json"))
    ap.add_argument("--pausa", type=float, default=None)
    a = ap.parse_args(argv)
    pausa = a.pausa if a.pausa is not None else (0.7 if os.environ.get("NVD_API_KEY") else 7.0)
    try:
        todas, total = descargar(a.desde, a.hasta, pausa)
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
        print(f"ERROR: no se pudo consultar NVD: {exc}", file=sys.stderr)
        return 1
    conteo = contar(todas)
    doc = {
        "procedencia": {
            "fuente": "https://services.nvd.nist.gov/rest/json/cves/2.0",
            "ventana_de_publicacion": f"{a.desde}..{a.hasta}",
            "fecha_consulta": time.strftime("%Y-%m-%d", time.gmtime()),
            "total_segun_nvd": total,
            "nombres_web": NOMBRE_WEB,
            "advertencia": "Foto del momento de la consulta; los estados cambian a diario. Una sola ventana no es una estadística general.",
        },
        **conteo,
        "porcentaje_por_estado": porcentajes(conteo),
    }
    os.makedirs(os.path.dirname(os.path.abspath(a.salida)), exist_ok=True)
    with open(a.salida, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print(f"{conteo['leidos']} CVE leídos (NVD declara {total}); escrito en {a.salida}", file=sys.stderr)
    return 0 if conteo["leidos"] == total else 1


if __name__ == "__main__":
    sys.exit(main())
