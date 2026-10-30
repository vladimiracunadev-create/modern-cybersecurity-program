"""Pruebas de la tabla de plazos de CISA BOD 26-04 (`bod2604.py`) y de su integración con el priorizador.

La tabla se transcribió de la directiva oficial (consultada el 2026-10-30,
https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk,
Table 1). Estas pruebas la fijan fila a fila para que una edición accidental no la altere
sin que alguien lo note, y comprueban propiedades que cualquier tabla coherente debe cumplir.

    python -m unittest discover -s labs/devsecops-pipeline/tests -v
"""
from __future__ import annotations

import contextlib
import io
import itertools
import json
import sys
import unittest
from pathlib import Path
from unittest import mock

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

import bod2604 as B  # noqa: E402
import priorizar as P  # noqa: E402

SNAPSHOT = LAB / "datos" / "casos-cwe-cve.json"
EJEMPLO = LAB / "hallazgos-cwe-ejemplo.json"

# Table 1 de BOD 26-04, filas 1 a 16: (expuesto, KEV, automatizable, impacto) -> texto del plazo.
FILAS_OFICIALES = [
    (True, True, True, "total", "3 días y triaje forense"),
    (True, True, True, "partial", "3 días"),
    (True, True, False, "total", "3 días y triaje forense"),
    (True, True, False, "partial", "14 días"),
    (True, False, True, "total", "3 días"),
    (True, False, True, "partial", "14 días"),
    (True, False, False, "total", "14 días"),
    (True, False, False, "partial", "60 días"),
    (False, True, True, "total", "3 días y triaje forense"),
    (False, True, True, "partial", "14 días"),
    (False, True, False, "total", "14 días"),
    (False, True, False, "partial", "14 días"),
    (False, False, True, "total", "60 días"),
    (False, False, True, "partial", "60 días"),
    (False, False, False, "total", "próxima actualización"),
    (False, False, False, "partial", "próxima actualización"),
]


def texto_corto(r: dict) -> str:
    if r["dias"] is None:
        return "próxima actualización"
    return f"{r['dias']} días" + (" y triaje forense" if r["triaje_forense"] else "")


def urgencia(r: dict) -> float:
    return float("inf") if r["dias"] is None else r["dias"]


class TablaOficial(unittest.TestCase):
    def test_tiene_las_16_combinaciones(self):
        self.assertEqual(len(B.TABLA), 16)
        self.assertEqual(set(B.TABLA), set(itertools.product((True, False), (True, False), (True, False), B.IMPACTOS)))

    def test_cada_fila_coincide_con_la_directiva(self):
        for n, (exp, kev, auto, imp, esperado) in enumerate(FILAS_OFICIALES, 1):
            with self.subTest(fila=n):
                self.assertEqual(texto_corto(B.plazo(exp, kev, auto, imp)), esperado)

    def test_mas_riesgo_nunca_alarga_el_plazo(self):
        """Pasar de «no» a «sí» en exposición, KEV o automatización, o de parcial a total, no puede dar más tiempo."""
        for exp, kev, auto, imp in itertools.product((True, False), (True, False), (True, False), B.IMPACTOS):
            base = urgencia(B.plazo(exp, kev, auto, imp))
            mas = []
            if not exp:
                mas.append(B.plazo(True, kev, auto, imp))
            if not kev:
                mas.append(B.plazo(exp, True, auto, imp))
            if not auto:
                mas.append(B.plazo(exp, kev, True, imp))
            if imp == "partial":
                mas.append(B.plazo(exp, kev, auto, "total"))
            for r in mas:
                self.assertLessEqual(urgencia(r), base, (exp, kev, auto, imp))

    def test_el_triaje_forense_solo_aparece_con_plazo_de_3_dias_y_impacto_total(self):
        for (exp, kev, auto, imp), (dias, forense) in B.TABLA.items():
            if forense:
                self.assertEqual((dias, imp), (3, "total"))

    def test_el_mismo_cve_cambia_de_plazo_al_cambiar_la_exposicion(self):
        # Mismo CVE (KEV, automatizable, impacto total): expuesto -> 3 días y triaje; interno -> 3 días y triaje (fila 9)
        # pero si NO está en KEV, pasa de 3 días (fila 5) a 60 días (fila 13) solo por salir de Internet.
        self.assertEqual(B.plazo(True, False, True, "total")["dias"], 3)
        self.assertEqual(B.plazo(False, False, True, "total")["dias"], 60)

    def test_rechaza_un_impacto_invalido(self):
        with self.assertRaises(ValueError):
            B.plazo(True, True, True, "medio")


class HallazgoConSSVC(unittest.TestCase):
    SSVC = {"automatizable": "yes", "impacto_tecnico": "total", "explotacion": "active"}

    def test_exposicion_publica_cuenta_como_expuesto(self):
        self.assertEqual(B.plazo_de_hallazgo("publica", True, self.SSVC)["dias"], 3)

    def test_interna_y_no_alcanzable_no_cuentan_como_expuesto(self):
        self.assertEqual(B.plazo_de_hallazgo("interna", False, self.SSVC)["dias"], 60)
        self.assertEqual(B.plazo_de_hallazgo("no-alcanzable", False, {**self.SSVC, "automatizable": "no"})["dias"], None)

    def test_exposicion_desconocida_se_asume_expuesta_y_se_declara(self):
        r = B.plazo_de_hallazgo("desconocida", True, self.SSVC)
        self.assertEqual(r["dias"], 3)
        self.assertTrue(r["supuesto_de_exposicion"])
        self.assertFalse(B.plazo_de_hallazgo("publica", True, self.SSVC)["supuesto_de_exposicion"])

    def test_sin_datos_ssvc_no_se_inventa_un_plazo(self):
        self.assertIsNone(B.plazo_de_hallazgo("publica", True, None))
        self.assertIsNone(B.plazo_de_hallazgo("publica", True, {}))
        self.assertIsNone(B.plazo_de_hallazgo("publica", True, {"automatizable": "?", "impacto_tecnico": "total"}))


class IntegracionConElPriorizador(unittest.TestCase):
    def ejecutar(self, *args: str) -> tuple[int, str]:
        salida, err = io.StringIO(), io.StringIO()
        with mock.patch.object(sys, "argv", ["priorizar.py", *args]), \
                contextlib.redirect_stdout(salida), contextlib.redirect_stderr(err):
            codigo = P.main()
        return codigo, salida.getvalue() + err.getvalue()

    def test_los_plazos_del_informe_coinciden_con_la_tabla_y_los_datos_de_cisa(self):
        codigo, out = self.ejecutar("--hallazgos", str(EJEMPLO), "--instantanea", str(SNAPSHOT), "--bod-26-04")
        self.assertEqual(codigo, 0)
        self.assertIn("obligatoria solo para agencias civiles federales", out)
        casos = {c["cve"]: c for c in json.loads(SNAPSHOT.read_text(encoding="utf-8"))["casos"]}
        hallazgos = json.loads(EJEMPLO.read_text(encoding="utf-8"))
        for h in hallazgos:
            c = casos[h["cve"]]
            esperado = B.plazo_de_hallazgo(h.get("exposicion", "desconocida"), bool(c["kev"]), c["ssvc_cisa"])["texto"]
            self.assertIn(esperado, out, h["cve"])

    def test_heartbleed_expuesto_exige_3_dias_y_la_inyeccion_sql_9_8_sin_kev_60(self):
        _, out = self.ejecutar("--hallazgos", str(EJEMPLO), "--instantanea", str(SNAPSHOT), "--bod-26-04")
        bloque_openssl = out.split("CVE-2014-0160")[1].split("- [ ]")[0]
        bloque_netentsec = out.split("CVE-2024-2021")[1].split("- [ ]")[0]
        self.assertIn("**3 días naturales**", bloque_openssl)
        self.assertIn("**60 días naturales**", bloque_netentsec)

    def test_sin_el_flag_el_informe_no_cambia(self):
        _, sin = self.ejecutar("--hallazgos", str(EJEMPLO), "--instantanea", str(SNAPSHOT))
        self.assertNotIn("BOD 26-04", sin)

    def test_el_flag_exige_la_instantanea(self):
        codigo, out = self.ejecutar("--hallazgos", str(EJEMPLO), "--bod-26-04", "--sin-red")
        self.assertEqual(codigo, 1)
        self.assertIn("necesita --instantanea", out)

    def test_cada_caso_de_la_instantanea_trae_sus_puntos_ssvc(self):
        for c in json.loads(SNAPSHOT.read_text(encoding="utf-8"))["casos"]:
            with self.subTest(cve=c["cve"]):
                self.assertIn(c["ssvc_cisa"]["automatizable"], ("yes", "no"))
                self.assertIn(c["ssvc_cisa"]["impacto_tecnico"], B.IMPACTOS)
                self.assertIn(c["ssvc_cisa"]["explotacion"], ("none", "poc", "active"))


if __name__ == "__main__":
    unittest.main()
