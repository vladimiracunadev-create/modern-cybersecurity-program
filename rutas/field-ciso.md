# 🛰️ Field CISO / Customer CISO

> El CISO **que no es tu CISO**. Trabaja para un proveedor —un fabricante de seguridad, un
> proveedor de nube, un MSSP, una consultora— y su día transcurre delante de los clientes de ese
> proveedor: entiende su problema, lo traduce a lenguaje ejecutivo, comparte lo que ha visto en
> otras organizaciones y ayuda a que la conversación técnica llegue al directorio. **No controla
> el presupuesto del cliente, no dirige a su equipo y no acepta su riesgo residual.**
>
> **Nivel de entrada:** ninguno; se llega con trayectoria en dirección de seguridad o consultoría
> senior · **Foco:** asesoría, comunicación ejecutiva, evangelización y acompañamiento comercial
> honesto · **Certificación faro:** CISSP + CISM (la credibilidad de la conversación, no el
> requisito formal)

**Alias y variantes:** *Field CISO*, *Customer CISO*, *Executive Security Advisor*, *Security
Advisor / Strategist*, *Office of the CISO* (nombre que varios proveedores dan al equipo entero),
*Cloud CISO* cuando el proveedor es de nube. La [página del ecosistema](ecosistema-ciso.md)
explica por qué «Cloud CISO» cae, casi siempre, dentro de esta guía.

**Fecha de consulta de las fuentes: 26 de agosto de 2026.**

## 🧭 Qué es y por qué importa

### Definición

Un Field CISO es un **profesional de nivel ejecutivo dentro de un proveedor** cuya materia prima
es la conversación con los responsables de seguridad de los clientes. Aporta contexto —qué está
pasando en el sector, qué han hecho otros, dónde suele fallar un proyecto— y ayuda a que el
cliente decida mejor. Que además exista un interés comercial detrás no lo invalida: lo obliga a
declararlo.

El **Customer CISO** es prácticamente el mismo puesto con el peso desplazado hacia la **cuenta ya
cliente**: adopción, valor obtenido, resolución de fricciones y relación a largo plazo, en lugar
de captación. Muchas empresas usan los dos nombres para el mismo trabajo; algunas los separan por
el momento del ciclo de vida del cliente.

### Nivel de consolidación del título

**Consolidado como práctica del sector, no estandarizado como cargo.** El título existe desde hace
años en fabricantes de seguridad, proveedores de nube y consultoras, y su contenido es reconocible
entre empresas; lo que varía enormemente es **a qué área reporta** (marketing, ventas, producto o
la oficina del CISO del proveedor) y **cuánto peso comercial explícito tiene**. Eso cambia el
puesto más que el nombre.

### Qué problema resuelve

Tres problemas a la vez, y por eso el puesto existe:

| Problema | De quién es el problema | Qué aporta el Field CISO |
|---|---|---|
| El proveedor habla de funcionalidades; el cliente necesita hablar de riesgo | Del proveedor | Traduce el producto a la conversación de riesgo, presupuesto y regulación que el cliente tiene de verdad |
| El CISO cliente está aislado: no sabe qué hacen los demás con su mismo problema | Del cliente | Aporta patrones observados en muchas organizaciones, sin revelar información de ninguna |
| El producto se construye lejos de la realidad operativa | Del proveedor | Devuelve a producto y a ingeniería lo que el mercado pide y lo que se rompe |

### Qué hace y qué no hace

| Sí hace | No hace |
|---|---|
| Sesiones de descubrimiento con la dirección del cliente | Auditorías independientes ni dictámenes de conformidad |
| Evaluaciones de madurez frente a un marco (NIST CSF, ISO 27001) como **insumo**, no como certificación | Certificar al cliente ni sustituir a un auditor acreditado |
| Recomendaciones con hipótesis y supuestos explícitos | Presentar la propuesta de su empresa como si fuera un dictamen neutral |
| Acompañar reuniones ejecutivas y responder al directorio del cliente | Decidir por el cliente ni aceptar su riesgo residual |
| Ponencias, contenido, webinars, mesas de trabajo del sector | Prometer resultados de seguridad («con esto no te hackean») |
| Retroalimentar la hoja de ruta del producto | Comprometer funcionalidades que producto no ha aprobado |
| Escalar internamente cuando el producto está fallando en un cliente | Ocultar una limitación conocida del producto |

### Dónde existe este cargo

Fabricantes de seguridad (endpoint, red, identidad, datos), proveedores de nube, MSSP y MDR,
consultoras grandes, integradores y algunas empresas de software con producto crítico. **No
existe** en la organización cliente: si dentro de tu empresa hay alguien llamado «Field CISO»,
casi seguro es un [BISO](biso.md) o un asesor interno con otro nombre.

## 🏛️ Mandato, autoridad y responsabilidad

### Línea de reporte

Depende de dónde lo hayan colgado, y esto define el puesto:

| Reporta a | Qué implica | Riesgo del modelo |
|---|---|---|
| **Oficina del CISO del proveedor** | Máxima credibilidad; el trabajo es de asesoría y de producto | Puede quedar lejos de la realidad comercial |
| **Ventas / preventa** | Acceso directo a cuentas y a la conversación real | La presión de cuota puede erosionar la honestidad del consejo |
| **Marketing / producto** | Mucho contenido, ponencias y voz pública | Riesgo de convertirse en portavoz sin contenido técnico |
| **Éxito del cliente (postventa)** | Es el patrón típico del **Customer CISO** | Riesgo de acabar haciendo soporte de nivel ejecutivo |

Pregunta por esta línea en la entrevista: dice más del día a día que la descripción del puesto.

### Autoridad y responsabilidad por el riesgo

- **Sobre el cliente: ninguna.** No firma políticas, no aprueba excepciones, no acepta riesgos, no
  dirige personas. Toda su capacidad es de influencia.
- **Sobre su propia empresa: variable.** Suele tener voz —a veces vinculante— en la hoja de ruta
  del producto, en el mensaje de mercado y en si una oportunidad concreta debería o no perseguirse.
- **Presupuesto:** el suyo de viajes, eventos y contenido, si acaso. Ninguno del cliente.
- **Equipo propio:** normalmente no; puede coordinar arquitectos de soluciones e ingenieros de
  preventa sin ser su jefe.

> ⚖️ **La frase que hay que decir en voz alta en la primera reunión:** «Trabajo para un proveedor
> que vende una solución en este espacio. Lo que les traiga puede estar sesgado por eso, así que
> voy a separar lo que observo de lo que opino y de lo que les propongo comprar.» Decirlo no te
> resta credibilidad: te la da.

### Conflictos de interés y límites éticos

Este es **el corazón del puesto** y lo que separa a un buen Field CISO de un vendedor con un
título grande.

| Situación | Límite | Qué hacer |
|---|---|---|
| El mayor riesgo del cliente **no** lo resuelve tu producto | No inventes que sí | Dilo, recomienda lo que corresponda aunque sea de la competencia, y deja constancia escrita |
| El cliente te pide una «auditoría» | Tu evaluación no es independiente | Llámala evaluación de madurez, declara el interés y recomienda un auditor externo si necesita un dictamen |
| Sabes de una vulnerabilidad no publicada de tu producto | La divulgación tiene un cauce | Sigue la política de divulgación de tu empresa; no la uses como argumento ni la ocultes al cliente afectado |
| Un cliente te cuenta su arquitectura y sus brechas | Es información confidencial de un tercero | No la reutilices con otro cliente, ni siquiera anonimizada, si es reconocible |
| El comercial te pide meter miedo para cerrar el trimestre | El miedo como técnica de venta es una falta profesional | Niégate por escrito y escala |
| Te piden firmar una recomendación que no sostienes | Tu nombre es tu único activo transferible | No la firmes |

La regla operativa, que además es el criterio con el que se te evalúa en este programa: en todo
documento que entregues, **separa cuatro cosas y etiquétalas**.

1. **Hecho observado** — lo que viste, con evidencia y fecha.
2. **Hipótesis** — lo que infieres, con lo que la sostiene y lo que la refutaría.
3. **Opinión profesional** — tu juicio, marcado como juicio.
4. **Propuesta del proveedor** — lo que tu empresa vende, con su precio y su alternativa.

## 🗓️ El día, el mes y el año

**Un día típico.** Preparación de una reunión con la dirección de una cuenta (leer su memoria
anual, su sector, sus incidentes públicos, no solo su arquitectura); esa reunión; una llamada
interna con producto para trasladar una carencia que ya han mencionado tres clientes; revisión de
un documento de recomendación que va a firmar tu nombre; media hora escribiendo un artículo o
preparando una charla.

**Un mes típico.** Entre cuatro y diez cuentas activas; una o dos evaluaciones de madurez; un
evento o webinar; una sesión con el equipo comercial para revisar el mensaje; una aportación
formal a la hoja de ruta del producto.

**Un año típico.** Un ciclo de conferencias del sector; la actualización del material cuando
cambia un marco de referencia (por ejemplo, la revisión de un estándar o una nueva obligación
regulatoria); la construcción de dos o tres **casos de referencia** publicables con permiso del
cliente; la retrospectiva de qué recomendaste y qué pasó después, que es la única métrica de
calidad real de este trabajo.

### Interlocutores

| Externos (cliente) | Internos (tu empresa) |
|---|---|
| CISO, Jefe de Seguridad, [BISO](biso.md) | Ventas y preventa |
| CIO, CTO, arquitectos | Producto e ingeniería |
| CRO, auditoría interna, cumplimiento | Marketing y comunicación |
| Comité de riesgo o directorio, en las cuentas grandes | Oficina del CISO del proveedor |
| Compras y legal, en la fase contractual | Éxito del cliente y soporte |

## 🧾 Entregables verificables

| Entregable | Qué demuestra | Cómo se verifica |
|---|---|---|
| **Formulario y acta de descubrimiento** | Que entendiste el negocio antes de proponer nada | Contiene el sector, el servicio crítico, la obligación regulatoria y el riesgo declarado por el cliente, con sus palabras |
| **Evaluación de madurez** frente a un marco | Que hay un diagnóstico, no una intuición | Perfil actual y objetivo por función, con la evidencia de cada puntuación |
| **Recomendación técnico-comercial transparente** | Que separas hecho, hipótesis, opinión y propuesta | Las cuatro etiquetas están presentes y el conflicto de interés está declarado |
| **Nota ejecutiva de una página** | Que un no técnico sabe qué decidir al terminarla | Decisión, plazo, coste, riesgo si no se hace |
| **Plan conjunto de éxito** (Customer CISO) | Que la relación tiene objetivos medibles | Hitos con fecha, dueño en ambas partes y criterio de cierre |
| **Informe de retroalimentación a producto** | Que el puesto devuelve valor hacia dentro | Carencias priorizadas con cuántos clientes las han pedido |
| **Charla o artículo publicado** | Capacidad de divulgación | Existe, es público y no es un folleto |

## 📏 KPI y KRI

Ojo con esto: la mitad de estas métricas empujan hacia el lado comercial y la otra mitad hacia el
lado de la confianza. Un puesto medido **solo** por las primeras deja de ser un Field CISO.

| Indicador | Tipo | Qué dice |
|---|---|---|
| Reuniones ejecutivas conseguidas y sostenidas | KPI | Si tienes acceso real a la altura correcta |
| Cuentas donde la conversación subió de nivel (de técnico a dirección) | KPI | El valor específico del puesto |
| Recomendaciones adoptadas y **resultado a 6–12 meses** | KPI | Si tu consejo era bueno, no solo persuasivo |
| Elementos de la hoja de ruta del producto originados en tu retroalimentación | KPI | Que el puesto cierra el círculo |
| Contenido publicado y su alcance cualificado | KPI | Presencia de mercado |
| Influencia en ingresos, cuando la empresa la mide | KPI (con cuidado) | Contribución comercial |
| **Recomendaciones que resultaron sesgadas hacia el producto propio** | **KRI** | La señal de alarma número uno |
| Clientes que dejaron de convocarte tras la venta | **KRI** | Estabas vendiendo, no asesorando |
| Compromisos de producto que no se cumplieron | **KRI** | Erosión de credibilidad, tuya y de la empresa |
| Información de un cliente reutilizada con otro | **KRI** | Falta grave: rompe la base del puesto |

## 🧠 Qué necesitas saber

### Competencias técnicas

Necesitas **amplitud con profundidad selectiva**: sostener una conversación con un arquitecto sin
farolear y con un director sin abrumarlo.

- **Marcos y gobierno:** NIST CSF (incluida la función *Gobernar*), ISO/IEC 27001, controles CIS,
  cómo se construye un programa y cómo se mide.
- **Operación:** cómo funciona de verdad un SOC, qué es y qué no es un SIEM, qué prometen y qué no
  cumplen el EDR y el XDR, cómo se mide la madurez de detección.
- **Respuesta a incidentes:** el ciclo completo, la diferencia entre contención y erradicación y
  por qué un ejercicio de mesa revela más que un simulacro técnico.
- **Nube y SDLC:** responsabilidad compartida, postura, identidad, cadena de suministro de
  software, por qué el SBOM importa y por qué no basta.
- **Riesgo de terceros:** el problema que tu propia empresa **es** para el cliente.
- **IA:** lo suficiente para no repetir el discurso de marketing de nadie, incluida tu empresa.

### Competencias de negocio

- Leer una memoria anual y encontrar el servicio del que depende el ingreso.
- Entender el modelo de negocio del cliente lo bastante para decir qué le duele más: la caída, la
  multa, la fuga o el retraso del proyecto.
- Construir un caso económico honesto: coste del control frente a pérdida esperada, con las
  hipótesis a la vista.
- Entender **tu propio** modelo de negocio: cómo se factura tu producto, qué margen tiene, qué
  parte del descuento es real. Sin eso te usan como decorado.

### Comunicación y negociación

Es la competencia que más pesa y la que menos se enseña.

- Escribir una página que un director lea entera y termine sabiendo qué decidir.
- Hablar en público sin diapositivas de producto.
- Sostener una mala noticia delante del cliente y de tu propio equipo comercial.
- Decir «no lo sé» y volver con la respuesta.
- Negociar dentro de tu empresa: defender ante ventas que una cuenta no está madura, y ante
  producto que una carencia es prioritaria.

### Competencias regulatorias

No para dar asesoría legal —no puedes—, sino para **no decir tonterías** y saber cuándo derivar:
qué obligaciones de reporte tiene el cliente y en qué plazos, qué régimen de datos personales le
aplica, qué exige su regulador sectorial y qué parte de eso toca tu producto. Ver el
[contexto chileno del ecosistema](ecosistema-ciso.md#-contexto-chileno-y-latinoamericano).

### Componente comercial

Existe y hay que gestionarlo, no negarlo:

- Participar en preventa está bien; **firmar como independiente una evaluación que sustenta tu
  propia venta, no**.
- Conocer el precio y las alternativas del cliente, incluida la de no hacer nada.
- Saber retirarte de una oportunidad que no es buena para el cliente y explicar por qué a tu
  empresa. Es lo que construye la reputación que hace funcionar el puesto los siguientes cinco
  años.

## 📚 Tu ruta en el programa

Empieza por la [**Parte 0**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md) si te
falta base técnica; el resto es el recorrido específico del puesto.

1. **Fundamentos y ética**
   - [**001** · Qué es la ciberseguridad: tríada CIA, AAA y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md)
   - [**002** · El panorama de amenazas moderno](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md) — el material del que vive tu conversación
   - [**003** · Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md)
   - [**025** · Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md) — **la clase que sostiene este puesto**
2. **Gobierno y riesgo, el idioma del cliente** — [Parte 14](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md)
   - [**276** · Gobernanza](../classes/parte-14-grc-riesgo-y-cumplimiento/276-gobernanza-de-la-seguridad-de-la-informacion/README.md) · [**277** · Gestión de riesgos](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md) · [**278** · ISO/IEC 27001](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md) · [**279** · NIST CSF](../classes/parte-14-grc-riesgo-y-cumplimiento/279-nist-cybersecurity-framework/README.md)
   - [**284** · Riesgo de terceros y proveedores](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md) — **léela desde el otro lado: el tercero eres tú**
   - [**287** · Métricas KPI y KRI](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md) · [**288** · Seguros cibernéticos](../classes/parte-14-grc-riesgo-y-cumplimiento/288-seguros-ciberneticos/README.md)
3. **Comunicación, contrato y programa**
   - [**321** · Comunicación y reporte](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md) — el músculo central del puesto
   - [**320** · Gobierno, aspectos legales y gestión del programa](../classes/parte-17-profundizacion-para-certificaciones/320-gobierno-aspectos-legales-regulatorios-y-gestion-del-programa/README.md)
   - [**328** · Riesgo cuantitativo y continuidad avanzada](../classes/parte-17-profundizacion-para-certificaciones/328-gestion-de-riesgos-cuantitativa-y-continuidad-avanzada/README.md) — para hacer un caso económico defendible
   - [**067** · Reglas de compromiso, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md) · [**085** · Reporte profesional](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md) — cómo se acota y se entrega un trabajo a un cliente
4. **Suficiente operación para no farolear**
   - [**181** · El SOC moderno](../classes/parte-8-blue-team-deteccion-y-soc/181-el-soc-moderno-roles-niveles-y-procesos/README.md) · [**183** · SIEM](../classes/parte-8-blue-team-deteccion-y-soc/183-siem-arquitectura-y-componentes/README.md) · [**195** · Threat intelligence](../classes/parte-8-blue-team-deteccion-y-soc/195-threat-intelligence-operacional/README.md) · [**197** · Métricas y madurez del SOC](../classes/parte-8-blue-team-deteccion-y-soc/197-metricas-y-madurez-del-soc/README.md)
   - [**202** · Ciclo de respuesta a incidentes](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/202-el-ciclo-de-respuesta-a-incidentes-nist-y-sans/README.md) · [**219** · Ejercicios de mesa](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md)
5. **Los dominios donde hoy están las conversaciones**
   - [**221** · Responsabilidad compartida en la nube](../classes/parte-10-seguridad-en-la-nube-y-contenedores/221-fundamentos-de-seguridad-en-la-nube-y-responsabilidad-compartida/README.md) · [**231** · CSPM](../classes/parte-10-seguridad-en-la-nube-y-contenedores/231-cloud-security-posture-management-cspm/README.md)
   - [**236** · Secure SDLC](../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md) · [**246** · SBOM y SLSA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md)
   - [**300** · Gobernanza y ética de la IA segura](../classes/parte-15-seguridad-de-ia-y-machine-learning/300-gobernanza-y-etica-de-la-ia-segura/README.md)

### Laboratorio y práctica

- 🧪 **[`labs/ciso-leadership`](../labs/ciso-leadership/README.md)** — tu laboratorio principal.
  Escenarios **8** (sesión de descubrimiento como Field CISO) y **9** (recomendación
  técnico-comercial transparente) están escritos para este puesto; los escenarios **1**, **2** y
  **6** te dan el material que tu cliente maneja.
- 🧪 [`cloud-security`](../labs/cloud-security/README.md) y
  [`blue-team-soc`](../labs/blue-team-soc/README.md) — para no perder el contacto técnico y poder
  decir «esto lo he hecho» en lugar de «esto se hace».

### Capstone

**Ciclo completo de una cuenta, con el conflicto de interés a la vista.** Sobre una organización
ficticia del laboratorio:

1. Ejecuta la **sesión de descubrimiento** y entrega el acta con las palabras del cliente.
2. Produce una **evaluación de madurez** frente a NIST CSF con la evidencia de cada puntuación.
3. Entrega una **recomendación técnico-comercial** de tres opciones —una de ellas explícitamente
   sin tu producto— con las cuatro etiquetas (hecho, hipótesis, opinión, propuesta) y la
   declaración de interés.
4. Redacta la **nota ejecutiva de una página** para el directorio del cliente.
5. Escribe el **informe de retroalimentación** a tu producto.

**Criterio de aceptación:** un lector que no sepa para quién trabajas debe poder identificar, sin
ayuda, qué parte del documento es un hecho y qué parte es una propuesta comercial. Si no puede, el
capstone no está aprobado.

### Portafolio

- El paquete completo del capstone, con los datos ficticios visibles.
- Una charla de quince minutos grabada, sin diapositivas de producto.
- Un artículo técnico-ejecutivo publicado.
- Una evaluación de madurez con su matriz de evidencias.
- Una recomendación donde recomendaste **no comprar** y por qué.

## 🎤 Preguntas de entrevista

1. Cuéntame la última vez que le dijiste a un cliente que tu producto no era su prioridad. ¿Qué
   pasó después, dentro y fuera de tu empresa?
2. ¿Cómo separas en un documento lo que observaste de lo que opinas y de lo que vendes?
3. Un cliente te pide una «auditoría independiente». ¿Qué le respondes exactamente?
4. ¿A quién reportarías en este puesto y cómo afectaría eso a lo que puedes decir?
5. El equipo comercial quiere que uses un incidente reciente de la competencia para meter presión.
   ¿Qué haces?
6. ¿Cómo mides si tu consejo fue bueno, no solo si convenció?
7. Explícame la responsabilidad compartida en la nube a un director financiero en dos minutos.
8. ¿Qué haces con lo que un cliente te cuenta en confianza cuando le sirve a otro?
9. ¿Qué carencia de tu producto actual llevarías tú mismo a la hoja de ruta y con qué argumento?
10. ¿Cuándo has cambiado de opinión por lo que te dijo un cliente?

## 🎓 Certificaciones

Ninguna certificación te da este puesto: te lo da la trayectoria y la capacidad de conversación.
Lo que hacen las credenciales aquí es **abrir la puerta y sostener la credibilidad** delante de un
CISO cliente que las tiene.

| Certificación | Para qué sirve en este puesto | Dónde la cubre el programa |
|---|---|---|
| **CISSP** (ISC2) | El lenguaje común con casi cualquier CISO cliente | [Parte 17](../classes/parte-17-profundizacion-para-certificaciones/README.md) y [**304**](../classes/parte-16-capstones-y-preparacion-de-certificaciones/304-preparacion-cissp-los-8-dominios/README.md) |
| **CISM** (ISACA) | Gestión del programa: es el examen que más se parece a la conversación del puesto | [Parte 14](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md) (fuera del programa como examen) |
| **CRISC** (ISACA) | Riesgo, si tus cuentas son financieras | [277](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md) y [328](../classes/parte-17-profundizacion-para-certificaciones/328-gestion-de-riesgos-cuantitativa-y-continuidad-avanzada/README.md) |
| **ISO/IEC 27001 Lead Implementer / Auditor** | Para hablar de SGSI con propiedad y saber dónde acaba tu evaluación | [278](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md) |
| Certificación **del fabricante** para el que trabajes | Requisito práctico habitual | Fuera del programa, por definición |

> Ninguna de estas garantiza empleo, y presentarlas como garantía es exactamente el tipo de
> afirmación que este puesto no debe hacer. Ver [**301** · Roadmap de certificaciones](../classes/parte-16-capstones-y-preparacion-de-certificaciones/301-roadmap-de-certificaciones-comptia-oscp-cissp-y-mas/README.md).

## 📈 Progresión de carrera y salario

### Cargos de entrada y experiencia previa razonable

No es un puesto de entrada. Las tres vías que funcionan:

| Vía de origen | Qué traes de sobra | Qué te falta y hay que construir |
|---|---|---|
| **Has sido CISO o Jefe de Seguridad** | Credibilidad, cicatrices, criterio ejecutivo | La conversación comercial honesta y la exposición pública |
| **Consultoría senior o preventa técnica** | Trato con clientes, hablar en público, ritmo comercial | Altura ejecutiva y experiencia real de haber respondido por un programa |
| **Arquitectura o liderazgo técnico en un fabricante** | Producto y profundidad | El idioma del negocio y del riesgo |

Una experiencia previa razonable —**no un requisito universal, y desconfía de quien te dé un número
exacto**— combina años de responsabilidad sobre un programa de seguridad con exposición sostenida
a clientes. Lo que se comprueba en la entrevista no son los años: es si puedes sostener una hora
delante de un directorio.

### Hacia dónde sigue

Field CISO → **líder de la oficina del CISO** del proveedor · → **CISO del propio proveedor** ·
→ vuelta a un cargo interno de [CISO](ciso.md) con una red de contactos mucho mayor ·
→ [vCISO o consultor independiente](vciso.md) · → asesoría de directorios.

### Sobre la remuneración

**Este programa no publica cifras para este puesto, a propósito.** La retribución del Field CISO
tiene una estructura particular —base más un componente variable ligado a objetivos comerciales o
de cuenta— y ese reparto varía tanto entre empresas que cualquier rango sería más engañoso que
útil. Lo que sí puedes hacer:

1. Preguntar en el proceso **qué porcentaje es variable y de qué depende**: si depende de cierres,
   sabes qué puesto te están ofreciendo de verdad.
2. Usar como referencia orientativa los rangos de la [ruta CISO](ciso.md#-progresión-de-carrera-y-salario),
   con la advertencia que allí se hace.
3. Contrastar con estudios de remuneración con **fecha y metodología publicadas**, y tratar las
   ofertas de empleo como evidencia contextual, no como dato.

## ⚠️ Mitos y errores comunes

- **«Field CISO es un CISO.»** No lo es. Comparte vocabulario y no comparte mandato. El CISO
  responde por un programa; el Field CISO responde por una conversación.
- **«Es un vendedor con un título elegante.»** Tampoco, si el puesto está bien montado. La prueba
  está en si puede recomendar no comprar y seguir en la empresa al mes siguiente.
- **«Mi evaluación equivale a una auditoría.»** No: te paga el proveedor que además vende la
  solución. Es un insumo valioso y no es un dictamen independiente.
- **«Como asesoro, no me alcanza la confidencialidad.»** Al contrario: manejas información de
  varios competidores del mismo sector. Es el puesto con más obligación de compartimentar.
- **«Si el cliente me hace caso, cumplí.»** El éxito se mide a doce meses, no en la reunión.
- **«Customer CISO y Field CISO son cosas distintas.»** Rara vez. Pregunta por el momento del
  ciclo de vida del cliente y sabrás cuál te están ofreciendo.
- **Señal de cargo decorativo:** te contratan por tu nombre, te ponen en el material de marketing
  y no te dejan hablar con producto ni discrepar en una cuenta. Estás siendo un logotipo.

## ↔️ Diferencias con los cargos vecinos

| Frente a | Se parecen en | Se separan en |
|---|---|---|
| [**CISO**](ciso.md) | Vocabulario, marcos, altura de conversación | El CISO tiene mandato, presupuesto, equipo y responde ante su directorio. El Field CISO no tiene nada de eso sobre el cliente |
| [**vCISO / Fractional / Interim**](vciso.md) | Ambos son externos y cobran de otro sitio | El vCISO **ejerce funciones** dentro del cliente por contrato; el Field CISO nunca ejerce, solo asesora. Y el vCISO no vende un producto |
| **Arquitecto de soluciones / preventa técnica** | Ambos acompañan la venta | La preventa trabaja la solución técnica; el Field CISO trabaja el riesgo y la decisión ejecutiva |
| [**Consultor GRC**](grc.md) | Ambos evalúan madurez | El consultor puede ser independiente y facturar por el diagnóstico; el Field CISO tiene un producto detrás y debe declararlo |
| **Auditor externo** | Ambos revisan controles | El auditor emite un dictamen bajo un marco y una acreditación; el Field CISO, jamás |
| [**BISO**](biso.md) | Ambos traducen entre mundos | El BISO traduce **dentro** de una organización; el Field CISO, **entre** dos organizaciones |
| **Evangelista técnico** | Ambos hablan en público | El evangelista promueve el producto; el Field CISO promueve una decisión mejor, aunque no incluya el producto |

## 📎 Fuentes y fecha de consulta

Consultadas el **26 de agosto de 2026**.

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — marco de la evaluación
  de madurez que produce este puesto; la función *Gobernar* estructura la conversación ejecutiva.
- [ISO/IEC 27001](https://www.iso.org/standard/27001) — referencia del SGSI del cliente. Norma de
  pago: este programa explica sus conceptos, no reproduce su texto.
- [ISACA](https://www.isaca.org/) e [ISC2](https://www.isc2.org/) — cuerpos de conocimiento de
  CISM, CRISC y CISSP, y sus respectivos códigos de ética profesional, que son la base de la
  sección de conflictos de interés de esta guía.
- [ENISA](https://www.enisa.europa.eu/) y [CISA](https://www.cisa.gov/) — panorama de amenazas y
  guías sectoriales que alimentan el contexto que aportas al cliente.
- [Ecosistema CISO de este programa](ecosistema-ciso.md) — taxonomía, matriz comparativa y
  contexto chileno con sus fuentes normativas.

## 🚀 Siguientes pasos

1. Lee el [ecosistema CISO](ecosistema-ciso.md) entero: este puesto solo se entiende por contraste.
2. Haz los escenarios **8** y **9** del [laboratorio ejecutivo](../labs/ciso-leadership/README.md).
3. Resuelve la [evaluación del ecosistema](../labs/ciso-leadership/EVALUACION.md), con especial
   atención al caso de conflicto de interés en preventa.
4. Rinde el [examen final de Field CISO](../docs/examen-final-por-rol.md).
5. Si lo que quieres es **ejercer** y no asesorar, tu página es [vCISO](vciso.md); si quieres el
   mandato interno, es [CISO](ciso.md).

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🗂️ [El ecosistema CISO](ecosistema-ciso.md) — mapa de cargos, matriz comparativa y test del mandato
- 🧾 [vCISO](vciso.md) · 🎩 [CISO](ciso.md) · 🏛️ [GRC](grc.md)
- 🧪 [Laboratorio ejecutivo CISO](../labs/ciso-leadership/README.md) · 🎓 [Evaluación del ecosistema](../labs/ciso-leadership/EVALUACION.md)
- 🏠 [Inicio del programa](../README.md)
