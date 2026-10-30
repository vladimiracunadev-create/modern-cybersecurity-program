#!/usr/bin/env bash
# Ejecuta SAST sobre la app vulnerable. Usa el contenedor oficial de Semgrep
# (no requiere instalar nada) y, si está disponible, también Bandit.
set -euo pipefail
cd "$(dirname "$0")"

echo "== Semgrep (reglas automáticas) =="
if command -v semgrep >/dev/null 2>&1; then
  semgrep --config auto vulnerable_app || true
else
  docker run --rm -v "$(pwd)":/src semgrep/semgrep \
    semgrep --config auto /src/vulnerable_app || true
fi

echo
echo "== Bandit (SAST específico de Python) =="
if command -v bandit >/dev/null 2>&1; then
  bandit -r vulnerable_app || true
else
  echo "(bandit no instalado: 'pip install bandit' para esta parte)"
fi

echo
echo "== Contraste de cada etiqueta CWE con el mapa del laboratorio =="
if command -v bandit >/dev/null 2>&1 && command -v python3 >/dev/null 2>&1; then
  SALIDA="$(mktemp)"
  bandit -r vulnerable_app -f json -o "$SALIDA" >/dev/null 2>&1 || true
  python3 ../../scripts/cwe_kb.py sast "$SALIDA" --mapa cwe-map.json || true
  rm -f "$SALIDA"
else
  echo "(se necesita bandit y python3; hay una salida ya verificada en tests/datos/bandit-1.9.4-app.json:"
  echo " python3 ../../scripts/cwe_kb.py sast tests/datos/bandit-1.9.4-app.json --mapa cwe-map.json)"
fi

echo
echo "Compara los hallazgos con SOLUCION.md. ¿Encontró el SAST las 8? ¿Algún falso positivo? ¿La etiqueta CWE de la herramienta es la correcta?"
