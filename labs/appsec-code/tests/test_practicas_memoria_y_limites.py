"""Pruebas de las prácticas de las clases 365 y 366 (`practicas/memoria_y_carreras.py` y `practicas/limites.py`).

Nada depende del azar: la memoria es simulada, el reloj es falso y las carreras se fuerzan con una barrera.

    python -m unittest discover -s labs/appsec-code/tests -v
"""
from __future__ import annotations

import io
import random
import sys
import threading
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB / "practicas"))

import limites as LIM  # noqa: E402
import memoria_y_carreras as M  # noqa: E402


class CadenaEnteroABuffer(unittest.TestCase):
    """CWE-190 -> CWE-787, la cadena que el catálogo nombra CWE-680."""

    def test_el_producto_da_la_vuelta_en_32_bits(self):
        self.assertEqual(M.tamano_vulnerable(0x2000_0000, 8), 0)            # 2**32 vale 0 en 32 bits
        self.assertEqual(M.tamano_vulnerable(0x2000_0001, 8), 8)            # 2**32 + 8 vale 8
        self.assertEqual(M.tamano_vulnerable(10, 8), 80)                    # sin desbordar, todo normal

    def test_el_resultado_desbordado_es_siempre_el_producto_modulo_2_a_la_32(self):
        azar = random.Random(7)  # semilla fija: la prueba es reproducible
        for _ in range(500):
            n, t = azar.randrange(0, 2**33), azar.choice([1, 2, 4, 8, 16, 24])
            self.assertEqual(M.tamano_vulnerable(n, t), (n * t) % 2**32)

    def test_el_buffer_diminuto_recibe_escrituras_fuera_de_limites(self):
        buf = M.copiar_vulnerable(0x2000_0000)
        self.assertEqual(buf.tamano, 0)                    # se reservó un buffer vacío...
        self.assertEqual(len(buf.fuera_de_limites), 1000)  # ...y todas las escrituras se salen (CWE-787)

    def test_corregir_el_calculo_elimina_la_escritura_fuera_de_limites(self):
        """Se corrige el eslabón RAÍZ (la aritmética) y desaparece la consecuencia (la escritura)."""
        with self.assertRaises(OverflowError):
            M.copiar_correcto(0x2000_0000)
        buf = M.copiar_correcto(100)
        self.assertEqual(buf.tamano, 800)
        self.assertEqual(buf.fuera_de_limites, [])

    def test_la_comprobacion_previa_coincide_con_la_aritmetica_de_enteros_grandes(self):
        azar = random.Random(11)
        for _ in range(500):
            n, t = azar.randrange(0, 2**33), azar.choice([1, 2, 4, 8, 16])
            cabe = n * t <= 0xFFFF_FFFF
            if cabe:
                self.assertEqual(M.tamano_correcto(n, t), n * t)
            else:
                with self.assertRaises(OverflowError):
                    M.tamano_correcto(n, t)

    def test_operandos_invalidos_se_rechazan(self):
        for n, t in ((-1, 8), (5, 0), (5, -4)):
            with self.assertRaises(OverflowError):
                M.tamano_correcto(n, t)


class ErrorDeUno(unittest.TestCase):
    def test_un_bucle_con_menor_o_igual_escribe_un_byte_de_mas(self):
        self.assertEqual(M.rellenar_vulnerable(8).fuera_de_limites, [8])
        self.assertEqual(M.rellenar_vulnerable(0).fuera_de_limites, [0])   # el caso límite también falla

    def test_la_version_correcta_no_se_sale_nunca(self):
        for n in (0, 1, 2, 8, 255, 1024):
            self.assertEqual(M.rellenar_correcto(n).fuera_de_limites, [], n)


class CondicionDeCarrera(unittest.TestCase):
    def test_dos_retiradas_simultaneas_vacian_mas_de_lo_que_hay(self):
        # Saldo 100 y dos retiradas de 80: solo una debería prosperar.
        for _ in range(3):
            cuenta = M.CuentaVulnerable(100, threading.Barrier(2))
            resultados = M.retirada_concurrente(cuenta, 80)
            self.assertEqual(resultados, [True, True])      # las DOS pasaron la comprobación
            self.assertEqual(cuenta.saldo, -60)             # el saldo queda negativo (CWE-362/367)

    def test_con_cerrojo_solo_prospera_una_y_el_saldo_nunca_es_negativo(self):
        for _ in range(3):
            cuenta = M.CuentaCorrecta(100, threading.Barrier(2))
            resultados = M.retirada_concurrente(cuenta, 80)
            self.assertEqual(sorted(resultados), [False, True])
            self.assertEqual(cuenta.saldo, 20)

    def test_sin_concurrencia_ambas_versiones_se_comportan_igual(self):
        # La debilidad solo aparece con concurrencia: una prueba secuencial no la detecta.
        for clase in (M.CuentaVulnerable, M.CuentaCorrecta):
            c = clase(100)
            self.assertTrue(c.retirar(80))
            self.assertFalse(c.retirar(80))
            self.assertEqual(c.saldo, 20)


class FlujoAcotado(unittest.TestCase):
    def test_sin_limite_lee_todo(self):
        self.assertEqual(len(LIM.leer_sin_limite(io.BytesIO(b"x" * 5000))), 5000)

    def test_con_limite_acepta_exactamente_el_maximo_y_rechaza_uno_mas(self):
        self.assertEqual(len(LIM.leer_acotado(io.BytesIO(b"x" * 1000), 1000)), 1000)
        with self.assertRaises(LIM.LimiteExcedido):
            LIM.leer_acotado(io.BytesIO(b"x" * 1001), 1000)

    def test_el_exceso_se_detecta_sin_cargar_el_cuerpo_entero(self):
        flujo = io.BytesIO(b"x" * 10_000_000)
        with self.assertRaises(LIM.LimiteExcedido):
            LIM.leer_acotado(flujo, 1000)
        self.assertEqual(flujo.tell(), 1001)               # solo se leyó un byte de más


class RelojFalso:
    def __init__(self, t: float = 0.0):
        self.t = t

    def __call__(self) -> float:
        return self.t


class LimitacionDeTasa(unittest.TestCase):
    def test_permite_la_rafaga_y_rechaza_el_exceso(self):
        reloj = RelojFalso()
        lim = LIM.LimitadorDeTasa(capacidad=3, fichas_por_segundo=1, reloj=reloj)
        self.assertEqual([lim.permitir("a") for _ in range(4)], [True, True, True, False])

    def test_se_recarga_con_el_tiempo_sin_pasar_de_la_capacidad(self):
        reloj = RelojFalso()
        lim = LIM.LimitadorDeTasa(3, 1, reloj)
        for _ in range(3):
            lim.permitir("a")
        reloj.t = 1.0
        self.assertTrue(lim.permitir("a"))                 # una ficha recuperada
        self.assertFalse(lim.permitir("a"))
        reloj.t = 1000.0
        self.assertEqual([lim.permitir("a") for _ in range(4)], [True, True, True, False])  # tope = capacidad

    def test_cada_cliente_tiene_su_cubo(self):
        lim = LIM.LimitadorDeTasa(1, 0.1, RelojFalso())
        self.assertTrue(lim.permitir("a"))
        self.assertFalse(lim.permitir("a"))
        self.assertTrue(lim.permitir("b"))                 # un cliente no gasta las fichas del otro

    def test_parametros_invalidos(self):
        for args in ((0, 1), (1, 0), (-1, 1)):
            with self.assertRaises(ValueError):
                LIM.LimitadorDeTasa(*args, reloj=RelojFalso())


class IntentosDeAutenticacion(unittest.TestCase):
    def test_se_bloquea_tras_los_fallos_y_se_desbloquea_con_el_tiempo(self):
        reloj = RelojFalso()
        ctl = LIM.ControlDeIntentos(maximo=3, bloqueo_s=60, reloj=reloj)
        for _ in range(3):
            self.assertFalse(ctl.esta_bloqueada("ana"))
            ctl.registrar("ana", acierto=False)
        self.assertTrue(ctl.esta_bloqueada("ana"))
        reloj.t = 59.9
        self.assertTrue(ctl.esta_bloqueada("ana"))
        reloj.t = 60.1
        self.assertFalse(ctl.esta_bloqueada("ana"))        # el bloqueo expira: no es permanente

    def test_un_acierto_reinicia_la_cuenta(self):
        ctl = LIM.ControlDeIntentos(3, 60, RelojFalso())
        ctl.registrar("ana", False)
        ctl.registrar("ana", False)
        ctl.registrar("ana", True)
        ctl.registrar("ana", False)
        ctl.registrar("ana", False)
        self.assertFalse(ctl.esta_bloqueada("ana"))        # los fallos anteriores al acierto ya no cuentan

    def test_el_bloqueo_es_por_cuenta(self):
        ctl = LIM.ControlDeIntentos(1, 60, RelojFalso())
        ctl.registrar("ana", False)
        self.assertTrue(ctl.esta_bloqueada("ana"))
        self.assertFalse(ctl.esta_bloqueada("luis"))


if __name__ == "__main__":
    unittest.main()
