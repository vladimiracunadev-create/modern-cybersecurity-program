#!/usr/bin/env python3
"""Plazos de remediación de CISA BOD 26-04 como tabla de decisión.

BOD 26-04 («Prioritizing Security Updates Based on Risk», 10 de junio de 2026)
sustituye a BOD 22-01 y BOD 19-02. Es una directiva OBLIGATORIA solo para las
agencias civiles federales de EE. UU.; para cualquier otra organización es una
**referencia** útil porque publica, con números, cómo combinar cuatro señales:

  1. Exposición del activo   ¿es alcanzable desde redes públicas?   (la determina TU organización)
  2. KEV                     ¿el CVE está en el catálogo CISA KEV?   (evidencia de explotación)
  3. Automatizable           ¿un adversario puede automatizar todos los pasos de la explotación?
  4. Impacto técnico         control parcial o total del activo tras explotar

Los puntos 3 y 4 los publica CISA para cada CVE a través de su programa Vulnrichment
(metodología SSVC). El resultado es una tabla de 16 filas (2×2×2×2) que da el plazo
en días naturales. Este módulo la reproduce tal cual aparece en la directiva
(consultada el 2026-10-30) para que puedas ver cómo el MISMO CVE pasa de «3 días y
triaje forense» a «arreglar en la próxima actualización del sistema» solo cambiando
dónde está el activo.

Lo que NO es: una tabla de CVSS. CVSS no interviene; el «impacto técnico» de SSVC se
parece al concepto de severidad pero es una decisión distinta, con dos valores.

Sin dependencias. Uso:

    python bod2604.py --expuesto si --kev si --automatizable si --impacto total
"""
from __future__ import annotations

import argparse
import sys

# (expuesto, en_kev, automatizable, impacto) -> (días, requiere_triaje_forense) ; días None = «en la próxima actualización».
# Orden y valores: Table 1 de BOD 26-04, filas 1 a 16.
TABLA: dict[tuple[bool, bool, bool, str], tuple[int | None, bool]] = {
    (True, True, True, "total"): (3, True),       # fila 1
    (True, True, True, "partial"): (3, False),    # fila 2
    (True, True, False, "total"): (3, True),      # fila 3
    (True, True, False, "partial"): (14, False),  # fila 4
    (True, False, True, "total"): (3, False),     # fila 5
    (True, False, True, "partial"): (14, False),  # fila 6
    (True, False, False, "total"): (14, False),   # fila 7
    (True, False, False, "partial"): (60, False), # fila 8
    (False, True, True, "total"): (3, True),      # fila 9
    (False, True, True, "partial"): (14, False),  # fila 10
    (False, True, False, "total"): (14, False),   # fila 11
    (False, True, False, "partial"): (14, False), # fila 12
    (False, False, True, "total"): (60, False),   # fila 13
    (False, False, True, "partial"): (60, False), # fila 14
    (False, False, False, "total"): (None, False),   # fila 15
    (False, False, False, "partial"): (None, False), # fila 16
}

IMPACTOS = ("total", "partial")


def plazo(expuesto: bool, en_kev: bool, automatizable: bool, impacto: str) -> dict:
    """Plazo de referencia según BOD 26-04. `impacto` es «total» o «partial» (control sobre el activo)."""
    if impacto not in IMPACTOS:
        raise ValueError(f"impacto debe ser 'total' o 'partial', no {impacto!r}")
    dias, forense = TABLA[(bool(expuesto), bool(en_kev), bool(automatizable), impacto)]
    if dias is None:
        texto = "arreglar en la próxima actualización o reconstrucción mayor del sistema"
    else:
        texto = f"{dias} días naturales" + (" y triaje forense del activo" if forense else "")
    return {"dias": dias, "triaje_forense": forense, "texto": texto}


def plazo_de_hallazgo(exposicion: str, en_kev: bool, ssvc: dict | None) -> dict | None:
    """Plazo para un hallazgo del laboratorio, o None si faltan los datos SSVC de CISA.

    `exposicion` usa el vocabulario del laboratorio: «publica» cuenta como expuesto;
    «interna» y «no-alcanzable», no; «desconocida» se trata como expuesto, porque
    asumir lo mejor sin haberlo comprobado es el error que esta tabla existe para evitar.
    """
    if not ssvc or ssvc.get("impacto_tecnico") not in IMPACTOS or ssvc.get("automatizable") not in ("yes", "no"):
        return None
    expuesto = exposicion not in ("interna", "no-alcanzable")
    r = plazo(expuesto, en_kev, ssvc["automatizable"] == "yes", ssvc["impacto_tecnico"])
    r["supuesto_de_exposicion"] = exposicion == "desconocida"
    return r


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Plazo de remediación de referencia (CISA BOD 26-04).")
    ap.add_argument("--expuesto", choices=["si", "no"], required=True)
    ap.add_argument("--kev", choices=["si", "no"], required=True)
    ap.add_argument("--automatizable", choices=["si", "no"], required=True)
    ap.add_argument("--impacto", choices=list(IMPACTOS), required=True)
    a = ap.parse_args(argv)
    r = plazo(a.expuesto == "si", a.kev == "si", a.automatizable == "si", a.impacto)
    print(f"Plazo de referencia (BOD 26-04): {r['texto']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
