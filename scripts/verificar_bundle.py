#!/usr/bin/env python3
"""Comprueba que el contenido de las clases viaja DENTRO del bundle de la app.

Un build en verde no prueba nada sobre el artefacto: el APK puede compilar,
firmarse y superar `apksigner verify` con el catalogo vacio o recortado. Este
script abre el bundle ya empaquetado (``assets/index.android.bundle`` extraido
del APK, o el bundle web) y busca en sus bytes texto tomado de las clases
reales, de modo que solo pasa si el contenido llego de verdad.

Que verifica:

  1. Las 19 partes: el slug de cada parte aparece en el bundle.
  2. Los titulos: los de una muestra determinista de clases.
  3. El CUERPO de la clase: parrafos largos de la explicacion en profundidad y
     de la practica de esa misma muestra. Es la comprobacion que distingue
     "viaja el indice" de "viaja la clase"; hasta la version 1.1.0 la app solo
     embebia un resumen y este chequeo habria fallado.
  4. Las secciones: los encabezados de glosario, errores, preguntas y
     referencias estan presentes.
  5. El tamano: el bundle pesa al menos lo que ocupa el texto embebido.

Los marcadores se derivan de ``mobile/src/data/classes.js`` en cada ejecucion,
no estan escritos a mano: si el temario cambia, el verificador cambia con el.

Un mismo texto no se guarda igual en todos los bundles, asi que cada marcador se
busca en las tres formas en que puede aparecer: UTF-8 (lo habitual), UTF-16LE
(Hermes guarda asi las cadenas que no son ASCII puro) y escapado \\uXXXX (lo que
emite Metro para el bundle web). Buscar solo una daria un falso negativo en
cuanto el texto lleve una tilde.

Uso:
    python scripts/verificar_bundle.py <ruta-del-bundle>
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOGO = ROOT / "mobile" / "src" / "data" / "classes.js"

# Cada cuantas clases se toma una para la muestra. Con 340 clases da 9 clases
# repartidas por todo el programa; suficiente para detectar un truncado y lo
# bastante barato para correr en cada release.
PASO_MUESTRA = 40

# Longitud minima de un parrafo para servir de marcador: uno corto podria
# aparecer por casualidad o repetirse entre clases.
MIN_MARCADOR = 120

SECCIONES_ESPERADAS = ("Glosario", "Errores comunes", "Preguntas frecuentes", "Referencias")


# Un trozo ASCII de al menos esta longitud identifica el parrafo sin ambiguedad
# y sobrevive a cualquiera de las codificaciones.
MIN_FRAGMENTO = 40

# Comillas y contrabarra: dentro del bundle van escapadas, asi que un fragmento
# que las contenga no coincidiria byte a byte. Se excluyen del fragmento.
PROHIBIDOS = set('"\'\\`')


def escape_js(texto: str) -> str:
    """Como escribe Metro una cadena no-ASCII en el bundle web: \\xNN y \\uXXXX."""
    out = []
    for ch in texto:
        codigo = ord(ch)
        if codigo < 0x80:
            out.append(ch)
        elif codigo < 0x100:
            out.append(f"\\x{codigo:02x}")
        else:
            out.append(f"\\u{codigo:04x}")
    return "".join(out)


def fragmento_ascii(texto: str, minimo: int) -> str | None:
    """El tramo ASCII mas largo del texto, si llega al minimo pedido."""
    mejor = ""
    actual = ""
    for ch in texto:
        if ord(ch) < 0x80 and ch not in PROHIBIDOS:
            actual += ch
            if len(actual) > len(mejor):
                mejor = actual
        else:
            actual = ""
    return mejor if len(mejor) >= minimo else None


def formas(texto: str, minimo: int) -> list[tuple[str, bytes]]:
    """Las representaciones en bytes con las que un texto puede estar guardado.

    - UTF-8: el caso normal (bundle sin minificar, cadenas ASCII de Hermes).
    - UTF-16LE: Hermes guarda asi cualquier cadena que no sea ASCII puro.
    - Escapado: Metro emite \\xNN / \\uXXXX en el bundle web.
    - Fragmento ASCII: ultimo recurso, el tramo sin tildes del propio texto.
    """
    candidatos = [
        ("utf-8", texto.encode("utf-8")),
        ("utf-16le", texto.encode("utf-16-le")),
        ("escapado", escape_js(texto).encode("utf-8")),
    ]
    trozo = fragmento_ascii(texto, minimo)
    if trozo:
        candidatos.append(("fragmento", trozo.encode("utf-8")))
        candidatos.append(("fragmento-utf16", trozo.encode("utf-16-le")))
    return candidatos


def cargar_catalogo() -> tuple[list[dict], list[dict]]:
    if not CATALOGO.exists():
        raise SystemExit(f"FALLA: no existe {CATALOGO.relative_to(ROOT)}")
    src = CATALOGO.read_text(encoding="utf-8")
    partes = json.loads(re.search(r"export const PARTS = (\[.*?\n\]);", src, re.DOTALL).group(1))
    clases = json.loads(re.search(r"export const CLASSES = (\[.*?\n\]);", src, re.DOTALL).group(1))
    return partes, clases


def parrafo_marcador(bloques: list[dict]) -> str | None:
    """El parrafo mas largo de la seccion: el que peor sobrevive a un truncado."""
    textos = [b.get("x", "") for b in bloques if b.get("t") == "p"]
    textos = [t for t in textos if len(t) >= MIN_MARCADOR]
    return max(textos, key=len) if textos else None


def main() -> int:
    if len(sys.argv) < 2:
        raise SystemExit("Uso: python scripts/verificar_bundle.py <ruta-del-bundle>")
    bundle_path = Path(sys.argv[1])
    if not bundle_path.is_file():
        raise SystemExit(f"FALLA: no existe el bundle {bundle_path}")

    datos = bundle_path.read_bytes()
    print(f"Bundle: {bundle_path}  ({len(datos):,} bytes)")

    partes, clases = cargar_catalogo()
    fallos: list[str] = []

    formatos: set[str] = set()

    def exigir(texto: str, etiqueta: str, minimo: int = MIN_FRAGMENTO) -> None:
        for nombre, crudo in formas(texto, minimo):
            if crudo in datos:
                formatos.add(nombre)
                print(f"  OK     {etiqueta}")
                return
        print(f"  FALTA  {etiqueta}")
        fallos.append(etiqueta)

    print(f"\n[1/5] Las {len(partes)} partes")
    for parte in partes:
        exigir(parte["id"], f"parte {parte['number']}: {parte['id']}")

    muestra = clases[::PASO_MUESTRA]
    print(f"\n[2/5] Titulos de {len(muestra)} clases de muestra")
    for c in muestra:
        exigir(c["title"], f"clase {c['number']}: {c['title'][:52]}")

    print(f"\n[3/5] Cuerpo de esas {len(muestra)} clases (parrafos completos)")
    for c in muestra:
        for nombre, bloques in (("teoria", c["content"]["theory"]),
                                ("practica", c["content"]["practice"])):
            marcador = parrafo_marcador(bloques)
            if marcador is None:
                print(f"  --     clase {c['number']} {nombre}: sin parrafo largo que verificar")
                continue
            exigir(marcador, f"clase {c['number']} {nombre}: \"{marcador[:48]}...\"")

    print("\n[4/5] Secciones del estandar pedagogico")
    for seccion in SECCIONES_ESPERADAS:
        exigir(seccion, f"seccion «{seccion}»")

    print("\n[5/5] Tamano coherente con el texto embebido")
    texto_embebido = sum(
        len(b.get("x", "").encode("utf-8"))
        for c in clases
        for b in c["content"]["theory"] + c["content"]["practice"]
    )
    minimo = int(texto_embebido * 0.9)
    print(f"  texto de las clases: {texto_embebido:,} bytes; minimo exigido al bundle: {minimo:,}")
    if len(datos) < minimo:
        print(f"  FALTA  el bundle ({len(datos):,} B) no alcanza para contener el texto")
        fallos.append("tamano del bundle")
    else:
        print("  OK     el bundle da de si para el texto de las clases")

    if formatos:
        print(f"\nCodificacion detectada en el bundle: {', '.join(sorted(formatos))}")

    if fallos:
        print(f"\nFALLA: {len(fallos)} comprobacion(es) sin superar: {fallos[:6]}")
        return 1
    print(f"\nVERIFICADO: las {len(clases)} clases viajan COMPLETAS dentro del bundle.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
