#!/usr/bin/env python3
"""Detección de abuso de identidades de aplicación en la nube (laboratorio sintético).

Inspirado en el patrón público del incidente ConnectWise Cloud Backup (octubre de 2026,
informe de Huntress): una credencial de una aplicación de proveedor, ya autorizada en muchos
inquilinos de Microsoft 365, se usa desde infraestructura ajena. Todo aquí es **ficticio**:
inquilinos, identificadores de aplicación y direcciones (rangos de documentación RFC 5737).

No es una réplica del ataque real ni de los registros de Microsoft: el esquema de eventos es
propio y mínimo. Las reglas expresan ideas defendibles:

R1  un principal de servicio **se asigna a sí mismo** un rol de directorio;
R2  se **añade una credencial** a una aplicación por un actor que no es su propietario;
R3  inicio de sesión de un principal de servicio desde una IP **fuera de los rangos conocidos del proveedor**;
R4  **pulverización de contraseñas**: muchas cuentas distintas fallan desde un mismo origen en poco tiempo.

Ninguna señal prueba por sí sola una intrusión (hay cambios legítimos); cada alerta lista su motivo
y el analista decide. Solo biblioteca estándar.
"""
from __future__ import annotations

import ipaddress
import random
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

APP_PROVEEDOR = "11111111-aaaa-4aaa-8aaa-000000000001"   # ficticio
APP_GESTION = "11111111-aaaa-4aaa-8aaa-000000000002"     # ficticio
RANGOS_PROVEEDOR = [ipaddress.ip_network("203.0.113.0/24")]  # «infraestructura habitual» del proveedor (ficticia)
ORIGEN_HOSTIL = "198.51.100.77"                              # ficticio
INICIO = datetime(2026, 10, 13, 0, 0, tzinfo=timezone.utc)
# propietarios registrados (inventario del cliente, ficticio): quién puede añadir credenciales a cada app
PROPIETARIOS = {APP_GESTION: {"admin.ti@tenant-03"}}


@dataclass
class Evento:
    t: datetime
    tipo: str            # signin_sp | signin_user | role_add | cred_add
    inquilino: str
    actor: str           # app id o usuario
    ip: str = ""
    destino: str = ""    # app/usuario afectado, o rol
    resultado: str = "ok"
    etiqueta: str = "benigno"   # verdad de terreno para medir; el detector no la lee


@dataclass
class Alerta:
    regla: str
    t: datetime
    inquilino: str
    motivo: str
    eventos: list[Evento] = field(default_factory=list)


def generar(semilla: int = 7, inquilinos: int = 12) -> list[Evento]:
    """Línea base de 3 días + un episodio malicioso en 2 inquilinos + un cambio legítimo parecido."""
    rng = random.Random(semilla)
    ev: list[Evento] = []
    ids = [f"tenant-{i:02d}" for i in range(inquilinos)]
    for dia in range(3):
        for t_id in ids:
            for _ in range(rng.randint(3, 6)):
                t = INICIO + timedelta(days=dia, minutes=rng.randint(0, 1439))
                ip = str(rng.choice(list(RANGOS_PROVEEDOR[0].hosts())[:40]))
                ev.append(Evento(t, "signin_sp", t_id, APP_PROVEEDOR, ip))
            for _ in range(rng.randint(1, 3)):
                t = INICIO + timedelta(days=dia, hours=rng.randint(7, 18), minutes=rng.randint(0, 59))
                ev.append(Evento(t, "signin_user", t_id, f"usuario{rng.randint(1, 30)}", f"192.0.2.{rng.randint(1, 50)}"))
    # cambio legítimo: un administrador humano añade una credencial a su propia app de gestión
    ev.append(Evento(INICIO + timedelta(days=1, hours=10), "cred_add", ids[3], "admin.ti@tenant-03", "192.0.2.10",
                     APP_GESTION, etiqueta="benigno"))
    # episodio malicioso (T0 = día 2, 01:58): pulverización, uso del principal desde fuera y escalada
    t0 = INICIO + timedelta(days=2, hours=1, minutes=58)
    for k in range(18):
        ev.append(Evento(t0 - timedelta(hours=8) + timedelta(seconds=20 * k), "signin_user", ids[0], f"cuenta{k:02d}",
                         ORIGEN_HOSTIL, resultado="fallo", etiqueta="malicioso"))
    for t_id in (ids[5], ids[6]):
        ev.append(Evento(t0, "signin_sp", t_id, APP_PROVEEDOR, ORIGEN_HOSTIL, etiqueta="malicioso"))
        ev.append(Evento(t0 + timedelta(minutes=1), "role_add", t_id, APP_PROVEEDOR, ORIGEN_HOSTIL,
                         "Exchange Administrator", etiqueta="malicioso"))
    ev.append(Evento(t0 + timedelta(minutes=2), "cred_add", ids[5], APP_PROVEEDOR, ORIGEN_HOSTIL, APP_GESTION,
                     etiqueta="malicioso"))
    ev.sort(key=lambda e: e.t)
    return ev


def _fuera_de_rangos(ip: str) -> bool:
    try:
        a = ipaddress.ip_address(ip)
    except ValueError:
        return True
    return not any(a in r for r in RANGOS_PROVEEDOR)


def _es_app(actor: str) -> bool:
    """En este esquema ficticio las aplicaciones se identifican con un GUID (4 guiones); las personas, con correo."""
    return actor.count("-") == 4 and "@" not in actor


def detectar(eventos: list[Evento], umbral_spray: int = 8, ventana_spray: timedelta = timedelta(hours=1),
             propietarios: dict[str, set[str]] | None = None) -> list[Alerta]:
    propietarios = PROPIETARIOS if propietarios is None else propietarios
    alertas: list[Alerta] = []
    for e in eventos:
        if e.tipo == "role_add" and _es_app(e.actor):
            alertas.append(Alerta("R1", e.t, e.inquilino, f"la app {e.actor} se asigna el rol «{e.destino}»", [e]))
        if e.tipo == "cred_add" and e.actor not in propietarios.get(e.destino, set()):
            alertas.append(Alerta("R2", e.t, e.inquilino,
                                  f"{e.actor} añade una credencial a {e.destino} sin figurar como propietario", [e]))
        if e.tipo == "signin_sp" and _fuera_de_rangos(e.ip):
            alertas.append(Alerta("R3", e.t, e.inquilino, f"principal de servicio {e.actor} desde {e.ip}, fuera de rangos conocidos", [e]))
    # R4: ventana deslizante por origen
    por_origen: dict[str, list[Evento]] = defaultdict(list)
    for e in eventos:
        if e.tipo == "signin_user" and e.resultado == "fallo":
            por_origen[e.ip].append(e)
    for ip, lista in por_origen.items():
        lista.sort(key=lambda x: x.t)
        j = 0
        for i, e in enumerate(lista):
            while lista[j].t < e.t - ventana_spray:
                j += 1
            cuentas = {x.actor for x in lista[j:i + 1]}
            if len(cuentas) >= umbral_spray:
                alertas.append(Alerta("R4", e.t, e.inquilino, f"{len(cuentas)} cuentas distintas fallan desde {ip} en {ventana_spray}", lista[j:i + 1]))
                break
    alertas.sort(key=lambda a: a.t)
    return alertas


def medir(eventos: list[Evento], alertas: list[Alerta]) -> dict:
    """Precisión y recall **por evento** (un evento malicioso cuenta como detectado si lo cubre una alerta)."""
    marcados = {id(x) for a in alertas for x in a.eventos}
    maliciosos = [e for e in eventos if e.etiqueta == "malicioso" and e.tipo != "signin_user"]
    # los fallos de pulverización se miden como un único episodio (R4)
    spray = [e for e in eventos if e.etiqueta == "malicioso" and e.tipo == "signin_user"]
    tp = sum(1 for e in maliciosos if id(e) in marcados)
    fp = sum(1 for a in alertas for x in a.eventos if x.etiqueta == "benigno")
    return {
        "eventos": len(eventos),
        "alertas": len(alertas),
        "maliciosos_no_spray": len(maliciosos),
        "detectados_no_spray": tp,
        "spray_detectado": any(a.regla == "R4" for a in alertas) if spray else None,
        "falsos_positivos": fp,
    }
