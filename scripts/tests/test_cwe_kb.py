"""Pruebas de la base de conocimiento CWE (`scripts/cwe_lib.py`, `cwe_analisis.py`, `cwe_kb.py`).

Todas se ejecutan sin red. Usan un extracto real del catálogo de MITRE
(`fixtures/cwe_mini.xml`) para probar la importación y, aparte, comprueban que
los datos reales versionados bajo `knowledge/cwe/` son íntegros.

    python -m unittest scripts.tests.test_cwe_kb -v
"""
from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import cwe_analisis as A  # noqa: E402
import cwe_kb  # noqa: E402
import cwe_lib as L  # noqa: E402

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "cwe_mini.xml"


def hacer_zip(destino: Path, xml: bytes | None = None, nombre: str = "cwec_v5.0.xml") -> Path:
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(nombre, xml if xml is not None else FIXTURE.read_bytes())
    return destino


@contextlib.contextmanager
def kb_temporal():
    """Redirige todas las rutas de la base a un directorio temporal."""
    with tempfile.TemporaryDirectory() as tmp:
        kb = Path(tmp) / "knowledge" / "cwe"
        with mock.patch.multiple(
            L,
            KB=kb,
            ORIGINAL=kb / "original",
            NORMALIZADO=kb / "normalizado",
            PEDAGOGICO=kb / "pedagogico",
            INDICES=kb / "indices",
            PROCEDENCIA=kb / "PROCEDENCIA.json",
        ):
            (kb / "LICENCIA-MITRE.md").parent.mkdir(parents=True, exist_ok=True)
            (kb / "LICENCIA-MITRE.md").write_text("aviso", encoding="utf-8")
            yield Path(tmp), kb


# --------------------------------------------------------------------------
class IdentificadoresYTexto(unittest.TestCase):
    def test_normalizar_id_acepta_variantes(self):
        for v in ("CWE-89", "cwe-89", "89", 89, "CWE89", " cwe_89 "):
            self.assertEqual(L.normalizar_id(v), "CWE-89", v)

    def test_normalizar_id_rechaza_lo_que_no_es_cwe(self):
        for v in ("CVE-2021-44228", "CWE-", "abc", "", "CWE-1234567"):
            with self.assertRaises(ValueError, msg=v):
                L.normalizar_id(v)

    def test_busqueda_ignora_acentos_y_mayusculas(self):
        self.assertEqual(L.tokens("Inyección de CÓDIGO SQL"), ["inyeccion", "codigo", "sql"])

    def test_aplanado_de_xhtml_separa_parrafos(self):
        import xml.etree.ElementTree as ET
        el = ET.fromstring(
            '<d xmlns:x="http://www.w3.org/1999/xhtml"><x:p>Primero</x:p><x:p>Segundo <x:b>negrita</x:b>.</x:p></d>'
        )
        self.assertEqual(L.texto_plano(el), "Primero\nSegundo negrita.")


class LecturaSegura(unittest.TestCase):
    def test_rechaza_dtd_y_entidades(self):
        bomba = b'<?xml version="1.0"?><!DOCTYPE x [<!ENTITY a "aaaa">]><x>&a;</x>'
        with self.assertRaises(ValueError):
            L.parsear_xml(bomba)

    def test_zip_con_dos_xml_se_rechaza(self):
        with tempfile.TemporaryDirectory() as tmp:
            z = Path(tmp) / "x.zip"
            with zipfile.ZipFile(z, "w") as zf:
                zf.writestr("a.xml", "<a/>")
                zf.writestr("b.xml", "<b/>")
            with self.assertRaises(ValueError):
                L.leer_xml_de_zip(z)

    def test_nombre_del_zip_no_permite_escapar_de_directorio(self):
        with tempfile.TemporaryDirectory() as tmp:
            z = hacer_zip(Path(tmp) / "x.zip", b"<a/>", nombre="../../evil.xml")
            nombre, datos = L.leer_xml_de_zip(z)
            self.assertEqual(nombre, "evil.xml")  # solo se usa el nombre base y se lee en memoria
            self.assertEqual(datos, b"<a/>")


# --------------------------------------------------------------------------
class Importacion(unittest.TestCase):
    def test_importa_entradas_vistas_y_procedencia(self):
        with kb_temporal() as (tmp, kb):
            res = L.importar(hacer_zip(tmp / "c.zip"), hoy="2026-10-30")
            self.assertEqual(res["estado"], "importado")
            proc = json.loads((kb / "PROCEDENCIA.json").read_text(encoding="utf-8"))
            self.assertEqual(proc["catalogo"]["version"], "5.0")
            self.assertEqual(proc["origen"]["fecha_consulta"], "2026-10-30")
            self.assertEqual(len(proc["origen"]["sha256_zip"]), 64)
            self.assertEqual(proc["catalogo"]["entradas"], 17)
            base = L.BaseCWE.cargar()
            self.assertEqual(len(base.entradas), 17)
            self.assertEqual(sum(1 for e in base.entradas.values() if e["tipo"] == "grouping"), 1)

    def test_reimportar_lo_mismo_no_cambia_nada(self):
        with kb_temporal() as (tmp, _):
            z = hacer_zip(tmp / "c.zip")
            L.importar(z)
            self.assertEqual(L.importar(z)["estado"], "sin_cambios")

    def test_importacion_es_determinista(self):
        with kb_temporal() as (tmp, kb):
            z = hacer_zip(tmp / "c.zip")
            L.importar(z)
            antes = (kb / "normalizado" / "cwe.jsonl").read_bytes()
            L.importar(z, forzar=True)
            self.assertEqual(antes, (kb / "normalizado" / "cwe.jsonl").read_bytes())

    def test_actualizacion_incremental_cuenta_cambios(self):
        with kb_temporal() as (tmp, _):
            L.importar(hacer_zip(tmp / "a.zip"))
            xml = FIXTURE.read_text(encoding="utf-8")
            # Renombra CWE-79 (modificada) y elimina CWE-1004 (eliminada).
            self.assertIn('Name="Improper Neutralization of Input During Web Page Generation', xml)
            xml = xml.replace("Improper Neutralization of Input During Web Page Generation",
                              "Nombre cambiado en una version nueva", 1)
            ini = xml.index('<Weakness ID="1004"')
            fin = xml.index("</Weakness>", ini) + len("</Weakness>")
            xml = xml[:ini] + xml[fin:]
            res = L.importar(hacer_zip(tmp / "b.zip", xml.encode("utf-8")))
            self.assertEqual(res["cambios"], {"anadidas": 0, "eliminadas": 1, "modificadas": 1})

    def test_catalogo_vacio_aborta_sin_borrar_lo_anterior(self):
        with kb_temporal() as (tmp, kb):
            L.importar(hacer_zip(tmp / "a.zip"))
            vacio = b'<?xml version="1.0"?><Weakness_Catalog xmlns="http://cwe.mitre.org/cwe-8" Version="9" Date="x"/>'
            with self.assertRaises(ValueError):
                L.importar(hacer_zip(tmp / "b.zip", vacio))
            self.assertEqual(len(L.BaseCWE.cargar().entradas), 17)


class ContenidoNormalizado(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._cm = kb_temporal()
        tmp, _ = cls._cm.__enter__()
        L.importar(hacer_zip(tmp / "c.zip"))
        cls.base = L.BaseCWE.cargar()

    @classmethod
    def tearDownClass(cls):
        cls._cm.__exit__(None, None, None)

    def test_sql_injection(self):
        e = self.base.obtener("CWE-89")
        self.assertEqual(e["tipo"], "weakness")
        self.assertEqual(e["abstraccion"], "Base")
        self.assertTrue(e["descripcion"].startswith("The product constructs all or part of an SQL command"))
        self.assertIn("Parameterization", [m["estrategia"] for m in e["mitigaciones"]])
        self.assertTrue(e["consecuencias"] and e["deteccion"])
        self.assertEqual(e["notas_mapeo"]["uso"], "Allowed")
        self.assertIn("1435", e["vistas"])  # miembro del Top 25 de 2025

    def test_agrupacion_no_es_una_debilidad(self):
        g = self.base.obtener("CWE-1345")
        self.assertEqual(g["tipo"], "grouping")
        self.assertEqual(g["abstraccion"], "")
        self.assertEqual(g["notas_mapeo"]["uso"], "Prohibited")

    def test_pilar_es_una_abstraccion(self):
        self.assertEqual(self.base.obtener("CWE-664")["abstraccion"], "Pillar")

    def test_entrada_obsoleta_se_marca(self):
        self.assertEqual(self.base.obtener("CWE-1187")["estado"], "Deprecated")

    def test_vista_top25_lista_sus_miembros(self):
        ids = {e["id"] for e in self.base.miembros_de_vista("1435")}
        self.assertTrue({"CWE-79", "CWE-89", "CWE-416"} <= ids)

    def test_el_texto_de_mitre_no_se_reescribe_ni_trunca(self):
        e = self.base.obtener("CWE-416")
        self.assertIn('the memory "belongs" to the code that operates on the new pointer', e["descripcion"])


class Consulta(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._cm = kb_temporal()
        tmp, _ = cls._cm.__enter__()
        L.importar(hacer_zip(tmp / "c.zip"))
        cls.base = L.BaseCWE.cargar()

    @classmethod
    def tearDownClass(cls):
        cls._cm.__exit__(None, None, None)

    def test_jerarquia_de_use_after_free(self):
        self.assertEqual(self.base.padres("CWE-416"), ["CWE-825"])
        caminos = self.base.ancestros("CWE-416")
        self.assertIn(["CWE-416", "CWE-825", "CWE-119", "CWE-118", "CWE-664"], caminos)
        self.assertEqual(len(caminos), 2)  # dos caminos: por memoria (119) y por ciclo de vida (672)

    def test_hijos_y_descendientes(self):
        self.assertIn("CWE-89", self.base.hijos("CWE-943"))
        self.assertEqual(self.base.descendientes("CWE-74", 2).get("CWE-89"), 2)

    def test_obtener_inexistente_da_error_claro(self):
        with self.assertRaises(KeyError):
            self.base.obtener("CWE-99999")
        with self.assertRaises(ValueError):
            self.base.obtener("CVE-1")

    def test_busqueda_por_nombre_id_y_filtros(self):
        self.assertEqual(self.base.buscar("use after free")[0][1]["id"], "CWE-416")
        self.assertEqual(self.base.buscar("cwe-79")[0][1]["id"], "CWE-79")
        # Ambas son de nivel Base y llevan «neutralization» en el nombre; el empate se ordena por número.
        self.assertEqual([e["id"] for _, e in self.base.buscar("neutralization", abstraccion="Base")][:2], ["CWE-79", "CWE-89"])
        self.assertEqual(self.base.buscar("neutralization", abstraccion="Pillar")[0][1]["id"], "CWE-707")
        self.assertEqual(self.base.buscar("zzzzzz"), [])

    def test_busqueda_oculta_obsoletas_salvo_que_se_pidan(self):
        self.assertFalse(any(e["id"] == "CWE-1187" for _, e in self.base.buscar("uninitialized")))
        self.assertTrue(any(e["id"] == "CWE-1187" for _, e in self.base.buscar("uninitialized", incluir_obsoletas=True)))


class Indices(unittest.TestCase):
    def test_indice_permite_leer_una_entrada_sin_cargar_las_demas(self):
        with kb_temporal() as (tmp, kb):
            L.importar(hacer_zip(tmp / "c.zip"))
            indice = json.loads((kb / "indices" / "indice.json").read_text(encoding="utf-8"))
            pos = indice["CWE-416"]
            with open(kb / "normalizado" / "cwe.jsonl", "rb") as fh:
                fh.seek(pos["offset"])
                self.assertEqual(json.loads(fh.read(pos["longitud"]))["id"], "CWE-416")

    def test_indice_invertido_y_jerarquia(self):
        with kb_temporal() as (tmp, kb):
            L.importar(hacer_zip(tmp / "c.zip"))
            inv = json.loads((kb / "indices" / "invertido.json").read_text(encoding="utf-8"))
            self.assertIn("CWE-416", inv["free"])
            self.assertIn("CWE-89", inv["sql"])
            jer = json.loads((kb / "indices" / "jerarquia.json").read_text(encoding="utf-8"))
            self.assertIn("CWE-89", jer["hijos"]["CWE-943"])
            self.assertIn("CWE-664", jer["raices"])


class ValidacionDeLaBase(unittest.TestCase):
    def importar(self, tmp):
        L.importar(hacer_zip(tmp / "c.zip"))

    def test_base_recien_importada_es_valida(self):
        with kb_temporal() as (tmp, _):
            self.importar(tmp)
            r = A.validar_base(completo=False)
            self.assertTrue(r.correcto, r.errores)

    def test_detecta_edicion_manual_de_los_datos(self):
        with kb_temporal() as (tmp, kb):
            self.importar(tmp)
            ruta = kb / "normalizado" / "cwe.jsonl"
            ruta.write_text(ruta.read_text(encoding="utf-8").replace("Use After Free", "Use After Free (editado)"), encoding="utf-8")
            r = A.validar_base(completo=False)
            self.assertFalse(r.correcto)
            self.assertTrue(any("huellas" in e for e in r.errores))

    def test_detecta_identificador_duplicado(self):
        with kb_temporal() as (tmp, kb):
            self.importar(tmp)
            ruta = kb / "normalizado" / "cwe.jsonl"
            lineas = ruta.read_text(encoding="utf-8").splitlines()
            ruta.write_text("\n".join(lineas + [lineas[0]]) + "\n", encoding="utf-8")
            self.assertTrue(any("únicos" in e for e in A.validar_base(completo=False).errores))

    def test_detecta_relacion_a_entrada_inexistente(self):
        with kb_temporal() as (tmp, kb):
            self.importar(tmp)
            ruta = kb / "normalizado" / "cwe.jsonl"
            filas = [json.loads(x) for x in ruta.read_text(encoding="utf-8").splitlines()]
            for f in filas[:12]:
                f["relaciones"].append({"naturaleza": "PeerOf", "id": "CWE-90000", "vista": "1000", "orden": ""})
            ruta.write_text("\n".join(L.serializar(f) for f in filas) + "\n", encoding="utf-8")
            self.assertTrue(any("relaciones" in e for e in A.validar_base(completo=False).errores))

    def test_detecta_ciclo_en_la_jerarquia(self):
        with kb_temporal() as (tmp, kb):
            self.importar(tmp)
            ruta = kb / "normalizado" / "cwe.jsonl"
            filas = [json.loads(x) for x in ruta.read_text(encoding="utf-8").splitlines()]
            por_id = {f["id"]: f for f in filas}
            # CWE-707 es ancestro de CWE-89 (89 -> 943 -> 74 -> 707); si 707 pasa a ser hija de 89, hay ciclo.
            por_id["CWE-707"]["relaciones"].append({"naturaleza": "ChildOf", "id": "CWE-89", "vista": "1000", "orden": ""})
            ruta.write_text("\n".join(L.serializar(f) for f in filas) + "\n", encoding="utf-8")
            self.assertTrue(any("ciclos" in e for e in A.validar_base(completo=False).errores))

    def test_el_hash_ignora_el_fin_de_linea(self):
        """Git en Windows entrega CRLF: la verificación no debe fallar por eso."""
        with kb_temporal() as (tmp, kb):
            self.importar(tmp)
            for n in ("normalizado/vistas.json", "normalizado/referencias.json", "indices/jerarquia.json"):
                ruta = kb / n
                ruta.write_bytes(ruta.read_bytes().replace(b"\n", b"\r\n"))
            self.assertTrue(A.validar_base(completo=False).correcto)

    def test_sin_aviso_de_licencia_falla(self):
        with kb_temporal() as (tmp, kb):
            self.importar(tmp)
            (kb / "LICENCIA-MITRE.md").unlink()
            self.assertFalse(A.validar_base(completo=False).correcto)


# --------------------------------------------------------------------------
class AuditoriaDeReferencias(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._cm = kb_temporal()
        tmp, _ = cls._cm.__enter__()
        L.importar(hacer_zip(tmp / "c.zip"))
        cls.base = L.BaseCWE.cargar()

    @classmethod
    def tearDownClass(cls):
        cls._cm.__exit__(None, None, None)

    def auditar(self, lineas: list[str]):
        menciones = [A.Mencion("docs/x.md", i + 1, f"CWE-{int(n)}", "Refs", t)
                     for i, t in enumerate(lineas) for n in A.CWE_RE.findall(t)]
        return A.auditar_referencias(self.base, menciones)

    def test_referencia_correcta_no_da_hallazgos(self):
        h = self.auditar(["- CWE-416: Use After Free — <https://cwe.mitre.org/data/definitions/416.html>"])
        self.assertEqual(h, [])

    def test_cwe_inexistente(self):
        h = self.auditar(["Ver CWE-99999"])
        self.assertEqual([x.gravedad for x in h], ["error"])
        self.assertIn("no existe", h[0].mensaje)

    def test_cwe_obsoleto(self):
        h = self.auditar(["Ver CWE-1187"])
        self.assertTrue(h and "obsoleto" in h[0].mensaje)

    def test_nombre_que_no_corresponde(self):
        h = self.auditar(["- CWE-79: Use After Free — <https://cwe.mitre.org/data/definitions/79.html>"])
        self.assertTrue(any("nombre oficial" in x.mensaje for x in h))

    def test_url_de_otra_debilidad(self):
        h = self.auditar(["- CWE-89: <https://cwe.mitre.org/data/definitions/79.html>"])
        self.assertTrue(any("apunta a CWE-79" in x.mensaje for x in h))

    def test_un_comentario_de_codigo_en_espanol_no_se_valida_como_nombre(self):
        # Tras los dos puntos hay una explicación, no el nombre oficial: no debe haber hallazgo.
        self.assertEqual(self.auditar(["# CWE-89: comprueba que el documento existe pero no de quién es."]), [])
        # En cambio, en una viñeta de referencias sí se contrasta el nombre.
        self.assertTrue(self.auditar(["- CWE-89: Use After Free — x"]))

    def test_citar_una_entrada_obsoleta_para_explicar_que_lo_esta_no_es_un_error(self):
        self.assertEqual(self.auditar(["La entrada CWE-1187 está obsoleta; consulta su sustituta."]), [])
        self.assertTrue(self.auditar(["Ver CWE-1187 para más detalle."]))

    def test_las_listas_con_prefijo_solo_en_el_primero_se_entienden(self):
        linea = "Fichas de CWE-79, 89 y 22 — <https://cwe.mitre.org/data/definitions/89.html> — jerarquía"
        self.assertEqual({int(x) for x in A.ids_de_linea(linea)}, {79, 89, 22})
        self.assertEqual(self.auditar([linea]), [])
        # Si la URL apunta a una que NO está en la lista, sí es un error.
        self.assertTrue(any("apunta a CWE-416" in x.mensaje for x in self.auditar(
            ["Fichas de CWE-79, 89 — <https://cwe.mitre.org/data/definitions/416.html>"])))

    def test_las_vistas_se_avisan_pero_no_son_un_error(self):
        h = self.auditar(["La vista CWE-1435 reúne el Top 25."])
        self.assertEqual([x.gravedad for x in h], ["aviso"])
        self.assertIn("VISTA", h[0].mensaje)

    def test_nombre_acortado_se_acepta(self):
        # Citar solo el comienzo del nombre oficial no es un error.
        self.assertEqual(self.auditar(["- CWE-89: Improper Neutralization of Special Elements used in an SQL Command — x"]), [])


class HallazgosSAST(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._cm = kb_temporal()
        tmp, _ = cls._cm.__enter__()
        L.importar(hacer_zip(tmp / "c.zip"))
        cls.base = L.BaseCWE.cargar()

    @classmethod
    def tearDownClass(cls):
        cls._cm.__exit__(None, None, None)

    def test_bandit(self):
        datos = {"results": [{"test_id": "B608", "filename": "app.py", "line_number": 27, "issue_severity": "MEDIUM",
                              "issue_text": "Possible SQL injection", "issue_cwe": {"id": 89, "link": "https://cwe.mitre.org/data/definitions/89.html"}}]}
        filas = A.anotar_hallazgos(self.base, A.leer_hallazgos_sast(datos))
        self.assertEqual(filas[0]["cwe"][0]["id"], "CWE-89")
        self.assertEqual(filas[0]["severidad"], "medium")

    def test_semgrep_con_lista_de_cwe_y_aviso_de_ambiguedad(self):
        datos = {"results": [{"check_id": "python.sqli", "path": "app.py", "start": {"line": 3},
                              "extra": {"severity": "ERROR", "message": "m",
                                        "metadata": {"cwe": ["CWE-89: Improper Neutralization of Special Elements used in an SQL Command", "CWE-20: Improper Input Validation"]}}}]}
        filas = A.anotar_hallazgos(self.base, A.leer_hallazgos_sast(datos))
        self.assertEqual([c["id"] for c in filas[0]["cwe"]], ["CWE-20", "CWE-89"])
        self.assertTrue(any("varias CWE" in a for a in filas[0]["avisos"]))

    def test_sarif(self):
        datos = {"version": "2.1.0", "runs": [{"tool": {"driver": {"name": "codeql", "rules": [
            {"id": "py/sql-injection", "properties": {"tags": ["security", "external/cwe/cwe-089", "external/cwe/cwe-1187"]}}]}},
            "results": [{"ruleId": "py/sql-injection", "level": "error", "message": {"text": "x"},
                         "locations": [{"physicalLocation": {"artifactLocation": {"uri": "app.py"}, "region": {"startLine": 9}}}]}]}]}
        filas = A.anotar_hallazgos(self.base, A.leer_hallazgos_sast(datos))
        self.assertEqual(filas[0]["linea"], 9)
        self.assertEqual({c["id"] for c in filas[0]["cwe"]}, {"CWE-89", "CWE-1187"})
        self.assertTrue(any("obsoleto" in a for a in filas[0]["avisos"]))

    def test_hallazgo_sin_cwe_pide_clasificacion_manual(self):
        datos = {"results": [{"check_id": "r", "path": "a.py", "start": {"line": 1}, "extra": {"severity": "WARNING", "message": "m", "metadata": {}}}]}
        filas = A.anotar_hallazgos(self.base, A.leer_hallazgos_sast(datos))
        self.assertTrue(any("clasificar a mano" in a for a in filas[0]["avisos"]))

    def test_formato_desconocido(self):
        with self.assertRaises(ValueError):
            A.leer_hallazgos_sast({"otra": 1})

    def test_contraste_con_el_mapa_de_un_laboratorio(self):
        """Dado el código fuente real y el mapa del lab, distingue coincide / menos específico / difiere."""
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            codigo = ["x = 1", "r = eval(expr)", "q = 'SELECT ' + name", "ok = 2"]  # líneas 1 a 4
            (raiz / "app.py").write_text("\n".join(codigo) + "\n", encoding="utf-8")
            mapa = {"vulnerabilidades": [
                {"titulo": "eval", "marcador": "eval(expr)", "cwe_principal": "CWE-89", "cwe_alternativas": [], "bandit": {"nota": "n"}},
                {"titulo": "sql", "marcador": "'SELECT '", "cwe_principal": "CWE-89",
                 "cwe_alternativas": [{"id": "CWE-79", "motivo": "m"}], "bandit": {"nota": "n"}},
            ]}
            filas = [
                {"archivo": "app.py", "linea": 2, "cwe": [{"id": "CWE-79"}]},   # eval: ni principal ni alternativa
                {"archivo": "app.py", "linea": 3, "cwe": [{"id": "CWE-79"}]},   # sql: es una alternativa válida
                {"archivo": "app.py", "linea": 3, "cwe": [{"id": "CWE-89"}]},   # sql: coincide
                {"archivo": "app.py", "linea": 4, "cwe": [{"id": "CWE-89"}]},   # línea sin defecto conocido
            ]
            r = A.contrastar_con_mapa(filas, mapa, raiz)
        self.assertEqual([x["contraste"]["estado"] if x["contraste"] else None for x in r],
                         ["difiere", "valido_pero_no_el_mas_especifico", "coincide", None])


# --------------------------------------------------------------------------
def crear_repo_de_prueba(tmp: Path) -> Path:
    """Mini repositorio: dos clases, un laboratorio con prueba y un mapa curricular."""
    raiz = tmp / "repo"
    c1 = raiz / "classes" / "parte-4-web" / "091-inyeccion-sql"
    c2 = raiz / "classes" / "parte-5-bin" / "127-use-after-free"
    c1.mkdir(parents=True)
    c2.mkdir(parents=True)
    (c1 / "README.md").write_text("# SQLi\n\n## 🧠 Explicación\nLa inyección SQL (CWE-89) ocurre cuando...\n\n## 🧪 Laboratorio\nHazlo.\n", encoding="utf-8")
    (c2 / "README.md").write_text("# UAF\n\n## 🧠 Explicación\nEl use-after-free reutiliza memoria liberada.\n", encoding="utf-8")
    lab = raiz / "labs" / "appsec-code"
    (lab / "tests").mkdir(parents=True)
    (lab / "README.md").write_text("# lab\n", encoding="utf-8")
    (lab / "tests" / "test_x.py").write_text("def test_sqli_corregida():\n    pass\n", encoding="utf-8")
    (raiz / "docs").mkdir()
    (raiz / "docs" / "quiz.md").write_text("Pregunta sobre SQL\n", encoding="utf-8")
    return raiz


MAPA = {
    "esquema": L.ESQUEMA,
    "familias": {"inyeccion": "Inyecciones", "memoria": "Memoria"},
    "entradas": {
        "CWE-89": {"familia": "inyeccion", "nivel": "basico", "palabras_clave": ["inyeccion sql"],
                   "teoria": [91], "ejercicio": [91], "laboratorio": ["labs/appsec-code"],
                   "prueba": ["labs/appsec-code/tests/test_x.py::test_sqli_corregida"], "correccion": "labs/appsec-code",
                   "mitigacion": "Consultas parametrizadas", "evaluacion": ["docs/quiz.md"]},
        "CWE-416": {"familia": "memoria", "nivel": "intermedio", "palabras_clave": ["use-after-free"], "teoria": [127]},
    },
}


class Cobertura(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._cm = kb_temporal()
        cls.tmp, _ = cls._cm.__enter__()
        L.importar(hacer_zip(cls.tmp / "c.zip"))
        cls.base = L.BaseCWE.cargar()
        cls.raiz = crear_repo_de_prueba(cls.tmp)

    @classmethod
    def tearDownClass(cls):
        cls._cm.__exit__(None, None, None)

    def calcular(self, mapa=None):
        mencion = A.escanear_menciones(self.raiz)
        return {f["id"]: f for f in A.cobertura(self.base, self.raiz, mapa or MAPA, mencion)}

    def test_niveles_y_estado(self):
        f = self.calcular()
        self.assertEqual(f["CWE-89"]["nivel_cobertura"], "correccion_prueba")
        self.assertEqual(f["CWE-89"]["estado"], "Completo")
        self.assertEqual(f["CWE-416"]["nivel_cobertura"], "explicado")
        self.assertEqual(f["CWE-416"]["estado"], "Parcial")

    def test_top25_se_incluye_aunque_el_mapa_no_lo_declare(self):
        f = self.calcular()
        self.assertIn("CWE-79", f)  # está en la vista 1435 del extracto
        self.assertEqual(f["CWE-79"]["estado"], "Pendiente")
        self.assertEqual(f["CWE-79"]["nivel_cobertura"], "pendiente")

    def test_la_mera_aparicion_del_id_no_es_cobertura(self):
        (self.raiz / "docs" / "nota.md").write_text("Se cita CWE-79 una sola vez.\n", encoding="utf-8")
        try:
            f = self.calcular()
            self.assertEqual(f["CWE-79"]["nivel_cobertura"], "mencionado")
            self.assertEqual(f["CWE-79"]["estado"], "Pendiente")
        finally:
            (self.raiz / "docs" / "nota.md").unlink()

    def test_declaracion_falsa_baja_la_cobertura_y_se_informa(self):
        mapa = json.loads(json.dumps(MAPA))
        mapa["entradas"]["CWE-416"]["teoria"] = [91]   # la clase 091 no trata use-after-free
        f = self.calcular(mapa)["CWE-416"]
        self.assertEqual(f["teoria"], [])
        self.assertEqual(f["estado"], "Pendiente")
        self.assertTrue(f["problemas"])
        errores = A.validar_mapa(self.base, self.raiz, mapa).errores
        self.assertTrue(any("CWE-416" in e and "no menciona" in e for e in errores))

    def test_prueba_inexistente_no_otorga_el_nivel_maximo(self):
        mapa = json.loads(json.dumps(MAPA))
        mapa["entradas"]["CWE-89"]["prueba"] = ["labs/appsec-code/tests/test_x.py::test_que_no_existe"]
        f = self.calcular(mapa)["CWE-89"]
        self.assertEqual(f["nivel_cobertura"], "laboratorio")
        self.assertTrue(any("no encontrada" in p for p in f["problemas"]))

    def test_la_evidencia_de_evaluacion_debe_citar_el_identificador(self):
        banco = self.raiz / "docs" / "banco-preguntas.txt"
        mapa = json.loads(json.dumps(MAPA))
        mapa["entradas"]["CWE-89"]["evaluacion"] = ["docs/banco-preguntas.txt"]
        try:
            # CWE-890 empieza igual que CWE-89, pero no es CWE-89: no debe valer como evidencia
            banco.write_text("Pregunta sobre CWE-890 y sobre CWE-79.\n", encoding="utf-8")
            errores = " ".join(A.validar_mapa(self.base, self.raiz, mapa).errores)
            self.assertIn("no cita el identificador", errores)
            fila = {f["id"]: f for f in A.cobertura(self.base, self.raiz, mapa, A.escanear_menciones(self.raiz))}["CWE-89"]
            self.assertEqual(fila["evaluacion"], [])
            self.assertTrue(any("sin citar" in p for p in fila["problemas"]))

            banco.write_text("Pregunta sobre CWE-89 (inyección SQL).\n", encoding="utf-8")
            self.assertFalse(any("CWE-89" in e and "evaluación" in e for e in A.validar_mapa(self.base, self.raiz, mapa).errores))
            fila = {f["id"]: f for f in A.cobertura(self.base, self.raiz, mapa, A.escanear_menciones(self.raiz))}["CWE-89"]
            self.assertEqual(fila["evaluacion"], ["docs/banco-preguntas.txt"])
        finally:
            banco.unlink(missing_ok=True)

    def test_cwe_obsoleto_o_inexistente_en_el_mapa_es_error(self):
        mapa = json.loads(json.dumps(MAPA))
        mapa["entradas"]["CWE-1187"] = {"familia": "memoria", "nivel": "basico"}
        mapa["entradas"]["CWE-99999"] = {"familia": "memoria", "nivel": "basico"}
        errores = " ".join(A.validar_mapa(self.base, self.raiz, mapa).errores)
        self.assertIn("obsoleto", errores)
        self.assertIn("no existe en el catálogo", errores)

    def test_matriz_es_reproducible_y_documenta_los_niveles(self):
        filas = self.calcular()
        menc = A.escanear_menciones(self.raiz)
        fuera = A.cwe_mencionados_fuera_de_objetivo(self.base, list(filas.values()), menc)
        huecos = A.clases_sin_cwe((4, 5), menc, self.raiz)
        m1 = A.render_matriz(self.base, list(filas.values()), fuera, huecos, self.raiz)
        m2 = A.render_matriz(self.base, list(filas.values()), fuera, huecos, self.raiz)
        self.assertEqual(m1, m2)
        self.assertIn("no** cuenta como cobertura", m1)
        self.assertIn("| CWE ID | Nombre |", m1)

    def test_clases_sin_cwe_detecta_las_que_no_lo_citan(self):
        menc = A.escanear_menciones(self.raiz)
        huecos = A.clases_sin_cwe((4, 5), menc, self.raiz)
        self.assertTrue(any(h.startswith("127") for h in huecos))
        self.assertFalse(any(h.startswith("091") for h in huecos))


# --------------------------------------------------------------------------
class CliSinRed(unittest.TestCase):
    """El CLI funciona sin conexión una vez importados los datos."""

    @classmethod
    def setUpClass(cls):
        cls._cm = kb_temporal()
        cls.tmp, _ = cls._cm.__enter__()
        L.importar(hacer_zip(cls.tmp / "c.zip"))

    @classmethod
    def tearDownClass(cls):
        cls._cm.__exit__(None, None, None)

    def correr(self, *args) -> tuple[int, str]:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), mock.patch("urllib.request.urlopen", side_effect=AssertionError("no debe usar la red")):
            codigo = cwe_kb.main(list(args))
        return codigo, buf.getvalue()

    def test_mostrar(self):
        codigo, out = self.correr("mostrar", "cwe-416")
        self.assertEqual(codigo, 0)
        self.assertIn("Use After Free", out)

    def test_mostrar_json(self):
        codigo, out = self.correr("mostrar", "89", "--json")
        self.assertEqual(json.loads(out)["id"], "CWE-89")

    def test_buscar_y_sin_resultados(self):
        self.assertIn("CWE-416", self.correr("buscar", "use after free")[1])
        self.assertEqual(self.correr("buscar", "zzzzz")[0], 1)

    def test_relaciones(self):
        _, out = self.correr("relaciones", "CWE-416")
        self.assertIn("CWE-825", out)
        self.assertIn("CWE-416  →  CWE-825", out)

    def test_mitigaciones(self):
        _, out = self.correr("mitigaciones", "CWE-89")
        self.assertIn("Parameterization", out)

    def test_ficha_markdown(self):
        _, out = self.correr("ficha", "CWE-89")
        self.assertIn("# CWE-89 —", out)
        self.assertIn("## Cómo se corrige", out)
        self.assertIn("LICENCIA-MITRE", out)

    def test_exportar_formatos(self):
        _, csv_ = self.correr("exportar", "--formato", "csv", "--vista", "1435")
        self.assertTrue(csv_.startswith("id,tipo,abstraccion"))
        self.assertIn("CWE-89", csv_)
        _, jl = self.correr("exportar", "--formato", "jsonl", "--ids", "89", "79")
        self.assertEqual([json.loads(x)["id"] for x in jl.splitlines()], ["CWE-79", "CWE-89"])

    def test_exportar_excluye_obsoletas_por_defecto(self):
        _, jl = self.correr("exportar", "--formato", "jsonl")
        self.assertNotIn("CWE-1187", jl)
        _, jl = self.correr("exportar", "--formato", "jsonl", "--obsoletas")
        self.assertIn("CWE-1187", jl)

    def test_id_invalido_devuelve_error(self):
        with self.assertRaises(SystemExit) as cm, contextlib.redirect_stderr(io.StringIO()):
            self.correr("mostrar", "CVE-2021-44228")
        self.assertEqual(cm.exception.code, 1)


# --------------------------------------------------------------------------
class DatosRealesVersionados(unittest.TestCase):
    """Garantías sobre `knowledge/cwe/` tal como está en el repositorio."""

    @classmethod
    def setUpClass(cls):
        if not (L.NORMALIZADO / "cwe.jsonl").is_file():
            raise unittest.SkipTest("La base local no está importada")
        cls.base = L.BaseCWE.cargar()

    def test_la_base_real_es_integra(self):
        r = A.validar_base()
        self.assertTrue(r.correcto, r.errores)

    def test_el_mapa_curricular_real_es_coherente(self):
        r = A.validar_mapa(self.base)
        self.assertTrue(r.correcto, r.errores)

    def test_las_referencias_cwe_del_temario_son_validas(self):
        h = [x for x in A.auditar_referencias(self.base, A.escanear_menciones()) + A.auditar_urls(self.base) if x.gravedad == "error"]
        self.assertEqual(h, [], "\n".join(f"{x.archivo}:{x.linea} {x.mensaje}" for x in h))

    def test_top25_2025_tiene_25_debilidades_vigentes(self):
        miembros = self.base.miembros_de_vista(A.TOP25_VISTA)
        self.assertEqual(len(miembros), 25)
        self.assertTrue(all(m["tipo"] == "weakness" and m["estado"] != "Deprecated" for m in miembros))

    def test_la_matriz_publicada_esta_al_dia(self):
        ruta = L.RAIZ / "docs" / "matriz-cobertura-cwe.md"
        if not ruta.is_file():
            self.skipTest("la matriz aún no se ha generado")
        menc = A.escanear_menciones()
        filas = A.cobertura(self.base, menciones=menc)
        esperado = A.render_matriz(self.base, filas, A.cwe_mencionados_fuera_de_objetivo(self.base, filas, menc),
                                   A.clases_sin_cwe(cwe_kb.PARTES_CON_DEBILIDADES, menc))
        self.assertEqual(ruta.read_text(encoding="utf-8").replace("\r\n", "\n"), esperado,
                         "docs/matriz-cobertura-cwe.md está desactualizada: python scripts/cwe_kb.py cobertura --escribir")

    def test_top25_guardado_es_coherente_con_la_vista_oficial(self):
        ruta = L.NORMALIZADO / "top25-2025.json"
        if not ruta.is_file():
            self.skipTest("Top 25 no descargado")
        doc = json.loads(ruta.read_text(encoding="utf-8"))
        self.assertEqual([e["id"] for e in doc["entradas"]], self.base.vista("1435")["miembros"])
        self.assertEqual([e["rango"] for e in doc["entradas"]], list(range(1, 26)))
        puntos = [e["puntuacion"] for e in doc["entradas"]]
        self.assertEqual(puntos, sorted(puntos, reverse=True))  # el ranking es por puntuación decreciente

    def test_owasp_2025_son_diez_agrupaciones_prohibidas_para_mapear(self):
        for i in range(1436, 1446):
            e = self.base.obtener(f"CWE-{i}")
            self.assertEqual(e["tipo"], "grouping")
            self.assertEqual(e["notas_mapeo"]["uso"], "Prohibited")
            self.assertGreaterEqual(len([r for r in e["relaciones"] if r["naturaleza"] == "Has_Member"]), 5)

    def test_aviso_de_licencia_acompana_a_los_datos(self):
        texto = (L.KB / "LICENCIA-MITRE.md").read_text(encoding="utf-8")
        self.assertIn("The MITRE Corporation", texto)
        self.assertIn("royalty-free", texto)


class ConservacionDelProgramaExistente(unittest.TestCase):
    """La integración de CWE no debe haber eliminado ni renumerado nada."""

    LABS_ORIGINALES = (
        "appsec-code", "appsec-web", "blue-team-soc", "ciso-leadership", "cloud-security", "cripto",
        "custodia-activos-digitales", "devsecops-pipeline", "dfir-memoria", "game-security", "kali-mcp-ia",
        "lanzamientos-virales", "pwn-binarios", "red-team-ad", "redes-nmap", "rootcause-windows",
    )

    def test_las_360_clases_originales_siguen_existiendo_en_orden(self):
        nums = []
        for p in (L.RAIZ / "classes").glob("parte-*"):  # sin ordenar: «parte-10» < «parte-2» alfabéticamente
            for c in p.glob("[0-9][0-9][0-9]-*"):
                self.assertTrue((c / "README.md").is_file(), c.name)
                nums.append(int(c.name[:3]))
        nums.sort()
        self.assertGreaterEqual(len(nums), 360)
        self.assertEqual(nums[:360], list(range(1, 361)))
        self.assertEqual(nums, list(range(1, len(nums) + 1)), "numeración con huecos o duplicados")

    def test_los_laboratorios_originales_siguen_existiendo(self):
        for lab in self.LABS_ORIGINALES:
            self.assertTrue((L.RAIZ / "labs" / lab / "README.md").is_file(), lab)

    def test_el_priorizador_original_conserva_su_interfaz(self):
        src = (L.RAIZ / "labs" / "devsecops-pipeline" / "priorizar.py").read_text(encoding="utf-8")
        # Interfaz original: tres opciones reales (la docstring citaba además una --exposicion que nunca existió).
        for simbolo in ("--hallazgos", "--salida", "--sin-red", "def descargar_kev", "FACTOR_EXPOSICION", "def prioridad"):
            self.assertIn(simbolo, src)


# --------------------------------------------------------------------------
def pagina_top25_falsa(filas: int = 25) -> str:
    """HTML con la misma estructura de líneas que la página oficial del Top 25 (datos de prueba)."""
    cuerpo = "".join(
        f"<div>{n}</div><div>CWE-{1000 + n}</div><div>Nombre {n}</div><div>{100 - n}.50</div><div>{n % 3}</div><div>+{n}</div>"
        for n in range(1, filas + 1)
    )
    return ("<html><body><h1>Top</h1><div>Rank</div><div>ID</div><div>Name</div><div>Score</div>"
            "<div>CVEs in KEV</div><div>Rank Change vs. 2024</div>" + cuerpo +
            "<div>Page Last Updated:</div><div>January 1, 2099</div></body></html>")


class Top25(unittest.TestCase):
    def test_parsea_las_25_filas(self):
        filas = L.parsear_top25(L.texto_de_html(pagina_top25_falsa()))
        self.assertEqual(len(filas), 25)
        self.assertEqual(filas[0], {"rango": 1, "id": "CWE-1001", "nombre": "Nombre 1", "puntuacion": 99.5,
                                    "cves_en_kev": 1, "cambio_vs_anterior": "+1"})

    def test_falla_en_voz_alta_si_cambia_el_formato(self):
        with self.assertRaises(ValueError):
            L.parsear_top25(L.texto_de_html(pagina_top25_falsa(filas=24)))
        with self.assertRaises(ValueError):
            L.parsear_top25("sin tabla")

    def test_importar_guarda_procedencia(self):
        with kb_temporal() as (tmp, kb):
            with mock.patch.object(L, "TOP25_JSON", kb / "normalizado" / "top25-2025.json"):
                doc = L.importar_top25(pagina_top25_falsa(), hoy="2099-02-03")
                guardado = json.loads((kb / "normalizado" / "top25-2025.json").read_text(encoding="utf-8"))
        self.assertEqual(doc, guardado)
        self.assertEqual(guardado["pagina_actualizada"], "January 1, 2099")
        self.assertEqual(guardado["fecha_consulta"], "2099-02-03")
        self.assertIn("methodology", guardado["metodologia"])


class Miembros(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._cm = kb_temporal()
        cls.tmp, _ = cls._cm.__enter__()
        L.importar(hacer_zip(cls.tmp / "c.zip"))

    @classmethod
    def tearDownClass(cls):
        cls._cm.__exit__(None, None, None)

    def correr(self, *args):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            codigo = cwe_kb.main(list(args))
        return codigo, buf.getvalue()

    def test_miembros_de_una_vista(self):
        codigo, out = self.correr("miembros", "1435")
        self.assertEqual(codigo, 0)
        self.assertIn("CWE-79", out)
        self.assertIn("Top 25", out)

    def test_miembros_de_una_agrupacion(self):
        codigo, out = self.correr("miembros", "CWE-1345")
        self.assertEqual(codigo, 0)
        self.assertIn("NO se usa para mapear", out)

    def test_una_debilidad_no_tiene_miembros(self):
        self.assertEqual(self.correr("miembros", "CWE-89")[0], 1)


if __name__ == "__main__":
    unittest.main()
