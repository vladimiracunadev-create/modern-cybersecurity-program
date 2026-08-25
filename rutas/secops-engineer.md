# ⚙️ Security Engineer / SecOps (endpoint y automatización)

> El ingeniero de la seguridad operativa: administras el EDR de toda la flota, respondes
> incidentes de endpoint y —sobre todo— **automatizas**. Escribes código (Python, Bash),
> construyes APIs internas e integras las herramientas de seguridad con el resto de los
> sistemas de la empresa. La regla del puesto: *si algo se hace dos veces, se automatiza*.
>
> **Nivel de entrada:** intermedio; perfil híbrido seguridad + desarrollo · **Foco:** EDR/XDR multi-SO, automatización, APIs REST, respuesta a incidentes de endpoint, SIEM · **Certificación faro:** CompTIA CySA+ (+ BTL1 en la parte operativa)

## 🧭 Qué es y por qué importa

Este es el rol donde la ciberseguridad **se convierte en software**. No es un analista que mira
alertas en un panel, ni un desarrollador que escribe features de producto: es quien mantiene los
**controles de seguridad de la flota** (portátiles, servidores, estaciones) funcionando de verdad, y
quien elimina el trabajo manual construyendo herramientas.

Se apoya sobre tres pilares:

- **Administración de endpoints y EDR/XDR.** Desplegar y operar la plataforma de detección y
  respuesta en endpoint (CrowdStrike, SentinelOne, Microsoft Defender) sobre **Windows, macOS y
  Linux** a la vez. Cobertura, visibilidad centralizada, políticas aplicadas y verificadas.
- **Ingeniería y automatización.** Scripts y servicios en **Python/Bash**, **APIs REST** internas
  que exponen capacidades de seguridad al resto de los equipos, e integraciones entre el stack de
  seguridad y los sistemas de la empresa (RRHH, IT, ticketing, identidad).
- **Respuesta operativa.** Investigar alertas, contener equipos comprometidos, hacer el análisis
  forense de un endpoint y cerrar el ciclo — con el músculo de [SOC / Blue Team](soc-blue-team.md)
  y [DFIR](dfir.md), pero desde el lado del que además **construye la herramienta**.

Importa porque es uno de los perfiles **mejor pagados y más difíciles de cubrir** del sector: exige
las dos mitades. Hay muchos analistas que no programan y muchos desarrolladores que no entienden de
seguridad; quien junta ambas se vuelve escaso. Y es un rol que **escala**: en una empresa que crece,
la única forma de no multiplicar el equipo de seguridad por el número de empleados es automatizar.

> **De dónde sale esta guía.** Está calcada de una oferta real de empleo
> ([Xepelin, *Cybersecurity Engineer (SecOps Sr)*, Santiago de Chile](https://www.linkedin.com/jobs/view/4432595681)):
> administración de plataformas de seguridad de endpoint, gestión de antivirus/EDR con respuesta a
> alertas, construcción de **APIs internas de seguridad**, automatización de onboarding/offboarding,
> rotación de credenciales y reportes de cumplimiento, integración de herramientas, respuesta a
> incidentes con análisis forense, inventario de activos y políticas de endpoint (cifrado de disco,
> control de accesos, gestión de parches). Requisitos: EDR/XDR, Python/Bash, APIs REST, multi-SO
> (Linux/macOS/Windows), respuesta a incidentes, SIEM. Es el retrato fiel del puesto de **SecOps
> Engineer** en una empresa de tecnología o fintech.

### 🚫 Qué NO es este rol (y con quién se confunde)

- **Ingeniero SecOps ≠ [Analista SecOps](secops-analista.md).** Aquí **construyes**: automatizaciones,
  integraciones, APIs internas, ingeniería de detección. Allí se **opera y se decide** sobre el
  riesgo: priorizar vulnerabilidades, negociar ventanas de parcheo, ejecutar runbooks, llevar SLA y
  métricas. En una empresa pequeña lo hará la misma persona, pero son dos puestos con dos rutinas y
  dos techos distintos. Si en la entrevista no te preguntan por código y APIs, la vacante
  probablemente sea la de analista con el título de ingeniero.
- **No es un [Analista SOC](soc-blue-team.md).** El SOC consume la plataforma; tú la administras,
  la integras y construyes encima de ella.
- **No es [DevSecOps](devsecops-engineer.md).** Misma mentalidad de ingeniería, distinto dominio:
  ese rol automatiza la **construcción y la entrega** del software (pipeline, SBOM, firma,
  políticas); tú automatizas la **operación** (flota, EDR, identidades, respuesta). Muchas carreras
  pasan por los dos, y el salto es de los más naturales del sector.
- **No es DevOps ni administración de sistemas** con un producto de seguridad encima: el criterio
  de riesgo y la respuesta a incidentes forman parte del puesto.

> 🗺️ La [matriz de roles SecOps y DevSecOps](../docs/matriz-roles-secops-devsecops.md) desarrolla
> estas fronteras con misión, decisiones, entregables y métricas de cada puesto.

## 🗓️ Un día en el puesto

Es una jornada partida entre **operar** y **construir** — y la proporción entre ambas es la métrica
real de tu éxito: cuanto mejor lo haces, más tiempo construyes y menos apagas fuegos.

- **Revisión de alertas del EDR:** empiezas por lo que disparó durante la noche. Trias, descartas
  falsos positivos, investigas lo serio: qué proceso, qué usuario, qué equipo, qué se ejecutó antes.
  Si algo se confirma, **aíslas el endpoint** desde la consola y abres el incidente.
- **Respuesta e investigación:** recolectas artefactos del equipo afectado (procesos, persistencia,
  conexiones, historial), reconstruyes qué pasó y decides contención, erradicación y recuperación.
  En una empresa pequeña o mediana, **tú eres el que responde**, no hay un DFIR aparte.
- **Cobertura e inventario:** ¿cuántos equipos hay?, ¿cuántos tienen el agente instalado y
  reportando?, ¿cuántos tienen el disco cifrado y los parches al día? La **diferencia entre el
  inventario real y el que dice la consola** es donde viven los incidentes.
- **Desarrollo:** el bloque más valioso del día. Escribes el script que rota credenciales, la
  función que cierra los accesos de alguien que sale de la empresa el mismo día, la **API interna**
  que permite a otro equipo consultar el estado de seguridad de un equipo sin escribirte por Slack.
- **Integraciones:** conectar el EDR con el SIEM, el SIEM con el ticketing, el sistema de RRHH con
  el de identidad. Cada integración que funciona es trabajo manual que desaparece para siempre.
- **Reportes de cumplimiento:** el % de flota cubierta, cifrada y parcheada — automatizado, no
  recolectado a mano cada mes.

Dicho sin adornos: si **no te gusta programar**, este rol te va a frustrar. La parte de análisis es
real, pero lo que separa a un SecOps Engineer de un analista de SOC es que aquí **se espera que
escribas código en producción**, con criterio de ingeniería: control de versiones, manejo de errores
y credenciales que no acaban escritas en el script.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **EDR/XDR de verdad, no de folleto.** Cómo funciona un agente, qué telemetría recoge, cómo se
  escriben y afinan políticas, cómo se investiga una detección y cómo se aísla un host. El producto
  concreto (CrowdStrike, SentinelOne, Defender) cambia; **el modelo mental se transfiere**.
- **Los tres sistemas operativos.** Windows (registro, servicios, Event Logs, Sysmon), Linux
  (procesos, systemd, permisos, logs) y **macOS** — el gran olvidado en las flotas corporativas y
  donde más equipos quedan sin cobertura.
- **Programación aplicada a seguridad.** **Python** como lenguaje principal (consumir APIs, procesar
  datos, orquestar) y **Bash** para el pegamento del sistema. No hace falta ser ingeniero de
  software senior; sí escribir código que otro pueda mantener.
- **APIs REST desde los dos lados:** consumirlas (las de tu EDR, tu SIEM, tu proveedor de identidad)
  y **construirlas** — autenticación, autorización, validación de entrada, versionado y no filtrar
  por la API interna lo que no filtrarías por la externa.
- **SIEM y correlación de eventos:** dónde acaba la telemetría del endpoint, cómo se consulta y cómo
  se correlaciona con lo que ve la red y la nube.
- **Respuesta a incidentes:** el ciclo NIST/SANS de preparación, detección, contención, erradicación
  y recuperación, y el análisis forense básico de un endpoint comprometido.
- **Higiene de la flota:** cifrado de disco, control de accesos, **gestión de parches** e inventario
  de activos. Poco glamuroso y responsable de la mayor parte del riesgo real.
- **Gestión de identidades y secretos:** el ciclo de alta y baja de personas (*onboarding /
  offboarding*), accesos privilegiados y **rotación de credenciales** — casi siempre lo primero que
  te tocará automatizar.

### Herramientas del oficio

```text
EDR/XDR:         CrowdStrike Falcon, SentinelOne, Microsoft Defender for Endpoint
SIEM:            Splunk, Microsoft Sentinel, Elastic Stack, Wazuh
Automatización:  Python (requests, FastAPI), Bash, PowerShell, SOAR
APIs/Integración: REST, webhooks, colas, tokens y OAuth cliente
Flota/endpoint:  MDM (Intune, Jamf), gestión de parches, BitLocker/FileVault/LUKS
Identidad:       IdP corporativo (SSO/SAML/OIDC), PAM, gestores de secretos (Vault, KMS)
Ingeniería:      Git, CI/CD, contenedores, gestión de secretos en el pipeline
```

Aquí la herramienta importa **menos que la capacidad de conectarla con las demás**. Todo producto
serio de seguridad tiene API; el valor que aportas es lo que construyes con ella.

### Habilidades no técnicas

- **Mentalidad de automatización.** La frase de la oferta —*si algo pasa dos veces, se automatiza*—
  no es un eslogan: es el criterio con el que priorizarás tu semana.
- **Criterio de ingeniería.** Tu script se convierte en infraestructura. Versiónalo, documéntalo,
  maneja los errores y no dejes credenciales dentro. Un automatismo mal hecho falla en silencio, y
  un control de seguridad que falla en silencio es peor que no tenerlo.
- **Servicio a otros equipos.** Construyes capacidades que consume el resto de la empresa. Si tu API
  no se entiende o tu proceso estorba, la gente lo rodea — y la seguridad se pierde.
- **Autonomía y ownership.** Es un rol donde a menudo eres **la persona** de seguridad operativa. Se
  espera que detectes qué falta y lo construyas sin que te lo pidan.
- **Equilibrio entre seguridad y fricción.** Bloquear todo es fácil; sostener una empresa que además
  funciona, no. En una fintech, además, hay reguladores y clientes mirando.

## 📚 Tu ruta en el programa

Ruta híbrida entre **operación defensiva** y **desarrollo**: hay que atravesar el bloque de Blue
Team y el de DevSecOps. Orden recomendado:

1. 📚 [**Parte 0 — Fundamentos**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md)
   (001–025) · **la base doble del rol**: sistemas (Linux 005–006, Windows 008) y, sobre todo,
   **programación**: Bash (007), PowerShell (009), Python (015–017), Git (018) y regex para logs (019).
2. 📚 [**Parte 1 — Redes**](../classes/parte-1-redes-y-seguridad-de-redes/README.md)
   (026–045) · lo suficiente para entender qué hace un endpoint en la red y leer su tráfico.
3. 📚 [**Parte 8 — Blue Team, detección y SOC**](../classes/parte-8-blue-team-deteccion-y-soc/README.md)
   (181–200) · **el núcleo operativo**: telemetría, SIEM, **EDR (189)** y **automatización con SOAR (196)**.
4. 📚 [**Parte 9 — DFIR**](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/README.md)
   (201–220) · el ciclo de incidentes y el análisis forense del endpoint que investigues.
5. 📚 [**Parte 11 — DevSecOps**](../classes/parte-11-devsecops-y-seguridad-del-sdlc/README.md)
   (236–248) · **la mitad de ingeniería**: pipelines, secretos en el código y **seguridad de APIs (247)**.
6. 📚 [**Parte 4 — Seguridad web**](../classes/parte-4-seguridad-de-aplicaciones-web/README.md)
   · en concreto **110 (APIs REST)**: si vas a construir APIs internas, empieza por saber cómo se rompen.
7. 📚 [**Parte 17 — Profundización**](../classes/parte-17-profundizacion-para-certificaciones/README.md)
   · operaciones y hardening (**324**), identidades (**313**, **315**), parches y vulnerabilidades (**318**)
   y **automatización de seguridad (330)**.

Clases concretas por las que empezar:

- 🐍 [015 · Python para seguridad: fundamentos](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md) y [007 · Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md) — los dos lenguajes que pide la oferta, literalmente.
- 🖥️ [189 · Análisis de endpoints con EDR](../classes/parte-8-blue-team-deteccion-y-soc/189-analisis-de-endpoints-con-edr/README.md) — **la clase central de este rol**.
- 🤖 [196 · Automatización con SOAR](../classes/parte-8-blue-team-deteccion-y-soc/196-automatizacion-con-soar/README.md) y [330 · Análisis de código y automatización de seguridad](../classes/parte-17-profundizacion-para-certificaciones/330-analisis-de-codigo-y-automatizacion-de-seguridad/README.md) — la mentalidad de "automatízalo" convertida en práctica.
- 🔌 [110 · Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md) y [247 · Seguridad de APIs en el ciclo de desarrollo](../classes/parte-11-devsecops-y-seguridad-del-sdlc/247-seguridad-de-apis-en-el-ciclo-de-desarrollo/README.md) — para construir las APIs internas sin abrir un agujero.
- 🪟 [190 · Análisis de logs de Windows (Event Logs y Sysmon)](../classes/parte-8-blue-team-deteccion-y-soc/190-analisis-de-logs-de-windows-event-logs-y-sysmon/README.md) · 🐧 [206 · Análisis de artefactos de Linux](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/206-analisis-de-artefactos-de-linux/README.md) — el lado multi-SO del puesto.
- 🚨 [202 · El ciclo de respuesta a incidentes (NIST y SANS)](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/202-el-ciclo-de-respuesta-a-incidentes-nist-y-sans/README.md) y [216 · Contención, erradicación y recuperación](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/216-contencion-erradicacion-y-recuperacion/README.md) — lo que haces cuando el EDR acierta.
- 🧱 [324 · Operaciones de seguridad, hardening y gestión de configuración](../classes/parte-17-profundizacion-para-certificaciones/324-operaciones-de-seguridad-hardening-y-gestion-de-configuracion/README.md) — políticas de endpoint, parches e inventario.
- 🔑 [313 · Gestión del ciclo de vida de identidades (IAM empresarial)](../classes/parte-17-profundizacion-para-certificaciones/313-gestion-del-ciclo-de-vida-de-identidades-iam-empresarial/README.md), [315 · MFA y gestión de accesos privilegiados (PAM)](../classes/parte-17-profundizacion-para-certificaciones/315-mfa-y-gestion-de-accesos-privilegiados-pam/README.md) y [063 · Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md) — onboarding/offboarding y rotación de credenciales, las automatizaciones estrella.
- 🔐 [241 · Secretos en el código y pre-commit hooks](../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md) — para no dejar el token del EDR dentro del script que lo consume.

### Laboratorio y CTF

- 🧪 [`blue-team-soc`](../labs/blue-team-soc/README.md) — monta el SIEM, ingiere telemetría de
  endpoint y escribe detecciones: la operación que después vas a automatizar.
- 🧪 [`rootcause-windows`](../labs/rootcause-windows/README.md) — un sensor forense de
  comportamiento en Windows: la mejor forma de entender **por dentro** qué hace un agente de EDR.
- 🧪 [`appsec-code`](../labs/appsec-code/README.md) — revisión de código y SAST, para que el código
  que escribas sea el que revisarías.
- 🧪 [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md) — auditar el pipeline entero en
  ocho capas y **automatizarlo**: es el trabajo de este rol aplicado al SDLC, y su script
  `auditar.sh` es un buen modelo de cómo debe comportarse una automatización de seguridad
  (distinguir siempre *sin hallazgos* de *no ejecutada*).
- 🚩 [CTF de forense y redes](../ctf/README.md) — reconstruir qué pasó a partir de artefactos:
  exactamente el músculo de la investigación de una alerta de endpoint.

## 🎓 Certificaciones

Con archivo en el programa (mapean a partes concretas):

- 📋 [**CompTIA CySA+** (CS0-003)](../certificaciones/comptia-cysa-plus-cs0-003.md) — **la
  certificación faro**: operaciones de seguridad, análisis de comportamiento, respuesta a incidentes
  y **automatización de la seguridad**, que es un dominio propio del examen. La que mejor encaja.
- 🥇 [**BTL1** (Blue Team Level 1)](../certificaciones/btl1.md) — cien por cien práctica: SIEM,
  análisis de logs, forense y respuesta. Demuestra que la mitad operativa la sabes hacer, no solo contar.
- 🎓 [**CompTIA Security+** (SY0-701)](../certificaciones/comptia-security-plus-sy0-701.md) — la de
  entrada: abre puertas de RRHH y asienta el vocabulario. Buen primer hito si aún no tienes ninguna.
- 🧯 [**SANS GCIH**](../certificaciones/sans-gcih-gcfa.md) — a medio plazo, si la parte de respuesta
  a incidentes acaba pesando más que la de ingeniería. Cara, pero muy reconocida.

Las **certificaciones de producto del propio EDR** (CrowdStrike CCFA/CCFR, SentinelOne, Microsoft
SC-200) son muy valoradas para este puesto en concreto y quedan **fuera del programa**: se sacan con
el fabricante, y normalmente las paga la empresa una vez dentro. Consulta el
[mapeo completo a certificaciones](../certificaciones/README.md) para ver cuánto cubre el programa.

## 📈 Progresión de carrera y salario

Ruta habitual: **Analista SOC o IT/sysadmin → Security Engineer / SecOps → SecOps Sr → Staff
Security Engineer o líder de Security Engineering**. Desde aquí se abre camino hacia
[Cloud Security](cloud-security.md) (la flota se vuelve infraestructura), hacia
[detección e ingeniería de detección](soc-blue-team.md) o hacia arquitectura de seguridad. Es de los
perfiles con **mejor techo técnico**, porque no obliga a pasar a gestión para seguir creciendo.

Rangos **orientativos y aproximados** (brutos anuales; varían mucho por sector, tamaño de empresa y
experiencia — referencia, no promesa):

```text
Región                      Semi-senior            Senior / staff
--------------------------  ---------------------  ------------------------
LATAM                       USD 18k – 36k / año    USD 40k – 75k+ / año
Chile (fintech/tech)*       USD 25k – 45k / año    USD 45k – 80k+ / año
España                      EUR 30k – 45k / año    EUR 48k – 75k+ / año
Remoto (USD)                USD 60k – 100k / año   USD 110k – 170k+ / año
```

\* Las **fintech y empresas de tecnología** suelen pagar por encima del promedio del país para este
perfil, precisamente por la escasez del híbrido seguridad + desarrollo. Los números remotos en USD
asumen contratación por empresas de EE. UU./Europa, con listón alto de inglés.

## ⚠️ Mitos y errores comunes

- **"Es un analista de SOC con otro nombre."** No. El analista consume la herramienta; aquí la
  administras, la integras y **construyes encima de ella**. Si en la entrevista no te preguntan por
  código y APIs, probablemente la vacante esté mal titulada.
- **"Hay que ser desarrollador senior."** Tampoco. Se pide **código funcional y mantenible**, no
  arquitectura de sistemas distribuidos. Python a nivel sólido y Bash decente cubren la mayoría del
  trabajo real.
- **"El EDR ya protege la flota."** Solo si está **desplegado, actualizado, configurado y sin huecos
  de cobertura**. La brecha entre lo que dice la consola y la realidad del inventario es el problema
  central del puesto — y por eso se automatiza el inventario.
- **"macOS y Linux son un detalle."** Son la mitad de la flota en muchas empresas de tecnología y
  donde suele fallar la cobertura. La oferta pide **multi-SO** por algo.
- **"Automatizar es escribir un script y olvidarse."** Un automatismo sin monitoreo ni manejo de
  errores es un control que puede llevar meses caído sin que nadie lo note.
- **"El curso me da todo lo que pide la oferta."** No del todo; lee la nota de abajo.

> **Honestidad, sin marketing:** este programa te da la **base técnica** del puesto —endpoints y
> EDR, SIEM y correlación, respuesta a incidentes y forense, Python/Bash aplicados a seguridad,
> seguridad de APIs REST, identidades, secretos, hardening y gestión de parches—. Lo que **no** te
> da es la **experiencia operando un producto comercial concreto** (CrowdStrike, SentinelOne,
> Defender) sobre una flota real de cientos de equipos, ni el **contexto de negocio** de una fintech
> (regulación financiera, clientes, escala). Tampoco convierte a nadie en desarrollador: si vienes
> de cero en programación, las clases de Python y Bash son el punto de partida, no la meta —
> practica escribiendo herramientas propias. El curso te hace **técnicamente capaz de aprender el
> producto en semanas**; la flota real y el negocio los pones tú.

## 🚀 Siguientes pasos

1. **Asegura las dos bases de la Parte 0**: sistemas (Linux, Windows) **y** programación. Si tuvieras
   que elegir por dónde empezar, empieza por **Python (015)** y **Bash (007)**: es lo que más te
   diferencia del resto de candidatos.
2. Haz la **Parte 8** completa con foco en **189 (EDR)**, **182–183 (telemetría y SIEM)** y
   **196 (SOAR)**, y monta el lab [`blue-team-soc`](../labs/blue-team-soc/README.md).
3. Cierra el ciclo operativo con la **Parte 9**: respuesta a incidentes (202), contención (216) y
   artefactos de Windows/Linux (205–206).
4. Añade la mitad de ingeniería con la **Parte 11** y la clase **110**: construye una API REST
   pequeña que consulte el estado de seguridad de un host y protégela como si fuera pública.
5. Remata con la **Parte 17**: hardening y configuración (324), identidades (313, 315) y
   automatización (330).
6. **Construye tu portfolio con código.** Para este puesto vale más un repositorio con tres
   herramientas propias —un inventario de agentes vía API, un automatismo de offboarding, un
   enriquecedor de alertas— que una certificación más. Es literalmente lo que harás en el trabajo.
7. Apunta a **CySA+** como certificación de rol (su dominio de automatización encaja de lleno) y,
   una vez dentro, a la certificación del EDR que use la empresa.

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Analista SecOps](secops-analista.md) · [Analista SOC / Blue Team](soc-blue-team.md) · [Ingeniero DevSecOps](devsecops-engineer.md) · [DFIR](dfir.md)
- 🗺️ [Matriz comparativa SecOps y DevSecOps](../docs/matriz-roles-secops-devsecops.md)
- 🏠 [Inicio del programa](../README.md)
