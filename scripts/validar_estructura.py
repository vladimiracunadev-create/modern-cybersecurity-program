#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Valida la integridad del currículo del Programa de Ciberseguridad Moderna.

Comprueba:
  1. Cada parte (classes/parte-*/) tiene su README.md.
  2. Cada carpeta de clase (classes/parte-*/NNN-slug/) tiene su README.md no trivial.
  3. La numeración de clases es secuencial y sin huecos (001..N).
  4. Todos los enlaces internos a archivos .md resuelven (no hay enlaces rotos).

Sobre el punto 4: se revisa **todo el repositorio**, no solo classes/, y se
aceptan las tres formas de escribir un enlace relativo —`../otra/README.md`,
`./otra/README.md` y `otra/README.md`—. La versión anterior exigía el prefijo `./` o
`../`, así que un enlace a una clase hermana escrito sin prefijo quedaba fuera
del recuento: resolvía a `clase-actual/otra-clase/README.md`, que no existe, y
el CI lo daba por bueno. Se detectaron 14 enlaces rotos así.

Uso:  python scripts/validar_estructura.py
Salida: código 0 si todo está bien; 1 si hay errores (para CI).
"""
from __future__ import annotations
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLASSES = os.path.join(ROOT, "classes")
MIN_BYTES = 400  # un README real es mucho mayor; esto detecta stubs vacíos

# Enlaces a un .md, con o sin ancla. NO se exige el prefijo `./` o `../`: el
# enlace a una clase hermana se escribe a menudo sin el, y esa es justamente la
# forma que se colaba sin revisar.
LINK_RE = re.compile(r"\]\(([^)\s]+?\.md)(?:#[^)]*)?\)")
# Enlaces que no apuntan a un fichero del repositorio y no hay que resolver.
LINK_EXTERNO = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|//|/)")
# Arboles que no se revisan: salida generada (site/), dependencias y binarios
# de la app movil. Su markdown no es fuente, es producto.
EXCLUIR = {".git", "node_modules", "site", "dist", "dist-web", "__pycache__"}

# Secciones que TODA clase debe incluir (robustez pedagógica).
SECCIONES_REQUERIDAS = [
    "## 🎯 Objetivo",
    "## 📚 Resultados de aprendizaje",
    "## ⚠️ Errores comunes",
    "## ❓ Preguntas frecuentes",
    "## 🔗 Referencias",
    "## ⬅️ Clase anterior",
    "## ➡️ Siguiente clase",
]

# Secciones del estandar pedagogico profundo. Se exigen solo en las partes ya
# migradas: el enriquecimiento avanza por partes y no tendria sentido poner el
# CI en rojo por las que aun no han pasado por el.
SECCIONES_PROFUNDAS = [
    "## 🧠 Explicación en profundidad",
    "## 📔 Glosario",
    "```mermaid",
]
PARTES_ESTANDAR_PROFUNDO = (
    "parte-0-fundamentos-y-prerrequisitos",
    "parte-1-redes-y-seguridad-de-redes",
    "parte-2-criptografia-aplicada",
    "parte-3-hacking-etico-y-pentesting-metodologia",
    "parte-4-seguridad-de-aplicaciones-web",
    "parte-5-explotacion-de-sistemas-y-binarios",
    "parte-6-analisis-de-malware",
    "parte-7-red-team-y-operaciones-ofensivas",
    "parte-8-blue-team-deteccion-y-soc",
)


def main() -> int:
    errores: list[str] = []
    nums: list[int] = []
    n_partes = 0
    n_clases = 0

    if not os.path.isdir(CLASSES):
        print("ERROR: no existe el directorio classes/")
        return 1

    for parte in sorted(os.listdir(CLASSES)):
        pdir = os.path.join(CLASSES, parte)
        if not (os.path.isdir(pdir) and parte.startswith("parte-")):
            continue
        n_partes += 1
        if not os.path.isfile(os.path.join(pdir, "README.md")):
            errores.append(f"Falta README de parte: {parte}/README.md")

        for clase in sorted(os.listdir(pdir)):
            cdir = os.path.join(pdir, clase)
            if not os.path.isdir(cdir):
                continue
            n_clases += 1
            m = re.match(r"^(\d{3})-", clase)
            if m:
                nums.append(int(m.group(1)))
            readme = os.path.join(cdir, "README.md")
            if not os.path.isfile(readme):
                errores.append(f"Falta README de clase: {parte}/{clase}/README.md")
            elif os.path.getsize(readme) < MIN_BYTES:
                errores.append(f"README demasiado corto (<{MIN_BYTES} B): {parte}/{clase}/README.md")
            else:
                contenido = open(readme, encoding="utf-8").read()
                exigidas = list(SECCIONES_REQUERIDAS)
                if parte in PARTES_ESTANDAR_PROFUNDO:
                    exigidas += SECCIONES_PROFUNDAS
                faltan = [s for s in exigidas if s not in contenido]
                if faltan:
                    errores.append(
                        f"Secciones faltantes en {parte}/{clase}/README.md: "
                        + ", ".join(f'"{s}"' for s in faltan)
                    )

    # numeración secuencial
    nums.sort()
    if nums:
        esperado = list(range(1, len(nums) + 1))
        if nums != esperado:
            faltan = sorted(set(esperado) - set(nums))
            dup = sorted({x for x in nums if nums.count(x) > 1})
            if faltan:
                errores.append(f"Huecos en la numeracion de clases: {faltan}")
            if dup:
                errores.append(f"Numeros de clase duplicados: {dup}")

    # enlaces internos .md, en todo el repositorio
    enlaces = 0
    rotos = 0
    ficheros_md = 0
    for cur, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUIR]
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(cur, fn)
            ficheros_md += 1
            with open(p, encoding="utf-8") as fh:
                txt = fh.read()
            for mm in LINK_RE.finditer(txt):
                destino = mm.group(1)
                if LINK_EXTERNO.match(destino):
                    continue
                enlaces += 1
                # normpath resuelve los `..` sin tocar el disco; ademas evita
                # pasarle a Windows una ruta larga con segmentos `..` dentro,
                # que os.path.exists rechaza aunque el fichero exista.
                tgt = os.path.normpath(os.path.join(cur, destino))
                if not os.path.exists(tgt):
                    rotos += 1
                    errores.append(f"Enlace roto en {os.path.relpath(p, ROOT)} -> {destino}")

    print("== Validacion del Programa de Ciberseguridad Moderna ==")
    print(f"Partes encontradas : {n_partes}")
    print(f"Clases encontradas : {n_clases}")
    print(f"Ficheros .md revisados: {ficheros_md}")
    print(f"Enlaces .md revisados: {enlaces} (rotos: {rotos})")

    if errores:
        print(f"\nFALLO: {len(errores)} problema(s):")
        for e in errores[:50]:
            print(f"  - {e}")
        if len(errores) > 50:
            print(f"  ... y {len(errores) - 50} mas")
        return 1

    print("\nOK: estructura y enlaces integros.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
