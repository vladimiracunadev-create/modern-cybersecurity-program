# 🗺️ Roadmap

El programa se construye por fases. El **currículo escrito** (README completo por cada una
de las 340 clases) es la base y el primer entregable.

## Fase 1 — Currículo escrito completo ✅ (completa)

- [x] Diseño del currículo: 19 partes, 340 clases, numeración 001–340.
- [x] Estructura de carpetas + índice maestro (`classes/README.md`).
- [x] README de cada parte (narrativa, prerrequisitos, fuentes).
- [x] README rico por clase (objetivo, temas, definiciones, laboratorio, ejercicios, reto, errores comunes, FAQ, referencias).

## Fase 2 — Laboratorios ejecutables ✅ (completa)

- [x] Estructura de laboratorios ([`labs/`](labs/README.md)) con convención común y guía de uso.
- [x] Lab **AppSec Web** ([`labs/appsec-web`](labs/appsec-web/README.md)) — OWASP Juice Shop + DVWA en Docker, recorrido guiado ligado a la Parte 4.
- [x] Lab **Blue Team / SOC** ([`labs/blue-team-soc`](labs/blue-team-soc/README.md)) — Elasticsearch + Kibana con telemetría de un ataque para detección/threat hunting (Parte 8).
- [x] Lab **Red Team / Active Directory** ([`labs/red-team-ad`](labs/red-team-ad/README.md)) — caja de atacante + guía GOAD (Parte 7).
- [x] Lab de **criptografía** ([`labs/cripto`](labs/cripto/README.md)) — 4 retos con solución en Python puro (Parte 2).
- [x] Lab **DFIR memoria/malware** ([`labs/dfir-memoria`](labs/dfir-memoria/README.md)) — Volatility 3 + YARA (Partes 9 y 17; prep SANS/BTL1).
- [x] Lab **code review / SAST** ([`labs/appsec-code`](labs/appsec-code/README.md)) — app vulnerable + Semgrep/Bandit (Partes 11 y 17; prep PenTest+/CISSP).
- [x] Lab **Pentest con IA (kali-mcp)** ([`labs/kali-mcp-ia`](labs/kali-mcp-ia/README.md)) — agente de IA orquestando Kali vía MCP (Parte 18).
- [x] Lab **Triaje forense de Windows** ([`labs/rootcause-windows`](labs/rootcause-windows/README.md)) — sensor de comportamiento en Rust (Partes 6, 8 y 9).
- [x] Lab **Escaneo de red** ([`labs/redes-nmap`](labs/redes-nmap/README.md)) y **explotación de binarios** ([`labs/pwn-binarios`](labs/pwn-binarios/README.md)) — Partes 1 y 5.
- [x] Lab **Auditoría cloud / CSPM** ([`labs/cloud-security`](labs/cloud-security/README.md)) — Prowler, ScoutSuite, trivy y kube-bench (Parte 10).
- [x] Lab **Pipeline de despliegue (DevSecOps)** ([`labs/devsecops-pipeline`](labs/devsecops-pipeline/README.md)) — repositorio vulnerable auditado en **ocho capas** (dependencias, SAST, secretos, Dockerfile, contenedor, CI/CD, typosquatting e inteligencia), con priorización KEV → EPSS → CVSS **implementada** (`priorizar.py`) e informe (Parte 11; también 227, 318 y 330).
- [x] Colección de **retos tipo CTF** ([`ctf/`](ctf/README.md)) con solución, por categoría.

## Fase 3 — Material complementario ✅ (completa)

Generado con `scripts/generar_material.py <parte>` (PDF vía navegador headless, PPTX vía
python-pptx). Notebooks **descartados** por decisión.

- [x] Guías **PDF** imprimibles por clase — **las 340 clases** (partes 0–18).
- [x] Presentaciones **PPTX** por clase — **las 340 clases** (partes 0–18).
- [x] Sección "📥 Material descargable" enlazada en cada README de clase.
- [x] ~~Notebooks~~ — descartado.

## Fase 4 — Portal y evaluación ✅ (completa)

- [x] Sitio web navegable del currículo (GitHub Pages, con nav a rutas/quiz/progreso).
- [x] Autoevaluaciones interactivas por parte ([`autoevaluaciones/`](autoevaluaciones/README.md), 97 preguntas).
- [x] Seguimiento de progreso de las 340 clases (localStorage).
- [x] Rutas guiadas por rol ([`rutas/`](rutas/README.md)): los roles clásicos (pentester, red team, SOC, DFIR, gestión de vulnerabilidades, AppSec, cloud, GRC y **CISO / director de seguridad de la información**) **más los derivados de ofertas de empleo reales** — analista de ciberseguridad en institución regulada, analista de seguridad ofensiva, SecOps, seguridad de infraestructura, operación de plataformas (MSSP/DLP), jefe de seguridad, **arquitecto de ciberseguridad IT/OT** y cooperación técnica. Cada una con su [examen final](docs/examen-final-por-rol.md); índice completo en [`rutas/README.md`](rutas/README.md).

## Fase 5 — App móvil Android ✅ (completa)

- [x] App **Expo / React Native** ([`mobile/`](mobile/README.md)) con las **340 clases en 19 partes** embebidas para leer **sin conexión**.
- [x] Navegación Home (partes + progreso) → Parte (clases + buscador) → Clase, con progreso local.
- [x] **Las clases enteras dentro del APK** (v1.1.0): explicación en profundidad, diagramas, glosario, laboratorio, ejercicios, reto, errores comunes, preguntas y referencias. Hasta la v1.0.0 la app embebía un resumen y había que salir al sitio para leer la clase.
- [x] Catálogo **generado** desde los README de las clases (`scripts/generar_curriculum_movil.py`, con `--check` de integridad).
- [x] **Release del APK por CI** ([`release-android.yml`](.github/workflows/release-android.yml)): compila, firma y publica el APK en la nube. Antes de publicar abre el artefacto y busca dentro del bytecode párrafos completos de las clases ([`scripts/verificar_bundle.py`](scripts/verificar_bundle.py)): un build en verde no prueba que el contenido viajara. Primer release: [**v1.0.0**](https://github.com/vladimiracunadev-create/modern-cybersecurity-program/releases/tag/v1.0.0) · último: [**v1.1.0**](https://github.com/vladimiracunadev-create/modern-cybersecurity-program/releases/tag/v1.1.0).

---

**Las 5 fases del roadmap están completas.** ¿Ideas o mejoras? Abre un *issue* o revisa
[CONTRIBUTING.md](CONTRIBUTING.md).
