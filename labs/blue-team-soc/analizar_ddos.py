"""Resume el dataset sintético DDoS sin generar tráfico de red."""

from __future__ import annotations

import csv
import statistics
from collections import defaultdict
from pathlib import Path


DATASET = Path(__file__).parent / "datos" / "ddos-telemetria.csv"
FIELDS = ("src_count", "pps", "bps", "http_rps", "http_429", "http_5xx", "latency_ms", "availability_pct")


def load_rows() -> list[dict[str, str]]:
    with DATASET.open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def main() -> None:
    rows = load_rows()
    by_phase: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_phase[row["phase"]].append(row)

    print("phase,metric,median")
    for phase, phase_rows in by_phase.items():
        for field in FIELDS:
            median = statistics.median(float(row[field]) for row in phase_rows)
            print(f"{phase},{field},{median:.2f}")

    baseline_pps = statistics.median(float(row["pps"]) for row in by_phase["baseline"])
    peak = max(rows, key=lambda row: float(row["pps"]))
    ratio = float(peak["pps"]) / baseline_pps
    print(f"peak={peak['timestamp']} pps_ratio_vs_baseline={ratio:.1f}x")
    print("verdict=investigate; volume alone does not prove DDoS")


if __name__ == "__main__":
    main()

