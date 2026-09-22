# 🗺️ Roadmap

El programa se construye por fases. El **currículo escrito** (README completo por cada una
de las 360 clases) es la base y el primer entregable.

## Fase 1 — Currículo escrito completo ✅ (completa)

- [x] Diseño del currículo vigente: 20 partes, 360 clases, numeración 001–360.
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
- [x] Caso transversal **Custodia de activos digitales** ([diagnóstico y arquitectura](docs/caso-custodia-activos-digitales.md) · [laboratorio](labs/custodia-activos-digitales/README.md)) — conciliación de ledger, operación y blockchain; IAM/PAM/SoD, insider risk, threat model, DFIR, ocho playbooks, doce fuentes sintéticas, analizador y tests (Partes 8, 9, 11, 14, 16 y 17).
- [x] Lab **Escaneo de red** ([`labs/redes-nmap`](labs/redes-nmap/README.md)) y **explotación de binarios** ([`labs/pwn-binarios`](labs/pwn-binarios/README.md)) — Partes 1 y 5.
- [x] Lab **Auditoría cloud / CSPM** ([`labs/cloud-security`](labs/cloud-security/README.md)) — Prowler, ScoutSuite, trivy y kube-bench (Parte 10).
- [x] Lab **Pipeline de despliegue (DevSecOps)** ([`labs/devsecops-pipeline`](labs/devsecops-pipeline/README.md)) — repositorio vulnerable auditado en **ocho capas** (dependencias, SAST, secretos, Dockerfile, contenedor, CI/CD, typosquatting e inteligencia), con priorización KEV → EPSS → CVSS **implementada** (`priorizar.py`) e informe (Parte 11; también 227, 318 y 330).
- [x] Colección de **retos tipo CTF** ([`ctf/`](ctf/README.md)) con solución, por categoría.

## Fase 3 — Material complementario ✅ (completa)

Generado con `scripts/generar_material.py <parte>` (PDF vía navegador headless, PPTX vía
python-pptx). Notebooks **descartados** por decisión.

- [x] Guías **PDF** imprimibles por clase — **las 360 clases** (partes 0–19).
- [x] Presentaciones **PPTX** por clase — **las 360 clases** (partes 0–19).
- [x] Sección "📥 Material descargable" enlazada en cada README de clase.
- [x] ~~Notebooks~~ — descartado.

## Fase 4 — Portal y evaluación ✅ (completa)

- [x] Sitio web navegable del currículo (GitHub Pages, con nav a rutas/quiz/progreso).
- [x] Autoevaluaciones interactivas por parte ([`autoevaluaciones/`](autoevaluaciones/README.md), 109 preguntas).
- [x] Seguimiento de progreso de las 360 clases (localStorage).
- [x] Rutas guiadas por rol ([`rutas/`](rutas/README.md)): los roles clásicos (pentester, red team, SOC, DFIR, gestión de vulnerabilidades, AppSec, cloud, GRC y **CISO / director de seguridad de la información**) **más los derivados de ofertas de empleo reales** — analista de ciberseguridad en institución regulada, analista de seguridad ofensiva, SecOps, seguridad de infraestructura, operación de plataformas (MSSP/DLP), jefe de seguridad, **arquitecto de ciberseguridad IT/OT** y cooperación técnica. Cada una con su [examen final](docs/examen-final-por-rol.md); índice completo en [`rutas/README.md`](rutas/README.md).
- [x] **Familia SecOps y DevSecOps diferenciada**: rutas propias de [analista SecOps](rutas/secops-analista.md), [analista DevSecOps](rutas/devsecops-analista.md) e [ingeniero DevSecOps](rutas/devsecops-engineer.md) (con el alias «Especialista DevSecOps» explicado), la [matriz comparativa transversal](docs/matriz-roles-secops-devsecops.md) frente a SOC, AppSec, Cloud Security y DFIR, tres **trayectos de laboratorio** sobre `blue-team-soc` y `devsecops-pipeline`, y tres exámenes finales nuevos. Esta fase se completó cuando el currículo terminaba en la clase 340; la Parte 19 amplió después el catálogo hasta la 360.

## Fase 5 — App móvil Android ✅ (completa)

- [x] App **Expo / React Native** ([`mobile/`](mobile/README.md)) con las **360 clases en 20 partes** embebidas para leer **sin conexión**.
- [x] Navegación Home (partes + progreso) → Parte (clases + buscador) → Clase, con progreso local.
- [x] **Las clases enteras dentro del APK** (v1.1.0): explicación en profundidad, diagramas, glosario, laboratorio, ejercicios, reto, errores comunes, preguntas y referencias. Hasta la v1.0.0 la app embebía un resumen y había que salir al sitio para leer la clase.
- [x] Catálogo **generado** desde los README de las clases (`scripts/generar_curriculum_movil.py`, con `--check` de integridad).
- [x] **Release multiplataforma por CI** ([`release-android.yml`](.github/workflows/release-android.yml)): compila y firma el APK, exporta la aplicación web y publica ambos junto con el manual PDF y sus sumas SHA-256. Antes de publicar abre los bundles y busca contenido completo de las clases y recursos ([`scripts/verificar_bundle.py`](scripts/verificar_bundle.py)): un build en verde no prueba por sí solo que el contenido viajara. Primer release: [**v1.0.0**](https://github.com/vladimiracunadev-create/modern-cybersecurity-program/releases/tag/v1.0.0) · último: [**v1.3.0**](https://github.com/vladimiracunadev-create/modern-cybersecurity-program/releases/tag/v1.3.0).

## Fase 6 — El ecosistema CISO ✅ (completa)

- [x] **Centro de navegación del ecosistema** ([`rutas/ecosistema-ciso.md`](rutas/ecosistema-ciso.md)): mapa de cargos, cuatro familias (dirección interna, asesoría externa, especializaciones y **cargos vecinos que no son tipos de CISO**), **matriz comparativa central** de diez atributos en tres bloques, diez distinciones inequívocas, **test del mandato** de ocho preguntas, rutas de progresión y **contexto chileno e internacional con fuentes oficiales y fecha de consulta**.
- [x] **Ruta CISO ampliada** ([`rutas/ciso.md`](rutas/ciso.md)): los cinco alcances del cargo (global, regional, divisional, deputy, associate), con quién se negocia y qué, delegación sin ceder responsabilidad, modelo operativo de la oficina del CISO, plan de 30/60/90 días y la diferencia entre tener el título y tener el mandato.
- [x] **Seis rutas nuevas**, cada una con la ficha completa del cargo (alias, consolidación del título, mandato, día/mes/año, entregables, KPI y KRI, competencias, conflictos de interés, entrevista, certificaciones, capstone, portafolio, diferencias con los cargos vecinos y fuentes con fecha): [Field CISO / Customer CISO](rutas/field-ciso.md), [vCISO / Fractional / Interim / CISOaaS](rutas/vciso.md), [BISO](rutas/biso.md), [Product CISO](rutas/product-ciso.md), [AI CISO](rutas/ai-ciso.md) y [OT CISO](rutas/ot-ciso.md). **«Cloud CISO» se analizó y no recibió ruta propia**: la decisión y su justificación están documentadas en el ecosistema.
- [x] **Laboratorio ejecutivo** ([`labs/ciso-leadership`](labs/ciso-leadership/README.md)): 14 escenarios no ofensivos sobre **cinco organizaciones ficticias**, cada uno con contexto, datos de entrada, instrucciones, entregable, rúbrica, criterio de aceptación, ejemplo de referencia y límites éticos; **[15 plantillas reutilizables](labs/ciso-leadership/PLANTILLAS.md)** (RACI, registro de riesgos, aceptación de riesgo, KPI/KRI, informe ejecutivo, 30/60/90, BIA, tabletop, terceros, declaración de trabajo de vCISO, descubrimiento de Field CISO, paquete de confianza de producto, inventario y riesgos de IA, y roadmap OT). Es el primer laboratorio **sin Docker** del repositorio, y la excepción está documentada en [`labs/README.md`](labs/README.md).
- [x] **Evaluación del ecosistema** ([`EVALUACION.md`](labs/ciso-leadership/EVALUACION.md)): 18 preguntas de escenario más cinco ejercicios prácticos (RACI de crisis, aceptación de riesgo, conflicto de interés en preventa, informe ejecutivo y clasificación de seis cargos reales), y **siete exámenes finales nuevos** en [`docs/examen-final-por-rol.md`](docs/examen-final-por-rol.md), ninguno aprobable con el entregable de otro.
- [x] **Validador de rutas** ([`scripts/validar_rutas.py`](scripts/validar_rutas.py)), en CI: comprueba que ninguna guía queda huérfana del índice, que cada una trae las secciones obligatorias, que las referencias apuntan a clases existentes dentro del catálogo vigente 001–360, que las rutas del ecosistema enlazan su laboratorio y su capstone, y —para todo el repositorio— que **ningún enlace con ancla** (`fichero.md#sección`) apunta a un encabezado inexistente, algo que el validador de estructura no miraba.
- [x] Esta fase no alteró la numeración de las **340 clases que existían entonces**: su contenido nuevo vivió en `rutas/`, `labs/` y `docs/`. La ampliación 341–360 corresponde a la Fase 7.

---

## Fase 7 — Game Security y Anti-Cheat ✅ (completa)

- [x] Parte 19 con 20 clases (341–360), progresión pedagógica y fuentes trazables.
- [x] Game Security Range con modos NORMAL/VULNERABLE/SECURE/DETECTION, tests y datasets.
- [x] Autoevaluación, CTF, ruta profesional, examen por rol, app, sitio, manual y materiales.

## Fase 8 — CTF, glosario y plataformas de práctica ✅ (completa)

- [x] Glosario global determinista generado desde los glosarios locales, con aliases, siglas y trazabilidad a clases.
- [x] Guía verificada de plataformas autorizadas, progresión por perfil y límites de publicación.
- [x] Plantilla transversal de writeup: evidencia, causa raíz, mitigación, detección y lecciones.
- [x] Integración en README, CTF, GitHub Pages y aplicación móvil offline, con búsqueda por sigla o plataforma.
- [x] Tests y CI contra deriva; auditoría documentada en [`docs/AUDITORIA-CTF-GLOSARIO-PLATAFORMAS.md`](docs/AUDITORIA-CTF-GLOSARIO-PLATAFORMAS.md).

**Las 8 fases del roadmap están completas.** ¿Ideas o mejoras? Abre un *issue* o revisa
[CONTRIBUTING.md](CONTRIBUTING.md).
