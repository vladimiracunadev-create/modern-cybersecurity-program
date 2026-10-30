#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Herramienta local para estudiar y consultar MITRE CWE sin conexión.

Primera vez (requiere red una sola vez, o un ZIP ya descargado):

    python scripts/cwe_kb.py importar --descargar
    python scripts/cwe_kb.py importar --zip cwec_latest.xml.zip

Después todo funciona sin red:

    python scripts/cwe_kb.py mostrar CWE-89              # ficha técnica de una debilidad
    python scripts/cwe_kb.py buscar "use after free"     # por nombre o descripción (inglés)
    python scripts/cwe_kb.py buscar "inyección sql"      # también por alias en español
    python scripts/cwe_kb.py relaciones CWE-89           # padres, hijos y vecinos
    python scripts/cwe_kb.py mitigaciones CWE-89         # cómo se corrige y cómo se detecta
    python scripts/cwe_kb.py clases CWE-89               # dónde se estudia en este programa
    python scripts/cwe_kb.py ficha CWE-89 --salida f.md  # ficha de estudio en Markdown
    python scripts/cwe_kb.py exportar --formato csv --vista 1435
    python scripts/cwe_kb.py sast bandit.json            # hallazgos SAST -> CWE oficial

Mantenimiento del programa:

    python scripts/cwe_kb.py validar                     # datos, mapa curricular y referencias
    python scripts/cwe_kb.py referencias                 # CWE inválidos u obsoletos en el temario
    python scripts/cwe_kb.py cobertura --escribir        # regenera docs/matriz-cobertura-cwe.md
    python scripts/cwe_kb.py cobertura --check           # falla si la matriz está desactualizada
    python scripts/cwe_kb.py enlaces [--red]             # valida URLs de cwe.mitre.org

Solo biblioteca estándar; no exige claves ni servicios de pago.
Código de salida 0 = correcto, 1 = hay errores (para CI).
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import cwe_analisis as A  # noqa: E402
import cwe_lib as L  # noqa: E402

MATRIZ = L.RAIZ / "docs" / "matriz-cobertura-cwe.md"
# Partes donde la integración con CWE es obligatoria: aplicaciones web, explotación,
# DevSecOps y la profundización para certificaciones.
PARTES_CON_DEBILIDADES = (4, 5, 11, 17)


# --------------------------------------------------------------------------
# Utilidades de salida
# --------------------------------------------------------------------------
def _cargar() -> L.BaseCWE:
    try:
        return L.BaseCWE.cargar()
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)


def _resolver(base: L.BaseCWE, valor: str) -> dict:
    try:
        return base.obtener(valor)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
    except KeyError as exc:
        print(f"ERROR: {exc.args[0]}", file=sys.stderr)
    raise SystemExit(1)


def _sangrar(texto: str, n: int = 4) -> str:
    return "\n".join(" " * n + ln for ln in texto.splitlines())


def _linea_id(e: dict) -> str:
    etiqueta = e["abstraccion"] or e["tipo"]
    marca = " [OBSOLETO]" if e["estado"] == "Deprecated" else ""
    return f"{e['id']:<9} {etiqueta:<9} {e['nombre']}{marca}"


def _alias_es(mapa: dict) -> dict[str, list[str]]:
    return {cid: d.get("alias_es", []) for cid, d in mapa.get("entradas", {}).items() if d.get("alias_es")}


# --------------------------------------------------------------------------
# Comandos
# --------------------------------------------------------------------------
def cmd_importar(a: argparse.Namespace) -> int:
    ruta = Path(a.zip) if a.zip else L.ORIGINAL / "cwec_latest.xml.zip"
    if a.descargar:
        print(f"Descargando {L.URL_CATALOGO} ...")
        try:
            sha = L.descargar(L.URL_CATALOGO, ruta)
        except RuntimeError as exc:
            print(f"ERROR: {exc}\nSin red, descarga el ZIP a mano y usa `importar --zip RUTA`.", file=sys.stderr)
            return 1
        print(f"  SHA-256: {sha}")
    elif not ruta.is_file():
        print(f"ERROR: no existe {ruta}. Usa --descargar o --zip RUTA.", file=sys.stderr)
        return 1
    try:
        res = L.importar(ruta, forzar=a.forzar)
    except (ValueError, zipfile_error()) as exc:
        print(f"ERROR al importar: {exc}", file=sys.stderr)
        return 1
    if res["estado"] == "sin_cambios":
        print(f"Sin cambios: el ZIP (SHA-256 {res['sha256_zip'][:12]}…) ya está importado como CWE {res['version']}.")
        return 0
    c, cat = res["cambios"], res["catalogo"]
    print(f"Importado CWE {cat['version']} ({cat['fecha']}): {cat['entradas']} entradas, {cat['vistas']} vistas.")
    print(f"  Respecto a la importación anterior: +{c['anadidas']} añadidas, -{c['eliminadas']} eliminadas, ~{c['modificadas']} modificadas.")
    print("  Por tipo:", ", ".join(f"{k} {v}" for k, v in cat["por_tipo"].items()))
    print("Ejecuta `validar` y, si cambió el catálogo, `cobertura --escribir`.")
    return 0


def zipfile_error():
    import zipfile
    return zipfile.BadZipFile


def cmd_indices(_: argparse.Namespace) -> int:
    base = _cargar()
    huellas = L.construir_indices(list(base.entradas.values()))
    proc = L.leer_procedencia()
    if proc:
        proc["huellas"].update(huellas)
        proc["huellas"] = dict(sorted(proc["huellas"].items()))
        L._escribir(L.PROCEDENCIA, json.dumps(proc, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    print(f"Índices regenerados: {', '.join(sorted(huellas))}")
    return 0


def cmd_mostrar(a: argparse.Namespace) -> int:
    base = _cargar()
    e = _resolver(base, a.id)
    if a.json:
        print(json.dumps(e, ensure_ascii=False, indent=2))
        return 0
    print(_linea_id(e))
    print(f"Estado: {e['estado']}  |  Estructura: {e['estructura'] or '-'}  |  Vistas: {', '.join(e.get('vistas', [])) or '-'}")
    print(f"URL oficial: https://cwe.mitre.org/data/definitions/{L.numero(e['id'])}.html")
    print("\nDescripción (MITRE, en inglés):")
    print(_sangrar(e["descripcion"]))
    if e.get("descripcion_extendida"):
        print("\nDescripción extendida:")
        print(_sangrar(e["descripcion_extendida"]))
    if e.get("consecuencias"):
        print("\nConsecuencias técnicas:")
        for c in e["consecuencias"]:
            print(f"  - {'/'.join(c['ambitos'])}: {'; '.join(c['impactos'])}")
    if e["notas_mapeo"].get("uso"):
        print(f"\nUso para mapear vulnerabilidades: {e['notas_mapeo']['uso']}")
        if e["notas_mapeo"].get("razon"):
            print(_sangrar(e["notas_mapeo"]["razon"]))
    if e.get("probabilidad_explotacion"):
        print(f"\nProbabilidad de explotación (MITRE): {e['probabilidad_explotacion']}")
    return 0


def cmd_buscar(a: argparse.Namespace) -> int:
    base = _cargar()
    mapa = A.cargar_mapa()
    resultados = base.buscar(a.consulta, tipo=a.tipo, abstraccion=a.abstraccion,
                             incluir_obsoletas=a.obsoletas, limite=a.limite)
    # Alias en español del mapa curricular (el catálogo de MITRE solo está en inglés).
    consulta_norm = L.sin_acentos(a.consulta)
    vistos = {e["id"] for _, e in resultados}
    for cid, alias in _alias_es(mapa).items():
        if cid in base and cid not in vistos and any(consulta_norm in L.sin_acentos(x) or L.sin_acentos(x) in consulta_norm for x in alias):
            resultados.append((50, base.obtener(cid)))
    resultados.sort(key=lambda x: (-x[0], L.numero(x[1]["id"])))
    resultados = resultados[: a.limite]
    if not resultados:
        print("Sin resultados. El catálogo está en inglés: prueba con el término técnico (p. ej. «injection», «overflow»).")
        return 1
    for puntos, e in resultados:
        print(_linea_id(e))
    return 0


def cmd_relaciones(a: argparse.Namespace) -> int:
    base = _cargar()
    e = _resolver(base, a.id)
    print(_linea_id(e))
    print(f"\nPadres (vista {L.VISTA_JERARQUIA}, Research Concepts):")
    for p in base.padres(e["id"]) or []:
        print(f"  ↑ {_linea_id(base.obtener(p)) if p in base else p}")
    if not base.padres(e["id"]):
        print("  (ninguno: es raíz de la jerarquía)")
    print("\nCaminos hasta la raíz:")
    for camino in base.ancestros(e["id"]):
        print("  " + "  →  ".join(camino))
    print(f"\nHijos (profundidad {a.profundidad}):")
    desc = base.descendientes(e["id"], a.profundidad)
    for cid, nivel in desc.items():
        print(f"  {'  ' * (nivel - 1)}↓ {_linea_id(base.obtener(cid))}")
    if not desc:
        print("  (ninguno)")
    otras = [r for r in base.relaciones(e["id"]) if not (r["vista"] == L.VISTA_JERARQUIA and r["naturaleza"] == "ChildOf")]
    if otras:
        print("\nOtras relaciones declaradas en esta entrada:")
        for r in otras:
            nombre = base.entradas[r["id"]]["nombre"] if r["id"] in base else "?"
            print(f"  {r['naturaleza']:<12} {r['id']:<9} {nombre}   (vista {r['vista']})")
    return 0


def cmd_miembros(a: argparse.Namespace) -> int:
    """Miembros de una vista (p. ej. 1435) o de una agrupación (p. ej. CWE-1440, OWASP A05:2025)."""
    base = _cargar()
    if a.id in base.vistas:
        v = base.vista(a.id)
        print(f"Vista {v['id']} ({v['tipo']}, {v['estado']}): {v['nombre']}")
        for m in v["miembros"]:
            print("  " + (_linea_id(base.obtener(m)) if m in base else m))
        if not v["miembros"]:
            print("  (vista implícita: sin lista de miembros; se define por un filtro)" + (f" {v['filtro']}" if v["filtro"] else ""))
        return 0
    e = _resolver(base, a.id)
    miembros = [r for r in e.get("relaciones", []) if r["naturaleza"] == "Has_Member"]
    if not miembros:
        print(f"{e['id']} no tiene miembros declarados (¿es una debilidad? usa `relaciones`).")
        return 1
    print(_linea_id(e))
    for r in miembros:
        print("  " + (_linea_id(base.obtener(r["id"])) if r["id"] in base else r["id"]))
    print(f"\n{len(miembros)} miembro(s). Una agrupación NO se usa para mapear vulnerabilidades: agrupa entradas.")
    return 0


def _cargar_top25() -> dict:
    if not L.TOP25_JSON.is_file():
        print("ERROR: no hay Top 25 local. Ejecuta `python scripts/cwe_kb.py top25 --descargar`.", file=sys.stderr)
        raise SystemExit(1)
    return json.loads(L.TOP25_JSON.read_text(encoding="utf-8"))


def cmd_top25(a: argparse.Namespace) -> int:
    if a.descargar:
        try:
            peticion = urllib.request.Request(L.URL_TOP25, headers={"User-Agent": "modern-cybersecurity-program/cwe-kb"})
            with urllib.request.urlopen(peticion, timeout=60) as r:
                crudo = r.read().decode("utf-8", "replace")
            doc = L.importar_top25(crudo)
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 1
        print(f"Top 25 guardado ({doc['pagina_actualizada']}).")
    doc = _cargar_top25()
    base = _cargar()
    owasp = {}
    for i in range(1436, 1446):
        g = base.entradas.get(f"CWE-{i}")
        if g:
            for r in g["relaciones"]:
                if r["naturaleza"] == "Has_Member":
                    owasp.setdefault(r["id"], g["nombre"].split(" - ")[0].split()[-1])
    print(f"{doc['lista']}  (página actualizada: {doc['pagina_actualizada']})\n")
    print(f"{'#':>2}  {'CWE':<8} {'Puntos':>6} {'KEV':>4}  {'OWASP 2025':<8} Nombre")
    for e in doc["entradas"]:
        print(f"{e['rango']:>2}  {e['id']:<8} {e['puntuacion']:>6} {e['cves_en_kev']:>4}  {owasp.get(e['id'], '—'):<8} {e['nombre'][:70]}")
    print("\nOWASP 2025: categoría del catálogo CWE 5.0 a la que pertenece (— = ninguna: p. ej. la memoria queda fuera del Top 10 web).")
    return 0


def cmd_mitigaciones(a: argparse.Namespace) -> int:
    base = _cargar()
    e = _resolver(base, a.id)
    print(_linea_id(e))
    if e["tipo"] != "weakness":
        print("Esta entrada es una agrupación: no tiene mitigaciones propias. Consulta sus miembros con `relaciones`.")
        return 0
    print("\nMitigaciones potenciales (MITRE):")
    if not e["mitigaciones"]:
        print("  (el catálogo no registra mitigaciones para esta entrada)")
    for m in e["mitigaciones"]:
        cab = f"[{', '.join(m['fases'])}]" + (f" {m['estrategia']}" if m["estrategia"] else "")
        ef = f"  (efectividad: {m['efectividad']})" if m["efectividad"] else ""
        print(f"\n  {cab}{ef}")
        print(_sangrar(m["descripcion"], 4))
    print("\nMétodos de detección (MITRE):")
    if not e["deteccion"]:
        print("  (el catálogo no registra métodos de detección)")
    for d in e["deteccion"]:
        ef = f" — efectividad: {d['efectividad']}" if d["efectividad"] else ""
        print(f"  - {d['metodo']}{ef}")
    return 0


def cmd_clases(a: argparse.Namespace) -> int:
    base = _cargar()
    e = _resolver(base, a.id)
    mapa = A.cargar_mapa().get("entradas", {}).get(e["id"], {})
    print(_linea_id(e))
    if mapa:
        for etiqueta, clave in (("Teoría", "teoria"), ("Ejercicio", "ejercicio")):
            for n in mapa.get(clave, []):
                d = A.directorio_clase(n)
                print(f"  {etiqueta:<10} clase {n:03d}  {d.relative_to(L.RAIZ).as_posix() if d else '(no existe)'}")
        for lab in mapa.get("laboratorio", []):
            print(f"  Laboratorio {lab}")
        for p in mapa.get("prueba", []):
            print(f"  Prueba      {p}")
        if mapa.get("mitigacion"):
            print(f"  Corrección enseñada: {mapa['mitigacion']}")
    else:
        print("  (no está en el mapa curricular)")
    menciones = [m for m in A.escanear_menciones() if m.cwe == e["id"]]
    print(f"\nApariciones del identificador en el repositorio: {len(menciones)}")
    for arch in sorted({m.archivo for m in menciones}):
        print(f"  {arch}")
    return 0


def _ficha_md(base: L.BaseCWE, e: dict, mapa: dict) -> str:
    cid, num = e["id"], L.numero(e["id"])
    s = [f"# {cid} — {e['nombre']}", ""]
    s.append(f"> Ficha de estudio generada desde el catálogo local (CWE {L.leer_procedencia().get('catalogo', {}).get('version', '?')}). "
             "El texto marcado como *MITRE* está en inglés y es de The MITRE Corporation; ver `knowledge/cwe/LICENCIA-MITRE.md`.")
    s += ["", f"**Tipo:** {e['abstraccion'] or e['tipo']} · **Estado:** {e['estado']} · **Oficial:** <https://cwe.mitre.org/data/definitions/{num}.html>", ""]
    if mapa.get("alias_es"):
        s += [f"**En español:** {', '.join(mapa['alias_es'])}", ""]
    s += ["## Qué es (MITRE)", "", e["descripcion"] or "_Sin descripción._", ""]
    if e.get("descripcion_extendida"):
        s += [e["descripcion_extendida"], ""]
    if e.get("introduccion"):
        s += ["## Por qué ocurre: cuándo se introduce", ""]
        s += [f"- **{i['fase']}.** {i['nota']}".rstrip() for i in e["introduccion"]] + [""]
    if e.get("consecuencias"):
        s += ["## Consecuencias técnicas", ""]
        s += [f"- **{', '.join(c['ambitos'])}** → {'; '.join(c['impactos'])}" + (f". {c['nota']}" if c["nota"] else "") for c in e["consecuencias"]] + [""]
    if e.get("deteccion"):
        s += ["## Cómo se detecta", ""]
        s += [f"- {d['metodo']}" + (f" (efectividad: {d['efectividad']})" if d["efectividad"] else "") for d in e["deteccion"]] + [""]
    if e.get("mitigaciones"):
        s += ["## Cómo se corrige (mitigaciones de MITRE)", ""]
        for m in e["mitigaciones"]:
            cab = ", ".join(m["fases"]) + (f" · {m['estrategia']}" if m["estrategia"] else "")
            s.append(f"- **{cab}.** {m['descripcion'].splitlines()[0] if m['descripcion'] else ''}")
        s.append("")
    padres = base.padres(cid)
    hijos = base.hijos(cid)
    if padres or hijos:
        s += ["## Relaciones (jerarquía Research Concepts)", ""]
        if padres:
            s.append("- **Padres:** " + ", ".join(f"{p} {base.entradas[p]['nombre']}" for p in padres if p in base))
        if hijos:
            s.append("- **Hijos:** " + ", ".join(f"{h} {base.entradas[h]['nombre']}" for h in hijos[:12]) + (" …" if len(hijos) > 12 else ""))
        s.append("")
    ejemplos = [x for x in e.get("ejemplos_observados", []) if x["referencia"].startswith("CVE-")]
    if ejemplos:
        s += ["## Vulnerabilidades reales que MITRE cita como ejemplos observados", "",
              "MITRE enlaza cada CVE a esta debilidad; es una correspondencia curada por el catálogo, no una inferencia de este programa. "
              "Para su CVSS, EPSS o presencia en KEV hay que consultar las fuentes vigentes: cambian con el tiempo.", ""]
        s += [f"- [{x['referencia']}](https://www.cve.org/CVERecord?id={x['referencia']}) — {x['descripcion']}" for x in ejemplos[:8]] + [""]
    s += ["## Dónde se estudia en este programa", ""]
    if mapa:
        for n in mapa.get("teoria", []):
            d = A.directorio_clase(n)
            s.append(f"- Teoría: clase {n:03d}" + (f" — `{d.relative_to(L.RAIZ).as_posix()}`" if d else ""))
        for n in mapa.get("ejercicio", []):
            s.append(f"- Práctica: clase {n:03d}")
        for lab in mapa.get("laboratorio", []):
            s.append(f"- Laboratorio: `{lab}`")
        if mapa.get("mitigacion"):
            s += ["", f"**Corrección que se enseña:** {mapa['mitigacion']}"]
        if mapa.get("prueba"):
            s += ["", "**Cómo se verifica la corrección:** " + ", ".join(f"`{p}`" for p in mapa["prueba"])]
    else:
        s.append("- Esta debilidad aún no está en el mapa curricular.")
    return "\n".join(s) + "\n"


def cmd_ficha(a: argparse.Namespace) -> int:
    base = _cargar()
    e = _resolver(base, a.id)
    mapa = A.cargar_mapa().get("entradas", {}).get(e["id"], {})
    md = _ficha_md(base, e, mapa)
    if a.salida:
        Path(a.salida).write_text(md, encoding="utf-8", newline="\n")
        print(f"Ficha escrita en {a.salida}")
    else:
        print(md)
    return 0


def cmd_exportar(a: argparse.Namespace) -> int:
    base = _cargar()
    entradas = list(base.entradas.values())
    if a.vista:
        miembros = set(base.vista(a.vista)["miembros"])
        entradas = [e for e in entradas if e["id"] in miembros]
    if a.ids:
        pedidos = {L.normalizar_id(x) for x in a.ids}
        entradas = [e for e in entradas if e["id"] in pedidos]
    if a.tipo:
        entradas = [e for e in entradas if e["tipo"] == a.tipo]
    if not a.obsoletas:
        entradas = [e for e in entradas if e["estado"] != "Deprecated"]
    entradas.sort(key=lambda e: L.numero(e["id"]))
    if a.formato == "json":
        salida = json.dumps(entradas, ensure_ascii=False, indent=1)
    elif a.formato == "jsonl":
        salida = "\n".join(L.serializar(e) for e in entradas) + "\n"
    elif a.formato == "csv":
        salida = A.exportar_csv(entradas)
    else:
        salida = "| CWE | Tipo | Nombre |\n|---|---|---|\n" + "\n".join(
            f"| {e['id']} | {e['abstraccion'] or e['tipo']} | {e['nombre'].replace('|', chr(92) + '|')} |" for e in entradas) + "\n"
    if a.salida:
        Path(a.salida).write_text(salida, encoding="utf-8", newline="\n")
        print(f"{len(entradas)} entradas escritas en {a.salida}")
    else:
        print(salida, end="")
    return 0


def cmd_sast(a: argparse.Namespace) -> int:
    base = _cargar()
    try:
        datos = json.loads(Path(a.archivo).read_text(encoding="utf-8"))
        hallazgos = A.leer_hallazgos_sast(datos)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    filas = A.anotar_hallazgos(base, hallazgos)
    if a.mapa:
        try:
            filas = A.contrastar_con_mapa(filas, json.loads(Path(a.mapa).read_text(encoding="utf-8")))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERROR al leer el mapa: {exc}", file=sys.stderr)
            return 1
    if a.json:
        print(json.dumps(filas, ensure_ascii=False, indent=2))
        return 0
    print(f"{len(filas)} hallazgo(s) de {', '.join(sorted({f['herramienta'] for f in filas})) or '—'}\n")
    for f in filas:
        cw = ", ".join(f"{c['id']} ({c['nombre']})" for c in f["cwe"]) or "sin CWE"
        print(f"{f['archivo']}:{f['linea']}  [{f['severidad'] or '-'}]  {f['regla']}")
        print(f"    CWE: {cw}")
        for av in f["avisos"]:
            print(f"    ! {av}")
        c = f.get("contraste")
        if c and c["estado"] == "coincide":
            print(f"    = coincide con el mapa del laboratorio ({c['vulnerabilidad']})")
        elif c:
            etiqueta = "válido pero menos específico" if c["estado"] == "valido_pero_no_el_mas_especifico" else "DIFIERE"
            print(f"    ≠ {etiqueta}: el mapa recomienda {c['recomendado']} para «{c['vulnerabilidad']}»")
            if c["motivo"]:
                print(f"      {c['motivo']}")
    sin = sum(1 for f in filas if not f["cwe"])
    if sin:
        print(f"\n{sin} hallazgo(s) sin CWE: la herramienta no los clasifica; asígnalos tú tras leer el código.")
    return 0


def _imprimir_hallazgos(hs: list[A.Hallazgo]) -> None:
    for h in hs:
        print(f"  [{h.gravedad}] {h.archivo}:{h.linea}  {h.mensaje}")


def cmd_validar(_: argparse.Namespace) -> int:
    res = A.validar_base()
    base = None
    if res.correcto:
        base = L.BaseCWE.cargar()
        mapa_res = A.validar_mapa(base)
        res.errores += mapa_res.errores
        res.comprobaciones += mapa_res.comprobaciones
        refs = A.auditar_referencias(base, A.escanear_menciones()) + A.auditar_urls(base)
        errores_ref = [h for h in refs if h.gravedad == "error"]
        res.comprobaciones.append(("referencias CWE del temario válidas y vigentes", not errores_ref, f"{len(errores_ref)} error(es)"))
        res.errores += [f"{h.archivo}:{h.linea} {h.mensaje}" for h in errores_ref]
        res.avisos += [f"{h.archivo}:{h.linea} {h.mensaje}" for h in refs if h.gravedad == "aviso"]
    print("== Validación de la base de conocimiento CWE ==")
    for nombre, ok, detalle in res.comprobaciones:
        print(f"  [{'OK ' if ok else 'FALLO'}] {nombre}" + (f" — {detalle}" if (not ok and detalle) else ""))
    for av in res.avisos:
        print(f"  [aviso] {av}")
    if res.errores:
        print(f"\nFALLO: {len(res.errores)} problema(s).")
        return 1
    print(f"\nOK: {len(res.comprobaciones)} comprobaciones correctas.")
    return 0


def cmd_referencias(_: argparse.Namespace) -> int:
    base = _cargar()
    hs = A.auditar_referencias(base, A.escanear_menciones()) + A.auditar_urls(base)
    if not hs:
        print("OK: todas las referencias CWE del temario existen, están vigentes y son coherentes.")
        return 0
    _imprimir_hallazgos(hs)
    return 1 if any(h.gravedad == "error" for h in hs) else 0


def cmd_cobertura(a: argparse.Namespace) -> int:
    base = _cargar()
    menciones = A.escanear_menciones()
    filas = A.cobertura(base, menciones=menciones)
    fuera = A.cwe_mencionados_fuera_de_objetivo(base, filas, menciones)
    huecos = A.clases_sin_cwe(PARTES_CON_DEBILIDADES, menciones)
    md = A.render_matriz(base, filas, fuera, huecos)
    if a.escribir:
        MATRIZ.write_text(md, encoding="utf-8", newline="\n")
        print(f"Matriz escrita en {MATRIZ.relative_to(L.RAIZ).as_posix()} ({len(filas)} CWE objetivo).")
    elif a.check:
        actual = MATRIZ.read_text(encoding="utf-8").replace("\r\n", "\n") if MATRIZ.is_file() else ""
        if actual != md:
            print("FALLO: docs/matriz-cobertura-cwe.md está desactualizada. Ejecuta `python scripts/cwe_kb.py cobertura --escribir`.")
            return 1
        print("OK: la matriz de cobertura está al día.")
        return 0
    resumen = {est: sum(1 for f in filas if f["estado"] == est) for est in ("Completo", "Parcial", "Pendiente")}
    print(f"CWE objetivo: {len(filas)} — " + ", ".join(f"{k} {v}" for k, v in resumen.items()))
    if a.huecos:
        print("\nCWE objetivo sin explicar:")
        for f in filas:
            if not f["teoria"]:
                print(f"  {f['id']:<9} {f['nombre']}  [{f['nivel_cobertura']}]")
        print(f"\nClases de las partes {PARTES_CON_DEBILIDADES} que no citan ningún CWE: {len(huecos)}")
        for h in huecos:
            print(f"  {h}")
    return 0


def _head(url: str, timeout: int = 20) -> int:
    peticion = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "modern-cybersecurity-program/cwe-kb"})
    try:
        with urllib.request.urlopen(peticion, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as exc:
        return exc.code
    except (urllib.error.URLError, TimeoutError, OSError):
        return 0


def cmd_enlaces(a: argparse.Namespace) -> int:
    base = _cargar()
    hs = A.auditar_urls(base)
    urls: set[str] = set()
    for ruta, rel in A.iter_archivos():
        if ruta.suffix == ".md":
            try:
                urls |= {f"https://cwe.mitre.org/data/definitions/{m.group(1)}.html" for m in A.URL_RE.finditer(ruta.read_text(encoding="utf-8"))}
            except (UnicodeDecodeError, OSError):
                pass
    print(f"{len(urls)} URL(s) distintas de cwe.mitre.org/data/definitions en el temario.")
    if hs:
        _imprimir_hallazgos(hs)
    if a.red:
        malas = []
        for u in sorted(urls):
            codigo = _head(u)
            if codigo != 200:
                malas.append((u, codigo))
        if not urls:
            pass
        elif malas:
            for u, c in malas:
                print(f"  [red] {u} -> {c or 'sin respuesta'}")
        else:
            print("OK: todas responden 200.")
        if malas and all(c == 0 for _, c in malas):
            print("(Ninguna respondió: probablemente no hay conectividad; no se considera fallo del temario.)")
            return 1 if hs else 0
        return 1 if (hs or malas) else 0
    return 1 if hs else 0


def cmd_procedencia(_: argparse.Namespace) -> int:
    p = L.leer_procedencia()
    if not p:
        print("No hay procedencia registrada: aún no se ha importado el catálogo.")
        return 1
    print(json.dumps({k: p[k] for k in ("origen", "catalogo", "ultima_actualizacion")}, ensure_ascii=False, indent=2))
    return 0


# --------------------------------------------------------------------------
def construir_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cwe_kb.py", description="Base de conocimiento local de MITRE CWE para el programa.")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("importar", help="importa el catálogo oficial (ZIP) a la base local")
    s.add_argument("--zip", help="ruta a un cwec_latest.xml.zip ya descargado")
    s.add_argument("--descargar", action="store_true", help="descarga el ZIP oficial de cwe.mitre.org")
    s.add_argument("--forzar", action="store_true", help="reimporta aunque el SHA-256 no haya cambiado")
    s.set_defaults(f=cmd_importar)

    sub.add_parser("indices", help="regenera los índices desde lo normalizado").set_defaults(f=cmd_indices)

    s = sub.add_parser("mostrar", help="ficha técnica de un CWE")
    s.add_argument("id"); s.add_argument("--json", action="store_true"); s.set_defaults(f=cmd_mostrar)

    s = sub.add_parser("buscar", help="busca por nombre, descripción o alias en español")
    s.add_argument("consulta"); s.add_argument("--tipo", choices=["weakness", "grouping"])
    s.add_argument("--abstraccion", choices=["Pillar", "Class", "Base", "Variant", "Compound"])
    s.add_argument("--obsoletas", action="store_true"); s.add_argument("--limite", type=int, default=25)
    s.set_defaults(f=cmd_buscar)

    s = sub.add_parser("relaciones", help="padres, hijos y relaciones de un CWE")
    s.add_argument("id"); s.add_argument("--profundidad", type=int, default=1); s.set_defaults(f=cmd_relaciones)

    s = sub.add_parser("miembros", help="miembros de una vista (1435) o de una agrupación (CWE-1440)")
    s.add_argument("id"); s.set_defaults(f=cmd_miembros)

    s = sub.add_parser("top25", help="CWE Top 25 de 2025 con puntuación, KEV y categoría OWASP")
    s.add_argument("--descargar", action="store_true", help="actualiza el ranking desde cwe.mitre.org (requiere red)")
    s.set_defaults(f=cmd_top25)

    s = sub.add_parser("mitigaciones", help="mitigaciones y métodos de detección")
    s.add_argument("id"); s.set_defaults(f=cmd_mitigaciones)

    s = sub.add_parser("clases", help="dónde se estudia un CWE en este programa")
    s.add_argument("id"); s.set_defaults(f=cmd_clases)

    s = sub.add_parser("ficha", help="ficha de estudio en Markdown")
    s.add_argument("id"); s.add_argument("--salida"); s.set_defaults(f=cmd_ficha)

    s = sub.add_parser("exportar", help="exporta entradas a json, jsonl, csv o md")
    s.add_argument("--formato", choices=["json", "jsonl", "csv", "md"], default="json")
    s.add_argument("--vista", help="solo los miembros de esta vista (p. ej. 1435 = Top 25 de 2025)")
    s.add_argument("--ids", nargs="+"); s.add_argument("--tipo", choices=["weakness", "grouping"])
    s.add_argument("--obsoletas", action="store_true"); s.add_argument("--salida")
    s.set_defaults(f=cmd_exportar)

    s = sub.add_parser("sast", help="relaciona hallazgos de Bandit, Semgrep o SARIF con CWE")
    s.add_argument("archivo"); s.add_argument("--json", action="store_true")
    s.add_argument("--mapa", help="cwe-map.json de un laboratorio: contrasta cada hallazgo con el CWE recomendado")
    s.set_defaults(f=cmd_sast)

    sub.add_parser("validar", help="valida datos, mapa curricular y referencias").set_defaults(f=cmd_validar)
    sub.add_parser("referencias", help="detecta CWE inválidos u obsoletos en el temario").set_defaults(f=cmd_referencias)

    s = sub.add_parser("cobertura", help="calcula la cobertura curricular y genera la matriz")
    g = s.add_mutually_exclusive_group()
    g.add_argument("--escribir", action="store_true", help="regenera docs/matriz-cobertura-cwe.md")
    g.add_argument("--check", action="store_true", help="falla si la matriz está desactualizada")
    s.add_argument("--huecos", action="store_true", help="lista lo que falta cubrir")
    s.set_defaults(f=cmd_cobertura)

    s = sub.add_parser("enlaces", help="valida URLs de cwe.mitre.org del temario")
    s.add_argument("--red", action="store_true", help="comprueba además que respondan (requiere conexión)")
    s.set_defaults(f=cmd_enlaces)

    sub.add_parser("procedencia", help="muestra origen y versión del catálogo importado").set_defaults(f=cmd_procedencia)
    return p


def main(argv: list[str] | None = None) -> int:
    L.configurar_salida()
    args = construir_parser().parse_args(argv)
    return args.f(args)


if __name__ == "__main__":
    sys.exit(main())
