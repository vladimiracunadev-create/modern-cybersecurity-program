#!/usr/bin/env python3
"""Concilia el dataset sintético de Nebula Custody sin dependencias externas."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from decimal import Decimal
from pathlib import Path


BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
ZERO = Decimal("0")


def rows(name: str, data_dir: Path = DATA) -> list[dict[str, str]]:
    with (data_dir / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def jsonl(name: str, data_dir: Path = DATA) -> list[dict[str, object]]:
    with (data_dir / name).open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def ledger_balances(data_dir: Path = DATA) -> dict[str, Decimal]:
    balances: dict[str, Decimal] = defaultdict(lambda: ZERO)
    for row in rows("ledger.csv", data_dir):
        balances[row["asset"]] += Decimal(row["amount"])
    return dict(balances)


def chain_balances(data_dir: Path = DATA) -> dict[str, Decimal]:
    openings = {
        row["asset"]: Decimal(row["opening_balance"])
        for row in rows("wallets.csv", data_dir)
    }
    balances: dict[str, Decimal] = defaultdict(lambda: ZERO, openings)
    for row in rows("blockchain.csv", data_dir):
        sign = Decimal("1") if row["direction"] == "in" else Decimal("-1")
        balances[row["asset"]] += sign * Decimal(row["amount"])
    return dict(balances)


def findings(data_dir: Path = DATA) -> dict[str, object]:
    ledger = ledger_balances(data_dir)
    chain = chain_balances(data_dir)
    approvals = {row["request_id"] for row in rows("approvals.csv", data_dir)}
    ledger_refs = {row["reference"] for row in rows("ledger.csv", data_dir)}
    withdrawals = rows("withdrawals.csv", data_dir)
    alerts = jsonl("security_alerts.jsonl", data_dir)

    assets = sorted(set(ledger) | set(chain))
    reconciliation = [
        {
            "asset": asset,
            "ledger": ledger.get(asset, ZERO),
            "chain": chain.get(asset, ZERO),
            "difference": ledger.get(asset, ZERO) - chain.get(asset, ZERO),
        }
        for asset in assets
    ]
    missing_approval = [
        row["request_id"]
        for row in withdrawals
        if row["status"] == "executed" and row["request_id"] not in approvals
    ]
    missing_ledger = [
        row["request_id"]
        for row in withdrawals
        if row["status"] == "executed" and row["request_id"] not in ledger_refs
    ]
    critical_open = [
        str(row["event_id"])
        for row in alerts
        if int(row["risk_score"]) >= 90 and row["result"] == "open"
    ]
    return {
        "reconciliation": reconciliation,
        "executed_without_approval": missing_approval,
        "executed_without_ledger": missing_ledger,
        "critical_open_alerts": critical_open,
    }


def serializable(result: dict[str, object]) -> dict[str, object]:
    return json.loads(json.dumps(result, default=str))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DATA)
    parser.add_argument("--json", action="store_true", help="emite JSON reproducible")
    args = parser.parse_args()
    result = findings(args.data_dir)

    if args.json:
        print(json.dumps(serializable(result), indent=2, ensure_ascii=False))
    else:
        print("CONCILIACIÓN LEDGER VS BLOCKCHAIN")
        for item in result["reconciliation"]:
            print(
                f"- {item['asset']}: ledger={item['ledger']:.8f} "
                f"blockchain={item['chain']:.8f} diferencia={item['difference']:.8f}"
            )
        print("Retiros ejecutados sin aprobación:", ", ".join(result["executed_without_approval"]) or "ninguno")
        print("Retiros ejecutados sin asiento:", ", ".join(result["executed_without_ledger"]) or "ninguno")
        print("Alertas críticas abiertas:", ", ".join(result["critical_open_alerts"]) or "ninguna")

    mismatch = any(item["difference"] != ZERO for item in result["reconciliation"])
    control_failure = any(
        result[key]
        for key in ("executed_without_approval", "executed_without_ledger", "critical_open_alerts")
    )
    print("RESULTADO: ALERTA" if mismatch or control_failure else "RESULTADO: CONCILIADO")
    return 2 if mismatch or control_failure else 0


if __name__ == "__main__":
    raise SystemExit(main())
