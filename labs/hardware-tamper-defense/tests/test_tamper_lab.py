import copy
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import tamper_lab as T  # noqa: E402


class Placa(unittest.TestCase):
    def test_muestra_a_coincide(self):
        c = T.comparar_pcb(T.REFERENCIA, T.muestras()["MUESTRA-A"])
        self.assertEqual(c["hallazgos"], [])

    def test_muestra_b_detecta_cinco_anadidos_criticos(self):
        c = T.comparar_pcb(T.REFERENCIA, T.muestras()["MUESTRA-B"])
        self.assertEqual(c["anadidos"], ["X1", "X2", "X3", "X4", "X5"])
        self.assertTrue(all(h["severidad"] == "alta" for h in c["hallazgos"] if h["ref"].startswith("X")))

    def test_secure_element_no_se_toca_en_b(self):
        self.assertEqual(T.muestras()["MUESTRA-B"]["U1"], T.REFERENCIA["U1"])

    def test_reparacion_legitima_no_es_implante(self):
        c = T.comparar_pcb(T.REFERENCIA, T.muestras()["MUESTRA-C"])
        self.assertEqual(c["anadidos"], [])
        self.assertIn("U3", c["modificados"])
        txt = T.interpretar_modificacion(c["hallazgos"][0])
        self.assertIn("reparacion", txt)

    def test_componente_ausente_es_grave(self):
        m = copy.deepcopy(T.REFERENCIA)
        del m["U2"]
        self.assertEqual(T.comparar_pcb(T.REFERENCIA, m)["hallazgos"][0]["severidad"], "alta")


class Bus(unittest.TestCase):
    def test_el_bus_lleva_el_contenido_visible(self):
        r = T.analizar_traza_spi(T.generar_traza_spi("MUESTRA FICTICIA 0001"))
        self.assertEqual(r["contenido_recuperable"], "MUESTRA FICTICIA 0001")

    def test_carga_extra_se_detecta_como_indicio_no_prueba(self):
        r = T.analizar_traza_spi(T.generar_traza_spi("PRUEBA 01", carga_extra_pf=8.0))
        self.assertTrue(r["indicio_de_carga_extra"])
        self.assertIn("no una prueba", r["limite"])

    def test_sin_carga_no_hay_indicio(self):
        self.assertFalse(T.analizar_traza_spi(T.generar_traza_spi("PRUEBA 01"))["indicio_de_carga_extra"])

    def test_glifos_inventados_no_son_ascii(self):
        self.assertNotEqual(T.GLIFOS["A"], ord("A"))


class Consumo(unittest.TestCase):
    def test_rafagas_periodicas_se_detectan(self):
        r = T.detectar_rafagas(T.generar_consumo(7, True))
        self.assertTrue(r["patron_periodico"])
        self.assertAlmostEqual(r["periodicidad_s"], 60, delta=1)

    def test_actividad_legitima_corta_no_se_marca(self):
        r = T.detectar_rafagas(T.generar_consumo(7, False))
        self.assertEqual(r["rafagas"], [])
        self.assertFalse(r["patron_periodico"])

    def test_determinista(self):
        self.assertEqual(T.generar_consumo(3, True), T.generar_consumo(3, True))


class Custodia(unittest.TestCase):
    def test_cadena_integra_y_alterada(self):
        c = T.crear_cadena(T.envio_ejemplo())
        self.assertTrue(T.verificar_cadena(c)["integra"])
        c2 = copy.deepcopy(c)
        c2[1]["a"] = "otro"
        self.assertFalse(T.verificar_cadena(c2)["integra"])

    def test_eliminar_un_eslabon_rompe_la_cadena(self):
        c = T.crear_cadena(T.envio_ejemplo())
        self.assertFalse(T.verificar_cadena([c[0], c[2]])["integra"])

    def test_envio_limpio_continuo(self):
        self.assertTrue(T.auditar_trazabilidad(T.envio_ejemplo())["continua"])

    def test_envio_con_huecos_detecta_todo(self):
        h = " ".join(T.auditar_trazabilidad(T.envio_con_huecos())["hallazgos"])
        for k in ("no autorizado", "salto de custodia", "sello", "devolucion reabierta"):
            self.assertIn(k, h)


class Veredictos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = T.ejecutar(7)["muestras"]

    def test_b_es_autentico_pero_no_integro(self):
        v = self.r["MUESTRA-B"]["veredictos"]
        self.assertEqual(v["autenticidad_del_secure_element"], "verificada")
        self.assertEqual(v["integridad_fisica"], "fallida")
        self.assertEqual(self.r["MUESTRA-B"]["riesgo"]["nivel"], "critico")

    def test_a_es_bajo_y_c_exige_inspeccion(self):
        self.assertEqual(self.r["MUESTRA-A"]["riesgo"]["nivel"], "bajo")
        self.assertIn(self.r["MUESTRA-C"]["riesgo"]["nivel"], ("medio",))

    def test_tres_veredictos_independientes(self):
        v = T.veredictos(True, {"hallazgos": []}, {"continua": False})
        self.assertEqual((v["autenticidad_del_secure_element"], v["cadena_de_custodia"]), ("verificada", "fallida"))

    def test_attestation_fallida_sube_el_riesgo(self):
        v = T.veredictos(False, {"hallazgos": []}, {"continua": True})
        self.assertGreaterEqual(T.evaluar_riesgo(v, False, False)["puntos"], 5)

    def test_reproducible(self):
        self.assertEqual(T.informe_md(T.ejecutar(7)), T.informe_md(T.ejecutar(7)))


class Controles(unittest.TestCase):
    def test_cumple_y_falla(self):
        ok = {c: True for c in T.POLITICA}
        self.assertTrue(T.verificar_controles(ok)["cumple"])
        ok["devoluciones_inspeccionadas"] = False
        self.assertEqual(T.verificar_controles(ok)["fallan"], ["devoluciones_inspeccionadas"])


class Limites(unittest.TestCase):
    def test_sin_modulos_de_red(self):
        src = (Path(__file__).resolve().parents[1] / "tamper_lab.py").read_text(encoding="utf-8")
        for p in ("import socket", "import requests", "urllib.request", "import http", "subprocess"):
            self.assertNotIn(p, src)

    def test_sin_palabras_de_recuperacion(self):
        src = (Path(__file__).resolve().parents[1] / "tamper_lab.py").read_text(encoding="utf-8").lower()
        for p in ("abandon", "bip39", "wordlist"):
            self.assertNotIn(p, src)

    def test_salida_a_disco(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(T.main(["run", "--seed", "7", "--out", str(Path(d) / "o")]), 0)
            self.assertTrue((Path(d) / "o" / "informe.md").exists())


if __name__ == "__main__":
    unittest.main()
