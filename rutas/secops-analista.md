# 📟 Analista SecOps (operaciones de seguridad)

> El rol que **sostiene la operación diaria de seguridad de una empresa entera**: vigila que los
> controles funcionen, prioriza y persigue las vulnerabilidades hasta que están cerradas, coordina
> el parcheo con TI, revisa accesos, ejecuta runbooks, lleva los SLA y reporta lo que pasó. No vive
> dentro de una sola consola: vive **entre equipos**, y su producto es que el riesgo operativo baje
> de forma medible.
>
> **Nivel de entrada:** junior alto / semi-senior · **Foco:** controles de seguridad, gestión de vulnerabilidades, parcheo y hardening, IAM, EDR/SIEM, runbooks, SLA y métricas · **Certificación faro:** CompTIA Security+ → CySA+

## 🧭 Qué es y por qué importa

Toda organización con más de cien personas descubre lo mismo: **tener herramientas de seguridad no
es tener seguridad**. Alguien tiene que mirar si el agente de EDR está instalado en todos los
equipos, si el parche crítico de hace tres semanas llegó a los servidores, si el usuario que se fue
de la empresa sigue teniendo acceso a la VPN, si la alerta que se cerró ayer volvió a aparecer hoy.
Ese alguien es el **Analista SecOps**.

Es el rol que convierte un conjunto de productos en un **programa operativo**. Su trabajo tiene
cuatro ejes:

- **Vigilancia de controles.** Cobertura y salud del EDR, del antivirus, del cifrado de disco, de la
  ingesta del SIEM, de la MFA. No "¿lo tenemos?", sino **"¿en qué porcentaje de la flota está
  funcionando hoy y quién es el dueño del hueco?"**.
- **Ciclo de vulnerabilidades.** Recibir el resultado del escaneo, quitar el ruido, priorizar por
  riesgo real, abrir el ticket con el dueño correcto, acordar la ventana de parcheo, verificar que
  el parche se aplicó y cerrar con evidencia.
- **Operación de incidentes de bajo y medio impacto.** Recibir la alerta, validarla, contener,
  ejecutar el runbook, escalar a [DFIR](dfir.md) o al [SOC L3](soc-blue-team.md) cuando toca, y
  documentar el cierre.
- **Higiene de identidades y accesos.** Revisiones periódicas de permisos, altas y bajas, cuentas
  privilegiadas, cuentas huérfanas y de servicio.

Importa porque es donde **se pierde o se gana el riesgo real** de una empresa. La mayoría de las
brechas documentadas no explotan un cero-día: explotan un servidor sin parchear, una cuenta sin
revocar o un control que llevaba meses caído sin que nadie lo notara. Ese es literalmente el terreno
de este puesto.

### Qué problema resuelve

El problema del **hueco entre saber y hacer**. El escáner sabe que hay 4 000 vulnerabilidades; el
SIEM sabe que hubo 1 200 alertas; RR. HH. sabe que se fueron once personas. Ninguno de esos tres
sistemas cierra nada. El Analista SecOps es quien traduce ese conocimiento disperso en **acciones
con dueño, plazo y evidencia de cierre**, y quien puede responder con datos a la pregunta del
directorio: *¿estamos mejor que el trimestre pasado?*

## 🚫 Qué NO es este rol

- **No es un SOC L1 con otro nombre.** El analista de SOC vive dentro de la cola de alertas y su
  unidad de trabajo es el *evento*. Aquí la unidad de trabajo es el **control y el riesgo**: una
  vulnerabilidad, un hueco de cobertura, un acceso que sobra, un SLA que se está venciendo.
- **No es quien construye las automatizaciones.** Las **usa**, las pide y detecta cuándo hacen
  falta; quien las diseña y las mantiene es el [Ingeniero SecOps](secops-engineer.md). Escribir un
  script para tratar un CSV es normal; mantener una API interna en producción, no.
- **No es DFIR.** Contiene y ejecuta el runbook; la investigación forense profunda de un incidente
  grave se escala a [DFIR](dfir.md).
- **No es GRC.** Alimenta el cumplimiento con evidencia real de operación, pero no redacta el SGSI
  ni gestiona el registro de riesgos corporativo: eso es [GRC](grc.md).
- **No es "el que pasa el Nessus".** Ejecutar el escáner es el 10 % del trabajo; el 90 % es
  priorizar, negociar la ventana con TI y **verificar que se cerró**.

### Frente a los perfiles vecinos

- Frente al [Analista SOC / Blue Team](soc-blue-team.md): el SOC **detecta**; SecOps **corrige y
  sostiene**. El SOC te entrega el incidente cerrado; tú te quedas con la causa (el parche que
  faltaba, el permiso de más) y la eliminas para que no vuelva.
- Frente al [Ingeniero SecOps / Security Engineer](secops-engineer.md): tú **operas y decides**; ese
  rol **construye la plataforma y automatiza**. Si tu semana se llena de tareas repetitivas, tu
  salida no es aguantarlas: es especificárselas a ingeniería (o cruzar tú a ese rol).
- Frente al [Analista de Gestión de Vulnerabilidades](gestion-vulnerabilidades.md): ese perfil es
  **la especialización profunda de uno de tus ejes**. SecOps es más ancho (controles, accesos,
  incidentes, métricas) y menos profundo en el ciclo de la vulnerabilidad.
- Frente al [Analista DevSecOps](devsecops-analista.md): mismo oficio —triaje, priorización, SLA,
  excepciones— aplicado a **superficies distintas**. Tú trabajas sobre la infraestructura y los
  endpoints en producción; el analista DevSecOps, sobre el código, las dependencias y el pipeline
  **antes** de que lleguen a producción.
- Frente al [Analista de Seguridad de Infraestructura](seguridad-infraestructura.md): ese rol
  **administra las plataformas** (firewall, NAC, fuentes del SIEM); tú **explotas su salida** y
  persigues el riesgo que revelan.

## 🪜 Nivel de entrada y prerrequisitos

Es un rol de **entrada realista al sector defensivo**, pero no de cero absoluto: se espera que ya
sepas moverte por un sistema operativo y una red.

- **Imprescindible:** administración básica de Linux y Windows, redes TCP/IP y DNS, entender qué es
  un CVE y qué es un CVSS, y saber leer un log sin asustarte.
- **Muy recomendable:** un año previo de mesa de ayuda, sysadmin, NOC o SOC L1. Es la vía de entrada
  más común y la que mejor prepara, porque ya conoces el dolor de coordinar con TI.
- **Deseable:** scripting a nivel de utilidad (Bash, PowerShell o Python) para tratar listados,
  cruzar inventarios y no hacer a mano lo que sale de un CSV.
- **No hace falta:** saber programar a nivel de ingeniería, ni explotar vulnerabilidades. Sí hace
  falta **entender** cómo se explotan para saber cuáles priorizar.

En el programa, esto se traduce en hacer la **Parte 0 completa** antes de empezar la ruta.

## 🧾 Responsabilidades habituales

- Monitorear la **salud y la cobertura de los controles** de seguridad (EDR, antivirus, cifrado,
  MFA, respaldo, ingesta del SIEM) y perseguir los huecos hasta cerrarlos.
- Ejecutar y explotar el **escaneo de vulnerabilidades**: descartar ruido, priorizar por riesgo real
  y asignar el hallazgo al dueño del activo.
- **Coordinar el parcheo y el hardening** con TI, infraestructura y desarrollo: ventanas, plan de
  reversión y verificación posterior.
- **Investigar y dar seguimiento a incidentes** de bajo y medio impacto; escalar los graves con el
  contexto ya recolectado.
- Ejecutar y mantener **runbooks** operativos (cuenta comprometida, equipo infectado, acceso
  indebido, fuga de credenciales).
- **Revisión de accesos e IAM**: altas, bajas, cuentas privilegiadas, cuentas de servicio, revisión
  periódica de permisos.
- Llevar **SLA, métricas y reportes** operativos: MTTD, MTTR, tiempo medio de remediación por
  criticidad, cobertura de control, deuda de vulnerabilidades.
- **Coordinar** con TI, SOC, [DFIR](dfir.md), [DevSecOps](devsecops-analista.md) y
  [Cloud Security](cloud-security.md): buena parte del valor del rol es que **alguien esté
  persiguiendo el cierre** a través de fronteras de equipo.

## 🗓️ Un día en el puesto

- **Primera hora — el tablero.** Revisas el estado de los controles y las alertas heredadas de la
  noche. Miras tres cosas: qué se rompió, qué SLA vence hoy y qué quedó sin dueño.
- **Triaje de lo pendiente.** Tomas las alertas que el SOC escaló o que quedaron abiertas: validas,
  descartas lo que es ruido conocido y abres caso formal para lo que no.
- **Bloque de vulnerabilidades.** Llega el escaneo semanal con cientos de hallazgos. Filtras por lo
  que de verdad importa —expuesto a internet, con explotación conocida, en un activo crítico— y
  conviertes eso en un puñado de tickets con dueño y fecha, no en un PDF de 200 páginas.
- **Reunión con TI o con el equipo de plataforma.** La parte del trabajo que nadie cuenta: negociar
  la ventana de mantenimiento, aceptar que el servidor heredado no se puede reiniciar hasta el
  sábado y acordar un **control compensatorio** mientras tanto.
- **Un incidente pequeño.** Un usuario cayó en un phishing. Ejecutas el runbook: aislar el equipo,
  revocar sesiones, forzar cambio de credencial, revisar qué tocó esa cuenta, documentar y cerrar.
  Si aparece algo raro de verdad, escalas a DFIR con el contexto ya listo.
- **Revisión de accesos.** Cruzas la lista de bajas de RR. HH. contra el directorio y encuentras dos
  cuentas que siguen activas. Las cierras y anotas por qué el proceso falló — esa nota es lo que
  después se convierte en automatización.
- **Cierre.** Actualizas las métricas de la semana, dejas escrito el estado de cada caso y preparas
  el reporte del mes. Si algo se te olvida documentar, para la organización **no ocurrió**.

Dicho sin adornos: hay **mucha coordinación y mucha insistencia**. Buena parte del oficio es
perseguir a otras personas para que cierren algo que no es su prioridad, sin quemar la relación.
Quien no soporta eso, se frustra.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Gestión de vulnerabilidades de punta a punta:** escaneo autenticado y no autenticado, CVE, CVSS
  (y por qué la nota base no basta), **CISA KEV** y **EPSS**, exposición real del activo y
  criticidad de negocio. Saber que priorizar es *decidir qué no vas a arreglar esta semana*.
- **Parcheo y hardening:** ciclos de parche por plataforma, líneas base (**CIS Benchmarks**),
  gestión de configuración, control de cambios y plan de reversión.
- **Endpoint y EDR:** qué telemetría existe, cómo se lee una detección, cómo se aísla un host, qué
  significa realmente "cobertura del agente".
- **SIEM y análisis de logs:** consultar, correlacionar y detectar cuándo una fuente dejó de
  reportar. No necesitas escribir la ingeniería de detección; sí saber interrogar al SIEM.
- **IAM operativo:** ciclo de vida de identidades, mínimo privilegio, cuentas privilegiadas y de
  servicio, MFA, revisión de accesos y evidencia de esa revisión.
- **Respuesta a incidentes:** el ciclo NIST/SANS, contención, erradicación, recuperación y los
  criterios de escalamiento. Runbooks y playbooks.
- **Redes y sistemas:** lo suficiente para entender qué es un activo expuesto, qué protege un
  firewall y por qué un servidor sin segmentar convierte una vulnerabilidad media en crítica.
- **Métricas y SLA:** MTTD, MTTR, tiempo de remediación por criticidad, cobertura de control, edad
  de la vulnerabilidad, tasa de reapertura. Y cómo se distorsionan sin querer.
- **Marcos de referencia:** NIST CSF 2.0 para estructurar el programa, **CIS Controls** para las
  prioridades operativas e ISO/IEC 27001 para el lenguaje del auditor.

### Herramientas del oficio

```text
Vulnerabilidades:  escáner de red/host (tipo Nessus, OpenVAS, Qualys), inventario de activos
Endpoint:          EDR/XDR, antivirus, gestión de parches, MDM, cifrado de disco
Detección:         SIEM (Splunk, Elastic, Wazuh, Sentinel), consultas y tableros
Identidad:         IdP corporativo, MFA, PAM, revisión de accesos
Inteligencia:      CISA KEV, EPSS, CVSS, avisos del fabricante, feeds del sector
Operación:         ticketing (Jira, ServiceNow), CMDB, runbooks, calendario de cambios
Reporte:           hoja de cálculo, tableros del SIEM/EDR, informe mensual
Scripting:         Bash, PowerShell o Python a nivel de utilidad (cruzar listados, no construir)
```

Las marcas cambian cada dos años y **ninguna de ellas es el objetivo de aprendizaje**. Lo que se
transfiere entre empresas es el proceso: cómo priorizas, cómo negocias una ventana y cómo demuestras
que algo se cerró.

### Habilidades no técnicas

- **Constancia y seguimiento.** El talento central del puesto: nada se cierra solo. Un hallazgo sin
  dueño y sin fecha es un hallazgo que sigue abierto dentro de un año.
- **Negociación sin autoridad formal.** No mandas sobre TI ni sobre desarrollo, pero necesitas que
  actúen. Se consigue con datos, con contexto de impacto y con no gritar "crítico" cada semana.
- **Criterio de priorización.** Decir *esto puede esperar* con argumentos es tan profesional como
  decir *esto hay que parar todo y arreglarlo*.
- **Escritura clara.** Tu trabajo se materializa en tickets, runbooks y reportes. Si el ticket no se
  entiende, el parche no se aplica.
- **Tolerancia a lo inconcluso.** Siempre habrá cosas abiertas. El objetivo no es cero pendientes:
  es que **lo que quede abierto sea lo que decidiste dejar abierto**.

## 📦 Artefactos que produces

- **Reporte de vulnerabilidades priorizado** con dueño, plazo y criterio de priorización explícito.
- **Tickets de remediación** con activo, impacto, evidencia y criterio de verificación.
- **Runbook** operativo por escenario (cuenta comprometida, endpoint infectado, acceso indebido).
- **Registro de excepciones y aceptaciones de riesgo temporales**, con responsable, vencimiento y
  control compensatorio.
- **Informe de incidente** de bajo/medio impacto con línea de tiempo, acciones y lección aprendida.
- **Informe mensual de operación** con métricas, tendencia y las tres cosas que hay que decidir.
- **Evidencia de control** para auditoría: exportaciones, capturas y trazas de que el control se
  ejecutó.

## 📊 Cómo se te mide

| Métrica | Qué mide | Trampa habitual |
|---|---|---|
| **Cobertura de control** (% de flota con EDR, cifrado, MFA) | Si el control existe **en la realidad** | Medir sobre el inventario de la consola, no sobre el real |
| **MTTR de remediación** por criticidad | Velocidad de cierre | Bajarlo cerrando lo fácil y dejando lo difícil |
| **Deuda de vulnerabilidades** (abiertas y su edad) | Si el programa gana o pierde terreno | Contar hallazgos en vez de riesgo |
| **Cumplimiento de SLA** por severidad | Si los plazos acordados se sostienen | SLA fijado solo por seguridad, sin acuerdo de TI |
| **Tasa de reapertura** | Si se arregló o se maquilló | Cerrar el ticket antes de verificar |
| **Excepciones vigentes y vencidas** | Riesgo aceptado a la vista | Excepciones sin fecha de vencimiento |
| **Tiempo hasta contención** en los incidentes que operas | Eficacia del runbook | No registrar la hora real de cada paso |

## 📚 Tu ruta en el programa

Ruta ancha y operativa: no vas a fondo en ninguna especialidad, vas **sólido en todas las que
tocas**.

1. 📚 [**Parte 0 — Fundamentos**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md)
   (001–025) · la base: [003 frameworks NIST/ISO/MITRE](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md),
   Linux (005–006), Windows (008), [PowerShell (009)](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md),
   redes (010–013), [Python (015)](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md),
   [regex para logs (019)](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md)
   y [ética y alcance (025)](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).
2. 📚 [**Parte 3 — solo la clase 071**](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md)
   · el escáner que vas a explotar cada semana, y sus falsos positivos.
3. 📚 [**Parte 8 — Blue Team, detección y SOC**](../classes/parte-8-blue-team-deteccion-y-soc/README.md)
   · **181** cómo se organiza un SOC · **182** telemetría · **183** SIEM · **189** EDR ·
   **195** threat intelligence · **196** SOAR (para saber qué pedir) · **197** métricas y madurez.
4. 📚 [**Parte 9 — DFIR**](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/README.md)
   · **202** ciclo de respuesta · **215** playbooks · **216** contención y recuperación ·
   **217** análisis de causa raíz · **219** ejercicios de mesa.
5. 📚 [**Parte 17 — Profundización**](../classes/parte-17-profundizacion-para-certificaciones/README.md)
   · **el núcleo especializado del rol**: **318** gestión del programa de vulnerabilidades ·
   **324** hardening y gestión de configuración · **313** ciclo de vida de identidades ·
   **315** MFA y PAM · **319** phishing · **321** comunicación y reporte · **322** threat intelligence.
6. 📚 [**Parte 14 — GRC**](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md)
   · **279** NIST CSF · **280** controles CIS · **282** políticas y procedimientos ·
   **285** auditoría · **287** métricas KPI/KRI: el marco que da forma a tu operación.
7. 📚 [**Parte 11 — DevSecOps**](../classes/parte-11-devsecops-y-seguridad-del-sdlc/README.md)
   · **240** dependencias · **245** gestión de vulnerabilidades a escala: la superficie que compartes
   con el [Analista DevSecOps](devsecops-analista.md).
8. 📚 [**Parte 10 — Nube**](../classes/parte-10-seguridad-en-la-nube-y-contenedores/README.md)
   · **222** IAM · **231** CSPM · **234** logging: hoy medio parque de activos vive ahí.

Clases concretas por las que empezar:

- 🎯 [318 · Gestión del programa de vulnerabilidades](../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md) — **la clase central de este rol**.
- 🧱 [324 · Operaciones de seguridad, hardening y gestión de configuración](../classes/parte-17-profundizacion-para-certificaciones/324-operaciones-de-seguridad-hardening-y-gestion-de-configuracion/README.md) — el otro pilar: líneas base y desviaciones.
- 🔎 [071 · Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md) — la materia prima de tu semana.
- 📖 [215 · Playbooks de respuesta a incidentes](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/215-playbooks-de-respuesta-a-incidentes/README.md) y [216 · Contención, erradicación y recuperación](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/216-contencion-erradicacion-y-recuperacion/README.md) — lo que ejecutas cuando suena algo.
- 🔑 [313 · Gestión del ciclo de vida de identidades](../classes/parte-17-profundizacion-para-certificaciones/313-gestion-del-ciclo-de-vida-de-identidades-iam-empresarial/README.md) y [315 · MFA y gestión de accesos privilegiados (PAM)](../classes/parte-17-profundizacion-para-certificaciones/315-mfa-y-gestion-de-accesos-privilegiados-pam/README.md) — la revisión de accesos que nadie quiere hacer y todos los auditores piden.
- 📊 [197 · Métricas y madurez del SOC](../classes/parte-8-blue-team-deteccion-y-soc/197-metricas-y-madurez-del-soc/README.md) y [287 · Métricas de seguridad (KPIs y KRIs)](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md) — cómo se demuestra que el programa avanza.
- 🗣️ [321 · Comunicación y reporte para analistas de seguridad](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md) — la mitad del puesto es escribir bien.
- 🧯 [217 · Análisis de causa raíz](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/217-analisis-de-causa-raiz/README.md) — para que el mismo incidente no vuelva tres veces.

### Laboratorios

- 🧪 [`blue-team-soc`](../labs/blue-team-soc/README.md) — la alerta de entrada de tu trayecto.
  Sigue el **[Trayecto Analista SecOps](../labs/blue-team-soc/TRAYECTO-ANALISTA-SECOPS.md)**: alerta
  → validación → activo y vulnerabilidad → contención → parcheo → SLA → cierre con evidencia →
  mejora preventiva. Es el ciclo completo del puesto en un solo ejercicio.
- 🧪 [`rootcause-windows`](../labs/rootcause-windows/README.md) — el triaje del endpoint afectado y
  la evidencia del cierre.
- 🧪 [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md) — usa **solo** `priorizar.py`
  (KEV → EPSS → CVSS ajustado por exposición): es el criterio de priorización del rol, aplicado a
  otra superficie.
- 🧪 [`cloud-security`](../labs/cloud-security/README.md) — la misma disciplina de control y
  desviación, en la nube.
- 🚩 [CTF de forense y redes](../ctf/README.md) — el músculo de reconstruir qué pasó.

## 🧩 Proyecto integrador

**"Un trimestre de operación en dos semanas".** Sobre una organización ficticia con un inventario
dado, entrega:

1. Un **inventario de activos** con criticidad de negocio asignada y justificada (aunque sean 20
   activos: lo que se evalúa es el criterio).
2. El resultado de un escaneo —real, del laboratorio— **priorizado** con KEV → EPSS → CVSS ajustado
   por exposición, y **la lista de lo que decidiste no arreglar**, con su porqué.
3. **Cinco tickets de remediación** completos y **una excepción de riesgo** documentada con
   responsable, vencimiento y control compensatorio.
4. Un **incidente llevado de punta a punta** con el runbook que escribiste tú y con las horas reales
   registradas.
5. Un **panel de métricas** del periodo y un **informe mensual de una página** que una persona de
   gerencia sin formación técnica pueda leer y saber qué decidir.

Criterio de aceptación: otra persona puede tomar tu paquete, reproducir el escaneo y llegar a la
misma lista de prioridades leyendo solo tu documentación.

## 🧪 Examen final del rol

Rinde el **[examen final de Analista SecOps](../docs/examen-final-por-rol.md)** — 100 puntos:
teoría (25), práctica reproducible (50) e informe (25). Se aprueba con ≥ 70/100 y ≥ 30/50 en la
práctica.

## 💼 Evidencias para tu portafolio

Con lo anterior tienes material real que enseñar en una entrevista, sin inventar experiencia:

- Un repositorio con tus **runbooks** (dos o tres bien escritos valen más que quince a medias).
- El **informe de priorización** con el criterio explícito y la sección de "qué quedó fuera".
- Un **informe de incidente** con línea de tiempo y horas.
- El **tablero de métricas** y su interpretación.
- Un **registro de excepciones** de ejemplo, que demuestra que entiendes que la seguridad se negocia
  y se documenta, no se impone.

Presenta cada pieza diciendo **qué decidiste y por qué**, no qué herramienta usaste. Eso es lo que
distingue a un analista de un operador de consola.

## 🎤 Preguntas típicas de entrevista

- Te llegan 4 000 hallazgos del escaneo. ¿Qué haces el lunes por la mañana?
- ¿Qué diferencia hay entre CVSS, EPSS y KEV, y cuándo usas cada uno?
- Un servidor crítico tiene una vulnerabilidad crítica y no se puede parchear hasta dentro de dos
  meses. ¿Qué propones?
- ¿Cómo verificas que un parche se aplicó de verdad? ¿Y si el escáner lo sigue reportando?
- ¿Cómo mides la cobertura de tu EDR y por qué el número de la consola puede mentir?
- Un usuario dice que la MFA le impide trabajar y su jefatura pide una excepción. ¿Cómo lo resuelves?
- Cuéntame un incidente que hayas cerrado: qué contuviste primero y por qué en ese orden.
- ¿Qué métricas llevarías a tu jefatura cada mes y cuáles no?
- ¿Cuándo escalas a DFIR en vez de seguir tú?

## 🎓 Certificaciones

Con archivo en el programa:

- 🎓 [**CompTIA Security+** (SY0-701)](../certificaciones/comptia-security-plus-sy0-701.md) — la
  puerta de entrada: vocabulario común, controles y operaciones. El primer hito natural.
- 📋 [**CompTIA CySA+** (CS0-003)](../certificaciones/comptia-cysa-plus-cs0-003.md) — **la
  certificación faro**: operaciones de seguridad, gestión de vulnerabilidades, respuesta a
  incidentes y reporte. Es el examen que más se parece a este puesto.
- 🥇 [**BTL1**](../certificaciones/btl1.md) — si tu operación pesa más del lado del análisis de
  alertas y la investigación.

Distingue siempre **formación** de **certificación**: este programa es formación —te da el cuerpo de
conocimiento y la práctica—; la certificación es un examen de un tercero que se rinde y se paga
aparte. Ninguna de las dos cosas garantiza empleo. Consulta el
[mapeo completo a certificaciones](../certificaciones/README.md).

## 📈 Progresión de carrera y salario

Ruta habitual: **mesa de ayuda / sysadmin / SOC L1 → Analista SecOps → Analista SecOps Sr.** Desde
ahí, tres salidas claras:

- Hacia la **ingeniería**: [Ingeniero SecOps / Security Engineer](secops-engineer.md), si lo que
  quieres es construir y automatizar lo que hoy haces a mano. Es la progresión más frecuente.
- Hacia el **análisis y la detección**: [SOC / Blue Team](soc-blue-team.md) L2–L3 o
  [DFIR](dfir.md), si te tira más la investigación.
- Hacia la **gestión**: [gestión de vulnerabilidades](gestion-vulnerabilidades.md) como
  especialidad, [GRC](grc.md) o [jefatura de seguridad](ciso-jefe-seguridad.md).

Y una cuarta, lateral y muy pedida: cruzar al mundo del desarrollo como
[Analista DevSecOps](devsecops-analista.md), porque el oficio de triar, priorizar y perseguir el
cierre es exactamente el mismo sobre otra superficie.

Sobre **salario**: este programa no publica un estudio salarial propio y no va a inventar cifras.
Como referencia orientativa, el rango de este perfil suele situarse **por debajo** del de
[Ingeniero SecOps](secops-engineer.md#-progresión-de-carrera-y-salario) —que sí incluye una tabla
orientativa por región— porque no exige la mitad de desarrollo. Consulta ofertas reales de tu país y
tu moneda antes de negociar: los rangos varían enormemente por sector, tamaño de empresa y año.

## ⚠️ Mitos y errores comunes

- **"Cerrar el ticket es cerrar el riesgo."** No: cerrar el ticket sin verificar es la forma más
  común de bajar el MTTR y subir la tasa de reapertura.
- **"Si es crítico según CVSS, es crítico para nosotros."** El CVSS no sabe si tu activo está
  expuesto ni si es el que factura. Priorizar sin contexto es hacer el trabajo del escáner.
- **"El objetivo es cero vulnerabilidades abiertas."** No existe. El objetivo es que la deuda
  **envejezca menos** y que lo abierto sea una decisión, no un descuido.
- **"Seguridad decide, TI obedece."** Casi nunca. Sin acuerdo, la ventana de parcheo no ocurre y el
  riesgo sigue ahí, ahora además con mala relación entre equipos.
- **"Escanear más seguido es mejor."** Escanear más seguido sin capacidad de remediar solo produce
  más deuda visible y más ruido.
- **"Es un rol de paso."** Puede serlo, pero también es un puesto con recorrido propio: la operación
  bien hecha es escasa y se paga.

## ⚖️ Límites éticos y legales

- **Escanea solo lo autorizado.** Un escaneo de vulnerabilidades es una actividad intrusiva: exige
  autorización escrita, ventana acordada y alcance definido, incluso dentro de tu propia empresa
  ([Clase 025](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)).
- **No explotes para "demostrar" el hallazgo** sin autorización explícita: validar no es explotar.
  Eso pertenece a una prueba de penetración con contrato.
- **Manejo de datos personales.** Revisar accesos y logs implica tocar datos de personas: aplica el
  mínimo necesario, registra tus consultas y respeta la normativa de privacidad vigente.
- **La aceptación de riesgo la firma quien tiene la autoridad**, no tú. Tu trabajo es documentar la
  opción, no cargar con la decisión de negocio.
- **Los laboratorios son laboratorios.** Todo entorno vulnerable de este programa escucha en
  `127.0.0.1`, sin credenciales reales y sin exposición a internet. No los publiques.

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Ingeniero SecOps](secops-engineer.md) · [Analista SOC / Blue Team](soc-blue-team.md) · [Analista DevSecOps](devsecops-analista.md) · [Gestión de vulnerabilidades](gestion-vulnerabilidades.md) · [DFIR](dfir.md)
- 🗺️ [Matriz comparativa SecOps y DevSecOps](../docs/matriz-roles-secops-devsecops.md)
- 🏠 [Inicio del programa](../README.md)
