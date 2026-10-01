#!/usr/bin/env python3
"""Analiza el caso sintético LV-001 sin red, claves ni transacciones reales."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DEFAULT_CASE = ROOT / "data" / "caso.json"


def finding(identifier: str, title: str, classification: str, evidence: list[str], limit: str) -> dict:
    return {
        "id": identifier,
        "title": title,
        "classification": classification,
        "evidence": evidence,
        "limit": limit,
    }


def analyze(case: dict) -> list[dict]:
    official = case["official_reference"]
    events = case["timeline"]
    by_type: dict[str, list[dict]] = {}
    for event in events:
        by_type.setdefault(event["type"], []).append(event)

    results: list[dict] = []
    page = by_type["airdrop_page"][0]
    visit = by_type["search_result_visit"][0]
    if page["advertised_asset_id"] != official["asset_id"]:
        results.append(finding(
            "F-01", "El símbolo coincide, pero el identificador del activo no",
            "fake-token", [page["event_id"]],
            "La discrepancia prueba que no es el activo de referencia; no atribuye quién lo creó.",
        ))
    if visit["domain"] != official["project_domain"] and not visit["linked_from_official_domain"]:
        results.append(finding(
            "F-02", "Dominio no corroborado usado como landing del lanzamiento",
            "fake-website", [visit["event_id"], page["event_id"]],
            "TLS cifra el canal; no autentica la relación comercial con el proyecto.",
        ))

    fake_accounts = [e for e in by_type["social_post"] if not e["account_matches_official"]]
    if fake_accounts:
        results.append(finding(
            "F-03", "Cuenta imitadora dirige al dominio no corroborado",
            "impersonation", [fake_accounts[0]["event_id"]],
            "El nombre visible no basta para identificar al operador de la cuenta.",
        ))

    anomaly = by_type["account_session_anomaly"][0]
    official_post = next(e for e in by_type["social_post"] if e["account_matches_official"])
    results.append(finding(
        "F-04", "La cuenta auténtica publicó durante una sesión anómala",
        "suspected-account-takeover", [anomaly["event_id"], official_post["event_id"]],
        "La correlación sostiene compromiso probable, no identifica a la persona detrás de la sesión.",
    ))

    video = by_type["viral_video"][0]
    results.append(finding(
        "F-05", "Autoridad aparente, urgencia y recompensa gratuita forman el pretexto",
        "fake-airdrop/fake-influencer/social-engineering/phishing",
        [video["event_id"], page["event_id"]],
        "La popularidad o apariencia del contenido no prueba autenticidad ni intención del creador.",
    ))
    if page["asks_for_seed_phrase"]:
        results.append(finding(
            "F-06", "La landing solicita un secreto que permite controlar la wallet",
            "seed-phrase-theft", [page["event_id"]],
            "El artefacto prueba la solicitud; no prueba que la víctima haya entregado la frase.",
        ))

    connection = by_type["wallet_connection"][0]
    request = by_type["transaction_request"][0]
    approval = request["decoded_actions"][0]
    results.append(finding(
        "F-07", "Conectar no cambió estado; la autorización firmada sí creó riesgo",
        "malicious-contract-authorization", [connection["event_id"], request["event_id"]],
        "La semántica exacta depende de la red y del programa/contrato; hay que decodificarla.",
    ))
    transfer = by_type["asset_transfer"][0]
    if approval["spender"] == transfer["spender"]:
        results.append(finding(
            "F-08", "El mismo spender autorizado ejecutó el gasto delegado posterior",
            "wallet-drainer", [request["event_id"], transfer["event_id"]],
            "La cadena muestra autorización y movimiento; la identidad humana requiere otras fuentes.",
        ))

    clipboard = by_type["clipboard_replacement"][0]
    results.append(finding(
        "F-09", "Un proceso sustituyó una dirección en el portapapeles",
        "clipboard-attack", [clipboard["event_id"]],
        "Es una ruta de compromiso de endpoint distinta del approval; no deben fusionarse sin evidencia.",
    ))

    liquidity = case["liquidity_case"]
    if not liquidity["lock_verified"] and float(liquidity["liquidity_after"]) < float(liquidity["liquidity_before"]) * 0.05:
        results.append(finding(
            "F-10", "Retiro de liquidez contradice la afirmación de bloqueo",
            "rug-pull-scenario", [liquidity["withdrawal_event_id"]],
            "Es un segundo caso: activo auténtico y drainer no son requisitos de un rug pull.",
        ))
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", nargs="?", type=Path, default=DEFAULT_CASE)
    parser.add_argument("--json", action="store_true", help="emite resultados JSON")
    args = parser.parse_args()
    case = json.loads(args.case.read_text(encoding="utf-8"))
    results = analyze(case)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        print(f"CASO: {case['case_id']} — {case['scenario']}")
        for item in results:
            print(f"{item['id']} [{item['classification']}]: {item['title']}")
            print(f"  evidencia={','.join(item['evidence'])}")
            print(f"  límite={item['limit']}")
        print(f"RESULTADO: {len(results)} hallazgos razonados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
