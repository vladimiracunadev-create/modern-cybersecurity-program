# -*- coding: utf-8 -*-
"""
Genera el MANUAL del curso en PDF: consolida las 340 clases en un unico
documento ordenado.

  - manual/MANUAL.pdf  render imprimible (via Microsoft Edge/Chrome headless)

El Markdown consolidado se construye en memoria como paso intermedio (se
convierte a HTML y de ahi a PDF); no se deja ningun .md en el repositorio.

El manual respeta el orden global 001->340 agrupado en las 19 partes, con
portada, aviso etico e indice enlazado a cada clase.

Transformaciones sobre cada README de clase para que funcione como documento
lineal (y no como pagina suelta):
  - Los encabezados bajan un nivel: la parte es H1, la clase H2, sus secciones
    H3+ (respetando los bloques de codigo, donde '#' no es encabezado).
  - Se quitan las secciones que solo tienen sentido navegando el repo:
    "Material descargable", "Clase anterior" y "Siguiente clase".
  - Los enlaces a otras clases pasan a anclas internas (#clase-NNN); el resto de
    enlaces/imagenes relativos pasan a URL absoluta de GitHub (blob/raw), para
    que no queden rotos fuera de su carpeta.

Uso:
    python scripts/generar_manual.py                 # genera manual/MANUAL.pdf
    python scripts/generar_manual.py --volcar-md R   # ademas escribe el MD en R (debug)
"""
from __future__ import annotations

import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLASSES = os.path.join(ROOT, "classes")
OUT_DIR = os.path.join(ROOT, "manual")

REPO = "vladimiracunadev-create/modern-cybersecurity-program"
BLOB = f"https://github.com/{REPO}/blob/main/"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"

# Secciones que se eliminan del README al consolidar (no aplican a un manual lineal).
CUT_MARKERS = ("📥 Material descargable", "⬅️ Clase anterior", "➡️ Siguiente clase")

NAVEGADORES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

CSS = """
@page { size: A4; margin: 16mm 15mm; }
* { box-sizing: border-box; }
body { font-family: -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
       font-size: 10.5pt; line-height: 1.45; color: #1a1f24; margin: 0; }
h1 { font-size: 21pt; color: #0b3d2e; border-bottom: 3px solid #2e8b57;
     padding-bottom: 5px; margin: 26px 0 12px; page-break-before: always; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 15pt; color: #0b3d2e; border-bottom: 1px solid #cdd8d1;
     padding-bottom: 3px; margin: 22px 0 8px; page-break-after: avoid; }
h3 { font-size: 12pt; color: #24503f; margin: 14px 0 6px; page-break-after: avoid; }
h4 { font-size: 11pt; color: #24503f; margin: 12px 0 4px; }
p, li { orphans: 2; widows: 2; }
code { font-family: "Cascadia Code", Consolas, monospace; font-size: 9pt;
       background: #f2f5f3; padding: 1px 4px; border-radius: 3px; }
pre { background: #f6f8f7; border: 1px solid #dde5e0; border-radius: 5px;
      padding: 9px 11px; overflow-x: auto; page-break-inside: avoid; }
pre code { background: none; padding: 0; font-size: 8.6pt; line-height: 1.4; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9pt;
        page-break-inside: avoid; }
th, td { border: 1px solid #c4ccd2; padding: 4px 7px; text-align: left;
         vertical-align: top; }
th { background: #eaf3ee; }
blockquote { border-left: 3px solid #2e8b57; margin: 8px 0; padding: 3px 12px;
             background: #f5f9f7; color: #333; page-break-inside: avoid; }
a { color: #0b6; text-decoration: none; }
img { max-width: 100%; }
hr { border: 0; border-top: 1px solid #d5ddd8; margin: 18px 0; }
.portada { page-break-after: always; text-align: center; padding-top: 60mm; }
.portada h1 { border: 0; page-break-before: avoid; font-size: 30pt; }
.portada .sub { font-size: 13pt; color: #24503f; margin-top: 8px; }
.portada .meta { font-size: 11pt; color: #556; margin-top: 26px; }
.toc a { color: #1a1f24; }
.toc-parte { font-weight: 600; margin-top: 10px; color: #0b3d2e; }
"""


def encontrar_navegador() -> str | None:
    for ruta in NAVEGADORES:
        if os.path.isfile(ruta):
            return ruta
    return shutil.which("msedge") or shutil.which("chrome")


def clases_ordenadas():
    """[(num, parte_dir, parte_titulo, clase_dir_rel, ruta_readme)] en orden global."""
    out = []
    for parte in sorted(os.listdir(CLASSES)):
        pdir = os.path.join(CLASSES, parte)
        if not (os.path.isdir(pdir) and parte.startswith("parte-")):
            continue
        for clase in sorted(os.listdir(pdir)):
            cdir = os.path.join(pdir, clase)
            readme = os.path.join(cdir, "README.md")
            m = re.match(r"^(\d{3})-", clase)
            if m and os.path.isfile(readme):
                rel = os.path.relpath(cdir, ROOT).replace("\\", "/")
                out.append((int(m.group(1)), parte, rel, readme))
    out.sort(key=lambda t: t[0])
    return out


def titulo_parte(parte_dir: str) -> str:
    """Lee el H1 (o la primera linea **negrita**) del README de la parte."""
    readme = os.path.join(CLASSES, parte_dir, "README.md")
    if os.path.isfile(readme):
        with open(readme, encoding="utf-8") as f:
            for linea in f:
                if linea.startswith("# "):
                    return linea[2:].strip()
    # fallback: del slug "parte-3-hacking-..." -> "Parte 3 — Hacking ..."
    m = re.match(r"parte-(\d+)-(.+)", parte_dir)
    if m:
        return f"Parte {m.group(1)} — {m.group(2).replace('-', ' ').capitalize()}"
    return parte_dir


def h1_de(readme: str) -> str:
    with open(readme, encoding="utf-8") as f:
        for linea in f:
            if linea.startswith("# "):
                return linea[2:].strip()
    return ""


def cortar_secciones_finales(md: str) -> str:
    """Trunca desde la primera seccion H2 de navegacion/material (van al final)."""
    lineas = md.split("\n")
    corte = len(lineas)
    for i, linea in enumerate(lineas):
        if re.match(r"^##\s", linea) and any(mk in linea for mk in CUT_MARKERS):
            corte = min(corte, i)
    return "\n".join(lineas[:corte]).rstrip() + "\n"


def subir_headings(md: str, inc: int = 1, maxlvl: int = 6) -> str:
    """Aumenta el nivel de los encabezados, sin tocar los '#' dentro de code fences."""
    out, en_fence = [], False
    for linea in md.split("\n"):
        if re.match(r"^\s*(```|~~~)", linea):
            en_fence = not en_fence
            out.append(linea)
            continue
        if not en_fence:
            m = re.match(r"^(#{1,6})(\s)", linea)
            if m:
                nivel = min(len(m.group(1)) + inc, maxlvl)
                linea = "#" * nivel + linea[len(m.group(1)):]
        out.append(linea)
    return "\n".join(out)


LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)(\s+\"[^\"]*\")?\)")
CLASE_RE = re.compile(r"(?:^|/)(\d{3})-[^/]+/README\.md$")


def reescribir_enlaces(md: str, clase_dir_rel: str) -> str:
    """Enlaces a otras clases -> #clase-NNN; el resto de relativos -> URL absoluta."""

    def repl(m):
        img, texto, href, titulo = m.groups()
        titulo = titulo or ""
        if href.startswith(("http://", "https://", "#", "mailto:")):
            destino = href
        else:
            mc = CLASE_RE.search(href.split("#")[0])
            if mc and not img:
                destino = f"#clase-{mc.group(1)}"
            else:
                # resuelve el relativo respecto a la carpeta de la clase
                objetivo = os.path.normpath(
                    os.path.join(clase_dir_rel, href)
                ).replace("\\", "/")
                base = RAW if img else BLOB
                destino = base + objetivo
        return f"{img}[{texto}]({destino}{titulo})"

    return LINK_RE.sub(repl, md)


def procesar_clase(num: int, clase_dir_rel: str, readme: str) -> str:
    with open(readme, encoding="utf-8") as f:
        md = f.read()
    md = cortar_secciones_finales(md)
    md = reescribir_enlaces(md, clase_dir_rel)
    md = subir_headings(md, inc=1)
    ancla = f'<a id="clase-{num:03d}"></a>\n\n'
    return ancla + md.rstrip() + "\n"


def construir_md(clases) -> str:
    n_clases = len(clases)
    partes_orden = []
    for _, parte, _, _ in clases:
        if parte not in partes_orden:
            partes_orden.append(parte)
    n_partes = len(partes_orden)

    p = []
    # Portada (HTML puro: el markdown dentro de un <div> no se procesaria)
    p.append(
        '<div class="portada">\n'
        "<h1>🛡️ Programa de Ciberseguridad Moderna</h1>\n"
        '<p class="sub">Manual completo · de fundamentos a nivel experto</p>\n'
        f'<p class="meta">{n_clases} clases · {n_partes} partes · '
        "generado automáticamente desde el repositorio</p>\n"
        "</div>\n"
    )

    # Aviso etico (un solo blockquote continuo: la linea ">" evita MD028)
    p.append(
        "\n> ⚠️ **Uso ético y legal.** Todo el contenido ofensivo de este programa "
        "(explotación, malware, Red Team, cracking) es para **aprendizaje "
        "autorizado, laboratorios propios, CTFs y trabajo profesional con permiso "
        "explícito**. Atacar sistemas sin autorización es delito en prácticamente "
        "todos los países.\n"
        ">\n"
        f"> 📖 Este manual consolida las {n_clases} clases del programa. La versión "
        "navegable, los laboratorios y los recursos interactivos están en el "
        f"[repositorio]({BLOB.rstrip('/')}) y en el "
        f"[sitio del curso](https://{REPO.split('/')[0]}.github.io/{REPO.split('/')[1]}/).\n"
    )

    # Indice
    p.append("\n---\n\n# 📑 Índice\n")
    parte_actual = None
    for num, parte, _, readme in clases:
        if parte != parte_actual:
            parte_actual = parte
            p.append(f'\n<p class="toc-parte">{titulo_parte(parte)}</p>\n\n')
        titulo = h1_de(readme)
        p.append(f"- [{titulo}](#clase-{num:03d})\n")

    # Contenido
    parte_actual = None
    for num, parte, clase_dir_rel, readme in clases:
        if parte != parte_actual:
            parte_actual = parte
            p.append(f"\n---\n\n# {titulo_parte(parte)}\n")
        p.append("\n" + procesar_clase(num, clase_dir_rel, readme) + "\n")

    return "".join(p).rstrip() + "\n"


def md_a_html(md_text: str) -> str:
    cuerpo = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc", "md_in_html"],
    )
    return (
        "<!doctype html><html lang='es'><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>{cuerpo}</body></html>"
    )


def generar_pdf(nav: str, html_path: str, pdf_path: str) -> None:
    uri = "file:///" + html_path.replace("\\", "/")
    subprocess.run(
        [nav, "--headless=new", "--disable-gpu", "--no-first-run",
         "--no-default-browser-check", "--no-pdf-header-footer",
         "--virtual-time-budget=20000",
         f"--print-to-pdf={pdf_path}", uri],
        check=True, timeout=600,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def main() -> int:
    clases = clases_ordenadas()
    if not clases:
        print("ERROR: no se encontraron clases")
        return 1

    # El Markdown consolidado es solo un intermedio (MD -> HTML -> PDF): se
    # mantiene en memoria y no se escribe ningun .md en el repositorio.
    md_text = construir_md(clases)
    kb = len(md_text.encode("utf-8")) / 1024
    print(f"Manual consolidado: {len(clases)} clases, {kb:.0f} KB de Markdown (intermedio).")

    if "--volcar-md" in sys.argv:  # solo para depurar el contenido
        destino = sys.argv[sys.argv.index("--volcar-md") + 1]
        with open(destino, "w", encoding="utf-8", newline="\n") as f:
            f.write(md_text)
        print(f"Markdown volcado en: {destino}")

    nav = encontrar_navegador()
    if not nav:
        print("ERROR: no se encontró Edge/Chrome; no se puede generar el PDF.")
        return 1

    os.makedirs(OUT_DIR, exist_ok=True)
    html = md_a_html(md_text)
    pdf_path = os.path.join(OUT_DIR, "MANUAL.pdf")
    with tempfile.NamedTemporaryFile(
        "w", suffix=".html", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(html)
        html_path = tmp.name
    try:
        generar_pdf(nav, html_path, pdf_path)
    finally:
        os.unlink(html_path)

    mb = os.path.getsize(pdf_path) / 1024 / 1024
    print(f"MANUAL.pdf generado: {mb:.1f} MB  ({nav.split(chr(92))[-1]}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
