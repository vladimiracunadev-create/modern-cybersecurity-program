#!/usr/bin/env python3
"""Laboratorio defensivo de LLMjacking: eventos sinteticos, deteccion explicable y controles.

Todo es local y determinista: no abre sockets, no llama a ningun proveedor, no usa
claves reales. Los eventos, identidades, IP (rangos de documentacion RFC 5737),
modelos y precios son FICTICIOS. Sirve para razonar sobre deteccion y controles,
no para estimar el rendimiento que tendria un detector en produccion.

Uso:
    python llmjacking_lab.py run --seed 7 --out salida/
    python llmjacking_lab.py robustez --seeds 5
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path

# --------------------------------------------------------------------------- #
# Constantes del mundo sintetico
# --------------------------------------------------------------------------- #

T0 = int(dt.datetime(2026, 1, 5, tzinfo=dt.timezone.utc).timestamp())  # lunes 00:00 UTC
DIA = 86_400
VENTANA = 600  # segundos: unidad de analisis del detector (10 min)
DIAS_BASE = 14  # dias 0..13 = linea base; 14 y 15 = evaluacion

# USD por 1000 tokens (entrada, salida). FICTICIOS. local-7b es costo imputado
# de computo propio (GPU/energia), no una factura de proveedor.
PRECIOS = {
    "m-small": (0.0005, 0.0015),
    "m-medium": (0.003, 0.015),
    "m-large": (0.015, 0.075),
    "local-7b": (0.002, 0.004),
}

ACCIONES_USO = {"InvokeModel", "ollama.generate"}
ACCIONES_PERMISOS = {"iam.AttachPolicy", "iam.PutPolicy", "service.EnableModel"}

# Perfil de linea base: (tipo, modelos permitidos, solicitudes/hora laboral, IP de origen)
IDENTIDADES = {
    "svc-chatbot": ("service", ["m-small", "m-medium"], 40, ["10.20.1.11", "10.20.1.12"]),
    "svc-summarizer": ("service", ["m-small"], 15, ["10.20.2.21"]),
    "svc-batch-marketing": ("service", ["m-small"], 3, ["10.20.3.31"]),
    "svc-ollama-internal": ("service", ["local-7b"], 6, ["10.20.4.41"]),
    "alice": ("user", ["m-medium"], 5, ["203.0.113.10"]),
    "bob": ("user", ["m-medium", "m-small"], 5, ["203.0.113.11"]),
}

# Pesos de las senales (puntos). La alerta exige suma >= UMBRAL_PUNTOS y al menos
# MIN_SENALES senales distintas: ninguna senal aislada basta.
PESOS = {
    "costo_z": 2,
    "tasa_z": 1,
    "identidad_nueva": 2,
    "modelo_no_autorizado": 2,
    "fuera_de_horario": 1,
    "cambio_de_permisos": 2,
    "barrido_minimo": 3,
    "origen_nuevo": 1,
    "clave_expuesta": 1,
}
UMBRAL_PUNTOS = 4
MIN_SENALES = 2
UMBRAL_Z = 6.0  # desviaciones robustas
UMBRAL_BARRIDO = 20  # solicitudes con max_tokens<=1 en una ventana
MIN_SOLICITUDES_CONTEXTO = 5

AVISO = (
    "Datos y costos FICTICIOS generados de forma determinista. Los resultados validan la "
    "logica del detector, no su rendimiento en produccion."
)


# --------------------------------------------------------------------------- #
# Generacion de eventos
# --------------------------------------------------------------------------- #

def costo(modelo: str, tok_in: int, tok_out: int) -> float:
    p_in, p_out = PRECIOS[modelo]
    return round(tok_in / 1000 * p_in + tok_out / 1000 * p_out, 6)


def _evento(ts, identidad, accion, modelo, tok_in, tok_out, max_tokens, ip, *,
            endpoint="api-sim", status=200, etiqueta="benigno", escenario="S1-normal",
            incidente=None, clave="k1"):
    en_uso = accion in ACCIONES_USO
    facturable = en_uso and status == 200
    return {
        "ts": int(ts),
        "identity": identidad,
        "key_id": clave,
        "action": accion,
        "endpoint": endpoint,
        "model": modelo,
        "input_tokens": tok_in,
        "output_tokens": tok_out,
        "max_tokens": max_tokens,
        "source_ip": ip,
        "status": status,
        "cost_usd": costo(modelo, tok_in, tok_out) if facturable and modelo in PRECIOS else 0.0,
        "label": etiqueta,
        "scenario": escenario,
        "incident": incidente,
    }


def _trafico_normal(rng, ident, dia_ini, dia_fin, multiplicador=1.0, horas=None, modelos=None,
                    escenario="S1-normal", clave="k1", etiqueta="benigno"):
    tipo, permitidos, tasa, ips = IDENTIDADES[ident]
    endpoint = "ollama-sim" if ident == "svc-ollama-internal" else "api-sim"
    accion = "ollama.generate" if endpoint == "ollama-sim" else "InvokeModel"
    out = []
    for dia in range(dia_ini, dia_fin):
        if dt.datetime.fromtimestamp(T0 + dia * DIA, dt.timezone.utc).weekday() >= 5:
            continue
        for hora in (horas if horas is not None else range(8, 18)):
            media = tasa * multiplicador
            n = max(0, round(rng.gauss(media, math.sqrt(media))))
            for _ in range(n):
                ts = T0 + dia * DIA + hora * 3600 + rng.randrange(3600)
                modelo = rng.choice(modelos or permitidos)
                tok_in = max(1, int(rng.gauss(600, 200)))
                tok_out = max(1, int(rng.gauss(250, 100)))
                out.append(_evento(ts, ident, accion, modelo, tok_in, tok_out, 1024,
                                   rng.choice(ips), endpoint=endpoint, escenario=escenario,
                                   clave=clave, etiqueta=etiqueta))
    return out


def generar(seed: int = 7) -> dict:
    """Devuelve {'eventos': [...], 'ventanas_aprobadas': [...], 'linea_base_dias': 14}."""
    rng = random.Random(seed)  # nosec B311 - datos de simulacion, no criptografia
    ev: list[dict] = []

    # S1: consumo normal, linea base + dias de evaluacion.
    for ident in IDENTIDADES:
        ev += _trafico_normal(rng, ident, 0, DIAS_BASE + 2)

    d14, d15 = T0 + 14 * DIA, T0 + 15 * DIA
    atacante = "198.51.100.23"

    # S8: rafaga LEGITIMA de alta demanda, con registro de cambio aprobado.
    inicio, fin = d14 + 9 * 3600, d14 + 12 * 3600
    # Se anade trafico extra (7x) sobre el normal: el total ronda 8x.
    ev += _trafico_normal(rng, "svc-summarizer", 14, 15, multiplicador=7.0, horas=range(9, 12),
                          escenario="S8-rafaga-legitima")
    aprobadas = [{
        "id": "CHG-1042", "identity": "svc-summarizer", "models": ["m-small"],
        "start": inicio, "end": fin,
        "motivo": "Resumen masivo de tickets historicos aprobado por el responsable del servicio",
    }]

    # S2: clave de svc-chatbot expuesta en un repositorio (evento de contexto, no uso).
    ev.append(_evento(d14 + 10 * 3600, "svc-chatbot", "secret.exposed", "m-small", 0, 0, 0,
                      "203.0.113.50", etiqueta="contexto", escenario="S2-clave-expuesta",
                      incidente="INC-A", clave="k1"))

    # S4: validacion minima de credenciales (max_tokens=1, varios modelos, 20 min).
    for i in range(120):
        ts = d14 + 13 * 3600 + i * 10
        modelo = ["m-small", "m-medium", "m-large"][i % 3]
        ev.append(_evento(ts, "svc-chatbot", "InvokeModel", modelo, 5, 1, 1, atacante,
                          etiqueta="malicioso", escenario="S4-validacion-minima", incidente="INC-A"))
    for k in range(2):
        ev.append(_evento(d14 + 13 * 3600 + 300 + k * 60, "svc-chatbot",
                          "GetModelInvocationLoggingConfiguration", "m-small", 0, 0, 0, atacante,
                          etiqueta="malicioso", escenario="S4-validacion-minima", incidente="INC-A"))

    # S3: consumo anomalo sostenido con el modelo mas caro, hasta la contencion.
    contencion = d14 + 17 * 3600 + 35 * 60
    ts = d14 + 13 * 3600 + 30 * 60
    while ts < contencion:
        ev.append(_evento(ts, "svc-chatbot", "InvokeModel", "m-large", 3000, 2000, 4096, atacante,
                          etiqueta="malicioso", escenario="S3-consumo-anomalo", incidente="INC-A"))
        ts += 3  # 20 solicitudes por minuto

    # S7: contencion (revocacion), reintentos denegados y recuperacion con clave nueva.
    ev.append(_evento(contencion, "svc-chatbot", "iam.DisableKey", "m-small", 0, 0, 0, "10.20.9.9",
                      etiqueta="contexto", escenario="S7-contencion", incidente="INC-A", clave="k1"))
    for i in range(10):
        ev.append(_evento(contencion + 30 + i * 60, "svc-chatbot", "InvokeModel", "m-large",
                          3000, 2000, 4096, atacante, status=403, etiqueta="malicioso",
                          escenario="S7-contencion", incidente="INC-A"))
    ev.append(_evento(d14 + 18 * 3600 + 30 * 60, "svc-chatbot", "iam.CreateKey", "m-small", 0, 0, 0,
                      "10.20.9.9", etiqueta="contexto", escenario="S7-recuperacion",
                      incidente="INC-A", clave="k2"))
    for i in range(30):
        ev.append(_evento(d14 + 18 * 3600 + 35 * 60 + i * 20, "svc-chatbot", "InvokeModel",
                          "m-small", 600, 250, 1024, "10.20.1.11", escenario="S7-recuperacion",
                          clave="k2"))

    # S5: acceso indebido a un Ollama simulado sin autenticacion (identidad "anonymous").
    ts = d15 + 4 * 3600
    while ts < d15 + 6 * 3600:
        ev.append(_evento(ts, "anonymous", "ollama.generate", "local-7b", 1500, 8000, 8192,
                          "203.0.113.77", endpoint="ollama-sim", etiqueta="malicioso",
                          escenario="S5-ollama-expuesto", incidente="INC-B", clave="none"))
        ts += 2  # 30 solicitudes por minuto

    # S6: credencial de servicio con privilegios excesivos: cambio de permisos y uso nocturno.
    ev.append(_evento(d15 + 2 * 3600, "svc-batch-marketing", "iam.AttachPolicy", "m-small", 0, 0, 0,
                      "192.0.2.99", etiqueta="malicioso", escenario="S6-privilegios-excesivos",
                      incidente="INC-C"))
    ts = d15 + 2 * 3600 + 300
    while ts < d15 + 5 * 3600:
        ev.append(_evento(ts, "svc-batch-marketing", "InvokeModel", "m-large", 2500, 1500, 4096,
                          "192.0.2.99", etiqueta="malicioso", escenario="S6-privilegios-excesivos",
                          incidente="INC-C"))
        ts += 6  # 10 solicitudes por minuto

    ev.sort(key=lambda e: (e["ts"], e["identity"], e["action"]))
    return {"seed": seed, "eventos": ev, "ventanas_aprobadas": aprobadas,
            "linea_base_dias": DIAS_BASE, "aviso": AVISO}


# --------------------------------------------------------------------------- #
# Linea base y deteccion
# --------------------------------------------------------------------------- #

def _ventana(ts: int) -> int:
    return (ts - T0) // VENTANA


def _red24(ip: str) -> str:
    return ".".join(ip.split(".")[:3])


def mad_robusta(valores: list[float]) -> tuple[float, float]:
    """Mediana y desviacion robusta sigma = 1.4826 * MAD (escala de una normal)."""
    med = statistics.median(valores)
    mad = statistics.median([abs(v - med) for v in valores])
    return med, 1.4826 * mad


def z_robusto(x: float, med: float, sigma: float) -> float:
    """z = (x - mediana) / max(sigma, 0.1*mediana). Sin unidades. El piso evita dividir por
    casi cero cuando la linea base es muy regular."""
    piso = max(sigma, 0.1 * med, 1e-9)
    return (x - med) / piso


def aprender_linea_base(eventos: list[dict]) -> dict:
    base: dict[str, dict] = {}
    usos = [e for e in eventos if e["ts"] < T0 + DIAS_BASE * DIA]
    por_ident: dict[str, list[dict]] = defaultdict(list)
    for e in usos:
        por_ident[e["identity"]].append(e)
    for ident, lst in por_ident.items():
        reqs = [e for e in lst if e["action"] in ACCIONES_USO]
        costos_v: dict[int, float] = defaultdict(float)
        n_v: dict[int, int] = defaultdict(int)
        for e in reqs:
            costos_v[_ventana(e["ts"])] += e["cost_usd"]
            n_v[_ventana(e["ts"])] += 1
        horas = defaultdict(int)
        for e in reqs:
            horas[(e["ts"] - T0) // 3600 % 24] += 1
        total = sum(horas.values()) or 1
        c_med, c_sig = mad_robusta(list(costos_v.values()) or [0.0])
        n_med, n_sig = mad_robusta([float(v) for v in n_v.values()] or [0.0])
        base[ident] = {
            "modelos": sorted({e["model"] for e in reqs}),
            "redes": sorted({_red24(e["source_ip"]) for e in reqs}),
            "costo_med": c_med, "costo_sigma": c_sig,
            "n_med": n_med, "n_sigma": n_sig,
            "horas": {h: v / total for h, v in horas.items()},
        }
    return base


def _aprobada(aprobadas, ident, modelo, ts):
    for a in aprobadas:
        if a["identity"] == ident and modelo in a["models"] and a["start"] <= ts < a["end"]:
            return a["id"]
    return None


def detectar(datos: dict, usar_contexto: bool = True) -> dict:
    """Evalua las ventanas de los dias de evaluacion. Devuelve alertas con su explicacion."""
    ev = datos["eventos"]
    base = aprender_linea_base(ev)
    aprobadas = datos["ventanas_aprobadas"] if usar_contexto else []
    ini_eval = T0 + DIAS_BASE * DIA

    expuestas: dict[str, int] = {}
    cambios: dict[str, list[int]] = defaultdict(list)
    for e in ev:
        if e["action"] == "secret.exposed":
            expuestas.setdefault(e["identity"], e["ts"])
        if e["action"] in ACCIONES_PERMISOS:
            cambios[e["identity"]].append(e["ts"])

    ventanas: dict[tuple[str, int], list[dict]] = defaultdict(list)
    for e in ev:
        if e["ts"] >= ini_eval:
            ventanas[(e["identity"], _ventana(e["ts"]))].append(e)

    resultado = []
    for (ident, w), lst in sorted(ventanas.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        reqs = [e for e in lst if e["action"] in ACCIONES_USO]
        sensibles = [e for e in lst if e["action"] in ACCIONES_PERMISOS]
        if not reqs and not sensibles and not any(
                e["action"] == "GetModelInvocationLoggingConfiguration" for e in lst):
            continue
        b = base.get(ident)
        fin = T0 + (w + 1) * VENTANA
        senales: dict[str, str] = {}
        ctx = None

        costo_v = sum(e["cost_usd"] for e in reqs)
        if b is None:
            senales["identidad_nueva"] = "identidad sin historial en la linea base"
            if len(reqs) >= MIN_SOLICITUDES_CONTEXTO:
                redes = ",".join(sorted({_red24(e["source_ip"]) for e in reqs}))
                senales["origen_nuevo"] = f"sin historial de origen para la identidad: {redes}"
        else:
            z = z_robusto(costo_v, b["costo_med"], b["costo_sigma"])
            if reqs and z > UMBRAL_Z:
                senales["costo_z"] = f"costo {costo_v:.2f} USD/ventana, z={z:.1f}"
            zn = z_robusto(float(len(reqs)), b["n_med"], b["n_sigma"])
            if reqs and zn > UMBRAL_Z:
                senales["tasa_z"] = f"{len(reqs)} solicitudes/ventana, z={zn:.1f}"
            modelos_nuevos = sorted({e["model"] for e in reqs} - set(b["modelos"]))
            if modelos_nuevos:
                senales["modelo_no_autorizado"] = "modelos fuera del perfil: " + ",".join(modelos_nuevos)
            nuevas = sorted({_red24(e["source_ip"]) for e in reqs} - set(b["redes"]))
            if nuevas and len(reqs) >= MIN_SOLICITUDES_CONTEXTO:
                senales["origen_nuevo"] = "red de origen nunca vista: " + ",".join(nuevas)

        # Fuera de horario: actividad en una hora con <1 % de la actividad historica.
        hora = (w * VENTANA) // 3600 % 24
        actividad = len(reqs) >= MIN_SOLICITUDES_CONTEXTO or sensibles
        if actividad:
            cuota = (b or {}).get("horas", {}).get(hora, 0.0)
            if cuota < 0.01:
                senales["fuera_de_horario"] = f"hora {hora:02d} UTC con {cuota:.1%} de la actividad histórica"

        if any(ts <= fin and fin - ts <= DIA for ts in cambios.get(ident, [])) and (reqs or sensibles):
            senales["cambio_de_permisos"] = "cambio de permisos en las 24 h previas"

        micro = [e for e in reqs if e["max_tokens"] <= 1]
        if len(micro) >= UMBRAL_BARRIDO:
            senales["barrido_minimo"] = (
                f"{len(micro)} solicitudes con max_tokens<=1 sobre {len({e['model'] for e in micro})} modelos")

        if ident in expuestas and expuestas[ident] <= fin and "origen_nuevo" in senales:
            senales["clave_expuesta"] = "la clave figura como expuesta y se usa desde un origen nuevo"

        # Contexto de cambio aprobado: neutraliza solo senales de VOLUMEN y de modelo cubiertas.
        if aprobadas and reqs:
            ids = {_aprobada(aprobadas, ident, e["model"], e["ts"]) for e in reqs}
            if ids and None not in ids and len(ids) == 1:
                ctx = ids.pop()
                for s in ("costo_z", "tasa_z", "modelo_no_autorizado"):
                    senales.pop(s, None)

        puntos = sum(PESOS[s] for s in senales)
        alerta = puntos >= UMBRAL_PUNTOS and len(senales) >= MIN_SENALES
        resultado.append({
            "identity": ident, "ventana": w, "inicio": T0 + w * VENTANA, "fin": fin,
            "puntos": puntos, "senales": senales, "alerta": alerta, "contexto_aprobado": ctx,
            "real_malicioso": any(e["label"] == "malicioso" for e in lst),
            "incidentes": sorted({e["incident"] for e in lst if e["label"] == "malicioso"}),
            "hipotesis": hipotesis(senales) if alerta else None,
        })
    return {"ventanas": resultado, "linea_base": base}


def hipotesis(senales: dict) -> str:
    """Etiqueta HIPOTETICA: la deteccion senala una anomalia, no atribuye un ataque."""
    if "barrido_minimo" in senales:
        return "posible validacion de credenciales (hipotesis; requiere correlacion con el origen)"
    if "cambio_de_permisos" in senales:
        return "posible uso de credencial con privilegios ampliados (hipotesis)"
    if "identidad_nueva" in senales:
        return "posible acceso sin identidad conocida a un endpoint (hipotesis)"
    return "anomalia de consumo sin causa determinada (hipotesis)"


# --------------------------------------------------------------------------- #
# Metricas
# --------------------------------------------------------------------------- #

def metricas(datos: dict, det: dict) -> dict:
    v = det["ventanas"]
    tp = sum(1 for x in v if x["alerta"] and x["real_malicioso"])
    fp = sum(1 for x in v if x["alerta"] and not x["real_malicioso"])
    fn = sum(1 for x in v if not x["alerta"] and x["real_malicioso"])
    tn = sum(1 for x in v if not x["alerta"] and not x["real_malicioso"])
    precision = tp / (tp + fp) if tp + fp else 1.0
    recall = tp / (tp + fn) if tp + fn else 1.0
    incidentes = {}
    for inc in sorted({e["incident"] for e in datos["eventos"] if e["label"] == "malicioso"}):
        primero = min(e["ts"] for e in datos["eventos"] if e["incident"] == inc and e["label"] == "malicioso")
        alertas = [x for x in v if x["alerta"] and inc in x["incidentes"]]
        det_ts = min((x["fin"] for x in alertas), default=None)
        incidentes[inc] = {
            "primer_evento_malicioso": primero,
            "primera_alerta": det_ts,
            "latencia_s": (det_ts - primero) if det_ts is not None else None,
        }
    return {
        "ventanas_evaluadas": len(v), "tp": tp, "fp": fp, "fn": fn, "tn": tn,
        "precision": round(precision, 4), "recall": round(recall, 4),
        "tasa_fp": round(fp / (fp + tn), 4) if fp + tn else 0.0,
        "incidentes": incidentes,
    }


# --------------------------------------------------------------------------- #
# Simulacion de controles y exposicion
# --------------------------------------------------------------------------- #

def exposicion(datos: dict, det: dict, retraso_presupuesto_h: float = 8.0,
               respuesta_humana_min: float = 15.0, mult_tope: float = 2.0) -> dict:
    """Costo facturado por incidente bajo cuatro estrategias.

    Supuestos explicitos (parametros): una alerta de presupuesto llega hasta
    `retraso_presupuesto_h` horas despues del gasto (AWS indica que Budgets se actualiza hasta tres
    veces al dia); un analista tarda `respuesta_humana_min` en revocar; el tope duro es
    `mult_tope` veces el mayor costo diario observado en la linea base de la identidad.
    """
    ev = datos["eventos"]
    base_dia: dict[str, dict[int, float]] = defaultdict(lambda: defaultdict(float))
    for e in ev:
        if e["ts"] < T0 + DIAS_BASE * DIA:
            base_dia[e["identity"]][(e["ts"] - T0) // DIA] += e["cost_usd"]
    topes = {i: mult_tope * max(d.values()) for i, d in base_dia.items()}
    aprobadas = datos["ventanas_aprobadas"]

    def tope_de(ident, ts, modelo, con_cambio):
        t = topes.get(ident, 0.0)  # identidad desconocida: tope 0 (denegar por defecto)
        # Un cambio aprobado amplia el tope de ESE DIA para esa identidad: el gasto acumulado
        # de la rafaga sigue contando despues de que la ventana cierra.
        if con_cambio and any(a["identity"] == ident and (a["start"] - T0) // DIA == (ts - T0) // DIA
                              for a in aprobadas):
            t *= 10
        return t

    def aplicar_tope(con_cambio: bool):
        gasto: dict[tuple[str, int], float] = defaultdict(float)
        aceptado, denegado_benigno = defaultdict(float), defaultdict(int)
        for e in ev:
            if e["action"] not in ACCIONES_USO or e["status"] != 200 or e["ts"] < T0 + DIAS_BASE * DIA:
                continue
            clave = (e["identity"], (e["ts"] - T0) // DIA)
            if gasto[clave] + e["cost_usd"] > tope_de(e["identity"], e["ts"], e["model"], con_cambio):
                if e["label"] == "benigno":
                    denegado_benigno[e["identity"]] += 1
                continue
            gasto[clave] += e["cost_usd"]
            if e["label"] == "malicioso":
                aceptado[e["incident"]] += e["cost_usd"]
        return dict(aceptado), denegado_benigno

    out: dict[str, dict] = {}
    incs = sorted({e["incident"] for e in ev if e["label"] == "malicioso"})
    alerta_por_inc = {i: m["primera_alerta"] for i, m in metricas(datos, det)["incidentes"].items()}
    tope_sin, benig_sin = aplicar_tope(False)
    tope_con, benig_con = aplicar_tope(True)
    for inc in incs:
        maliciosos = [e for e in ev if e["incident"] == inc and e["label"] == "malicioso"
                      and e["status"] == 200]
        primero = min(e["ts"] for e in ev if e["incident"] == inc and e["label"] == "malicioso")
        sin_control = sum(e["cost_usd"] for e in maliciosos)
        corte_pres = primero + retraso_presupuesto_h * 3600 + respuesta_humana_min * 60
        corte_det = (alerta_por_inc[inc] + respuesta_humana_min * 60) if alerta_por_inc.get(inc) else None
        out[inc] = {
            "sin_control": round(sin_control, 2),
            "solo_alerta_presupuesto": round(sum(e["cost_usd"] for e in maliciosos if e["ts"] < corte_pres), 2),
            "deteccion_y_revocacion": (
                round(sum(e["cost_usd"] for e in maliciosos if e["ts"] < corte_det), 2)
                if corte_det else round(sin_control, 2)),
            "tope_duro": round(tope_sin.get(inc, 0.0), 2),
        }
    return {
        "por_incidente": out,
        "parametros": {"retraso_presupuesto_h": retraso_presupuesto_h,
                       "respuesta_humana_min": respuesta_humana_min, "mult_tope": mult_tope},
        "colateral_benigno_denegado": {"tope_sin_contexto": sum(benig_sin.values()),
                                      "tope_con_cambio_aprobado": sum(benig_con.values()),
                                      "por_identidad_sin_contexto": dict(sorted(benig_sin.items()))},
    }


# --------------------------------------------------------------------------- #
# Reportes y exportacion
# --------------------------------------------------------------------------- #

def exportar_ecs(datos: dict, ruta: Path) -> int:
    """NDJSON con campos al estilo ECS para quien quiera cargarlo en un SIEM propio.
    No se ha probado la carga en Elastic: es un formato de intercambio, no una integracion."""
    n = 0
    with ruta.open("w", encoding="utf-8", newline="\n") as fh:
        for e in datos["eventos"]:
            doc = {
                "@timestamp": dt.datetime.fromtimestamp(e["ts"], dt.timezone.utc).isoformat(),
                "event": {"action": e["action"], "outcome": "success" if e["status"] == 200 else "failure",
                          "dataset": "llmjacking.sintetico"},
                "user": {"name": e["identity"]},
                "source": {"ip": e["source_ip"]},
                "llm": {"model": e["model"], "input_tokens": e["input_tokens"],
                        "output_tokens": e["output_tokens"], "max_tokens": e["max_tokens"],
                        "cost_usd": e["cost_usd"], "endpoint": e["endpoint"]},
                "labels": {"ground_truth": e["label"], "scenario": e["scenario"]},
            }
            fh.write(json.dumps(doc, ensure_ascii=False, sort_keys=True) + "\n")
            n += 1
    return n


def _fmt_ts(ts):
    return dt.datetime.fromtimestamp(ts, dt.timezone.utc).strftime("%Y-%m-%d %H:%M") if ts else "—"


def informe_md(datos: dict, det: dict, met: dict, exp: dict, sin_ctx: dict) -> str:
    L = ["# Informe del laboratorio LLMjacking (datos sintéticos)", "", f"> {AVISO}", "",
         "## Resumen ejecutivo", ""]
    total_sin = sum(v["sin_control"] for v in exp["por_incidente"].values())
    total_det = sum(v["deteccion_y_revocacion"] for v in exp["por_incidente"].values())
    total_pres = sum(v["solo_alerta_presupuesto"] for v in exp["por_incidente"].values())
    total_tope = sum(v["tope_duro"] for v in exp["por_incidente"].values())
    L += [
        f"- Sin controles, los tres incidentes simulados cuestan **{total_sin:,.2f} USD** ficticios.",
        f"- Con solo alerta de presupuesto (retraso supuesto de {exp['parametros']['retraso_presupuesto_h']} h): **{total_pres:,.2f} USD**.",
        f"- Con detección + revocación manual: **{total_det:,.2f} USD**.",
        f"- Con tope duro por identidad: **{total_tope:,.2f} USD**, a costa de "
        f"{exp['colateral_benigno_denegado']['tope_sin_contexto']} solicitudes legítimas denegadas "
        f"({exp['colateral_benigno_denegado']['tope_con_cambio_aprobado']} si el tope se amplía con el cambio aprobado).",
        "", "## Detección", "",
        f"| Variante | Precisión | Recall | FP | FN | Tasa FP |", "|---|---|---|---|---|---|",
        f"| Con contexto de cambio aprobado | {met['precision']:.2%} | {met['recall']:.2%} | {met['fp']} | {met['fn']} | {met['tasa_fp']:.2%} |",
        f"| Sin contexto | {sin_ctx['precision']:.2%} | {sin_ctx['recall']:.2%} | {sin_ctx['fp']} | {sin_ctx['fn']} | {sin_ctx['tasa_fp']:.2%} |",
        "", "## Incidentes", "",
        "| Incidente | Primer evento malicioso (UTC) | Primera alerta (UTC) | Latencia | Exposición sin control | Solo presupuesto | Detección + revocación | Tope duro |",
        "|---|---|---|---|---|---|---|---|"]
    for inc, m in met["incidentes"].items():
        x = exp["por_incidente"][inc]
        lat = f"{m['latencia_s'] / 60:.0f} min" if m["latencia_s"] is not None else "no detectado"
        L.append(f"| {inc} | {_fmt_ts(m['primer_evento_malicioso'])} | {_fmt_ts(m['primera_alerta'])} | {lat} | "
                 f"{x['sin_control']:,.2f} | {x['solo_alerta_presupuesto']:,.2f} | "
                 f"{x['deteccion_y_revocacion']:,.2f} | {x['tope_duro']:,.2f} |")
    L += ["", "## Alertas agrupadas en episodios (explicación técnica)", ""]
    episodios: list[dict] = []
    ultimo: dict[str, dict] = {}
    for x in det["ventanas"]:
        if not x["alerta"]:
            continue
        ult = ultimo.get(x["identity"])
        if ult and x["inicio"] - ult["fin"] <= VENTANA:
            ult["fin"], ult["n"] = x["fin"], ult["n"] + 1
            ult["puntos"] = max(ult["puntos"], x["puntos"])
            ult["senales"].update(x["senales"])
        else:
            ep = {"identity": x["identity"], "inicio": x["inicio"], "fin": x["fin"], "n": 1,
                  "puntos": x["puntos"], "senales": dict(x["senales"]), "hip": x["hipotesis"]}
            episodios.append(ep)
            ultimo[x["identity"]] = ep
    for ep in episodios:
        s = "; ".join(f"{k}: {v}" for k, v in ep["senales"].items())
        L.append(f"- **{ep['identity']}**, {_fmt_ts(ep['inicio'])}–{_fmt_ts(ep['fin'])} UTC "
                 f"({ep['n']} ventanas, máx. {ep['puntos']} pts). Señales observadas (con el detalle de la ventana más reciente): {s}. "
                 f"Hipótesis: {ep['hip']}.")
    L += ["", "## Límites", "",
          "- Una alerta es una anomalía, no una atribución: la confirmación exige correlar con registros de identidad y de red.",
          "- Los umbrales se ajustaron sobre este mismo generador; usa `robustez` para ver la variación entre semillas.",
          "- El tope duro de la simulación es por día e identidad; no sustituye cuotas del proveedor.", ""]
    return "\n".join(L)


def ejecutar(seed: int, salida: Path | None = None) -> dict:
    datos = generar(seed)
    det = detectar(datos, True)
    met = metricas(datos, det)
    sin = metricas(datos, detectar(datos, False))
    exp = exposicion(datos, det)
    res = {"seed": seed, "metricas": met, "metricas_sin_contexto": sin, "exposicion": exp,
           "aviso": AVISO}
    if salida:
        salida.mkdir(parents=True, exist_ok=True)
        (salida / "metricas.json").write_text(
            json.dumps(res, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
        (salida / "informe.md").write_text(informe_md(datos, det, met, exp, sin), encoding="utf-8", newline="\n")
        exportar_ecs(datos, salida / "eventos-ecs.ndjson")
    res["_datos"], res["_det"] = datos, det
    return res


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="genera datos, detecta, mide y escribe informe")
    r.add_argument("--seed", type=int, default=7)
    r.add_argument("--out", type=Path, default=Path("salida"))
    q = sub.add_parser("robustez", help="repite el experimento con varias semillas")
    q.add_argument("--seeds", type=int, default=5)
    a = ap.parse_args(argv)
    if a.cmd == "run":
        res = ejecutar(a.seed, a.out)
        m = res["metricas"]
        print(f"precision={m['precision']:.2%} recall={m['recall']:.2%} fp={m['fp']} fn={m['fn']}")
        for inc, x in m["incidentes"].items():
            lat = "no detectado" if x["latencia_s"] is None else f"{x['latencia_s'] / 60:.0f} min"
            print(f"  {inc}: latencia {lat}")
        print(f"salida en {a.out}/ (informe.md, metricas.json, eventos-ecs.ndjson)")
    else:
        for s in range(1, a.seeds + 1):
            m = ejecutar(s)["metricas"]
            print(f"seed={s} precision={m['precision']:.2%} recall={m['recall']:.2%} fp={m['fp']} fn={m['fn']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
