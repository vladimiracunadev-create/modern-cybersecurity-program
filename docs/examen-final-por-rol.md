# 🎓 Examen final por rol

Cada [ruta por rol](../rutas/README.md) cierra con un **examen final** que combina teoría,
práctica y comunicación — igual que una entrevista técnica o una certificación real. Todos
comparten la misma estructura; cambia el contenido.

## Estructura común (100 puntos)

| Bloque | Peso | Formato |
|---|---:|---|
| **Teoría** | 25 | Quiz de la(s) parte(s) de la ruta ([autoevaluación](../autoevaluaciones/README.md)) ≥ 70%. |
| **Práctica** | 50 | Un ejercicio en laboratorio —o aplicado, en los roles de gestión—, con evidencia reproducible. |
| **Informe/comunicación** | 25 | Documento entregable (informe, playbook o política) evaluado con la [rúbrica](rubrica-evaluacion.md). |

**Aprobado:** ≥ 70/100 y práctica ≥ 30/50.

---

## 🎯 Pentester / Ethical Hacker

- **Teoría:** quizzes de las Partes 1, 3, 4, 5.
- **Práctica:** compromete la VM del lab [`appsec-web`](../labs/appsec-web/README.md) o una VM propia: recon → explotación de una vuln → PoC de bajo impacto.
- **Informe:** informe de pentest (resumen ejecutivo + hallazgos con CVSS + remediación), clase 085.

## 🔴 Red Teamer

- **Teoría:** Parte 7 (+ 5, 6).
- **Práctica:** en el lab [`red-team-ad`](../labs/red-team-ad/README.md)/GOAD: enumeración AD → Kerberoasting → ruta a Domain Admin con BloodHound.
- **Informe:** narrativa de la operación mapeada a MITRE ATT&CK + recomendaciones de detección.

## 🔵 Analista SOC / Blue Team

- **Teoría:** Partes 8, 6, 1.
- **Práctica:** en el lab [`blue-team-soc`](../labs/blue-team-soc/README.md): detecta la fuerza bruta + movimiento lateral y escribe una regla (Sigma) que dispare.
- **Informe:** informe de incidente + regla de detección validada.

## 🛡️ Analista de Gestión de Vulnerabilidades

- **Teoría:** Partes 3 (071), 17 (318, 324), 8.
- **Práctica:** en [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md), audita el repositorio en las ocho capas y prioriza con `priorizar.py` (KEV → EPSS → CVSS **ajustado por exposición real**), define SLAs y valida un parcheo con reversión si rompe los tests.
- **Informe:** reporte semanal de VM + plan de remediación priorizado.

## 🕵️ DFIR / Analista forense

- **Teoría:** Partes 9, 6.
- **Práctica:** en el lab [`dfir-memoria`](../labs/dfir-memoria/README.md): identifica el proceso malicioso, el C2 y extrae IOCs.
- **Informe:** informe forense con línea de tiempo y cadena de custodia.

## 🕸️ AppSec / Bug Bounty

- **Teoría:** Partes 4, 2, 11.
- **Práctica:** encuentra y explota (en tu lab) 3 vulns del OWASP Top 10 en [`appsec-web`](../labs/appsec-web/README.md); haz code review con [`appsec-code`](../labs/appsec-code/README.md); y audita el SDLC completo en [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md).
- **Informe:** 3 reportes tipo bug bounty (impacto, PoC, remediación) + la **sección de cobertura** del informe de auditoría: qué quedó fuera del alcance y por qué.

## ☁️ Cloud Security Engineer

- **Teoría:** Partes 10, 11, 2.
- **Práctica:** en el lab [`cloud-security`](../labs/cloud-security/README.md): audita una configuración con Prowler/kube-bench y corrige 3 hallazgos.
- **Informe:** informe CSPM con hallazgos priorizados y remediación como código.

## 🏛️ GRC / Gestión de seguridad

- **Teoría:** Partes 14, 17.
- **Práctica (aplicada):** construye una matriz de riesgo, un SoA de ISO 27001 y un perfil NIST CSF para una organización ficticia.
- **Informe:** política de seguridad + análisis de riesgo cuantitativo (FAIR).

## 🎩 CISO / Director de Seguridad de la Información

- **Teoría:** Partes 14 y 17 completas (+ 8, 9 y los bloques de nube/DevSecOps de 10–11).
- **Práctica (de dirección, sin consola):** sobre una organización ficticia con un contexto dado (sector, tamaño, servicios digitales críticos), entrega el **paquete de gobierno**: evaluación contra NIST CSF (actual vs objetivo), **registro de riesgos** con los diez riesgos principales cuantificados y con dueño, **BIA con RTO/RPO** acordados y **plan director a 24 meses con presupuesto**. Después **dirige** un [ejercicio de mesa](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md) de ransomware con reloj: decisiones de contención, criterio de notificación al regulador y comunicación a clientes.
- **Informe:** **informe ejecutivo de una página** con KPIs/KRIs para el directorio + **acta de aceptación formal de un riesgo** (quién firma, con qué vigencia) + **defensa del presupuesto** en cinco minutos, con pérdida esperada con y sin control. Se evalúa que un lector sin formación técnica sepa **qué tiene que decidir** al terminar.

---

## 🧭 Roles derivados de ofertas reales

Estas ocho rutas están calcadas de anuncios de empleo reales, así que su examen se parece más a una
**prueba de selección** que a un examen académico: el entregable es el que produce el puesto.

## 🏦 Analista de Ciberseguridad (institución regulada)

- **Teoría:** Partes 8, 9, 14 (+ 3).
- **Práctica:** en el lab [`blue-team-soc`](../labs/blue-team-soc/README.md), lleva una alerta hasta el cierre como caso formal de **ISO 27035** (triaje → investigación → contención → lecciones aprendidas), registrando tiempos; en paralelo, prioriza los hallazgos de un escaneo de vulnerabilidades y define SLAs de remediación.
- **Informe:** informe de incidente + **evidencia de auditoría** mapeada a un control concreto de ISO 27001.

## 🤝 Analista de Cooperación y Alianzas Técnicas

- **Teoría:** Partes 14, 0 (+ 8).
- **Práctica (aplicada):** diseña un acuerdo de **intercambio de información de amenazas** entre dos organizaciones ficticias: qué se comparte, con qué clasificación (TLP), bajo qué base legal, con qué controles de protección de datos y qué pasa ante un incumplimiento. Evalúa además el riesgo del tercero (clase 284).
- **Informe:** memorando de entendimiento + informe de riesgo de terceros + una **nota ejecutiva de una página** dirigida a alguien sin formación técnica.

## ⚙️ Security Engineer / SecOps

- **Teoría:** Partes 8, 9, 11 (+ la programación de la Parte 0).
- **Práctica (con código, obligatorio):** construye una **API REST** que exponga el estado de seguridad de los hosts a partir de la telemetría del lab [`blue-team-soc`](../labs/blue-team-soc/README.md) —autenticada, con validación de entrada y sin secretos en el código— y automatiza en Python/Bash una tarea de *offboarding* (revocar accesos y dejar registro). Somete tu propio código a las ocho capas de [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md): lo que escribas se audita igual que lo demás.
- **Informe:** documentación de la API + **runbook** de respuesta a un incidente de endpoint + el repositorio con historial de Git legible.

## 🧰 Analista de Seguridad Ofensiva (consultoría)

- **Teoría:** Partes 3, 4, 1.
- **Práctica:** escanea el laboratorio con Nessus/OpenVAS y **valida a mano** cinco hallazgos —descartando al menos un falso positivo y justificando por qué—; después explota dos vulnerabilidades del OWASP Top 10 en [`appsec-web`](../labs/appsec-web/README.md), una de ellas **sobre una API**.
- **Informe:** los cinco hallazgos en formato profesional (descripción, CVSS justificado, evidencia reproducible, impacto y remediación) + un acta de alcance previa al trabajo.

## 👔 Jefe de Seguridad de la Información

- **Teoría:** Partes 14, 17 (+ 8).
- **Práctica (de dirección):** **dirige** un [ejercicio de mesa](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md) sobre un incidente grave, con roles asignados, decisiones cronometradas y comunicación a dirección; construye el registro de riesgos de la organización y un plan de remediación priorizado con responsables y fechas.
- **Informe:** **informe ejecutivo de una página** con KPIs/KRIs + acta de aceptación formal de un riesgo (con quién lo firma) + plan de tratamiento.

## 🧱 Analista de Seguridad de Infraestructura

- **Teoría:** Partes 1, 8, 10 (+ PKI y TLS de la Parte 2).
- **Práctica:** en [`blue-team-soc`](../labs/blue-team-soc/README.md), **conecta tú mismo al menos tres fuentes distintas** (Windows, Linux y un dispositivo de red o firewall), verifica la integridad de la ingesta y luego **rompe una fuente a propósito**: detéctalo, documenta cuánto tardaste y qué lo delató. Aplica una línea base de configuración y detecta una desviación.
- **Informe:** **runbook** de alta de una fuente de log + el mismo hallazgo redactado en dos registros (técnico y ejecutivo) + evidencia de ejecución de un control.

## 🧩 Ingeniero de Operación de Plataformas (MSSP y DLP)

- **Teoría:** Parte 17 (311, 312) y Parte 14 (280, 281, 289).
- **Práctica (aplicada):** define un esquema de **clasificación de datos** para una organización ficticia y el conjunto de políticas de **DLP** que lo hace cumplir; toma una tanda de casos de ejemplo, **afina los falsos positivos** y justifica cada ajuste; diseña un plan de hardening de la plataforma.
- **Informe:** **playbook** completo de un incidente de fuga de datos (detección → contención → comunicación al cliente → cierre) + **informe mensual de servicio** con métricas. Redactarlo en inglés técnico es opcional, pero es justo lo que el puesto exige.

## 🏭 Arquitecto de Ciberseguridad IT/OT

- **Teoría:** Partes 1 y 13 (**273**), 17 (316, 329, 315) y 14 (278, 279, 283, 284).
- **Práctica (de diseño, con laboratorio):** monta un **PLC simulado** (OpenPLC/GRFICS/Conpot) en una red aislada siguiendo la [clase 273](../classes/parte-13-seguridad-movil-iot-e-inalambrica/273-seguridad-de-sistemas-de-control-industrial-ics-scada/README.md), **construye el inventario de forma pasiva** (captura de tráfico, sin escaneo activo) y sobre él entrega el **modelo Purdue** del entorno con sus **zonas y conductos**: por cada conducto, protocolo permitido, sentido, inspección y quién lo aprueba. Implementa al menos un conducto de verdad con reglas de firewall ([034](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md)) y demuestra con tráfico que lo que no está permitido no pasa. Después **audita tu propio diseño** contra NIST CSF y marca la brecha.
- **Informe:** **memoria de diseño** (diagrama Purdue + matriz de flujos + justificación de cada zona) + **informe de brecha** con esfuerzo estimado y dueño + la **respuesta a una solicitud de acceso remoto de un proveedor**, resuelta como diseño (salto, MFA, sesión grabada, vigencia) y no como un sí o un no. Se evalúa que un ingeniero de automatización entienda el diagrama sin traductor.

---

## 🤖 Complemento IA (para cualquier rol)

Quien complete la **Parte 18** puede añadir el [capstone 340](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/340-capstone-pentest-autorizado-asistido-por-ia-con-mcp/README.md): repetir el examen práctico **asistido por IA** (kali-mcp) y comparar — con retrospectiva sobre qué aportó la IA y qué tuvo que corregir.

## 🔗 Relacionado

- [Rutas por rol](../rutas/README.md) · [Rúbrica de evaluación](rubrica-evaluacion.md) · [Syllabus](syllabus.md) · [Certificaciones](../certificaciones/README.md)
