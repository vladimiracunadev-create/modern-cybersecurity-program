# Auditoría de la integración de LLMjacking y abuso de recursos de IA

> Fecha de la revisión: 10 de noviembre de 2026. Estado del repositorio verificado: 21 partes y 370 clases (`scripts/validar_estructura.py`). La integración **no crea clases ni partes nuevas** y no renumera nada.

## 1. Decisión curricular

El tema se absorbe en la **Parte 15** porque ya existía el vocabulario (OWASP LLM, extracción de modelos, injection, agentes, gobierno) y faltaba el eslabón económico y operativo. Crear una parte o una clase 371 habría duplicado la taxonomía de la 295 y fragmentado una cadena que se entiende de una sola vez: acceso → validación → reconocimiento → persistencia → monetización → control.

| Competencia | Ubicación natural | Por qué ahí |
|---|---|---|
| Qué es, historia, cadena de intrusión, controles, presupuesto vs límite, detección | **295** | Es donde se estudia la taxonomía y el riesgo LLM10:2025 |
| Agentes, gateways, MCP, servidores de modelos, presupuesto por tarea | **297** | El agente consume inferencia con credenciales propias |
| Riesgo económico, inventario, KRI, aceptación de coste colateral, RACI | **300** | Es un asunto de gobierno antes que de ingeniería |
| Detección con métricas | 199 (Parte 8) | Ingeniería de detección |
| Contención y evidencia | 216 (Parte 9) | Contención, erradicación y recuperación |
| Permisos de invocación | 222 (Parte 10) | IAM en la nube |
| Claves como secretos | 241 (Parte 11) | Secretos y pre-commit |
| Escenarios de estrés económico | 277 (Parte 14) | Riesgo cuantitativo |
| Agentes que consumen inferencia | 332 (Parte 18) | Agentes y MCP para seguridad |

Las clases 199, 216, 222, 241, 277 y 332 reciben solo una nota breve que remite a la 295: el desarrollo no se duplica.

## 2. Matriz de cobertura previa

| Concepto | Cobertura existente | Archivo verificado | Brecha | Acción | Riesgo de regresión |
|---|---|---|---|---|---|
| LLMjacking | ninguna (0 menciones en `classes/`) | búsqueda en `HEAD` | tema ausente | desarrollar en 295 | bajo: añade contenido |
| Consumo no acotado / *Denial of Wallet* | LLM04 *Model DoS* (2023) en 295; *denial-of-wallet* y «un budget alerta y no siempre detiene» en serverless | 295, 232 | la 295 usaba la numeración 2023 sin avisar de la 2025 (LLM10:2025) | tabla de ediciones y sección propia; la 232 se conserva | bajo |
| Alertas de presupuesto vs límites | 232 (serverless) lo dice en una frase | 232 | sin evidencia ni medición | explicación con fuente (AWS Budgets) y simulación | bajo |
| Robo/reutilización de tokens, OAuth | 52 líneas con «OAuth» en clases de IAM, web y cloud | búsqueda en `HEAD` | sin enfoque en credenciales de IA | explicado como *vector* en 295 | bajo |
| Servidores Ollama | una mención en el laboratorio de la 296 | 296 | exposición y autenticación sin cubrir | 297 + evaluador local en el laboratorio | bajo |
| Secret scanning | gitleaks en el CI y en `devsecops-pipeline`; clase 241 | `.github/workflows/security.yml`, 241 | formatos de claves de IA no ilustrados | escáner **didáctico** en el laboratorio; no se tocan las reglas de gitleaks | bajo: no se modifica nada existente |
| SOC y detección | `blue-team-soc` (Elastic, escenario DDoS) | `labs/blue-team-soc` | sin telemetría de IA | exportación NDJSON de intercambio; **carga en Elastic no probada** | nulo: el laboratorio no se modifica |
| IAM/CSPM | clases 222 y 231; `labs/cloud-security` | — | permisos de invocación de modelos | nota en 222 + escenario S6 | bajo |
| Respuesta a incidentes | 215/216/235 | — | playbook de credencial de IA | playbook propio en el laboratorio + nota en 216 | bajo |
| Gobierno | 300, 277, 284 | — | riesgo económico y coste colateral | sección en 300, nota en 277 | bajo |
| Mapeo MITRE ATLAS | referencias generales | 291, 295 | identificadores de técnica no verificados | **no se asignan IDs**; se declara | — |

## 3. Decisiones técnicas y razones

- **Python estándar, sin `uv` ni dependencias.** El laboratorio no necesita librerías: reducir superficie y funcionar igual en Windows y Linux. Los demás laboratorios Python del repositorio usan también `unittest` y no `uv`.
- **Datos deterministas con semilla** y generador `random.Random(seed)`; reproducible byte a byte (probado).
- **Detector por señales ponderadas con exigencia de al menos dos señales y cuatro puntos.** Ninguna señal basta por sí sola; la geolocalización no participa; el z robusto usa mediana y MAD.
- **Ventanas de 10 minutos.** Es el compromiso entre latencia y estabilidad del conteo; define la latencia mínima de detección (≈10 min en los escenarios).
- **Contexto de cambio aprobado** neutraliza solo señales de volumen y modelo; el resto sigue activo.
- **El retraso de 8 h de la alerta de presupuesto es un supuesto** inspirado en la documentación de AWS Budgets (actualización hasta tres veces al día), no una medición.
- **CI:** se añade un paso con las pruebas y la repetición con cinco semillas, y el directorio entra en el análisis bandit. No se modifica ningún otro paso.
- **Enlaces a artefactos generados** (PDF, PPTX, manual, catálogo móvil, sitio) por los generadores oficiales; no se editaron a mano.

## 4. Fuentes: qué respalda cada una y qué no

| Fuente | Fecha | Respalda | No se usa para |
|---|---|---|---|
| Sysdig TRT, LLMjacking | 2024-05-06 | acceso inicial vía Laravel CVE-2021-3129, validación con parámetro inválido, consulta de logging, estimación de 46 080 USD/día | afirmar la intención del atacante al consultar el logging (es interpretación de los autores) |
| Sysdig TRT, LLMjacking evolved | 2026-06-17 | Ollama como motor de una herramienta ofensiva; solo objetivos privados; intención incierta | generalizar a todos los atacantes |
| GTIG / Mandiant | 2026-11-02 | vectores, validación `max_tokens=1`, LLM Mixers, caso Jet Night, cifras, recomendaciones | su previsión de que los actores priorizarán el LLMjacking (es previsión) |
| CSA AI Safety Initiative | 2026-06-18 | interpretación del cambio de uso y recomendaciones | cifras de terceros que cita (Bizarre Bazaar) |
| OWASP LLM10:2025 y lista 2025 | vigente | numeración 2025, definición y mitigaciones | — |
| Ollama FAQ | vigente | escucha por defecto y `OLLAMA_HOST`; no menciona autenticación | afirmar que Ollama «no puede» autenticarse por otros medios |
| AWS Budgets | vigente | frecuencia de actualización, retraso y acciones | extrapolar a otros proveedores |
| Chema Alonso | 2026-11-09 | divulgación; resume GTIG | hechos que GTIG no confirme |

## 5. Verificaciones ejecutadas

Ver el informe final de la sesión y el historial del commit: pruebas del laboratorio, suite existente, estructura, navegación, rutas, codificación, trazabilidad de fuentes, glosario, catálogo móvil y análisis estático.

## 6. Pendiente y límites

- No se consultó documentación oficial de **Azure ni GCP** en esta pasada; las referencias a sus registros no se incluyeron. Queda como ampliación.
- No se asignan identificadores de técnicas **MITRE ATLAS** (no se pudieron verificar en la matriz durante la revisión).
- La **carga del NDJSON en Elastic** no se probó.
- El detector se afinó con el mismo generador que lo evalúa: las métricas validan la lógica, no el rendimiento real.
- No se ejecutó en local la exportación web de Expo ni la compilación del APK: las cubre el CI.
