#!/usr/bin/env python3
"""Construye la instantánea de casos reales CWE → CVE → CVSS → EPSS → KEV.

Para estudiar el ciclo «debilidad → vulnerabilidad → priorización» hacen falta
casos REALES con todas las señales juntas. Copiarlos a mano es la forma más
rápida de introducir un error, así que este script los arma consultando las
fuentes oficiales y escribe `datos/casos-cwe-cve.json`:

  NVD (nvd.nist.gov, API 2.0)     CWE asignados por NIST, CVSS v3.1/v4.0 de NIST, versiones afectadas
  CVE Program (cveawg.mitre.org)  CWE y CVSS asignados por el CNA (quien reportó la vulnerabilidad)
  CISA KEV                         ¿explotación activa documentada? ¿uso en ransomware?
  FIRST EPSS                       probabilidad de explotación en 30 días y percentil

Por qué guardar CNA y NVD por separado: pueden discrepar, y esa discrepancia es
materia de estudio (véase la clase 369). Mezclarlos en un solo campo la ocultaría.

La instantánea es una FOTO: KEV y EPSS cambian a diario. El archivo declara la
fecha de consulta; no la trates como el estado actual de esos CVE.

Sin dependencias ni claves obligatorias. NVD limita las consultas anónimas a
unas 5 por cada 30 s; el script espera lo necesario. Con una clave gratuita
en la variable de entorno NVD_API_KEY va más rápido (opcional).

Uso:
    python actualizar_casos.py                       # reconstruye datos/casos-cwe-cve.json
    python actualizar_casos.py --cves CVE-2021-44228 CVE-2014-0160 --salida /tmp/x.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "datos", "casos-cwe-cve.json")

URL_NVD = "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={}"
URL_CVE_ORG = "https://cveawg.mitre.org/api/cve/{}"
URL_KEV = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
URL_EPSS = "https://api.first.org/data/v1/epss?cve={}"

# Casos elegidos porque cada uno enseña algo distinto (el porqué está en la clase 369).
CASOS = [
    "CVE-2021-44228",  # Log4Shell: varios CWE, ninguno «primario»
    "CVE-2014-0160",   # Heartbleed: CWE-125; CVSS «solo» High pero explotación masiva
    "CVE-2019-0708",   # BlueKeep: CWE-416
    "CVE-2023-4863",   # libwebp: CWE-787 en una biblioteca embebida en muchos productos
    "CVE-2023-34362",  # MOVEit: CWE-89 con uso en ransomware
    "CVE-2021-3156",   # sudo: CWE-193 (off-by-one), vector local
    "CVE-2017-5638",   # Struts: CWE-755, clasificación que sorprende
    "CVE-2022-22965",  # Spring4Shell: CWE-94
    "CVE-2021-41773",  # Apache httpd: CWE-22; 9.8 (NVD) vs 7.5 (CNA)
    "CVE-2023-44487",  # HTTP/2 Rapid Reset: NVD sin CWE concreto, CNA CWE-400
    "CVE-2024-6387",   # regreSSHion: CNA CWE-364 vs NVD CWE-362
    "CVE-2024-2021",   # CWE-89 crítico en NVD, medio para el CNA, ni KEV ni EPSS alto
    "CVE-2024-27565",  # CWE-918 con 9.8 y sin explotación documentada
    "CVE-2023-50716",  # CWE-416 con 9.8 y sin explotación documentada
]


def _get(url: str, timeout: int = 60) -> dict | None:
    cabeceras = {"User-Agent": "modern-cybersecurity-program/casos"}
    if "nvd.nist.gov" in url and os.environ.get("NVD_API_KEY"):
        cabeceras["apiKey"] = os.environ["NVD_API_KEY"]
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=cabeceras), timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, ValueError, OSError) as exc:
        print(f"  [!] {url.split('?')[0]}: {exc}", file=sys.stderr)
        return None


# --------------------------------------------------------------------------
# Transformaciones puras (se prueban sin red)
# --------------------------------------------------------------------------
# NVD identifica a quien aportó cada dato con un correo o un UUID de organización.
# Verificado en cveawg.mitre.org: 134c704f-... es el ADP (Authorized Data Publisher) de CISA.
FUENTES_CONOCIDAS = {
    "nvd@nist.gov": "NVD",
    "134c704f-9b21-4f2e-91b3-4a467353bcc0": "CISA-ADP",
}


def etiqueta_fuente(fuente: str) -> str:
    return FUENTES_CONOCIDAS.get(fuente, fuente)


def severidad(puntuacion: float) -> str:
    if puntuacion == 0:
        return "NONE"
    return "LOW" if puntuacion < 4 else "MEDIUM" if puntuacion < 7 else "HIGH" if puntuacion < 9 else "CRITICAL"


def extraer_nvd(registro: dict) -> dict:
    """Del JSON de NVD: CWE, CVSS y versiones afectadas, separando la fuente de cada dato."""
    cve = registro["cve"]
    cwes = []
    for w in cve.get("weaknesses", []):
        for d in w["description"]:
            cwes.append({"id": d["value"], "tipo": w["type"], "fuente": etiqueta_fuente(w["source"])})
    cvss31, cvss40 = [], []
    for m in cve.get("metrics", {}).get("cvssMetricV31", []):
        cvss31.append({"fuente": etiqueta_fuente(m["source"]), "vector": m["cvssData"]["vectorString"], "puntuacion": m["cvssData"]["baseScore"]})
    for m in cve.get("metrics", {}).get("cvssMetricV40", []):
        cvss40.append({"fuente": etiqueta_fuente(m["source"]), "vector": m["cvssData"]["vectorString"], "puntuacion": m["cvssData"]["baseScore"]})
    afectado = []
    for conf in cve.get("configurations", []):
        for nodo in conf.get("nodes", []):
            for cm in nodo.get("cpeMatch", []):
                if not cm.get("vulnerable"):
                    continue
                partes = cm["criteria"].split(":")
                fila = {"vendedor": partes[3], "producto": partes[4]}
                for clave, destino in (("versionStartIncluding", "desde_incluida"), ("versionStartExcluding", "desde_excluida"),
                                       ("versionEndIncluding", "hasta_incluida"), ("versionEndExcluding", "hasta_excluida")):
                    if cm.get(clave):
                        fila[destino] = cm[clave]
                if len(partes) > 5 and partes[5] not in ("*", "-"):
                    fila["version"] = partes[5]
                if fila not in afectado:
                    afectado.append(fila)
    descripcion = next((d["value"] for d in cve.get("descriptions", []) if d.get("lang") == "en"), "")
    return {
        "publicada": cve.get("published", "")[:10],
        "descripcion_en": descripcion,
        "cwe_nvd": cwes,
        "cvss31": cvss31,
        "cvss40": cvss40,
        "afectado": afectado[:40],
    }


def extraer_cna(registro: dict) -> dict:
    """Del JSON de CVE Program: CWE y CVSS tal como los publicó el CNA que asignó el CVE."""
    cna = registro.get("containers", {}).get("cna", {})
    cwes = []
    for pt in cna.get("problemTypes", []):
        for d in pt.get("descriptions", []):
            if d.get("cweId"):
                cwes.append(d["cweId"])
    cvss40 = []
    cvss31 = []
    for m in cna.get("metrics", []):
        if "cvssV4_0" in m:
            cvss40.append({"vector": m["cvssV4_0"]["vectorString"], "puntuacion": m["cvssV4_0"]["baseScore"]})
        if "cvssV3_1" in m:
            cvss31.append({"vector": m["cvssV3_1"]["vectorString"], "puntuacion": m["cvssV3_1"]["baseScore"]})
    # Datos que aportan los ADP (p. ej. CISA-ADP) en sus propios contenedores.
    cwe_adp: dict[str, list[str]] = {}
    ssvc: dict | None = None
    for adp in registro.get("containers", {}).get("adp", []):
        nombre = adp.get("providerMetadata", {}).get("shortName", "")
        ids = [d["cweId"] for pt in adp.get("problemTypes", []) for d in pt.get("descriptions", []) if d.get("cweId")]
        if ids:
            cwe_adp[nombre] = sorted(dict.fromkeys(ids))
        # CISA-ADP (Vulnrichment) publica los puntos de decisión SSVC de cada CVE: es de donde
        # BOD 26-04 toma «Automatable» y «Technical Impact».
        if nombre == "CISA-ADP":
            for m in adp.get("metrics", []):
                otro = m.get("other", {})
                if otro.get("type") == "ssvc":
                    opciones = {k: v for o in otro["content"].get("options", []) for k, v in o.items()}
                    ssvc = {
                        "explotacion": opciones.get("Exploitation", ""),
                        "automatizable": opciones.get("Automatable", ""),
                        "impacto_tecnico": opciones.get("Technical Impact", ""),
                        "version": otro["content"].get("version", ""),
                        "fecha": otro["content"].get("timestamp", "")[:10],
                    }
    return {
        "asignador": registro.get("cveMetadata", {}).get("assignerShortName", ""),
        "cwe_cna": sorted(dict.fromkeys(cwes)),
        "cwe_adp": cwe_adp,
        "ssvc_cisa": ssvc,
        "cvss31_cna": cvss31,
        "cvss40_cna": cvss40,
    }


def extraer_kev(catalogo: dict, cve: str) -> dict | None:
    for v in catalogo.get("vulnerabilities", []):
        if v.get("cveID") == cve:
            return {
                "agregada": v.get("dateAdded", ""),
                "fecha_limite": v.get("dueDate", ""),
                "ransomware": v.get("knownRansomwareCampaignUse", ""),
                "nombre": v.get("vulnerabilityName", ""),
                "cwes": v.get("cwes", []),
            }
    return None


def armar_caso(cve: str, nvd: dict | None, cve_org: dict | None, kev: dict, epss: dict | None) -> dict:
    caso: dict = {"cve": cve}
    if nvd:
        caso.update(extraer_nvd(nvd))
    if cve_org:
        caso.update(extraer_cna(cve_org))
    caso["kev"] = extraer_kev(kev, cve)
    caso["epss"] = (
        {"puntuacion": float(epss["epss"]), "percentil": float(epss["percentile"]), "fecha": epss["date"]} if epss else None
    )
    return caso


# --------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Reconstruye la instantánea de casos reales CWE/CVE/CVSS/EPSS/KEV.")
    ap.add_argument("--cves", nargs="+", default=CASOS)
    ap.add_argument("--salida", default=SALIDA)
    ap.add_argument("--pausa", type=float, default=None, help="segundos entre consultas a NVD (por defecto 6.5; 0.7 con NVD_API_KEY)")
    a = ap.parse_args(argv)
    pausa = a.pausa if a.pausa is not None else (0.7 if os.environ.get("NVD_API_KEY") else 6.5)

    print("Descargando catálogo CISA KEV ...", file=sys.stderr)
    kev = _get(URL_KEV, timeout=120)
    if not kev:
        print("ERROR: sin KEV no se puede construir la instantánea.", file=sys.stderr)
        return 1

    casos = []
    for i, cve in enumerate(sorted(set(a.cves))):
        print(f"[{i + 1}/{len(set(a.cves))}] {cve}", file=sys.stderr)
        nvd = _get(URL_NVD.format(cve))
        nvd_cve = nvd["vulnerabilities"][0] if nvd and nvd.get("vulnerabilities") else None
        org = _get(URL_CVE_ORG.format(cve))
        epss_resp = _get(URL_EPSS.format(cve))
        epss = epss_resp["data"][0] if epss_resp and epss_resp.get("data") else None
        if not (nvd_cve and org and epss):
            print(f"  [!] datos incompletos para {cve}; se omite (no se rellenan huecos)", file=sys.stderr)
            continue
        casos.append(armar_caso(cve, nvd_cve, org, kev, epss))
        time.sleep(pausa)

    doc = {
        "procedencia": {
            "fecha_consulta": time.strftime("%Y-%m-%d", time.gmtime()),
            "kev_version_catalogo": kev.get("catalogVersion", ""),
            "kev_fecha_publicacion": kev.get("dateReleased", ""),
            "fuentes": {
                "nvd": "https://services.nvd.nist.gov/rest/json/cves/2.0",
                "cve_program": "https://cveawg.mitre.org/api/cve/",
                "cisa_kev": URL_KEV,
                "first_epss": "https://api.first.org/data/v1/epss",
            },
            "advertencia": "Instantánea: KEV y EPSS cambian a diario. No es el estado actual de estos CVE.",
        },
        "casos": casos,
    }
    os.makedirs(os.path.dirname(os.path.abspath(a.salida)), exist_ok=True)
    with open(a.salida, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    print(f"{len(casos)} caso(s) escritos en {a.salida}", file=sys.stderr)
    return 0 if len(casos) == len(set(a.cves)) else 1


if __name__ == "__main__":
    sys.exit(main())
