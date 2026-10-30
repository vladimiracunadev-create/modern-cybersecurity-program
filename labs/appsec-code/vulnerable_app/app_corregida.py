# -*- coding: utf-8 -*-
"""
Versión CORREGIDA de `app.py` para el laboratorio de code review / SAST.

Conserva las mismas rutas y los mismos nombres de función que la app vulnerable
para que puedas compararlas con `diff` y para que las MISMAS pruebas
(`tests/test_correcciones.py`) demuestren dos cosas:

  1. contra `app.py`, el ataque funciona (la prueba confirma la debilidad);
  2. contra `app_corregida.py`, el mismo ataque falla (la prueba confirma la defensa).

Una corrección sin una prueba que fallaba antes de aplicarla es una opinión,
no una evidencia. Cada bloque dice qué CWE corrige y por qué esa solución y no otra.

No es un producto terminado: es la mínima corrección defendible de cada fallo,
sin autenticación ni registro de auditoría, que quedan fuera del laboratorio.
"""
import ast
import hashlib
import hmac
import ipaddress
import json
import operator
import os
import re
import sqlite3
import subprocess

from flask import Flask, abort, request

app = Flask(__name__)

# --- Fallo 1 · CWE-798 / CWE-259 · secretos embebidos -------------------------
# Antes: la contraseña de la base y una clave de AWS estaban escritas como literales. (Aquí
# no se copian ni siquiera como ejemplo: un secreto citado en un comentario sigue siendo un
# secreto publicado, y es lo primero que encuentra un escáner.) Un secreto escrito en
# el código viaja a cada clon, a cada fork y a todo el historial de Git: borrar la línea
# después NO lo retira. Ahora se lee del entorno (o de un gestor de secretos); si falta,
# la app lo dice en vez de arrancar con un valor por defecto inseguro.
# Y además hay que ROTAR la credencial que estuvo publicada: es la parte que más se olvida.
DB_PASSWORD = os.environ.get("DB_PASSWORD")  # None si no está configurada: nunca un valor por defecto
# La clave de AWS desaparece del código: en AWS se usan roles de IAM o el proveedor de
# credenciales por defecto del SDK, que nunca pasa por el repositorio.

# Directorio permitido para /read. Configurable para poder probarlo sin tocar /var/data.
DATA_DIR = os.environ.get("DATA_DIR", "/var/data")

# Parámetros de scrypt: una de las combinaciones mínimas de la guía de OWASP
# (Password Storage Cheat Sheet): N=2^17 (128 MiB), r=8, p=1. Las pruebas los bajan
# para ir rápido; en producción NO se bajan.
SCRYPT_N, SCRYPT_R, SCRYPT_P = 2**17, 8, 1
SALT_BYTES = 16


@app.route("/user")
def get_user():
    # --- Fallo 2 · CWE-89 · inyección SQL ---
    # Antes: la entrada se concatenaba a la consulta, así que `' OR '1'='1` cambiaba su
    # ESTRUCTURA. Ahora la consulta lleva un marcador (?) y el valor viaja aparte: el
    # motor lo trata siempre como dato, jamás como parte del SQL. Escapar comillas a mano
    # no es equivalente: depende de acertar con cada carácter especial del dialecto.
    name = request.args.get("name", "")
    conn = sqlite3.connect("app.db")
    try:
        rows = conn.execute("SELECT * FROM users WHERE name = ?", (name,)).fetchall()
    finally:
        conn.close()  # el original dejaba la conexión abierta
    return {"rows": rows}


# Un nombre de host DNS: etiquetas de letras, dígitos y guiones separadas por puntos,
# sin empezar por guion (así una entrada no puede pasar por una opción de `ping`).
_HOST_RE = re.compile(r"^(?=.{1,253}$)(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*$")


def _host_valido(host: str) -> bool:
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return bool(_HOST_RE.match(host))


@app.route("/ping")
def ping():
    # --- Fallo 3 · CWE-78 · inyección de comandos del sistema operativo ---
    # Antes: "ping -c 1 " + host con shell=True. El shell interpreta `;`, `&&`, `$(...)`,
    # así que `127.0.0.1; id` ejecutaba un segundo comando. Dos defensas, y se necesitan las dos:
    #  1) NO pasar por el shell: una lista de argumentos se entrega al programa tal cual,
    #     sin interpretar metacaracteres. Es la defensa estructural.
    #  2) Validar que `host` sea un host (lista permitida, no lista de prohibidos): reduce
    #     la superficie y evita que un valor como `-f` se interprete como opción de ping.
    host = request.args.get("host", "127.0.0.1")
    if not _host_valido(host):
        abort(400)
    resultado = subprocess.run(["ping", "-c", "1", host], capture_output=True, timeout=10, check=False)
    return resultado.stdout


def hash_contrasena(contrasena: str, sal: bytes | None = None) -> str:
    """Devuelve «scrypt$N$r$p$sal_hex$hash_hex». Cada llamada usa una sal nueva."""
    sal = sal if sal is not None else os.urandom(SALT_BYTES)
    # maxmem: por defecto Python limita scrypt a 32 MiB y N=2^17 necesita ~128 MiB.
    derivada = hashlib.scrypt(
        contrasena.encode(), salt=sal, n=SCRYPT_N, r=SCRYPT_R, p=SCRYPT_P,
        maxmem=2**28, dklen=32,
    )
    return f"scrypt${SCRYPT_N}${SCRYPT_R}${SCRYPT_P}${sal.hex()}${derivada.hex()}"


def verificar_contrasena(contrasena: str, almacenado: str) -> bool:
    """Recalcula con los parámetros guardados y compara en tiempo constante."""
    try:
        esquema, n, r, p, sal_hex, hash_hex = almacenado.split("$")
        if esquema != "scrypt":
            return False  # otro algoritmo (p. ej. un hash heredado): no se «acepta» por parecido
        derivada = hashlib.scrypt(
            contrasena.encode(), salt=bytes.fromhex(sal_hex), n=int(n), r=int(r), p=int(p),
            maxmem=2**28, dklen=32,
        )
    except (ValueError, TypeError):
        return False
    # compare_digest evita que el tiempo de respuesta revele cuántos bytes coinciden.
    return hmac.compare_digest(derivada.hex(), hash_hex)


@app.route("/hash")
def hash_password():
    # --- Fallo 4 · CWE-916 (y CWE-327/328) · hash de contraseña débil ---
    # Antes: MD5 sin sal. MD5 es rápido A PROPÓSITO (miles de millones de intentos por segundo
    # en una GPU) y sin sal dos usuarios con la misma contraseña tienen el mismo hash. Una función
    # para contraseñas debe ser LENTA y consumir memoria (scrypt/Argon2id/bcrypt) y llevar sal única.
    # Argon2id es la primera opción de OWASP; scrypt es una alternativa válida disponible en la
    # biblioteca estándar, por eso se usa aquí sin añadir dependencias.
    pwd = request.args.get("pwd", "")
    return {"hash": hash_contrasena(pwd)}


@app.route("/load")
def load_object():
    # --- Fallo 5 · CWE-502 · deserialización de datos no confiables ---
    # Antes: pickle.loads sobre el cuerpo de la petición. Pickle no «lee datos»: ejecuta un
    # programa de reconstrucción, de modo que quien controla los bytes controla el código.
    # No existe una forma segura de deserializar pickle de origen no confiable. La corrección
    # es cambiar de formato: JSON solo describe datos (números, texto, listas, diccionarios).
    try:
        obj = json.loads(request.get_data())
    except (ValueError, UnicodeDecodeError):
        abort(400)
    return {"loaded": str(obj)}


@app.route("/read")
def read_file():
    # --- Fallo 6 · CWE-22 (relativo: CWE-23) · path traversal ---
    # Antes: "/var/data/" + filename. Con `../../etc/passwd` la ruta final sale del directorio.
    # Bloquear la cadena «..» no basta (codificaciones, enlaces simbólicos, mayúsculas...). Lo
    # robusto es RESOLVER la ruta final y comprobar que sigue dentro del directorio permitido.
    filename = request.args.get("file", "notes.txt")
    base = os.path.realpath(DATA_DIR)
    ruta = os.path.realpath(os.path.join(base, filename))
    # commonpath compara por componentes: «/var/data-secreto» NO cuenta como dentro de «/var/data»,
    # error clásico de usar startswith sobre cadenas.
    if os.path.commonpath([base, ruta]) != base:
        abort(403)
    with open(ruta) as fh:
        return fh.read()


# --- Fallo 7 · CWE-95 (padre: CWE-94) · evaluación de código arbitrario ---
# Antes: eval(expr). Cualquier expresión Python se ejecutaba, incluido `__import__('os')...`.
# Ahora se recorre el árbol sintáctico y solo se permiten números y operadores aritméticos
# de una lista cerrada. Lo que no está en la lista se rechaza: no se intenta «limpiar» eval.
_OPERADORES = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.Div: operator.truediv, ast.FloorDiv: operator.floordiv, ast.Mod: operator.mod,
}
_UNARIOS = {ast.UAdd: operator.pos, ast.USub: operator.neg}
_MAX_EXPRESION = 100  # tope de longitud: evita expresiones gigantes que agoten la CPU


def evaluar_aritmetica(expr: str) -> float:
    """Evalúa una expresión aritmética simple. Lanza ValueError ante cualquier otra cosa."""
    if len(expr) > _MAX_EXPRESION:
        raise ValueError("expresión demasiado larga")

    def visitar(nodo):
        if isinstance(nodo, ast.Expression):
            return visitar(nodo.body)
        if isinstance(nodo, ast.Constant) and type(nodo.value) in (int, float):
            return nodo.value
        if isinstance(nodo, ast.BinOp) and type(nodo.op) in _OPERADORES:
            return _OPERADORES[type(nodo.op)](visitar(nodo.left), visitar(nodo.right))
        if isinstance(nodo, ast.UnaryOp) and type(nodo.op) in _UNARIOS:
            return _UNARIOS[type(nodo.op)](visitar(nodo.operand))
        # Llamadas, nombres, atributos, potencias (** permite 9**9**9), etc.: todo fuera.
        raise ValueError("expresión no permitida")

    try:
        return visitar(ast.parse(expr, mode="eval"))
    except (SyntaxError, ZeroDivisionError, RecursionError, MemoryError) as exc:
        # MITRE advierte (ficha de CWE-95) que hasta ast.literal_eval puede agotar memoria o pila con
        # estructuras muy anidadas: además del tope de longitud, esos fallos se tratan como rechazo.
        raise ValueError(str(exc)) from exc


@app.route("/calc")
def calc():
    expr = request.args.get("expr", "1+1")
    try:
        return {"result": evaluar_aritmetica(expr)}
    except ValueError:
        abort(400)


if __name__ == "__main__":
    # --- Fallo 8 · CWE-489 (y CWE-1327) · depuración activa y enlace a todas las interfaces ---
    # Antes: debug=True y host 0.0.0.0. El depurador de Werkzeug permite ejecutar código desde el
    # navegador. CWE-489 describe la DEBILIDAD (dejar activo código de depuración); que de ahí se
    # derive ejecución de código (CWE-94, como lo etiqueta Bandit) es la CONSECUENCIA. Se corrige
    # la causa: debug apagado, y escuchar solo en local salvo que un proxy inverso lo requiera.
    app.run(host="127.0.0.1", debug=False)
