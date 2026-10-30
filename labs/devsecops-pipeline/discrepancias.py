#!/usr/bin/env python3
"""Detecta discrepancias entre las fuentes que describen un mismo CVE (CNA, CISA-ADP y NVD).

Un CVE no tiene «una» puntuación ni «un» CWE: tiene los que aporta cada fuente, y pueden no
coincidir. Esta herramienta no decide quién tiene razón; señala DÓNDE no hay acuerdo para que
una persona lo mire. Las discrepancias que busca son las que aparecen en datos reales:

  cvss_distinto            dos fuentes puntúan distinto el mismo CVE (p. ej. NVD 9.8 frente a CISA-ADP 7.5)
  puntuacion_vs_vector     la puntuación declarada no es la que da su propio vector (error de la fuente)
  cwe_distinto             el CNA y NVD asignan CWE distintos (p. ej. hija frente a padre)
  nvd_sin_cwe_concreto     NVD marca «NVD-CWE-noinfo» u «Other» mientras otra fuente sí da CWE
  sin_cwe_primario         hay CWE pero ninguno figura como primario
  sin_cvss_en_ninguna_fuente  no hay puntuación CVSS 3.1 de ninguna fuente

Trabaja sobre `datos/casos-cwe-cve.json` (la instantánea de casos reales). Sin red.

Uso:
    python discrepancias.py                 # resumen de todos los casos
    python discrepancias.py CVE-2024-6387   # detalle de uno
"""
from __future__ import annotations

import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import cvss  # noqa: E402

INSTANTANEA = os.path.join(AQUI, "datos", "casos-cwe-cve.json")
MARCADORES_NVD = ("NVD-CWE-noinfo", "NVD-CWE-Other")


def discrepancias(caso: dict) -> list[dict]:
    hallazgos: list[dict] = []

    # --- CVSS 3.1: puntuaciones de las distintas fuentes -------------------------------------
    puntos: dict[str, float] = {}
    for m in caso.get("cvss31", []):
        puntos[m["fuente"]] = m["puntuacion"]
    if puntos and max(puntos.values()) - min(puntos.values()) >= 0.1:
        hallazgos.append({"tipo": "cvss_distinto", "detalle": dict(sorted(puntos.items()))})
    if not puntos:
        hallazgos.append({"tipo": "sin_cvss_en_ninguna_fuente", "detalle": {}})

    # --- Puntuación declarada frente a la que da su propio vector ------------------------------
    for m in caso.get("cvss31", []) + caso.get("cvss31_cna", []):
        try:
            calculada = cvss.puntuar(m["vector"])["base"]
        except cvss.VectorInvalido:
            continue
        if abs(calculada - m["puntuacion"]) > 0.05:
            hallazgos.append({"tipo": "puntuacion_vs_vector",
                              "detalle": {"fuente": m.get("fuente", "CNA (registro CVE)"), "declarada": m["puntuacion"],
                                          "calculada": calculada, "vector": m["vector"]}})

    # --- CWE ---------------------------------------------------------------------------------
    cna = set(caso.get("cwe_cna", []))
    adp = {c for lista in caso.get("cwe_adp", {}).values() for c in lista}
    nvd_primario = {c["id"] for c in caso.get("cwe_nvd", []) if c["tipo"] == "Primary" and c["fuente"] == "NVD"}
    nvd_todos = {c["id"] for c in caso.get("cwe_nvd", [])}
    if cna and nvd_primario and not (cna & nvd_primario):
        hallazgos.append({"tipo": "cwe_distinto", "detalle": {"CNA": sorted(cna), "NVD (primario)": sorted(nvd_primario)}})
    if nvd_primario & set(MARCADORES_NVD) and (cna - set(MARCADORES_NVD) or adp):
        hallazgos.append({"tipo": "nvd_sin_cwe_concreto",
                          "detalle": {"NVD": sorted(nvd_primario), "CNA": sorted(cna), "ADP": sorted(adp)}})
    concretos = {c for c in nvd_todos if not c.startswith("NVD-CWE")}
    if concretos and not any(c["tipo"] == "Primary" for c in caso.get("cwe_nvd", [])):
        hallazgos.append({"tipo": "sin_cwe_primario", "detalle": {"CWE": sorted(concretos)}})
    return hallazgos


def cargar(ruta: str = INSTANTANEA) -> dict[str, dict]:
    with open(ruta, encoding="utf-8") as fh:
        return {c["cve"]: c for c in json.load(fh)["casos"]}


def main(argv: list[str] | None = None) -> int:
    for flujo in (sys.stdout, sys.stderr):
        if hasattr(flujo, "reconfigure"):
            flujo.reconfigure(encoding="utf-8")
    casos = cargar()
    pedidos = (argv if argv is not None else sys.argv[1:]) or sorted(casos)
    for cve_id in pedidos:
        if cve_id not in casos:
            print(f"{cve_id}: no está en la instantánea", file=sys.stderr)
            return 1
        hs = discrepancias(casos[cve_id])
        print(f"{cve_id}: {len(hs)} discrepancia(s)" if hs else f"{cve_id}: sin discrepancias entre fuentes")
        for h in hs:
            print(f"    - {h['tipo']}: {json.dumps(h['detalle'], ensure_ascii=False)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
