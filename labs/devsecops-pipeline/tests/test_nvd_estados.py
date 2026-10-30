"""Pruebas de `nvd_estados.py`: el recuento se prueba sin red con registros de la misma forma que devuelve la API de NVD.

    python -m unittest discover -s labs/devsecops-pipeline/tests -v
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

import nvd_estados as N  # noqa: E402


def cve(estado, v31_fuentes=(), v40=False, cwe_fuentes=()):
    metricas = {}
    if v31_fuentes:
        metricas["cvssMetricV31"] = [{"source": s} for s in v31_fuentes]
    if v40:
        metricas["cvssMetricV40"] = [{"source": "cna@x"}]
    return {"cve": {"vulnStatus": estado, "metrics": metricas,
                    "weaknesses": [{"source": s, "type": "Primary", "description": []} for s in cwe_fuentes]}}


MUESTRA = [
    cve("Analyzed", ("nvd@nist.gov", "cna@x"), cwe_fuentes=("nvd@nist.gov",)),
    cve("Analyzed", ("cna@x",), cwe_fuentes=("cna@x",)),
    cve("Deferred", ("cna@x",), v40=True, cwe_fuentes=("cna@x",)),
    cve("Deferred"),
    cve("Awaiting Analysis", v40=True),
    cve("Rejected"),
]


class Recuento(unittest.TestCase):
    def test_cuenta_los_estados(self):
        c = N.contar(MUESTRA)
        self.assertEqual(c["leidos"], 6)
        self.assertEqual(c["estados"], {"Analyzed": 2, "Awaiting Analysis": 1, "Deferred": 2, "Rejected": 1})

    def test_distingue_el_dato_publicado_por_nvd_del_de_cualquier_fuente(self):
        c = N.contar(MUESTRA)
        self.assertEqual(c["con_cvss31_publicado_por_nvd"], 1)
        self.assertEqual(c["con_cvss31_de_cualquier_fuente"], 3)
        self.assertEqual(c["con_cwe_asignado_por_nvd"], 1)
        self.assertEqual(c["con_cwe_de_cualquier_fuente"], 3)
        self.assertEqual(c["con_cvss40_de_alguna_fuente"], 2)

    def test_los_porcentajes_suman_cien(self):
        p = N.porcentajes(N.contar(MUESTRA))
        self.assertAlmostEqual(sum(p.values()), 100.0, delta=0.3)

    def test_una_lista_vacia_no_divide_por_cero(self):
        self.assertEqual(N.porcentajes(N.contar([])), {})

    def test_cubre_todos_los_estados_de_la_api_con_su_nombre_web(self):
        for estado in ("Received", "Awaiting Analysis", "Undergoing Analysis", "Analyzed", "Modified", "Deferred", "Rejected"):
            self.assertIn(estado, N.NOMBRE_WEB)
        self.assertEqual(N.NOMBRE_WEB["Deferred"], "Not Scheduled")


class DatosVersionados(unittest.TestCase):
    """La foto guardada es coherente consigo misma (la clase 367 cita sus cifras)."""

    @classmethod
    def setUpClass(cls):
        cls.d = json.loads((LAB / "datos" / "nvd-estados-2026-09-01_10.json").read_text(encoding="utf-8"))

    def test_los_estados_suman_el_total(self):
        self.assertEqual(sum(self.d["estados"].values()), self.d["leidos"])
        self.assertEqual(self.d["leidos"], self.d["procedencia"]["total_segun_nvd"])

    def test_declara_ventana_fecha_y_advertencia(self):
        p = self.d["procedencia"]
        self.assertEqual(p["ventana_de_publicacion"], "2026-09-01..2026-09-10")
        self.assertRegex(p["fecha_consulta"], r"^\d{4}-\d{2}-\d{2}$")
        self.assertIn("Foto", p["advertencia"])

    def test_los_datos_de_nvd_son_una_fraccion_de_los_de_cualquier_fuente(self):
        self.assertLess(self.d["con_cvss31_publicado_por_nvd"], self.d["con_cvss31_de_cualquier_fuente"])
        self.assertLess(self.d["con_cwe_asignado_por_nvd"], self.d["con_cwe_de_cualquier_fuente"])


if __name__ == "__main__":
    unittest.main()
