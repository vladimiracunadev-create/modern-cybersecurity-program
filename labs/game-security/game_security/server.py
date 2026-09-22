"""Simulación autoritativa local con un modo vulnerable deliberado."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from .core import Vec3


class Mode(str, Enum):
    NORMAL = "NORMAL"
    VULNERABLE = "VULNERABLE"
    SECURE = "SECURE"
    DETECTION = "DETECTION"


@dataclass
class PlayerState:
    position: Vec3 = field(default_factory=lambda: Vec3(0, 0, 0))
    velocity: Vec3 = field(default_factory=lambda: Vec3(0, 0, 0))
    health: int = 100
    ammo: int = 30
    score: int = 0
    last_shot_ms: int = -10_000


@dataclass(frozen=True)
class PlayerCommand:
    timestamp_ms: int
    sequence: int
    position: Vec3 | None = None
    claimed_health: int | None = None
    claimed_ammo: int | None = None
    fire: bool = False


@dataclass(frozen=True)
class Decision:
    accepted: bool
    reasons: tuple[str, ...]
    event: dict


class GameServer:
    """Solo acepta estructuras del rango; no lee procesos ni tráfico externo."""

    def __init__(self, mode: Mode = Mode.SECURE, max_speed: float = 8.0, fire_interval_ms: int = 120):
        self.mode = mode
        self.max_speed = max_speed
        self.fire_interval_ms = fire_interval_ms
        self.state = PlayerState()
        self.last_sequence = -1

    def apply(self, command: PlayerCommand) -> Decision:
        reasons: list[str] = []
        previous = self.state.position
        if command.sequence <= self.last_sequence:
            reasons.append("sequence_replay")
        if command.position is not None:
            elapsed = max((command.timestamp_ms - max(self.state.last_shot_ms, 0)) / 1000, 0.016)
            speed = (command.position - previous).length() / elapsed
            if speed > self.max_speed:
                reasons.append("impossible_speed")
        if command.fire and command.timestamp_ms - self.state.last_shot_ms < self.fire_interval_ms:
            reasons.append("fire_rate_violation")
        if command.fire and self.state.ammo <= 0:
            reasons.append("no_ammo")

        vulnerable = self.mode == Mode.VULNERABLE
        accepted = vulnerable or not reasons
        if accepted:
            self.last_sequence = max(self.last_sequence, command.sequence)
            if command.position is not None:
                self.state.position = command.position
            if vulnerable and command.claimed_health is not None:
                self.state.health = command.claimed_health
            if vulnerable and command.claimed_ammo is not None:
                self.state.ammo = command.claimed_ammo
            if command.fire:
                self.state.last_shot_ms = command.timestamp_ms
                self.state.ammo = max(0, self.state.ammo - 1)

        event = {
            "event_id": f"cmd-{command.sequence}",
            "timestamp_ms": command.timestamp_ms,
            "sequence": command.sequence,
            "position": [self.state.position.x, self.state.position.y, self.state.position.z],
            "ammo": self.state.ammo,
            "health": self.state.health,
            "server_decision": "accept" if accepted else "reject",
            "signals": reasons,
        }
        return Decision(accepted, tuple(reasons), event)
