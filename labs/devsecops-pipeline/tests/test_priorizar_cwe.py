"""Pruebas del priorizador ampliado, de la instantánea de casos reales y del actualizador.

Todo es offline: la red se sustituye por la instantánea versionada
(`datos/casos-cwe-cve.json`) o por respuestas simuladas con la misma forma
que devuelven NVD, CVE Program, KEV y EPSS.

    python -m unittest discover -s labs/devsecops-pipeline/tests -v
"""
from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

import actualizar_casos as AC  # noqa: E402
import cvss  # noqa: E402
import priorizar as P  # noqa: E402

SNAPSHOT = LAB / "datos" / "casos-cwe-cve.json"
EJEMPLO_CWE = LAB / "hallazgos-cwe-ejemplo.json"
EJEMPLO_ORIGINAL = LAB / "hallazgos-ejemplo.json"
RAIZ = LAB.parents[1]


def ejecutar(*args: str) -> tuple[int, str]:
    """Lanza priorizar.main() con esos argumentos y captura lo que imprime."""
    salida, errores = io.StringIO(), io.StringIO()
    with mock.patch.object(sys, "argv", ["priorizar.py", *args]), \
            contextlib.redirect_stdout(salida), contextlib.redirect_stderr(errores):
        codigo = P.main()
    return codigo, salida.getvalue()


class InstantaneaDeCasosReales(unittest.TestCase):
    """La foto guardada debe ser coherente consigo misma y con las demás piezas del repositorio."""

    @classmethod
    def setUpClass(cls):
        cls.doc = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        cls.casos = {c["cve"]: c for c in cls.doc["casos"]}

    def test_declara_fecha_fuentes_y_advertencia(self):
        pr = self.doc["procedencia"]
        self.assertRegex(pr["fecha_consulta"], r"^\d{4}-\d{2}-\d{2}$")
        self.assertTrue(pr["kev_version_catalogo"])
        self.assertIn("nvd", pr["fuentes"])
        self.assertIn("cambian a diario", pr["advertencia"])

    def test_catorce_casos_sin_duplicados(self):
        self.assertEqual(len(self.casos), len(self.doc["casos"]))
        self.assertEqual(len(self.casos), 14)

    def test_cada_puntuacion_cvss_se_reproduce_desde_su_vector(self):
        n = 0
        for c in self.casos.values():
            for m in c["cvss31"]:
                with self.subTest(cve=c["cve"], fuente=m["fuente"]):
                    self.assertEqual(cvss.puntuar(m["vector"])["base"], m["puntuacion"])
                n += 1
        self.assertGreaterEqual(n, 20)

    def test_los_cwe_de_los_casos_existen_y_estan_vigentes_en_la_base_local(self):
        sys.path.insert(0, str(RAIZ / "scripts"))
        import cwe_lib as L
        if not (L.NORMALIZADO / "cwe.jsonl").is_file():
            self.skipTest("base CWE no importada")
        base = L.BaseCWE.cargar()
        for c in self.casos.values():
            ids = {x["id"] for x in c["cwe_nvd"]} | set(c.get("cwe_cna", []))
            for cid in ids:
                if cid.startswith("NVD-CWE"):
                    continue  # marcadores de NVD («noinfo», «Other»), no son entradas del catálogo
                with self.subTest(cve=c["cve"], cwe=cid):
                    self.assertIn(cid, base)
                    self.assertNotEqual(base.obtener(cid)["estado"], "Deprecated")

    def test_epss_es_probabilidad_y_percentil_valido(self):
        for c in self.casos.values():
            self.assertTrue(0.0 <= c["epss"]["puntuacion"] <= 1.0, c["cve"])
            self.assertTrue(0.0 <= c["epss"]["percentil"] <= 1.0, c["cve"])

    def test_los_contrastes_que_ensena_la_clase_siguen_presentes(self):
        # Si una foto futura los cambia, la clase 369 deja de ser verdad y hay que revisarla.
        c = self.casos
        self.assertEqual([x["id"] for x in c["CVE-2014-0160"]["cwe_nvd"] if x["tipo"] == "Primary"], ["CWE-125"])
        self.assertFalse([x for x in c["CVE-2021-44228"]["cwe_nvd"] if x["tipo"] == "Primary"])  # sin CWE primario
        self.assertEqual(c["CVE-2024-6387"]["cwe_cna"], ["CWE-364"])
        self.assertIn("CWE-362", [x["id"] for x in c["CVE-2024-6387"]["cwe_nvd"]])             # CNA y NVD discrepan
        self.assertIsNone(c["CVE-2024-6387"]["kev"])
        self.assertGreater(c["CVE-2024-6387"]["epss"]["puntuacion"], 0.9)                       # EPSS alto sin estar en KEV
        self.assertIsNone(c["CVE-2024-2021"]["kev"])
        self.assertLess(c["CVE-2024-2021"]["epss"]["puntuacion"], 0.05)
        notas = sorted(x["puntuacion"] for x in c["CVE-2024-2021"]["cvss31"])
        self.assertEqual(notas, [6.3, 9.8])                                                    # CNA 6.3 vs NVD 9.8
        self.assertEqual(c["CVE-2023-34362"]["kev"]["ransomware"], "Known")


class Priorizacion(unittest.TestCase):
    def setUp(self):
        self.codigo, self.informe = ejecutar("--hallazgos", str(EJEMPLO_CWE), "--instantanea", str(SNAPSHOT))

    def posicion(self, cve: str) -> int:
        return self.informe.index(f"· {cve} ·")

    def test_termina_bien_y_declara_que_usa_una_foto(self):
        self.assertEqual(self.codigo, 0)
        self.assertIn("instantánea", self.informe)
        self.assertIn("no el estado de hoy", self.informe)

    def test_kev_manda_sobre_cvss(self):
        # Heartbleed (CVSS 7.5, en KEV) va antes que una inyección SQL 9.8 sin explotación documentada.
        self.assertLess(self.posicion("CVE-2014-0160"), self.posicion("CVE-2024-2021"))

    def test_lo_no_alcanzable_baja_aunque_el_cvss_sea_alto(self):
        self.assertLess(self.posicion("CVE-2024-2021"), self.posicion("CVE-2023-50716"))
        self.assertRegex(self.informe, r"\*\*P4\*\* · CVE-2023-50716")

    def test_muestra_la_causa_raiz_con_nombre_oficial(self):
        self.assertIn("CWE-502 Deserialization of Untrusted Data", self.informe)

    def test_avisa_cuando_la_nota_no_corresponde_al_vector(self):
        self.assertIn("la nota declarada (9.8) no coincide con la del vector (9.6)", self.informe)

    def test_sin_version_corregida_pide_decision_documentada(self):
        self.assertIn("sin versión corregida publicada", self.informe)

    def test_un_cve_fuera_de_la_instantanea_se_declara_desconocido_no_inocente(self):
        with tempfile.TemporaryDirectory() as tmp:
            h = Path(tmp) / "h.json"
            h.write_text(json.dumps([{"cve": "CVE-2000-0001", "paquete": "x", "version": "1", "cvss": 9.0,
                                      "exposicion": "publica"}]), encoding="utf-8")
            _, out = ejecutar("--hallazgos", str(h), "--instantanea", str(SNAPSHOT))
        self.assertIn("no figuran en la instantánea", out)
        self.assertIn("no sabemos", out)


class CompatibilidadConElLaboratorioOriginal(unittest.TestCase):
    def test_el_ejemplo_original_sigue_funcionando_sin_red(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(P, "CACHE", tmp):
            codigo, out = ejecutar("--hallazgos", str(EJEMPLO_ORIGINAL), "--sin-red")
        self.assertEqual(codigo, 0)
        self.assertIn("NO DISPONIBLE", out)           # sin red y sin caché lo declara en vez de callar
        self.assertIn("provisional", out)
        self.assertIn("CVE-2021-44228", out)

    def test_hallazgo_sin_los_campos_nuevos_no_rompe(self):
        with tempfile.TemporaryDirectory() as tmp:
            h = Path(tmp) / "h.json"
            h.write_text(json.dumps([{"cve": "CVE-2014-0160", "cvss": 7.5}]), encoding="utf-8")
            codigo, out = ejecutar("--hallazgos", str(h), "--instantanea", str(SNAPSHOT))
        self.assertEqual(codigo, 0)
        self.assertNotIn("causa raíz", out)

    def test_instantanea_inexistente_es_un_error_claro(self):
        self.assertEqual(ejecutar("--hallazgos", str(EJEMPLO_CWE), "--instantanea", "no-existe.json")[0], 1)


class PiezasSueltas(unittest.TestCase):
    def test_extraer_cwes_acepta_varias_formas(self):
        self.assertEqual(P.extraer_cwes("CWE-79"), ["CWE-79"])
        self.assertEqual(P.extraer_cwes(79), ["CWE-79"])
        self.assertEqual(P.extraer_cwes(["CWE-79", "cwe-89", "CWE-79"]), ["CWE-79", "CWE-89"])
        self.assertEqual(P.extraer_cwes("ver CWE-20 y CWE-502"), ["CWE-20", "CWE-502"])
        self.assertEqual(P.extraer_cwes(None), [])

    def test_vector_invalido_no_detiene_la_priorizacion(self):
        h = {"cvss": 7.0, "cvss_vector": "CVSS:3.1/AV:N"}
        P.verificar_vector(h)
        self.assertIn("inválido", h["_aviso_vector"])
        self.assertEqual(h["cvss"], 7.0)

    def test_si_falta_la_nota_se_toma_del_vector(self):
        h = {"cvss_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"}
        P.verificar_vector(h)
        self.assertEqual(h["cvss"], 9.8)
        self.assertNotIn("_aviso_vector", h)

    def test_la_version_minima_que_corrige_sigue_siendo_la_mas_baja(self):
        self.assertEqual(P.version_minima_que_corrige(["2.17.1", "2.16.0", "2.15.0"]), "2.15.0")


# --------------------------------------------------------------------------
class ActualizadorDeCasos(unittest.TestCase):
    """Las transformaciones puras, con respuestas que tienen la forma de las APIs reales."""

    NVD = {"cve": {
        "id": "CVE-2099-0001", "published": "2099-01-02T10:00:00.000",
        "descriptions": [{"lang": "es", "value": "x"}, {"lang": "en", "value": "Fallo de ejemplo"}],
        "weaknesses": [
            {"source": "nvd@nist.gov", "type": "Primary", "description": [{"lang": "en", "value": "CWE-89"}]},
            {"source": "134c704f-9b21-4f2e-91b3-4a467353bcc0", "type": "Secondary", "description": [{"lang": "en", "value": "CWE-89"}]},
        ],
        "metrics": {
            "cvssMetricV31": [{"source": "nvd@nist.gov", "cvssData": {"vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", "baseScore": 9.8}}],
            "cvssMetricV40": [{"source": "cna@x", "cvssData": {"vectorString": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N", "baseScore": 9.3}}],
        },
        "configurations": [{"nodes": [{"cpeMatch": [
            {"vulnerable": True, "criteria": "cpe:2.3:a:acme:widget:*:*:*:*:*:*:*:*", "versionEndExcluding": "1.2.3"},
            {"vulnerable": False, "criteria": "cpe:2.3:o:acme:os:1.0:*:*:*:*:*:*:*"},
            {"vulnerable": True, "criteria": "cpe:2.3:a:acme:widget:*:*:*:*:*:*:*:*", "versionEndExcluding": "1.2.3"},
        ]}]}],
    }}
    CVE_ORG = {
        "cveMetadata": {"assignerShortName": "acme"},
        "containers": {
            "cna": {"problemTypes": [{"descriptions": [{"cweId": "CWE-89"}, {"cweId": "CWE-89"}, {"description": "n/a"}]}],
                    "metrics": [{"cvssV3_1": {"vectorString": "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L", "baseScore": 6.3}}]},
            "adp": [{"providerMetadata": {"shortName": "CISA-ADP"}, "problemTypes": [{"descriptions": [{"cweId": "CWE-20"}]}]}],
        },
    }
    KEV = {"vulnerabilities": [{"cveID": "CVE-2099-0001", "dateAdded": "2099-02-01", "dueDate": "2099-02-22",
                                "knownRansomwareCampaignUse": "Known", "vulnerabilityName": "Acme Widget SQLi", "cwes": ["CWE-89"]}]}

    def test_nvd_separa_la_fuente_de_cada_cwe_y_cvss(self):
        d = AC.extraer_nvd(self.NVD)
        self.assertEqual([(x["id"], x["tipo"], x["fuente"]) for x in d["cwe_nvd"]],
                         [("CWE-89", "Primary", "NVD"), ("CWE-89", "Secondary", "CISA-ADP")])
        self.assertEqual(d["cvss31"][0]["fuente"], "NVD")
        self.assertEqual(d["cvss40"][0]["puntuacion"], 9.3)
        self.assertEqual(d["descripcion_en"], "Fallo de ejemplo")

    def test_nvd_ignora_lo_no_vulnerable_y_deduplica_versiones_afectadas(self):
        self.assertEqual(AC.extraer_nvd(self.NVD)["afectado"],
                         [{"vendedor": "acme", "producto": "widget", "hasta_excluida": "1.2.3"}])

    def test_cna_y_adp_se_guardan_aparte(self):
        d = AC.extraer_cna(self.CVE_ORG)
        self.assertEqual(d["cwe_cna"], ["CWE-89"])
        self.assertEqual(d["cwe_adp"], {"CISA-ADP": ["CWE-20"]})
        self.assertEqual(d["cvss31_cna"][0]["puntuacion"], 6.3)

    def test_kev_presente_y_ausente(self):
        self.assertEqual(AC.extraer_kev(self.KEV, "CVE-2099-0001")["ransomware"], "Known")
        self.assertIsNone(AC.extraer_kev(self.KEV, "CVE-2099-0002"))

    def test_armar_caso_junta_las_cuatro_fuentes(self):
        epss = {"epss": "0.01234", "percentile": "0.7", "date": "2099-03-01"}
        caso = AC.armar_caso("CVE-2099-0001", self.NVD, self.CVE_ORG, self.KEV, epss)
        self.assertEqual(caso["epss"], {"puntuacion": 0.01234, "percentil": 0.7, "fecha": "2099-03-01"})
        self.assertEqual(caso["kev"]["agregada"], "2099-02-01")
        self.assertIn("cwe_nvd", caso)
        self.assertIn("cwe_cna", caso)

    def test_no_se_rellenan_huecos_si_una_fuente_falla(self):
        # main() omite el CVE si falta NVD, CVE.org o EPSS: mejor menos casos que casos inventados.
        with tempfile.TemporaryDirectory() as tmp:
            salida = Path(tmp) / "s.json"
            kev = {"vulnerabilities": [], "catalogVersion": "x", "dateReleased": "y"}

            def falso(url, timeout=60):
                if "known_exploited" in url:
                    return kev
                return None  # NVD, CVE.org y EPSS caídos

            with mock.patch.object(AC, "_get", side_effect=falso), contextlib.redirect_stderr(io.StringIO()):
                codigo = AC.main(["--cves", "CVE-2099-0001", "--salida", str(salida), "--pausa", "0"])
            self.assertEqual(codigo, 1)
            self.assertEqual(json.loads(salida.read_text(encoding="utf-8"))["casos"], [])


if __name__ == "__main__":
    unittest.main()
