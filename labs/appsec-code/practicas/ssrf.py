# -*- coding: utf-8 -*-
"""Práctica de la clase 363: falsificación de peticiones del lado del servidor (CWE-918).

Una función que descarga la URL que le indica el usuario convierte al servidor en un proxy hacia
dentro: puede alcanzar servicios internos y el servicio de metadatos de la nube (169.254.169.254).
Este módulo compara la versión vulnerable con una defensa que valida el DESTINO FINAL, no el texto
de la URL, y es la solución de referencia del reto de la clase 363.

Todo es determinista y sin red: el resolutor de nombres se inyecta, de modo que las pruebas dicen qué
dirección devuelve cada nombre (incluido el caso de un nombre permitido que resuelve a una dirección
interna, y el de un DNS que cambia de respuesta entre dos consultas).

    validar_url_vulnerable   solo mira el esquema: acepta cualquier destino          (CWE-918)
    resolver_destino         lista de destinos permitidos + dirección pública + dirección fijada
    seguir_redireccion       cada salto de una redirección se valida igual que el primero
"""
from __future__ import annotations

import ipaddress
from typing import Callable
from urllib.parse import urlsplit

Resolutor = Callable[[str], list[str]]

ESQUEMAS = ("http", "https")
PUERTOS = {"http": 80, "https": 443}


class DestinoNoPermitido(Exception):
    """La URL apunta a un destino que el servidor no debe alcanzar."""


# ---------------------------------------------------------------------------
# Versión vulnerable
# ---------------------------------------------------------------------------
def validar_url_vulnerable(url: str) -> str:
    """CWE-918: comprueba el esquema y nada más. `http://169.254.169.254/` pasa sin problema."""
    if urlsplit(url).scheme not in ESQUEMAS:
        raise DestinoNoPermitido("esquema no permitido")
    return url


# ---------------------------------------------------------------------------
# Versión correcta
# ---------------------------------------------------------------------------
def _es_publica(direccion: str) -> bool:
    """Una dirección es utilizable solo si es global (no privada, loopback, link-local, reservada...)."""
    ip = ipaddress.ip_address(direccion)
    if isinstance(ip, ipaddress.IPv6Address) and ip.ipv4_mapped is not None:
        ip = ip.ipv4_mapped  # ::ffff:127.0.0.1 es, a efectos prácticos, 127.0.0.1
    return ip.is_global and not ip.is_multicast


def resolver_destino(url: str, permitidos: set[str], resolutor: Resolutor) -> tuple[str, str, int]:
    """Valida la URL y devuelve (host, direccion_ip, puerto) a la que SÍ se puede conectar.

    Reglas, en este orden (cada una cierra una evasión conocida):
      1. esquema http o https (no `file:`, `gopher:`, etc.);
      2. sin credenciales en la URL (`https://permitido@169.254.169.254/` tiene como host el segundo);
      3. el host debe estar en la lista de permitidos, por nombre exacto: una lista de nombres no se
         puede esquivar escribiendo la dirección en decimal, hexadecimal u octal;
      4. el puerto debe ser el del esquema (no se escanean puertos internos);
      5. TODAS las direcciones a las que resuelve el nombre deben ser públicas: un nombre permitido
         cuyo DNS apunte a una dirección interna es el ataque de «DNS a medida»;
      6. se devuelve la dirección ya resuelta para conectar a ELLA y no volver a resolver el nombre
         (así un DNS que cambia de respuesta entre la comprobación y el uso no sirve de nada).
    """
    partes = urlsplit(url)
    if partes.scheme not in ESQUEMAS:
        raise DestinoNoPermitido("esquema no permitido")
    if partes.username is not None or partes.password is not None:
        raise DestinoNoPermitido("la URL no puede llevar credenciales")
    host = (partes.hostname or "").lower()
    if host not in {p.lower() for p in permitidos}:
        raise DestinoNoPermitido(f"host no permitido: {host or '(vacío)'}")
    try:
        puerto = partes.port or PUERTOS[partes.scheme]
    except ValueError as exc:
        raise DestinoNoPermitido("puerto inválido") from exc
    if puerto != PUERTOS[partes.scheme]:
        raise DestinoNoPermitido(f"puerto no permitido: {puerto}")
    direcciones = resolutor(host)
    if not direcciones:
        raise DestinoNoPermitido("el nombre no resuelve")
    try:
        malas = [d for d in direcciones if not _es_publica(d)]
    except ValueError as exc:
        raise DestinoNoPermitido("el resolutor devolvió algo que no es una dirección") from exc
    if malas:
        raise DestinoNoPermitido(f"resuelve a una dirección no pública: {malas[0]}")
    return host, direcciones[0], puerto


def seguir_redireccion(url_actual: str, location: str, permitidos: set[str], resolutor: Resolutor) -> tuple[str, str, int]:
    """Una redirección es una URL nueva: se valida con las mismas reglas que la original.

    Si el servidor remoto responde `302 Location: http://169.254.169.254/`, el cliente NO debe seguirla
    sin comprobarla. `location` puede ser relativa, y se resuelve contra la URL actual.
    """
    from urllib.parse import urljoin
    return resolver_destino(urljoin(url_actual, location), permitidos, resolutor)
