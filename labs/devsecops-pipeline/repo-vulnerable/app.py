"""Aplicación de laboratorio DELIBERADAMENTE INSEGURA.

No la despliegues. No la ejecutes fuera de un entorno aislado. Su única
finalidad es servir de objetivo a las herramientas de análisis del laboratorio
`devsecops-pipeline`.

Cada bloque marcado con [SAST-n] contiene un patrón inseguro reconocible. El
ejercicio NO es encontrarlos leyendo este archivo: es comprobar cuáles detecta
cada herramienta, cuáles se le escapan y por qué.
"""

import hashlib
import os
import pickle
import random
import sqlite3
import subprocess

import requests
import yaml
from flask import Flask, request

from config import AWS_ACCESS_KEY_ID, DB_PASSWORD, SECRET_KEY

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


# [SAST-1] Inyección SQL por concatenación de cadenas.
@app.route("/usuario")
def obtener_usuario():
    nombre = request.args.get("nombre", "")
    conexion = sqlite3.connect("lab.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre = '" + nombre + "'")
    return str(cursor.fetchall())


# [SAST-2] Inyección de comandos: shell=True sobre entrada del usuario.
@app.route("/ping")
def ping():
    destino = request.args.get("host", "127.0.0.1")
    salida = subprocess.check_output("ping -c 1 " + destino, shell=True)
    return salida.decode("utf-8", errors="replace")


# [SAST-3] Ejecución de código arbitrario con eval().
@app.route("/calcular")
def calcular():
    expresion = request.args.get("expr", "1+1")
    return str(eval(expresion))


# [SAST-4] Deserialización insegura de datos controlados por el usuario.
@app.route("/restaurar", methods=["POST"])
def restaurar_sesion():
    return str(pickle.loads(request.get_data()))


# [SAST-5] Carga de YAML con el Loader inseguro (permite construir objetos).
@app.route("/config", methods=["POST"])
def cargar_config():
    return str(yaml.load(request.get_data()))


# [SAST-6] Hash criptográficamente roto para almacenar contraseñas.
def guardar_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# [SAST-7] Generador pseudoaleatorio no criptográfico para un token de sesión.
def nuevo_token():
    return "".join(random.choice("0123456789abcdef") for _ in range(32))


# [SAST-8] Verificación de certificados TLS desactivada.
def consultar_api_interna(ruta):
    return requests.get("https://api.interno.lab" + ruta, verify=False, timeout=10)


# [SAST-9] Path traversal: ruta construida con entrada sin normalizar.
@app.route("/descargar")
def descargar():
    nombre = request.args.get("archivo", "notas.txt")
    with open(os.path.join("/var/datos", nombre), "rb") as fh:
        return fh.read()


# [SAST-10] Secreto usado directamente desde el código fuente.
def cabeceras_de_autenticacion():
    return {"X-Api-Key": AWS_ACCESS_KEY_ID, "X-Db-Pass": DB_PASSWORD}


if __name__ == "__main__":
    # [SAST-11] Servidor de desarrollo, en modo debug y escuchando en todas las
    # interfaces: consola interactiva de Python expuesta a la red.
    app.run(host="0.0.0.0", port=8080, debug=True)
