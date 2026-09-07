#!/usr/bin/env python3
"""Adquiere evidencia pública de Bitcoin testnet sin transmitir transacciones."""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.error
import urllib.request
from pathlib import Path


BASE_URL = "https://blockstream.info/testnet/api"


def endpoint(kind: str, value: str) -> str:
    if not value or any(char.isspace() for char in value):
        raise ValueError("el identificador no puede estar vacío ni contener espacios")
    if kind == "tx":
        return f"{BASE_URL}/tx/{value}"
    return f"{BASE_URL}/address/{value}/txs"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("tx", "address"))
    parser.add_argument("value", help="TXID o dirección exclusivamente de testnet")
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    url = endpoint(args.kind, args.value)
    request = urllib.request.Request(url, headers={"User-Agent": "Nebula-Custody-Lab/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:  # nosec B310
            payload = response.read()
    except urllib.error.URLError as exc:
        parser.error(f"no fue posible consultar testnet: {exc}")

    json.loads(payload)  # impide guardar una página de error como evidencia JSON
    args.out.write_bytes(payload)
    digest = hashlib.sha256(payload).hexdigest()
    print(f"Fuente: {url}")
    print(f"Bytes: {len(payload)}")
    print(f"SHA-256: {digest}")
    print(f"Guardado: {args.out.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
