"""Pruebas de `discrepancias.py`: casos reales de la instantánea y casos sintéticos mínimos.

    python -m unittest discover -s labs/devsecops-pipeline/tests -v
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

import discrepancias as D  # noqa: E402

CASOS = D.cargar()


def tipos(cve: str) -> set[str]:
    return {h["tipo"] for h in D.discrepancias(CASOS[cve])}


class CasosReales(unittest.TestCase):
    def test_apache_2_4_49_nvd_y_cisa_adp_puntuan_distinto(self):
        h = next(x for x in D.discrepancias(CASOS["CVE-2021-41773"]) if x["tipo"] == "cvss_distinto")
        self.assertEqual(h["detalle"], {"CISA-ADP": 7.5, "NVD": 9.8})

    def test_regresshion_el_cna_elige_la_hija_y_nvd_el_padre(self):
        h = next(x for x in D.discrepancias(CASOS["CVE-2024-6387"]) if x["tipo"] == "cwe_distinto")
        self.assertEqual(h["detalle"], {"CNA": ["CWE-364"], "NVD (primario)": ["CWE-362"]})

    def test_rapid_reset_nvd_sin_cwe_pero_cisa_adp_aporta_uno(self):
        self.assertIn("nvd_sin_cwe_concreto", tipos("CVE-2023-44487"))

    def test_log4shell_tiene_cwe_pero_ninguno_primario(self):
        self.assertIn("sin_cwe_primario", tipos("CVE-2021-44228"))

    def test_fast_dds_el_cna_declara_una_puntuacion_que_no_es_la_de_su_vector(self):
        h = next(x for x in D.discrepancias(CASOS["CVE-2023-50716"]) if x["tipo"] == "puntuacion_vs_vector")
        self.assertEqual((h["detalle"]["declarada"], h["detalle"]["calculada"]), (9.7, 9.6))

    def test_netentsec_cna_y_nvd_difieren_en_tres_puntos(self):
        h = next(x for x in D.discrepancias(CASOS["CVE-2024-2021"]) if x["tipo"] == "cvss_distinto")
        self.assertEqual(h["detalle"], {"NVD": 9.8, "cna@vuldb.com": 6.3})

    def test_los_casos_consistentes_no_dan_falsos_positivos(self):
        for cve in ("CVE-2014-0160", "CVE-2017-5638", "CVE-2019-0708", "CVE-2021-3156", "CVE-2022-22965",
                    "CVE-2023-34362", "CVE-2023-4863", "CVE-2024-27565"):
            with self.subTest(cve=cve):
                self.assertEqual(D.discrepancias(CASOS[cve]), [])


class CasosSinteticos(unittest.TestCase):
    def test_sin_ninguna_puntuacion_se_avisa(self):
        self.assertEqual([h["tipo"] for h in D.discrepancias({"cve": "X", "cvss31": []})], ["sin_cvss_en_ninguna_fuente"])

    def test_diferencias_inferiores_a_una_decima_no_cuentan(self):
        caso = {"cvss31": [{"fuente": "A", "puntuacion": 7.0, "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N"},
                           {"fuente": "B", "puntuacion": 7.05, "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N"}]}
        self.assertNotIn("cvss_distinto", {h["tipo"] for h in D.discrepancias(caso)})

    def test_un_vector_invalido_no_rompe_la_deteccion(self):
        caso = {"cvss31": [{"fuente": "A", "puntuacion": 5.0, "vector": "CVSS:3.1/AV:N"}]}
        self.assertEqual(D.discrepancias(caso), [])

    def test_cna_y_nvd_con_el_mismo_cwe_no_discrepan(self):
        caso = {"cvss31": [{"fuente": "NVD", "puntuacion": 7.5, "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N"}],
                "cwe_cna": ["CWE-89"], "cwe_nvd": [{"id": "CWE-89", "tipo": "Primary", "fuente": "NVD"}]}
        self.assertEqual(D.discrepancias(caso), [])


if __name__ == "__main__":
    unittest.main()
