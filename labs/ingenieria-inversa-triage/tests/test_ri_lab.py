import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import ri_lab as R  # noqa: E402


class Estructura(unittest.TestCase):
    def test_cabecera_y_secciones(self):
        info = R.analizar_elf(R.binario_demo(1))
        self.assertEqual(info["arquitectura"], "x86-64")
        self.assertEqual(info["tipo"], "ET_EXEC")
        nombres = [s["nombre"] for s in info["secciones"]]
        for esperado in (".text", ".rodata", ".symtab", ".strtab", ".shstrtab"):
            self.assertIn(esperado, nombres)

    def test_simbolos_presentes_y_stripped(self):
        con = R.analizar_elf(R.binario_demo(1))
        sin = R.analizar_elf(R.binario_demo(1, stripped=True))
        self.assertEqual([s["nombre"] for s in con["simbolos"]], ["main", "check_license", "copy_name"])
        self.assertFalse(con["stripped"])
        self.assertTrue(sin["stripped"])
        self.assertEqual(sin["simbolos"], [])

    def test_stripped_conserva_el_codigo(self):
        a = R.analizar_elf(R.binario_demo(1))
        b = R.analizar_elf(R.binario_demo(1, stripped=True))
        sa = next(s for s in a["secciones"] if s["nombre"] == ".text")
        sb = next(s for s in b["secciones"] if s["nombre"] == ".text")
        self.assertEqual(sa["sha256"], sb["sha256"])

    def test_entry_apunta_a_text(self):
        info = R.analizar_elf(R.binario_demo(1))
        texto = next(s for s in info["secciones"] if s["nombre"] == ".text")
        self.assertEqual(info["entry"], texto["addr"])

    def test_cadenas_con_offset(self):
        datos = R.binario_demo(1)
        cad = dict((t, o) for o, t in R.extraer_cadenas(datos))
        self.assertIn("Licencia invalida", cad)
        self.assertEqual(datos[cad["Licencia invalida"]:cad["Licencia invalida"] + 17], b"Licencia invalida")

    def test_rechaza_basura(self):
        with self.assertRaises(R.ErrorFormato):
            R.analizar_elf(b"MZ" + b"\x00" * 100)
        with self.assertRaises(R.ErrorFormato):
            R.analizar_elf(b"\x7fELF\x01\x01" + b"\x00" * 100)  # ELF32

    def test_rechaza_tabla_de_secciones_truncada(self):
        with self.assertRaises(R.ErrorFormato):
            R.analizar_elf(R.binario_demo(1)[:-40])


class Entropia(unittest.TestCase):
    def test_extremos(self):
        self.assertEqual(R.entropia(b""), 0.0)
        self.assertEqual(R.entropia(b"\x00" * 100), 0.0)
        self.assertAlmostEqual(R.entropia(bytes(range(256))), 8.0, places=6)

    def test_seccion_empaquetada_se_marca(self):
        info = R.analizar_elf(R.binario_empaquetado())
        self.assertEqual([s["nombre"] for s in R.secciones_sospechosas(info)], [".packed"])

    def test_binario_normal_no_se_marca(self):
        self.assertEqual(R.secciones_sospechosas(R.analizar_elf(R.binario_demo(1))), [])


class Comparacion(unittest.TestCase):
    def test_solo_cambia_copy_name(self):
        d = R.comparar_versiones(R.binario_demo(1), R.binario_demo(2))
        self.assertEqual(d["nivel"], "funcion")
        self.assertEqual(d["funciones_cambiadas"], ["copy_name"])
        self.assertIn("Nombre demasiado largo", d["cadenas_nuevas"])
        self.assertIn("build-1.0.0", d["cadenas_eliminadas"])
        self.assertGreater(d["bytes_cambiados"]["copy_name"], 0)

    def test_sin_simbolos_degrada_a_seccion(self):
        d = R.comparar_versiones(R.binario_demo(1, stripped=True), R.binario_demo(2, stripped=True))
        self.assertEqual(d["nivel"], "seccion")
        self.assertEqual(d["funciones_cambiadas"], [])
        self.assertIn(".text", d["secciones_cambiadas"])

    def test_identicos(self):
        d = R.comparar_versiones(R.binario_demo(1), R.binario_demo(1))
        self.assertEqual(d["funciones_cambiadas"], [])
        self.assertEqual(d["secciones_cambiadas"], [])


class ArtefactoComoDato(unittest.TestCase):
    def test_detecta_texto_dirigido_en_dos_idiomas(self):
        h = R.detectar_texto_dirigido(R.extraer_cadenas(R.binario_con_texto_dirigido()))
        self.assertEqual(len(h), 2)

    def test_cadenas_normales_no_se_marcan(self):
        self.assertEqual(R.detectar_texto_dirigido(R.extraer_cadenas(R.binario_demo(2))), [])

    def test_el_informe_no_obedece_el_texto(self):
        informe = R.informe_triaje(R.binario_con_texto_dirigido(), "muestra")
        self.assertIn("se trata como DATO", informe.replace("Se trata", "se trata"))
        self.assertIn("Texto dirigido a un lector", informe)

    def test_ausencia_de_indicios_no_declara_inocuo(self):
        informe = R.informe_triaje(R.binario_demo(1), "demo")
        self.assertIn("no demuestra", informe)


class Hipotesis(unittest.TestCase):
    def test_no_se_confirma_sin_evidencia(self):
        r = R.RegistroHipotesis()
        h = r.proponer("copy_name no limita la longitud", origen="agente")
        with self.assertRaises(ValueError):
            r.resolver(h, "confirmada", [])
        with self.assertRaises(ValueError):
            r.resolver(h, "confirmada", ["  "])
        r.resolver(h, "confirmada", ["demo_v1.elf .text+0x20: rep movsb sin comparacion previa"])
        self.assertEqual(r.pendientes(), [])

    def test_estado_invalido(self):
        r = R.RegistroHipotesis()
        h = r.proponer("x")
        with self.assertRaises(ValueError):
            r.resolver(h, "probablemente", ["algo"])

    def test_pendientes(self):
        r = R.RegistroHipotesis()
        r.proponer("a")
        r.proponer("b")
        r.resolver(1, "refutada", ["evidencia"])
        self.assertEqual([i["id"] for i in r.pendientes()], [2])


class Seguridad(unittest.TestCase):
    def test_el_laboratorio_no_usa_red_ni_procesos(self):
        fuente = (Path(__file__).resolve().parents[1] / "ri_lab.py").read_text(encoding="utf-8")
        for prohibido in ("import socket", "import subprocess", "import urllib", "import requests", "os.system",
                          "import ctypes"):
            self.assertNotIn(prohibido, fuente)


class Cli(unittest.TestCase):
    def test_demo_escribe_y_es_determinista(self):
        with tempfile.TemporaryDirectory() as t1, tempfile.TemporaryDirectory() as t2:
            self.assertEqual(R.main(["demo", "--out", t1]), 0)
            self.assertEqual(R.main(["demo", "--out", t2]), 0)
            self.assertEqual((Path(t1) / "resumen.json").read_text(), (Path(t2) / "resumen.json").read_text())
            self.assertTrue((Path(t1) / "diff_v1_v2.md").exists())

    def test_archivo_inexistente_devuelve_error(self):
        self.assertEqual(R.main(["triaje", "no-existe.elf"]), 2)


if __name__ == "__main__":
    unittest.main()
