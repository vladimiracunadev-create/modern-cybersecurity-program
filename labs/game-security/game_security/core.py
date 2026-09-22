"""Matemática pequeña y auditable para el target educativo del rango."""

from __future__ import annotations

from dataclasses import dataclass
from math import acos, degrees, sqrt


@dataclass(frozen=True)
class Vec2:
    x: float
    y: float


@dataclass(frozen=True)
class Vec3:
    x: float
    y: float
    z: float

    def __add__(self, other: "Vec3") -> "Vec3":
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vec3") -> "Vec3":
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def scale(self, value: float) -> "Vec3":
        return Vec3(self.x * value, self.y * value, self.z * value)

    def dot(self, other: "Vec3") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self) -> float:
        return sqrt(self.dot(self))

    def normalized(self) -> "Vec3":
        length = self.length()
        if length == 0:
            raise ValueError("un vector cero no tiene dirección")
        return self.scale(1.0 / length)


def angle_degrees(a: Vec3, b: Vec3) -> float:
    """Ángulo robusto entre direcciones; acota el coseno por redondeo."""
    cosine = a.normalized().dot(b.normalized())
    return degrees(acos(max(-1.0, min(1.0, cosine))))


def in_fov(camera_direction: Vec3, target_direction: Vec3, fov_degrees: float) -> bool:
    if not 0 < fov_degrees <= 360:
        raise ValueError("el FOV debe estar en (0, 360]")
    return angle_degrees(camera_direction, target_direction) <= fov_degrees / 2


def predict_intercept(
    shooter: Vec3,
    target: Vec3,
    target_velocity: Vec3,
    projectile_speed: float,
) -> Vec3:
    """Predicción lineal didáctica; no modela gravedad ni aceleración."""
    if projectile_speed <= 0:
        raise ValueError("la velocidad del proyectil debe ser positiva")
    travel_time = (target - shooter).length() / projectile_speed
    return target + target_velocity.scale(travel_time)


def world_to_screen(point: Vec3, view_projection: tuple[tuple[float, ...], ...], width: int, height: int) -> Vec2 | None:
    """Transforma WORLD→CLIP→NDC→SCREEN con una matriz 4x4."""
    if width <= 0 or height <= 0 or len(view_projection) != 4 or any(len(row) != 4 for row in view_projection):
        raise ValueError("se requiere matriz 4x4 y viewport positivo")
    vector = (point.x, point.y, point.z, 1.0)
    clip = tuple(sum(row[i] * vector[i] for i in range(4)) for row in view_projection)
    if clip[3] <= 1e-9:
        return None
    ndc_x, ndc_y = clip[0] / clip[3], clip[1] / clip[3]
    if abs(ndc_x) > 1 or abs(ndc_y) > 1:
        return None
    return Vec2((ndc_x + 1) * width / 2, (1 - ndc_y) * height / 2)
