"""Detectores explicables: señal, umbral y alternativas legítimas."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Alert:
    rule: str
    observed: float
    threshold: float
    confidence: str
    evidence: str
    legitimate_explanations: tuple[str, ...]


class DetectionEngine:
    def __init__(self, max_speed: float = 8.0, min_fire_interval_ms: float = 120.0, snap_degrees: float = 35.0):
        self.max_speed = max_speed
        self.min_fire_interval_ms = min_fire_interval_ms
        self.snap_degrees = snap_degrees

    def evaluate(self, sample: dict) -> list[Alert]:
        alerts: list[Alert] = []
        if sample.get("speed", 0) > self.max_speed:
            alerts.append(Alert("impossible_speed", sample["speed"], self.max_speed, "high", "speed excede la invariante del simulador", ("teleport autorizado", "delta temporal corrupto")))
        if 0 < sample.get("shot_interval_ms", 10_000) < self.min_fire_interval_ms:
            alerts.append(Alert("fire_rate", sample["shot_interval_ms"], self.min_fire_interval_ms, "high", "intervalo menor al cooldown del arma", ("reloj desincronizado", "arma mal catalogada")))
        if sample.get("aim_delta_degrees", 0) >= self.snap_degrees and sample.get("reaction_ms", 10_000) < 100:
            alerts.append(Alert("snap_aim_candidate", sample["aim_delta_degrees"], self.snap_degrees, "medium", "giro amplio y disparo sub-100 ms correlacionados", ("jugador experto", "alta sensibilidad", "accesibilidad")))
        return alerts
