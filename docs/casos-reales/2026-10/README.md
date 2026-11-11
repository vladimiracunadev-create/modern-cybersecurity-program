# Octubre de 2026: CVE e incidentes reales integrados en el programa

> **Fecha de corte de la investigación:** 2026-11-10 (catálogo KEV versión 2026.11.10). **Verificación:** 2026-11-11. **Periodo:** 1 al 31 de octubre de 2026.
> Este informe documenta qué se investigó, qué se confirmó, qué se corrigió respecto de la lista inicial, dónde se integró en el programa y **qué no se hizo**. Los hechos van separados de las hipótesis; donde una fuente no lo dice, el informe tampoco.

**Decisión curricular.** El programa es un curso, no un archivo de noticias: los casos se incorporan **dentro de las clases existentes** (sin clases ni partes nuevas, sin renumerar) donde enseñan una competencia concreta. La explicación canónica de cada familia está en una sola clase; las demás remiten a ella. Archivos de este informe: [registro verificado](registro-verificado.md) · [incidentes sin CVE](incidentes.md) · [matriz curricular](matriz-curricular.md). Datos reutilizables en `knowledge/cve/2026-10/` (`instantanea.json`, `mapa-curricular.json`, `incidentes.json`) y laboratorio en [`labs/octubre-2026-casos-reales`](../../../labs/octubre-2026-casos-reales/README.md).

## 1. Método y alcance de la investigación

Tres conjuntos independientes, tal como pide el encargo:

| Conjunto | Definición | Cómo se construyó | Resultado |
|---|---|---|---|
| A | CVE con **registro publicado** en octubre de 2026 | De los 36 CVE de la lista (todos en KEV de octubre), se leyó `datePublished` del registro CVE | **20** publicados en octubre; 15 antes; 1 después |
| B | CVE **incorporados a KEV** en octubre | `dateAdded` del catálogo oficial (`cisagov/kev-data`) | **36** |
| C | Incidentes de octubre | Búsquedas y lectura de avisos de fabricantes, CISA y analistas | **4** estudiados |

**Límites que conviene leer.** (1) El conjunto A **no es exhaustivo**: solo cubre los CVE publicados en octubre que además entraron a KEV ese mes. No se recorrió el repositorio `cvelistV5` completo (decenas de miles de registros) y no se afirma haber cubierto todos los CVE de octubre. (2) El conjunto C **no cubre todos los hackeos del mundo**: los resúmenes mensuales consultados citan muchos más, pero la mayoría son reclamaciones de grupos de ransomware sin confirmar o cifras sin fuente primaria; los 4 incluidos tienen fuente identificable y valor didáctico (véase [incidentes](incidentes.md)). (3) No se incorporaron CVE de fuentes no verificables.

**Fuentes consultadas** (todas el 2026-11-10 u 11): catálogo KEV (`raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json`), API del CVE Program (`cveawg.mitre.org/api/cve/<id>`, formato CVE JSON 5, que incluye los datos de CISA-ADP/*Vulnrichment*), API de EPSS de FIRST, avisos de los fabricantes y de CISA (AA26-293A, BOD 26-04), el informe de Huntress y el informe preliminar de Railway. **No se consultó** la web de NVD (devuelve 403 a clientes automáticos) ni el repositorio `cvelistV5` completo; el CVSS de NIST no figura en la instantánea, solo el del CNA y el de CISA-ADP cuando existe.

## 2. Verificación de los 36 identificadores iniciales

| Pregunta | Resultado |
|---|---|
| ¿Existen en el registro oficial? | **Los 36**; todos con estado `PUBLISHED` |
| ¿Están en KEV con fecha de octubre? | **Los 36** (entre 2026-10-01 y 2026-10-30) |
| ¿Se publicó su registro en octubre? | 20 sí; 15 antes de octubre (incluidos 3 de 2015-2016, uno de 2021 y uno de 2023); 1 después (`CVE-2026-118527`) |
| ¿Descartados, rechazados o con identificador erróneo? | **Ninguno** |
| ¿Corregidos? | Ninguno de los identificadores; **sí varias hipótesis del encargo** (§3) |

Esos números salen de `knowledge/cve/2026-10/instantanea.json` y están fijados por pruebas automáticas (`python -m unittest discover -s labs/octubre-2026-casos-reales/tests`). No se añadieron CVE adicionales a los 36: el conjunto B coincide exactamente con la lista inicial.

## 3. Hipótesis del encargo que los datos corrigen o matizan

1. **Plex:** los cuatro CVE de Plex existen y son de la misma versión corregida (1.43.3.10861), pero **solo dos** (`CVE-2026-96652`, `CVE-2026-96655`) son SSRF; `CVE-2026-96654` es neutralización incorrecta de valores de URL y `CVE-2026-96656` es escritura de archivos que acaba en la carga de bibliotecas. La clase 99 trata los SSRF y la 105, la escritura.
2. **PHP y kernel de Linux como «cadena»:** los registros **no relacionan** `CVE-2026-109618/109619` (PHP) con `CVE-2026-46300` (kernel, red). Se estudian por separado y la clase 365 lo dice expresamente. Por eso **no se creó** el «Laboratorio A» como cadena PHP→Linux.
3. **Ivanti, BeyondTrust y «autenticación»:** los CVE de Ivanti comparten aviso en KEV, pero que se encadenen es una hipótesis, no un hecho documentado. BeyondTrust (`CWE-290`) es validación de **origen de mensajes internos**, no inicio de sesión.
4. **Fechas:** `CVE-2026-118527` aparece en KEV (2026-10-30) **antes** de la publicación de su registro (2026-11-03); varios CVE «de octubre» se publicaron en septiembre o antes; `CVE-2025-61624` lleva el año 2025 pero se publicó en abril de 2026.
5. **CWE:** KEV y el registro CVE discrepan en 4 casos (`CVE-2015-5477`, `CVE-2026-104286`, `CVE-2026-111357`, `CVE-2026-46300`). Se cita la fuente de cada CWE.
6. **CVE antiguos:** tres CVE de 2015-2016 (ProFTPD, BIND, Struts), uno de 2021 (ONLYOFFICE) y uno de 2023 (Strapi) entraron a KEV en octubre; su entrada **no** significa que sean hallazgos de octubre.
7. **Severidad:** 6 de los 36 tienen CVSS máximo inferior a 7 y 13 tienen EPSS inferior al 5 %; todos están en KEV. Es el hallazgo central de la clase 369.

## 4. Auditoría previa y matriz de diagnóstico

Estado verificado en la rama `main` (370 clases, 21 partes, validadores en verde antes de intervenir). Se buscó en `HEAD` cada fabricante o concepto antes de escribir.

| Tema | Clases relacionadas | Cobertura previa | Preservado | Vacío pedagógico | Laboratorio previo | Trabajo | Riesgo de compatibilidad |
|---|---|---|---|---|---|---|---|
| Inyección de comandos | 95 | técnica general; ningún caso de 2026 | toda la explicación | casos con condiciones de alcance y privilegio | `labs/appsec-code` (Bandit, Semgrep) | sección de casos + `argv_seguro` | bajo: añade contenido |
| SSRF | 99 | mecánica, metadatos y un caso (wechat) en 99/369 | todo | cadena de decisiones de un caso 2026 | — | sección Plex + `validar_destino` | bajo |
| Autenticación | 101 | fallos genéricos | todo | separar autenticación, autorización y privilegio con casos | `labs/appsec-web` | sección + tabla de siete CVE | bajo |
| Rutas y archivos | 105 | traversal e IDOR | todo | lectura/escritura/carga; byte nulo | `labs/appsec-web` | sección + `ruta_segura` | bajo |
| Memoria y enteros | 365 (119–140 son práctica ofensiva) | familias CWE | todo | ningún caso 2026 | `labs/pwn-binarios` | siete CVE + límite honesto | bajo |
| Fechas de un CVE | 367 | anatomía del CVE | todo | las tres fechas con datos reales | `devsecops-pipeline` | sección + comando de instantánea | bajo |
| Priorización | 369 (y 245) | KEV, EPSS, BOD 26-04 con 14 casos históricos | tabla de 14 casos | un mes completo | `devsecops-pipeline/bod2604.py` | sección con 36 CVE | bajo |
| Detección en la nube | 199, 222 | genérica | todo | caso real de identidad de aplicación | `blue-team-soc` (Elastic) | reglas R1–R4 + métricas | bajo; **no probado en Elastic** |
| Recuperación tras ransomware | 216 | contención y recuperación | todo | supervivencia de copias | `dfir-memoria` | caso IDCF + `evaluar_respaldos` | bajo |
| Secretos en plataformas | 241 | secretos y pre-commit | todo | rotación sin saber qué se vio | `devsecops-pipeline` | nota con el caso Railway | bajo |

## 5. Qué se integró y dónde

| Clase | Aporte (canónico = explicación completa) | Casos |
|---|---|---|
| [095](../../../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md) | **Canónico**: inyección de comandos y de código | Ahsay, Collabora, SiteGuard, Windows Shell, PAN-OS, Struts 2016 |
| [099](../../../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md) | **Canónico**: SSRF | Plex (4 CVE) |
| [101](../../../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md) | **Canónico**: autenticación, sesión, autorización, escalada | Ivanti, BeyondTrust, Ahsay, Zammad, Arista |
| [105](../../../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md) | **Canónico**: lectura, escritura y carga de archivos | Atlassian, Fortinet, Cisco, Adobe, ProFTPD, ONLYOFFICE |
| [199](../../../classes/parte-8-blue-team-deteccion-y-soc/199-ingenieria-de-deteccion-como-disciplina/README.md) | Reglas de detección sobre identidades de aplicación | ConnectWise |
| [216](../../../classes/parte-9-forense-digital-y-respuesta-a-incidentes/216-contencion-erradicacion-y-recuperacion/README.md) | Supervivencia de copias y rotación | IDC Frontier, Railway |
| [222](../../../classes/parte-10-seguridad-en-la-nube-y-contenedores/222-iam-en-la-nube-identidades-roles-y-permisos/README.md) | **Canónico**: identidad de aplicación de un proveedor | ConnectWise |
| [241](../../../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md) | Nota breve | Railway |
| [245](../../../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md) | Nota breve | SafePay (AA26-293A) |
| [364](../../../classes/parte-20-debilidades-y-vulnerabilidades-cwe-cve-cvss/364-familias-cwe-identidad-acceso-criptografia-informacion/README.md) | Inferencia por filtros | Strapi |
| [365](../../../classes/parte-20-debilidades-y-vulnerabilidades-cwe-cve-cvss/365-familias-cwe-memoria-enteros-concurrencia-recursos/README.md) | **Canónico**: memoria y enteros | PHP (2), Brotli, GitLab, kernel, NetScaler, Cisco ASA |
| [366](../../../classes/parte-20-debilidades-y-vulnerabilidades-cwe-cve-cvss/366-familias-cwe-configuracion-dependencias-contenedores-apis-nube-so/README.md) | Ruta de búsqueda de DLL | Siemens |
| [367](../../../classes/parte-20-debilidades-y-vulnerabilidades-cwe-cve-cvss/367-cve-identificar-vulnerabilidades-concretas/README.md) | **Canónico**: las tres fechas de un CVE | los 36 |
| [369](../../../classes/parte-20-debilidades-y-vulnerabilidades-cwe-cve-cvss/369-epss-cisa-kev-y-priorizacion-por-riesgo/README.md) | **Canónico**: severidad frente a explotación frente a exposición | los 36 |

Cada clase intervenida recibió, además de la sección, una fila en su tabla de temas, un ejercicio con solución razonada y fuentes citadas en su bloque de referencias. Las 11 preguntas nuevas de [autoevaluaciones](../../../autoevaluaciones/preguntas.json) cubren las partes 4, 8, 9, 10, 11 y 20.

## 6. Laboratorios: qué se hizo y qué no

| Propuesta | Estado | Razón |
|---|---|---|
| **A** PHP + Linux | **No creado** | No hay relación documentada entre los CVE; reproducir los defectos de memoria sería un exploit, no una práctica defensiva. Se cubre con análisis (clase 365) y `labs/pwn-binarios` |
| **B** Acceso remoto (auth + escalada + archivos) | **Parcial** | `ruta_segura`, `argv_seguro` y la tabla de la clase 101; no hay un simulador de VPN |
| **C** SSRF y multimedia | **Hecho** (sin multimedia) | `validar_destino` y servidor ficticio; **no** se modela el procesamiento multimedia de Plex |
| **D** CI/CD | **No creado** | GitLab `CVE-2026-97229` es un desbordamiento de enteros en el compilador de expresiones regulares; el aviso no detalla la ruta y una réplica sería especulación. Pendiente si GitLab publica detalles |
| **E** Detección SOC | **Hecho** | `deteccion_identidad_app.py` con métricas; **no** se cargó en Elastic |
| **F** Ransomware | **Hecho** (modelo) | `evaluar_respaldos` con inventario ficticio; no hay artefactos de cifrado |

El laboratorio es **un solo directorio** reutilizando `bod2604.py`, no un entorno nuevo. Detalles, soluciones y criterios en su [README](../../../labs/octubre-2026-casos-reales/README.md).

## 7. Motor de actualización mensual

Se evaluó y se hizo **mínimo**: [`scripts/cve_mensual.py`](../../../scripts/cve_mensual.py) (solo biblioteca estándar) con dos órdenes, `snapshot --mes AAAA-MM` y `comparar`. Reutiliza la convención de `labs/devsecops-pipeline/actualizar_casos.py` (foto fechada, sin servicio permanente) pero a diferencia de ella cubre un **mes entero** desde KEV y no hace falta una clave de NVD. No se ejecuta en CI (necesita red) y su salida se **revisa antes de publicarse**. No se convirtió el programa en un servicio de monitorización.

## 8. Limitaciones y trabajo pendiente

- Conjunto A parcial (§1). Incidente IDC Frontier con fuente solo secundaria; las cifras de recuperación varían entre fuentes.
- No se consultó NVD; no hay CVSS de NIST. El «CVSS máximo» de la clase 369 es el mayor entre los publicados por el CNA y CISA-ADP.
- EPSS es una foto del 2026-11-10: el análisis es **retrospectivo** y no demuestra el EPSS previo a la explotación.
- Laboratorios A y D no creados (§6); la integración con Elastic y el procesamiento multimedia de Plex no se probaron ni modelaron.
- No se verificó el estado de explotación de cada CVE más allá de su presencia en KEV; los avisos de los fabricantes se leyeron a través de los campos del registro CVE y no, en todos los casos, en su texto íntegro.
- Los ATT&CK citados (T1098.001, T1098.003, T1110.003) se verificaron en v20.1; el mapeo con el incidente de ConnectWise es **inferencia del programa**, no del informe de Huntress.
- El Android/Expo no se reconstruyó: el catálogo embebido se regeneró y su comprobación `--check` pasa, pero no se ejecutó `npm ci` ni `expo export`.

## 9. Evidencia de validación (ejecutada el 2026-11-11, Windows, Python 3.12)

| Comprobación | Resultado |
|---|---|
| `validar_estructura.py` | OK (0 enlaces rotos) |
| `generar_navegacion.py --check` | OK, 370 clases |
| `validar_rutas.py` | OK |
| `validar_encoding.py` | OK, sin mojibake |
| `verify-sources` | OK; 800 entradas en el registro (21 nuevas, todas citadas) |
| `generar_glosario_global.py --check` y su prueba | OK |
| `generar_curriculum_movil.py --check` | OK: 370 clases, 406 diagramas |
| `test_cwe_kb` (84), `cwe_kb.py validar / referencias / cobertura --check` | OK tras regenerar `docs/matriz-cobertura-cwe.md` |
| Laboratorios: appsec-code, devsecops-pipeline, llmjacking, hardware, custodia, lanzamientos, game-security | OK (appsec-code con 2 pruebas omitidas por diseño) |
| Laboratorio de octubre de 2026 (33 pruebas) | OK |
| `bandit -ll` sobre `scripts` y el laboratorio nuevo | sin hallazgos |
| `markdownlint-cli2@0.23.0` sobre todo el repositorio | 0 errores |
| `actionlint` sobre `ci.yml` y `security.yml` | OK |
| `generar_sitio.py` | OK, 523 páginas |
| `generar_material.py --clases …` (14 clases) y `generar_manual.py` | OK: PDF y PPTX de 14 clases. `generar_manual.py` renderizó el PDF pero su espera de publicación (60 s) venció antes de que Windows mostrara el temporal; se publicó el temporal con `salida_atomica.publicar` tras comprobar 1 536 páginas y el contenido nuevo, y pasaron `verificar_diagramas` (20/20) y `verificar_recurso` (13/13) |
| Expo (`npm ci`, `expo export`) y comprobación del bundle | **No ejecutado** |

**Línea base antes de intervenir:** estructura, navegación, rutas, codificación y fuentes estaban en verde; no se detectaron regresiones en ninguna de ellas.
