# 🧱 Analista de Seguridad de Infraestructura (plataformas, SIEM y cumplimiento)

> El puesto que sostiene la seguridad de la infraestructura desde dentro: administras los controles
> (firewalls, IPS, NAC, EDR, antivirus), **conectas y mantienes las fuentes de log del SIEM**,
> analizas eventos de plataformas muy distintas, investigas desviaciones de configuración,
> documentas runbooks y ejecutas los controles de cumplimiento que audita un tercero.
>
> **Nivel de entrada:** junior/semi-senior; ~1 año administrando servidores Linux y Windows · **Foco:** plataformas de seguridad, ingeniería de fuentes del SIEM, análisis de eventos y controles de cumplimiento (SOX/PCI) · **Certificación faro:** CompTIA Security+ → CySA+ (+ SC-200 del lado Microsoft)

## 🧭 Qué es y por qué importa

Todo SOC del mundo depende de una cosa que casi nadie explica: **que los logs lleguen**. Este rol es
el que se encarga de eso, y de bastante más. Es el punto donde se cruzan **administración de
infraestructura** y **seguridad**, y por eso suele contratarse a gente que viene de sistemas o redes
más que de un perfil puramente defensivo.

El trabajo tiene tres capas:

- **Ingeniería de las fuentes del SIEM.** Configurar y administrar qué se ingiere, desde dónde y en
  qué formato; **vigilar la integridad de la ingesta** — que una fuente que dejó de reportar hace
  seis semanas es un punto ciego que nadie ve hasta que hace falta. Esto no es analizar alertas: es
  **construir y sostener la tubería** por la que viajan.
- **Administración de los controles de infraestructura.** Firewalls, IPS, NAC, EDR/ATP, antivirus:
  implementarlos, configurarlos, mantenerlos y verificar su cobertura real. En un entorno
  corporativo real conviven además plataformas de todas las épocas —desde servidores Linux y
  Windows modernos hasta un **AS/400** con datos críticos—, y todas tienen que entrar al alcance.
- **Cumplimiento con evidencia.** Ejecutar los controles que exige la regulación del sector
  —**SOX** en empresas que cotizan, **PCI DSS** si se procesan pagos— y dejar el rastro documental
  que el auditor va a pedir. Aquí el trabajo técnico se convierte en evidencia formal.

En qué se diferencia de las rutas vecinas de este curso:

- Frente a [Analista SOC / Blue Team](soc-blue-team.md): el analista de SOC **consume** el SIEM —
  triaje, hunting, detección. Tú **lo alimentas y lo mantienes**, y administras además los controles
  de red y endpoint que producen esos eventos. Son dos oficios que se necesitan mutuamente.
- Frente a [SecOps / Security Engineer](secops-engineer.md): ese rol **automatiza y construye
  herramientas** con código; este **opera y sostiene plataformas** comerciales, con scripting como
  apoyo (deseable, no núcleo).
- Frente a [Gestión de Vulnerabilidades](gestion-vulnerabilidades.md): allí el eje es el ciclo de la
  vulnerabilidad; aquí es la **plataforma y la telemetría**, con el cumplimiento como marco.

Importa porque es **uno de los puestos más abundantes y peor explicados** del sector: no tiene
épica, pero sin él no hay detección posible. Y porque es la puerta natural para quien viene de
**administración de sistemas o redes**: aprovecha lo que ya sabes en lugar de pedirte empezar de
cero.

> **De dónde sale esta guía.** Está calcada de una oferta real de empleo
> ([Evertec, *Cyber Security Analyst*, Las Condes, Chile](https://www.linkedin.com/jobs/view/4437917273)):
> identificar amenazas a la infraestructura y mantener el cumplimiento de los controles de
> seguridad; **configurar y administrar las fuentes de log en el SIEM** (Sentinel, QRadar, Splunk,
> XSIAM); **monitorear la ingesta de eventos y la integridad de los datos**; analizar eventos de
> **AS/400, IPS, NAC, Windows, Linux, bases de datos y firewalls**; investigar anomalías y
> desviaciones de configuración; implementar controles (**firewalls, EDR/ATP, antivirus**); apoyar
> la coordinación de respuesta a incidentes; elaborar documentación técnica y **runbooks**; generar
> reportes para audiencias técnicas y ejecutivas; y **ejecutar controles de cumplimiento SOX**.
> Requisitos: título en sistemas o afín, **1 año mínimo administrando servidores Linux y Windows**,
> experiencia práctica en **Azure y/o AWS**, protocolos **TCP/IP, DNS, HTTPS, LDAPS**, experiencia
> demostrable con SIEM y buena redacción técnica. Deseables: **Python y PowerShell**, Security+ o
> Network+, **SC-200** y AWS CloudOps Associate.

## 🗓️ Un día en el puesto

Es un trabajo de **mantener cosas funcionando** y de responder cuando algo se sale de lo normal:

- **Revisión de salud de la ingesta:** ¿qué fuentes dejaron de reportar?, ¿alguna está enviando el
  doble de volumen sin razón?, ¿cambió un formato tras una actualización? Es lo primero del día y lo
  que nadie agradece hasta que falla.
- **Onboarding de una fuente nueva:** entró un servidor, una base de datos o un firewall al alcance.
  Hay que conectarlo, normalizar sus campos, validar que los eventos llegan completos y avisar al
  equipo de detección de que ya pueden escribir reglas sobre él.
- **Análisis de eventos:** algo raro en un firewall, un IPS que bloquea un patrón nuevo, un
  servidor que empezó a autenticar desde un origen inesperado. Investigas, descartas o escalas.
- **Desviaciones de configuración:** el control estaba definido de una forma y alguien lo cambió.
  Detectarlo, entender por qué y devolverlo a la línea base — o documentar la excepción.
- **Administración de controles:** una regla de firewall, una política de EDR, la cobertura del
  antivirus, una excepción del IPS que hay que revisar antes de aprobarla.
- **Documentación y runbooks:** el procedimiento de lo que acabas de resolver. En este rol la
  documentación no es opcional: es lo que permite que el turno siguiente haga lo mismo.
- **Evidencia de cumplimiento:** llega el ciclo de **SOX** o la auditoría de PCI y hay que
  demostrar, con capturas y registros, que el control existe y se ejecutó. Es un bloque fijo del
  calendario, no una sorpresa.
- **Reportes:** los mismos datos, en dos idiomas distintos — el detalle para el equipo técnico y el
  resumen para la gerencia.

Dicho sin adornos: hay **mucho mantenimiento, mucha coordinación con otras áreas** (redes, sistemas,
bases de datos, aplicaciones) y una parte de trabajo repetitivo de verificación. Si buscas
investigar amenazas todo el día, el rol de [SOC / Blue Team](soc-blue-team.md) se ajusta más. Si te
satisface que la infraestructura esté ordenada, medida y demostrable, este encaja — y es de los
puestos con más **estabilidad** del sector.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Administración de servidores Linux y Windows.** Es el requisito de entrada literal: procesos,
  servicios, permisos, dónde vive cada log y cómo se configura su envío.
- **Protocolos de red de verdad:** **TCP/IP**, **DNS**, **HTTPS** y **LDAPS**. Los cuatro que nombra
  la oferta, y no por casualidad: son el tráfico que vas a autorizar, inspeccionar y depurar todos
  los días. LDAPS además te obliga a entender **directorio y certificados**.
- **Plataformas de seguridad de red:** **firewalls** (reglas, NAT, políticas), **IDS/IPS**
  (detección, firmas, falsos positivos) y **NAC** (control de acceso a la red por postura del
  equipo).
- **Endpoint:** EDR/ATP y antivirus — despliegue, políticas y, sobre todo, **cobertura real**.
- **SIEM desde el lado de la ingeniería:** arquitectura, colectores, parsers, normalización y
  monitoreo de la propia plataforma. Saber **por qué** un evento llega mal formado vale más aquí que
  saber escribir una consulta compleja.
- **Nube (Azure y/o AWS):** cómo se generan y se recogen los logs de nube y cómo se aplican
  controles en un entorno híbrido, que es lo que tiene casi toda empresa real.
- **Cumplimiento como práctica técnica:** qué es un control, cómo se ejecuta, cómo se evidencia y
  qué espera un auditor de **SOX** o de **PCI DSS**.
- **Scripting de apoyo (deseable):** **PowerShell** y **Python** para automatizar verificaciones,
  extraer evidencia y procesar salidas. No es el núcleo, pero es lo que te separa del resto.

### Herramientas del oficio

```text
SIEM:            Microsoft Sentinel, QRadar, Splunk, XSIAM (y sus colectores/parsers)
Red:             firewalls, IDS/IPS, NAC, proxy, VPN
Endpoint:        EDR/ATP, antivirus, gestión de agentes y cobertura
Sistemas:        Linux, Windows Server, bases de datos, plataformas legadas (AS/400)
Nube:            Azure, AWS — logging, identidad y controles en entorno híbrido
Scripting:       PowerShell, Python (verificaciones, evidencia, automatización simple)
Cumplimiento:    matrices de control, evidencia de auditoría, SOX y PCI DSS
```

Aquí se valora la **amplitud** más que la profundidad en una sola herramienta: el puesto toca
plataformas de generaciones muy distintas y hay que moverse entre todas sin perder el criterio.

### Habilidades no técnicas

- **Redacción técnica.** La oferta la marca como requisito, no como deseable: runbooks, evidencia y
  reportes. Y en dos registros distintos — técnico y ejecutivo.
- **Método y constancia.** Buena parte del valor está en hacer siempre lo mismo, bien y dejando
  rastro. Un control ejecutado sin evidencia, para un auditor, no se ejecutó.
- **Coordinación con otras áreas.** No eres dueño de los servidores, ni de la red, ni de las bases
  de datos. Casi todo lo consigues **pidiéndolo bien y con argumentos**.
- **Criterio para priorizar.** Todo parece urgente; muy poco lo es. Distinguirlo es lo que separa a
  quien sostiene la operación de quien se ahoga en ella.
- **Curiosidad por lo viejo.** Vas a encontrarte sistemas legados con datos críticos y sin
  documentación. Es normal, y quien no los esquiva se vuelve valioso rápido.

## 📚 Tu ruta en el programa

Ruta **defensiva y de infraestructura**: mucho de redes, plataformas y telemetría; nada de ofensiva
avanzada. Orden recomendado:

1. 📚 [**Parte 0 — Fundamentos**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md)
   (001–025) · **la base literal del requisito**: Linux (005–006), Windows (008), **PowerShell
   (009)**, **TCP/IP, DNS y HTTPS (010–013)**, Python (015) y regex para logs (019).
2. 📚 [**Parte 1 — Redes y seguridad de redes**](../classes/parte-1-redes-y-seguridad-de-redes/README.md)
   (026–045) · **el núcleo de plataformas**: **034 (firewalls)**, **035 (IDS/IPS con Snort y
   Suricata)**, 036 (VPN), 041 (seguridad de DNS), **042 (segmentación y zero trust** — el marco del
   NAC**)**, 043 (NSM) y 045 (NetFlow).
3. 📚 [**Parte 8 — Blue Team, detección y SOC**](../classes/parte-8-blue-team-deteccion-y-soc/README.md)
   (181–200) · **la mitad SIEM del puesto**: **182 (logging y fuentes de telemetría)** —la clase más
   alineada con el rol—, **183 (arquitectura del SIEM)**, 184 (Splunk), 185 (Elastic y Wazuh), 189
   (EDR), 190 (logs de Windows) y 191 (logs de red y proxy).
4. 📚 [**Parte 2 — Criptografía aplicada**](../classes/parte-2-criptografia-aplicada/README.md)
   · **055 (PKI y certificados X.509)** y **056 (TLS en profundidad)** — lo que hay detrás de HTTPS
   y de **LDAPS**, y la causa de la mitad de las incidencias que vas a depurar.
5. 📚 [**Parte 10 — Nube y contenedores**](../classes/parte-10-seguridad-en-la-nube-y-contenedores/README.md)
   · **223 (AWS)**, **224 (Azure)** y **234 (logging y detección en la nube)**: el requisito de
   experiencia práctica en nube.
6. 📚 [**Parte 14 y 17**](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md) · **281 (PCI
   DSS)**, **285 (auditoría de seguridad)** y **282 (políticas y procedimientos)** para el marco de
   cumplimiento y los runbooks; **324 (hardening y gestión de configuración)** para las desviaciones;
   **313 (IAM empresarial)** para el directorio y LDAPS; **321 (comunicación y reporte)** para los
   dos tipos de informe.
7. 📚 [**Parte 9 — DFIR**](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/README.md)
   · **202 (ciclo de respuesta a incidentes)**: tu papel es de apoyo y coordinación, pero hay que
   conocer el proceso completo.

Clases concretas por las que empezar:

- 🗃️ [182 · Logging y fuentes de telemetría](../classes/parte-8-blue-team-deteccion-y-soc/182-logging-y-fuentes-de-telemetria/README.md) — **la clase central de esta ruta**: de dónde salen los eventos y cómo se llevan al SIEM.
- 🔎 [183 · SIEM: arquitectura y componentes](../classes/parte-8-blue-team-deteccion-y-soc/183-siem-arquitectura-y-componentes/README.md), [184 · Splunk para detección](../classes/parte-8-blue-team-deteccion-y-soc/184-splunk-para-deteccion/README.md) y [185 · Elastic Stack y Wazuh](../classes/parte-8-blue-team-deteccion-y-soc/185-elastic-stack-y-wazuh/README.md) — el SIEM por dentro, con dos implementaciones que puedes montar tú.
- 🧱 [034 · Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md) y [035 · IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md) — dos de los controles que administras, con las manos.
- 🚧 [042 · Segmentación de red y arquitectura zero trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md) — el marco conceptual del NAC y del control de acceso a la red.
- 🪟 [190 · Análisis de logs de Windows (Event Logs y Sysmon)](../classes/parte-8-blue-team-deteccion-y-soc/190-analisis-de-logs-de-windows-event-logs-y-sysmon/README.md) y [191 · Análisis de logs de red y proxy](../classes/parte-8-blue-team-deteccion-y-soc/191-analisis-de-logs-de-red-y-proxy/README.md) — los eventos que más vas a mirar.
- 🔐 [055 · PKI y certificados X.509](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md) y [056 · TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md) — HTTPS y **LDAPS** explicados de raíz.
- ☁️ [224 · Seguridad en Azure](../classes/parte-10-seguridad-en-la-nube-y-contenedores/224-seguridad-en-azure/README.md), [223 · Seguridad en AWS](../classes/parte-10-seguridad-en-la-nube-y-contenedores/223-seguridad-en-aws/README.md) y [234 · Logging y detección en la nube](../classes/parte-10-seguridad-en-la-nube-y-contenedores/234-logging-y-deteccion-en-la-nube/README.md) — la parte híbrida del alcance.
- 📋 [285 · Auditoría de seguridad](../classes/parte-14-grc-riesgo-y-cumplimiento/285-auditoria-de-seguridad/README.md) y [281 · Cumplimiento GDPR, HIPAA y PCI DSS](../classes/parte-14-grc-riesgo-y-cumplimiento/281-cumplimiento-gdpr-hipaa-y-pci-dss/README.md) — qué es un control, cómo se evidencia y qué busca un auditor.
- 🧰 [324 · Operaciones de seguridad, hardening y gestión de configuración](../classes/parte-17-profundizacion-para-certificaciones/324-operaciones-de-seguridad-hardening-y-gestion-de-configuracion/README.md) — las líneas base contra las que detectas desviaciones.
- ✍️ [282 · Políticas, estándares y procedimientos](../classes/parte-14-grc-riesgo-y-cumplimiento/282-politicas-estandares-y-procedimientos/README.md) y [321 · Comunicación y reporte](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md) — runbooks y los dos registros de reporte.

### Laboratorio y CTF

- 🧪 [`blue-team-soc`](../labs/blue-team-soc/README.md) — **el laboratorio de esta ruta**: monta el
  SIEM, **conecta las fuentes tú mismo** y verifica que la telemetría llega completa. Es literalmente
  el trabajo del puesto, no una aproximación.
- 🧪 [`redes-nmap`](../labs/redes-nmap/README.md) — descubrimiento y enumeración: saber qué hay
  realmente en la red que dices proteger.
- 🧪 [`rootcause-windows`](../labs/rootcause-windows/README.md) — controles y visibilidad en el
  endpoint, el lado EDR/antivirus del alcance.
- 🧪 [`cloud-security`](../labs/cloud-security/README.md) — postura y configuración en nube, con el
  tipo de hallazgo que después conviertes en evidencia.
- 🚩 [CTF de redes y forense](../ctf/README.md) — leer una captura y reconstruir un flujo: el
  músculo del análisis de eventos.

## 🎓 Certificaciones

Con archivo en el programa (mapean a partes concretas):

- 🎓 [**CompTIA Security+** (SY0-701)](../certificaciones/comptia-security-plus-sy0-701.md) — **la
  que pide la oferta** y el filtro más común del sector. Es tu primer hito.
- 📋 [**CompTIA CySA+** (CS0-003)](../certificaciones/comptia-cysa-plus-cs0-003.md) — el paso
  siguiente: análisis de eventos, monitoreo continuo y controles. La que mejor describe el rol una
  vez tienes rodaje.
- 🥇 [**BTL1** (Blue Team Level 1)](../certificaciones/btl1.md) — práctica y muy útil si quieres
  reforzar el lado de análisis, aunque no la pide la oferta.

Fuera del programa y nombradas en la oferta: **CompTIA Network+** (la base de red pura, buen
complemento si vienes de sistemas y no de redes), **Microsoft SC-200** (Security Operations Analyst
— muy alineada si el SIEM es **Sentinel**, que es el caso más frecuente hoy) y **AWS Certified
CloudOps Engineer – Associate** para la parte de nube. Las tres se sacan con su proveedor. Consulta
el [mapeo completo a certificaciones](../certificaciones/README.md) para ver la cobertura del
programa.

## 📈 Progresión de carrera y salario

Ruta habitual: **Administrador de sistemas/redes → Analista de seguridad de infraestructura →
Especialista o ingeniero de seguridad → Arquitecto de seguridad** (o jefatura de operaciones de
seguridad). Es un rol **bisagra**: desde aquí se salta con facilidad a
[SOC / Blue Team](soc-blue-team.md) si te tira el análisis, a
[SecOps](secops-engineer.md) si te tira la automatización, a
[Cloud Security](cloud-security.md) si el entorno híbrido te engancha, o hacia
[GRC](grc.md) si lo que te interesa acaba siendo el cumplimiento.

Rangos **orientativos y aproximados** (brutos anuales; varían por sector, tamaño y madurez de la
organización — referencia, no promesa):

```text
Región                      Entrada (~1 año)       Especialista / senior
--------------------------  ---------------------  ------------------------
LATAM                       USD 14k – 28k / año    USD 30k – 58k+ / año
Chile (financiero/pagos)*   USD 18k – 34k / año    USD 36k – 65k+ / año
España                      EUR 24k – 34k / año    EUR 38k – 60k+ / año
Remoto (USD)                USD 45k – 80k / año    USD 85k – 140k+ / año
```

\* En **procesamiento de pagos, banca y empresas que cotizan** el puesto paga por encima del
promedio y es **muy estable** (los controles SOX y PCI son obligatorios y anuales), a cambio de una
carga de evidencia y auditoría constante. La experiencia en **nube** es hoy la variable que más
mueve el rango dentro del mismo rol.

## ⚠️ Mitos y errores comunes

- **"Esto es administración de sistemas con otro nombre."** Comparte base, pero el eje es distinto:
  aquí el objetivo es la **visibilidad, el control y la evidencia**, no la disponibilidad del
  servicio.
- **"El SIEM se configura una vez."** Es lo contrario: las fuentes cambian, los formatos cambian
  tras cada actualización y una fuente caída **no avisa**. Vigilar la ingesta es trabajo permanente,
  y es justo donde este rol aporta valor.
- **"Si el control está desplegado, está cubierto."** Cobertura real ≠ cobertura contratada. La
  diferencia entre lo que dice la consola y lo que hay en la red es donde ocurren los incidentes.
- **"El cumplimiento es papeleo."** SOX y PCI son obligaciones con consecuencias legales y
  económicas. Además, la disciplina de evidenciar controles **mejora la operación** de verdad: te
  obliga a saber qué tienes.
- **"Los sistemas legados no son mi problema."** Un AS/400 con datos críticos es exactamente tu
  problema, y esquivarlo es dejar el mayor punto ciego dentro del alcance.
- **"Necesito saber hackear para esto."** No. Necesitas entender cómo se ve un ataque en los logs y
  cómo se configura un control bien. La ofensiva ayuda, pero no es el requisito.
- **"El curso me da todo lo que pide la oferta."** Casi todo, pero no; lee la nota de abajo.

> **Honestidad, sin marketing:** este programa te da **la base técnica** del puesto —Linux y
> Windows, TCP/IP, DNS, HTTPS y el TLS/PKI que hay detrás de LDAPS, firewalls, IDS/IPS,
> segmentación (el marco del NAC), EDR, arquitectura e ingeniería del SIEM con dos implementaciones
> montables, nube en Azure y AWS, hardening, auditoría, PCI DSS, runbooks y reporte—. Lo que **no**
> te da: **AS/400 / IBM i**, que no está cubierto en ninguna clase y aparece explícito en la oferta;
> **SOX** como normativa concreta (el programa enseña qué es un control y cómo se evidencia —clases
> 285 y 281—, pero no la ley Sarbanes-Oxley en sí); el **NAC como producto** (se cubre el concepto
> de control de acceso a red en la clase 042, no la administración de una plataforma comercial); la
> experiencia real con **una consola concreta** de SIEM comercial —Sentinel, QRadar o XSIAM— más
> allá de Splunk, Elastic y Wazuh; y la **titulación** que se pide como requisito formal. El curso
> te hace **capaz de administrar la telemetría y los controles**; la plataforma comprada y la
> normativa de tu empresa las pones tú.

## 🚀 Siguientes pasos

1. **Asegura la base de sistemas y redes** (Partes 0 y 1). Si ya vienes de administrar servidores,
   esta parte es repaso y llegas con ventaja: es exactamente lo que la oferta valora.
2. **Empieza por 182 y 183.** La telemetría y la arquitectura del SIEM son el corazón del rol, y la
   parte que ningún otro candidato junior sabe explicar.
3. **Monta el lab [`blue-team-soc`](../labs/blue-team-soc/README.md) y conecta las fuentes tú.** No
   te limites a consultar el SIEM: rompe una fuente a propósito y detecta que dejó de reportar. Esa
   es la habilidad del puesto.
4. Cubre los controles de red con **034 (firewalls)**, **035 (IDS/IPS)** y **042 (segmentación)**, y
   el endpoint con **189 (EDR)**.
5. Estudia **055 y 056** (PKI y TLS): entender certificados te va a resolver una parte
   desproporcionada de las incidencias reales, LDAPS incluido.
6. Añade la **nube** (223, 224, 234) — es la variable que más mueve el sueldo dentro de este mismo
   puesto.
7. Cierra con el marco de **cumplimiento** (281, 285) y **escribe un runbook completo** de una tarea
   que hayas hecho en el laboratorio: es el entregable del rol y demuestra la redacción técnica que
   la oferta exige.
8. Saca la **Security+** como primer hito y apunta a **CySA+** o **SC-200** según hacia dónde
   crezcas.

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🏠 [Inicio del programa](../README.md)
