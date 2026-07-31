# 🧩 Ingeniero de Operación de Plataformas de Seguridad (MSSP y DLP)

> Operas las plataformas de seguridad **de otras empresas**. Trabajas desde un proveedor de
> servicios gestionados: administras y monitoreas las herramientas, gestionas incidentes y alertas,
> escribes los procedimientos, propones mejoras y **te sientas con el cliente a explicárselo**. Con
> una especialidad concreta: la **protección del dato** — clasificación, descubrimiento y DLP.
>
> **Nivel de entrada:** junior; ~1 año operando herramientas de seguridad · **Foco:** operación de plataformas, DLP y clasificación de datos, incidentes, hardening, documentación y relación técnica con el cliente · **Certificación faro:** Security+ como base, y la certificación del fabricante de la plataforma que operes

## 🧭 Qué es y por qué importa

Hay dos formas de trabajar en ciberseguridad: **dentro** de la empresa que se protege, o **para
muchas empresas a la vez** desde un proveedor. Este rol es el segundo, y es la vía de entrada al
sector que menos se explica: los **MSSP** (proveedores de servicios gestionados de seguridad) e
integradores contratan constantemente perfiles junior, porque su negocio es operar plataformas a
escala para decenas de clientes.

El puesto tiene dos mitades:

- **Operar la plataforma.** Administrar, monitorear y mantener las herramientas de seguridad:
  atender alertas e incidentes, resolver requerimientos, escalar al fabricante cuando el problema
  es del producto, aplicar líneas base de configuración según **CIS, NIST** y las guías del
  proveedor, y ejecutar planes de **hardening** y mejora.
- **Ser la cara técnica ante el cliente.** Reuniones periódicas, documentación operativa
  (**playbooks y procedimientos**), análisis de métricas para proponer mejoras, y participación
  técnica en propuestas y renovaciones del servicio. No es un rol de trastienda: **el cliente sabe
  tu nombre**.

Y una especialidad que lo distingue de todo lo demás en este programa: **el dato como objeto a
proteger**. Clasificación y descubrimiento de información, y **DLP** (prevención de fuga de datos).
Mientras casi toda la seguridad se organiza alrededor de sistemas, redes y endpoints, aquí la
pregunta es otra: *¿dónde está la información sensible, quién la toca y por dónde se está yendo?*

Importa por tres razones. Primero, porque **contrata junior de verdad**: pide un año de experiencia
operando herramientas, no una trayectoria. Segundo, porque en un MSSP ves en un año más productos,
industrias y arquitecturas que en tres años dentro de una sola empresa — es un acelerador brutal.
Y tercero, porque **DLP y protección del dato es una especialidad escasa**: casi nadie la elige a
propósito, y toda organización regulada acaba necesitándola.

> **De dónde sale esta guía.** Está calcada de una oferta real de empleo
> ([WDGroup / Widefense, *Cybersecurity Engineer*, Santiago de Chile](https://www.linkedin.com/jobs/view/4440906457)):
> administrar, monitorear y operar plataformas de ciberseguridad; gestionar incidentes, alertas,
> requerimientos y problemas técnicos **en coordinación con clientes y fabricantes**; analizar
> métricas y eventos para proponer mejoras; definir y aplicar lineamientos según **CIS, NIST** y
> estándares del fabricante; elaborar **documentación operativa (playbooks y procedimientos)**;
> mantener la relación técnica con el cliente en reuniones periódicas; diseñar y ejecutar **planes
> de mejora y hardening**; participar técnicamente en **propuestas y renovaciones**; y coordinarse
> con MSOC, soporte y preventa. Requisitos: título de ingeniería (obligatorio), **1 año mínimo** en
> operación, soporte o administración de herramientas de ciberseguridad, experiencia demostrable en
> al menos un pilar —**clasificación/descubrimiento de datos o DLP**— e **inglés técnico avanzado
> obligatorio**. Deseables: certificación **SC-401**, experiencia en banca y conocimiento de NIST,
> CIS y PCI.

## 🗓️ Un día en el puesto

El día lo parte en dos el hecho de que **tu trabajo lo consume alguien que paga por él**:

- **Cola de tickets y alertas:** requerimientos del cliente, alertas de la plataforma, incidentes
  abiertos. Priorizas por SLA, no por interés técnico — y esa es la diferencia mental más grande
  con un puesto in-house.
- **Operación de la plataforma:** ajustar una política de DLP que está generando demasiados falsos
  positivos, agregar un repositorio al descubrimiento de datos, revisar por qué un agente dejó de
  reportar, aplicar una línea base de configuración.
- **Investigación de un evento:** alguien intentó sacar un archivo con datos de tarjetas a un
  correo personal. ¿Fue un error?, ¿un proceso legítimo mal diseñado?, ¿algo peor? Aquí el análisis
  es **tan humano como técnico**, y esa es la particularidad del DLP.
- **Escalamiento al fabricante:** cuando el problema es del producto, abres el caso, lo defiendes
  con evidencia y le das seguimiento. Aprender a tratar con el soporte de un fabricante es una
  habilidad real del puesto.
- **Documentación:** el playbook del procedimiento que acabas de resolver, para que el siguiente no
  reinvente la rueda. En un MSSP la documentación **es el activo de la empresa**.
- **Reunión con el cliente:** informe del período, métricas, incidentes relevantes, propuestas de
  mejora. Aquí es donde el trabajo técnico se transforma en renovación del contrato.
- **Apoyo a preventa:** un comercial necesita el respaldo técnico de una propuesta o del alcance de
  una renovación. Vas.

Dicho sin adornos: hay **SLA, tickets y clientes exigentes**, y la agenda no siempre la manejas tú.
El componente de servicio es real: se espera trato profesional, respuesta a tiempo y capacidad de
explicarle algo técnico a alguien que está molesto. A cambio, la curva de aprendizaje es de las más
rápidas del sector.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **El ciclo de vida del dato.** Dónde nace la información, dónde se almacena, quién la usa, cuándo
  se archiva y cómo se destruye. Sin este mapa, el DLP es una lista de reglas sin sentido.
- **Clasificación y descubrimiento.** Cómo se etiqueta la información por sensibilidad y cómo se
  rastrea dónde está realmente — que casi nunca es donde la organización cree.
- **DLP de verdad:** los tres frentes (datos en reposo, en tránsito y en uso), cómo se escriben
  políticas que atrapen lo que importa sin frenar el negocio, y cómo se afinan los **falsos
  positivos**, que es el 80 % del trabajo real de la herramienta.
- **Marcos de referencia: CIS, NIST** y, en clientes financieros, **PCI DSS**. Son el criterio con
  el que justificas una configuración ante el cliente y ante su auditor.
- **Sistemas y redes lo suficiente** para operar: Windows, Linux, HTTP/HTTPS, correo, y cómo se
  mueve un archivo entre sistemas — porque por ahí es por donde se fuga.
- **Identidades y permisos.** Casi toda fuga empieza en un acceso que no debería existir.
- **Operación y hardening de plataformas:** líneas base, gestión de configuración, actualizaciones
  y verificación de que el control **realmente está activo** en toda la cobertura contratada.
- **Gestión de incidentes y alertas:** el ciclo de triaje, investigación, contención y cierre, con
  la trazabilidad que el cliente va a auditar.

### Herramientas del oficio

```text
Datos/DLP:       plataformas de clasificación, descubrimiento y DLP (Microsoft Purview,
                 Forcepoint, Symantec, Netskope y equivalentes de cada fabricante)
Operación:       consolas de administración, ticketing (SLA), gestión de configuración
Monitoreo:       SIEM y consolas del MSOC, métricas y reportería del servicio
Endpoint/red:    EDR, proxy/CASB, correo — los caminos por los que el dato sale
Marcos:          CIS Benchmarks, NIST CSF, PCI DSS
Documentación:   playbooks, procedimientos, informes periódicos al cliente
```

En este rol **la marca de la plataforma importa más que en cualquier otro** del programa: te
contratan para operar *una* familia de productos. La buena noticia es que el modelo mental se
transfiere entre fabricantes, y la certificación del producto suele pagarla la empresa.

### Habilidades no técnicas

- **Inglés técnico, y aquí no es opcional.** La oferta lo marca como requisito obligatorio: la
  documentación del fabricante, los casos de soporte y las certificaciones están en inglés. Es,
  probablemente, el requisito que más candidatos deja fuera.
- **Trato con el cliente.** Explicar, informar, sostener una recomendación y dar malas noticias sin
  perder la relación. Eres el rostro técnico del proveedor.
- **Autonomía.** La oferta la pide explícitamente: en un MSSP nadie te va a estar mirando por
  encima del hombro; se espera que resuelvas y que preguntes cuando toca.
- **Escritura de procedimientos.** Documentar de forma que **otra persona pueda ejecutarlo sin
  llamarte**. Es la métrica real de calidad de un playbook.
- **Criterio ante el dato ajeno.** Vas a ver información confidencial de empresas que no son la
  tuya: nóminas, contratos, datos de clientes. La discreción no es una virtud opcional, es la base
  del contrato.
- **Aguante al ritmo de servicio:** varios clientes, SLA que corren y prioridades que cambian.

## 📚 Tu ruta en el programa

Es una ruta **corta y muy dirigida**: mucho de operación y de dato, poco de ofensiva. Orden
recomendado:

1. 📚 [**Parte 0 — Fundamentos**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md)
   (001–025) · Linux (005), Windows (008), HTTP/HTTPS (013) y **003 (frameworks NIST/ISO/CIS)**, el
   vocabulario con el que justificarás cada configuración.
2. 📚 [**Parte 17 — Profundización**](../classes/parte-17-profundizacion-para-certificaciones/README.md)
   · **311 (clasificación y ciclo de vida de los datos)** y **312 (retención, destrucción segura y
   DLP)** — **el núcleo especializado del puesto**, y las dos clases por las que empezar.
3. 📚 [**Parte 14 — GRC, riesgo y cumplimiento**](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md)
   · **280 (controles CIS)**, **279 (NIST CSF)**, **281 (PCI DSS)**, **289 (privacidad y protección
   de datos)**, **282 (políticas y procedimientos)** y **287 (métricas)**: el marco con el que se
   discute con el cliente.
4. 📚 [**Parte 8 — Blue Team y SOC**](../classes/parte-8-blue-team-deteccion-y-soc/README.md)
   · **182** (telemetría), **183** (SIEM), **189** (EDR) y **197** (métricas y madurez) — la
   operación del MSOC con el que te coordinas.
5. 📚 [**Parte 9 — DFIR**](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/README.md)
   · **202** (ciclo de incidentes) y **215 (playbooks)** — literalmente el entregable que la oferta
   pide escribir.
6. 📚 [**Parte 17**](../classes/parte-17-profundizacion-para-certificaciones/README.md) otra vez ·
   **324** (hardening y gestión de configuración) para los planes de mejora, **313**/**315**
   (identidades y accesos privilegiados) y **321** (comunicación y reporte) para la reunión mensual.
7. 📚 [**Parte 10 — Nube**](../classes/parte-10-seguridad-en-la-nube-y-contenedores/README.md)
   · **234** (logging y detección en la nube) y **233** (secretos): hoy casi todas las plataformas
   que vas a operar son SaaS.

Clases concretas por las que empezar:

- 🗂️ [311 · Clasificación y ciclo de vida de los datos](../classes/parte-17-profundizacion-para-certificaciones/311-clasificacion-y-ciclo-de-vida-de-los-datos/README.md) y [312 · Retención, destrucción segura de datos y DLP](../classes/parte-17-profundizacion-para-certificaciones/312-retencion-destruccion-segura-de-datos-y-dlp/README.md) — **las dos clases centrales de esta ruta**. Si solo pudieras estudiar dos, serían estas.
- 🔒 [289 · Privacidad y protección de datos](../classes/parte-14-grc-riesgo-y-cumplimiento/289-privacidad-y-proteccion-de-datos/README.md) y [281 · Cumplimiento GDPR, HIPAA y PCI DSS](../classes/parte-14-grc-riesgo-y-cumplimiento/281-cumplimiento-gdpr-hipaa-y-pci-dss/README.md) — **por qué** existe el DLP: la obligación legal detrás de la herramienta.
- 📐 [280 · Controles CIS](../classes/parte-14-grc-riesgo-y-cumplimiento/280-controles-cis/README.md) y [279 · NIST Cybersecurity Framework](../classes/parte-14-grc-riesgo-y-cumplimiento/279-nist-cybersecurity-framework/README.md) — los marcos que la oferta nombra como base de los lineamientos.
- 📘 [215 · Playbooks de respuesta a incidentes](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/215-playbooks-de-respuesta-a-incidentes/README.md) y [282 · Políticas, estándares y procedimientos](../classes/parte-14-grc-riesgo-y-cumplimiento/282-politicas-estandares-y-procedimientos/README.md) — la documentación operativa que se te va a pedir desde la primera semana.
- 🧱 [324 · Operaciones de seguridad, hardening y gestión de configuración](../classes/parte-17-profundizacion-para-certificaciones/324-operaciones-de-seguridad-hardening-y-gestion-de-configuracion/README.md) — los "planes de mejora y hardening" del puesto.
- 🚨 [202 · El ciclo de respuesta a incidentes (NIST y SANS)](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/202-el-ciclo-de-respuesta-a-incidentes-nist-y-sans/README.md) — el proceso con el que gestionas alertas e incidentes.
- 🔑 [313 · Gestión del ciclo de vida de identidades](../classes/parte-17-profundizacion-para-certificaciones/313-gestion-del-ciclo-de-vida-de-identidades-iam-empresarial/README.md) y [315 · MFA y accesos privilegiados (PAM)](../classes/parte-17-profundizacion-para-certificaciones/315-mfa-y-gestion-de-accesos-privilegiados-pam/README.md) — casi toda fuga de datos empieza en un permiso de más.
- 📊 [287 · Métricas de seguridad: KPIs y KRIs](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md) y [321 · Comunicación y reporte](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md) — el informe periódico que sostiene la renovación del servicio.

### Laboratorio y práctica

- 🧪 [`blue-team-soc`](../labs/blue-team-soc/README.md) — operar una plataforma real (ingesta,
  consultas, alertas) es lo más cercano a la operación diaria del puesto.
- 🧪 [`rootcause-windows`](../labs/rootcause-windows/README.md) — visibilidad y controles en el
  endpoint, que es donde se instala buena parte del DLP.
- 🧪 [`cloud-security`](../labs/cloud-security/README.md) — auditar postura y configuración: el tipo
  de revisión con el que armarás un plan de hardening.
- 📋 **Practica el entregable, no solo la herramienta:** escribe un **playbook** completo de un
  incidente de fuga de datos (detección, verificación, contención, comunicación al cliente y
  cierre) y un **informe mensual de servicio** de una página con métricas. Es exactamente lo que
  produce este puesto, y casi ningún candidato junior lo lleva a la entrevista.

## 🎓 Certificaciones

Con archivo en el programa (mapean a partes concretas):

- 🎓 [**CompTIA Security+** (SY0-701)](../certificaciones/comptia-security-plus-sy0-701.md) — la
  base y el filtro más habitual para entrar a un MSSP. Empieza aquí.
- 📋 [**CompTIA CySA+** (CS0-003)](../certificaciones/comptia-cysa-plus-cs0-003.md) — el siguiente
  paso natural: análisis de eventos, gestión de vulnerabilidades y respuesta, que es hacia donde
  crece la parte operativa del rol.

Fuera del programa, y muy relevantes aquí: la oferta pide como deseable **SC-401** (Microsoft
Information Security Administrator), que es **la certificación específica de clasificación,
etiquetado y DLP en Microsoft Purview** — si el cliente es Microsoft, es la más rentable que puedes
sacar. Y en general, la **certificación del fabricante de la plataforma que operes**: en un MSSP es
la moneda de cambio, suele financiarla la empresa y es lo que te hace facturable. Consulta el
[mapeo completo a certificaciones](../certificaciones/README.md) para ver la cobertura del programa.

## 📈 Progresión de carrera y salario

Ruta habitual dentro del proveedor: **Ingeniero de operación → Especialista de producto o líder
técnico de la cuenta → Arquitecto de soluciones o preventa → Jefatura de servicios gestionados**.
La bifurcación clásica llega a los 2–3 años: **profundizar en el producto** (te vuelves *el* experto
de una plataforma, camino muy bien pagado y muy demandado) o **abrirte hacia arquitectura y
preventa**, donde entra el componente comercial.

El otro salto típico es **pasarte al lado del cliente**: con dos años operando plataformas para
varias empresas, eres un candidato fuerte para un puesto in-house de
[SecOps](secops-engineer.md), [analista de ciberseguridad](analista-ciberseguridad.md) o gestión de
vulnerabilidades — normalmente con mejor calidad de vida y sin SLA encima.

Rangos **orientativos y aproximados** (brutos anuales; varían por proveedor, cartera de clientes y
—mucho— por el nivel de inglés — referencia, no promesa):

```text
Región                      Entrada (~1 año)       Especialista / líder técnico
--------------------------  ---------------------  ------------------------
LATAM                       USD 12k – 25k / año    USD 28k – 55k+ / año
Chile (MSSP/integrador)*    USD 16k – 30k / año    USD 32k – 60k+ / año
España                      EUR 21k – 30k / año    EUR 35k – 55k+ / año
Remoto (USD)                USD 40k – 70k / año    USD 80k – 130k+ / año
```

\* Los MSSP no suelen ser los que mejor pagan en el escalón de entrada, pero **forman, certifican y
exponen a muchísima tecnología** — es una inversión de 2–3 años que se cobra después, dentro o
fuera. El **inglés avanzado** mueve estos números más que casi cualquier otra variable, porque
habilita clientes y equipos regionales.

## ⚠️ Mitos y errores comunes

- **"Trabajar en un MSSP es soporte técnico de segunda."** Es operación de seguridad real, con
  responsabilidad sobre los controles de empresas que confían en ti. La diferencia es el modelo de
  negocio, no el nivel técnico.
- **"El DLP es poner unas reglas y listo."** Es de las disciplinas con **peor relación
  señal/ruido** del sector: una política mal calibrada genera cientos de falsos positivos, el
  negocio se queja, y la herramienta acaba desactivada. Afinar es el trabajo, no un ajuste inicial.
- **"El inglés se puede dejar para después."** En este puesto es requisito **obligatorio**, no
  deseable. Documentación, soporte del fabricante y certificaciones están en inglés.
- **"La documentación es burocracia."** En un MSSP los procedimientos son literalmente el producto:
  permiten que el servicio no dependa de una persona. Escribir bien te hace ascender.
- **"Como es entry level, no piden nada."** Piden **título de ingeniería** (obligatorio), un año de
  experiencia y experiencia demostrable en un pilar concreto. "Entry level" significa primer puesto
  *de este tipo*, no primer trabajo.
- **"Especializarse en datos es un nicho sin salida."** Al contrario: es una especialidad escasa,
  con demanda garantizada por regulación de privacidad, y transferible a privacidad, GRC y
  cumplimiento.
- **"El curso me da todo lo que pide la oferta."** No del todo; lee la nota de abajo.

> **Honestidad, sin marketing:** este programa te da **la base conceptual y normativa** del puesto
> —ciclo de vida y clasificación del dato, DLP, privacidad y PCI, controles CIS y NIST, operación e
> incidentes, hardening, playbooks, identidades y métricas—. Lo que **no** te da: la experiencia con
> la **plataforma comercial concreta** que vayas a operar (Purview, Forcepoint, Symantec, Netskope
> …), que se aprende con el fabricante y en el trabajo; el **inglés técnico avanzado**, que aquí es
> requisito obligatorio y no se estudia en este repositorio; el **título de ingeniería** que la
> oferta exige; y el **oficio de servicio** — SLA, trato con clientes, escalamiento a fabricantes y
> apoyo a preventa—, que solo se gana dentro. El curso te hace **entender lo que la plataforma hace
> y por qué**; el producto y el cliente los pones tú.

## 🚀 Siguientes pasos

1. **Empieza por 311 y 312.** Son el corazón de la especialidad y lo que te diferencia de cualquier
   otro candidato junior: casi nadie llega sabiendo hablar de clasificación del dato y DLP.
2. Añade el **porqué normativo** con **289** (privacidad), **281** (PCI DSS) y **280** (CIS): es lo
   que convierte una regla de DLP en una decisión justificable ante el cliente.
3. Cubre la **operación** con la Parte 8 (**182, 183, 189, 197**) y monta el lab
   [`blue-team-soc`](../labs/blue-team-soc/README.md).
4. **Escribe los entregables del rol**: un playbook de incidente de fuga de datos y un informe
   mensual de servicio con métricas. Llévalos a la entrevista.
5. **Trabaja el inglés técnico en paralelo desde hoy.** No es un extra de este puesto: es un
   requisito eliminatorio. Lee la documentación de un fabricante de DLP en inglés como práctica.
6. Saca la **Security+** como primer hito, y apunta a **SC-401** si el ecosistema del cliente es
   Microsoft — es la certificación que más directamente describe esta especialidad.
7. Cuando entrevistes, **pregunta con qué plataformas y cuántos clientes vas a trabajar**. Define
   por completo tu día a día y tu curva de aprendizaje.

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🏠 [Inicio del programa](../README.md)
