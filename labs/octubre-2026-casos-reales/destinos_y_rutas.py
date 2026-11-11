#!/usr/bin/env python3
"""Validación de destinos (SSRF), rutas (path traversal) y argumentos (inyección de comandos).

Tres familias que aparecen en el catálogo KEV de octubre de 2026 (Plex, Fortinet, Cisco,
Atlassian, Collabora, Ahsay, EG Secure Solutions). Cada función «vulnerable» **no ejecuta
nada ni abre ninguna conexión**: devuelve la decisión que tomaría un servidor ingenuo para que
puedas razonar sobre ella y compararla con la versión corregida. Solo biblioteca estándar.

Las implementaciones vulnerables son **didácticas y ficticias**: no reproducen el código de
ningún producto real (los avisos de fabricante no publican ese código y aquí no se infiere).
"""
from __future__ import annotations

import ipaddress
import posixpath
import re
from urllib.parse import unquote, urlsplit

# --------------------------------------------------------------------------- SSRF (CWE-918, CWE-84)

PUERTOS_PERMITIDOS = {80, 443}
ESQUEMAS_PERMITIDOS = {"http", "https"}


def construir_destino_vulnerable(protocolo: str, host: str, ruta: str = "/timeline") -> str:
    """Servidor ingenuo: el cliente aporta el «protocolo» y el servidor lo concatena sin validar.

    Es el patrón descrito para el campo `protocol` de CVE-2026-96652 (una URL completa en un
    parámetro que debía ser un esquema). Devuelve la URL a la que el servidor haría un POST.
    """
    if "://" in protocolo:  # el cliente entrega la URL completa y manda él
        return protocolo
    return f"{protocolo}://{host}{ruta}"


def _es_privada(ip: ipaddress._BaseAddress) -> bool:
    return (ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_multicast
            or ip.is_reserved or ip.is_unspecified)


def validar_destino(url: str, resolver: dict[str, list[str]], permitidos: set[str] | None = None) -> tuple[bool, str]:
    """Decide si el servidor puede conectarse a `url`. Devuelve (permitido, motivo).

    Reglas, en el orden en que importan:
    1. esquema en lista cerrada (http/https): bloquea `file:`, `gopher:`, `ftp:`...
    2. sin credenciales embebidas (`usuario@host`) que confundan al lector humano;
    3. puerto en lista cerrada;
    4. el nombre se **resuelve** y se comprueban *todas* las direcciones resultantes: filtrar el
       texto del host no sirve, porque `localtest.me`, `2130706433` o `0x7f.1` apuntan a loopback;
    5. ninguna dirección privada, de loopback, link-local (incluye 169.254.169.254, metadatos de nube),
       multicast o reservada;
    6. si hay lista de destinos permitidos, el host debe estar en ella (lo más fuerte: lista cerrada).

    `resolver` simula el DNS para que la prueba sea determinista y no toque la red. En producción hay que
    **conectar a la IP ya validada** (no volver a resolver) para evitar el cambio de respuesta DNS entre
    la comprobación y el uso (*DNS rebinding*, TOCTOU).
    """
    partes = urlsplit(url)
    if partes.scheme.lower() not in ESQUEMAS_PERMITIDOS:
        return False, f"esquema no permitido: {partes.scheme or '(vacío)'}"
    if partes.username or partes.password:
        return False, "credenciales embebidas en la URL"
    host = partes.hostname
    if not host:
        return False, "sin host"
    puerto = partes.port or (443 if partes.scheme == "https" else 80)
    if puerto not in PUERTOS_PERMITIDOS:
        return False, f"puerto no permitido: {puerto}"
    if permitidos is not None and host.lower() not in permitidos:
        return False, f"host fuera de la lista cerrada: {host}"
    try:
        literales = [ipaddress.ip_address(host)]
    except ValueError:
        literales = []
    direcciones = [str(i) for i in literales] or resolver.get(host.lower(), [])
    if not direcciones:
        return False, "el nombre no resuelve"
    for d in direcciones:
        if _es_privada(ipaddress.ip_address(d)):
            return False, f"resuelve a una dirección no pública: {d}"
    return True, "ok"


# --------------------------------------------------------------------------- Rutas (CWE-22, 23, 73, 158)

def ruta_vulnerable(base: str, nombre: str) -> str:
    """Une `base` y `nombre` sin comprobar nada: `../` sale del directorio."""
    return posixpath.normpath(posixpath.join(base, nombre))


def ruta_segura(base: str, nombre: str) -> tuple[str | None, str]:
    """Devuelve la ruta normalizada dentro de `base`, o (None, motivo).

    Orden: (1) decodificar **una sola vez** hasta un punto fijo y rechazar si cambia más de una vez
    (la doble codificación `%252e%252e` es una evasión clásica); (2) rechazar NUL (CWE-158), barra
    invertida y rutas absolutas; (3) normalizar y comprobar que el resultado **sigue dentro** de `base`.
    La comprobación final sobre la ruta *resuelta* es la que importa: las anteriores solo acotan formas.
    """
    actual = nombre
    for _ in range(2):
        siguiente = unquote(actual)
        if siguiente == actual:
            break
        actual = siguiente
    else:
        if unquote(actual) != actual:
            return None, "codificación múltiple"
    if "\x00" in actual:
        return None, "byte nulo"
    if "\\" in actual:
        return None, "barra invertida"
    if actual.startswith("/"):
        return None, "ruta absoluta"
    destino = posixpath.normpath(posixpath.join(base, actual))
    base_n = posixpath.normpath(base)
    if destino != base_n and not destino.startswith(base_n + "/"):
        return None, "sale del directorio base"
    return destino, "ok"


# --------------------------------------------------------------------------- Comandos (CWE-77, 78)

METACARACTERES = set(";|&$`<>(){}\n\\'\"* ?!#~")
HOST_VALIDO = re.compile(r"^(?=.{1,253}$)([A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)*[A-Za-z0-9]([A-Za-z0-9-]{0,61}[A-Za-z0-9])?$")


def linea_de_shell_vulnerable(host: str) -> str:
    """Construye la línea que un servidor ingenuo pasaría a `sh -c`. No se ejecuta."""
    return f"ping -c 1 {host}"


def comandos_que_ejecutaria_un_shell(linea: str) -> list[str]:
    """Cuenta cuántos comandos independientes vería un shell POSIX en la línea (modelo simplificado).

    Separadores considerados: `;`, `&&`, `||`, `|`, salto de línea y sustitución `$()` / backticks.
    Sirve para demostrar que el valor «8.8.8.8; id» deja de ser un host: son dos órdenes.
    """
    sust = re.findall(r"\$\(([^)]*)\)|`([^`]*)`", linea)
    cuerpo = re.sub(r"\$\([^)]*\)|`[^`]*`", "", linea)
    trozos = [t.strip() for t in re.split(r";|&&|\|\||\||\n", cuerpo) if t.strip()]
    return trozos + [a or b for a, b in sust]


def argv_seguro(host: str) -> tuple[list[str] | None, str]:
    """Valida `host` con lista blanca y devuelve el argv (sin shell). Un argv no se reinterpreta."""
    if any(c in METACARACTERES for c in host):
        return None, "metacaracteres de shell"
    if not HOST_VALIDO.match(host):
        return None, "no es un nombre de host válido"
    if host.startswith("-"):
        return None, "podría interpretarse como opción"
    return ["ping", "-c", "1", "--", host], "ok"
