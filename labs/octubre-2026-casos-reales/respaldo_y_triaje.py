#!/usr/bin/env python3
"""Dos herramientas del caso de octubre de 2026: supervivencia de respaldos y triaje del mes.

1. `evaluar_respaldos`: ¿qué copias sobreviven si el atacante controla el plano de gestión de un dominio de confianza?
   Inspirado en la lección pública del incidente de IDC Frontier (IDCF Cloud, 7 de octubre de 2026): la compañía informó
   que la recuperación por *snapshot* solo alcanzaba a una parte de los clientes afectados. El inventario aquí es
   **ficticio**; no se infieren detalles técnicos del proveedor real (su vector inicial no fue divulgado).
2. `triaje_del_mes`: lee la instantánea `knowledge/cve/2026-10/instantanea.json` y calcula, con datos oficiales, el
   desfase entre publicación y entrada a KEV, la categoría de fecha, y el plazo de referencia de BOD 26-04 reutilizando
   `labs/devsecops-pipeline/bod2604.py`.

Solo biblioteca estándar.
"""
from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "labs" / "devsecops-pipeline"))
import bod2604  # noqa: E402

# ------------------------------------------------------------------ respaldos


@dataclass(frozen=True)
class Copia:
    nombre: str
    dominio: str              # dominio de confianza: quién la administra (mismas credenciales/plano de control)
    inmutable: bool           # no puede borrarse ni sobrescribirse antes del fin de retención, ni con credenciales de admin
    fuera_de_banda: bool      # separada del entorno de producción (otro proveedor, otra cuenta, desconectada)
    restauracion_probada: int | None   # días desde la última restauración completa verificada (None = nunca)
    rpo_horas: int


def sobrevive(c: Copia, dominio_comprometido: str) -> bool:
    """Una copia sobrevive si el atacante no puede alcanzarla con el control que ya tiene."""
    if c.dominio != dominio_comprometido:
        return True
    return c.inmutable and c.fuera_de_banda


def evaluar_respaldos(copias: list[Copia], dominio_comprometido: str, max_dias_sin_probar: int = 90) -> dict:
    vivas = [c for c in copias if sobrevive(c, dominio_comprometido)]
    utiles = [c for c in vivas if c.restauracion_probada is not None and c.restauracion_probada <= max_dias_sin_probar]
    return {
        "dominio_comprometido": dominio_comprometido,
        "copias": len(copias),
        "sobreviven": [c.nombre for c in vivas],
        "perdidas": [c.nombre for c in copias if c not in vivas],
        "utilizables_probadas": [c.nombre for c in utiles],
        "sin_probar_o_caducadas": [c.nombre for c in vivas if c not in utiles],
        "rpo_mejor_horas": min((c.rpo_horas for c in utiles), default=None),
        "recuperable": bool(utiles),
    }


# ------------------------------------------------------------------ triaje del mes


def _fecha(s: str | None) -> date | None:
    return datetime.fromisoformat(s.replace("Z", "+00:00")).date() if s else None


def categoria_fecha(publicado: date, kev: date, mes: str) -> str:
    """Compara la fecha de publicación del registro CVE con el mes estudiado y con la entrada a KEV."""
    a, m = mes.split("-")
    ini = date(int(a), int(m), 1)
    fin = date(int(a) + (int(m) == 12), int(m) % 12 + 1, 1)
    if publicado < ini:
        return "publicado-antes-del-mes"
    if publicado >= fin:
        return "registro-publicado-despues-del-mes"
    return "publicado-en-el-mes"


def triaje_del_mes(ruta: Path | str, expuesto: bool = True) -> list[dict]:
    datos = json.loads(Path(ruta).read_text(encoding="utf-8"))
    mes = datos["mes"]
    filas = []
    for c in datos["cves"]:
        r, k = c["registro"], c.get("kev")
        if not k:
            continue
        pub, alta = _fecha(r["publicado"]), _fecha(k["fecha_incorporacion"])
        ssvc = r.get("ssvc_cisa") or {}
        plazo = None
        if ssvc.get("Technical Impact") in ("total", "partial") and ssvc.get("Automatable") in ("yes", "no"):
            plazo = bod2604.plazo(expuesto, True, ssvc["Automatable"] == "yes", ssvc["Technical Impact"])
        cvss = [x["puntuacion"] for x in r.get("cvss", []) if x.get("puntuacion") is not None]
        filas.append({
            "cve": c["cve"],
            "fabricante": k["fabricante"], "producto": k["producto"],
            "publicado": pub.isoformat(), "kev": alta.isoformat(),
            "dias_publicacion_a_kev": (alta - pub).days,
            "categoria": categoria_fecha(pub, alta, mes),
            "cvss_max": max(cvss) if cvss else None,
            "epss": (c.get("epss") or {}).get("probabilidad"),
            "plazo_bod": plazo["texto"] if plazo else None,
            "triaje_forense": plazo["triaje_forense"] if plazo else None,
        })
    return sorted(filas, key=lambda f: f["kev"])


def resumen(filas: list[dict]) -> dict:
    cat: dict[str, int] = {}
    for f in filas:
        cat[f["categoria"]] = cat.get(f["categoria"], 0) + 1
    return {"total": len(filas), "por_categoria": cat,
            "kev_antes_que_el_registro": [f["cve"] for f in filas if f["dias_publicacion_a_kev"] < 0],
            "mismo_dia": [f["cve"] for f in filas if f["dias_publicacion_a_kev"] == 0]}


def main() -> int:
    ruta = RAIZ / "knowledge" / "cve" / "2026-10" / "instantanea.json"
    filas = triaje_del_mes(ruta)
    print(json.dumps(resumen(filas), ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
