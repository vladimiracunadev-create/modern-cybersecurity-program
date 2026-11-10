#!/usr/bin/env python3
"""Laboratorio defensivo de manipulacion fisica de hardware (datos 100 % sinteticos).

Modela un dispositivo FICTICIO ("Modelo-X") con secure element, microcontrolador, pantalla
y bateria, y practica seis habilidades defensivas: comparar una placa con su referencia,
leer un bus de pantalla simulado, buscar rafagas de consumo, separar autenticidad de
integridad y de cadena de custodia, preservar evidencia con una cadena de hashes y verificar
controles de distribucion.

NO contiene: firmware de implante, esquemas de montaje, protocolos reales de pantalla,
tipografias reales, listas de palabras de recuperacion ni captura de nada real. El "texto"
del bus es una cadena ficticia codificada con una tabla de glifos inventada.

Uso:
    python tamper_lab.py run --seed 7 --out salida/
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import statistics
import sys
from pathlib import Path

AVISO = ("Dispositivo, componentes, trazas, consumos y envios FICTICIOS. Los resultados ensenan a razonar "
         "sobre evidencia; no describen un producto real ni construyen un implante.")

# --------------------------------------------------------------------------- #
# A y C. Referencia, muestras y comparacion de placa
# --------------------------------------------------------------------------- #

REFERENCIA = {
    "U1": {"tipo": "secure_element", "paquete": "QFN32", "marcado": "SE-DEMO-1"},
    "U2": {"tipo": "mcu", "paquete": "LQFP48", "marcado": "MCU-DEMO-2"},
    "U3": {"tipo": "pantalla_oled", "paquete": "modulo", "marcado": "OLED-DEMO-A"},
    "U4": {"tipo": "radio_corto_alcance", "paquete": "modulo", "marcado": "BLE-DEMO-1"},
    "J1": {"tipo": "conector_usb", "paquete": "SMD", "marcado": "USB-DEMO"},
    "Y1": {"tipo": "cristal", "paquete": "SMD", "marcado": "XTAL-DEMO"},
    "BT1": {"tipo": "bateria", "paquete": "celda", "marcado": "BAT-DEMO-100", "capacidad_mah": 100},
}

# Tipos cuya presencia NO prevista indica capacidad de computo, comunicacion o identidad ajena.
TIPOS_CRITICOS = {"mcu", "modem_celular", "esim", "antena", "radio_corto_alcance", "memoria", "secure_element"}
TIPOS_SOSPECHOSOS = {"flex_adicional", "bateria", "pantalla_oled"}


def _copia(d):
    return json.loads(json.dumps(d))


def muestras() -> dict:
    """Tres muestras. B anade electronica sin tocar el secure element; C es una reparacion legitima."""
    a = _copia(REFERENCIA)
    b = _copia(REFERENCIA)
    b["X1"] = {"tipo": "mcu", "paquete": "QFN16", "marcado": ""}
    b["X2"] = {"tipo": "modem_celular", "paquete": "modulo", "marcado": ""}
    b["X3"] = {"tipo": "esim", "paquete": "2x2mm", "marcado": ""}
    b["X4"] = {"tipo": "antena", "paquete": "flex", "marcado": ""}
    b["X5"] = {"tipo": "flex_adicional", "paquete": "bajo_pantalla", "marcado": ""}
    b["BT1"]["capacidad_mah"] = 90  # bateria algo menor: hay que hacer sitio
    c = _copia(REFERENCIA)
    c["U3"]["marcado"] = "OLED-DEMO-B"  # pantalla de otro lote
    return {"MUESTRA-A": a, "MUESTRA-B": b, "MUESTRA-C": c}


def comparar_pcb(ref: dict, muestra: dict) -> dict:
    anadidos = sorted(k for k in muestra if k not in ref)
    ausentes = sorted(k for k in ref if k not in muestra)
    modificados = {}
    for k in sorted(set(ref) & set(muestra)):
        difs = {c: (ref[k].get(c), muestra[k].get(c)) for c in set(ref[k]) | set(muestra[k])
                if ref[k].get(c) != muestra[k].get(c)}
        if difs:
            modificados[k] = difs
    hallazgos = []
    for k in anadidos:
        t = muestra[k]["tipo"]
        sev = "alta" if t in TIPOS_CRITICOS or t == "modem_celular" else "media"
        if not muestra[k].get("marcado"):
            sev = "alta"
        hallazgos.append({"ref": k, "tipo": t, "severidad": sev,
                          "motivo": "componente no previsto" + (" y sin marcado" if not muestra[k].get("marcado") else "")})
    for k, difs in modificados.items():
        t = ref[k]["tipo"]
        hallazgos.append({"ref": k, "tipo": t, "severidad": "media" if t in TIPOS_SOSPECHOSOS else "baja",
                          "motivo": "difiere de la referencia: " + ", ".join(sorted(difs))})
    for k in ausentes:
        hallazgos.append({"ref": k, "tipo": ref[k]["tipo"], "severidad": "alta", "motivo": "componente previsto ausente"})
    return {"anadidos": anadidos, "ausentes": ausentes, "modificados": modificados, "hallazgos": hallazgos}


def interpretar_modificacion(hallazgo: dict) -> str:
    """Un cambio no es un implante. Hay que separar reparacion, lote distinto y componente anadido."""
    if hallazgo["motivo"].startswith("difiere"):
        return "compatible con reparacion o cambio de lote; verifica orden de servicio y proveedor antes de concluir"
    return "no explicado por la referencia; requiere inspeccion adicional (no basta la apariencia)"


# --------------------------------------------------------------------------- #
# B. Bus de pantalla simulado con texto ficticio
# --------------------------------------------------------------------------- #

# Tabla de glifos INVENTADA para este laboratorio: no corresponde a ninguna pantalla real.
GLIFOS = {c: i + 17 for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- ")}
INVERSA = {v: k for k, v in GLIFOS.items()}


def generar_traza_spi(texto: str, seed: int = 1, carga_extra_pf: float = 0.0) -> dict:
    """Traza sintetica: tramas de datos de pantalla + un parametro analogico (tiempo de subida).

    `carga_extra_pf` simula la capacitancia anadida por un dispositivo conectado al bus; es un
    modelo didactico de una medicion que SI puede delatar un tercero, no una receta."""
    rng = random.Random(seed)  # nosec B311
    tramas = []
    for i, ch in enumerate(texto):
        tramas.append({"t_us": i * 120, "dc": 1, "payload": [GLIFOS[ch]]})
    base_rise_ns = 22.0 + 0.9 * carga_extra_pf  # ns, crece con la carga
    subida = [round(rng.gauss(base_rise_ns, 0.6), 2) for _ in range(len(tramas))]
    return {"tramas": tramas, "tiempo_subida_ns": subida}


def analizar_traza_spi(traza: dict, referencia_subida_ns: float = 22.0) -> dict:
    datos = [b for t in traza["tramas"] if t["dc"] == 1 for b in t["payload"]]
    texto = "".join(INVERSA.get(b, "?") for b in datos)
    cuenta = {}
    for b in datos:
        cuenta[b] = cuenta.get(b, 0) + 1
    n = len(datos) or 1
    entropia = -sum((c / n) * math.log2(c / n) for c in cuenta.values())
    subida = statistics.mean(traza["tiempo_subida_ns"]) if traza["tiempo_subida_ns"] else 0.0
    desv = subida - referencia_subida_ns
    return {
        "bytes_de_datos": len(datos),
        "entropia_bits_por_byte": round(entropia, 3),
        "contenido_recuperable": texto,
        "lectura": ("El bus lleva lo que el usuario ve: cualquier dispositivo conectado a el observa lo mismo. "
                    "El secure element no puede protegerlo una vez que sale hacia la pantalla."),
        "tiempo_subida_medio_ns": round(subida, 2),
        "desviacion_subida_ns": round(desv, 2),
        "indicio_de_carga_extra": desv > 3.0,
        "limite": "Un tiempo de subida mayor es un indicio compatible con carga adicional, no una prueba; "
                  "depende de la sonda, el cableado y la temperatura.",
    }


# --------------------------------------------------------------------------- #
# D. Consumo electrico simulado
# --------------------------------------------------------------------------- #

def generar_consumo(seed: int, con_rafagas: bool, segundos: int = 600) -> list:
    rng = random.Random(seed)  # nosec B311
    s = []
    for t in range(segundos):
        v = rng.gauss(12.0, 0.4)
        if t % 150 == 20:  # actividad corta y legitima del radio de corto alcance
            v += 18
        if con_rafagas and 5 <= (t % 60) < 9:  # rafaga periodica: 4 s cada 60 s
            v += 85
        s.append(round(v, 2))
    return s


def detectar_rafagas(serie: list, z_min: float = 6.0, duracion_min_s: int = 3) -> dict:
    med = statistics.median(serie)
    mad = statistics.median([abs(x - med) for x in serie])
    sigma = max(1.4826 * mad, 0.05)
    altos = [(x - med) / sigma > z_min for x in serie]
    rafagas, ini = [], None
    for i, a in enumerate(altos + [False]):
        if a and ini is None:
            ini = i
        elif not a and ini is not None:
            if i - ini >= duracion_min_s:
                rafagas.append((ini, i - ini))
            ini = None
    inicios = [r[0] for r in rafagas]
    pasos = [b - a for a, b in zip(inicios, inicios[1:])]
    periodica = len(pasos) >= 3 and statistics.pstdev(pasos) <= 2
    return {"mediana_ma": round(med, 2), "sigma_ma": round(sigma, 3), "rafagas": rafagas,
            "periodicidad_s": round(statistics.median(pasos), 1) if pasos else None,
            "patron_periodico": periodica,
            "limite": "Una rafaga periodica es compatible con una radio activa; no identifica su funcion. Las "
                      "rafagas cortas legitimas se descartan con la duracion minima."}


# --------------------------------------------------------------------------- #
# F. Cadena de custodia con hashes encadenados
# --------------------------------------------------------------------------- #

def _h(prev: str, e: dict) -> str:
    cuerpo = json.dumps(e, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256((prev + cuerpo).encode("utf-8")).hexdigest()


def crear_cadena(eslabones: list) -> list:
    cadena, prev = [], "0" * 64
    for e in eslabones:
        h = _h(prev, e)
        cadena.append({**e, "prev": prev, "hash": h})
        prev = h
    return cadena


def verificar_cadena(cadena: list) -> dict:
    prev, problemas = "0" * 64, []
    for i, e in enumerate(cadena):
        base = {k: v for k, v in e.items() if k not in ("prev", "hash")}
        if e["prev"] != prev:
            problemas.append(f"eslabon {i}: prev no coincide")
        if e["hash"] != _h(e["prev"], base):
            problemas.append(f"eslabon {i}: hash no coincide con el contenido")
        prev = e["hash"]
    return {"integra": not problemas, "problemas": problemas}


AUTORIZADOS = {"fabricante-demo", "distribuidor-demo", "revendedor-autorizado-demo", "cliente-final"}


def envio_ejemplo() -> list:
    return [
        {"de": "fabricante-demo", "a": "distribuidor-demo", "fecha": "2026-03-01", "sello": "S-1001", "estado_sello": "intacto"},
        {"de": "distribuidor-demo", "a": "revendedor-autorizado-demo", "fecha": "2026-03-20", "sello": "S-1001", "estado_sello": "intacto"},
        {"de": "revendedor-autorizado-demo", "a": "cliente-final", "fecha": "2026-04-02", "sello": "S-1001", "estado_sello": "intacto"},
    ]


def envio_con_huecos() -> list:
    return [
        {"de": "fabricante-demo", "a": "distribuidor-demo", "fecha": "2026-03-01", "sello": "S-2001", "estado_sello": "intacto"},
        {"de": "intermediario-desconocido", "a": "revendedor-no-autorizado", "fecha": "2026-03-25", "sello": "S-2001", "estado_sello": "reemplazado"},
        {"de": "revendedor-no-autorizado", "a": "cliente-final", "fecha": "2026-05-10", "sello": "S-9999", "estado_sello": "intacto", "devolucion_reabierta": True},
    ]


def auditar_trazabilidad(envio: list) -> dict:
    hallazgos = []
    for i, e in enumerate(envio):
        if e["de"] not in AUTORIZADOS:
            hallazgos.append(f"eslabon {i}: origen no autorizado ({e['de']})")
        if e["a"] not in AUTORIZADOS:
            hallazgos.append(f"eslabon {i}: destino no autorizado ({e['a']})")
        if i and envio[i - 1]["a"] != e["de"]:
            hallazgos.append(f"eslabon {i}: salto de custodia ({envio[i - 1]['a']} -> {e['de']})")
        if i and envio[i - 1].get("sello") != e.get("sello"):
            hallazgos.append(f"eslabon {i}: el numero de sello cambia ({envio[i - 1].get('sello')} -> {e.get('sello')})")
        if e.get("estado_sello") != "intacto":
            hallazgos.append(f"eslabon {i}: sello {e.get('estado_sello')}")
        if e.get("devolucion_reabierta"):
            hallazgos.append(f"eslabon {i}: devolucion reabierta y reingresada a venta")
    return {"continua": not hallazgos, "hallazgos": hallazgos}


# --------------------------------------------------------------------------- #
# E. Veredictos independientes y riesgo
# --------------------------------------------------------------------------- #

def veredictos(attestation_ok: bool, comparacion: dict, trazabilidad: dict) -> dict:
    graves = [h for h in comparacion["hallazgos"] if h["severidad"] == "alta"]
    return {
        "autenticidad_del_secure_element": "verificada" if attestation_ok else "fallida",
        "integridad_fisica": "fallida" if graves else ("no_concluyente" if comparacion["hallazgos"] else "verificada"),
        "cadena_de_custodia": "verificada" if trazabilidad["continua"] else "fallida",
        "nota": "Son tres preguntas distintas: aprobar una no demuestra las otras dos.",
    }


def evaluar_riesgo(v: dict, rafagas: bool, indicio_bus: bool) -> dict:
    puntos, razones = 0, []
    if v["integridad_fisica"] == "fallida":
        puntos += 5
        razones.append("componentes no previstos en la placa")
    elif v["integridad_fisica"] == "no_concluyente":
        puntos += 2
        razones.append("diferencias sin explicar frente a la referencia")
    if v["cadena_de_custodia"] == "fallida":
        puntos += 3
        razones.append("cadena de custodia interrumpida o no autorizada")
    if rafagas:
        puntos += 2
        razones.append("rafagas periodicas de consumo compatibles con una radio")
    if indicio_bus:
        puntos += 1
        razones.append("carga adicional en el bus de pantalla (indicio)")
    if v["autenticidad_del_secure_element"] == "fallida":
        puntos += 5
        razones.append("el secure element no supera la attestation")
    nivel = "critico" if puntos >= 8 else "alto" if puntos >= 5 else "medio" if puntos >= 2 else "bajo"
    accion = {"critico": "No inicializar ni usar. Si ya se uso, tratar como expuesto cualquier secreto mostrado y migrar a un dispositivo de confianza.",
              "alto": "Aislar, no usar para secretos, preservar evidencia e inspeccionar.",
              "medio": "Inspeccionar antes de usar.", "bajo": "Uso normal con controles de rutina."}[nivel]
    return {"puntos": puntos, "nivel": nivel, "razones": razones, "accion": accion}


# --------------------------------------------------------------------------- #
# H. Controles de distribucion
# --------------------------------------------------------------------------- #

POLITICA = ["canal_autorizado", "sello_numerado_registrado", "fotos_de_recepcion", "numero_de_serie_coincide",
            "devoluciones_inspeccionadas", "masa_dentro_de_tolerancia"]


def verificar_controles(envio_real: dict) -> dict:
    res = {c: bool(envio_real.get(c)) for c in POLITICA}
    falla = [c for c, ok in res.items() if not ok]
    return {"controles": res, "fallan": falla, "cumple": not falla,
            "limite": "La masa y el sello detectan manipulaciones groseras; un implante de pocos gramos o un sello "
                      "reproducido pueden pasar. Por eso se combinan con compra autorizada y trazabilidad."}


# --------------------------------------------------------------------------- #
# G. Informe
# --------------------------------------------------------------------------- #

def ejecutar(seed: int = 7) -> dict:
    ms = muestras()
    out = {"seed": seed, "aviso": AVISO, "muestras": {}}
    cadenas = {"MUESTRA-A": envio_ejemplo(), "MUESTRA-B": envio_con_huecos(), "MUESTRA-C": envio_ejemplo()}
    for nombre, bom in ms.items():
        comp = comparar_pcb(REFERENCIA, bom)
        traza = generar_traza_spi("MUESTRA FICTICIA 0001", seed, carga_extra_pf=8.0 if nombre == "MUESTRA-B" else 0.0)
        bus = analizar_traza_spi(traza)
        cons = detectar_rafagas(generar_consumo(seed, nombre == "MUESTRA-B"))
        tra = auditar_trazabilidad(cadenas[nombre])
        v = veredictos(True, comp, tra)  # el secure element es autentico en las tres
        riesgo = evaluar_riesgo(v, cons["patron_periodico"], bus["indicio_de_carga_extra"])
        out["muestras"][nombre] = {"comparacion": comp, "bus": bus, "consumo": cons, "trazabilidad": tra,
                                   "veredictos": v, "riesgo": riesgo}
    return out


def informe_md(res: dict) -> str:
    L = ["# Informe forense del laboratorio de hardware (datos sintéticos)", "", f"> {res['aviso']}", ""]
    L += ["## Resumen", "", "| Muestra | Autenticidad SE | Integridad física | Cadena de custodia | Riesgo |", "|---|---|---|---|---|"]
    for n, m in res["muestras"].items():
        v = m["veredictos"]
        L.append(f"| {n} | {v['autenticidad_del_secure_element']} | {v['integridad_fisica']} | {v['cadena_de_custodia']} | {m['riesgo']['nivel']} |")
    L += ["", "> Las tres primeras columnas responden preguntas **distintas**. En la MUESTRA-B el secure element es auténtico y aun así el riesgo es crítico.", ""]
    for n, m in res["muestras"].items():
        L += [f"## {n}", "", "**Hechos (observados en datos sintéticos)**", ""]
        if m["comparacion"]["hallazgos"]:
            for h in m["comparacion"]["hallazgos"]:
                L.append(f"- `{h['ref']}` ({h['tipo']}), severidad {h['severidad']}: {h['motivo']}.")
        else:
            L.append("- La placa coincide con la referencia.")
        if m["consumo"]["rafagas"]:
            L.append(f"- {len(m['consumo']['rafagas'])} ráfagas de consumo; periodicidad {m['consumo']['periodicidad_s']} s.")
        L.append(f"- Tiempo de subida medio en el bus: {m['bus']['tiempo_subida_medio_ns']} ns (desviación {m['bus']['desviacion_subida_ns']} ns).")
        for h in m["trazabilidad"]["hallazgos"]:
            L.append(f"- Custodia: {h}.")
        L += ["", "**Inferencias**", "", f"- Riesgo **{m['riesgo']['nivel']}** ({m['riesgo']['puntos']} puntos): " + "; ".join(m["riesgo"]["razones"] or ["sin razones"]) + ".",
              f"- Acción: {m['riesgo']['accion']}", "", "**Límites**", "",
              f"- {m['bus']['limite']}", f"- {m['consumo']['limite']}",
              "- Ninguna medición sustituye la inspección física y el análisis del componente, ni prueba por sí sola la intención.", ""]
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--seed", type=int, default=7)
    r.add_argument("--out", type=Path, default=Path("salida"))
    a = ap.parse_args(argv)
    res = ejecutar(a.seed)
    a.out.mkdir(parents=True, exist_ok=True)
    (a.out / "resultado.json").write_text(json.dumps(res, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    (a.out / "informe.md").write_text(informe_md(res), encoding="utf-8", newline="\n")
    for n, m in res["muestras"].items():
        v = m["veredictos"]
        print(f"{n}: autenticidad={v['autenticidad_del_secure_element']} integridad={v['integridad_fisica']} "
              f"custodia={v['cadena_de_custodia']} riesgo={m['riesgo']['nivel']}")
    print(f"salida en {a.out}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
