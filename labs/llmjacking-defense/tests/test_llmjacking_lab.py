import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import llmjacking_lab as L  # noqa: E402
import secret_scan as S  # noqa: E402


class Determinismo(unittest.TestCase):
    def test_misma_semilla_mismos_eventos(self):
        self.assertEqual(L.generar(3)["eventos"], L.generar(3)["eventos"])

    def test_semillas_distintas_difieren(self):
        self.assertNotEqual(L.generar(3)["eventos"], L.generar(4)["eventos"])

    def test_ips_solo_en_rangos_de_documentacion_o_privados(self):
        permitidos = ("10.", "192.0.2.", "198.51.100.", "203.0.113.")
        for e in L.generar(1)["eventos"]:
            self.assertTrue(e["source_ip"].startswith(permitidos), e["source_ip"])

    def test_los_ocho_escenarios_estan_presentes(self):
        esc = {e["scenario"] for e in L.generar(1)["eventos"]}
        for s in ("S1-normal", "S2-clave-expuesta", "S3-consumo-anomalo", "S4-validacion-minima",
                  "S5-ollama-expuesto", "S6-privilegios-excesivos", "S7-contencion", "S8-rafaga-legitima"):
            self.assertIn(s, esc)


class Formulas(unittest.TestCase):
    def test_mad_robusta_ignora_un_atipico(self):
        med, sig = L.mad_robusta([10, 11, 9, 10, 10, 1000])
        self.assertEqual(med, 10)
        self.assertLess(sig, 3)  # la media/desviacion clasicas explotarian con el 1000

    def test_z_con_piso_no_divide_por_cero(self):
        self.assertAlmostEqual(L.z_robusto(2.0, 1.0, 0.0), 10.0)

    def test_costo_es_lineal_en_tokens(self):
        self.assertAlmostEqual(L.costo("m-large", 2000, 1000), 2 * 0.015 + 1 * 0.075)


class Deteccion(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.res = {s: L.ejecutar(s) for s in (1, 2, 3)}

    def test_cada_incidente_se_detecta_en_menos_de_20_minutos(self):
        for s, r in self.res.items():
            for inc, m in r["metricas"]["incidentes"].items():
                self.assertIsNotNone(m["latencia_s"], f"seed {s} {inc} no detectado")
                self.assertLessEqual(m["latencia_s"], 1200, f"seed {s} {inc}")

    def test_recall_completo_y_precision_alta(self):
        for s, r in self.res.items():
            self.assertEqual(r["metricas"]["recall"], 1.0, s)
            self.assertGreaterEqual(r["metricas"]["precision"], 0.95, s)

    def test_la_rafaga_legitima_no_genera_alertas_con_contexto(self):
        det = self.res[1]["_det"]
        falsas = [x for x in det["ventanas"] if x["alerta"] and x["identity"] == "svc-summarizer"]
        self.assertEqual(falsas, [])

    def test_sin_contexto_la_rafaga_se_marca_pero_sin_alertar_por_una_sola_senal(self):
        det = L.detectar(self.res[1]["_datos"], usar_contexto=False)
        ventanas = [x for x in det["ventanas"] if x["identity"] == "svc-summarizer"
                    and 9 * 3600 <= x["inicio"] - L.T0 - 14 * L.DIA < 12 * 3600]
        self.assertTrue(any(x["senales"] for x in ventanas))
        for x in ventanas:  # solo senales de volumen: no cumplen "2 senales independientes + 4 puntos"
            self.assertFalse(x["alerta"], x["senales"])

    def test_ninguna_senal_aislada_alcanza_el_umbral(self):
        self.assertTrue(all(w < L.UMBRAL_PUNTOS for w in L.PESOS.values()) or L.MIN_SENALES >= 2)
        self.assertGreaterEqual(L.MIN_SENALES, 2)

    def test_la_alerta_es_hipotesis_no_atribucion(self):
        det = self.res[1]["_det"]
        for x in det["ventanas"]:
            if x["alerta"]:
                self.assertIn("hipotesis", x["hipotesis"])

    def test_geolocalizacion_no_es_una_senal(self):
        self.assertNotIn("geolocalizacion", L.PESOS)
        self.assertEqual(L.PESOS["origen_nuevo"], 1)


class Controles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        r = L.ejecutar(1)
        cls.exp = r["exposicion"]

    def test_alerta_de_presupuesto_sola_no_reduce_el_gasto_de_un_incidente_corto(self):
        for v in self.exp["por_incidente"].values():
            self.assertEqual(v["solo_alerta_presupuesto"], v["sin_control"])

    def test_deteccion_y_tope_reducen_la_exposicion(self):
        for v in self.exp["por_incidente"].values():
            self.assertLess(v["deteccion_y_revocacion"], v["sin_control"])
            self.assertLess(v["tope_duro"], v["sin_control"])
        # INC-A se detecta en el barrido de validacion, antes de la fase de consumo: la deteccion
        # temprana cuesta menos que dejar que el tope diario se agote.
        a = self.exp["por_incidente"]["INC-A"]
        self.assertLess(a["deteccion_y_revocacion"], a["tope_duro"])

    def test_el_tope_duro_tiene_costo_colateral_y_el_cambio_aprobado_lo_reduce(self):
        c = self.exp["colateral_benigno_denegado"]
        self.assertGreater(c["tope_sin_contexto"], 0)
        self.assertLess(c["tope_con_cambio_aprobado"], c["tope_sin_contexto"])

    def test_el_atacante_agota_la_cuota_y_deniega_trafico_legitimo(self):
        # Lo observado por Sysdig (2024): el abuso puede impedir el uso legitimo del modelo.
        por = self.exp["colateral_benigno_denegado"]["por_identidad_sin_contexto"]
        self.assertGreater(por.get("svc-chatbot", 0), 0)


class Contencion(unittest.TestCase):
    def test_tras_la_revocacion_el_atacante_recibe_403_y_no_factura(self):
        ev = L.generar(1)["eventos"]
        post = [e for e in ev if e["scenario"] == "S7-contencion" and e["action"] == "InvokeModel"]
        self.assertTrue(post)
        self.assertTrue(all(e["status"] == 403 and e["cost_usd"] == 0 for e in post))

    def test_la_recuperacion_usa_clave_nueva_y_origen_conocido(self):
        ev = [e for e in L.generar(1)["eventos"] if e["scenario"] == "S7-recuperacion"
              and e["action"] == "InvokeModel"]
        self.assertTrue(all(e["key_id"] == "k2" and e["source_ip"].startswith("10.") for e in ev))


class Exportacion(unittest.TestCase):
    def test_ecs_ndjson_valido_y_reproducible(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = Path(d) / "a.ndjson", Path(d) / "b.ndjson"
            n = L.exportar_ecs(L.generar(2), a)
            L.exportar_ecs(L.generar(2), b)
            self.assertEqual(a.read_bytes(), b.read_bytes())
            lineas = a.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lineas), n)
            doc = json.loads(lineas[0])
            self.assertIn("@timestamp", doc)

    def test_el_informe_menciona_limites_y_es_estable(self):
        with tempfile.TemporaryDirectory() as d:
            L.ejecutar(5, Path(d) / "x")
            L.ejecutar(5, Path(d) / "y")
            tx = (Path(d) / "x" / "informe.md").read_text(encoding="utf-8")
            self.assertEqual(tx, (Path(d) / "y" / "informe.md").read_text(encoding="utf-8"))
            self.assertIn("no una atribución", tx.replace("es una anomalía,", "es una anomalía,"))


class Secretos(unittest.TestCase):
    # Los fixtures se construyen en tiempo de ejecucion: el repo no contiene cadenas con
    # forma de clave, de modo que los escaneres de secretos del CI no tienen nada que marcar.
    def _claves(self):
        return {
            "aws-access-key-id": "AK" + "IA" + "ABCDEFGHIJKLMNOP",
            "clave-llm-prefijo-sk": "sk" + "-" + "a1" * 20,
            "huggingface-token": "hf" + "_" + "B" * 34,
        }

    def test_detecta_formatos_y_oculta_el_valor(self):
        for regla, clave in self._claves().items():
            h = S.escanear_texto(f"TOKEN={clave}\n")
            self.assertEqual([x["regla"] for x in h], [regla])
            self.assertNotIn(clave, json.dumps(h))

    def test_no_marca_texto_comun(self):
        self.assertEqual(S.escanear_texto("el modelo sk-learn no es una clave\n"), [])

    def test_ollama_loopback_bajo_y_todas_las_interfaces_alto(self):
        self.assertEqual(S.evaluar_bind_ollama(None)["riesgo"], "bajo")
        self.assertEqual(S.evaluar_bind_ollama("0.0.0.0:11434")["riesgo"], "alto")
        self.assertEqual(S.evaluar_bind_ollama("0.0.0.0:11434", True)["riesgo"], "medio")
        self.assertEqual(S.evaluar_bind_ollama("[::]:11434")["riesgo"], "alto")
        self.assertEqual(S.evaluar_bind_ollama("localhost:11434")["riesgo"], "bajo")

    def test_el_laboratorio_no_importa_modulos_de_red(self):
        for modulo in ("llmjacking_lab.py", "secret_scan.py"):
            src = (Path(__file__).resolve().parents[1] / modulo).read_text(encoding="utf-8")
            for prohibido in ("import socket", "import requests", "urllib.request", "import http"):
                self.assertNotIn(prohibido, src, f"{modulo}: {prohibido}")


if __name__ == "__main__":
    unittest.main()
