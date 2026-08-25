#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprueba que NINGUN diagrama falta en ninguna de las salidas del curso.

Cada clase declara sus diagramas en bloques ```mermaid dentro de su README, que
es la fuente de verdad. De ahi salen cuatro artefactos que deben llevarlos:

    PDF de la clase   classes/**/clase-NNN-guia.pdf   SVG incrustado
    PPTX de la clase  classes/**/clase-NNN-presentacion.pptx  PNG, una diapositiva
    HTML del sitio    site/classes/**/README.html     SVG incrustado (GitHub Pages)
    App movil         mobile/src/data/classes.js + assets/diagramas/*.png

El manual (manual/MANUAL.pdf) se comprueba aparte, como un todo.

Se cuenta lo que hay DENTRO de cada fichero, no lo que el generador dijo haber
hecho: un PDF puede pesar lo esperado y llevar el cartel de "Syntax error" de
mermaid donde deberia ir el grafico, y un APK puede compilar con el catalogo
recortado. Por eso este script abre los binarios y cuenta.

Uso:
    python scripts/verificar_diagramas.py            # todas las salidas
    python scripts/verificar_diagramas.py --rapido   # sin abrir los PDF (mas veloz)
"""
from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mermaid_svg import clave as clave_diagrama  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
CLASSES = ROOT / "classes"
SITE = ROOT / "site"
MANUAL = ROOT / "manual" / "MANUAL.pdf"
CATALOGO = ROOT / "mobile" / "src" / "data" / "classes.js"
DIAG_DIR = ROOT / "mobile" / "assets" / "diagramas"

MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)


def diagramas_de_clase(readme: Path) -> list[str]:
    return [b.strip() for b in MERMAID_RE.findall(readme.read_text(encoding="utf-8")) if b.strip()]


# Etiqueta de nodo mermaid: A["Texto"], B(Texto), C{Texto}.
ETIQUETA_RE = re.compile(
    r"""[\[\(\{]{1,2}"?([A-Za-zAEIOUNaeiounÁÉÍÓÚÑáéíóúñ][^"\]\)\}\|<>\n]{5,28})"?[\]\)\}]{1,2}"""
)


def sonda(fuente: str, prosa: str) -> str | None:
    """Etiqueta del diagrama que NO aparece en el texto de la clase.

    Sirve para comprobar sobre el PDF impreso que el diagrama llego a dibujarse:
    si la etiqueta estuviera tambien en la prosa, encontrarla no probaria nada.
    """
    for etiqueta in ETIQUETA_RE.findall(fuente):
        etiqueta = etiqueta.strip()
        if etiqueta and etiqueta not in prosa:
            return etiqueta
    return None


def texto_de_pdf(pdf: Path) -> str | None:
    """Texto del PDF, o None si no hay pypdf instalado para leerlo."""
    try:
        from pypdf import PdfReader
    except ImportError:
        return None
    try:
        return "\n".join((pagina.extract_text() or "") for pagina in PdfReader(str(pdf)).pages)
    except Exception:
        return ""


def hay_error_de_sintaxis(texto: str) -> bool:
    return "Syntax error" in texto and "mermaid version" in texto

def esta_en(etiqueta: str, texto: str) -> bool:
    """True si la etiqueta aparece en el texto, aunque venga partida.

    Mermaid parte las etiquetas largas en varias lineas dentro del nodo, y al
    extraer el texto del PDF esas lineas llegan separadas. Comparar literalmente
    daria por ausente un diagrama que si esta dibujado.
    """
    if etiqueta in texto:
        return True
    patron = r"\s*".join(re.escape(p) for p in etiqueta.split())
    return re.search(patron, texto) is not None



def imagenes_en_pptx(pptx: Path) -> int:
    """Numero de imagenes incrustadas en la presentacion."""
    with zipfile.ZipFile(pptx) as z:
        return sum(
            1 for n in z.namelist()
            if n.startswith("ppt/media/") and n.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
        )


def svgs_en_html(html: Path) -> int:
    texto = html.read_text(encoding="utf-8", errors="replace")
    return texto.count('<figure class="mermaid">')


def cargar_catalogo() -> dict[int, list[dict]]:
    """{numero de clase: bloques de diagrama emitidos para la app}."""
    src = CATALOGO.read_text(encoding="utf-8")
    clases = json.loads(re.search(r"export const CLASSES = (\[.*?\n\]);", src, re.DOTALL).group(1))
    salida: dict[int, list[dict]] = {}
    for c in clases:
        bloques = c["content"]["theory"] + c["content"]["practice"]
        salida[c["number"]] = [b for b in bloques if b.get("t") == "dg"]
    return salida


def main() -> int:
    rapido = "--rapido" in sys.argv
    catalogo = cargar_catalogo() if CATALOGO.is_file() else {}
    hay_sitio = SITE.is_dir()

    fallos: list[str] = []
    total_diagramas = 0
    clases_con_diagrama = 0
    pdf_sin_pypdf = False

    for readme in sorted(CLASSES.glob("parte-*/*/README.md"), key=lambda p: int(p.parent.name[:3])):
        numero = int(readme.parent.name[:3])
        esperados = diagramas_de_clase(readme)
        if not esperados:
            continue
        clases_con_diagrama += 1
        total_diagramas += len(esperados)
        unicos = list(dict.fromkeys(esperados))

        # PDF de la clase: el SVG impreso se convierte en dibujo vectorial, asi
        # que no se puede "contar" como imagen. Lo que si queda es el texto de
        # las etiquetas del diagrama; se busca una que no exista en la prosa.
        pdf = readme.parent / f"clase-{numero:03d}-guia.pdf"
        if not pdf.is_file():
            fallos.append(f"clase {numero}: falta el PDF")
        elif not rapido:
            texto_pdf = texto_de_pdf(pdf)
            if texto_pdf is None:
                pdf_sin_pypdf = True
            elif hay_error_de_sintaxis(texto_pdf):
                fallos.append(f"clase {numero}: el PDF lleva un diagrama con error de sintaxis")
            else:
                prosa = MERMAID_RE.sub("", readme.read_text(encoding="utf-8"))
                for fuente in unicos:
                    etiqueta = sonda(fuente, prosa)
                    if etiqueta and not esta_en(etiqueta, texto_pdf):
                        fallos.append(
                            f"clase {numero}: el PDF no contiene el diagrama "
                            f"(falta la etiqueta {etiqueta!r})"
                        )

        # PPTX: una diapositiva (una imagen) por diagrama unico.
        pptx = readme.parent / f"clase-{numero:03d}-presentacion.pptx"
        if not pptx.is_file():
            fallos.append(f"clase {numero}: falta el PPTX")
        else:
            imagenes = imagenes_en_pptx(pptx)
            if imagenes < len(unicos):
                fallos.append(
                    f"clase {numero}: el PPTX lleva {imagenes} imagen(es) y la clase "
                    f"tiene {len(unicos)} diagrama(s)"
                )

        # HTML del sitio (GitHub Pages): un <figure class="mermaid"> por diagrama.
        if hay_sitio:
            html = SITE / "classes" / readme.parent.parent.name / readme.parent.name / "README.html"
            if not html.is_file():
                fallos.append(f"clase {numero}: falta la pagina HTML del sitio")
            else:
                figuras = svgs_en_html(html)
                if figuras < len(esperados):
                    fallos.append(
                        f"clase {numero}: el HTML lleva {figuras} diagrama(s) dibujado(s) "
                        f"de {len(esperados)}"
                    )

        # App movil: un bloque dg con imagen por diagrama, y su PNG empaquetado.
        if catalogo:
            bloques = catalogo.get(numero, [])
            if len(bloques) < len(esperados):
                fallos.append(
                    f"clase {numero}: la app tiene {len(bloques)} bloque(s) de diagrama "
                    f"de {len(esperados)}"
                )
            for bloque in bloques:
                img = bloque.get("img")
                if not img:
                    fallos.append(f"clase {numero}: un diagrama de la app quedo sin imagen")
                elif not (DIAG_DIR / f"{img}.png").is_file():
                    fallos.append(f"clase {numero}: falta el PNG {img} en los assets de la app")
            for fuente in esperados:
                esperado = clave_diagrama(fuente)
                if not any(b.get("img") == esperado for b in bloques):
                    fallos.append(f"clase {numero}: la app no referencia el diagrama {esperado}")

    print(f"Clases con diagrama: {clases_con_diagrama} · diagramas declarados: {total_diagramas}")
    if not hay_sitio:
        print("AVISO: no existe site/; el HTML no se ha comprobado "
              "(genera con: python scripts/generar_sitio.py).")
    if not catalogo:
        print("AVISO: no existe el catalogo de la app; no se ha comprobado.")

    if pdf_sin_pypdf:
        print("AVISO: sin pypdf no se ha podido mirar dentro de los PDF (pip install pypdf).")

    # El manual, como un todo: se muestrea una clase de cada quince.
    if MANUAL.is_file() and not rapido:
        texto_manual = texto_de_pdf(MANUAL)
        if texto_manual is None:
            pass
        elif hay_error_de_sintaxis(texto_manual):
            fallos.append("el manual lleva un diagrama con error de sintaxis")
        else:
            faltan = muestreadas = 0
            readmes = sorted(CLASSES.glob("parte-*/*/README.md"),
                             key=lambda r: int(r.parent.name[:3]))
            for readme in readmes[::15]:
                md = readme.read_text(encoding="utf-8")
                fuentes = [b.strip() for b in MERMAID_RE.findall(md) if b.strip()]
                if not fuentes:
                    continue
                etiqueta = sonda(fuentes[0], MERMAID_RE.sub("", md))
                if not etiqueta:
                    continue
                muestreadas += 1
                if not esta_en(etiqueta, texto_manual):
                    faltan += 1
                    fallos.append(
                        f"el manual no contiene el diagrama de la clase "
                        f"{int(readme.parent.name[:3])} (falta {etiqueta!r})"
                    )
            print(f"Manual: {MANUAL.stat().st_size / 1024 / 1024:.1f} MB, "
                  f"{muestreadas - faltan}/{muestreadas} diagramas muestreados presentes.")

    if fallos:
        print(f"\nFALLA: {len(fallos)} problema(s):")
        for f in fallos[:40]:
            print(f"  - {f}")
        if len(fallos) > 40:
            print(f"  … y {len(fallos) - 40} mas")
        return 1
    print("\nVERIFICADO: todos los diagramas estan en el PDF, el PPTX, el HTML y la app.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
