# -*- coding: utf-8 -*-
"""Práctica de la clase 365: memoria, enteros y concurrencia (CWE-190, 193, 787, 362/367, 770).

Por qué en Python
-----------------
Los fallos de memoria clásicos ocurren en C o C++. Python comprueba límites y no los
permite, así que para estudiarlos sin compilador y sin riesgo se SIMULA la memoria: la clase
`BufferSimulado` registra las escrituras fuera de límites en lugar de corromper nada. Así se ve
el mecanismo exacto de la cadena

    desbordamiento de entero (CWE-190)  ->  buffer demasiado pequeño  ->  escritura fuera de límites (CWE-787)

que el catálogo CWE nombra como la cadena CWE-680, y se prueba la corrección. Para ver el efecto
real en C, usa el laboratorio de la clase 128 (`intov.c`) con sanitizers.

Todo es determinista: ni hilos que dependan del azar ni memoria real.
"""
from __future__ import annotations

import threading
from dataclasses import dataclass, field

MASCARA_32 = 0xFFFF_FFFF  # un entero sin signo de 32 bits solo guarda los 32 bits bajos


# ---------------------------------------------------------------------------
# Memoria simulada: registra lo que en C sería corrupción silenciosa
# ---------------------------------------------------------------------------
@dataclass
class BufferSimulado:
    """Un buffer de tamaño fijo que anota las escrituras que se salen de sus límites."""

    tamano: int
    datos: bytearray = field(init=False)
    fuera_de_limites: list[int] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.datos = bytearray(self.tamano)

    def escribir(self, indice: int, valor: int) -> None:
        if 0 <= indice < self.tamano:
            self.datos[indice] = valor & 0xFF
        else:
            # En C esta escritura sobrescribiría memoria vecina. Aquí solo se registra.
            self.fuera_de_limites.append(indice)


# ---------------------------------------------------------------------------
# CWE-190 -> CWE-787: la cadena CWE-680
# ---------------------------------------------------------------------------
def tamano_vulnerable(n: int, tam_elemento: int) -> int:
    """CWE-190: n * tam_elemento calculado en 32 bits SIN SIGNO «da la vuelta» si no cabe.

    Con n = 0x20000000 (536.870.912) y 8 bytes por elemento, el producto real es 2**32, que en
    32 bits vale 0: se reservaría un buffer de tamaño 0 para guardar 536 millones de elementos.
    """
    return (n * tam_elemento) & MASCARA_32


def copiar_vulnerable(n: int, tam_elemento: int = 8) -> BufferSimulado:
    """Reserva con el tamaño desbordado y escribe los n elementos: CWE-787 como consecuencia."""
    buf = BufferSimulado(tamano_vulnerable(n, tam_elemento))
    for i in range(min(n, 1000)):          # tope solo para que la práctica termine; el patrón es el mismo
        buf.escribir(i * tam_elemento, 0x41)
    return buf


def tamano_correcto(n: int, tam_elemento: int) -> int:
    """Comprueba ANTES de calcular: ¿cabe el producto en 32 bits? Si no, se rechaza.

    Es la aritmética segura: validar los operandos, no confiar en el resultado ya desbordado.
    (En C: `__builtin_mul_overflow`, o comprobar `n > SIZE_MAX / tam_elemento` antes de multiplicar.)
    """
    if n < 0 or tam_elemento <= 0 or n > MASCARA_32 // tam_elemento:
        raise OverflowError("el tamaño solicitado no cabe en 32 bits")
    return n * tam_elemento


def copiar_correcto(n: int, tam_elemento: int = 8) -> BufferSimulado:
    buf = BufferSimulado(tamano_correcto(n, tam_elemento))
    for i in range(min(n, 1000)):
        buf.escribir(i * tam_elemento, 0x41)
    return buf


# ---------------------------------------------------------------------------
# CWE-193: error de uno (off-by-one)
# ---------------------------------------------------------------------------
def rellenar_vulnerable(n: int) -> BufferSimulado:
    """Bucle con `<=`: escribe n+1 elementos en un buffer de n. Un solo byte de más (CWE-193)."""
    buf = BufferSimulado(n)
    for i in range(n + 1):                 # BUG: debería ser range(n)
        buf.escribir(i, 0x42)
    return buf


def rellenar_correcto(n: int) -> BufferSimulado:
    buf = BufferSimulado(n)
    for i in range(n):
        buf.escribir(i, 0x42)
    return buf


# ---------------------------------------------------------------------------
# CWE-362 / CWE-367: condición de carrera (comprobar y usar no es atómico)
# ---------------------------------------------------------------------------
class CuentaVulnerable:
    """Comprueba el saldo y, DESPUÉS, lo descuenta: entre ambos pasos otro hilo puede colarse.

    `punto_de_encuentro` fuerza que los dos hilos hayan hecho ya la comprobación antes de que
    cualquiera actualice. Es un artificio para que la práctica sea determinista: en un programa
    real la ventana existe igual y se acierta o no según el azar del planificador, que es
    justo lo que hace a estas debilidades tan difíciles de reproducir y de detectar.
    """

    def __init__(self, saldo: int, punto_de_encuentro: threading.Barrier | None = None):
        self.saldo = saldo
        self._barrera = punto_de_encuentro

    def retirar(self, monto: int) -> bool:
        if self.saldo >= monto:                       # COMPROBAR
            if self._barrera is not None:
                try:
                    self._barrera.wait(timeout=2)     # los dos hilos llegan aquí antes de seguir
                except threading.BrokenBarrierError:
                    pass
            self.saldo -= monto                       # USAR (el saldo comprobado ya puede ser falso)
            return True
        return False


class CuentaCorrecta:
    """Comprobar y descontar forman una sola operación atómica gracias a un cerrojo."""

    def __init__(self, saldo: int, punto_de_encuentro: threading.Barrier | None = None):
        self.saldo = saldo
        self._cerrojo = threading.Lock()
        self._barrera = punto_de_encuentro

    def retirar(self, monto: int) -> bool:
        with self._cerrojo:                           # solo un hilo a la vez entra aquí
            if self.saldo >= monto:
                if self._barrera is not None:
                    try:
                        # Con el cerrojo, el segundo hilo no puede llegar: este tiempo agotado
                        # demuestra que la ventana de la versión vulnerable ya no existe.
                        self._barrera.wait(timeout=0.2)
                    except threading.BrokenBarrierError:
                        pass
                self.saldo -= monto
                return True
            return False


def retirada_concurrente(cuenta, monto: int, hilos: int = 2) -> list[bool]:
    """Lanza `hilos` retiradas simultáneas y devuelve el resultado de cada una."""
    resultados: list[bool] = [False] * hilos

    def tarea(i: int) -> None:
        resultados[i] = cuenta.retirar(monto)

    ts = [threading.Thread(target=tarea, args=(i,)) for i in range(hilos)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return resultados
