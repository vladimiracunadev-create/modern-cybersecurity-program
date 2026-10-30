# -*- coding: utf-8 -*-
"""Práctica de las clases 365 y 366: agotamiento de recursos y falta de límites (CWE-770, CWE-400, CWE-307).

Una aplicación que acepta trabajo sin límite deja que un cliente decida cuántos recursos del
servidor consume. El catálogo CWE lo describe como «asignación de recursos sin límites ni
limitación de tasa» (CWE-770, hija de la clase CWE-400, consumo no controlado de recursos).

Dos defensas básicas, ambas con el reloj inyectable para que las pruebas sean deterministas:

  * `leer_acotado`:       no leer más de un máximo de bytes de un flujo (límite de tamaño).
  * `LimitadorDeTasa`:    algoritmo del «cubo de fichas» (token bucket): limita cuántas peticiones por segundo.
  * `ControlDeIntentos`:  bloqueo temporal tras demasiados intentos fallidos (CWE-307).
"""
from __future__ import annotations

import io
from typing import Callable


class LimiteExcedido(Exception):
    """El cliente superó un límite de tamaño o de tasa."""


# ---------------------------------------------------------------------------
# Límite de tamaño
# ---------------------------------------------------------------------------
def leer_sin_limite(flujo: io.BufferedIOBase) -> bytes:
    """CWE-770: lee TODO lo que envíe el cliente. Un cuerpo de varios GB agota la memoria."""
    return flujo.read()


def leer_acotado(flujo: io.BufferedIOBase, maximo: int) -> bytes:
    """Lee como mucho `maximo` bytes y falla si hay más, sin llegar a cargarlos en memoria.

    Se pide `maximo + 1` bytes: si llegan `maximo + 1`, el cuerpo excede el límite. Así se detecta
    el exceso leyendo un solo byte de más, no el cuerpo entero.
    """
    datos = flujo.read(maximo + 1)
    if len(datos) > maximo:
        raise LimiteExcedido(f"el cuerpo supera {maximo} bytes")
    return datos


# ---------------------------------------------------------------------------
# Limitación de tasa: cubo de fichas
# ---------------------------------------------------------------------------
class LimitadorDeTasa:
    """Cada cliente tiene un «cubo» con capacidad `capacidad` que se rellena a `fichas_por_segundo`.

    Cada petición gasta una ficha. Sin fichas, se rechaza. Permite ráfagas cortas (hasta la capacidad)
    pero impide un ritmo sostenido mayor que el configurado. `reloj` devuelve segundos y es inyectable:
    en producción es `time.monotonic`; en las pruebas, un reloj falso que avanzamos a mano.
    """

    def __init__(self, capacidad: int, fichas_por_segundo: float, reloj: Callable[[], float]):
        if capacidad <= 0 or fichas_por_segundo <= 0:
            raise ValueError("capacidad y tasa deben ser positivas")
        self.capacidad = capacidad
        self.tasa = fichas_por_segundo
        self._reloj = reloj
        self._cubos: dict[str, tuple[float, float]] = {}   # cliente -> (fichas, instante de la última actualización)

    def permitir(self, cliente: str) -> bool:
        ahora = self._reloj()
        fichas, ultimo = self._cubos.get(cliente, (float(self.capacidad), ahora))
        fichas = min(self.capacidad, fichas + (ahora - ultimo) * self.tasa)   # recarga proporcional al tiempo
        if fichas >= 1:
            self._cubos[cliente] = (fichas - 1, ahora)
            return True
        self._cubos[cliente] = (fichas, ahora)
        return False


# ---------------------------------------------------------------------------
# Intentos de autenticación: CWE-307
# ---------------------------------------------------------------------------
class ControlDeIntentos:
    """Bloquea una cuenta `bloqueo_s` segundos tras `maximo` fallos seguidos. Un acierto reinicia la cuenta.

    Sin esto, un atacante puede probar contraseñas sin freno (CWE-307, «restricción indebida de intentos
    excesivos de autenticación»). Matiz importante: el bloqueo por cuenta puede usarse para BLOQUEAR a un
    usuario legítimo a propósito (denegación de servicio selectiva); por eso se combina con limitación por origen
    y bloqueos que expiran, no permanentes.
    """

    def __init__(self, maximo: int, bloqueo_s: float, reloj: Callable[[], float]):
        self.maximo, self.bloqueo_s, self._reloj = maximo, bloqueo_s, reloj
        self._fallos: dict[str, int] = {}
        self._bloqueado_hasta: dict[str, float] = {}

    def esta_bloqueada(self, cuenta: str) -> bool:
        return self._reloj() < self._bloqueado_hasta.get(cuenta, 0.0)

    def registrar(self, cuenta: str, acierto: bool) -> None:
        if acierto:
            self._fallos.pop(cuenta, None)
            return
        self._fallos[cuenta] = self._fallos.get(cuenta, 0) + 1
        if self._fallos[cuenta] >= self.maximo:
            self._bloqueado_hasta[cuenta] = self._reloj() + self.bloqueo_s
            self._fallos[cuenta] = 0
