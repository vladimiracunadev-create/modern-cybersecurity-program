#!/usr/bin/env python3
"""Escaneo didactico de secretos de IA/cloud en texto y evaluacion local de exposicion de Ollama.

NUNCA valida una credencial contra un proveedor: reconocer el formato de una clave no
exige usarla, y usarla seria acceso no autorizado. La salida siempre oculta el valor.
No sustituye a gitleaks (que ya corre en el CI del programa): sirve para entender por
que una regla acierta o falla y para probar reglas nuevas con fixtures falsos.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Prefijos de formato documentados por los proveedores/proyectos de escaneo. Son
# heuristicas: pueden dar falsos positivos y las claves cambian de formato con el tiempo.
REGLAS = {
    "aws-access-key-id": re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    "google-api-key": re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    "github-pat-clasico": re.compile(r"\bghp_[A-Za-z0-9]{36}\b"),
    "huggingface-token": re.compile(r"\bhf_[A-Za-z0-9]{34}\b"),
    "clave-llm-prefijo-sk": re.compile(r"\bsk-[A-Za-z0-9_\-]{32,}\b"),
}


def ocultar(valor: str) -> str:
    return valor[:4] + "…" + f"[{len(valor)} car.]"


def escanear_texto(texto: str, origen: str = "<texto>") -> list[dict]:
    hallazgos = []
    for n, linea in enumerate(texto.splitlines(), 1):
        for regla, rx in REGLAS.items():
            for m in rx.finditer(linea):
                hallazgos.append({"regla": regla, "origen": origen, "linea": n,
                                  "valor_oculto": ocultar(m.group(0))})
    return hallazgos


def escanear_ruta(ruta: Path) -> list[dict]:
    salida = []
    archivos = [ruta] if ruta.is_file() else sorted(p for p in ruta.rglob("*") if p.is_file())
    for p in archivos:
        try:
            salida += escanear_texto(p.read_text(encoding="utf-8"), str(p))
        except (UnicodeDecodeError, OSError):
            continue
    return salida


def evaluar_bind_ollama(ollama_host: str | None, detras_de_proxy_autenticado: bool = False) -> dict:
    """Evalua el valor de OLLAMA_HOST sin tocar la red.

    Por defecto Ollama escucha en 127.0.0.1:11434 (documentacion oficial). Las direcciones
    0.0.0.0 o '::' lo exponen en todas las interfaces; la FAQ oficial no describe autenticacion
    integrada, asi que la exposicion exige un proxy con autenticacion delante.
    """
    host = (ollama_host or "127.0.0.1:11434").strip()
    nombre = host.rsplit(":", 1)[0].strip("[]") if ":" in host and not host.startswith("[") else host
    if host.startswith("["):
        nombre = host[1:].split("]")[0]
    local = nombre in ("127.0.0.1", "localhost", "::1")
    # nosec B104 - se COMPARA el texto de configuracion para clasificar riesgo; no se abre ningun socket
    todas = nombre in ("0.0.0.0", "::", "")  # nosec B104
    if local:
        riesgo, motivo = "bajo", "solo escucha en loopback"
    elif detras_de_proxy_autenticado:
        riesgo, motivo = "medio", "interfaz accesible, pero con proxy autenticado delante (verifica que no haya bypass directo)"
    elif todas:
        riesgo, motivo = "alto", "escucha en todas las interfaces sin autenticacion propia"
    else:
        riesgo, motivo = "alto", "escucha en una interfaz de red sin autenticacion propia"
    return {"host": host, "riesgo": riesgo, "motivo": motivo}


def main(argv=None) -> int:
    args = (argv if argv is not None else sys.argv)[1:]
    if not args:
        print("uso: python secret_scan.py <archivo-o-carpeta>")
        return 2
    h = escanear_ruta(Path(args[0]))
    for x in h:
        print(f"{x['origen']}:{x['linea']}: {x['regla']} {x['valor_oculto']}")
    return 1 if h else 0


if __name__ == "__main__":
    sys.exit(main())
