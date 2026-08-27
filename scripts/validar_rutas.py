#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Valida el catalogo de rutas por rol y el ecosistema CISO.

`validar_estructura.py` ya comprueba que ningun enlace .md este roto. Lo que no
comprobaba es lo contrario: que una guia nueva **este enlazada desde algun
sitio**. Una ruta que existe y no aparece en el indice es invisible: no llega al
sitio publicado por navegacion, no la encuentra nadie y se queda sin mantener.
Tampoco miraba el ancla de los enlaces, asi que un `#seccion` mal escrito
dejaba al lector arriba de la pagina sin que nada lo detectara.

Comprueba:

  1. Ninguna guia de `rutas/` queda huerfana: todas estan enlazadas desde
     `rutas/README.md`.
  2. Toda guia enlaza de vuelta al indice (`README.md`).
  3. Cada guia trae las secciones obligatorias del formato de ruta.
  4. Las rutas del **ecosistema CISO** traen ademas las secciones propias de la
     ficha de cargo (capstone, entrevista, diferencias con los vecinos y fuentes
     con fecha) y enlazan el laboratorio ejecutivo y el centro del ecosistema.
  5. Los slugs son kebab-case en minusculas, sin acentos ni espacios.
  6. Toda referencia a una clase (`../classes/parte-*/NNN-slug/README.md`)
     apunta a una clase que existe, y su numero cae dentro del rango real del
     catalogo (001..N). No hay numeraciones inventadas.
  7. Los ficheros del laboratorio ejecutivo existen y estan enlazados desde el
     indice de laboratorios.
  8. Todo enlace con ancla (`fichero.md#seccion`) apunta a un encabezado que
     existe de verdad. Se revisa **todo el repositorio**, no solo rutas/.

Uso:  python scripts/validar_rutas.py
Salida: codigo 0 si todo esta bien; 1 si hay errores (para CI).
"""
from __future__ import annotations

import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUTAS = os.path.join(ROOT, "rutas")
CLASSES = os.path.join(ROOT, "classes")
LAB_CISO = os.path.join(ROOT, "labs", "ciso-leadership")

# Enlace a un .md, con o sin ancla. Misma expresion que validar_estructura.py.
LINK_RE = re.compile(r"\]\(([^)\s]+?\.md)(?:#[^)]*)?\)")
# Referencia a una clase dentro de un enlace relativo.
CLASE_RE = re.compile(r"classes/(parte-[^/]+)/(\d{3})-([^/)]+)/README\.md")
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Comprobacion de anclas (punto 8). Se recorre todo el repositorio.
LINK_ANCLA_RE = re.compile(r"\]\(([^)\s]+?\.md)#([^)\s]+)\)")
ENCABEZADO_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)
ANCLA_HTML_RE = re.compile(r'<a\s+id="([^"]+)"')
EXTERNO_RE = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|//|/)")
EXCLUIR_ARBOL = {".git", "node_modules", "site", "dist", "dist-web", "__pycache__"}

# Secciones que toda guia de ruta debe tener. Son las que ya comparten las 21
# guias que existian antes del ecosistema CISO: no se inventa un formato nuevo,
# se fija el que el repositorio ya usaba.
SECCIONES_RUTA = [
    "## 🧭 Qué es y por qué importa",
    "## 🧠 Qué necesitas saber",
    "## 📚 Tu ruta en el programa",
    "## 🎓 Certificaciones",
    "## 📈 Progresión de carrera y salario",
    "## ⚠️ Mitos y errores comunes",
]

# Guias del ecosistema CISO: ficha de cargo completa. El centro
# (ecosistema-ciso.md) es un indice, no una guia de cargo, y por eso queda fuera
# de esta lista y de SECCIONES_RUTA.
ECOSISTEMA = [
    "field-ciso.md",
    "vciso.md",
    "biso.md",
    "product-ciso.md",
    "ai-ciso.md",
    "ot-ciso.md",
]
SECCIONES_ECOSISTEMA = [
    "**Alias y variantes:**",
    "### Nivel de consolidación del título",
    "## 🏛️ Mandato, autoridad y responsabilidad",
    "## 🧾 Entregables verificables",
    "## 📏 KPI y KRI",
    "### Capstone",
    "## 🎤 Preguntas de entrevista",
    "## ↔️ Diferencias con los cargos vecinos",
    "## 📎 Fuentes y fecha de consulta",
]

# El centro del ecosistema tiene sus propias secciones obligatorias.
CENTRO = "ecosistema-ciso.md"
SECCIONES_CENTRO = [
    "## 🗺️ Mapa de cargos",
    "## 🧩 Las cuatro familias",
    "## 📊 Matriz comparativa central",
    "## 🧪 El test del mandato",
    "## 🧗 Rutas de progresión",
    "## 🇨🇱 Contexto chileno y latinoamericano",
    "## 📎 Fuentes y fecha de consulta",
]

LAB_FICHEROS = ("README.md", "ORGANIZACIONES.md", "PLANTILLAS.md", "EVALUACION.md")
LAB_ENLACE = "../labs/ciso-leadership/README.md"


def sin_acentos(t: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", t) if not unicodedata.combining(c))


def catalogo_clases() -> dict:
    """{numero: (parte_slug, clase_slug)} leido del disco, no de un manifiesto."""
    cat = {}
    if not os.path.isdir(CLASSES):
        return cat
    for parte in sorted(os.listdir(CLASSES)):
        pdir = os.path.join(CLASSES, parte)
        if not (os.path.isdir(pdir) and parte.startswith("parte-")):
            continue
        for clase in sorted(os.listdir(pdir)):
            m = re.match(r"^(\d{3})-", clase)
            if m and os.path.isdir(os.path.join(pdir, clase)):
                cat[int(m.group(1))] = (parte, clase)
    return cat


def slug_github(texto: str) -> str:
    """Aproximacion al generador de anclas de GitHub.

    Minusculas; los enlaces se reducen a su texto; el enfasis y el codigo se
    quitan; los espacios pasan a guion; y la puntuacion, los simbolos y los
    emoji se descartan (por eso `## 📊 Matriz` ancla en `-matriz`).
    """
    t = texto.strip().lower()
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[`*_~]", "", t)
    salida = []
    for c in t:
        cat = unicodedata.category(c)
        if c in " \t":
            salida.append("-")
        elif c in "-_" or cat.startswith("L") or cat.startswith("N"):
            salida.append(c)
    return "".join(salida)


def anclas_de(texto: str) -> set:
    """Anclas que ofrece un documento: sus encabezados y sus <a id=...>."""
    encontradas = set()
    repetidos: dict = {}
    for m in ENCABEZADO_RE.finditer(texto):
        base = slug_github(m.group(1))
        n = repetidos.get(base, 0)
        repetidos[base] = n + 1
        encontradas.add(base if n == 0 else f"{base}-{n}")
    encontradas |= set(ANCLA_HTML_RE.findall(texto))
    return encontradas


def _markdown_del_repo():
    for cur, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUIR_ARBOL]
        for fn in files:
            if fn.endswith(".md"):
                yield cur, os.path.join(cur, fn)


def revisa_anclas(errores: list) -> int:
    """Comprueba los enlaces `fichero.md#ancla` de todo el repositorio."""
    documentos = {}
    for _, p in _markdown_del_repo():
        clave = os.path.normcase(os.path.abspath(p))
        documentos[clave] = anclas_de(open(p, encoding="utf-8").read())

    revisados = 0
    for cur, p in _markdown_del_repo():
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        for m in LINK_ANCLA_RE.finditer(open(p, encoding="utf-8").read()):
            destino, frag = m.group(1), m.group(2)
            if EXTERNO_RE.match(destino):
                continue
            revisados += 1
            clave = os.path.normcase(os.path.abspath(
                os.path.normpath(os.path.join(cur, destino))))
            if clave not in documentos:
                continue  # el fichero que falta ya lo canta validar_estructura.py
            if frag not in documentos[clave]:
                errores.append(f"Ancla rota en {rel} -> {destino}#{frag}")
    return revisados


def main() -> int:
    errores: list[str] = []

    if not os.path.isdir(RUTAS):
        print("ERROR: no existe el directorio rutas/")
        return 1

    guias = sorted(
        f for f in os.listdir(RUTAS)
        if f.endswith(".md") and f != "README.md"
    )
    if not guias:
        print("ERROR: rutas/ no contiene ninguna guia")
        return 1

    indice = open(os.path.join(RUTAS, "README.md"), encoding="utf-8").read()
    enlaces_indice = {m.group(1) for m in LINK_RE.finditer(indice)}

    # 1. Huerfanas
    for g in guias:
        if g not in enlaces_indice and ("./" + g) not in enlaces_indice:
            errores.append(f"Ruta huerfana: rutas/{g} no esta enlazada desde rutas/README.md")

    # 5. Slugs
    for g in guias:
        base = g[:-3]
        if not SLUG_RE.match(base) or base != sin_acentos(base):
            errores.append(f"Slug de ruta no canonico (kebab-case ASCII): rutas/{g}")

    cat = catalogo_clases()
    n_max = max(cat) if cat else 0

    for g in guias:
        txt = open(os.path.join(RUTAS, g), encoding="utf-8").read()

        # 2. Enlace de vuelta al indice
        if "](README.md)" not in txt and "](./README.md)" not in txt:
            errores.append(f"rutas/{g} no enlaza de vuelta al indice (README.md)")

        # 3/4. Secciones obligatorias
        if g == CENTRO:
            exigidas = SECCIONES_CENTRO
        else:
            exigidas = list(SECCIONES_RUTA)
            if g in ECOSISTEMA:
                exigidas += SECCIONES_ECOSISTEMA
        faltan = [s for s in exigidas if s not in txt]
        if faltan:
            errores.append(
                f"Secciones faltantes en rutas/{g}: " + ", ".join(f'"{s}"' for s in faltan)
            )

        # 4b. Las rutas del ecosistema practican en el laboratorio ejecutivo
        if g in ECOSISTEMA and LAB_ENLACE not in txt:
            errores.append(f"rutas/{g} no enlaza el laboratorio ejecutivo ({LAB_ENLACE})")

        # 4c. y citan el centro del ecosistema
        if g in ECOSISTEMA and "](ecosistema-ciso.md" not in txt:
            errores.append(f"rutas/{g} no enlaza el centro del ecosistema (ecosistema-ciso.md)")

    # 6. Referencias a clases: existen y estan dentro del catalogo
    revisados = 0
    for base in (RUTAS, LAB_CISO, os.path.join(ROOT, "docs")):
        if not os.path.isdir(base):
            continue
        for fn in sorted(os.listdir(base)):
            if not fn.endswith(".md"):
                continue
            p = os.path.join(base, fn)
            txt = open(p, encoding="utf-8").read()
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            for m in CLASE_RE.finditer(txt):
                revisados += 1
                parte, num, slug = m.group(1), int(m.group(2)), m.group(3)
                if num not in cat:
                    errores.append(
                        f"{rel}: referencia a la clase {num:03d}, que no existe "
                        f"(el catalogo llega hasta {n_max:03d})"
                    )
                    continue
                esperado_parte, esperado_slug = cat[num]
                if parte != esperado_parte or f"{num:03d}-{slug}" != esperado_slug:
                    errores.append(
                        f"{rel}: la clase {num:03d} apunta a {parte}/{num:03d}-{slug} "
                        f"pero en el catalogo es {esperado_parte}/{esperado_slug}"
                    )

    # 7. Laboratorio ejecutivo completo y enlazado
    for fn in LAB_FICHEROS:
        if not os.path.isfile(os.path.join(LAB_CISO, fn)):
            errores.append(f"Falta labs/ciso-leadership/{fn}")
    idx_labs = os.path.join(ROOT, "labs", "README.md")
    if os.path.isfile(idx_labs):
        if "ciso-leadership/README.md" not in open(idx_labs, encoding="utf-8").read():
            errores.append("labs/README.md no cataloga el laboratorio ciso-leadership")

    # 8. Anclas
    anclas_revisadas = revisa_anclas(errores)

    print("== Validacion de rutas por rol y ecosistema CISO ==")
    print(f"Guias de ruta        : {len(guias)}")
    print(f"Del ecosistema CISO  : {len([g for g in guias if g in ECOSISTEMA])} + 1 centro")
    print(f"Clases del catalogo  : {len(cat)} (001..{n_max:03d})")
    print(f"Referencias a clases : {revisados}")
    print(f"Enlaces con ancla    : {anclas_revisadas}")

    if errores:
        print(f"\nFALLO: {len(errores)} problema(s):")
        for e in errores[:50]:
            print(f"  - {e}")
        if len(errores) > 50:
            print(f"  ... y {len(errores) - 50} mas")
        return 1

    print("\nOK: catalogo integro, sin huerfanas, sin clases inexistentes y sin anclas rotas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
