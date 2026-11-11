#!/usr/bin/env python3
"""Instantánea mensual verificable de CVE para el programa.

Cruza tres fuentes públicas oficiales y escribe un JSON reproducible:

* CISA KEV (``cisagov/kev-data``): qué CVE entraron al catálogo en el mes.
* Registro CVE (``cveawg.mitre.org``, formato CVE JSON 5): fechas, producto,
  versiones, CWE, CVSS y referencias del CNA.
* FIRST EPSS (``api.first.org``): probabilidad de explotación en la fecha de consulta.

Solo biblioteca estándar. No se ejecuta en CI (necesita red) y no es un servicio
de monitorización: se lanza a mano cada mes y su salida se revisa antes de
incorporarla a las clases.

Ejemplos::

    python scripts/cve_mensual.py snapshot --mes 2026-10 --salida knowledge/cve/2026-10/instantanea.json
    python scripts/cve_mensual.py snapshot --mes 2026-10 --ids CVE-2026-96655 CVE-2026-0322
    python scripts/cve_mensual.py comparar knowledge/cve/2026-10/instantanea.json nueva.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

KEV_URL = "https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json"
CVE_URL = "https://cveawg.mitre.org/api/cve/{id}"
EPSS_URL = "https://api.first.org/data/v1/epss?cve={ids}"
UA = "modern-cybersecurity-program-snapshot/1.0"


def _get(url: str, timeout: int = 40) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})  # nosec B310
    with urllib.request.urlopen(req, timeout=timeout) as r:  # nosec B310
        return json.loads(r.read().decode("utf-8"))


def kev_del_mes(kev: dict, mes: str) -> list[dict]:
    """Entradas de KEV cuya ``dateAdded`` cae en ``AAAA-MM``."""
    return [v for v in kev["vulnerabilities"] if v["dateAdded"].startswith(mes)]


def resumir_registro(reg: dict) -> dict:
    """Extrae del CVE JSON 5 solo lo que el programa usa."""
    meta = reg.get("cveMetadata", {})
    cna = reg.get("containers", {}).get("cna", {})
    desc = next((d["value"] for d in cna.get("descriptions", []) if d.get("lang", "").startswith("en")), "")
    cwes = sorted({d.get("cweId") for p in cna.get("problemTypes", []) for d in p.get("descriptions", []) if d.get("cweId")})
    afectados = []
    for a in cna.get("affected", []):
        afectados.append({
            "fabricante": a.get("vendor"),
            "producto": a.get("product"),
            "versiones": [
                {k: v for k, v in ver.items() if k in ("version", "status", "lessThan", "lessThanOrEqual", "versionType")}
                for ver in a.get("versions", [])
            ],
        })
    cvss = []
    for m in cna.get("metrics", []):
        for clave, v in m.items():
            if clave.startswith("cvssV"):
                cvss.append({"version": v.get("version"), "puntuacion": v.get("baseScore"),
                             "severidad": v.get("baseSeverity"), "vector": v.get("vectorString"), "fuente": "CNA"})
    # CISA-ADP (Vulnrichment) puede aportar CVSS, CWE y SSVC.
    ssvc = None
    for adp in reg.get("containers", {}).get("adp", []):
        for m in adp.get("metrics", []):
            for clave, v in m.items():
                if clave.startswith("cvssV"):
                    cvss.append({"version": v.get("version"), "puntuacion": v.get("baseScore"),
                                 "severidad": v.get("baseSeverity"), "vector": v.get("vectorString"),
                                 "fuente": adp.get("providerMetadata", {}).get("shortName", "ADP")})
            other = m.get("other")
            if other and other.get("type") == "ssvc":
                ssvc = {o_k: o_v for o in other["content"].get("options", []) for o_k, o_v in o.items()}
        for p in adp.get("problemTypes", []):
            for d in p.get("descriptions", []):
                if d.get("cweId"):
                    cwes = sorted(set(cwes) | {d["cweId"]})
    if ssvc is None:
        for m in cna.get("metrics", []):
            other = m.get("other")
            if other and other.get("type") == "ssvc":
                ssvc = {o_k: o_v for o in other["content"].get("options", []) for o_k, o_v in o.items()}
    return {
        "estado": meta.get("state"),
        "cna": meta.get("assignerShortName"),
        "reservado": meta.get("dateReserved"),
        "publicado": meta.get("datePublished"),
        "actualizado": meta.get("dateUpdated"),
        "titulo": cna.get("title"),
        "descripcion": desc,
        "cwe_registro": cwes,
        "afectados": afectados,
        "cvss": cvss,
        "ssvc_cisa": ssvc,
        "referencias": [r["url"] for r in cna.get("references", [])][:12],
    }


def construir(mes: str, ids: list[str] | None) -> dict:
    kev = _get(KEV_URL)
    del_mes = {v["cveID"]: v for v in kev_del_mes(kev, mes)}
    lista = ids or sorted(del_mes)
    kev_all = {v["cveID"]: v for v in kev["vulnerabilities"]}
    epss: dict[str, dict] = {}
    for i in range(0, len(lista), 30):
        lote = lista[i:i + 30]
        for fila in _get(EPSS_URL.format(ids=",".join(lote)))["data"]:
            epss[fila["cve"]] = fila
    salida = []
    for cve in lista:
        fila: dict = {"cve": cve}
        try:
            fila["registro"] = resumir_registro(_get(CVE_URL.format(id=cve)))
        except urllib.error.HTTPError as e:
            fila["registro"] = {"estado": f"HTTP {e.code}"}
        k = kev_all.get(cve)
        if k:
            fila["kev"] = {"fecha_incorporacion": k["dateAdded"], "plazo_federal": k.get("dueDate"),
                           "nombre": k["vulnerabilityName"], "fabricante": k["vendorProject"], "producto": k["product"],
                           "accion_requerida": k.get("requiredAction"), "ransomware": k.get("knownRansomwareCampaignUse"),
                           "cwe_kev": k.get("cwes", []), "notas": k.get("notes", "")}
        e = epss.get(cve)
        if e:
            fila["epss"] = {"probabilidad": float(e["epss"]), "percentil": float(e["percentile"]), "fecha": e["date"]}
        salida.append(fila)
    return {
        "mes": mes,
        "generado": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fuentes": {"kev": KEV_URL, "kev_version": kev.get("catalogVersion"), "kev_publicado": kev.get("dateReleased"),
                    "registro_cve": CVE_URL, "epss": EPSS_URL},
        "kev_incorporados_en_el_mes": len(del_mes),
        "cves": salida,
    }


def comparar(a: dict, b: dict) -> list[str]:
    """Diferencias entre dos instantáneas: altas, bajas y cambios de campos clave."""
    ia = {c["cve"]: c for c in a["cves"]}
    ib = {c["cve"]: c for c in b["cves"]}
    out = [f"nuevos: {sorted(set(ib) - set(ia))}", f"retirados: {sorted(set(ia) - set(ib))}"]
    for k in sorted(set(ia) & set(ib)):
        for campo in ("publicado", "actualizado", "cwe_registro", "afectados"):
            va, vb = ia[k]["registro"].get(campo), ib[k]["registro"].get(campo)
            if va != vb:
                out.append(f"{k}: cambia {campo}")
        if ia[k].get("kev") != ib[k].get("kev"):
            out.append(f"{k}: cambia la entrada KEV")
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("snapshot", help="construye la instantánea del mes")
    s.add_argument("--mes", required=True, help="AAAA-MM")
    s.add_argument("--ids", nargs="*", help="lista explícita de CVE (por defecto, los de KEV del mes)")
    s.add_argument("--salida", type=Path)
    c = sub.add_parser("comparar", help="compara dos instantáneas")
    c.add_argument("a", type=Path)
    c.add_argument("b", type=Path)
    a = p.parse_args(argv)
    if a.cmd == "snapshot":
        datos = construir(a.mes, a.ids)
        txt = json.dumps(datos, ensure_ascii=False, indent=1) + "\n"
        if a.salida:
            a.salida.parent.mkdir(parents=True, exist_ok=True)
            a.salida.write_text(txt, encoding="utf-8")
            print(f"{len(datos['cves'])} CVE -> {a.salida}")
        else:
            sys.stdout.write(txt)
        return 0
    la = json.loads(a.a.read_text(encoding="utf-8"))
    lb = json.loads(a.b.read_text(encoding="utf-8"))
    print("\n".join(comparar(la, lb)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
