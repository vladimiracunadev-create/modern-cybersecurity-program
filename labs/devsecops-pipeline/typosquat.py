#!/usr/bin/env python3
"""Detecta posibles typosquats en las dependencias declaradas.

El *typosquatting* consiste en publicar un paquete con un nombre casi idéntico
al de uno popular —`requets` por `requests`, `python-dateutils` por
`python-dateutil`— esperando el error de tecleo de alguien, o de un modelo de
lenguaje que "recuerda" mal un nombre. El paquete falso se instala y ejecuta
código en tu máquina y en tu pipeline.

Es la capa que ninguna otra cubre: un escáner de vulnerabilidades busca CVE en
paquetes *conocidos*; un paquete malicioso recién publicado no tiene CVE, tiene
carga útil. Aquí no se busca una vulnerabilidad, se busca **una impostura**.

Método: distancia de Levenshtein contra una lista de paquetes muy descargados.
Es una heurística deliberadamente simple y con falsos positivos — su valor es
señalar candidatos para revisión humana, no dictar veredictos.

Sin dependencias externas: solo biblioteca estándar.

Uso:
    python typosquat.py repo-vulnerable/requirements.txt
    python typosquat.py repo-vulnerable/requirements.txt --distancia 2
"""
from __future__ import annotations

import argparse
import os
import re
import sys

# Paquetes de PyPI muy descargados, que son los que se suplantan. La lista es
# corta a propósito: en un entorno real se toma del top-N de descargas del
# índice, no de una constante en el código.
POPULARES = [
    "requests", "urllib3", "boto3", "botocore", "setuptools", "certifi",
    "charset-normalizer", "idna", "python-dateutil", "six", "numpy", "pandas",
    "cryptography", "pyyaml", "click", "jinja2", "markupsafe", "flask",
    "django", "sqlalchemy", "pytest", "packaging", "attrs", "colorama",
    "pillow", "protobuf", "google-api-core", "typing-extensions", "wheel",
    "pip", "virtualenv", "paramiko", "beautifulsoup4", "lxml", "scipy",
    "matplotlib", "werkzeug", "tqdm", "aiohttp", "httpx", "pydantic",
]

RE_DEP = re.compile(r"^\s*([A-Za-z0-9][A-Za-z0-9._-]*)\s*(?:[=<>!~]|$)")


def normalizar(nombre: str) -> str:
    """PyPI trata como equivalentes '-', '_' y '.', y no distingue mayúsculas."""
    return re.sub(r"[-_.]+", "-", nombre.strip().lower())


def levenshtein(a: str, b: str) -> int:
    """Número mínimo de ediciones (inserción, borrado, sustitución) entre a y b."""
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)

    previa = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        actual = [i]
        for j, cb in enumerate(b, start=1):
            actual.append(min(
                previa[j] + 1,                      # borrado
                actual[j - 1] + 1,                  # inserción
                previa[j - 1] + (ca != cb),         # sustitución
            ))
        previa = actual
    return previa[-1]


def leer_dependencias(ruta: str) -> list[str]:
    nombres: list[str] = []
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.strip()
            if not linea or linea.startswith("#"):
                continue
            m = RE_DEP.match(linea)
            if m:
                nombres.append(m.group(1))
    return nombres


def analizar(nombres: list[str], distancia_max: int) -> list[tuple[str, str, int]]:
    populares = {normalizar(p) for p in POPULARES}
    sospechosos: list[tuple[str, str, int]] = []

    for nombre in nombres:
        norma = normalizar(nombre)
        if norma in populares:
            continue  # es el paquete legítimo, no una imitación
        for popular in sorted(populares):
            # Nombres muy cortos generan ruido: se exige una longitud mínima.
            if len(norma) < 4 or len(popular) < 4:
                continue
            d = levenshtein(norma, popular)
            if 0 < d <= distancia_max:
                sospechosos.append((nombre, popular, d))
                break
    return sospechosos


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Detecta posibles typosquats en un requirements.txt.",
    )
    parser.add_argument("requirements", help="Ruta al archivo de dependencias.")
    parser.add_argument("--distancia", type=int, default=1,
                        help="Distancia máxima de Levenshtein (por defecto 1).")
    args = parser.parse_args()

    if not os.path.isfile(args.requirements):
        print(f"ERROR: no existe {args.requirements}", file=sys.stderr)
        return 1

    nombres = leer_dependencias(args.requirements)
    sospechosos = analizar(nombres, args.distancia)

    print(f"Dependencias analizadas: {len(nombres)}")
    print(f"Distancia máxima aplicada: {args.distancia}")
    print("")

    if not sospechosos:
        print("Sin candidatos a typosquat con este umbral.")
        print("")
        print("IMPORTANTE: esto NO significa que las dependencias sean legítimas.")
        print("La heurística solo compara contra una lista corta de paquetes")
        print("populares. Un paquete malicioso con nombre propio, que no imite a")
        print("ninguno conocido, es invisible para esta capa.")
        return 0

    print("Candidatos a revisión humana:")
    print("")
    for nombre, popular, d in sospechosos:
        print(f"  - '{nombre}' se parece a '{popular}' (distancia {d})")
    print("")
    print("Ninguno es un veredicto. Antes de concluir nada, comprueba en el índice:")
    print("  fecha de publicación, número de descargas, repositorio de origen,")
    print("  autor y si el paquete legítimo ya está también en tu lista.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
