#!/usr/bin/env python3
"""Calculadora CVSS v3.1 y v4.0 para entender de dónde sale un número.

CVSS (Common Vulnerability Scoring System, mantenido por FIRST) convierte un
*vector* —una cadena como `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`— en una
puntuación de 0.0 a 10.0. Este módulo implementa las dos versiones vigentes para
que puedas ver cada paso del cálculo en vez de confiar en una web:

  v3.1  Fórmulas cerradas (especificación oficial, sección 7).
        https://www.first.org/cvss/v3.1/specification-document
  v4.0  No hay fórmula cerrada: cada vector cae en un «macrovector» de 6
        niveles (EQ1..EQ6), una tabla da la puntuación de ese macrovector y se
        interpola según lo cerca que esté el vector del siguiente nivel.
        https://www.first.org/cvss/v4.0/specification-document

Lo que CVSS mide y lo que NO mide (importante para las clases 368 y 369):
  - Mide la SEVERIDAD técnica de una vulnerabilidad bajo ciertos supuestos.
  - NO mide el riesgo para tu organización, ni la probabilidad de que se
    explote (eso es EPSS), ni si ya se explota (eso es CISA KEV).
  - Dos fuentes legítimas pueden puntuar la misma vulnerabilidad distinto
    (el CNA que la reportó y el NVD) porque asumen contextos distintos.

El algoritmo de v4.0 y sus tablas son un port a Python de la calculadora oficial
de FIRST (https://github.com/FIRSTdotorg/cvss-v4-calculator, BSD-2-Clause,
Copyright (c) 2023 FIRST.ORG, Inc., Red Hat, and contributors). Las tablas están
en `datos/cvss4/tablas-cvss-v4.json`; su licencia, en la misma carpeta.

Solo biblioteca estándar. Uso:

    python cvss.py "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
    python cvss.py "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N" --explicar
    python cvss.py "CVSS:3.1/..." --json
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RUTA_TABLAS_V4 = os.path.join(AQUI, "datos", "cvss4", "tablas-cvss-v4.json")


class VectorInvalido(ValueError):
    """El vector no cumple la especificación (métrica desconocida, valor inválido, faltante...)."""


def severidad(puntuacion: float) -> str:
    """Escala cualitativa común a v3.1 y v4.0 (tabla 14 de la especificación v3.1)."""
    if puntuacion == 0:
        return "None"
    if puntuacion < 4.0:
        return "Low"
    if puntuacion < 7.0:
        return "Medium"
    if puntuacion < 9.0:
        return "High"
    return "Critical"


def _partir(vector: str) -> tuple[str, list[tuple[str, str]]]:
    """Separa «CVSS:3.1/AV:N/...» en la versión y los pares (métrica, valor)."""
    if not isinstance(vector, str) or "/" not in vector:
        raise VectorInvalido("El vector debe empezar por «CVSS:3.1/» o «CVSS:4.0/»")
    cabecera, *resto = vector.strip().split("/")
    if not cabecera.startswith("CVSS:"):
        raise VectorInvalido("Falta el prefijo «CVSS:x.y»")
    version = cabecera[5:]
    pares = []
    for trozo in resto:
        if ":" not in trozo:
            raise VectorInvalido(f"Métrica mal formada: {trozo!r}")
        k, v = trozo.split(":", 1)
        pares.append((k, v))
    return version, pares


def _validar(pares: list[tuple[str, str]], validos: dict[str, list[str]], obligatorias: tuple[str, ...]) -> dict[str, str]:
    metricas: dict[str, str] = {}
    for k, v in pares:
        if k not in validos:
            raise VectorInvalido(f"Métrica desconocida: {k}")
        if k in metricas:
            raise VectorInvalido(f"Métrica repetida: {k}")
        if v not in validos[k]:
            raise VectorInvalido(f"Valor inválido para {k}: {v!r} (válidos: {', '.join(validos[k])})")
        metricas[k] = v
    faltan = [m for m in obligatorias if m not in metricas]
    if faltan:
        raise VectorInvalido(f"Faltan métricas obligatorias: {', '.join(faltan)}")
    return metricas


# ==========================================================================
# CVSS v3.1
# ==========================================================================
# Valores permitidos por métrica. «X» = «Not Defined»: la métrica opcional no se evaluó.
V31_VALIDOS: dict[str, list[str]] = {
    "AV": ["N", "A", "L", "P"], "AC": ["L", "H"], "PR": ["N", "L", "H"], "UI": ["N", "R"],
    "S": ["U", "C"], "C": ["H", "L", "N"], "I": ["H", "L", "N"], "A": ["H", "L", "N"],
    "E": ["X", "H", "F", "P", "U"], "RL": ["X", "U", "W", "T", "O"], "RC": ["X", "C", "R", "U"],
    "CR": ["X", "H", "M", "L"], "IR": ["X", "H", "M", "L"], "AR": ["X", "H", "M", "L"],
    "MAV": ["X", "N", "A", "L", "P"], "MAC": ["X", "L", "H"], "MPR": ["X", "N", "L", "H"],
    "MUI": ["X", "N", "R"], "MS": ["X", "U", "C"], "MC": ["X", "H", "L", "N"],
    "MI": ["X", "H", "L", "N"], "MA": ["X", "H", "L", "N"],
}
V31_BASE = ("AV", "AC", "PR", "UI", "S", "C", "I", "A")
V31_TEMPORAL = ("E", "RL", "RC")
V31_ENTORNO = ("CR", "IR", "AR", "MAV", "MAC", "MPR", "MUI", "MS", "MC", "MI", "MA")

# Pesos numéricos (tabla 16 de la especificación). Son el corazón del cálculo:
# cada letra del vector se traduce en uno de estos números.
PESO_AV = {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2}
PESO_AC = {"L": 0.77, "H": 0.44}
PESO_UI = {"N": 0.85, "R": 0.62}
PESO_CIA = {"H": 0.56, "L": 0.22, "N": 0.0}
# PR depende del alcance (Scope): si el ataque cambia de dominio de seguridad, exigir
# privilegios «bajos» o «altos» pesa menos porque el atacante ya salta una barrera.
PESO_PR = {"U": {"N": 0.85, "L": 0.62, "H": 0.27}, "C": {"N": 0.85, "L": 0.68, "H": 0.5}}
PESO_E = {"X": 1.0, "H": 1.0, "F": 0.97, "P": 0.94, "U": 0.91}
PESO_RL = {"X": 1.0, "U": 1.0, "W": 0.97, "T": 0.96, "O": 0.95}
PESO_RC = {"X": 1.0, "C": 1.0, "R": 0.96, "U": 0.92}
PESO_REQ = {"X": 1.0, "H": 1.5, "M": 1.0, "L": 0.5}


def roundup(x: float) -> float:
    """«Roundup» de CVSS v3.1 (apéndice A): redondea HACIA ARRIBA a un decimal.

    Se pasa por un entero de 5 decimales para esquivar el error de coma flotante:
    en binario 0.1+0.2 vale 0.30000000000000004, y un redondeo ingenuo hacia
    arriba lo convertiría en 0.4. Truncar a 5 decimales antes lo evita.
    """
    entero = int(math.floor(x * 100000 + 0.5))
    if entero % 10000 == 0:
        return entero / 100000.0
    return (math.floor(entero / 10000) + 1) / 10.0


def _ajustar(m: dict[str, str], base: str) -> str:
    """Métrica modificada (MAV...) si está definida; si no, la base. Así funciona el entorno."""
    mod = m.get("M" + base, "X")
    return m[base] if mod == "X" else mod


def puntuar_v31(vector: str) -> dict:
    """Calcula base, temporal y ambiental de un vector CVSS v3.1."""
    version, pares = _partir(vector)
    if version != "3.1":
        raise VectorInvalido(f"Este cálculo es para CVSS:3.1 (recibido CVSS:{version})")
    m = _validar(pares, V31_VALIDOS, V31_BASE)
    pasos: list[str] = []

    # --- Base ---------------------------------------------------------------
    # ISS (Impact Sub-Score): cuánto se pierde en confidencialidad, integridad
    # y disponibilidad. La fórmula 1-(1-C)(1-I)(1-A) crece rápido con el primer
    # impacto alto y poco con los siguientes: perder las tres a la vez no es el triple.
    c, i, a = PESO_CIA[m["C"]], PESO_CIA[m["I"]], PESO_CIA[m["A"]]
    iss = 1 - (1 - c) * (1 - i) * (1 - a)
    cambiado = m["S"] == "C"
    impacto = 7.52 * (iss - 0.029) - 3.25 * (iss - 0.02) ** 15 if cambiado else 6.42 * iss
    explotabilidad = 8.22 * PESO_AV[m["AV"]] * PESO_AC[m["AC"]] * PESO_PR[m["S"]][m["PR"]] * PESO_UI[m["UI"]]
    if impacto <= 0:
        base = 0.0
    elif cambiado:
        base = roundup(min(1.08 * (impacto + explotabilidad), 10))
    else:
        base = roundup(min(impacto + explotabilidad, 10))
    pasos += [
        f"Pesos: AV={PESO_AV[m['AV']]} AC={PESO_AC[m['AC']]} PR={PESO_PR[m['S']][m['PR']]} UI={PESO_UI[m['UI']]} C={c} I={i} A={a}",
        f"ISS = 1 - (1-{c})(1-{i})(1-{a}) = {iss:.4f}",
        f"Impacto = {'7.52×(ISS-0.029) - 3.25×(ISS-0.02)^15' if cambiado else '6.42×ISS'} = {impacto:.4f}",
        f"Explotabilidad = 8.22×AV×AC×PR×UI = {explotabilidad:.4f}",
        f"Base = {'Roundup(min(1.08×(Impacto+Explotabilidad), 10))' if cambiado else 'Roundup(min(Impacto+Explotabilidad, 10))'} = {base}"
        if impacto > 0 else "Impacto <= 0  =>  Base = 0",
    ]

    resultado = {
        "version": "3.1", "vector": _canonico_v31(m), "base": base, "severidad_base": severidad(base),
        "impacto": round(impacto, 4), "explotabilidad": round(explotabilidad, 4),
        "temporal": None, "ambiental": None,
    }

    # --- Temporal -----------------------------------------------------------
    # Ajusta la base según cuánto se ha madurado la explotación (E), si hay
    # corrección (RL) y cuánta confianza hay en el informe (RC).
    e, rl, rc = (m.get(k, "X") for k in V31_TEMPORAL)
    tiene_temporal = any(m.get(k, "X") != "X" for k in V31_TEMPORAL)
    factor_t = PESO_E[e] * PESO_RL[rl] * PESO_RC[rc]
    if tiene_temporal:
        resultado["temporal"] = roundup(base * factor_t)
        pasos.append(f"Temporal = Roundup(Base × E × RL × RC) = Roundup({base} × {factor_t:.4f}) = {resultado['temporal']}")

    # --- Ambiental ----------------------------------------------------------
    # Rehace el cálculo con lo que sabe TU organización: qué importan C/I/A para
    # tu activo (requisitos) y cómo se modifica el ataque en tu entorno.
    tiene_entorno = any(m.get(k, "X") != "X" for k in V31_ENTORNO)
    if tiene_entorno:
        ms = _ajustar(m, "S")
        mc = PESO_CIA[_ajustar(m, "C")]
        mi = PESO_CIA[_ajustar(m, "I")]
        ma = PESO_CIA[_ajustar(m, "A")]
        miss = min(1 - (1 - PESO_REQ[m.get("CR", "X")] * mc) * (1 - PESO_REQ[m.get("IR", "X")] * mi)
                   * (1 - PESO_REQ[m.get("AR", "X")] * ma), 0.915)
        mod_cambiado = ms == "C"
        # Nota: aquí el exponente es 13 (en v3.0 era 15) y MISS se multiplica por 0.9731.
        mod_impacto = 7.52 * (miss - 0.029) - 3.25 * (miss * 0.9731 - 0.02) ** 13 if mod_cambiado else 6.42 * miss
        mod_expl = 8.22 * PESO_AV[_ajustar(m, "AV")] * PESO_AC[_ajustar(m, "AC")] \
            * PESO_PR[ms][_ajustar(m, "PR")] * PESO_UI[_ajustar(m, "UI")]
        if mod_impacto <= 0:
            amb = 0.0
        else:
            suma = 1.08 * (mod_impacto + mod_expl) if mod_cambiado else mod_impacto + mod_expl
            amb = roundup(roundup(min(suma, 10)) * factor_t)
        resultado["ambiental"] = amb
        pasos.append(f"Ambiental: MISS={miss:.4f} ImpactoMod={mod_impacto:.4f} ExplotabilidadMod={mod_expl:.4f} => {amb}")

    final = resultado["ambiental"] if resultado["ambiental"] is not None else (
        resultado["temporal"] if resultado["temporal"] is not None else base)
    resultado["puntuacion"] = final
    resultado["severidad"] = severidad(final)
    resultado["nomenclatura"] = "CVSS-" + "B" + ("T" if tiene_temporal else "") + ("E" if tiene_entorno else "")
    resultado["pasos"] = pasos
    return resultado


def _canonico_v31(m: dict[str, str]) -> str:
    orden = V31_BASE + V31_TEMPORAL + V31_ENTORNO
    return "CVSS:3.1/" + "/".join(f"{k}:{m[k]}" for k in orden if k in m)


# ==========================================================================
# CVSS v4.0
# ==========================================================================
_TABLAS_V4: dict | None = None


def _tablas_v4() -> dict:
    global _TABLAS_V4
    if _TABLAS_V4 is None:
        with open(RUTA_TABLAS_V4, encoding="utf-8") as fh:
            _TABLAS_V4 = json.load(fh)
    return _TABLAS_V4


V40_BASE = ("AV", "AC", "AT", "PR", "UI", "VC", "VI", "VA", "SC", "SI", "SA")

# «Distancia de severidad» de cada valor respecto al peor caso de su macrovector.
# Valores más altos = menos severo. Se tomaron tal cual de la calculadora oficial.
NIVEL = {
    "AV": {"N": 0.0, "A": 0.1, "L": 0.2, "P": 0.3},
    "PR": {"N": 0.0, "L": 0.1, "H": 0.2},
    "UI": {"N": 0.0, "P": 0.1, "A": 0.2},
    "AC": {"L": 0.0, "H": 0.1},
    "AT": {"N": 0.0, "P": 0.1},
    "VC": {"H": 0.0, "L": 0.1, "N": 0.2},
    "VI": {"H": 0.0, "L": 0.1, "N": 0.2},
    "VA": {"H": 0.0, "L": 0.1, "N": 0.2},
    "SC": {"H": 0.1, "L": 0.2, "N": 0.3},
    "SI": {"S": 0.0, "H": 0.1, "L": 0.2, "N": 0.3},
    "SA": {"S": 0.0, "H": 0.1, "L": 0.2, "N": 0.3},
    "CR": {"H": 0.0, "M": 0.1, "L": 0.2},
    "IR": {"H": 0.0, "M": 0.1, "L": 0.2},
    "AR": {"H": 0.0, "M": 0.1, "L": 0.2},
}


def _efectivo(m: dict[str, str], metrica: str) -> str:
    """Valor que realmente se usa al puntuar una métrica (equivale a `m()` de la calculadora oficial).

    - E sin definir se trata como «A» (explotación activa): peor caso razonable.
    - CR, IR, AR sin definir se tratan como «H» (requisito alto).
    - Una métrica modificada (MAV, MSC...) sustituye a la base cuando está definida.
    """
    valor = m[metrica]
    if metrica == "E" and valor == "X":
        return "A"
    if metrica in ("CR", "IR", "AR") and valor == "X":
        return "H"
    mod = m.get("M" + metrica)
    if mod is not None and mod != "X":
        return mod
    return valor


def _macrovector(m: dict[str, str]) -> str:
    """Clasifica el vector en 6 «equivalence classes» (EQ1..EQ6) y devuelve p. ej. «001001»."""
    e = lambda k: _efectivo(m, k)  # noqa: E731
    # EQ1: ¿qué tan fácil es llegar al sistema? (vector de red, privilegios, interacción)
    if e("AV") == "N" and e("PR") == "N" and e("UI") == "N":
        eq1 = 0
    elif (e("AV") == "N" or e("PR") == "N" or e("UI") == "N") and e("AV") != "P":
        eq1 = 1
    else:
        eq1 = 2
    # EQ2: ¿exige condiciones especiales o una condición del objetivo?
    eq2 = 0 if (e("AC") == "L" and e("AT") == "N") else 1
    # EQ3: impacto en el propio sistema vulnerable (confidencialidad e integridad altas)
    if e("VC") == "H" and e("VI") == "H":
        eq3 = 0
    elif e("VC") == "H" or e("VI") == "H" or e("VA") == "H":
        eq3 = 1
    else:
        eq3 = 2
    # EQ4: impacto en sistemas subsecuentes, o seguridad física (Safety) del entorno
    if m.get("MSI") == "S" or m.get("MSA") == "S":
        eq4 = 0
    elif e("SC") == "H" or e("SI") == "H" or e("SA") == "H":
        eq4 = 1
    else:
        eq4 = 2
    # EQ5: madurez de la explotación (Threat)
    eq5 = {"A": 0, "P": 1, "U": 2}[e("E")]
    # EQ6: ¿un impacto alto coincide con un requisito de seguridad alto en el mismo eje?
    alto = (e("CR") == "H" and e("VC") == "H") or (e("IR") == "H" and e("VI") == "H") or (e("AR") == "H" and e("VA") == "H")
    eq6 = 0 if alto else 1
    return f"{eq1}{eq2}{eq3}{eq4}{eq5}{eq6}"


def _vector_a_dict(texto: str) -> dict[str, str]:
    return dict(p.split(":", 1) for p in texto.rstrip("/").split("/"))


def puntuar_v40(vector: str) -> dict:
    """Calcula la puntuación CVSS v4.0 (algoritmo oficial de FIRST, portado)."""
    t = _tablas_v4()
    version, pares = _partir(vector)
    if version != "4.0":
        raise VectorInvalido(f"Este cálculo es para CVSS:4.0 (recibido CVSS:{version})")
    m = _validar(pares, t["orden_metricas"], V40_BASE)
    # Las métricas opcionales ausentes equivalen a «X» (no definidas).
    for k in t["orden_metricas"]:
        m.setdefault(k, "X")

    macro = _macrovector(m)
    tabla = t["tabla_macrovectores"]
    resultado = {
        "version": "4.0", "vector": _canonico_v40(m, t["orden_metricas"]), "macrovector": macro,
        "equivalencias": {f"EQ{n + 1}": int(d) for n, d in enumerate(macro)},
        "nomenclatura": _nomenclatura_v40(m),
    }

    # Excepción oficial: si no hay impacto en ningún eje, la puntuación es 0.
    if all(_efectivo(m, k) == "N" for k in ("VC", "VI", "VA", "SC", "SI", "SA")):
        resultado.update(puntuacion=0.0, severidad="None")
        return resultado

    valor = tabla[macro]
    eq = [int(d) for d in macro]

    def siguiente(i: int, delta: int = 1) -> str:
        """Macrovector «un nivel menos severo» en el EQ i (0-based), o '' si no se puede."""
        lista = list(macro)
        lista[i] = str(eq[i] + delta)
        return "".join(lista)

    def puntuacion_de(clave: str) -> float | None:
        return tabla.get(clave)

    # EQ3 y EQ6 están acoplados (no todas las combinaciones existen), por eso su «siguiente» es especial.
    eq1_sig = puntuacion_de(siguiente(0))
    eq2_sig = puntuacion_de(siguiente(1))
    if eq[2] == 1 and eq[5] == 1:
        eq36_sig = puntuacion_de(siguiente(2))
    elif eq[2] == 0 and eq[5] == 1:
        eq36_sig = puntuacion_de(siguiente(2))
    elif eq[2] == 1 and eq[5] == 0:
        eq36_sig = puntuacion_de(siguiente(5))
    elif eq[2] == 0 and eq[5] == 0:
        izquierda = puntuacion_de(siguiente(5))
        derecha = puntuacion_de(siguiente(2))
        # Hay dos caminos posibles; la calculadora oficial toma el de mayor puntuación.
        if izquierda is not None and derecha is not None:
            eq36_sig = izquierda if izquierda > derecha else derecha
        else:
            eq36_sig = izquierda if izquierda is not None else derecha
    else:
        lista = list(macro)
        lista[2], lista[5] = str(eq[2] + 1), str(eq[5] + 1)
        eq36_sig = puntuacion_de("".join(lista))
    eq4_sig = puntuacion_de(siguiente(3))
    eq5_sig = puntuacion_de(siguiente(4))

    # Vectores «peores» (de máxima severidad) dentro de este macrovector: contra ellos se mide la distancia.
    mc = t["maximos_compuestos"]
    eq1_max, eq2_max = mc["eq1"][macro[0]], mc["eq2"][macro[1]]
    eq36_max = mc["eq3"][macro[2]][macro[5]]
    eq4_max, eq5_max = mc["eq4"][macro[3]], mc["eq5"][macro[4]]
    candidatos = [a + b + c + d + e for a in eq1_max for b in eq2_max for c in eq36_max for d in eq4_max for e in eq5_max]

    distancia: dict[str, float] = {}
    for candidato in candidatos:
        maximo = _vector_a_dict(candidato)
        distancia = {k: NIVEL[k][_efectivo(m, k)] - NIVEL[k][maximo[k]] for k in NIVEL}
        if all(d >= 0 for d in distancia.values()):
            break  # el primero cuyo vector no es «más severo» que el evaluado

    d1 = distancia["AV"] + distancia["PR"] + distancia["UI"]
    d2 = distancia["AC"] + distancia["AT"]
    d36 = sum(distancia[k] for k in ("VC", "VI", "VA", "CR", "IR", "AR"))
    d4 = distancia["SC"] + distancia["SI"] + distancia["SA"]

    paso = 0.1
    sev = t["severidad_maxima"]
    max1 = sev["eq1"][macro[0]] * paso
    max2 = sev["eq2"][macro[1]] * paso
    max36 = sev["eq3eq6"][macro[2]][macro[5]] * paso
    max4 = sev["eq4"][macro[3]] * paso

    # Para cada EQ: (puntos que se pierden al bajar al siguiente nivel) × (fracción del camino recorrido).
    existentes = 0
    suma = 0.0
    for sig, dist, maxim in ((eq1_sig, d1, max1), (eq2_sig, d2, max2), (eq36_sig, d36, max36), (eq4_sig, d4, max4)):
        if sig is not None:
            existentes += 1
            suma += (valor - sig) * (dist / maxim)
    if eq5_sig is not None:
        existentes += 1  # EQ5 siempre aporta fracción 0, pero cuenta en el promedio
    media = suma / existentes if existentes else 0.0

    final = min(max(valor - media, 0.0), 10.0)
    final = math.floor(final * 10 + 0.5) / 10  # redondeo «half up», como Math.round en la calculadora oficial
    resultado.update(puntuacion=final, severidad=severidad(final), valor_macrovector=valor)
    return resultado


def _nomenclatura_v40(m: dict[str, str]) -> str:
    """CVSS-B / -BT / -BE / -BTE: qué grupos de métricas se usaron (sección 1.1 de la especificación)."""
    amenaza = m.get("E", "X") != "X"
    entorno = any(m.get(k, "X") != "X" for k in ("CR", "IR", "AR", "MAV", "MAC", "MAT", "MPR", "MUI", "MVC", "MVI", "MVA", "MSC", "MSI", "MSA"))
    return "CVSS-B" + ("T" if amenaza else "") + ("E" if entorno else "")


def _canonico_v40(m: dict[str, str], orden: dict[str, list[str]]) -> str:
    return "CVSS:4.0/" + "/".join(f"{k}:{m[k]}" for k in orden if m.get(k, "X") != "X" or k in V40_BASE)


# ==========================================================================
# Interfaz común
# ==========================================================================
def puntuar(vector: str) -> dict:
    """Detecta la versión y calcula. Es lo que usan el priorizador y las pruebas."""
    version, _ = _partir(vector)
    if version == "3.1":
        return puntuar_v31(vector)
    if version == "4.0":
        return puntuar_v40(vector)
    raise VectorInvalido(f"Versión no soportada: CVSS:{version} (este módulo calcula 3.1 y 4.0)")


def main(argv: list[str] | None = None) -> int:
    for flujo in (sys.stdout, sys.stderr):
        if hasattr(flujo, "reconfigure"):
            flujo.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Calcula la puntuación de un vector CVSS v3.1 o v4.0.")
    ap.add_argument("vector")
    ap.add_argument("--explicar", action="store_true", help="muestra el cálculo paso a paso (v3.1) o el macrovector (v4.0)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        r = puntuar(a.vector)
    except VectorInvalido as exc:
        print(f"Vector inválido: {exc}", file=sys.stderr)
        return 1
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return 0
    print(f"{r['vector']}")
    if r["version"] == "3.1":
        print(f"Base: {r['base']} ({r['severidad_base']})   Temporal: {r['temporal']}   Ambiental: {r['ambiental']}")
        print(f"Puntuación final: {r['puntuacion']} ({r['severidad']})  [{r['nomenclatura']}]")
        if a.explicar:
            print("\nPaso a paso:")
            for p in r["pasos"]:
                print("  " + p)
    else:
        print(f"Puntuación: {r['puntuacion']} ({r['severidad']})  [{r['nomenclatura']}]  macrovector {r['macrovector']}")
        if a.explicar:
            print("\nNiveles de equivalencia (0 = más severo):")
            for k, v in r["equivalencias"].items():
                print(f"  {k} = {v}")
            print(f"Puntuación del macrovector en la tabla oficial: {r.get('valor_macrovector', '-')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
