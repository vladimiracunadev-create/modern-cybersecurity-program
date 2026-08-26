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
- **Frontera:** este examen termina cuando la detección está escrita. **Lo que viene después
  —contener, parchear, medir el SLA y cerrar con evidencia— es el examen de Analista SecOps**, no
  este.

## 📟 Analista SecOps

- **Teoría:** Partes 8 y 9 (operación e incidentes), 17 (**318**, **324**, **313**, **315**) y 14 (**279**, **280**, **287**).
- **Práctica (operativa, con reloj):** sobre el
  **[trayecto Analista SecOps](../labs/blue-team-soc/TRAYECTO-ANALISTA-SECOPS.md)** de
  [`blue-team-soc`](../labs/blue-team-soc/README.md), lleva **una alerta hasta el cierre verificado**
  registrando las seis marcas de tiempo (recepción, validación, contención, asignación, remediación,
  verificación). Debes: relacionar la alerta con el **activo y su criticidad**, identificar las
  causas de configuración que la hicieron posible, priorizarlas con **KEV → EPSS → exposición →
  criticidad → CVSS** (usando `priorizar.py` de
  [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md)), **escribir y ejecutar tu propio
  runbook**, redactar el ticket de remediación con plan de reversión y criterio de verificación
  escrito **antes** del cambio, documentar **una excepción** con responsable, control compensatorio y
  vencimiento, y aportar la **prueba negativa** del cierre (el intento que ahora falla).
- **Informe:** **informe de incidente** con la línea de tiempo y las métricas derivadas + el
  **runbook** reutilizable + una **propuesta de mejora preventiva** que nombre la métrica que debería
  moverse + un **informe mensual de una página** para una jefatura sin formación técnica.
- **Suspende automáticamente** quien cierre el caso sin evidencia de verificación: es el error
  central que este examen busca detectar.

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
- **Variante AppSec Engineer (defensiva):** sustituye uno de los tres reportes por un **modelo de
  amenazas** de la aplicación (STRIDE, clase 237) con los requisitos de seguridad derivados y el
  mapeo a **OWASP ASVS** de la funcionalidad revisada. Es lo que separa a quien encuentra fallos de
  quien evita que existan.

## 🧮 Analista DevSecOps

- **Teoría:** Parte 11 (**238**–**241**, **243**, **245**, **246**), Parte 17 (**318**, **323**) y Parte 14 (**277**, **284**).
- **Práctica (de triaje y decisión):** sobre el
  **[trayecto Analista DevSecOps](../labs/devsecops-pipeline/TRAYECTO-ANALISTA-DEVSECOPS.md)**, parte
  de la salida cruda de las ocho capas de [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md)
  y entrega: registro **normalizado y deduplicado** con la regla de deduplicación escrita;
  clasificación en **real / falso positivo / real pero no aplicable** con al menos **tres descartes
  argumentados sobre el código**; **priorización reproducible** de un máximo de doce elementos con la
  fórmula explícita y la exposición declarada de cada hallazgo; la comparación entre `priorizar.py`
  normal y `--sin-red`; **cinco tickets** con criterio de verificación escrito antes del cambio; y
  **una excepción** con sus cuatro elementos innegociables. Cierra con una **verificación con control
  negativo**: reintroduce el patrón vulnerable y demuestra que el escáner vuelve a detectarlo.
- **Informe:** **informe de riesgo del SDLC** en dos vistas —una para desarrollo y una de página
  única para dirección, que termine con una decisión concreta que pedir— + **matriz de evidencia**
  contra al menos cinco prácticas de **NIST SP 800-218 (SSDF)** + la **sección de cobertura**
  (qué capa no se ejecutó y por qué).
- **No se acepta** un informe que confunda *sin hallazgos* con *no escaneado*.

## 🏗️ Ingeniero DevSecOps

- **Teoría:** Parte 11 completa (**236**–**248**), Parte 10 (**227**–**230**, **233**), **063** y Parte 17 (**330**).
- **Práctica (de construcción, obligatoriamente con código):** sobre el
  **[trayecto Ingeniero DevSecOps](../labs/devsecops-pipeline/TRAYECTO-INGENIERO-DEVSECOPS.md)** y en
  **un repositorio propio**, entrega un pipeline funcionando con: controles integrados en el punto
  correcto del ciclo y **versiones fijadas**; **tres niveles de bloqueo** justificados y con línea
  base que no bloquee la deuda preexistente; **cero credenciales de larga vida** (federación OIDC o
  inventario de secretos con su vía de rotación probada); cobertura de las **cinco superficies**
  (código, dependencias, IaC, imagen y aplicación en ejecución); **SBOM consultable** por artefacto;
  **firma verificada en el despliegue**, demostrando que un artefacto manipulado **se rechaza**; una
  **política OPA/Rego con sus pruebas** que rechace un manifiesto real; y un **mecanismo de excepción
  que caduque** y haga fallar el pipeline al vencer.
- **Prueba de resiliencia (obligatoria):** introduce a propósito un **control defectuoso** que rompa
  los despliegues y demuestra la recuperación, midiendo **tiempo hasta la detección**, **tiempo hasta
  la reversión** y **equipos afectados**.
- **Informe:** **modelo de amenazas del propio pipeline** en una página + **runbook de reversión** +
  **postmortem sin culpables** del control defectuoso, con una mejora concreta + **métricas de
  adopción y de tiempo añadido** al pipeline.
- **No aprueba** quien entregue un pipeline que solo funciona en su máquina: el criterio es que otra
  persona lo clone y obtenga el mismo resultado, incluida la verificación de firma.

## ☁️ Cloud Security Engineer

- **Teoría:** Partes 10, 11, 2.
- **Práctica:** en el lab [`cloud-security`](../labs/cloud-security/README.md): audita una configuración con Prowler/kube-bench y corrige 3 hallazgos.
- **Informe:** informe CSPM con hallazgos priorizados y remediación como código.
- **Frontera con DevSecOps:** aquí se evalúa la **plataforma ya desplegada** (identidades, postura,
  clúster, logging y respuesta). El pipeline que produjo esos artefactos —gates, SBOM, firma— es el
  examen de Ingeniero DevSecOps. Añade una **página de acuerdo de frontera**: qué controles de IaC y
  de contenedores asumes tú y cuáles asume DevSecOps, y quién responde si falla lo que queda en medio.

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

Estas nueve rutas están calcadas de anuncios de empleo reales, así que su examen se parece más a una
**prueba de selección** que a un examen académico: el entregable es el que produce el puesto.

## 🏦 Analista de Ciberseguridad (institución regulada)

- **Teoría:** Partes 8, 9, 14 (+ 3).
- **Práctica:** en el lab [`blue-team-soc`](../labs/blue-team-soc/README.md), lleva una alerta hasta el cierre como caso formal de **ISO 27035** (triaje → investigación → contención → lecciones aprendidas), registrando tiempos; en paralelo, prioriza los hallazgos de un escaneo de vulnerabilidades y define SLAs de remediación.
- **Informe:** informe de incidente + **evidencia de auditoría** mapeada a un control concreto de ISO 27001.

## 🤝 Analista de Cooperación y Alianzas Técnicas

- **Teoría:** Partes 14, 0 (+ 8).
- **Práctica (aplicada):** diseña un acuerdo de **intercambio de información de amenazas** entre dos organizaciones ficticias: qué se comparte, con qué clasificación (TLP), bajo qué base legal, con qué controles de protección de datos y qué pasa ante un incumplimiento. Evalúa además el riesgo del tercero (clase 284).
- **Informe:** memorando de entendimiento + informe de riesgo de terceros + una **nota ejecutiva de una página** dirigida a alguien sin formación técnica.

## ⚙️ Ingeniero SecOps / Security Engineer

> Es el examen **de ingeniería** de la familia SecOps: se aprueba escribiendo código. El de
> **Analista SecOps** (más abajo) evalúa lo contrario —operar, priorizar, coordinar y cerrar—
> y no comparte ni un solo entregable con este.

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

## 🏢 Jefe de Infraestructura y Ciberseguridad

- **Teoría:** Partes 14 y 17 (+ 1, 8, 9 y 10).
- **Práctica (mitad consola, mitad dirección):** sobre una organización ficticia en sector regulado, entrega **el paquete de jefatura**: análisis de riesgos con dueños, **plan de continuidad con RTO/RPO** y —esto es lo que se evalúa de verdad— la **restauración real de un respaldo en una máquina limpia, cronometrada**, comparando el tiempo obtenido con el RTO comprometido. Además, en [`blue-team-soc`](../labs/blue-team-soc/README.md) verifica la ingesta de al menos tres fuentes y lleva un incidente hasta el cierre, y **dirige** un [ejercicio de mesa](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md) de ransomware que incluya el punto de decisión de **notificar al regulador**.
- **Informe:** **procedimiento de notificación de incidentes** (quién decide, en qué plazo, con qué contenido) + **matriz de proveedores con SLA** y su escalamiento + informe mensual de una página para dirección. Se evalúa que la evidencia sirva ante un auditor externo, no solo ante ti mismo.

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

## 🧭 Familia SecOps y DevSecOps: siete exámenes, ninguno intercambiable

Estos siete puestos se confunden en las ofertas, así que sus exámenes están construidos para **no
poder aprobarse con el mismo entregable**:

| Examen | Entregable que lo define |
|---|---|
| **Analista SOC / Blue Team** | Una regla de detección validada sobre un ataque real |
| **Analista SecOps** | Un incidente cerrado con SLA, evidencia de verificación y mejora preventiva |
| **Ingeniero SecOps / Security Engineer** | Una API interna y una automatización en producción, auditadas |
| **Analista DevSecOps** | Una priorización reproducible con falsos positivos argumentados y excepción |
| **Ingeniero DevSecOps** | Un pipeline con firma verificada y una reversión demostrada |
| **AppSec Engineer** (sección *AppSec / Bug Bounty*) | Un modelo de amenazas con requisitos y mapeo a ASVS |
| **Cloud Security Engineer** | Un informe CSPM con remediación como código y el acuerdo de frontera |

Las diferencias de fondo entre los roles están desarrolladas en la
**[matriz de roles SecOps y DevSecOps](matriz-roles-secops-devsecops.md)**.

## 🔗 Relacionado

- [Rutas por rol](../rutas/README.md) · [Matriz de roles SecOps y DevSecOps](matriz-roles-secops-devsecops.md) · [Rúbrica de evaluación](rubrica-evaluacion.md) · [Syllabus](syllabus.md) · [Certificaciones](../certificaciones/README.md)
