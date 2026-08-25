#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dibuja los diagramas ```mermaid a SVG una sola vez y los cachea.

Por que existe
--------------
El manual junta las 340 clases en una sola pagina HTML de 1.242 paginas con 360
diagramas. La forma facil de dibujarlos —cargar mermaid.js y dejar que Chrome
imprima— **no funciona a esa escala**: Chrome imprime cuando se agota el
presupuesto de tiempo virtual, y con 360 diagramas mermaid no ha empezado
siquiera. Se comprobo midiendo: con 60 s y con 900 s de presupuesto el PDF sale
del mismo tamano y sin **ningun** diagrama dentro (la palabra "Emisor", que solo
existe dentro del diagrama de la clase 021, aparecia 0 veces en todo el manual).
Subir el presupuesto no arregla nada porque el tiempo virtual se consume mucho
antes de que el dibujado termine.

La solucion es separar las dos cosas: primero se dibuja cada diagrama por su
cuenta, y despues el PDF se imprime desde un HTML que ya lleva los SVG dentro y no
necesita JavaScript. De paso, imprimir sin JS es mucho mas rapido y el resultado
deja de depender de cuanto tarde una CDN.

Un diagrama por pagina, y no varios: medido sobre las clases de este repositorio,
una pagina con 20 diagramas devuelve 5 dibujados y 15 esqueletos vacios; con 5,
11 de 20; de uno en uno, 20 de 20. Subir el presupuesto de tiempo virtual no
cambia nada (60 s y 300 s dan el mismo resultado), porque el volcado no espera a
que mermaid termine. Y el esqueleto vacio es traicionero: es un ``<svg>`` valido
con su hoja de estilos y un ``<g></g>`` sin nada dentro, asi que comprobar solo
que "hay un svg" da por bueno un diagrama que no existe.

Los SVG se cachean por hash del codigo fuente del diagrama, asi que regenerar el
manual tras editar una clase solo vuelve a dibujar lo que cambio.

Ademas del SVG se genera un PNG de cada diagrama. No es un duplicado por gusto:
el HTML y los PDF incrustan el SVG (vectorial, nitido a cualquier zoom), pero una
presentacion PPTX y la app movil no saben pintar SVG —python-pptx solo inserta
imagenes de mapa de bits, y el <Image> de React Native tampoco lee SVG sin una
dependencia nativa que ademas no aplicaria el CSS que mermaid mete dentro del
SVG—. Con el PNG, el mismo diagrama llega a las cuatro salidas.

Uso como modulo:
    from mermaid_svg import dibujar, rasterizar
    svgs = dibujar(lista_de_codigos_mermaid)     # {codigo: svg}
    pngs = rasterizar(lista_de_codigos_mermaid)  # {codigo: ruta del png}

Uso directo (calienta la cache de todas las clases del repositorio):
    python scripts/mermaid_svg.py
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / ".cache" / "mermaid"

PRESUPUESTO_MS = 60_000
TIMEOUT_S = 600
# Procesos de navegador en paralelo. Cada diagrama tarda unos segundos por si
# mismo; en serie, las 360 figuras del programa son casi veinte minutos.
PARALELO = 4
REINTENTOS = 2

NAVEGADORES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]

MERMAID_ESM = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs"

# Rasterizado. El ancho maximo mantiene los PNG manejables (la app movil los
# empaqueta dentro del APK) y la escala 2x evita que el texto salga borroso en
# pantallas densas y al proyectar una diapositiva.
PNG_ANCHO_MAX = 900
PNG_ESCALA = 2
PNG_COLORES = 128  # los diagramas usan pocos colores: la paleta reduce mucho el peso

VIEWBOX_RE = re.compile(r'viewBox="\s*[-\d.]+\s+[-\d.]+\s+([\d.]+)\s+([\d.]+)"')

PRE_RE = re.compile(r'<pre class="mermaid" id="d0"[^>]*>(.*?)</pre>', re.DOTALL)
STYLE_RE = re.compile(r"<style>.*?</style>", re.DOTALL)
# mermaid nombra cada SVG y su CSS con un id propio; al venir de lotes distintos
# esos ids podrian repetirse y un diagrama acabaria pintado con el CSS de otro.
ID_MERMAID_RE = re.compile(r"mermaid-\d+")


def encontrar_navegador() -> str | None:
    for ruta in NAVEGADORES:
        if Path(ruta).is_file():
            return ruta
    return None


def clave(fuente: str) -> str:
    """Nombre del fichero de cache. Es una clave de contenido, no un control de
    seguridad; se usa sha256 igualmente para no dejar sha1 en el codigo."""
    return hashlib.sha256(fuente.strip().encode("utf-8")).hexdigest()[:16]


def _pagina(fuente: str) -> str:
    return (
        "<!doctype html><html lang='es'><head><meta charset='utf-8'></head><body>"
        f'<pre class="mermaid" id="d0">{fuente}</pre>'
        "<script type='module'>"
        f'import mermaid from "{MERMAID_ESM}";'
        'mermaid.initialize({ startOnLoad: true, theme: "default", securityLevel: "strict" });'
        "</script></body></html>"
    )


def _dibujado(svg: str) -> bool:
    """True solo si el SVG tiene diagrama de verdad.

    Mermaid crea primero el <svg> con su hoja de estilos y un <g> vacio, y lo
    rellena despues. Ese esqueleto pasa cualquier comprobacion de "¿hay un svg?"
    y no dibuja nada, asi que se exige contenido fuera del <style>.
    """
    if 'roledescription="error"' in svg or "Syntax error" in svg:
        return False  # diagrama con la sintaxis rota: mermaid pinta un cartel
    cuerpo = STYLE_RE.sub("", svg)
    return "<path" in cuerpo or "<text" in cuerpo or "foreignObject" in cuerpo


def _dibujar_uno(nav: str, fuente: str) -> str | None:
    """Dibuja un diagrama en su propia pagina y devuelve su SVG, o None."""
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp:
        tmp.write(_pagina(fuente))
        ruta = tmp.name
    try:
        resultado = subprocess.run(
            [nav, "--headless=new", "--disable-gpu", "--no-first-run",
             "--no-default-browser-check", f"--virtual-time-budget={PRESUPUESTO_MS}",
             "--dump-dom", "file:///" + ruta.replace("\\", "/")],
            capture_output=True, timeout=TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        return None
    finally:
        Path(ruta).unlink(missing_ok=True)

    match = PRE_RE.search(resultado.stdout.decode("utf-8", "replace"))
    if not match:
        return None
    svg = match.group(1).strip()
    return svg if "<svg" in svg and _dibujado(svg) else None


# Cache en memoria del proceso: el generador del sitio pide diagramas una vez
# por pagina (425 veces), y sin esto cada llamada volvia a leer los SVG del
# disco. Con ella, el build del sitio baja de casi tres minutos a segundos.
_EN_MEMORIA: dict[str, str] = {}


def dibujar(fuentes: list[str], nav: str | None = None, verbose: bool = True) -> dict[str, str]:
    """Devuelve {codigo mermaid: SVG}. Usa la cache y solo dibuja lo que falta."""
    unicas = list(dict.fromkeys(f.strip() for f in fuentes if f.strip()))
    CACHE.mkdir(parents=True, exist_ok=True)

    svgs: dict[str, str] = {}
    pendientes: list[str] = []
    for fuente in unicas:
        if fuente in _EN_MEMORIA:
            svgs[fuente] = _EN_MEMORIA[fuente]
            continue
        fichero = CACHE / f"{clave(fuente)}.svg"
        if fichero.is_file():
            svgs[fuente] = _EN_MEMORIA[fuente] = fichero.read_text(encoding="utf-8")
        else:
            pendientes.append(fuente)

    if not pendientes:
        if verbose:
            print(f"Diagramas: {len(svgs)} en cache, nada que dibujar.")
        return svgs

    nav = nav or encontrar_navegador()
    if not nav:
        raise SystemExit("No se encontro Edge ni Chrome para dibujar los diagramas.")

    if verbose:
        print(f"Diagramas: {len(svgs)} en cache, {len(pendientes)} por dibujar "
              f"({PARALELO} en paralelo).")

    fallidos = list(pendientes)
    for intento in range(1, REINTENTOS + 2):
        if not fallidos:
            break
        tanda, fallidos = fallidos, []
        with ThreadPoolExecutor(max_workers=PARALELO) as pool:
            futuros = {pool.submit(_dibujar_uno, nav, f): f for f in tanda}
            hechos = 0
            for futuro in as_completed(futuros):
                fuente = futuros[futuro]
                svg = futuro.result()
                hechos += 1
                if not svg:
                    fallidos.append(fuente)
                    continue
                # Ids unicos por diagrama: sin esto, dos SVG podrian compartir id
                # y con el la hoja de estilos que mermaid les inyecta dentro.
                svg = ID_MERMAID_RE.sub(f"mermaid-{clave(fuente)}", svg)
                svgs[fuente] = _EN_MEMORIA[fuente] = svg
                (CACHE / f"{clave(fuente)}.svg").write_text(svg, encoding="utf-8")
                if verbose and hechos % 40 == 0:
                    print(f"  dibujados {hechos}/{len(tanda)}", flush=True)
        if verbose:
            print(f"  pasada {intento}: {len(tanda) - len(fallidos)}/{len(tanda)} dibujados",
                  flush=True)

    if fallidos:
        print(f"AVISO: {len(fallidos)} diagrama(s) no se pudieron dibujar tras "
              f"{REINTENTOS + 1} pasadas; el primero empieza por: {fallidos[0][:70]!r}")
    return svgs


# ── Rasterizado a PNG ───────────────────────────────────────────────────────


def _dimensiones(svg: str) -> tuple[int, int]:
    """Ancho y alto de la pagina en la que se fotografia el diagrama."""
    match = VIEWBOX_RE.search(svg)
    ancho, alto = (float(match.group(1)), float(match.group(2))) if match else (800.0, 400.0)
    if ancho <= 0 or alto <= 0:
        ancho, alto = 800.0, 400.0
    escala = min(1.0, PNG_ANCHO_MAX / ancho)
    return max(1, round(ancho * escala)), max(1, round(alto * escala))


def _pagina_png(svg: str, ancho: int, alto: int) -> str:
    # El SVG se fuerza al tamano exacto de la ventana para que la captura no
    # deje bordes ni recorte el diagrama.
    return (
        "<!doctype html><html><head><meta charset='utf-8'><style>"
        "html,body{margin:0;padding:0;background:#fff;}"
        f"svg{{display:block;width:{ancho}px;height:{alto}px;}}"
        "</style></head><body>" + svg + "</body></html>"
    )


def _optimizar_png(ruta: Path) -> None:
    """Reduce el peso del PNG con paleta. Si no hay Pillow, se deja tal cual."""
    try:
        from PIL import Image
    except ImportError:
        return
    with Image.open(ruta) as img:
        paleta = img.convert("RGB").convert(
            "P", palette=Image.Palette.ADAPTIVE, colors=PNG_COLORES
        )
        paleta.save(ruta, optimize=True)


def rasterizar(fuentes: list[str], nav: str | None = None, verbose: bool = True) -> dict[str, Path]:
    """Devuelve {codigo mermaid: ruta del PNG}. Cachea igual que los SVG."""
    svgs = dibujar(fuentes, nav=nav, verbose=verbose)
    if not svgs:
        return {}

    pngs: dict[str, Path] = {}
    pendientes: list[str] = []
    for fuente in svgs:
        ruta = CACHE / f"{clave(fuente)}.png"
        if ruta.is_file() and ruta.stat().st_size > 0:
            pngs[fuente] = ruta
        else:
            pendientes.append(fuente)

    if not pendientes:
        return pngs

    nav = nav or encontrar_navegador()
    if not nav:
        raise SystemExit("No se encontro Edge ni Chrome para rasterizar los diagramas.")
    if verbose:
        print(f"PNG: {len(pngs)} en cache, {len(pendientes)} por rasterizar.")

    def _capturar(fuente: str) -> Path | None:
        ancho, alto = _dimensiones(svgs[fuente])
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False,
                                         encoding="utf-8") as tmp:
            tmp.write(_pagina_png(svgs[fuente], ancho, alto))
            ruta_html = tmp.name
        destino = CACHE / f"{clave(fuente)}.png"
        try:
            subprocess.run(
                [nav, "--headless=new", "--disable-gpu", "--no-first-run",
                 "--no-default-browser-check", "--hide-scrollbars",
                 "--default-background-color=ffffffff",
                 f"--force-device-scale-factor={PNG_ESCALA}",
                 f"--window-size={ancho},{alto}",
                 f"--screenshot={destino}", "file:///" + ruta_html.replace("\\", "/")],
                capture_output=True, timeout=TIMEOUT_S,
            )
        except subprocess.TimeoutExpired:
            return None
        finally:
            Path(ruta_html).unlink(missing_ok=True)
        if not destino.is_file() or destino.stat().st_size == 0:
            return None
        _optimizar_png(destino)
        return destino

    hechos = 0
    with ThreadPoolExecutor(max_workers=PARALELO) as pool:
        futuros = {pool.submit(_capturar, f): f for f in pendientes}
        for futuro in as_completed(futuros):
            ruta = futuro.result()
            hechos += 1
            if ruta:
                pngs[futuros[futuro]] = ruta
            if verbose and hechos % 40 == 0:
                print(f"  rasterizados {hechos}/{len(pendientes)}", flush=True)

    return pngs


def fuentes_del_repositorio() -> list[str]:
    bloque = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
    fuentes: list[str] = []
    for md in sorted((ROOT / "classes").glob("parte-*/*/README.md")):
        fuentes.extend(bloque.findall(md.read_text(encoding="utf-8")))
    return fuentes


def main() -> int:
    fuentes = fuentes_del_repositorio()
    print(f"{len(fuentes)} bloques mermaid en las clases.")
    svgs = dibujar(fuentes)
    unicas = len(set(f.strip() for f in fuentes))
    pngs = rasterizar(fuentes)
    peso = sum(r.stat().st_size for r in pngs.values()) / 1024 / 1024
    print(f"Cache lista en {CACHE.relative_to(ROOT)}: "
          f"{len(svgs)}/{unicas} SVG y {len(pngs)}/{unicas} PNG ({peso:.1f} MB).")
    return 0 if len(svgs) == unicas and len(pngs) == unicas else 1


if __name__ == "__main__":
    raise SystemExit(main())
