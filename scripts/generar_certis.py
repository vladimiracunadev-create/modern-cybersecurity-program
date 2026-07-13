# -*- coding: utf-8 -*-
"""
Genera los documentos de mapeo de certificaciones a partir de
certificaciones/_mapeo.json:
  - certificaciones/README.md            (índice con cobertura ponderada por cert)
  - certificaciones/<id>.md              (un doc por certificación)

La cobertura total es la suma ponderada por el peso oficial de cada dominio
(los pesos de cada cert suman 100). Cálculo auditable, no "a ojo".

Uso: python scripts/generar_certis.py
"""
from __future__ import annotations
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "certificaciones")


def cobertura_total(cert) -> float:
    suma_peso = sum(d["peso"] for d in cert["dominios"])
    if suma_peso != 100:
        raise ValueError(f"{cert['id']}: los pesos suman {suma_peso}, no 100")
    return sum(d["peso"] * d["cobertura"] for d in cert["dominios"]) / 100.0


def barra(pct: float) -> str:
    llenos = round(pct / 10)
    return "█" * llenos + "░" * (10 - llenos)


def escribir(path, texto):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def doc_cert(cert) -> str:
    total = cobertura_total(cert)
    pesos = "pesos oficiales del examen" if cert["pesos_oficiales"] else "pesos estimados (el proveedor no publica ponderación oficial por dominio)"
    L = []
    L.append(f"# {cert['nombre']}")
    L.append("")
    L.append(f"> **Código:** {cert['codigo']} · **Proveedor:** {cert['proveedor']} · "
             f"**Nivel:** {cert['nivel']} · [Página oficial]({cert['url']})")
    L.append("")
    L.append(f"[⬅️ Volver al índice de certificaciones](README.md)")
    L.append("")
    L.append(cert["resumen"])
    L.append("")
    L.append(f"## 📊 Cobertura estimada del programa: **{total:.0f}%**")
    L.append("")
    L.append(f"`{barra(total)}` {total:.1f}% — suma ponderada por dominio ({pesos}).")
    L.append("")
    L.append("## Mapeo por dominio")
    L.append("")
    L.append("| Dominio del examen | Peso | Partes del programa | Cobertura | Notas |")
    L.append("|---|---:|---|---:|---|")
    for d in cert["dominios"]:
        notas = d["notas"].replace("|", "/")
        L.append(f"| {d['nombre']} | {d['peso']}% | Parte {d['partes']} | {d['cobertura']}% | {notas} |")
    L.append(f"| **Total ponderado** | **100%** | | **{total:.0f}%** | |")
    L.append("")
    L.append("## 🎯 Brecha y cómo cerrarla")
    L.append("")
    L.append(cert["brecha"])
    L.append("")
    L.append("## 🧭 Ruta sugerida")
    L.append("")
    L.append(f"{cert['ruta']} Ver [rutas por rol](../rutas/README.md) y la "
             f"[Parte 16 — preparación de certificaciones](../classes/parte-16-capstones-y-preparacion-de-certificaciones/README.md).")
    L.append("")
    L.append("---")
    L.append("")
    L.append("> ⚠️ Mapeo orientativo, no avalado por el proveedor. La cobertura del temario no "
             "garantiza aprobar: las certificaciones prácticas requieren laboratorios y experiencia.")
    L.append("")
    return "\n".join(L)


def indice(data) -> str:
    L = []
    L.append("# 🎓 Certificaciones")
    L.append("")
    L.append("Cómo se alinea el **Programa de Ciberseguridad Moderna** con las certificaciones "
             "más relevantes. Para cada una se cruza **cada dominio oficial del examen** con las "
             "**partes/clases** que lo cubren y se calcula un **porcentaje de cobertura ponderado** "
             "por el peso del dominio en el examen.")
    L.append("")
    L.append(data["meta"]["descripcion"])
    L.append("")
    L.append("| Certificación | Código | Nivel | Cobertura estimada | Detalle |")
    L.append("|---|---|---|---|---|")
    for c in data["certs"]:
        total = cobertura_total(c)
        L.append(f"| {c['nombre']} | {c['codigo']} | {c['nivel']} | "
                 f"`{barra(total)}` {total:.0f}% | [ver mapeo]({c['id']}.md) |")
    L.append("")
    L.append("## ¿Cómo se calcula la cobertura?")
    L.append("")
    L.append("Para cada dominio del examen se estima, de forma honesta, en qué grado el programa "
             "prepara ese dominio (0–100%). El total es la **media ponderada** por el peso oficial "
             "de cada dominio: `Σ (peso_dominio × cobertura_dominio) / 100`. El cálculo se genera "
             "con [`scripts/generar_certis.py`](../scripts/generar_certis.py) a partir de "
             "[`_mapeo.json`](_mapeo.json), así que es reproducible y auditable.")
    L.append("")
    L.append("## Certificaciones mapeadas")
    L.append("")
    for c in data["certs"]:
        L.append(f"- **[{c['nombre']} ({c['codigo']})]({c['id']}.md)** — {c['nivel']}.")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"> {data['meta']['disclaimer']}")
    L.append("")
    return "\n".join(L)


def main():
    with open(os.path.join(DIR, "_mapeo.json"), encoding="utf-8") as f:
        data = json.load(f)
    escribir(os.path.join(DIR, "README.md"), indice(data))
    for c in data["certs"]:
        escribir(os.path.join(DIR, f"{c['id']}.md"), doc_cert(c))
    print(f"Certificaciones generadas: {len(data['certs'])} docs + índice.")
    for c in data["certs"]:
        print(f"  {c['codigo']:14s} -> {cobertura_total(c):.0f}%")


if __name__ == "__main__":
    main()
