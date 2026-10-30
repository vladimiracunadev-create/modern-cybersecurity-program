# Registro de progreso — integración CWE / CVE / CVSS / EPSS / KEV

Archivo de reanudación: si la sesión se interrumpe, leer este documento antes de tocar nada.
Se actualiza al cerrar cada bloque de trabajo. Las decisiones de diseño están en la sección
«Decisiones»; las pruebas ejecutadas, con su resultado real, en «Pruebas».

## Punto de partida (verificado el 2026-10-30)

- Rama `main`, árbol de trabajo limpio, último commit `68f278d`.
- 360 clases en 20 partes (001–360); el `_manifest.json` (ignorado por Git) dice 310 y está desfasado.
- `validar_estructura.py` exige numeración sin huecos y secciones fijas por clase.
- Python 3.12.9, `pnpm` 11.2.2; `uv` **no** está instalado. La solución usa solo biblioteca
  estándar, así que no añade dependencias.
- Red disponible hacia `cwe.mitre.org` y `first.org`; `nvd.nist.gov` responde 403 a clientes sin API.

## Decisiones

| # | Decisión | Motivo |
|---|---|---|
| D1 | Datos CWE en `knowledge/cwe/`, herramienta en `scripts/cwe_kb.py` | Reutiliza la convención de `scripts/` y deja los datos fuera de `classes/` |
| D2 | Solo biblioteca estándar (sin `uv`, sin dependencias nuevas) | Regla 7 del encargo; el repositorio no tiene `pyproject.toml` |
| D3 | El ZIP/XML original **no** se versiona; se versiona su procedencia (URL, SHA-256, versión) | El XML pesa ~19 MB; la importación es reproducible |
| D4 | Contenido pedagógico nuevo en una **Parte 20** (361+) | Conserva la numeración 001–360; Partes 17–19 se añadieron igual |

## Plan de la Parte 20 (clases 361–370)

| N.º | Título de trabajo | Núcleo |
|---|---|---|
| 361 | CWE: qué es y cómo está construido | Historia, MITRE, tipos (Weakness, Category/Grouping, View, Pillar), abstracción, estados, herramienta local |
| 362 | Del síntoma a la causa raíz | Relaciones, cadenas, consecuencias, mapeo, ambigüedad, límites; CWE vs CVE vs CVSS vs OWASP |
| 363 | Familias (1): entradas no confiables | Inyección SQL/comandos/código, XSS, CSRF, rutas, deserialización, SSRF |
| 364 | Familias (2): identidad, acceso, criptografía y exposición | Autenticación, autorización, sesiones, cripto, información sensible |
| 365 | Familias (3): memoria, enteros, concurrencia y recursos | OOB, UAF, desbordamientos, carreras, agotamiento |
| 366 | Familias (4): configuración, dependencias, contenedores, APIs, nube y SO | Solo con correspondencia CWE válida |
| 367 | CVE | Anatomía, CNA, estados, CPE, NVD, CWE dentro de un CVE |
| 368 | CVSS v3.1 y v4.0 | Calcular, leer vectores, B/BT/BE/BTE, límites |
| 369 | EPSS, CISA KEV y priorización | Casos reales y contrastes entre señales |
| 370 | Ciclo completo | Capstone: debilidad → vulnerabilidad → corrección verificada |

## Estado de las tareas (actualizado)

### Hecho y verificado

- [x] **Base de conocimiento CWE** (`knowledge/cwe/`, CWE 5.0 de 2026-10-28): 1415 entradas (984 debilidades, 431 agrupaciones), 62 vistas, 1081 referencias externas. `scripts/cwe_lib.py`, `cwe_analisis.py`, `cwe_kb.py`.
- [x] **Pruebas de la base**: `scripts/tests/test_cwe_kb.py` (69 pruebas, 1 omitida si no existe la matriz).
- [x] **Calculadora CVSS v3.1 y v4.0** (`labs/devsecops-pipeline/cvss.py`): reproduce 26 puntuaciones v3.1 de NVD/CNA y 36 v4.0 de CNA + 11 ejemplos oficiales de FIRST. Tablas de v4.0 de FIRST (BSD-2-Clause) con su licencia.
- [x] **Instantánea de 14 casos reales** (`datos/casos-cwe-cve.json`) + actualizador reproducible (`actualizar_casos.py`) + `priorizar.py` ampliado (CWE, vector CVSS, `--instantanea`).
- [x] **Laboratorio `appsec-code`**: `app_corregida.py`, `cwe-map.json`, 25 pruebas de regresión, `SOLUCION.md` reescrita con mediciones reales de Bandit 1.9.4.
- [x] Pruebas del laboratorio `devsecops-pipeline`: `tests/` (46 pruebas).

- [x] **Clases 361–365 redactadas** (`classes/parte-20-...`): CWE, causa raíz y mapeo, familias de entradas no confiables, identidad/acceso/criptografía y memoria/concurrencia/recursos. Pendientes de registrar fuentes y generar PDF/PPTX.
- [x] **Prácticas ejecutables** `labs/appsec-code/practicas/` (autorización, memoria y carreras, límites) con 56 pruebas del laboratorio.
- [x] `cwe_kb.py`: comandos `miembros`, `top25`, `sast --mapa`; auditor de referencias afinado (vistas, obsoletas explicadas, listas).
- [x] `bod2604.py` (tabla oficial de plazos de CISA BOD 26-04, 16 filas) integrada con `priorizar.py --bod-26-04`.

### Hallazgos de la auditoría hasta ahora (para el informe)

- `priorizar.py` fallaba al imprimir en consolas Windows (cp1252) por el carácter `→` cuando no se pasaba `--salida`. **Corregido.**
- La docstring de `priorizar.py` citaba una opción `--exposicion` inexistente. **Corregido.**
- `SOLUCION.md` de `appsec-code` afirmaba reglas obsoletas (`B303`) y que Bandit marca los secretos con `B105/B106` (solo marca `DB_PASSWORD`, no `AWS_KEY`) y asignaba CWE-95 a `eval` sin advertir que Bandit lo etiqueta CWE-78. **Corregido y medido.**
- Bandit 1.9.4 asigna CWE-605 a «bind a 0.0.0.0» (el catálogo tiene CWE-1327 para eso) y CWE-78 a `eval` (CWE-95).
- `hallazgos-ejemplo.json` usa CVE ficticios (CVE-2023-99999/88888/77777) correctamente rotulados; hoy no existen en CVE.org, pero un identificador futuro podría colisionar.
- `classes/_manifest.json` (ignorado por Git) dice 310 clases; hay 360.
- La clase 087 afirma que OWASP Top 10:2021 es «la edición vigente»; OWASP publica ya el Top 10:2025 (verificado en top10.owasp.org/2025). El registro de fuentes ya lo avisaba (`owasp-top10-2021`).
- `sources/bibliography.json`: `mitre-cwe` figura como CWE 4.20; el catálogo vigente es 5.0 (2026-10-28).
- CISA derogó BOD 22-01 y BOD 19-02 con BOD 26-04 (2026-06-10); el temario no cita directivas, así que se añade en la clase 369.
- Las páginas web de NVD y CISA bloquean clientes sin navegador (403): se consultan por API o con el navegador integrado; no se elude el bloqueo.
- 83 clases de las partes 4, 5, 11 y 17 no citaban ningún CWE al empezar.
- De las 25 CWE del Top 25 de 2025: 0 completas, 11 solo mencionadas, 14 sin mención. 83 clases de las partes 4, 5, 11 y 17 no citan ningún CWE.

### Completado después (2026-10-30)

- [x] **Parte 20 completa** (clases 361–370) con README de parte, diagramas interpretados, material PDF/PPTX y navegación; 367 y 368 reciben su diagrama.
- [x] **Mapa curricular** `knowledge/cwe/pedagogico/mapa-curricular.json` (81 CWE) y **matriz** `docs/matriz-cobertura-cwe.md` (32 completos, 49 parciales, 0 pendientes; 18 de las 25 del Top 25 completas). `cobertura --check` va en CI.
- [x] La evidencia de evaluación de un CWE ahora debe **citar el identificador** (prueba nueva en `test_cwe_kb.py`); la batería de autoevaluación de la Parte 20 tiene 25 preguntas.
- [x] **Enriquecimiento** de 51 clases (Partes 3, 4, 5, 11 y 17) con la sección «Cómo lo nombra el catálogo CWE y qué cambia al priorizar», reescritura de la 087 (OWASP Top 10:2025) y correcciones de afirmaciones absolutas en 065, 115, 240 y 318.
- [x] **Prácticas nuevas** `appsec-code/practicas/ssrf.py` y `subida.py` (CWE-918 y CWE-434) con 25 pruebas; el reto de la clase 363 enlaza su solución de referencia.
- [x] **READMEs de los laboratorios**, `escanear.sh` con contraste CWE, fuentes (765 entradas), licencias, rutas (5 rutas con el paso de la Parte 20), cifras (370 clases · 21 partes) en README, índices, silabo, hoja de ruta, app móvil y generadores, catálogo móvil, glosario global, sitio y manual PDF regenerados.
- [x] **CI**: pruebas y validaciones de la base CWE, la matriz y los dos laboratorios.
- [x] **Auditoría** `docs/auditoria-cobertura-cwe-cve-cvss.md`.

### Pruebas ejecutadas al cierre (resultado real)

| Comprobación | Resultado |
|---|---|
| `scripts/validar_estructura.py` | OK (21 partes, 370 clases) |
| `scripts/generar_navegacion.py --check` | OK |
| `scripts/validar_rutas.py` | OK |
| `scripts/validar_encoding.py` | OK (672 archivos) |
| `scripts/verify-sources` | OK (765 entradas, 1.783 citas resueltas) |
| `scripts/generar_glosario_global.py --check` | OK |
| `scripts/generar_curriculum_movil.py --check` | OK |
| `scripts/verificar_diagramas.py` | OK (404 diagramas) |
| `scripts/cwe_kb.py validar`, `referencias`, `cobertura --check` | OK |
| `python -m unittest discover -s scripts/tests` | 88 pruebas OK |
| `python -m unittest discover -s labs/appsec-code/tests` | 81 pruebas OK (2 omitidas por sistema operativo) |
| `python -m unittest discover -s labs/devsecops-pipeline/tests` | 87 pruebas OK |
| Pruebas de custodia, lanzamientos virales y Game Security Range | OK |
| `markdownlint-cli2 "**/*.md"` | 0 incidencias |
| `actionlint .github/workflows/ci.yml` | OK |

### No hecho o limitado (ver la auditoría)

- Los porcentajes de `certificaciones/_mapeo.json` no se recalcularon: exigen contrastar los objetivos vigentes de cada examen.
- No hay laboratorio compilable para los CWE de memoria (C/C++); la cadena `CWE-190` → `CWE-787` se practica en simulación.
- Semgrep no se ejecutó localmente: lo que se afirma de él es una expectativa.
- No se compiló ni publicó ninguna versión de la app; la CI lo hace al etiquetar.
- Nada se ha confirmado (`git commit`) ni empujado: la decisión es de la persona responsable del repositorio.
