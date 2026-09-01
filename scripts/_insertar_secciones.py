#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Inserta las secciones del estandar profundo en una clase.

Uso:
    python scripts/_insertar_secciones.py <README.md> <bloque.md>

<bloque.md> contiene, en este orden y con sus encabezados `##`:
    ## 🧠 Explicación en profundidad
    ...prosa y diagramas...
    ## 📔 Glosario
    ...tabla...

- La "Explicacion" se inserta antes de "## 📖 Definiciones y características".
- El "Glosario" se inserta antes de "## 🧰 Herramientas y preparación".

Idempotente: si la clase ya tiene esas secciones, avisa y no toca nada.
Herramienta interna de migracion; no forma parte del CI.
"""
from __future__ import annotations

import sys
from pathlib import Path

H_EXP = "## 🧠 Explicación en profundidad"
H_GLO = "## 📔 Glosario"
A_DEF = "## 📖 Definiciones y características"
A_HERR = "## 🧰 Herramientas y preparación"


def main() -> int:
    readme = Path(sys.argv[1])
    bloque = Path(sys.argv[2]).read_text(encoding="utf-8")

    if H_GLO not in bloque:
        print(f"BLOQUE-SIN-GLOSARIO: {sys.argv[2]}")
        return 4
    exp_part, glo_part = bloque.split(H_GLO, 1)
    exp_block = exp_part.strip() + "\n\n"
    glo_block = (H_GLO + glo_part).strip() + "\n\n"

    texto = readme.read_text(encoding="utf-8")
    if H_EXP in texto or H_GLO in texto:
        print(f"YA-MIGRADA: {readme}")
        return 0
    if A_DEF not in texto:
        print(f"SIN-ANCLA-DEFINICIONES: {readme}")
        return 2
    if A_HERR not in texto:
        print(f"SIN-ANCLA-HERRAMIENTAS: {readme}")
        return 3

    texto = texto.replace(A_DEF, exp_block + A_DEF, 1)
    texto = texto.replace(A_HERR, glo_block + A_HERR, 1)
    readme.write_text(texto, encoding="utf-8")
    print(f"OK: {readme}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
