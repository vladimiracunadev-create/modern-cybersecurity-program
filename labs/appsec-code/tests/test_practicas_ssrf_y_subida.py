"""Pruebas de las prácticas de la clase 363: SSRF (`practicas/ssrf.py`) y subida de archivos (`practicas/subida.py`).

Sin red y sin azar: el resolutor de nombres es un diccionario y los nombres de archivo se inyectan.

    python -m unittest discover -s labs/appsec-code/tests -v
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB / "practicas"))

import ssrf as S  # noqa: E402
import subida as U  # noqa: E402

PERMITIDOS = {"api.ejemplo.org", "cdn.ejemplo.org"}


def resolutor_de(tabla: dict[str, list[str]]):
    def resolver(nombre: str) -> list[str]:
        return list(tabla.get(nombre, []))
    return resolver


PUBLICO = resolutor_de({"api.ejemplo.org": ["93.184.216.34"], "cdn.ejemplo.org": ["93.184.216.35"]})


class SSRFVulnerable(unittest.TestCase):
    """CWE-918: la versión vulnerable solo mira el esquema."""

    def test_acepta_el_servicio_de_metadatos_de_la_nube(self):
        self.assertEqual(S.validar_url_vulnerable("http://169.254.169.254/latest/meta-data/"),
                         "http://169.254.169.254/latest/meta-data/")

    def test_acepta_servicios_internos_y_localhost(self):
        for url in ("http://10.0.0.5:8080/admin", "http://127.0.0.1:6379/", "http://localhost/"):
            with self.subTest(url=url):
                self.assertEqual(S.validar_url_vulnerable(url), url)

    def test_al_menos_rechaza_esquemas_que_no_son_http(self):
        with self.assertRaises(S.DestinoNoPermitido):
            S.validar_url_vulnerable("file:///etc/passwd")


class SSRFCorrecta(unittest.TestCase):
    def test_un_host_permitido_que_resuelve_a_una_direccion_publica_se_acepta(self):
        host, ip, puerto = S.resolver_destino("https://api.ejemplo.org/datos?x=1", PERMITIDOS, PUBLICO)
        self.assertEqual((host, ip, puerto), ("api.ejemplo.org", "93.184.216.34", 443))

    def test_el_mismo_host_permitido_resolviendo_a_una_direccion_interna_se_rechaza(self):
        for interna in ("169.254.169.254", "127.0.0.1", "10.0.0.5", "192.168.1.10", "172.16.0.9",
                        "::1", "fe80::1", "::ffff:127.0.0.1", "0.0.0.0", "100.64.0.1"):
            with self.subTest(direccion=interna):
                resolutor = resolutor_de({"api.ejemplo.org": [interna]})
                with self.assertRaises(S.DestinoNoPermitido):
                    S.resolver_destino("https://api.ejemplo.org/", PERMITIDOS, resolutor)

    def test_si_una_sola_de_las_direcciones_es_interna_se_rechaza(self):
        resolutor = resolutor_de({"api.ejemplo.org": ["93.184.216.34", "10.0.0.5"]})
        with self.assertRaises(S.DestinoNoPermitido):
            S.resolver_destino("https://api.ejemplo.org/", PERMITIDOS, resolutor)

    def test_los_hosts_que_no_estan_en_la_lista_se_rechazan_aunque_resuelvan_a_publico(self):
        resolutor = resolutor_de({"otro.ejemplo.org": ["93.184.216.40"]})
        with self.assertRaises(S.DestinoNoPermitido):
            S.resolver_destino("https://otro.ejemplo.org/", PERMITIDOS, resolutor)

    def test_las_formas_alternativas_de_escribir_una_direccion_no_pasan_la_lista_de_nombres(self):
        for url in ("http://2130706433/", "http://0x7f000001/", "http://0177.0.0.1/", "http://[::1]/",
                    "http://127.1/", "http://localhost/"):
            with self.subTest(url=url):
                with self.assertRaises(S.DestinoNoPermitido):
                    S.resolver_destino(url, PERMITIDOS, PUBLICO)

    def test_las_credenciales_en_la_url_no_engañan_al_analisis_del_host(self):
        # el host real de esta URL es 169.254.169.254, no el nombre permitido que aparece antes de la arroba
        with self.assertRaises(S.DestinoNoPermitido):
            S.resolver_destino("https://api.ejemplo.org@169.254.169.254/", PERMITIDOS, PUBLICO)
        with self.assertRaises(S.DestinoNoPermitido):
            S.resolver_destino("https://usuario:clave@api.ejemplo.org/", PERMITIDOS, PUBLICO)

    def test_esquemas_y_puertos_fuera_de_lo_esperado_se_rechazan(self):
        for url in ("file:///etc/passwd", "gopher://api.ejemplo.org/", "ftp://api.ejemplo.org/",
                    "https://api.ejemplo.org:6379/", "http://api.ejemplo.org:22/"):
            with self.subTest(url=url):
                with self.assertRaises(S.DestinoNoPermitido):
                    S.resolver_destino(url, PERMITIDOS, PUBLICO)

    def test_un_nombre_que_no_resuelve_se_rechaza(self):
        with self.assertRaises(S.DestinoNoPermitido):
            S.resolver_destino("https://api.ejemplo.org/", PERMITIDOS, resolutor_de({}))

    def test_el_nombre_se_resuelve_una_vez_y_se_conecta_a_esa_direccion(self):
        """DNS rebinding: la primera respuesta es pública y la segunda, interna. Se usa la primera y no se vuelve a preguntar."""
        respuestas = [["93.184.216.34"], ["127.0.0.1"]]
        consultas = []

        def cambiante(nombre: str) -> list[str]:
            consultas.append(nombre)
            return respuestas[min(len(consultas) - 1, 1)]

        _, ip, _ = S.resolver_destino("https://api.ejemplo.org/", PERMITIDOS, cambiante)
        self.assertEqual(ip, "93.184.216.34")
        self.assertEqual(len(consultas), 1)  # la función no resuelve dos veces: el llamador conecta a `ip`

    def test_las_mayusculas_en_el_nombre_no_evitan_la_lista(self):
        host, _, _ = S.resolver_destino("https://API.Ejemplo.ORG/", PERMITIDOS, PUBLICO)
        self.assertEqual(host, "api.ejemplo.org")

    def test_cada_salto_de_una_redireccion_se_valida_igual(self):
        actual = "https://api.ejemplo.org/a"
        # redirección hacia el servicio de metadatos, absoluta
        with self.assertRaises(S.DestinoNoPermitido):
            S.seguir_redireccion(actual, "http://169.254.169.254/latest/meta-data/", PERMITIDOS, PUBLICO)
        # redirección relativa al mismo host permitido: válida
        host, ip, puerto = S.seguir_redireccion(actual, "/b", PERMITIDOS, PUBLICO)
        self.assertEqual((host, ip, puerto), ("api.ejemplo.org", "93.184.216.34", 443))
        # redirección a otro host permitido que resuelve a una dirección interna
        interno = resolutor_de({"cdn.ejemplo.org": ["10.1.1.1"]})
        with self.assertRaises(S.DestinoNoPermitido):
            S.seguir_redireccion(actual, "https://cdn.ejemplo.org/c", PERMITIDOS, interno)


PNG = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16
JPG = b"\xff\xd8\xff\xe0" + b"\x00" * 16
PDF = b"%PDF-1.7\n" + b"\x00" * 16
# Marcador inofensivo: lo que importa a la defensa es el nombre y los primeros bytes, no lo que haría el script.
# (Una carga con aspecto de webshell real podría ser borrada por un antivirus en mitad de la prueba.)
PHP = b"#!/bin/sh\n# SIMULACION: contenido de un script, no hace nada\n"


class SubidaVulnerable(unittest.TestCase):
    """CWE-434: el servidor guarda lo que le llega con el nombre que elige el cliente."""

    def test_un_script_ejecutable_se_guarda_con_su_extension(self):
        with tempfile.TemporaryDirectory() as tmp:
            destino = U.guardar_vulnerable("perfil.php", PHP, Path(tmp))
            self.assertEqual(destino.name, "perfil.php")
            self.assertEqual(destino.read_bytes(), PHP)

    def test_un_nombre_conocido_permite_sobrescribir_un_archivo_existente(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "logo.png").write_bytes(PNG)
            U.guardar_vulnerable("logo.png", PHP, Path(tmp))
            self.assertEqual((Path(tmp) / "logo.png").read_bytes(), PHP)


class SubidaCorrecta(unittest.TestCase):
    def guardar(self, nombre, contenido, nombre_generado="abc123"):
        with tempfile.TemporaryDirectory() as tmp:
            destino = U.guardar_correcto(nombre, contenido, Path(tmp), generar_nombre=lambda: nombre_generado)
            return destino.name, destino.read_bytes(), sorted(p.name for p in Path(tmp).iterdir())

    def test_los_tipos_legitimos_se_aceptan_con_nombre_generado(self):
        for nombre, contenido, ext in (("foto.png", PNG, ".png"), ("FOTO.JPG", JPG, ".jpg"), ("informe.pdf", PDF, ".pdf")):
            with self.subTest(nombre=nombre):
                guardado, datos, listado = self.guardar(nombre, contenido)
                self.assertEqual(guardado, "abc123" + ext)
                self.assertEqual(datos, contenido)
                self.assertEqual(listado, [guardado])

    def test_un_script_con_extension_peligrosa_se_rechaza(self):
        for nombre in ("perfil.php", "shell.jsp", "run.py", "x.exe", "sin_extension", ".htaccess"):
            with self.subTest(nombre=nombre):
                with self.assertRaises(U.SubidaRechazada):
                    self.guardar(nombre, PHP)

    def test_un_script_disfrazado_de_imagen_se_rechaza_por_su_contenido(self):
        for nombre in ("foto.png", "foto.jpg", "foto.pdf"):
            with self.subTest(nombre=nombre):
                with self.assertRaises(U.SubidaRechazada):
                    self.guardar(nombre, PHP)

    def test_un_png_declarado_como_pdf_se_rechaza(self):
        with self.assertRaises(U.SubidaRechazada):
            self.guardar("informe.pdf", PNG)

    def test_la_doble_extension_no_engaña_porque_solo_cuenta_la_ultima(self):
        with self.assertRaises(U.SubidaRechazada):
            self.guardar("foto.png.php", PNG)
        guardado, _, _ = self.guardar("foto.php.png", PNG)  # termina en .png y su contenido es un PNG
        self.assertEqual(guardado, "abc123.png")

    def test_el_nombre_original_no_llega_al_sistema_de_archivos(self):
        for nombre in ("../../etc/cron.d/x.png", "..\\..\\sistema.png", "/abs/ruta.png"):
            with self.subTest(nombre=nombre):
                guardado, _, listado = self.guardar(nombre, PNG)
                self.assertEqual(guardado, "abc123.png")
                self.assertEqual(listado, ["abc123.png"])

    def test_el_tamano_maximo_se_respeta_en_el_limite_exacto(self):
        justo = PNG + b"\x00" * (U.MAXIMO_BYTES - len(PNG))
        guardado, _, _ = self.guardar("grande.png", justo)
        self.assertEqual(guardado, "abc123.png")
        with self.assertRaises(U.SubidaRechazada):
            self.guardar("grande.png", justo + b"\x00")

    def test_dos_subidas_con_el_mismo_nombre_no_se_pisan_si_el_servidor_genera_nombres_distintos(self):
        with tempfile.TemporaryDirectory() as tmp:
            nombres = iter(["uno", "dos"])
            a = U.guardar_correcto("logo.png", PNG, Path(tmp), generar_nombre=lambda: next(nombres))
            b = U.guardar_correcto("logo.png", PNG, Path(tmp), generar_nombre=lambda: next(nombres))
            self.assertNotEqual(a, b)
            self.assertEqual(len(list(Path(tmp).iterdir())), 2)

    def test_el_archivo_guardado_no_es_ejecutable_en_sistemas_posix(self):
        import os
        if os.name == "nt":
            self.skipTest("los permisos POSIX no existen en Windows")
        with tempfile.TemporaryDirectory() as tmp:
            destino = U.guardar_correcto("foto.png", PNG, Path(tmp), generar_nombre=lambda: "n")
            self.assertEqual(destino.stat().st_mode & 0o111, 0)


if __name__ == "__main__":
    unittest.main()
