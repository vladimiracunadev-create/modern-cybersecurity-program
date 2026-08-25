#!/usr/bin/env python3
"""Genera el currículo embebido de la app móvil a partir de las clases.

Recorre ``classes/parte-*/NNN-*/README.md`` — la única fuente de verdad de las
340 clases — y escribe ``mobile/src/data/classes.js`` con estos exports:

    PARTS            — las 19 partes, con su rango de clases y nivel dominante
    CLASSES          — las 340 clases, planas y ordenadas por número
    CLASSES_BY_PART  — las mismas clases indexadas por slug de parte
    TOTAL_CLASSES / TOTAL_PARTS
    classesForPart(slug)

La app embebe este archivo en el bundle JS para que el curso funcione **sin
conexión**; lo único que necesita red son los enlaces "Abrir la clase" (sitio en
GitHub Pages) y "Ver en GitHub".

Cada clase viaja **entera**, no resumida: además de los campos de tarjeta
(objetivo, temas, nivel, duración) se emite ``content``, la secuencia de bloques
—encabezados, párrafos, viñetas, tablas, citas y bloques de código— en la que se
convierte el README completo. Antes solo viajaba un resumen recortado a unos
cientos de caracteres, así que la explicación en profundidad, el glosario, los
errores comunes, las preguntas frecuentes y las referencias no llegaban al
teléfono; quien leía la clase en la app leía otra cosa que quien la leía en el
sitio. Los bloques se reparten en dos pestañas por el emoji de su sección:
``theory`` (objetivo, resultados, temas, explicación, definiciones, glosario) y
``practice`` (preparación, laboratorio, ejercicios, reto, errores, preguntas,
referencias).

Los diagramas viajan como imagen: cada bloque ` ```mermaid ` se convierte en un
bloque ``{"t": "dg", "img": "<hash>"}`` y su PNG se copia a
``mobile/assets/diagramas/``. El archivo generado ``mobile/src/data/diagramas.js``
mapea cada hash a su ``require(...)``, que es lo que Metro necesita —una ruta
literal— para empaquetar la imagen dentro del APK.

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
import shutil
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mermaid_svg import clave as clave_diagrama  # noqa: E402
from mermaid_svg import rasterizar as rasterizar_diagramas  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
CLASSES_DIR = ROOT / "classes"
OUT_FILE = ROOT / "mobile" / "src" / "data" / "classes.js"
# Los diagramas se empaquetan como PNG dentro del APK: Metro los mete como
# recursos (no como texto del bundle), asi que pesan lo que pesan y no inflan el
# JavaScript. Se usa PNG y no SVG porque el <Image> de React Native no lee SVG
# sin una dependencia nativa que, ademas, ignoraria el CSS que mermaid incrusta
# dentro del SVG y dejaria los diagramas en blanco y negro sin estilos.
DIAG_DIR = ROOT / "mobile" / "assets" / "diagramas"
DIAG_FILE = ROOT / "mobile" / "src" / "data" / "diagramas.js"

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

# ── Reparto de secciones entre las dos pestañas de la app ────────────────────
#
# Se ancla en el emoji, no en el texto: el título varía ("🧪 Laboratorio guiado
# (defensivo)"), el emoji no. Lo que no está en ninguna de las dos listas es
# navegación del repositorio y no tiene sentido dentro de la app.

THEORY_EMOJIS = ("🎯", "📚", "🗺️", "🧠", "📖", "📔")
PRACTICE_EMOJIS = ("🧰", "🧪", "✍️", "📝", "⚠️", "❓", "🔗")
# 📥 Material descargable, ⬅️ Clase anterior y ➡️ Siguiente clase se descartan:
# son enlaces a ficheros del repo y a páginas que la app ya cubre con su
# navegación propia.

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


# Bloques ```mermaid ... ``` — se descartan antes de aplanar la sección a texto.
# La app no dibuja diagramas (renderiza <Text> planos); sin esto, el código del
# diagrama se colaría como prosa cruda (fue la causa del revert anterior).
MERMAID_FENCE_RE = re.compile(
    r"^[ \t]*```mermaid[ \t]*\n.*?^[ \t]*```[ \t]*$\n?",
    re.MULTILINE | re.DOTALL,
)


def strip_mermaid(text: str) -> str:
    return MERMAID_FENCE_RE.sub("", text)


def section(body: str, emoji: str) -> str:
    """Cuerpo crudo de la sección ``## <emoji> ...``, anclada en el emoji."""
    pattern = re.compile(
        rf"^##\s+{re.escape(emoji)}[^\n]*\n(.*?)(?=^##\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(body)
    return strip_mermaid(match.group(1).strip()) if match else ""


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


# ── README completo -> bloques que la app sabe pintar ────────────────────────

# Codigo de cada diagrama encontrado al recorrer las clases, en orden. Se
# recopila aqui para pedir todos los PNG de una vez al terminar el recorrido.
DIAGRAMAS_USADOS: list[str] = []

SECTION_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)
HEADING_RE = re.compile(r"^(#{3,6})\s+(.+)$")
FENCE_RE = re.compile(r"^\s*```\s*([\w+-]*)\s*$")
ORDERED_RE = re.compile(r"^(\s*)(\d+)[.)]\s+(.*)$")
UNORDERED_RE = re.compile(r"^(\s*)[-*]\s+(.*)$")
TABLE_SEP_RE = re.compile(r"^\|[\s:|-]+\|?$")


def table_cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


def blocks_from(body: str) -> list[dict]:
    """Convierte el cuerpo de una sección en bloques para el renderizador de la app.

    Se mantiene deliberadamente simple —la app pinta <Text>, no HTML—, pero
    conserva la estructura que hace legible una clase: jerarquía de subtítulos,
    párrafos separados, viñetas con su nivel, tablas con su cabecera, citas y
    bloques de código sin tocar (un comando mal cortado deja de ser un comando).
    """
    blocks: list[dict] = []
    lines = body.splitlines()
    i = 0
    parrafo: list[str] = []

    def cerrar_parrafo() -> None:
        if parrafo:
            texto = strip_inline(" ".join(parrafo))
            if texto:
                blocks.append({"t": "p", "x": texto})
            parrafo.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Bloque de código: se copia literal, sin aplanar el markdown inline.
        fence = FENCE_RE.match(line)
        if fence:
            cerrar_parrafo()
            lang = fence.group(1)
            i += 1
            buf: list[str] = []
            while i < len(lines) and not FENCE_RE.match(lines[i]):
                buf.append(lines[i])
                i += 1
            i += 1  # cierre
            if lang == "mermaid":
                # El código del diagrama no se emite como texto (sería prosa
                # ilegible), sino su imagen: el bloque guarda el hash con el que
                # la app la encuentra en diagramas.js.
                fuente = "\n".join(buf).strip()
                bloque = {"t": "dg"}
                if fuente:
                    bloque["img"] = clave_diagrama(fuente)
                    DIAGRAMAS_USADOS.append(fuente)
                blocks.append(bloque)
            elif buf:
                blocks.append({"t": "code", "x": "\n".join(buf).rstrip(), "lang": lang})
            continue

        if not stripped:
            cerrar_parrafo()
            i += 1
            continue

        heading = HEADING_RE.match(line)
        if heading:
            cerrar_parrafo()
            nivel = "h3" if len(heading.group(1)) == 3 else "h4"
            blocks.append({"t": nivel, "x": strip_inline(heading.group(2))})
            i += 1
            continue

        # Tabla: cabecera + separador + filas.
        if stripped.startswith("|") and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1].strip()):
            cerrar_parrafo()
            head = [strip_inline(c) for c in table_cells(stripped)]
            i += 2
            filas: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                filas.append([strip_inline(c) for c in table_cells(lines[i].strip())])
                i += 1
            blocks.append({"t": "table", "h": head, "r": filas})
            continue

        if stripped.startswith(">"):
            cerrar_parrafo()
            cita: list[str] = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                cita.append(lines[i].strip().lstrip(">").strip())
                i += 1
            texto = strip_inline(" ".join(c for c in cita if c))
            if texto:
                blocks.append({"t": "q", "x": texto})
            continue

        ordered = ORDERED_RE.match(line)
        if ordered:
            cerrar_parrafo()
            texto = strip_inline(ordered.group(3))
            if texto:
                blocks.append({"t": "li", "n": int(ordered.group(2)),
                               "d": len(ordered.group(1)) // 2, "x": texto})
            i += 1
            continue

        unordered = UNORDERED_RE.match(line)
        if unordered:
            cerrar_parrafo()
            texto = strip_inline(unordered.group(2))
            if texto:
                blocks.append({"t": "li", "d": len(unordered.group(1)) // 2, "x": texto})
            i += 1
            continue

        parrafo.append(stripped)
        i += 1

    cerrar_parrafo()
    return blocks


def full_content(md: str) -> tuple[list[dict], list[dict]]:
    """Todas las secciones del README repartidas en (teoría, práctica)."""
    theory: list[dict] = []
    practice: list[dict] = []
    matches = list(SECTION_RE.finditer(md))
    for idx, match in enumerate(matches):
        titulo = match.group(1).strip()
        fin = matches[idx + 1].start() if idx + 1 < len(matches) else len(md)
        cuerpo = md[match.end():fin].strip()
        if titulo.startswith(THEORY_EMOJIS):
            destino = theory
        elif titulo.startswith(PRACTICE_EMOJIS):
            destino = practice
        else:
            continue
        bloques = blocks_from(cuerpo)
        if not bloques:
            continue
        destino.append({"t": "h2", "x": strip_inline(titulo)})
        destino.extend(bloques)
    return theory, practice


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

    theory_blocks, practice_blocks = full_content(md)

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
        # La clase entera, en bloques: es lo que la app pinta al abrirla.
        "content": {"theory": theory_blocks, "practice": practice_blocks},
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

    def dump_classes(items: list[dict]) -> str:
        # Con la clase completa embebida, indentar cada bloque multiplicaría el
        # tamaño del fichero y haría ilegible cualquier diff. Una clase por
        # línea deja el diff en "cambiaron estas N clases".
        cuerpo = ",\n  ".join(json.dumps(c, ensure_ascii=False) for c in items)
        return "[\n  " + cuerpo + "\n]"

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
        f"export const CLASSES = {dump_classes(classes)};\n\n"
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


def proporcion_png(ruta: Path) -> float:
    """Alto/ancho del PNG, leido de su cabecera IHDR.

    Se hace a mano en vez de con Pillow porque este dato tambien se necesita en
    modo --check, que corre en CI sin dependencias extra. Y se emite con los
    datos en vez de preguntarlo en tiempo de ejecucion: el
    ``Image.resolveAssetSource`` de React Native no existe en react-native-web y
    reventaba la pantalla al abrir una clase en el navegador.
    """
    try:
        cabecera = ruta.read_bytes()[:24]
        ancho = int.from_bytes(cabecera[16:20], "big")
        alto = int.from_bytes(cabecera[20:24], "big")
        if ancho > 0 and alto > 0:
            return round(alto / ancho, 4)
    except OSError:
        pass
    return 0.6


def render_diagramas(ids: set[str]) -> str:
    """Genera mobile/src/data/diagramas.js con el require() de cada imagen."""
    lineas = [
        "// ============================================================",
        "// GENERADO AUTOMÁTICAMENTE — NO EDITAR A MANO",
        "// Fuente: bloques ```mermaid de classes/parte-*/NNN-*/README.md",
        "// Regenera con:  python scripts/generar_curriculum_movil.py",
        "// ============================================================",
        "//",
        "// Metro necesita una ruta literal en require() para empaquetar la imagen",
        "// dentro del APK, así que el mapa se escribe entero en vez de construir",
        "// la ruta en runtime. La proporción (alto/ancho) viaja con los datos para",
        "// que la app pinte el diagrama a su tamaño sin preguntárselo al sistema:",
        "// Image.resolveAssetSource no existe en react-native-web.",
        "",
        "export const DIAGRAMAS = {",
    ]
    for identificador in sorted(ids):
        proporcion = proporcion_png(DIAG_DIR / f"{identificador}.png")
        lineas.append(
            f"  \"{identificador}\": {{ fuente: "
            f"require('../../assets/diagramas/{identificador}.png'), "
            f"proporcion: {proporcion} }},"
        )
    lineas += [
        "};",
        "",
        "export const diagramaPorId = (id) => (id ? DIAGRAMAS[id] : undefined);",
        "",
        f"export const TOTAL_DIAGRAMAS = {len(ids)};",
        "",
    ]
    return "\n".join(lineas)


def sincronizar_diagramas(check: bool) -> tuple[str, int]:
    """Deja en los assets de la app el PNG de cada diagrama usado.

    En modo ``--check`` **no se dibuja nada**: se comprueba contra los PNG que ya
    estan versionados en ``mobile/assets/diagramas/``. Es deliberado — el check
    corre en CI antes de compilar el APK, y alli no hay navegador con el que
    rasterizar; si el check intentara dibujar, el release fallaria siempre.
    """
    ids = {clave_diagrama(f) for f in DIAGRAMAS_USADOS}
    if not ids:
        return render_diagramas(set()), 0

    if check:
        presentes = {i for i in ids if (DIAG_DIR / f"{i}.png").is_file()}
        return render_diagramas(presentes), len(presentes)

    pngs = rasterizar_diagramas(DIAGRAMAS_USADOS, verbose=True)
    DIAG_DIR.mkdir(parents=True, exist_ok=True)
    esperados = set()
    for fuente, origen in pngs.items():
        destino = DIAG_DIR / f"{clave_diagrama(fuente)}.png"
        esperados.add(destino.name)
        if not destino.is_file() or destino.stat().st_size != origen.stat().st_size:
            shutil.copyfile(origen, destino)
    # Un diagrama que ya no existe en ninguna clase no debe seguir ocupando
    # sitio dentro del APK.
    for sobrante in DIAG_DIR.glob("*.png"):
        if sobrante.name not in esperados:
            sobrante.unlink()
    return render_diagramas({clave_diagrama(f) for f in pngs}), len(pngs)


def main() -> int:
    check = "--check" in sys.argv
    parts, classes = collect()
    content = render(parts, classes)
    contenido_diagramas, total_diagramas = sincronizar_diagramas(check)

    if check:
        if not OUT_FILE.exists():
            print(f"FALLA: no existe {OUT_FILE.relative_to(ROOT)} — ejecuta el generador.")
            return 1
        actual = OUT_FILE.read_text(encoding="utf-8")
        if actual != content:
            print("FALLA: mobile/src/data/classes.js está desincronizado con las clases.")
            print("       Ejecuta: python scripts/generar_curriculum_movil.py")
            return 1
        if not DIAG_FILE.exists() or DIAG_FILE.read_text(encoding="utf-8") != contenido_diagramas:
            print("FALLA: mobile/src/data/diagramas.js no coincide con los diagramas de las")
            print("       clases o faltan PNG en mobile/assets/diagramas/.")
            print("       Ejecuta: python scripts/generar_curriculum_movil.py")
            return 1
        faltan = [
            b["img"] for c in classes
            for b in c["content"]["theory"] + c["content"]["practice"]
            if b.get("t") == "dg" and b.get("img")
            and not (DIAG_DIR / f"{b['img']}.png").is_file()
        ]
        if faltan:
            print(f"FALLA: {len(faltan)} diagrama(s) sin imagen en mobile/assets/diagramas.")
            return 1
        print(f"OK: {len(classes)} clases en {len(parts)} partes y {total_diagramas} "
              f"diagramas; datos embebidos al día.")
        return 0

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUT_FILE.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)
    with DIAG_FILE.open("w", encoding="utf-8", newline="\n") as fh:
        fh.write(contenido_diagramas)
    print(f"Generado {OUT_FILE.relative_to(ROOT)}: {len(classes)} clases en {len(parts)} partes.")
    empty = [c["id"] for c in classes if not c["theory"] or not c["outcomes"]]
    if empty:
        print(f"AVISO: {len(empty)} clases sin objetivo o sin resultados: {empty[:5]}")
    sin_cuerpo = [
        c["id"] for c in classes
        if len(c["content"]["theory"]) < 5 or not c["content"]["practice"]
    ]
    if sin_cuerpo:
        print(f"AVISO: {len(sin_cuerpo)} clases con contenido embebido escaso: {sin_cuerpo[:5]}")
    bloques = sum(len(c["content"]["theory"]) + len(c["content"]["practice"]) for c in classes)
    kb = len(content.encode("utf-8")) / 1024
    peso_png = sum(f.stat().st_size for f in DIAG_DIR.glob("*.png")) / 1024 / 1024 if DIAG_DIR.is_dir() else 0
    print(f"Contenido embebido: {bloques} bloques, {kb:.0f} KB de catálogo.")
    print(f"Diagramas empaquetados: {total_diagramas} PNG ({peso_png:.1f} MB) en "
          f"{DIAG_DIR.relative_to(ROOT)}.")
    sin_imagen = sum(
        1 for c in classes
        for b in c["content"]["theory"] + c["content"]["practice"]
        if b.get("t") == "dg" and not b.get("img")
    )
    if sin_imagen:
        print(f"AVISO: {sin_imagen} diagrama(s) quedaron sin imagen.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
