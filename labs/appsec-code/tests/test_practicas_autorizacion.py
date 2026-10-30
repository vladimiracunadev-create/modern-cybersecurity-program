"""Pruebas de la práctica de la clase 364 (`practicas/autorizacion.py`).

    python -m unittest discover -s labs/appsec-code/tests -v
"""
from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB / "practicas"))

import autorizacion as A  # noqa: E402


class MatrizDeAcceso(unittest.TestCase):
    def test_la_version_vulnerable_viola_la_politica_en_las_parejas_ajenas(self):
        # Ana lee el documento de Luis y Luis el de Ana: exactamente las dos parejas prohibidas.
        self.assertEqual(A.violaciones(A.leer_vulnerable), [("ana", 2), ("luis", 1)])

    def test_la_version_con_comprobacion_equivocada_tambien_falla(self):
        # CWE-863: comprueba el rol, no la relación con el recurso.
        self.assertEqual(A.violaciones(A.leer_con_error), [("ana", 2), ("luis", 1)])

    def test_la_version_correcta_cumple_la_politica_en_las_seis_parejas(self):
        self.assertEqual(A.violaciones(A.leer_correcto), [])

    def test_un_identificador_inexistente_y_uno_ajeno_dan_la_misma_respuesta(self):
        with self.assertRaises(A.Denegado) as ajeno:
            A.leer_correcto("luis", 1)
        with self.assertRaises(A.Denegado) as inexistente:
            A.leer_correcto("luis", 999)
        self.assertEqual(str(ajeno.exception), str(inexistente.exception))  # no permite enumerar IDs

    def test_un_usuario_desconocido_se_deniega_por_defecto(self):
        with self.assertRaises(A.Denegado):
            A.leer_correcto("intruso", 1)

    def test_la_matriz_cubre_todas_las_parejas(self):
        self.assertEqual(len(A.matriz_de_acceso(A.leer_correcto)), len(A.USUARIOS) * len(A.DOCUMENTOS))


class AutorizacionDeFuncion(unittest.TestCase):
    def setUp(self):
        self._copia = copy.deepcopy(A.DOCUMENTOS)

    def tearDown(self):
        A.DOCUMENTOS.clear()
        A.DOCUMENTOS.update(self._copia)

    def test_cualquiera_borra_en_la_version_vulnerable(self):
        self.assertTrue(A.borrar_vulnerable("ana", 2))
        self.assertNotIn(2, A.DOCUMENTOS)  # Ana borró el documento de Luis

    def test_solo_el_admin_borra_en_la_version_correcta(self):
        with self.assertRaises(A.Denegado):
            A.borrar_correcto("ana", 2)
        self.assertIn(2, A.DOCUMENTOS)          # no se borró nada
        self.assertTrue(A.borrar_correcto("root", 2))
        self.assertNotIn(2, A.DOCUMENTOS)

    def test_borrar_algo_que_no_existe_no_rompe_al_admin(self):
        self.assertFalse(A.borrar_correcto("root", 999))


if __name__ == "__main__":
    unittest.main()
