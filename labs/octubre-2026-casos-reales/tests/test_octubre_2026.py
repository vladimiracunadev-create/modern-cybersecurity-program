"""Pruebas del laboratorio «Octubre de 2026: casos reales».

    python -m unittest discover -s labs/octubre-2026-casos-reales/tests -v
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
RAIZ = LAB.parents[1]
sys.path.insert(0, str(LAB))

import destinos_y_rutas as D  # noqa: E402
import deteccion_identidad_app as I  # noqa: E402
import respaldo_y_triaje as R  # noqa: E402

SNAP = RAIZ / "knowledge" / "cve" / "2026-10" / "instantanea.json"
DNS = {"ejemplo.test": ["93.184.216.34"], "interno.test": ["10.0.0.5"], "meta.test": ["169.254.169.254"],
       "rebind.test": ["93.184.216.34", "127.0.0.1"]}


class SSRF(unittest.TestCase):
    def test_vulnerable_acepta_url_completa(self):
        self.assertEqual(D.construir_destino_vulnerable("http://169.254.169.254/latest", "x"), "http://169.254.169.254/latest")

    def test_bloquea_destinos_internos(self):
        for url in ("http://interno.test/", "http://meta.test/latest", "http://127.0.0.1/", "http://[::1]/",
                    "http://rebind.test/", "http://169.254.169.254/", "http://10.1.2.3/"):
            self.assertFalse(D.validar_destino(url, DNS)[0], url)

    def test_bloquea_esquemas_y_puertos(self):
        for url in ("file:///etc/passwd", "gopher://ejemplo.test/", "ftp://ejemplo.test/", "http://ejemplo.test:6379/",
                    "http://usuario:clave@ejemplo.test/"):
            self.assertFalse(D.validar_destino(url, DNS)[0], url)

    def test_permite_destino_publico(self):
        self.assertTrue(D.validar_destino("https://ejemplo.test/api", DNS)[0])

    def test_lista_cerrada(self):
        self.assertFalse(D.validar_destino("https://ejemplo.test/", DNS, permitidos={"otro.test"})[0])
        self.assertTrue(D.validar_destino("https://ejemplo.test/", DNS, permitidos={"ejemplo.test"})[0])

    def test_no_resuelve(self):
        self.assertFalse(D.validar_destino("https://fantasma.test/", DNS)[0])

    def test_literales_alternativos_de_loopback(self):
        # urlsplit.hostname devuelve la cadena tal cual; los literales raros no son IP válidas y no resuelven en el DNS simulado
        for url in ("http://2130706433/", "http://0x7f.1/", "http://127.1/"):
            self.assertFalse(D.validar_destino(url, DNS)[0], url)


class Rutas(unittest.TestCase):
    BASE = "/srv/app/archivos"

    def test_vulnerable_sale_del_directorio(self):
        self.assertEqual(D.ruta_vulnerable(self.BASE, "../../../etc/passwd"), "/etc/passwd")

    def test_segura_rechaza_variantes(self):
        for n in ("../x", "a/../../x", "%2e%2e/x", "%252e%252e/x", "/etc/passwd", "a\\..\\x", "a\x00.png", "a%00.png"):
            self.assertIsNone(D.ruta_segura(self.BASE, n)[0], repr(n))

    def test_segura_acepta_legitimas(self):
        self.assertEqual(D.ruta_segura(self.BASE, "informes/2026/octubre.pdf")[0], self.BASE + "/informes/2026/octubre.pdf")
        self.assertEqual(D.ruta_segura(self.BASE, "a/../b.txt")[0], self.BASE + "/b.txt")


class Comandos(unittest.TestCase):
    def test_inyeccion_produce_varias_ordenes(self):
        self.assertEqual(len(D.comandos_que_ejecutaria_un_shell(D.linea_de_shell_vulnerable("8.8.8.8"))), 1)
        for malo in ("8.8.8.8; id", "8.8.8.8 && id", "8.8.8.8 | id", "8.8.8.8\nid", "$(id)", "`id`"):
            self.assertGreater(len(D.comandos_que_ejecutaria_un_shell(D.linea_de_shell_vulnerable(malo))), 1, malo)

    def test_argv_seguro(self):
        for malo in ("8.8.8.8; id", "-oProxy=x", "a b", "$(id)", "a`b`", "x|y", ""):
            self.assertIsNone(D.argv_seguro(malo)[0], repr(malo))
        argv, _ = D.argv_seguro("ejemplo.test")
        self.assertEqual(argv, ["ping", "-c", "1", "--", "ejemplo.test"])


class Deteccion(unittest.TestCase):
    def setUp(self):
        self.ev = I.generar(7)
        self.al = I.detectar(self.ev)
        self.m = I.medir(self.ev, self.al)

    def test_determinista(self):
        a = [(e.t, e.tipo, e.inquilino, e.actor) for e in I.generar(7)]
        b = [(e.t, e.tipo, e.inquilino, e.actor) for e in I.generar(7)]
        self.assertEqual(a, b)

    def test_detecta_el_episodio(self):
        self.assertEqual(self.m["detectados_no_spray"], self.m["maliciosos_no_spray"])
        self.assertTrue(self.m["spray_detectado"])

    def test_sin_falsos_positivos_por_el_cambio_legitimo(self):
        self.assertEqual(self.m["falsos_positivos"], 0)

    def test_sin_inventario_de_propietarios_el_cambio_legitimo_alerta(self):
        al = I.detectar(self.ev, propietarios={})
        self.assertGreater(I.medir(self.ev, al)["falsos_positivos"], 0)

    def test_robusto_a_otras_semillas(self):
        for s in range(1, 6):
            ev = I.generar(s)
            m = I.medir(ev, I.detectar(ev))
            self.assertEqual(m["detectados_no_spray"], m["maliciosos_no_spray"], s)
            self.assertEqual(m["falsos_positivos"], 0, s)


class Respaldos(unittest.TestCase):
    def test_copias_en_el_mismo_dominio_se_pierden(self):
        copias = [R.Copia("snapshots", "nube-A", False, False, 30, 4),
                  R.Copia("replica-mismo-proveedor", "nube-A", False, False, 200, 24)]
        r = R.evaluar_respaldos(copias, "nube-A")
        self.assertFalse(r["recuperable"])
        self.assertEqual(r["sobreviven"], [])

    def test_copia_fuera_de_banda_inmutable_y_probada_salva(self):
        copias = [R.Copia("snapshots", "nube-A", False, False, 30, 4),
                  R.Copia("boveda", "nube-A", True, True, 45, 24),
                  R.Copia("otra-nube", "nube-B", False, False, 10, 12)]
        r = R.evaluar_respaldos(copias, "nube-A")
        self.assertEqual(sorted(r["sobreviven"]), ["boveda", "otra-nube"])
        self.assertTrue(r["recuperable"])
        self.assertEqual(r["rpo_mejor_horas"], 12)

    def test_copia_viva_pero_nunca_probada_no_cuenta(self):
        r = R.evaluar_respaldos([R.Copia("boveda", "nube-B", True, True, None, 24)], "nube-A")
        self.assertEqual(r["sobreviven"], ["boveda"])
        self.assertFalse(r["recuperable"])


@unittest.skipUnless(SNAP.exists(), "falta la instantánea de octubre")
class TriajeOctubre(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.datos = json.loads(SNAP.read_text(encoding="utf-8"))
        cls.filas = R.triaje_del_mes(SNAP)
        cls.res = R.resumen(cls.filas)

    def test_los_36_estan_en_kev_en_octubre(self):
        self.assertEqual(len(self.filas), 36)
        self.assertTrue(all(f["kev"].startswith("2026-10") for f in self.filas))
        self.assertEqual(self.datos["kev_incorporados_en_el_mes"], 36)

    def test_tres_fechas_distintas(self):
        # el hallazgo pedagógico: publicación, KEV y explotación no son la misma fecha
        self.assertEqual(self.res["por_categoria"], {"publicado-en-el-mes": 20, "publicado-antes-del-mes": 15,
                                                      "registro-publicado-despues-del-mes": 1})

    def test_kev_antes_que_el_registro(self):
        self.assertEqual(self.res["kev_antes_que_el_registro"], ["CVE-2026-118527"])

    def test_cve_antiguos_en_kev(self):
        viejos = [f["cve"] for f in self.filas if f["publicado"] < "2020"]
        self.assertEqual(sorted(viejos), ["CVE-2015-3306", "CVE-2015-5477", "CVE-2016-3081"])

    def test_cvss_bajo_con_explotacion(self):
        f = {x["cve"]: x for x in self.filas}
        self.assertLess(f["CVE-2026-41709"]["cvss_max"], 3.0)         # KEV con CVSS 2,7
        self.assertLess(f["CVE-2026-96655"]["cvss_max"], 6.0)         # Plex SSRF
        self.assertGreater(f["CVE-2026-109618"]["epss"], 0.99)

    def test_plazo_bod_calculado_con_ssvc(self):
        f = {x["cve"]: x for x in self.filas}
        self.assertIn("3 días", f["CVE-2026-104935"]["plazo_bod"])
        self.assertTrue(f["CVE-2026-104935"]["triaje_forense"])

    def test_cwe_del_registro_coherente_con_kev(self):
        for c in self.datos["cves"]:
            kev = set(c["kev"]["cwe_kev"])
            reg = set(c["registro"]["cwe_registro"])
            if kev and reg:
                self.assertTrue(kev & reg or c["cve"] in {"CVE-2015-5477", "CVE-2026-111357", "CVE-2026-46300"},
                                f"{c['cve']}: KEV {kev} vs registro {reg}")


class Trazabilidad(unittest.TestCase):
    """El mapa curricular y los incidentes deben apuntar a cosas que existen."""

    @classmethod
    def setUpClass(cls):
        cls.mapa = json.loads((SNAP.parent / "mapa-curricular.json").read_text(encoding="utf-8"))
        cls.inc = json.loads((SNAP.parent / "incidentes.json").read_text(encoding="utf-8"))
        cls.snap = json.loads(SNAP.read_text(encoding="utf-8"))

    def _clase(self, n):
        return list((RAIZ / "classes").glob(f"*/{n:03d}-*/README.md"))

    def test_mapa_cubre_exactamente_los_cve_de_la_instantanea(self):
        self.assertEqual({c["cve"] for c in self.mapa["casos"]}, {c["cve"] for c in self.snap["cves"]})

    def test_clases_existen_y_citan_el_caso(self):
        for c in self.mapa["casos"]:
            for n in [c["clase_canonica"], *c["clases_relacionadas"]]:
                self.assertEqual(len(self._clase(n)), 1, f"{c['cve']}: clase {n}")

    def test_la_clase_canonica_menciona_el_cve(self):
        for c in self.mapa["casos"]:
            texto = self._clase(c["clase_canonica"])[0].read_text(encoding="utf-8")
            self.assertIn(c["cve"], texto, f"{c['cve']} no aparece en la clase {c['clase_canonica']}")

    def test_laboratorio_citado_existe(self):
        for c in self.mapa["casos"]:
            if c["laboratorio"]:
                archivo = c["laboratorio"].split("::")[0]
                self.assertTrue((RAIZ / archivo).exists(), archivo)

    def test_cwe_del_mapa_coincide_con_la_instantanea(self):
        por_cve = {c["cve"]: c for c in self.snap["cves"]}
        for c in self.mapa["casos"]:
            self.assertEqual(c["cwe_registro"], por_cve[c["cve"]]["registro"]["cwe_registro"])

    def test_incidentes_sin_cve_inventado(self):
        validos = {c["cve"] for c in self.snap["cves"]}
        for i in self.inc["incidentes"]:
            self.assertTrue(i["id"].startswith("INC-2026-10-"))
            self.assertTrue(i["fuentes"] and i["incertidumbre"])
            for cve in i["cve_asociados"]:
                self.assertRegex(cve, r"^CVE-\d{4}-\d{4,}$")
            for n in i["clases"]:
                self.assertEqual(len(self._clase(n)), 1)
        self.assertGreater(len(validos), 0)


if __name__ == "__main__":
    unittest.main()
