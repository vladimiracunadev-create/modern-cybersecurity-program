# -*- coding: utf-8 -*-
"""Extraccion y resolucion de las fuentes que citan las clases del programa.

Modulo compartido por `scripts/verify-sources` (offline, bloquea en CI) y
`scripts/refresh-sources` (en red, no bloquea). Aqui vive la unica definicion
de que cuenta como fuente, como se normaliza y como se resuelve contra el
registro `sources/bibliography.json`.

Regla de oro: este modulo no inventa nada. Solo lee lo que las clases ya
declaran y lo compara con el registro.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
REGISTRO = RAIZ / "sources" / "bibliography.json"
CLASES_GLOB = "classes/*/*/README.md"

# La seccion de fuentes de una clase. El programa usa un unico encabezado, pero
# aceptamos las variantes habituales para que anadir "## Fuentes" no deje un
# bloque sin detectar en silencio: una fuente no extraida es una fuente no
# auditada, y ese es justo el fallo que este trabajo viene a cerrar.
RE_ENCABEZADO_FUENTES = re.compile(
    r"^#{2,4}\s+.*(Referencias|Fuentes|Bibliograf)", re.IGNORECASE
)
RE_ENCABEZADO = re.compile(r"^#{2,4}\s+")
RE_VINETA = re.compile(r"^\s*[-*]\s+(.*)$")
RE_URL = re.compile(r"https?://[^\s<>)\]`\"']+")
RE_MD_LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

# Vinetas que no son fuentes bibliograficas.
RE_NOTA_EMPRESA = re.compile(r"(^|\s)(\U0001F3E2|\*\*En la empresa)")
RE_SOLO_INTERNO = re.compile(r"^(\.\.?/|#|/)")
# Remisiones a otras partes o clases del propio programa: no son bibliografia.
RE_REMISION_INTERNA = re.compile(
    r"(?i)(partes?|clases?)\s.*\bdel (programa|curso)\b|\bdel programa\.?$"
)

# Marcas con las que una clase declara para que usa la fuente, no solo cual es.
RE_PROPOSITO = re.compile(
    r"(cap\.|caps\.|capitulos?|capitulo|apendice|secc\.|seccion|dominios?|"
    r"clausula|controles?\s|anexo|parte\s|pags?\.|vol\.|"
    r"—|–|\s-\s|\([^)]{6,}\))",
    re.IGNORECASE,
)


def _sin_tildes(texto: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn"
    )


def normaliza_url(url: str) -> str:
    """Forma canonica comparable de una URL: sin fragmento ni barra final."""
    url = url.rstrip(".,;:)")
    url = re.sub(r"#.*$", "", url)
    if url.endswith("/") and url.count("/") > 3:
        url = url[:-1]
    return url


def sin_esquema(url: str) -> str:
    """La URL sin http/https ni www, para comparar cita y locator.

    Una clase que cita http://phrack.org y un locator https://phrack.org
    apuntan al mismo recurso: el esquema no debe partir la resolucion.
    """
    url = normaliza_url(url)
    url = re.sub(r"^https?://", "", url)
    return re.sub(r"^www\.", "", url).rstrip("/")


def clave_texto(texto: str) -> str:
    """Clave de comparacion de una obra citada sin URL.

    Baja a minusculas, quita tildes, enfasis Markdown y puntuacion. No recorta
    el detalle de uso (cap., dominio...): eso se conserva porque es informacion.
    """
    t = _sin_tildes(texto.lower())
    t = re.sub(r"[*_`\"’']", "", t)
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return " ".join(t.split())


@dataclass
class Uso:
    """Una vineta del bloque de fuentes de una clase."""

    clase: str
    parte: str
    linea: int
    crudo: str
    urls: list = field(default_factory=list)
    tipo: str = "bibliografica"  # bibliografica | interna | nota

    @property
    def declara_uso(self) -> bool:
        """Si la vineta dice para que usa esa fuente la clase, no solo cual es."""
        cuerpo = RE_URL.sub("", self.crudo)
        cuerpo = RE_MD_LINK.sub(r"\1", cuerpo)
        return bool(RE_PROPOSITO.search(cuerpo))


def _clasifica(crudo: str, urls: list, enlaces_md: list) -> str:
    if RE_NOTA_EMPRESA.search(crudo):
        return "nota"
    if not urls:
        if RE_REMISION_INTERNA.search(crudo):
            return "interna"
        # Sin URL externa: es interno solo si todo lo que enlaza es del repo.
        if enlaces_md and all(RE_SOLO_INTERNO.match(d.strip()) for _, d in enlaces_md):
            return "interna"
        return "bibliografica"
    return "bibliografica"


def lee_clases(raiz: Path = RAIZ) -> list:
    return sorted(raiz.glob(CLASES_GLOB))


def extrae_bloque(ruta: Path) -> tuple:
    """Devuelve las lineas del bloque de fuentes y la linea donde empieza."""
    lineas = ruta.read_text(encoding="utf-8").splitlines()
    dentro = False
    inicio = -1
    bloque = []
    for i, linea in enumerate(lineas, 1):
        if not dentro and RE_ENCABEZADO_FUENTES.match(linea):
            dentro, inicio = True, i
            continue
        if dentro and RE_ENCABEZADO.match(linea):
            break
        if dentro:
            bloque.append(linea)
    return bloque, inicio


def extrae_usos(raiz: Path = RAIZ) -> tuple:
    """Extrae todas las vinetas de fuentes y el texto de cada bloque por clase."""
    usos = []
    bloques = {}
    for ruta in lee_clases(raiz):
        rel = ruta.relative_to(raiz).as_posix()
        parte = rel.split("/")[1]
        bloque, inicio = extrae_bloque(ruta)
        vinetas = []
        for desplazamiento, linea in enumerate(bloque):
            m = RE_VINETA.match(linea)
            if not m:
                continue
            crudo = m.group(1).strip()
            if not crudo:
                continue
            vinetas.append(crudo)
            urls = [normaliza_url(u) for u in RE_URL.findall(crudo)]
            enlaces = RE_MD_LINK.findall(crudo)
            usos.append(
                Uso(
                    clase=rel,
                    parte=parte,
                    linea=inicio + 1 + desplazamiento,
                    crudo=crudo,
                    urls=urls,
                    tipo=_clasifica(crudo, urls, enlaces),
                )
            )
        bloques[rel] = "\n".join(vinetas)
    return usos, bloques


# --------------------------------------------------------------------------
# Registro
# --------------------------------------------------------------------------


def carga_registro(ruta: Path = REGISTRO) -> dict:
    return json.loads(ruta.read_text(encoding="utf-8"))


def digito_control_isbn13(isbn: str) -> bool:
    """Valida el digito de control de un ISBN-13 (norma ISO 2108)."""
    digitos = re.sub(r"[^0-9Xx]", "", isbn or "")
    if len(digitos) != 13 or not digitos.isdigit():
        return False
    suma = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digitos[:12]))
    return (10 - suma % 10) % 10 == int(digitos[12])


class Resolutor:
    """Resuelve un Uso contra las entradas del registro.

    Dos vias, en este orden:
      1. por URL: gana el prefijo declarado mas largo (el mas especifico);
      2. por texto: patrones declarados en la entrada, sobre la clave normalizada.
    """

    def __init__(self, registro: dict):
        self.entradas = registro["entries"]
        self._por_prefijo = []
        self._patrones = []
        for e in self.entradas:
            m = e.get("matches", {})
            for prefijo in m.get("url_prefixes", []):
                self._por_prefijo.append((sin_esquema(prefijo), e["id"]))
            for patron in m.get("text_patterns", []):
                self._patrones.append((re.compile(patron, re.IGNORECASE), e["id"]))
        # Prefijo mas largo primero: /pubs/sp/800/53 gana sobre /pubs/sp.
        self._por_prefijo.sort(key=lambda p: -len(p[0]))

    def por_url(self, url: str):
        url = sin_esquema(url)
        for prefijo, ident in self._por_prefijo:
            if url == prefijo or url.startswith(prefijo.rstrip("/") + "/"):
                return ident
        return None

    def por_texto(self, crudo: str) -> list:
        clave = clave_texto(crudo)
        return [ident for patron, ident in self._patrones if patron.search(clave)]

    def resuelve(self, uso: Uso) -> tuple:
        """Devuelve (ids resueltos, urls sin entrada en el registro)."""
        ids = []
        huerfanas = []
        for url in uso.urls:
            ident = self.por_url(url)
            if ident:
                ids.append(ident)
            else:
                huerfanas.append(url)
        ids.extend(self.por_texto(uso.crudo))
        vistos = []
        for i in ids:
            if i not in vistos:
                vistos.append(i)
        return vistos, huerfanas
