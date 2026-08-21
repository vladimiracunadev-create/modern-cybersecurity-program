# 🧰 Analista de Seguridad Ofensiva (consultoría)

> La puerta de entrada real al oficio ofensivo: ejecutas pruebas de intrusión de nivel básico a
> intermedio sobre aplicaciones, **APIs**, redes e infraestructura, apoyas evaluaciones de
> vulnerabilidades, **validas hallazgos** y —sobre todo— elaboras la evidencia técnica y la
> documentación. Trabajas dentro de un método definido y con supervisión, en una consultora que
> presta el servicio a terceros.
>
> **Nivel de entrada:** junior / semi-senior; 1–2 años de experiencia y titulación · **Foco:** pentest de apps/APIs/redes, validación de hallazgos, evidencia y reporte · **Certificación faro:** eJPT o CompTIA PenTest+ (no OSCP todavía)

## 🧭 Qué es y por qué importa

Casi nadie entra al mundo ofensivo dirigiendo engagements. Se entra **aquí**: como analista dentro
de un equipo de consultoría que vende servicios de seguridad ofensiva a clientes. Ejecutas la parte
técnica acotada que te asignan, la documentas con rigor y aprendes el método de gente que lleva
años haciéndolo.

Es un rol distinto del de [Pentester / Ethical Hacker](pentester.md) en tres cosas concretas:

- **El alcance de lo que ejecutas.** Pruebas de intrusión **básicas e intermedias**, no cadenas de
  explotación complejas ni desarrollo de exploits. Se espera que uses bien Nmap, Burp, ZAP,
  Nessus/OpenVAS y Metasploit, no que escribas el tuyo.
- **La validación por encima del descubrimiento.** Buena parte del trabajo es tomar la salida de un
  escáner y **confirmar a mano si el hallazgo es real** o un falso positivo. Suena menos glamuroso
  de lo que es: es la habilidad que separa un informe creíble de una lista automática.
- **El peso de la documentación.** La evidencia técnica —capturas, peticiones, comandos, pasos
  reproducibles— **es tu entregable**. En una consultora el informe se factura, se audita y se
  discute con el cliente. Si tu evidencia no se sostiene, el hallazgo se cae.

Importa porque es **el puesto que realmente contrata gente sin trayectoria ofensiva previa**. Pide
1–2 años (a menudo de SOC, soporte o redes), titulación y certificaciones de nivel de entrada
—eJPT, Security+, PenTest+, CEH—, no un OSCP. Y porque en una consultora ves en dos años más
sectores, tecnologías y arquitecturas que en cinco años dentro de una sola empresa: es un acelerador
de aprendizaje difícil de igualar.

> **De dónde sale esta guía.** Está calcada de una oferta real de empleo
> ([EY, *Analista de Seguridad Ofensiva*, Santiago de Chile](https://www.linkedin.com/jobs/view/4407028796)):
> ejecución de pruebas de intrusión de nivel básico a intermedio sobre aplicaciones, APIs, redes o
> infraestructura; apoyo en evaluaciones de vulnerabilidades y **validación de hallazgos**;
> elaboración de evidencia técnica y documentación; participación en reuniones internas de
> **alcance (scoping)** y seguimiento. Requisitos: título en informática, ciberseguridad, redes o
> telecomunicaciones; 1–2 años en seguridad ofensiva, gestión de vulnerabilidades o SOC; manejo de
> **Nmap, Burp Suite, OWASP ZAP, Nessus/OpenVAS, Metasploit, Wireshark, Linux/Kali y Bash/Python
> básico**; conocimientos de HTTP/HTTPS, OWASP Top 10, APIs, redes TCP/IP, fundamentos de Active
> Directory y reporte de vulnerabilidades. Deseables: **eJPT, Security+/PenTest+, CEH**. La oferta
> menciona además proyectos de **ciberseguridad industrial** sobre infraestructura crítica.

## 🗓️ Un día en el puesto

En consultoría el día lo marca el **proyecto facturable** en el que estás y el calendario del
cliente, no tu curiosidad:

- **Reunión interna de alcance:** qué entra y qué no en la evaluación, qué IPs y dominios, qué
  ventanas de tiempo, qué está prohibido. Al principio escuchas y tomas notas; en un año, opinas.
  Aquí se decide si el trabajo va a salir bien.
- **Ejecución de la prueba:** reconocimiento y enumeración del objetivo, escaneo, y las pruebas
  concretas que te tocan — el módulo web de una aplicación, un conjunto de APIs, un rango de red.
  Trabajas dentro de una metodología definida (PTES, OWASP), no improvisando.
- **Validación de hallazgos:** el escáner reporta 200 cosas. Verificas cuáles son reales, cuáles son
  ruido y cuál es el **impacto verdadero** en ese contexto concreto. Un "crítico" de Nessus sobre un
  servicio interno sin exposición no es un crítico.
- **Evidencia y documentación:** capturas, peticiones y respuestas, comandos exactos, pasos para
  reproducir. Se documenta **mientras** se trabaja, no tres días después: lo que no anotaste en el
  momento, no lo recuperas.
- **Redacción de hallazgos:** descripción, criticidad (CVSS), evidencia, impacto de negocio y
  remediación accionable. Al principio escribes hallazgos sueltos que un senior revisa; con el
  tiempo, informes completos.
- **Seguimiento:** el cliente pregunta, discute una criticidad o dice que ya lo corrigió. Se
  re-testea y se cierra.

Dicho sin adornos: hay **más documentación y más burocracia de proyecto** de lo que la gente imagina
al entrar, y menos "hackear" del que se ve en redes sociales. También hay control de horas, plazos
ajustados y varios clientes a la vez. A cambio, aprendes rápido y con red de seguridad.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Redes TCP/IP de verdad.** Direccionamiento, puertos, protocolos, DNS. Sin esto, el escaneo es
  ruido y el pivoting es magia.
- **HTTP/HTTPS y la web por dentro.** Peticiones, respuestas, cabeceras, cookies, sesiones, TLS. Es
  el terreno donde ocurre la mayor parte del trabajo.
- **OWASP Top 10 con las manos**, no de memoria: saber encontrar, explotar de forma controlada y
  explicar una inyección, un XSS o un control de acceso roto.
- **APIs.** La oferta las nombra aparte por algo: REST y GraphQL tienen su propia superficie
  —autenticación, autorización por objeto, exposición de datos— y hoy son la mitad de los objetivos.
- **Linux y Kali** como entorno de trabajo diario, y **Windows** lo suficiente para no perderte.
- **Fundamentos de Active Directory:** qué es un dominio, un usuario, un grupo, cómo se enumera y
  por qué es el objetivo natural en una red corporativa. **Fundamentos**, no compromiso total de
  dominio: eso es territorio de [Red Team](red-team.md).
- **Análisis de vulnerabilidades:** operar Nessus/OpenVAS, leer su salida con criterio y **validar**.
  El escáner propone; tú decides.
- **Scripting básico en Bash y Python:** automatizar lo repetitivo, adaptar un exploit público,
  procesar la salida de una herramienta. "Básico" en la oferta significa *funcional*, no *nulo*.
- **CVSS y reporte de vulnerabilidades:** puntuar con consistencia y justificar la nota.

### Herramientas del oficio

```text
Recon/red:       Nmap (+ NSE), Wireshark, herramientas de enumeración de servicios
Web/APIs:        Burp Suite (el estándar), OWASP ZAP, sqlmap, clientes REST/GraphQL
Vulnerabilidades: Nessus, OpenVAS, Qualys — y el criterio para validar su salida
Explotación:     Metasploit, msfvenom, Meterpreter (uso controlado y con alcance)
Entorno:         Kali Linux, Bash, Python, Git
Documentación:   capturas, plantillas de informe, CVSS, gestor de evidencia
```

En este puesto se te va a evaluar por **usar bien lo estándar**, no por herramientas exóticas. Un
Burp bien manejado vale más que diez utilidades de GitHub a medio entender.

### Habilidades no técnicas

- **Redacción técnica.** Es *la* habilidad diferenciadora del rol. Tu entregable es un documento
  que alguien tiene que poder ejecutar para reproducir el fallo y arreglarlo.
- **Rigor con la evidencia.** Capturas legibles, comandos completos, pasos que funcionan. Un
  hallazgo sin evidencia sólida es una opinión, y en consultoría las opiniones no se facturan.
- **Ética y límites legales.** Actúas dentro de un alcance contratado y por escrito. Salirte de él
  no es iniciativa: es un incidente con consecuencias legales para ti y para la firma.
- **Trabajo en equipo y bajo supervisión.** Eres el eslabón junior: se espera que preguntes, que
  aceptes revisión de tu trabajo y que no te lo tomes personal cuando te devuelvan un hallazgo.
- **Gestión del tiempo y de varios clientes.** En consultoría el reloj se factura. Estimar cuánto te
  va a llevar algo es parte del oficio.
- **Comunicación con no técnicos.** Traducir un hallazgo a impacto de negocio para alguien que no
  sabe qué es una cabecera HTTP.

## 📚 Tu ruta en el programa

Es la ruta ofensiva **acotada al perfil de entrada**: llega hasta donde llega el puesto y no más.
Compárala con la de [Pentester](pentester.md), que sigue hacia binarios y explotación avanzada.

1. 📚 [**Parte 0 — Fundamentos**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md)
   (001–025) · el laboratorio con Kali (**004**), Linux (005–006), **Bash (007)**, Windows (008),
   **TCP/IP y HTTP (010–013)**, **Python (015)** y —no negociable— **ética y legalidad (025)**.
2. 📚 [**Parte 1 — Redes y seguridad de redes**](../classes/parte-1-redes-y-seguridad-de-redes/README.md)
   (026–045) · **Wireshark (026)** y el bloque completo de **Nmap (029–032)** más enumeración de
   servicios (033): las herramientas que la oferta nombra primero.
3. 📚 [**Parte 3 — Pentesting: metodología**](../classes/parte-3-hacking-etico-y-pentesting-metodologia/README.md)
   (066–085) · **el núcleo del rol**: metodología (066), **alcance y reglas de engagement (067)**,
   reconocimiento (068–069), enumeración (070), **Nessus/OpenVAS (071)**, **Metasploit (072–074)**,
   escaladas (076–077) y **reporte profesional (085)**.
4. 📚 [**Parte 4 — Seguridad de aplicaciones web**](../classes/parte-4-seguridad-de-aplicaciones-web/README.md)
   (086–115) · **OWASP Top 10 (087)**, **Burp (088)** y **ZAP (089)**, las inyecciones y el control
   de acceso, y muy en concreto **APIs: 110 (REST) y 111 (GraphQL)**.
5. 📚 [**Parte 7 — Red Team**](../classes/parte-7-red-team-y-operaciones-ofensivas/README.md)
   · **solo 170 (enumeración de Active Directory)**, que es el "fundamentos de AD" que pide la
   oferta. El resto de la parte es para más adelante.
6. 📚 [**Parte 17 — Profundización**](../classes/parte-17-profundizacion-para-certificaciones/README.md)
   · **323** pruebas de seguridad del software · **321** comunicación y reporte · **318** gestión del
   programa de vulnerabilidades: la mitad "consultoría" del puesto.
7. 📚 [**Parte 13**](../classes/parte-13-seguridad-movil-iot-e-inalambrica/README.md) · **273
   (ICS/SCADA)** si te toca la línea de **ciberseguridad industrial** e infraestructura crítica.

Clases concretas por las que empezar:

- 🗺️ [066 · Metodología de pentesting (PTES y OSSTMM)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md) y [067 · Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md) — el método y **las reuniones de alcance** que menciona la oferta.
- 🔍 [029–032 · Nmap](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md) (empezando por descubrimiento) y [026 · Wireshark](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md) — las dos herramientas de red del puesto.
- 🩹 [071 · Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md) — el escaneo cuya salida vas a **validar** todos los días.
- 🕸️ [087 · OWASP Top 10](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md), [088 · Burp Suite](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md) y [089 · OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md) — el trío literal de la oferta.
- 🔌 [110 · Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md) y [111 · Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md) — las APIs que el puesto nombra como objetivo propio.
- 💥 [072 · Metasploit Framework](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md) — explotación controlada dentro del alcance.
- 🏢 [170 · Active Directory: enumeración](../classes/parte-7-red-team-y-operaciones-ofensivas/170-active-directory-enumeracion/README.md) — los fundamentos de AD que se piden, sin ir más lejos.
- 📝 [085 · Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md) y [321 · Comunicación y reporte para analistas de seguridad](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md) — **tu entregable real**; trátalas como clases técnicas, no como relleno.
- ⚖️ [025 · Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md) — la línea que separa el oficio del delito.

### Laboratorio y CTF

- 🧪 [`appsec-web`](../labs/appsec-web/README.md) — Juice Shop y DVWA: el OWASP Top 10 con Burp y
  ZAP, que es literalmente el 60 % del trabajo técnico del puesto.
- 🧪 [`redes-nmap`](../labs/redes-nmap/README.md) — escaneo y enumeración con Nmap, la base del
  reconocimiento.
- 🧪 [`red-team-ad`](../labs/red-team-ad/README.md) — solo la parte de enumeración de AD, para los
  "fundamentos de Active Directory".
- 🧪 [`appsec-code`](../labs/appsec-code/README.md) — útil para entender **por qué** existe el fallo
  que reportas: eleva mucho la calidad de la recomendación de remediación.
- 🚩 [CTF de web y redes](../ctf/README.md) — y **escribe el writeup**: es el ensayo perfecto de la
  documentación de evidencia que te van a pedir.

## 🎓 Certificaciones

Este es un rol donde las certis **sí pesan** en el filtro: las consultoras las usan como criterio de
selección y muchas veces las financian una vez dentro.

Con archivo en el programa (mapean a partes concretas):

- 🎓 [**CompTIA Security+** (SY0-701)](../certificaciones/comptia-security-plus-sy0-701.md) — la de
  entrada. No es ofensiva, pero es la que más aparece como requisito filtro. Empieza aquí si no
  tienes ninguna.
- 🎯 [**CompTIA PenTest+** (PT0-002)](../certificaciones/comptia-pentest-plus-pt0-002.md) — **la que
  mejor describe este puesto**: método, herramientas, análisis de vulnerabilidades y reporte, con un
  examen mucho más abordable que el OSCP. El programa la cubre al **91 %**.
- 🏴 [**OSCP** (PEN-200)](../certificaciones/oscp-pen-200.md) — **no para entrar, sí como meta a 2–3
  años**. Es lo que te mueve de este puesto al de [pentester](pentester.md) con engagements propios.

Las tres que la oferta marca como deseables y **no tienen ficha en el programa**: **eJPT** (INE) es
la certificación práctica de entrada por excelencia para este perfil y probablemente la de mejor
relación esfuerzo/valor para conseguir el puesto; **CEH** (EC-Council) es cara y muy teórica, pero
sigue apareciendo en filtros de RR. HH. de grandes firmas y del sector público. Ambas se sacan
aparte con su proveedor. Consulta el
[mapeo completo a certificaciones](../certificaciones/README.md) para ver cuánto cubre el programa.

## 📈 Progresión de carrera y salario

Ruta habitual dentro de una consultora: **Analista de seguridad ofensiva → Consultor / pentester →
Consultor senior o líder técnico → Manager de la práctica ofensiva**. Los dos primeros saltos son
técnicos; a partir del tercero, la carrera se bifurca entre **especialización** (red team, AppSec,
seguridad industrial) y **gestión** (dirigir proyectos, vender y armar equipo).

Dos caminos típicos a los 2–3 años: **quedarte y subir** en la firma, o **saltar al lado del
cliente** (in-house) — normalmente con mejor calidad de vida y menos horas facturables, a cambio de
menos variedad.

Rangos **orientativos y aproximados** (brutos anuales; varían mucho por país, firma, tamaño e
inglés — referencia, no promesa):

```text
Región                      Analista (1–2 años)    Consultor / senior
--------------------------  ---------------------  ------------------------
LATAM                       USD 12k – 26k / año    USD 28k – 55k+ / año
Chile (consultoría/Big4)*   USD 18k – 32k / año    USD 35k – 65k+ / año
España                      EUR 22k – 32k / año    EUR 38k – 60k+ / año
Remoto (USD)                USD 45k – 75k / año    USD 90k – 140k+ / año
```

\* Las **grandes firmas de consultoría** no suelen ser las que mejor pagan en el escalón de entrada,
pero compensan con formación estructurada, certificaciones financiadas, marca en el currículum y una
variedad de proyectos que difícilmente consigues en otro sitio. Es una inversión de 2–3 años que
después se cobra. Los números remotos en USD asumen clientes de EE. UU./Europa e inglés alto.

## ⚠️ Mitos y errores comunes

- **"Voy a hackear todo el día."** No. Vas a escanear, validar, documentar y asistir a reuniones de
  proyecto. La ejecución técnica es una parte, y al principio es la parte acotada que te asignan.
- **"Necesito el OSCP para entrar."** Falso, y es el error que más gente frena. Esta oferta pide
  **eJPT, Security+, PenTest+ o CEH** y 1–2 años de experiencia que pueden venir de SOC o de gestión
  de vulnerabilidades. El OSCP es para el siguiente escalón.
- **"La documentación es lo aburrido del trabajo."** Es **el producto** que la firma factura. El
  analista junior que escribe evidencia impecable asciende antes que el que encuentra más cosas y
  las reporta mal.
- **"Un crítico del escáner es un crítico."** No: la criticidad depende del contexto —exposición,
  datos, compensaciones—. Validar y recalificar es justo el trabajo que se te paga.
- **"Todo lo que aprendo lo puedo probar donde sea."** Nunca. Fuera del alcance contratado es
  delito, y en una consultora arrastras a la firma contigo. Practica en los laboratorios.
- **"Es un rol de segunda respecto al pentester."** Es el mismo oficio en su primer escalón. Casi
  todos los pentesters senior empezaron exactamente aquí.
- **"El curso me da todo lo que pide la oferta."** No del todo; lee la nota de abajo.

> **Honestidad, sin marketing:** este programa te da **la totalidad del stack técnico que enumera la
> oferta** —Nmap, Burp, ZAP, Nessus/OpenVAS, Metasploit, Wireshark, Kali, Bash/Python, HTTP/HTTPS,
> OWASP Top 10, APIs, TCP/IP, fundamentos de AD y reporte de vulnerabilidades—; es, de todas las
> rutas de este curso, la que **más literalmente** cubre un anuncio de empleo. Lo que **no** te da
> es el **título universitario** que la oferta pide como requisito formal, ni la **experiencia de
> consultoría**: trabajar con horas facturables, tratar con un cliente que discute una criticidad,
> sostener un hallazgo en una reunión o gestionar tres proyectos a la vez. Tampoco te da las
> certificaciones deseables (eJPT, CEH), que se sacan aparte. El curso te hace **técnicamente capaz
> de aprobar la parte práctica de la entrevista**; el título y el oficio de consultor los pones tú.

## 🚀 Siguientes pasos

1. **Haz la Parte 0 completa**, sin saltártela por impaciencia — y con la clase **025 (ética)**
   leída de verdad, porque en este oficio el permiso es el trabajo.
2. Encadena **Parte 1 → Parte 3**: Nmap y Wireshark primero, después la metodología completa. No
   pases de la 3 sin sentirte cómodo con el método y el alcance.
3. Ataca la **Parte 4** en paralelo con el lab [`appsec-web`](../labs/appsec-web/README.md), y no
   te saltes **110 y 111 (APIs)**: es donde muchos candidatos flojean y la oferta lo pide explícito.
4. Añade **170** (enumeración de AD) para cubrir los fundamentos de Active Directory, y **273** si
   te interesa la línea de seguridad industrial.
5. **Practica la evidencia, no solo la explotación.** Por cada máquina o reto que resuelvas, escribe
   el hallazgo en formato profesional: descripción, CVSS, evidencia reproducible, impacto y
   remediación. Diez hallazgos bien escritos son un portafolio mejor que treinta writeups sueltos.
6. Apunta a **eJPT** o **PenTest+** como primer hito de certificación (Security+ antes si vienes de
   cero), y deja el **OSCP** planificado a 2–3 años.
7. Cuando entrevistes, **pregunta por el mix real**: qué porcentaje del tiempo es ejecución técnica,
   cuánto documentación y cuánto proyecto. Te dirá mucho más del puesto que el título del anuncio.

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🏠 [Inicio del programa](../README.md)
