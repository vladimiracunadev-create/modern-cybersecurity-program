"""Pruebas de la calculadora CVSS (`cvss.py`).

El criterio de verdad no es esta implementación sino los números que otros
publicaron: NVD, los CNA y los ejemplos oficiales de FIRST. Si la calculadora
se aparta de uno solo, es la calculadora la que está mal.

    python -m unittest discover -s labs/devsecops-pipeline/tests -v
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

import cvss  # noqa: E402

ORACULO = json.loads((Path(__file__).resolve().parent / "datos" / "cvss-verificados.json").read_text(encoding="utf-8"))


class OraculoPublicado(unittest.TestCase):
    def test_v31_reproduce_las_puntuaciones_de_nvd_y_cna(self):
        self.assertGreaterEqual(len(ORACULO["v31"]), 20)
        for r in ORACULO["v31"]:
            with self.subTest(cve=r["cve"], fuente=r["fuente"]):
                self.assertEqual(cvss.puntuar(r["vector"])["base"], r["puntuacion"], r["vector"])

    def test_v40_reproduce_las_puntuaciones_publicadas_por_los_cna(self):
        self.assertGreaterEqual(len(ORACULO["v40_cna"]), 30)
        for r in ORACULO["v40_cna"]:
            with self.subTest(cve=r["cve"], proveedor=r["proveedor"]):
                self.assertEqual(cvss.puntuar(r["vector"])["puntuacion"], r["puntuacion"], r["vector"])

    def test_v40_reproduce_los_ejemplos_oficiales_de_first_con_amenaza_y_entorno(self):
        for r in ORACULO["v40_ejemplos_first"]:
            with self.subTest(vector=r["vector"][:60]):
                self.assertEqual(cvss.puntuar(r["vector"])["puntuacion"], r["puntuacion"], r["vector"])


class SeveridadYNomenclatura(unittest.TestCase):
    def test_limites_de_la_escala_cualitativa(self):
        casos = {0.0: "None", 0.1: "Low", 3.9: "Low", 4.0: "Medium", 6.9: "Medium",
                 7.0: "High", 8.9: "High", 9.0: "Critical", 10.0: "Critical"}
        for puntos, esperado in casos.items():
            self.assertEqual(cvss.severidad(puntos), esperado, puntos)

    def test_nomenclatura_v40_indica_que_grupos_se_usaron(self):
        base = "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N"
        self.assertEqual(cvss.puntuar(base)["nomenclatura"], "CVSS-B")
        self.assertEqual(cvss.puntuar(base + "/E:A")["nomenclatura"], "CVSS-BT")
        self.assertEqual(cvss.puntuar(base + "/CR:H")["nomenclatura"], "CVSS-BE")
        self.assertEqual(cvss.puntuar(base + "/E:P/CR:L")["nomenclatura"], "CVSS-BTE")

    def test_metricas_suplementarias_de_v40_no_cambian_la_puntuacion(self):
        base = "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N"
        con = base + "/S:P/AU:Y/R:U/V:C/RE:H/U:Red"
        self.assertEqual(cvss.puntuar(con)["puntuacion"], cvss.puntuar(base)["puntuacion"])

    def test_sin_impacto_la_puntuacion_es_cero(self):
        v4 = "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:N/SC:N/SI:N/SA:N"
        v31 = "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:N"
        self.assertEqual(cvss.puntuar(v4)["puntuacion"], 0.0)
        self.assertEqual(cvss.puntuar(v31)["base"], 0.0)


class PropiedadesDeV31(unittest.TestCase):
    BASE = "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"

    def test_roundup_evita_el_error_de_coma_flotante(self):
        # En binario 0.1 + 0.2 = 0.30000000000000004; un redondeo ingenuo daría 0.4.
        self.assertEqual(cvss.roundup(0.1 + 0.2), 0.3)
        self.assertEqual(cvss.roundup(4.02), 4.1)   # siempre hacia arriba
        self.assertEqual(cvss.roundup(4.0), 4.0)
        self.assertEqual(cvss.roundup(9.999), 10.0)

    def test_temporal_no_supera_la_base_y_defaults_la_igualan(self):
        r = cvss.puntuar(self.BASE + "/E:U/RL:O/RC:U")
        self.assertLess(r["temporal"], r["base"])
        igual = cvss.puntuar(self.BASE + "/E:H/RL:U/RC:C")
        self.assertEqual(igual["temporal"], igual["base"])

    def test_temporal_se_comprueba_a_mano_con_los_pesos_de_la_especificacion(self):
        # Cálculo manual con la tabla 16 de la especificación v3.1: base 7.5 con
        # E:F (0.97), RL:O (0.95), RC:C (1.0) => 7.5 × 0.97 × 0.95 = 6.91 => Roundup = 7.0.
        r = cvss.puntuar("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N/E:F/RL:O/RC:C")
        self.assertEqual((r["base"], r["temporal"]), (7.5, 7.0))

    def test_entorno_sin_cambios_reproduce_la_base(self):
        # Declarar como modificadas exactamente las métricas base no debe mover la nota.
        v = self.BASE + "/MAV:N/MAC:L/MPR:N/MUI:N/MS:U/MC:H/MI:H/MA:H"
        self.assertEqual(cvss.puntuar(v)["ambiental"], cvss.puntuar(self.BASE)["base"])

    def test_requisito_de_seguridad_bajo_reduce_y_alto_aumenta_pero_no_pasa_de_10(self):
        base = "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L"
        bajo = cvss.puntuar(base + "/CR:L/IR:L/AR:L")["ambiental"]
        alto = cvss.puntuar(base + "/CR:H/IR:H/AR:H")["ambiental"]
        self.assertLess(bajo, cvss.puntuar(base)["base"])
        self.assertGreater(alto, cvss.puntuar(base)["base"])
        self.assertLessEqual(cvss.puntuar(self.BASE + "/CR:H/IR:H/AR:H")["ambiental"], 10.0)

    def test_aislar_el_activo_baja_la_nota_modificando_el_vector_de_ataque(self):
        # El mismo fallo, pero el activo solo es alcanzable con acceso físico.
        r = cvss.puntuar(self.BASE + "/MAV:P")
        self.assertLess(r["ambiental"], r["base"])

    def test_el_alcance_cambiado_pesa_mas_el_privilegio_bajo(self):
        sin = cvss.puntuar("CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H")["base"]
        con = cvss.puntuar("CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H")["base"]
        self.assertEqual((sin, con), (8.8, 9.9))

    def test_el_resultado_trae_los_pasos_del_calculo(self):
        r = cvss.puntuar(self.BASE)
        self.assertTrue(any("ISS" in p for p in r["pasos"]))
        self.assertEqual(r["nomenclatura"], "CVSS-B")


class ValidacionDeVectores(unittest.TestCase):
    def malo(self, vector):
        with self.assertRaises(cvss.VectorInvalido, msg=vector):
            cvss.puntuar(vector)

    def test_rechaza_vectores_mal_formados(self):
        self.malo("")
        self.malo("AV:N/AC:L")
        self.malo("CVSS:9.9/AV:N")
        self.malo("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H")            # falta A
        self.malo("CVSS:3.1/AV:Z/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H")        # valor inválido
        self.malo("CVSS:3.1/AV:N/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H")   # repetida
        self.malo("CVSS:3.1/XX:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H")        # métrica desconocida
        self.malo("CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H")    # faltan SC/SI/SA
        self.malo("CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:X")

    def test_el_calculo_de_cada_version_rechaza_la_otra(self):
        with self.assertRaises(cvss.VectorInvalido):
            cvss.puntuar_v31("CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N")
        with self.assertRaises(cvss.VectorInvalido):
            cvss.puntuar_v40("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H")

    def test_cli_devuelve_error_en_vector_invalido(self):
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(cvss.main(["CVSS:3.1/AV:N"]), 1)
            self.assertEqual(cvss.main(["CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"]), 0)

    def test_las_tablas_de_v40_estan_completas(self):
        t = cvss._tablas_v4()
        self.assertEqual(len(t["tabla_macrovectores"]), 270)
        self.assertIn("BSD-2-Clause", t["procedencia"]["licencia"])
        self.assertTrue((LAB / "datos" / "cvss4" / "LICENSE-FIRST-CVSS-v4-BSD-2.txt").is_file())


class MismaVulnerabilidadDosVersiones(unittest.TestCase):
    def test_v31_y_v40_no_son_comparables_directamente(self):
        # Ejemplo oficial de FIRST (fallo de NGINX con ataque local): v3.1 -> 7.0, v4.0 -> 7.3.
        # Cada versión mide con otro modelo; que difieran no significa que una esté mal.
        v31 = cvss.puntuar("CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H")["base"]
        v40 = cvss.puntuar("CVSS:4.0/AV:L/AC:L/AT:P/PR:L/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N")["puntuacion"]
        self.assertEqual((v31, v40), (7.0, 7.3))


if __name__ == "__main__":
    unittest.main()
