# -*- coding: utf-8 -*-
"""Práctica de la clase 363: subida de archivos sin restricciones (CWE-434).

Aceptar un archivo y guardarlo con el nombre y el contenido que elige el cliente permite colocar
código ejecutable en el servidor. Este módulo compara la versión vulnerable con una defensa en capas
y es la referencia de la sección sobre `CWE-434` de la clase 363.

La defensa NO confía en lo que dice el cliente:

  1. la extensión final debe estar en una lista de permitidas;
  2. el CONTENIDO debe corresponder al tipo declarado (primeros bytes, o «números mágicos»);
  3. hay un tamaño máximo;
  4. el archivo se guarda con un nombre generado por el servidor (el nombre original se descarta, así
     que `../../x`, `shell.php` o `foto.php.png` no llegan al sistema de archivos);
  5. se guarda sin permisos de ejecución, fuera de cualquier directorio que se sirva como código.

Es una defensa de implementación: el diseño completo (almacén de objetos separado, análisis antimalware,
servir con `Content-Disposition` y un dominio distinto) se discute en la clase.
"""
from __future__ import annotations

import os
import uuid
from pathlib import Path
from typing import Callable

# extensión -> firmas válidas al inicio del contenido
FIRMAS: dict[str, tuple[bytes, ...]] = {
    ".png": (b"\x89PNG\r\n\x1a\n",),
    ".jpg": (b"\xff\xd8\xff",),
    ".pdf": (b"%PDF-",),
}
MAXIMO_BYTES = 1_000_000


class SubidaRechazada(Exception):
    """El archivo no cumple alguna de las reglas de aceptación."""


# ---------------------------------------------------------------------------
# Versión vulnerable
# ---------------------------------------------------------------------------
def guardar_vulnerable(nombre: str, contenido: bytes, directorio: Path) -> Path:
    """CWE-434: usa el nombre del cliente tal cual y no mira el contenido.

    Un archivo `perfil.php` (o `.py`, `.jsp`...) acaba en el directorio con su extensión ejecutable;
    si ese directorio se sirve como código, subir el archivo equivale a ejecutarlo.
    """
    destino = directorio / os.path.basename(nombre)
    destino.write_bytes(contenido)
    return destino


# ---------------------------------------------------------------------------
# Versión correcta
# ---------------------------------------------------------------------------
def _extension_final(nombre: str) -> str:
    return os.path.splitext(os.path.basename(nombre.replace("\\", "/")))[1].lower()


def guardar_correcto(nombre: str, contenido: bytes, directorio: Path,
                     generar_nombre: Callable[[], str] = lambda: uuid.uuid4().hex) -> Path:
    """Valida extensión, contenido y tamaño, y guarda con un nombre generado por el servidor."""
    ext = _extension_final(nombre)
    if ext not in FIRMAS:
        raise SubidaRechazada(f"extensión no permitida: {ext or '(ninguna)'}")
    if len(contenido) > MAXIMO_BYTES:
        raise SubidaRechazada("archivo demasiado grande")
    if not any(contenido.startswith(firma) for firma in FIRMAS[ext]):
        raise SubidaRechazada("el contenido no corresponde a la extensión declarada")
    directorio = Path(directorio)
    destino = directorio / f"{generar_nombre()}{ext}"
    if destino.resolve().parent != directorio.resolve():
        raise SubidaRechazada("destino fuera del directorio de subidas")
    destino.write_bytes(contenido)
    try:
        os.chmod(destino, 0o644)  # lectura y escritura del propietario, lectura del resto; nunca ejecución
    except OSError:
        pass  # en sistemas de archivos sin permisos POSIX no hay nada que quitar
    return destino
