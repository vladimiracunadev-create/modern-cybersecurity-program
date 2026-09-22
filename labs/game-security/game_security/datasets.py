"""Generador determinista de telemetría sintética, sin datos personales."""

from __future__ import annotations

import csv
import random
from pathlib import Path


PROFILES = {
    "normal": (210, 5, 1.2),
    "expert-synthetic": (145, 3, 2.0),
    "snap-aim": (42, 38, 1.0),
    "smooth-aim": (85, 8, 1.0),
    "tracking": (95, 4, 1.0),
    "trigger": (28, 2, 1.0),
    "speed-anomaly": (210, 5, 14.0),
    "fire-rate-anomaly": (55, 4, 1.0),
    "high-latency": (280, 7, 1.0),
    "jitter": (210, 10, 1.0),
    "packet-loss": (230, 8, 1.0),
}


def generate(profile: str, rows: int = 200, seed: int = 190341) -> list[dict]:
    if profile not in PROFILES or rows <= 0:
        raise ValueError("perfil desconocido o filas no positivas")
    rng = random.Random(seed)
    reaction, aim_delta, speed = PROFILES[profile]
    result = []
    for index in range(rows):
        shot_interval = 55 if profile == "fire-rate-anomaly" else 160 + rng.randint(-20, 25)
        result.append({
            "event_id": f"{profile}-{index:04d}",
            "profile": profile,
            "reaction_ms": max(1, reaction + rng.randint(-15, 15)),
            "aim_delta_degrees": max(0.0, aim_delta + rng.uniform(-1.5, 1.5)),
            "speed": max(0.0, speed + rng.uniform(-0.2, 0.2)),
            "shot_interval_ms": shot_interval,
            "latency_ms": 260 + rng.randint(-40, 40) if profile == "high-latency" else 45 + rng.randint(-8, 8),
            "packet_lost": profile == "packet-loss" and index % 7 == 0,
        })
    return result


def write_csv(path: Path, profile: str, rows: int = 200, seed: int = 190341) -> None:
    data = generate(profile, rows, seed)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
