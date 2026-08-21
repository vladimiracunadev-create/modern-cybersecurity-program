#!/usr/bin/env python3
"""Genera el currículo embebido de la app móvil a partir de las clases.

Recorre ``classes/parte-*/NNN-*/README.md`` — la única fuente de verdad de las
340 clases — y escribe ``mobile/src/data/classes.js`` con estos exports:

    PARTS            — las 19 partes, con su rango de clases y nivel dominante
    CLASSES          — las 340 clases, planas y ordenadas por número
    CLASSES_BY_PART  — las mismas clases indexadas por slug de parte
    TOTAL_CLASSES / TOTAL_PARTS
    classesForPart(slug)

La app embebe este archivo en el bundle JS para que el temario funcione **sin
conexión**; lo único que necesita red son los enlaces "Abrir la clase" (sitio en
GitHub Pages) y "Ver en GitHub".

A diferencia del repo de data-science, aquí las clases son solo ``README.md`` (no
hay notebooks), así que cada clase enlaza a su página del sitio y a su fuente en
GitHub, no a Colab.

El parseo se ancla en el **emoji** del encabezado, no en su texto: el título de la
sección puede variar ("🧪 Laboratorio guiado — Diseña tu SOC") pero el emoji es
estable en las 340 clases. Vuelve a ejecutarlo tras cualquier edición del temario;
``--check`` falla (exit 1) si el archivo generado quedó desincronizado.

Uso:
    python scripts/generar_curriculum_movil.py            # (re)genera el archivo
    python scripts/generar_curriculum_movil.py --check    # solo verifica deriva
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSES_DIR = ROOT / "classes"
OUT_FILE = ROOT / "mobile" / "src" / "data" / "classes.js"

GITHUB_USER = "vladimiracunadev-create"
GITHUB_REPO = "modern-cybersecurity-program"
GITHUB_BRANCH = "main"
PAGES_BASE = f"https://{GITHUB_USER}.github.io/{GITHUB_REPO}"
GITHUB_BASE = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/blob/{GITHUB_BRANCH}"

# Foco de cada parte (tomado de la primera línea descriptiva de su README).
PART_SUBTITLE: dict[str, str] = {
    "parte-0-fundamentos-y-prerrequisitos": "Redes, SO, Linux, Windows, cripto base, Python ofensivo y laboratorio",
    "parte-1-redes-y-seguridad-de-redes": "Análisis de tráfico, escaneo, firewalls, IDS/IPS, VPN y monitoreo",
    "parte-2-criptografia-aplicada": "Simétrica, asimétrica, hashing, PKI, TLS y criptoanálisis",
    "parte-3-hacking-etico-y-pentesting-metodologia": "PTES, recon, enumeración, explotación, post-explotación y reporte",
    "parte-4-seguridad-de-aplicaciones-web": "OWASP Top 10, Burp Suite, inyecciones, XSS, SSRF, APIs y bug bounty",
    "parte-5-explotacion-de-sistemas-y-binarios": "Assembly, buffer overflows, ROP, heap, fuzzing e ingeniería inversa",
    "parte-6-analisis-de-malware": "Estático, dinámico, PE, unpacking, YARA y reporte",
    "parte-7-red-team-y-operaciones-ofensivas": "Adversary emulation, C2, evasión de EDR y Active Directory",
    "parte-8-blue-team-deteccion-y-soc": "SIEM, ingeniería de detección, threat hunting y SOAR",
    "parte-9-forense-digital-y-respuesta-a-incidentes": "DFIR, adquisición, memoria, timelines y playbooks",
    "parte-10-seguridad-en-la-nube-y-contenedores": "AWS, Azure, GCP, IAM, Docker, Kubernetes e IaC",
    "parte-11-devsecops-y-seguridad-del-sdlc": "Shift-left, threat modeling, SAST/DAST/SCA y supply chain",
    "parte-12-osint-e-ingenieria-social": "Inteligencia de fuentes abiertas, phishing y OPSEC personal",
    "parte-13-seguridad-movil-iot-e-inalambrica": "Android, iOS, firmware, hardware, SDR e ICS/SCADA",
    "parte-14-grc-riesgo-y-cumplimiento": "Gobernanza, ISO 27001, NIST, PCI-DSS, auditoría y carrera",
    "parte-15-seguridad-de-ia-y-machine-learning": "Ataques adversariales, OWASP LLM, prompt injection y defensa con IA",
    "parte-16-capstones-y-preparacion-de-certificaciones": "Roadmap OSCP/CISSP, proyectos integradores y aprendizaje continuo",
    "parte-17-profundizacion-para-certificaciones": "Gestión de datos, IAM, arquitectura, gestión de vulnerabilidades y gobierno",
    "parte-18-ia-aplicada-a-la-ciberseguridad": "LLMs y agentes: MCP, kali-mcp, pentesting asistido, defensa e informes",
}

# Título corto y legible de cada parte para la tarjeta del Home.
PART_SHORT: dict[str, str] = {
    "parte-0-fundamentos-y-prerrequisitos": "Fundamentos y prerrequisitos",
    "parte-1-redes-y-seguridad-de-redes": "Redes y seguridad de redes",
    "parte-2-criptografia-aplicada": "Criptografía aplicada",
    "parte-3-hacking-etico-y-pentesting-metodologia": "Hacking ético y pentesting",
    "parte-4-seguridad-de-aplicaciones-web": "Seguridad de aplicaciones web",
    "parte-5-explotacion-de-sistemas-y-binarios": "Explotación de sistemas y binarios",
    "parte-6-analisis-de-malware": "Análisis de malware",
    "parte-7-red-team-y-operaciones-ofensivas": "Red Team y operaciones ofensivas",
    "parte-8-blue-team-deteccion-y-soc": "Blue Team, detección y SOC",
    "parte-9-forense-digital-y-respuesta-a-incidentes": "Forense digital y respuesta a incidentes",
    "parte-10-seguridad-en-la-nube-y-contenedores": "Seguridad en la nube y contenedores",
    "parte-11-devsecops-y-seguridad-del-sdlc": "DevSecOps y seguridad del SDLC",
    "parte-12-osint-e-ingenieria-social": "OSINT e ingeniería social",
    "parte-13-seguridad-movil-iot-e-inalambrica": "Seguridad móvil, IoT e inalámbrica",
    "parte-14-grc-riesgo-y-cumplimiento": "GRC, riesgo y cumplimiento",
    "parte-15-seguridad-de-ia-y-machine-learning": "Seguridad de IA y machine learning",
    "parte-16-capstones-y-preparacion-de-certificaciones": "Capstones y certificaciones",
    "parte-17-profundizacion-para-certificaciones": "Profundización para certificaciones",
    "parte-18-ia-aplicada-a-la-ciberseguridad": "IA aplicada a la ciberseguridad",
}

# ── Regexes ──────────────────────────────────────────────────────────────────

TITLE_RE = re.compile(r"^#\s+Clase\s+(\d{1,3})\s*[—–-]\s*(.+)$", re.MULTILINE)
LEVEL_RE = re.compile(r"Nivel:\s*\*\*(.+?)\*\*")
DURATION_RE = re.compile(r"Duración estimada:\s*\*\*(.+?)\*\*")
PART_DIR_RE = re.compile(r"^parte-(\d+)")
CLASS_DIR_RE = re.compile(r"^(\d{1,3})-(.+)$")

LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
CODE_RE = re.compile(r"`([^`]+)`")
BULLET_RE = re.compile(r"^\s*(?:[-*]|\d+[.)])\s+(.*)$")


def strip_inline(text: str) -> str:
    """Aplana el markdown inline a texto plano (los <Text> de RN no lo renderizan)."""
    text = LINK_RE.sub(r"\1", text)
    text = BOLD_RE.sub(r"\1", text)
    text = ITALIC_RE.sub(r"\1", text)
    text = CODE_RE.sub(r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def section(body: str, emoji: str) -> str:
    """Cuerpo crudo de la sección ``## <emoji> ...``, anclada en el emoji."""
    pattern = re.compile(
        rf"^##\s+{re.escape(emoji)}[^\n]*\n(.*?)(?=^##\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(body)
    return match.group(1).strip() if match else ""


def list_items(block: str, limit: int | None = None) -> list[str]:
    """Extrae ítems de lista (con o sin numeración), ignorando continuaciones."""
    items: list[str] = []
    for line in block.splitlines():
        if line.startswith(("  ", "\t")):
            continue
        match = BULLET_RE.match(line)
        if not match:
            continue
        cleaned = strip_inline(match.group(1))
        if cleaned:
            items.append(cleaned)
    return items[:limit] if limit else items


def table_topics(block: str, limit: int | None = None) -> list[str]:
    """Columna "Tema" de la tabla ``| # | Tema | Por qué importa |``."""
    rows: list[str] = []
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) < 2:
            continue
        if set(cells[0]) <= set("-: "):
            continue  # separador
        if cells[0] in {"#", "Fase", "Componente"}:
            continue  # cabecera
        value = strip_inline(cells[1])
        if value:
            rows.append(value)
    return rows[:limit] if limit else rows


def first_sentence(text: str, max_len: int = 220) -> str:
    """Recorta un párrafo a una descripción de tarjeta."""
    text = strip_inline(text)
    match = re.search(r"^(.+?[.!?])(?:\s|$)", text)
    candidate = match.group(1) if match else text
    if len(candidate) > max_len:
        candidate = candidate[: max_len - 1].rstrip() + "…"
    return candidate


def paragraph(block: str, max_len: int = 600) -> str:
    """Colapsa un bloque a prosa plana, quitando la sintaxis de lista."""
    lines = [ln for ln in block.splitlines() if ln.strip()]
    text = strip_inline(" ".join(lines))
    if len(text) > max_len:
        text = text[: max_len - 1].rstrip() + "…"
    return text


def parse_class(part_slug: str, class_dir: str, md: str) -> dict:
    """Convierte el README de una clase en el objeto que consume la app."""
    title_match = TITLE_RE.search(md)
    if not title_match:
        raise ValueError(f"Sin título 'Clase NNN' en {part_slug}/{class_dir}")
    number = int(title_match.group(1))
    title = strip_inline(title_match.group(2))

    level_match = LEVEL_RE.search(md)
    level = level_match.group(1).strip() if level_match else "Intermedio"
    duration_match = DURATION_RE.search(md)
    duration = duration_match.group(1).strip() if duration_match else "—"

    objetivo = paragraph(section(md, "🎯"))
    outcomes = list_items(section(md, "📚"), limit=8)
    topics = table_topics(section(md, "🗺️"), limit=10)
    if not topics:  # la única clase sin tabla de Temas cae aquí
        topics = list_items(section(md, "🗺️"), limit=10)
    definitions = list_items(section(md, "📖"), limit=8)
    tools = list_items(section(md, "🧰"), limit=10)
    lab = paragraph(section(md, "🧪"), max_len=400)
    exercises = list_items(section(md, "✍️"), limit=10)

    class_path = f"classes/{part_slug}/{class_dir}"
    return {
        "id": f"{number:03d}-{class_dir}",
        "number": number,
        "partSlug": part_slug,
        "title": title,
        "level": level,
        "duration": duration,
        "description": first_sentence(objetivo) if objetivo else title,
        "theory": objetivo,
        "outcomes": outcomes,
        "topics": topics,
        "definitions": definitions,
        "tools": tools,
        "lab": lab,
        "exercises": exercises,
        "siteUrl": f"{PAGES_BASE}/{class_path}/README.html",
        "githubUrl": f"{GITHUB_BASE}/{class_path}/README.md",
    }


def collect() -> tuple[list[dict], list[dict]]:
    """Recorre classes/ y devuelve (partes, clases)."""
    part_dirs = sorted(
        (p for p in CLASSES_DIR.iterdir() if p.is_dir() and PART_DIR_RE.match(p.name)),
        key=lambda p: int(PART_DIR_RE.match(p.name).group(1)),
    )
    parts: list[dict] = []
    classes: list[dict] = []

    for part_dir in part_dirs:
        slug = part_dir.name
        part_number = int(PART_DIR_RE.match(slug).group(1))
        class_subdirs = sorted(
            (c for c in part_dir.iterdir() if c.is_dir() and CLASS_DIR_RE.match(c.name)),
            key=lambda c: int(CLASS_DIR_RE.match(c.name).group(1)),
        )
        part_classes: list[dict] = []
        for class_dir in class_subdirs:
            readme = class_dir / "README.md"
            if not readme.exists():
                continue
            data = parse_class(slug, class_dir.name, readme.read_text(encoding="utf-8"))
            data["partNumber"] = part_number
            part_classes.append(data)
            classes.append(data)

        if not part_classes:
            continue
        numbers = [c["number"] for c in part_classes]
        level_mode = Counter(c["level"] for c in part_classes).most_common(1)[0][0]
        parts.append(
            {
                "id": slug,
                "number": part_number,
                "title": PART_SHORT.get(slug, slug),
                "subtitle": PART_SUBTITLE.get(slug, ""),
                "level": level_mode,
                "classCount": len(part_classes),
                "firstClass": min(numbers),
                "lastClass": max(numbers),
            }
        )

    classes.sort(key=lambda c: c["number"])
    return parts, classes


def render(parts: list[dict], classes: list[dict]) -> str:
    """Genera el contenido de mobile/src/data/classes.js."""
    def dump(obj) -> str:
        return json.dumps(obj, ensure_ascii=False, indent=2)

    header = (
        "// ============================================================\n"
        "// GENERADO AUTOMÁTICAMENTE — NO EDITAR A MANO\n"
        "// Fuente: classes/parte-*/NNN-*/README.md\n"
        "// Regenera con:  python scripts/generar_curriculum_movil.py\n"
        "// Verifica con:  python scripts/generar_curriculum_movil.py --check\n"
        "// ============================================================\n\n"
    )
    body = (
        f"export const PARTS = {dump(parts)};\n\n"
        f"export const CLASSES = {dump(classes)};\n\n"
        "// Índice por parte derivado en runtime (evita duplicar los objetos de clase).\n"
        "export const CLASSES_BY_PART = CLASSES.reduce((acc, c) => {\n"
        "  (acc[c.partSlug] = acc[c.partSlug] || []).push(c);\n"
        "  return acc;\n"
        "}, {});\n\n"
        f"export const TOTAL_CLASSES = {len(classes)};\n"
        f"export const TOTAL_PARTS = {len(parts)};\n\n"
        "export const classesForPart = (partSlug) => CLASSES_BY_PART[partSlug] || [];\n"
    )
    return header + body


def main() -> int:
    check = "--check" in sys.argv
    parts, classes = collect()
    content = render(parts, classes)

    if check:
        if not OUT_FILE.exists():
            print(f"FALLA: no existe {OUT_FILE.relative_to(ROOT)} — ejecuta el generador.")
            return 1
        actual = OUT_FILE.read_text(encoding="utf-8")
        if actual != content:
            print("FALLA: mobile/src/data/classes.js está desincronizado con las clases.")
            print("       Ejecuta: python scripts/generar_curriculum_movil.py")
            return 1
        print(f"OK: {len(classes)} clases en {len(parts)} partes; datos embebidos al día.")
        return 0

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUT_FILE.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)
    print(f"Generado {OUT_FILE.relative_to(ROOT)}: {len(classes)} clases en {len(parts)} partes.")
    empty = [c["id"] for c in classes if not c["theory"] or not c["outcomes"]]
    if empty:
        print(f"AVISO: {len(empty)} clases sin objetivo o sin resultados: {empty[:5]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
