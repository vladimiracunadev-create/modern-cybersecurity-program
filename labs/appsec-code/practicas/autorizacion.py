# -*- coding: utf-8 -*-
"""Práctica de la clase 364: autorización rota (CWE-862, CWE-863, CWE-639).

Qué demuestra
-------------
Un sistema responde a dos preguntas distintas y casi siempre se confunden:

  AUTENTICACIÓN  ¿quién eres?                 (CWE-287, CWE-306...)
  AUTORIZACIÓN   ¿qué tienes permiso de hacer? (CWE-862, CWE-863, CWE-639...)

Que el usuario haya iniciado sesión (autenticación correcta) NO significa que pueda
leer el documento número 1. Esta práctica tiene dos implementaciones de la misma
función, una vulnerable y otra correcta, y una *matriz de acceso*: la prueba más
útil contra autorización rota, porque comprueba TODAS las parejas usuario-recurso
en lugar de las dos o tres que se le ocurren a quien programa.

Cómo se relaciona con el catálogo CWE
-------------------------------------
  CWE-862  Missing Authorization       No hay comprobación de autorización. (leer_vulnerable, borrar_vulnerable)
  CWE-863  Incorrect Authorization     Hay comprobación pero está mal hecha. (leer_con_error)
  CWE-639  Authorization Bypass Through User-Controlled Key
           El atacante cambia un identificador (doc_id) y accede a otro objeto: IDOR.

Todo es en memoria, sin red ni archivos, para que la práctica sea determinista.
"""
from __future__ import annotations

# Datos de ejemplo: dos usuarios con un documento cada uno y un administrador.
USUARIOS = {
    "ana": {"rol": "usuario"},
    "luis": {"rol": "usuario"},
    "root": {"rol": "admin"},
}
DOCUMENTOS = {
    1: {"dueno": "ana", "texto": "nómina de Ana"},
    2: {"dueno": "luis", "texto": "contrato de Luis"},
}


class Denegado(Exception):
    """Acceso no permitido. El mensaje es deliberadamente igual para «no existe» y «no es tuyo»."""


# ---------------------------------------------------------------------------
# Lectura de un documento
# ---------------------------------------------------------------------------
def leer_vulnerable(usuario: str, doc_id: int) -> str:
    """CWE-862 / CWE-639: comprueba que el documento existe pero no de quién es.

    Cualquier usuario autenticado puede leer cualquier documento con solo cambiar `doc_id`.
    """
    return DOCUMENTOS[doc_id]["texto"]


def leer_con_error(usuario: str, doc_id: int) -> str:
    """CWE-863: SÍ hay comprobación, pero está mal hecha.

    Error típico: confiar en el ROL en lugar de en la RELACIÓN con el recurso. Aquí se deja
    pasar a cualquiera con rol «usuario», que son todos los usuarios corrientes, de modo
    que se comprueba algo pero no lo que importa.
    """
    if USUARIOS[usuario]["rol"] in ("usuario", "admin"):
        return DOCUMENTOS[doc_id]["texto"]
    raise Denegado("recurso no disponible")


def leer_correcto(usuario: str, doc_id: int) -> str:
    """Autorización correcta: dueño del recurso o administrador, y misma respuesta si no existe.

    Responder igual a «no existe» y «no es tuyo» evita que el atacante use la diferencia para
    enumerar qué identificadores existen (eso sería exposición de información, CWE-200).
    """
    doc = DOCUMENTOS.get(doc_id)
    es_admin = USUARIOS.get(usuario, {}).get("rol") == "admin"
    if doc is None or (doc["dueno"] != usuario and not es_admin):
        raise Denegado("recurso no disponible")
    return doc["texto"]


# ---------------------------------------------------------------------------
# Autorización a nivel de función: una operación solo para administradores
# ---------------------------------------------------------------------------
def borrar_vulnerable(usuario: str, doc_id: int) -> bool:
    """CWE-862: la operación administrativa no comprueba el rol de quien la invoca.

    La interfaz puede ocultar el botón «borrar» a los usuarios corrientes, pero ocultar un botón
    no es autorizar: la petición se puede construir a mano.
    """
    DOCUMENTOS.pop(doc_id, None)
    return True


def borrar_correcto(usuario: str, doc_id: int) -> bool:
    """Autorización en el servidor, en la propia operación, con denegación por defecto."""
    if USUARIOS.get(usuario, {}).get("rol") != "admin":
        raise Denegado("operación no permitida")
    return DOCUMENTOS.pop(doc_id, None) is not None


# ---------------------------------------------------------------------------
# La prueba que de verdad detecta autorización rota: la matriz de acceso
# ---------------------------------------------------------------------------
# Política que queremos hacer cumplir: (usuario, documento) -> ¿debe poder leerlo?
POLITICA_LECTURA = {
    ("ana", 1): True, ("ana", 2): False,
    ("luis", 1): False, ("luis", 2): True,
    ("root", 1): True, ("root", 2): True,
}


def matriz_de_acceso(funcion, usuarios=USUARIOS, documentos=DOCUMENTOS) -> dict[tuple[str, int], bool]:
    """Ejecuta `funcion` para TODAS las parejas usuario-documento y devuelve quién pudo leer qué."""
    resultado = {}
    for u in usuarios:
        for d in documentos:
            try:
                funcion(u, d)
                resultado[(u, d)] = True
            except Denegado:
                resultado[(u, d)] = False
    return resultado


def violaciones(funcion) -> list[tuple[str, int]]:
    """Parejas en las que el comportamiento real difiere de la política. Lista vacía = correcto."""
    real = matriz_de_acceso(funcion)
    return sorted(par for par, esperado in POLITICA_LECTURA.items() if real[par] != esperado)
