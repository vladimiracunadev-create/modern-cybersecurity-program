#!/usr/bin/env python3
"""Genera docs/GLOSARIO-GLOBAL.md desde los glosarios de las clases.

El generador consolida variantes tipográficas y aliases conocidos, conserva las
clases donde aparece cada término y añade un pequeño conjunto de conceptos
transversales que conectan el currículo con la práctica externa. La salida es
determinista; ``--check`` no escribe y falla si el documento quedó obsoleto.
"""
from __future__ import annotations

import argparse
import re
import string
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSES = ROOT / "classes"
OUTPUT = ROOT / "docs" / "GLOSARIO-GLOBAL.md"

TITLE_RE = re.compile(r"^#\s+Clase\s+(\d{1,3})\s*[—–-]\s*(.+)$", re.MULTILINE)
GLOSSARY_RE = re.compile(r"^##\s+📔\s+Glosario[^\n]*\n(.*?)(?=^##\s|\Z)", re.MULTILINE | re.DOTALL)
LINK_RE = re.compile(r"\[([^]]+)]\([^)]+\)")
MARKUP_RE = re.compile(r"[*_`]+")


def plain(text: str) -> str:
    """Texto comparable sin destruir el Markdown de la definición original."""
    return " ".join(MARKUP_RE.sub("", LINK_RE.sub(r"\1", text)).split())


def normalize(text: str) -> str:
    """Clave estable: Unicode, mayúsculas, puntuación y espacios no separan aliases."""
    value = unicodedata.normalize("NFKD", plain(text).casefold())
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9+#]+", " ", value).strip()


CANONICAL: dict[str, str] = {}


def aliases(canonical: str, *variants: str) -> None:
    for value in (canonical, *variants):
        CANONICAL[normalize(value)] = canonical


aliases("CTF — Capture The Flag", "CTF", "Capture The Flag")
aliases("Flag", "bandera")
aliases("Writeup", "write-up", "informe de resolución")
aliases("Reconocimiento", "Recon", "Reconnaissance")
aliases("Enumeración", "Enumeration")
aliases("Pentesting", "Prueba de penetración", "Penetration testing")
aliases("Explotación", "Exploit", "Exploitation")
aliases("Payload", "carga útil")
aliases("Post-explotación", "Post explotación", "Post-exploitation")
aliases("Escalada de privilegios", "Privesc", "Privilege escalation")
aliases("Movimiento lateral", "Lateral movement")
aliases("Pivoting", "Pivot")
aliases("Pwn", "Binary exploitation")
aliases("Reversing", "Ingeniería inversa", "Reverse engineering")
aliases("Triage", "Triaje")
aliases("RCA — Análisis de causa raíz", "RCA", "Root Cause Analysis")
aliases("IOC — Indicador de compromiso", "IOC", "Indicator of Compromise")
aliases("TTP — Tácticas, técnicas y procedimientos", "TTP", "TTPs")
aliases("SOC — Security Operations Center", "SOC")
aliases("SIEM — Security Information and Event Management", "SIEM")
aliases("DFIR — Digital Forensics and Incident Response", "DFIR")
aliases("OSINT — Open Source Intelligence", "OSINT")
aliases("AppSec — Application Security", "AppSec")
aliases("Bug bounty", "Bug Bounty")
aliases("Hack The Box (HTB)", "HTB", "Hack The Box")
aliases("TryHackMe (THM)", "THM", "TryHackMe")
aliases("Web Security Academy", "PortSwigger Web Security Academy", "WSA")
aliases("CyLab Security Academy", "picoCTF", "picoCTF/CyLab")


SUPPLEMENTAL = {
    "CTF — Capture The Flag": "Competición o práctica de seguridad en la que se resuelven desafíos autorizados para recuperar una flag verificable.",
    "Flag": "Cadena de prueba que demuestra que se alcanzó el objetivo de un reto; no sustituye la explicación del método ni la evidencia.",
    "Jeopardy": "Formato CTF con desafíos independientes agrupados por categoría y puntuación.",
    "Attack-Defense": "Formato CTF donde cada equipo protege sus servicios mientras analiza y ataca los de otros equipos dentro de las reglas.",
    "KOTH — King of the Hill": "Formato competitivo en el que se obtiene y conserva control de un objetivo autorizado durante un intervalo.",
    "Writeup": "Informe reproducible que documenta alcance, hipótesis, pasos, evidencia, causa raíz, mitigación, detección y lecciones de un reto.",
    "Pentesting": "Evaluación autorizada que busca demostrar y documentar rutas de ataque dentro de un alcance, tiempo y reglas acordados.",
    "SOC — Security Operations Center": "Función organizativa que monitorea, investiga y coordina la respuesta ante señales de seguridad.",
    "DFIR — Digital Forensics and Incident Response": "Disciplina que combina preservación y análisis forense con contención, erradicación, recuperación y aprendizaje de incidentes.",
    "AppSec — Application Security": "Práctica de reducir y verificar riesgos de seguridad durante el diseño, desarrollo, despliegue y operación de aplicaciones.",
    "RCA — Análisis de causa raíz": "Análisis que explica el mecanismo fundamental que permitió un fallo, más allá del síntoma observado.",
    "Mitigación": "Cambio que reduce la probabilidad o el impacto de un riesgo sin afirmar necesariamente que lo elimina.",
    "Hack The Box (HTB)": "Plataforma de laboratorios prácticos de ciberseguridad; sus reglas limitan la publicación de soluciones de contenido activo.",
    "TryHackMe (THM)": "Plataforma de aprendizaje guiado mediante rutas, salas explicativas y salas de desafío.",
    "Web Security Academy": "Plataforma gratuita de PortSwigger con material y laboratorios interactivos de seguridad web.",
    "CyLab Security Academy": "Plataforma educativa gratuita de Carnegie Mellon que continúa el ecosistema de picoCTF.",
    "CyberDefenders": "Cyber range orientado a investigaciones defensivas, SOC y DFIR.",
    "OverTheWire": "Colección de wargames que comienza con Bandit para fundamentos de terminal y seguridad.",
    "PentesterLab": "Plataforma centrada en seguridad web y revisión de código, con ejercicios guiados y contenido de pago.",
    "LetsDefend": "Plataforma de entrenamiento SOC con investigaciones simuladas y modalidades gratuita y de pago.",
    "CTFtime": "Directorio comunitario de eventos CTF, equipos, resultados y writeups; no es por sí mismo una ruta guiada.",
    "pwn.college": "Plataforma educativa gratuita de seguridad práctica; sus reglas restringen publicar walkthroughs de desafíos.",
    "ROP Emporium": "Serie de retos progresivos para practicar return-oriented programming en binarios deliberadamente vulnerables.",
    "VulnHub": "Catálogo de máquinas virtuales vulnerables descargables para practicar en una red local aislada.",
    "crackmes.one": "Repositorio de crackmes para practicar ingeniería inversa sobre binarios creados con ese propósito.",
}

RELATED = {
    "CTF — Capture The Flag": ("Flag", "Writeup", "Jeopardy", "Attack-Defense", "KOTH — King of the Hill"),
    "Writeup": ("CTF — Capture The Flag", "RCA — Análisis de causa raíz", "Mitigación", "IOC — Indicador de compromiso"),
    "Pentesting": ("Reconocimiento", "Enumeración", "Explotación", "Post-explotación"),
    "DFIR — Digital Forensics and Incident Response": ("Triage", "IOC — Indicador de compromiso", "RCA — Análisis de causa raíz"),
}

PLATFORM_URLS = {
    "Hack The Box (HTB)": "https://www.hackthebox.com/",
    "TryHackMe (THM)": "https://tryhackme.com/",
    "Web Security Academy": "https://portswigger.net/web-security",
    "CyLab Security Academy": "https://cylabacademy.org/",
    "CyberDefenders": "https://cyberdefenders.org/",
    "OverTheWire": "https://overthewire.org/wargames/",
    "PentesterLab": "https://pentesterlab.com/",
    "LetsDefend": "https://letsdefend.io/",
    "CTFtime": "https://ctftime.org/",
    "pwn.college": "https://pwn.college/",
    "ROP Emporium": "https://ropemporium.com/",
    "VulnHub": "https://www.vulnhub.com/",
    "crackmes.one": "https://crackmes.one/",
}


@dataclass
class Entry:
    names: Counter = field(default_factory=Counter)
    definitions: Counter = field(default_factory=Counter)
    classes: dict[str, tuple[int, str, str]] = field(default_factory=dict)


def split_row(line: str) -> list[str]:
    """Divide una fila Markdown sencilla, respetando pipes escapados."""
    return [cell.strip().replace(r"\|", "|") for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]


def parse_glossary_table(block: str) -> list[tuple[str, str]]:
    """Extrae término/definición de una tabla de glosario válida."""
    lines = [line for line in block.splitlines() if line.strip().startswith("|")]
    if len(lines) < 3:
        return []
    header = [normalize(cell) for cell in split_row(lines[0])]
    term_names = ("termino", "term", "concepto", "sigla")
    definition_names = ("definicion", "definition", "significado", "descripcion")
    try:
        term_index = next(
            i for i, value in enumerate(header)
            if any(value == name or value.startswith(f"{name} ") for name in term_names)
        )
        definition_index = next(
            i for i, value in enumerate(header)
            if any(value == name or value.startswith(f"{name} ") for name in definition_names)
        )
    except StopIteration:
        return []
    rows: list[tuple[str, str]] = []
    for line in lines[2:]:
        cells = split_row(line)
        if max(term_index, definition_index) >= len(cells):
            continue
        term, definition = cells[term_index].strip(), cells[definition_index].strip()
        if term and definition and not set(plain(term)) <= {"-", ":", " "}:
            rows.append((term, definition))
    return rows


def canonical_name(term: str) -> str:
    return CANONICAL.get(normalize(term), plain(term))


def collect(classes_dir: Path = CLASSES) -> tuple[dict[str, Entry], int]:
    entries: dict[str, Entry] = defaultdict(Entry)
    scanned = 0
    for path in sorted(classes_dir.glob("parte-*/[0-9][0-9][0-9]-*/README.md")):
        text = path.read_text(encoding="utf-8")
        title_match = TITLE_RE.search(text)
        if not title_match:
            continue
        number, title = int(title_match.group(1)), plain(title_match.group(2))
        blocks = GLOSSARY_RE.findall(text)
        if not blocks:
            continue
        scanned += 1
        rel = path.relative_to(ROOT).as_posix()
        for block in blocks:
            for term, definition in parse_glossary_table(block):
                name = canonical_name(term)
                key = normalize(name)
                entry = entries[key]
                entry.names[name] += 1
                entry.definitions[definition] += 1
                entry.classes[rel] = (number, title, rel)
    for name, definition in SUPPLEMENTAL.items():
        key = normalize(canonical_name(name))
        entries[key].names[canonical_name(name)] += 1
        entries[key].definitions.setdefault(definition, 0)
    return dict(entries), scanned


def best(counter: Counter) -> str:
    """Elige de forma estable: frecuencia, contenido informativo y alfabético."""
    return sorted(counter, key=lambda value: (-counter[value], -len(plain(value)), normalize(value)))[0]


def anchor(text: str) -> str:
    return normalize(text).replace(" ", "-").replace("+", "")


def render(entries: dict[str, Entry], scanned: int) -> str:
    values = []
    for entry in entries.values():
        name = best(entry.names)
        definition = best(entry.definitions)
        values.append((normalize(name), name, definition, entry))
    values.sort(key=lambda row: row[0])

    lines = [
        "# 📚 Glosario global",
        "",
        "Referencia alfabética generada desde los glosarios locales de las clases. Consolida",
        "siglas y aliases sin borrar su contexto: cada término indica en qué clases aparece.",
        "Los conceptos transversales y plataformas se completan con metadatos mantenidos por",
        "el generador; la modalidad y disponibilidad pueden cambiar en sus sitios oficiales.",
        "",
        "> **Archivo generado.** No lo edites a mano. Ejecuta",
        "> `python scripts/generar_glosario_global.py` y valida con `--check`.",
        "",
        f"**Cobertura:** {len(values)} términos consolidados · {scanned} clases con glosario.",
        "",
        "## Cómo usarlo",
        "",
        "- Busca la sigla o el nombre completo: ambos apuntan a la misma entrada cuando son aliases.",
        "- Abre las clases de procedencia para recuperar mecanismo, límites, laboratorio y referencias.",
        "- Para elegir un entorno autorizado, consulta [Plataformas de práctica](PLATAFORMAS-DE-PRACTICA.md).",
        "- Para documentar una resolución, usa la [plantilla de writeup](../templates/writeup-ctf.md).",
        "",
        "## Índice alfabético",
        "",
    ]
    groups: dict[str, list[tuple[str, str, str, Entry]]] = defaultdict(list)
    for row in values:
        initial = unicodedata.normalize("NFKD", row[1])[0].upper()
        initial = "".join(ch for ch in initial if not unicodedata.combining(ch)) or "#"
        group = initial if initial in string.ascii_uppercase + string.digits else "Otros"
        groups[group].append(row)
    lines.append(" · ".join(f"[{group}](#{anchor(group)})" for group in sorted(groups)))
    lines.append("")

    for group in sorted(groups):
        lines += [f"## {group}", ""]
        for _, name, definition, entry in groups[group]:
            lines += [f"### {name}", "", definition, ""]
            alias_values = sorted(
                {variant for variant, canonical in CANONICAL.items() if canonical == name and variant != normalize(name)}
            )
            if alias_values:
                lines += [f"**Claves de búsqueda normalizadas:** {', '.join(f'`{a}`' for a in alias_values)}.", ""]
            if name in PLATFORM_URLS:
                lines += [f"**Sitio oficial:** [{name}]({PLATFORM_URLS[name]}).", ""]
            if name in RELATED:
                related = ", ".join(RELATED[name])
                lines += [f"**Relacionados:** {related}.", ""]
            refs = sorted(entry.classes.values())
            if refs:
                shown = refs[:10]
                ref_links = ", ".join(
                    f"[Clase {number} — {title}](../{rel})" for number, title, rel in shown
                )
                extra = f" y {len(refs) - len(shown)} más" if len(refs) > len(shown) else ""
                lines += [f"**Aparece en {len(refs)} clase(s):** {ref_links}{extra}.", ""]
            else:
                lines += ["**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.", ""]
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    entries, scanned = collect()
    content = render(entries, scanned)
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != content:
            print("FALLA: docs/GLOSARIO-GLOBAL.md está desincronizado.")
            print("Ejecuta: python scripts/generar_glosario_global.py")
            return 1
        print(f"OK: glosario global determinista ({len(entries)} términos; {scanned} clases).")
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(content, encoding="utf-8", newline="\n")
    print(f"Generado {OUTPUT.relative_to(ROOT)}: {len(entries)} términos; {scanned} clases.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
