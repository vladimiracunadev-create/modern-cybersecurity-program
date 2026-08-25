#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Publicar un fichero generado sin dejarlo a medias (y sin perderlo por el antivirus).

Los generadores escriben primero a `<destino>.tmp` y luego mueven el temporal
encima del definitivo. Asi una interrupcion nunca deja un PDF truncado en el
repositorio, y —lo que motivo este modulo— un fallo de escritura deja de ser
invisible.

El caso real: al regenerar los 340 PDF de clase de golpe, el antivirus de Windows
se queda escaneando los ficheros recien escritos y mantiene mapeado el anterior.
Mientras dura, truncarlo devuelve EINVAL y renombrar encima devuelve "Acceso
denegado". Como el navegador imprime con stderr silenciado, el sintoma era que la
clase conservaba su PDF viejo **sin que nadie se enterara**: el generador decia
"[OK]" y el fichero seguia siendo el de antes.

La espera resuelve el caso normal (el antivirus suelta el fichero en segundos).
Si aun asi no se puede publicar, se lanza la excepcion: es preferible parar a
seguir generando material que en realidad no se esta actualizando.
"""
from __future__ import annotations

import os
import time

INTENTOS = 8
ESPERA_INICIAL = 0.5


def reemplazar(origen: str, destino: str, intentos: int = INTENTOS) -> None:
    """Mueve `origen` sobre `destino`, reintentando si el sistema lo bloquea."""
    espera = ESPERA_INICIAL
    for intento in range(1, intentos + 1):
        try:
            os.replace(origen, destino)
            return
        except OSError:
            if intento == intentos:
                raise
            time.sleep(espera)
            espera = min(espera * 2, 8.0)


def publicar(origen: str, destino: str, minimo_bytes: int = 0) -> None:
    """Comprueba que el temporal es plausible y lo publica como definitivo."""
    if not os.path.isfile(origen):
        raise RuntimeError(f"no se genero el fichero temporal: {origen}")
    tam = os.path.getsize(origen)
    if tam < minimo_bytes:
        raise RuntimeError(
            f"el fichero generado es demasiado pequeno para ser valido "
            f"({tam} bytes, minimo {minimo_bytes}): {destino}"
        )
    reemplazar(origen, destino)
