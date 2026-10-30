"""Pruebas de regresión del laboratorio de code review / SAST.

La idea central: cada corrección se demuestra con DOS ejecuciones de la misma
prueba de ataque.

  * contra `vulnerable_app/app.py` el ataque FUNCIONA  -> la prueba confirma la debilidad;
  * contra `vulnerable_app/app_corregida.py` FALLA     -> la prueba confirma la defensa.

Si la prueba no fallara sobre el código original, no demostraría nada: podría
pasar también con un código que nunca estuvo roto.

Para no exigir Flask, se inyecta un sustituto mínimo (`FlaskFalso`) que registra
rutas y ofrece `request` y `abort`. Se prueba el código REAL de cada vista,
llamándola directamente. Nada se ejecuta contra la red ni contra el sistema:
`subprocess` y `open` se sustituyen por registradores, y la base de datos es un
SQLite temporal.

    python -m unittest discover -s labs/appsec-code/tests -v
"""
from __future__ import annotations

import ast
import contextlib
import gc
import importlib.util
import json
import os
import posixpath
import re
import sqlite3
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

LAB = Path(__file__).resolve().parents[1]
APP_DIR = LAB / "vulnerable_app"
RAIZ = LAB.parents[1]
MAPA = json.loads((LAB / "cwe-map.json").read_text(encoding="utf-8"))


# --------------------------------------------------------------------------
# Sustituto mínimo de Flask
# --------------------------------------------------------------------------
class Abortado(Exception):
    """Equivale a la excepción HTTP que lanza flask.abort(código)."""

    def __init__(self, codigo: int):
        super().__init__(codigo)
        self.codigo = codigo


class _Peticion:
    def __init__(self):
        self.args: dict[str, str] = {}
        self.cuerpo: bytes = b""

    def get_data(self) -> bytes:
        return self.cuerpo


def crear_flask_falso() -> types.ModuleType:
    mod = types.ModuleType("flask")
    peticion = _Peticion()

    class Flask:
        def __init__(self, nombre):
            self.rutas = {}
            self.ejecuciones = []

        def route(self, ruta):
            def registrar(f):
                self.rutas[ruta] = f
                return f
            return registrar

        def run(self, **kwargs):
            self.ejecuciones.append(kwargs)

    def abort(codigo):
        raise Abortado(codigo)

    mod.Flask, mod.request, mod.abort = Flask, peticion, abort
    return mod


def cargar_app(archivo: str, entorno: dict[str, str] | None = None, ejecutar_main: bool = False):
    """Importa una de las apps con el Flask falso. Devuelve (módulo, flask_falso)."""
    falso = crear_flask_falso()
    nombre = "app_bajo_prueba_" + Path(archivo).stem
    spec = importlib.util.spec_from_file_location(nombre, APP_DIR / archivo)
    modulo = importlib.util.module_from_spec(spec)
    with mock.patch.dict(sys.modules, {"flask": falso}), mock.patch.dict(os.environ, entorno or {}):
        spec.loader.exec_module(modulo)
        if ejecutar_main:
            modulo.__name__ = "__main__"
    return modulo, falso


@contextlib.contextmanager
def en_directorio_temporal():
    anterior = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        try:
            yield Path(tmp)
        finally:
            os.chdir(anterior)
            # La app original no cierra su conexión SQLite (otro defecto que la corregida arregla).
            # En Windows un archivo abierto no se puede borrar: se fuerza la liberación antes de limpiar.
            gc.collect()


def llamar(modulo, falso, ruta: str, args: dict | None = None, cuerpo: bytes = b""):
    falso.request.args = args or {}
    falso.request.cuerpo = cuerpo
    return modulo.app.rutas[ruta]() if hasattr(modulo.app, "rutas") else None


# --------------------------------------------------------------------------
# 1 · CWE-798 / 259 · secretos
# --------------------------------------------------------------------------
class Secretos(unittest.TestCase):
    AWS = re.compile(r"AKIA[0-9A-Z]{16}")

    def test_secretos_no_estan_en_el_codigo(self):
        original = (APP_DIR / "app.py").read_text(encoding="utf-8")
        corregida = (APP_DIR / "app_corregida.py").read_text(encoding="utf-8")
        # La app original contiene ambos secretos...
        self.assertIn("SuperSecreta123!", original)
        self.assertTrue(self.AWS.search(original))
        # ...y la corregida ninguno, ni siquiera comentado.
        self.assertNotIn("SuperSecreta123!", corregida)
        self.assertFalse(self.AWS.search(corregida))

    def test_la_contrasena_se_lee_del_entorno_sin_valor_por_defecto(self):
        m, _ = cargar_app("app_corregida.py", {"DB_PASSWORD": "valor-de-prueba"})
        self.assertEqual(m.DB_PASSWORD, "valor-de-prueba")
        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("DB_PASSWORD", None)
            m2, _ = cargar_app("app_corregida.py")
            self.assertIsNone(m2.DB_PASSWORD)  # sin configurar: None, nunca una contraseña por defecto


# --------------------------------------------------------------------------
# 2 · CWE-89 · inyección SQL
# --------------------------------------------------------------------------
class InyeccionSQL(unittest.TestCase):
    PAYLOAD = "x' OR '1'='1"

    def preparar_bd(self):
        con = sqlite3.connect("app.db")
        con.execute("CREATE TABLE users (name TEXT, secreto TEXT)")
        con.executemany("INSERT INTO users VALUES (?, ?)", [("alice", "secreto-de-alice"), ("bob", "secreto-de-bob")])
        con.commit()
        con.close()

    def filas(self, archivo: str, nombre: str) -> list:
        m, f = cargar_app(archivo)
        with en_directorio_temporal():
            self.preparar_bd()
            f.request.args = {"name": nombre}
            return m.get_user()["rows"]

    def test_inyeccion_sql(self):
        # Entrada legítima: igual en ambas.
        self.assertEqual(len(self.filas("app.py", "alice")), 1)
        self.assertEqual(len(self.filas("app_corregida.py", "alice")), 1)
        # Ataque: en la original cambia la estructura de la consulta y devuelve TODAS las filas.
        self.assertEqual(len(self.filas("app.py", self.PAYLOAD)), 2)
        # En la corregida la misma cadena es solo un nombre que no existe.
        self.assertEqual(self.filas("app_corregida.py", self.PAYLOAD), [])


# --------------------------------------------------------------------------
# 3 · CWE-78 · inyección de comandos
# --------------------------------------------------------------------------
class InyeccionDeComandos(unittest.TestCase):
    ATAQUE = "127.0.0.1; echo comando-inyectado"

    def test_inyeccion_de_comandos(self):
        # Original: la entrada llega CONCATENADA a una cadena que se pasa al shell.
        m, f = cargar_app("app.py")
        f.request.args = {"host": self.ATAQUE}
        with mock.patch("subprocess.check_output", return_value=b"") as sp:
            m.ping()
        orden = sp.call_args.args[0]
        self.assertIsInstance(orden, str)
        self.assertIn("; echo comando-inyectado", orden)
        self.assertTrue(sp.call_args.kwargs.get("shell"))

        # Corregida: el ataque se rechaza antes de ejecutar nada...
        m, f = cargar_app("app_corregida.py")
        f.request.args = {"host": self.ATAQUE}
        with mock.patch("subprocess.run") as sp:
            with self.assertRaises(Abortado) as cm:
                m.ping()
        self.assertEqual(cm.exception.codigo, 400)
        sp.assert_not_called()

    def test_la_version_corregida_no_pasa_por_el_shell_y_acepta_hosts_legitimos(self):
        m, f = cargar_app("app_corregida.py")
        for legitimo in ("example.com", "127.0.0.1", "::1", "sub.dominio-1.example.org"):
            f.request.args = {"host": legitimo}
            with mock.patch("subprocess.run") as sp:
                sp.return_value.stdout = b"ok"
                self.assertEqual(m.ping(), b"ok")
            self.assertEqual(sp.call_args.args[0], ["ping", "-c", "1", legitimo])  # lista, no cadena
            self.assertFalse(sp.call_args.kwargs.get("shell", False))

    def test_la_validacion_rechaza_opciones_y_metacaracteres(self):
        m, _ = cargar_app("app_corregida.py")
        for malo in ("-f", "--help", "a b", "a;b", "$(id)", "`id`", "a|b", "a&b", "a\nb", "", "-" + "a" * 10,
                     "a" * 300, "exa_mple.com", ".com", "a..com"):
            self.assertFalse(m._host_valido(malo), repr(malo))


# --------------------------------------------------------------------------
# 4 · CWE-916 · hash de contraseña
# --------------------------------------------------------------------------
class HashDeContrasena(unittest.TestCase):
    def test_hash_de_contrasena(self):
        # Original: MD5 sin sal -> siempre el mismo valor, conocido en tablas públicas.
        m, f = cargar_app("app.py")
        f.request.args = {"pwd": "password"}
        h1, h2 = m.hash_password()["hash"], m.hash_password()["hash"]
        self.assertEqual(h1, h2)
        self.assertEqual(h1, "5f4dcc3b5aa765d61d8327deb882cf99")  # md5("password"), valor público de referencia

        # Corregida: con sal, dos hashes de la misma contraseña difieren, y se puede verificar.
        c, f = cargar_app("app_corregida.py")
        c.SCRYPT_N = 2**4  # solo para que la prueba sea rápida; producción usa 2**17
        f.request.args = {"pwd": "password"}
        a, b = c.hash_password()["hash"], c.hash_password()["hash"]
        self.assertNotEqual(a, b)
        self.assertTrue(a.startswith("scrypt$"))
        self.assertTrue(c.verificar_contrasena("password", a))
        self.assertTrue(c.verificar_contrasena("password", b))
        self.assertFalse(c.verificar_contrasena("otra", a))

    def test_verificacion_rechaza_entradas_manipuladas(self):
        c, _ = cargar_app("app_corregida.py")
        c.SCRYPT_N = 2**4
        valido = c.hash_contrasena("clave")
        for roto in ("", "basura", valido[:-2], valido.replace("scrypt", "md5"), "scrypt$x$y$z$w$v", valido + "00"):
            self.assertFalse(c.verificar_contrasena("clave", roto), roto)

    def test_parametros_de_scrypt_son_los_de_owasp(self):
        c, _ = cargar_app("app_corregida.py")
        # Combinación mínima de la guía de OWASP (Password Storage Cheat Sheet): N=2^17, r=8, p=1.
        self.assertEqual((c.SCRYPT_N, c.SCRYPT_R, c.SCRYPT_P), (2**17, 8, 1))


# --------------------------------------------------------------------------
# 5 · CWE-502 · deserialización
# --------------------------------------------------------------------------
class Sonda:
    """Objeto que, al deserializarse con pickle, LLAMA a os.getcwd (inofensivo, pero es ejecución)."""

    def __reduce__(self):
        return (os.getcwd, ())


class Deserializacion(unittest.TestCase):
    def test_deserializacion(self):
        import pickle
        carga = pickle.dumps(Sonda())

        m, f = cargar_app("app.py")
        f.request.cuerpo = carga
        # La original EJECUTÓ una función indicada por el atacante: el «objeto» cargado es su resultado.
        self.assertEqual(m.load_object()["loaded"], os.getcwd())

        c, f = cargar_app("app_corregida.py")
        f.request.cuerpo = carga
        with self.assertRaises(Abortado) as cm:
            c.load_object()
        self.assertEqual(cm.exception.codigo, 400)

        f.request.cuerpo = b'{"clave": [1, 2, 3]}'
        self.assertIn("clave", c.load_object()["loaded"])  # JSON legítimo sigue funcionando


# --------------------------------------------------------------------------
# 6 · CWE-22 · path traversal
# --------------------------------------------------------------------------
class PathTraversal(unittest.TestCase):
    def test_path_traversal(self):
        # Original: la ruta se arma por concatenación y NO se normaliza ni se comprueba.
        m, f = cargar_app("app.py")
        f.request.args = {"file": "../../etc/passwd"}
        with mock.patch("builtins.open", mock.mock_open(read_data="x")) as abierto:
            m.read_file()
        pedido = abierto.call_args.args[0]
        self.assertEqual(pedido, "/var/data/../../etc/passwd")
        self.assertFalse(posixpath.normpath(pedido).startswith("/var/data"))  # sale del directorio

        # Corregida: la ruta se resuelve y se comprueba contra el directorio permitido.
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            base = raiz / "datos"
            base.mkdir()
            (base / "ok.txt").write_text("contenido permitido", encoding="utf-8")
            (raiz / "secreto.txt").write_text("fuera", encoding="utf-8")
            (raiz / "datos-secretos").mkdir()  # hermano cuyo nombre EMPIEZA igual que «datos»
            (raiz / "datos-secretos" / "x.txt").write_text("fuera", encoding="utf-8")

            c, f = cargar_app("app_corregida.py", {"DATA_DIR": str(base)})
            f.request.args = {"file": "ok.txt"}
            self.assertEqual(c.read_file(), "contenido permitido")
            for ataque in ("../secreto.txt", "../../secreto.txt", str(raiz / "secreto.txt"),
                           "../datos-secretos/x.txt", "subdir/../../secreto.txt"):
                f.request.args = {"file": ataque}
                with self.assertRaises(Abortado, msg=ataque) as cm:
                    c.read_file()
                self.assertEqual(cm.exception.codigo, 403, ataque)

    @unittest.skipUnless(hasattr(os, "symlink") and os.name != "nt", "enlaces simbólicos: se prueban en Linux/macOS")
    def test_un_enlace_simbolico_hacia_fuera_tambien_se_bloquea(self):
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp)
            (raiz / "datos").mkdir()
            (raiz / "secreto.txt").write_text("fuera", encoding="utf-8")
            os.symlink(raiz / "secreto.txt", raiz / "datos" / "atajo.txt")
            c, f = cargar_app("app_corregida.py", {"DATA_DIR": str(raiz / "datos")})
            f.request.args = {"file": "atajo.txt"}
            with self.assertRaises(Abortado):
                c.read_file()


# --------------------------------------------------------------------------
# 7 · CWE-95 · eval
# --------------------------------------------------------------------------
class EvaluacionDeCodigo(unittest.TestCase):
    def test_evaluacion_de_codigo(self):
        ataque = "__import__('math').sqrt(16)"  # importa un módulo arbitrario: inofensivo pero prueba el punto
        m, f = cargar_app("app.py")
        f.request.args = {"expr": ataque}
        self.assertEqual(m.calc()["result"], 4.0)  # la original EJECUTÓ código Python arbitrario

        c, f = cargar_app("app_corregida.py")
        f.request.args = {"expr": ataque}
        with self.assertRaises(Abortado) as cm:
            c.calc()
        self.assertEqual(cm.exception.codigo, 400)

    def test_la_aritmetica_legitima_sigue_funcionando(self):
        c, f = cargar_app("app_corregida.py")
        for expr, esperado in (("1+1", 2), ("2*(3+4)", 14), ("-5 + 2", -3), ("7 // 2", 3), ("7 % 4", 3), ("1/4", 0.25)):
            f.request.args = {"expr": expr}
            self.assertEqual(c.calc()["result"], esperado, expr)

    def test_las_expresiones_muy_anidadas_no_derrumban_el_evaluador(self):
        # Aviso de MITRE en CWE-95: la estructura profundamente anidada es un vector de agotamiento de recursos.
        c, _ = cargar_app("app_corregida.py")
        self.assertEqual(c.evaluar_aritmetica("(" * 49 + "1" + ")" * 49), 1)      # 99 caracteres: cabe en el tope
        self.assertEqual(c.evaluar_aritmetica("-" * 99 + "1"), -1)
        for malo in ("(" * 100, "(" * 400 + "1" + ")" * 400, "-" * 5000 + "1"):
            with self.assertRaises(ValueError, msg=malo[:12]):
                c.evaluar_aritmetica(malo)

    def test_todo_lo_demas_se_rechaza(self):
        c, _ = cargar_app("app_corregida.py")
        peligrosos = ["__import__('os')", "open('/etc/passwd')", "().__class__", "[1]", "'a'*10", "x + 1", "lambda: 1",
                      "9**9**9", "2**64", "1 if 1 else 2", "print(1)", "1;2", "", "1 +", "a.b", "True", "1j", "not 1",
                      "1" + "+1" * 100]
        for p in peligrosos:
            with self.assertRaises(ValueError, msg=repr(p)):
                c.evaluar_aritmetica(p)

    def test_division_por_cero_es_un_rechazo_no_un_error_500(self):
        c, f = cargar_app("app_corregida.py")
        f.request.args = {"expr": "1/0"}
        with self.assertRaises(Abortado) as cm:
            c.calc()
        self.assertEqual(cm.exception.codigo, 400)


# --------------------------------------------------------------------------
# 8 · CWE-489 / 1327 · depuración y enlace
# --------------------------------------------------------------------------
def llamadas_a_run(archivo: str) -> list[dict]:
    """Argumentos con que el código fuente llama a app.run(...), leídos del árbol sintáctico."""
    arbol = ast.parse((APP_DIR / archivo).read_text(encoding="utf-8"))
    salida = []
    for nodo in ast.walk(arbol):
        if (isinstance(nodo, ast.Call) and isinstance(nodo.func, ast.Attribute) and nodo.func.attr == "run"
                and isinstance(nodo.func.value, ast.Name) and nodo.func.value.id == "app"):  # app.run, no subprocess.run
            salida.append({k.arg: ast.literal_eval(k.value) for k in nodo.keywords})
    return salida


class DepuracionYEnlace(unittest.TestCase):
    def test_depuracion_y_enlace(self):
        self.assertEqual(llamadas_a_run("app.py"), [{"host": "0.0.0.0", "debug": True}])
        self.assertEqual(llamadas_a_run("app_corregida.py"), [{"host": "127.0.0.1", "debug": False}])


# --------------------------------------------------------------------------
# Coherencia del mapa CWE con el código, las pruebas, Bandit y el catálogo
# --------------------------------------------------------------------------
class MapaCWE(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = (APP_DIR / "app.py").read_text(encoding="utf-8")
        cls.corregida = (APP_DIR / "app_corregida.py").read_text(encoding="utf-8")
        cls.pruebas = Path(__file__).read_text(encoding="utf-8")
        cls.bandit = json.loads((LAB / "tests" / "datos" / "bandit-1.9.4-app.json").read_text(encoding="utf-8"))

    def test_hay_ocho_vulnerabilidades_numeradas(self):
        self.assertEqual([v["id"] for v in MAPA["vulnerabilidades"]], list(range(1, 9)))

    def test_cada_marcador_esta_en_la_app_vulnerable_y_cada_correccion_en_la_corregida(self):
        for v in MAPA["vulnerabilidades"]:
            with self.subTest(vuln=v["id"]):
                self.assertIn(v["marcador"], self.original)
                self.assertIn(v["simbolo_correccion"], self.corregida)

    def test_cada_vulnerabilidad_tiene_una_prueba_que_existe(self):
        for v in MAPA["vulnerabilidades"]:
            with self.subTest(vuln=v["id"]):
                self.assertRegex(self.pruebas, rf"def {v['prueba']}\b")

    def test_lo_que_el_mapa_dice_de_bandit_coincide_con_su_salida_verificada(self):
        por_linea: dict[int, list[dict]] = {}
        for r in self.bandit["results"]:
            por_linea.setdefault(r["line_number"], []).append(r)
        lineas = self.original.splitlines()

        def linea_de(marcador: str) -> int:
            return next(i + 1 for i, ln in enumerate(lineas) if marcador in ln)

        for v in MAPA["vulnerabilidades"]:
            with self.subTest(vuln=v["id"]):
                hallazgos = por_linea.get(linea_de(v["marcador"]), [])
                reglas = {h["test_id"]: f"CWE-{h['issue_cwe']['id']}" for h in hallazgos}
                b = v["bandit"]
                if b["detecta"]:
                    self.assertIn(b["regla"], reglas, f"Bandit ya no reporta {b['regla']} en esa línea")
                    self.assertEqual(reglas[b["regla"]], b["cwe_reportado"])
                else:
                    self.assertEqual(reglas, {}, "el mapa dice que Bandit no lo detecta, pero hay hallazgos")

    def test_la_clave_aws_es_un_falso_negativo_de_bandit(self):
        lineas = self.original.splitlines()
        n_aws = next(i + 1 for i, ln in enumerate(lineas) if ln.startswith("AWS_KEY"))
        self.assertNotIn(n_aws, {r["line_number"] for r in self.bandit["results"]})

    def test_eval_tiene_en_bandit_un_cwe_distinto_al_correcto(self):
        eval_ = next(v for v in MAPA["vulnerabilidades"] if v["id"] == 7)
        self.assertNotEqual(eval_["bandit"]["cwe_reportado"], eval_["cwe_principal"])

    def test_los_cwe_del_mapa_existen_y_estan_vigentes_en_el_catalogo_local(self):
        sys.path.insert(0, str(RAIZ / "scripts"))
        import cwe_lib as L
        if not (L.NORMALIZADO / "cwe.jsonl").is_file():
            self.skipTest("base CWE no importada")
        base = L.BaseCWE.cargar()
        ids = set()
        for v in MAPA["vulnerabilidades"]:
            ids.add(v["cwe_principal"])
            ids.update(a["id"] for a in v["cwe_alternativas"])
            if v["bandit"]["cwe_reportado"]:
                ids.add(v["bandit"]["cwe_reportado"])
        for cid in sorted(ids):
            with self.subTest(cwe=cid):
                self.assertIn(cid, base)
                self.assertNotEqual(base.obtener(cid)["estado"], "Deprecated")

    def test_el_cwe_principal_es_hijo_o_igual_de_lo_que_dice_la_herramienta_cuando_deberia(self):
        """Donde el mapa elige una entrada más específica que la de Bandit, debe ser su descendiente."""
        sys.path.insert(0, str(RAIZ / "scripts"))
        import cwe_lib as L
        if not (L.NORMALIZADO / "cwe.jsonl").is_file():
            self.skipTest("base CWE no importada")
        base = L.BaseCWE.cargar()

        def desciende(hijo: str, ancestro: str) -> bool:
            return any(ancestro in camino for camino in base.ancestros(hijo))

        pares = {  # id de la vulnerabilidad -> (principal, referencia con la que debe estar emparentada)
            1: ("CWE-259", "CWE-798"),   # Bandit (259) es hija del paraguas (798)
            4: ("CWE-916", "CWE-328"),   # principal (916) es hija de «hash débil»
            6: ("CWE-23", "CWE-22"),
            7: ("CWE-95", "CWE-94"),
        }
        for _, (hijo, padre) in pares.items():
            with self.subTest(hijo=hijo, padre=padre):
                self.assertTrue(desciende(hijo, padre), f"{hijo} debería descender de {padre} en el catálogo")


if __name__ == "__main__":
    unittest.main()
