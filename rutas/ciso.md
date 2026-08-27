# 🎩 CISO / Director de Seguridad de la Información

> El **máximo responsable** de la seguridad de la información y la ciberseguridad de una
> organización. En español, *Director de Seguridad de la Información*. Su función **no es
> "evitar hackers"**: es proteger los **datos**, los **sistemas**, los **servicios digitales** y la
> **continuidad operacional del negocio** — y responder por ello ante la dirección, el directorio,
> el regulador y, cuando hay brecha, ante los clientes.
>
> **Nivel de entrada:** ninguno; es un cargo de dirección al que se llega con 8–15 años de carrera · **Foco:** mandato, estrategia, riesgo empresarial, presupuesto, cumplimiento y resiliencia · **Certificación faro:** CISSP + CISM (y CRISC / ISO 27001 Lead Implementer según el peso del cargo)

## 🧭 Qué es y por qué importa

> 🗂️ **¿Te han ofrecido un cargo con «CISO» en el nombre y no sabes si es este?** El programa tiene
> un mapa completo del ecosistema —Global, Regional, Divisional, Deputy y Associate CISO; Field
> CISO y Customer CISO; vCISO, fractional e interim; BISO, Product CISO, AI CISO y OT CISO; y los
> cargos vecinos que **no** son tipos de CISO—, con una matriz comparativa y un test de ocho
> preguntas para comprobar si un cargo tiene mandato real:
> **[🗂️ El ecosistema CISO](ecosistema-ciso.md)**.

Un CISO es la persona que tiene **el mandato formal** de la seguridad de la información en la
organización: define la estrategia, la financia, la ejecuta a través de su equipo y de otras áreas,
y **responde por el resultado**. No es un rol de consola ni de herramienta. Es un rol de dirección
cuya materia prima es el riesgo del negocio.

La confusión más extendida —dentro y fuera del sector— es reducir el cargo a "el que impide que
nos hackeen". Eso es una parte, y ni siquiera la mayor. Un CISO responde de cuatro cosas
simultáneamente:

| Ámbito | Qué significa en la práctica | Cómo se demuestra |
|---|---|---|
| 🗄️ **Datos** | Saber qué datos existen, dónde están, quién los toca, cómo se clasifican, cuánto se retienen y cómo se destruyen. Incluye datos personales y el deber legal que arrastran. | Inventario y clasificación, controles de acceso, cifrado, DLP, registro de tratamientos |
| 🖥️ **Sistemas** | Que la infraestructura y las aplicaciones estén configuradas, parcheadas, segmentadas y monitorizadas — las propias y las de terceros. | Hardening, gestión de vulnerabilidades con SLA, arquitectura revisada, telemetría |
| 🌐 **Servicios digitales** | Que lo que el cliente usa —la web, la app, la API, el canal de pago— siga funcionando, íntegro y disponible. Es donde la seguridad toca ingresos directamente. | Disponibilidad, protección DDoS/WAF, seguridad en el SDLC, gestión de incidentes |
| 🔁 **Continuidad operacional** | Que la organización siga operando cuando algo falle: ransomware, caída de un proveedor crítico, un centro de datos, un error humano. | BIA, RTO/RPO acordados, plan de continuidad **probado**, copias verificadas |

Importa porque estas cuatro cosas dejaron de ser un asunto de TI. Una brecha hoy es un evento
**financiero, legal y reputacional**: multas por protección de datos, interrupción del servicio,
demandas, cláusulas contractuales incumplidas y clientes que se van. La organización necesita a
alguien con nombre y apellido que sostenga esa exposición, la explique en el idioma del directorio y
la reduzca con un presupuesto finito. Ese alguien es el CISO.

Y en sectores regulados —banca, pensiones, seguros, salud, telecomunicaciones, utilities,
administración pública— el cargo **existe por obligación normativa**, no por convicción. La ley
exige que la responsabilidad esté asignada, documentada y sea auditable.

### Cómo se diferencia de las rutas vecinas

Este es el punto donde más gente se pierde, porque los títulos se solapan:

| Rol | Alcance | Autoridad | Ante quién responde |
|---|---|---|---|
| **CISO / Director de Seguridad** (esta ruta) | Toda la organización, incluido lo que no es TI | Mandato formal, presupuesto propio, veto argumentado | Directorio / CEO / comité de riesgo |
| [**Jefe de Seguridad de la Información**](ciso-jefe-seguridad.md) | El programa de seguridad y su equipo | Prioriza y ejecuta; el presupuesto lo pide | Gerencia de TI o de riesgo |
| [**GRC / Gestión de seguridad**](grc.md) | Gobierno, riesgo y cumplimiento | Asesora y mide; no decide | El CISO o auditoría interna |
| [**Analista de Ciberseguridad**](analista-ciberseguridad.md) / [**SOC**](soc-blue-team.md) | La operación diaria | Ejecuta | Su jefatura directa |
| [**Field CISO / Customer CISO**](field-ciso.md) | Las cuentas de clientes que atiende | **Ninguna sobre el cliente**: influye, no decide | Su empleador, que es **un proveedor** |
| [**vCISO / Fractional / Interim**](vciso.md) | Lo que diga el contrato | La que el contrato le conceda | La dirección de la empresa contratante |
| [**BISO**](biso.md) | Una unidad de negocio | Influencia fuerte, decisión limitada | El CISO y la dirección de su unidad |
| [**Product CISO**](product-ciso.md) | Lo que la empresa **vende** | Puertas de publicación y requisitos | Ingeniería, producto y clientes |
| [**AI CISO**](ai-ciso.md) | Los sistemas de IA | Normativa: la evaluación previa | El CISO o un comité de IA |
| [**OT CISO**](ot-ciso.md) | La planta y el proceso físico | **Compartida** con Operaciones | Tecnología y dirección industrial |

Dicho corto: el [jefe de seguridad](ciso-jefe-seguridad.md) **dirige el programa**; el CISO
**es dueño del riesgo de seguridad de la empresa**. En organizaciones medianas la misma persona
hace ambas cosas y el título depende del tamaño; en organizaciones grandes son dos capas distintas
y el jefe de seguridad reporta al CISO.

La comparación completa —con las diez columnas que de verdad separan estos cargos: interno o
externo, alcance, autoridad, presupuesto, equipo, responsabilidad por el riesgo, audiencia,
componente comercial y entregables— está en la
[**matriz central del ecosistema CISO**](ecosistema-ciso.md#-matriz-comparativa-central).

### Los alcances del cargo: global, regional, divisional, deputy y associate

Estos cinco títulos **no son cargos distintos**: son este mismo cargo con otro alcance. El trabajo
esencial —mandato, estrategia, riesgo, presupuesto, equipo, crisis y relación con el gobierno de la
organización— es el que se explica en esta página. Lo que cambia es el perímetro y, con él, dos o
tres tensiones características.

| Alcance | Qué cambia de verdad | La tensión propia del puesto |
|---|---|---|
| **Global CISO** | Responde por todo el grupo, en varios países y varios marcos legales | Decidir qué es **política global vinculante** y qué es adaptación local. Si todo es global, nada se cumple; si todo es local, no hay programa |
| **Regional CISO** | Una región (LatAm, EMEA, APAC), bajo una política corporativa | Vive entre dos jefes. Ejecuta lo global y a la vez responde por obligaciones locales que la casa matriz no siempre entiende |
| **Divisional / BU CISO** | Una división o filial con su propio resultado, normalmente con presupuesto propio | Alinearse con el programa corporativo sin ahogar a un negocio que tiene su propio ritmo y sus propios clientes |
| **Deputy CISO** | Delegación amplia; cubre al CISO y suele llevar la ejecución del programa | Ejecutar sin ser el titular: toma decisiones diarias sin la autoridad formal de firmarlas todas |
| **Associate CISO** | Un dominio acotado, como escalón de progresión interna | Título poco estandarizado: hay que comprobar qué incluye antes de aceptarlo |

Tres advertencias que valen para los cinco:

1. **El adjetivo no da poder.** «Global» describe geografía, no autoridad. Un Global CISO sin
   presupuesto consolidado y sin línea al directorio decide menos que un Divisional CISO que sí los
   tiene.
2. **En un grupo, la pregunta clave es dónde vive el presupuesto.** Si cada filial financia su
   seguridad, el CISO de grupo influye; si el presupuesto se consolida arriba, manda. Todo lo demás
   —comités, políticas, reportes— se deriva de ahí.
3. **El Divisional CISO no es un [BISO](biso.md).** El primero tiene mandato y presupuesto de su
   división; el segundo es un enlace sin presupuesto. Si una oferta usa los dos términos como
   sinónimos, la oferta no sabe lo que ofrece.

## 🏛️ Mandato, autoridad y línea de reporte

Antes que las herramientas y que los marcos, un CISO se define por **tres preguntas** que hay que
resolver el primer mes. Quien no las resuelve tiene el título pero no el cargo:

1. **¿A quién reporto?** Un CISO que depende del gerente de TI tiene un conflicto estructural: la
   mayoría de sus hallazgos apuntan a decisiones de su propio jefe (deuda técnica, parches
   aplazados, proyectos entregados sin controles). La configuración sana es reportar al **CEO, al
   directorio o a riesgo/compliance**, con una vía de escalamiento que no pase por TI. En la
   entrevista, esta pregunta vale más que el salario.
2. **¿Qué decido yo y qué decide el negocio?** El CISO **propone** controles, cuantifica el riesgo
   y recomienda; el dueño del proceso de negocio es quien **acepta** el riesgo residual. Y esa
   aceptación va **firmada, fechada y con vigencia**. Es la diferencia entre un profesional y un
   chivo expiatorio.
3. **¿Con qué presupuesto y qué equipo?** Un mandato sin recursos es un mandato decorativo. Si la
   respuesta es "empieza y ya veremos", el número que hay que llevar al comité es el del riesgo sin
   tratar, no el de la ilusión.

Los instrumentos formales del cargo son tres: la **política de seguridad aprobada por el máximo
órgano de gobierno** (es lo que te da autoridad sobre áreas que no te reportan), el **comité de
seguridad** (donde el negocio participa de las decisiones y por tanto las asume) y el **registro de
riesgos con aceptaciones firmadas** (la trazabilidad de quién decidió qué). Sin los tres, el cargo
se sostiene solo en la simpatía personal, que se agota en el primer conflicto.

> **La autoridad real de un CISO es prestada.** Casi nadie de quien depende el arreglo te reporta:
> lo parchea infraestructura, lo corrige desarrollo, lo firma legal y lo paga finanzas. Se gobierna
> con datos, con comité y con credibilidad — no con jerarquía.

### Con quién te relacionas y qué negocias con cada uno

Buena parte del cargo es una red de relaciones con pares que no te reportan y a los que no puedes
dar órdenes. Cada una tiene su propia moneda de cambio:

| Interlocutor | Qué espera de ti | Qué necesitas de él | La tensión que hay que gestionar |
|---|---|---|---|
| **CEO** | Que el riesgo no le explote y que no le frenes el negocio | Respaldo público cuando hay que imponer un control impopular | Te mide por ausencia de problemas, que es justo lo que no se puede demostrar |
| **Directorio y comité de riesgo** | Una página, cifras comparables y decisiones claras | Aprobación de la política, del apetito de riesgo y del presupuesto | Ven seguridad dos veces al año: cada sesión tiene que valer por seis meses |
| **CIO / CTO** | Que no bloquees entregas ni proyectos | Inventario, arquitectura, capacidad de parcheo y de despliegue | Sus incentivos son entregar rápido; los tuyos, entregar seguro. Si además le reportas, el conflicto es estructural y hay que compensarlo con una vía de escalamiento |
| **CRO / riesgo operacional** | Riesgo cibernético en su taxonomía y comparable con los demás | Que el riesgo cibernético entre en el mapa de riesgos de la empresa | Traducir controles técnicos a categorías de riesgo empresarial sin perder el significado |
| **Auditoría interna** | Evidencia, no explicaciones | Que sus hallazgos empujen lo que tú no consigues empujar solo | No puedes auditarte a ti mismo: lo que tú diseñas, otro lo revisa |
| **Legal y cumplimiento** | Aviso temprano y decisiones documentadas | Interpretación de obligaciones y redacción de cláusulas | Legal responde a la ley; tú, al riesgo. No siempre coinciden |
| **[DPO](ecosistema-ciso.md#d-cargos-vecinos-que-no-son-tipos-de-ciso)** | Colaboración sin absorción | Criterio de privacidad en decisiones sobre datos | Su independencia está protegida: no se integra en tu equipo ni depende de ti |
| **Finanzas** | Un caso económico defendible | El presupuesto y su ejecución | Compites con proyectos que sí tienen retorno demostrable |
| **Recursos humanos** | Un programa de cultura que no moleste | Altas, bajas, disciplina y el proceso de desvinculación | La baja de un empleado es un control de seguridad y casi nunca se trata como tal |
| **Reguladores** | Interlocución seria y plazos cumplidos | Claridad sobre qué te aplica | No se improvisa en crisis: la relación se construye antes |
| **Clientes corporativos y aseguradoras** | Evidencia verificable de tus controles | Que sus exigencias financien mejoras reales | Sus cuestionarios pueden ser tu mejor palanca presupuestaria |

### Delegar sin dejar de responder

Un CISO delega la **ejecución**, nunca la **responsabilidad**. La distinción es sencilla de decir y
difícil de sostener:

- **Se delega:** operar controles, dirigir la respuesta técnica, mantener el registro de riesgos,
  llevar la relación diaria con un proveedor, preparar el informe.
- **No se delega:** la relación con el directorio, la firma de la política, la coherencia del
  programa, la decisión de escalar un riesgo que el negocio quiere enterrar, y la conversación
  incómoda con un par que no quiere aplicar un control.
- **Regla práctica:** cada delegación se documenta —qué, a quién, con qué límite y hasta cuándo— y
  se acompaña de un punto de retorno de información. Delegar sin punto de retorno no es delegar: es
  desentenderse.

Con [Deputy CISO](ecosistema-ciso.md#a-dirección-interna-y-jerarquía), [BISO](biso.md) o
[vCISO](vciso.md) contratados, la regla se vuelve más importante, no menos: **cuanto más reparto
hay, más explícito tiene que ser quién responde por qué**.

### El modelo operativo de la oficina del CISO

En cuanto el cargo pasa de una persona a un área, hay que decidir cómo se organiza. Cinco funciones
cubren casi todo, y en organizaciones pequeñas las hace la misma persona en días distintos:

| Función | Qué produce | Con quién trabaja |
|---|---|---|
| **Gobierno y riesgo** | Política, registro de riesgos, comité, métricas, cumplimiento y auditoría | Legal, riesgo, auditoría, [GRC](grc.md) |
| **Arquitectura e ingeniería de seguridad** | Estándares, revisión de diseño, controles nuevos | [Arquitectura](arquitecto-it-ot.md), TI, [nube](cloud-security.md) |
| **Operaciones de seguridad** | Detección, respuesta, vulnerabilidades, accesos | [SOC](soc-blue-team.md), [SecOps](secops-analista.md), TI |
| **Seguridad de producto o de aplicaciones** | Ciclo de desarrollo seguro, requisitos, revisión de código | [AppSec](appsec.md), [DevSecOps](devsecops-engineer.md), [Product CISO](product-ciso.md) |
| **Enlace con el negocio** | Traducción, priorización, excepciones | [BISO](biso.md), dueños de proceso |

Dos decisiones definen el modelo más que el organigrama: **qué se externaliza** (el monitoreo
24 × 7 casi siempre; el criterio, nunca) y **qué se federa** en las unidades de negocio frente a
qué se centraliza. Ambas se revisan cada año, porque la organización cambia.

### Tener el título frente a tener el mandato

Se puede llevar la tarjeta y no tener el cargo. La prueba está en tres respuestas:

1. ¿Existe un presupuesto de seguridad y lo firmas o lo defiendes tú?
2. ¿Quién firma la aceptación de un riesgo que decides no tratar? Si la respuesta es «tú», te han
   dado la responsabilidad sin la autoridad.
3. ¿Puedes detener un despliegue o una compra, y está escrito en algún sitio?

Si las tres respuestas son negativas, el cargo es **decorativo**: la organización ha nombrado a un
responsable para poder señalarlo, no para que cambie nada. Es una situación negociable —muchos CISO
empiezan así y construyen el mandato— pero hay que verla antes de firmar, no después. El
[test completo de ocho preguntas](ecosistema-ciso.md#-el-test-del-mandato-cómo-comprobar-un-cargo-real)
está en la página del ecosistema.

## 🗓️ El año del CISO

El día a día del cargo se entiende mal si se mira un solo día: el trabajo tiene **ciclo anual**, y
los incidentes lo interrumpen sin avisar.

- **Ciclo estratégico (anual).** Revisión del **plan director de seguridad** a 2–3 años, defensa del
  **presupuesto** (capex, opex, personas, licencias, servicios gestionados), y actualización del
  apetito de riesgo con el directorio.
- **Ciclo de riesgo (trimestral).** Revisión del registro de riesgos, riesgos nuevos por proyectos
  o cambios regulatorios, seguimiento de tratamientos y **renovación de las aceptaciones vencidas**.
- **Ciclo de cumplimiento (marcado por terceros).** Auditoría interna, auditoría externa,
  certificación del SGSI, requerimientos del regulador, cuestionarios de clientes corporativos y
  cierre de observaciones de la vuelta anterior.
- **Ciclo operativo (mensual).** El **informe ejecutivo**: vulnerabilidades críticas abiertas y su
  antigüedad, cobertura de parches y de EDR, incidentes y su impacto, avance del plan, presupuesto
  ejecutado. Una página. En el idioma del comité.
- **Ciclo de resiliencia (semestral/anual).** Simulacro de continuidad, **prueba real de
  restauración de copias** (no el informe que dice que existen) y **ejercicio de mesa** de crisis
  con la alta dirección, incluido el guion de comunicación.
- **Ciclo de cultura (continuo).** Programa de concienciación, campañas de phishing simulado y
  formación específica a los grupos de mayor exposición (finanzas, RR. HH., dirección).
- **Continuo, todo el año.** Revisión de seguridad de proyectos nuevos y de proveedores, contratos y
  cláusulas, relación con legal y privacidad, y **desbloquear al equipo**.
- **Cuando hay incidente grave.** Diriges la crisis: comité, decisiones (apagar o no apagar, pagar o
  no pagar, notificar o no notificar), reloj regulatorio de notificación, comunicación a clientes,
  legal, aseguradora y —si escala— prensa. No estás en la consola: estás sosteniendo las decisiones
  que nadie más puede tomar.

Sin adornos: es un cargo de **reunión, política organizacional, documento y presión**. Se toca
mucha menos tecnología de la que imagina quien llega desde un puesto técnico, y esa es la principal
causa de frustración de quien asciende. La compensación es que las decisiones que tomas cambian la
exposición real de miles de personas.

## 🧠 Qué necesitas saber

### Conocimiento técnico

Un CISO que no entiende lo que gobierna acaba **gestionado por su propio equipo y por sus
proveedores**: firma arquitecturas que no comprende y compra soluciones que no necesita.

- **Gobierno y marcos:** **ISO/IEC 27001** (montar y sostener un SGSI, no solo aprobar la
  auditoría), **NIST CSF**, **controles CIS** y la normativa sectorial aplicable.
- **Riesgo:** metodología cualitativa y **cuantitativa** (FAIR), apetito y tolerancia, tratamiento
  —mitigar, transferir, evitar, aceptar— y **transferencia real** vía seguro cibernético.
- **Arquitectura de seguridad:** segmentación, **zero trust**, identidad como perímetro, gestión de
  accesos privilegiados, cifrado y gestión de claves. Lo suficiente para revisar un diseño y
  encontrar el hueco, no para implementarlo.
- **Operación que supervisas:** qué puede y qué no puede darte un **SIEM**, cómo se mide la madurez
  de la detección, qué es un programa de vulnerabilidades (cobertura, SLA por criticidad,
  priorización por exposición real) y cómo se sostiene la respuesta a incidentes.
- **Resiliencia:** BIA, RTO/RPO, plan de continuidad y recuperación, y la disciplina de **probarlos**.
  Ante ransomware, la copia verificada vale más que cualquier producto del catálogo.
- **Nube y desarrollo:** modelo de responsabilidad compartida, postura de nube, y seguridad dentro
  del SDLC. Buena parte de los servicios digitales que proteges ya no están en tu centro de datos.
- **Terceros y cadena de suministro:** evaluación, cláusulas contractuales, dependencias críticas y
  planes de salida. El riesgo que más crece es el que no está en tu red.
- **Privacidad y legal:** protección de datos personales, plazos de notificación de brechas,
  retención y evidencia. Aquí se trabaja **pegado a legal**, no en paralelo.
- **IA:** gobierno del uso de IA en la organización y de los datos que se le entregan. Es la
  superficie que más rápido está creciendo y la que más rápido llega al comité.

### Herramientas del oficio

```text
Marcos:        ISO/IEC 27001 + 27002, NIST CSF, CIS Controls, normativa sectorial
Riesgo:        registro de riesgos, matrices, FAIR, apetito y aceptaciones firmadas
Resiliencia:   BIA, RTO/RPO, plan de continuidad, pruebas de restauración
Operación:     SIEM, EDR, gestión de vulnerabilidades (Nessus/Qualys/Tenable), WAF
Terceros:      cuestionarios, cláusulas contractuales, mapa de dependencias críticas
Gestión:       presupuesto, plan director, roadmap, KPIs/KRIs, informe a directorio
Ofimática:     Excel y presentaciones — el registro de riesgos y el reporte viven ahí
```

### Habilidades no técnicas

Es donde se decide de verdad si sirves para el cargo:

- **Comunicación con el directorio.** Traducir exposición técnica a **riesgo, dinero y
  cumplimiento**, en quince minutos y sin jerga. La primera causa de fracaso de un buen técnico
  ascendido.
- **Criterio económico.** Priorizar con presupuesto finito y saber decir "este riesgo no lo
  tratamos, cuesta más el control que el daño esperado" — con el número delante.
- **Influencia sin autoridad.** Conseguir que áreas que no te reportan cierren hallazgos, con datos
  y alianzas en lugar de con correos escalados.
- **Liderazgo.** Contratar en un mercado escaso, retener, desarrollar y **proteger** al equipo
  cuando la presión aprieta.
- **Temple en crisis.** Cuando todo el mundo mira el mismo problema, alguien tiene que decidir con
  información incompleta y sostener la decisión después.
- **Trato con reguladores y auditores.** Con un regulador, **lo que no se puede demostrar no
  existe**: registro escrito, medible y trazable.
- **Ética.** Vas a saber cosas incómodas de la organización. Cómo las reportas define tu carrera más
  que cualquier certificación.

## 🧾 Los entregables que firma un CISO

Si quieres demostrar el cargo en una entrevista, **no lleves un writeup de CTF: lleva estos
documentos** construidos sobre una organización ficticia. Son el producto real del puesto:

1. **Política general de seguridad de la información** — aprobada por el órgano de gobierno · clase [282](../classes/parte-14-grc-riesgo-y-cumplimiento/282-politicas-estandares-y-procedimientos/README.md)
2. **Plan director de seguridad** a 2–3 años con presupuesto e hitos · clases [276](../classes/parte-14-grc-riesgo-y-cumplimiento/276-gobernanza-de-la-seguridad-de-la-informacion/README.md) y [320](../classes/parte-17-profundizacion-para-certificaciones/320-gobierno-aspectos-legales-regulatorios-y-gestion-del-programa/README.md)
3. **Registro de riesgos** con propietario, tratamiento y **aceptaciones firmadas** · clases [277](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md) y [328](../classes/parte-17-profundizacion-para-certificaciones/328-gestion-de-riesgos-cuantitativa-y-continuidad-avanzada/README.md)
4. **Declaración de aplicabilidad (SoA)** de ISO 27001 y el perfil **NIST CSF** actual vs objetivo · clases [278](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md) y [279](../classes/parte-14-grc-riesgo-y-cumplimiento/279-nist-cybersecurity-framework/README.md)
5. **BIA + plan de continuidad y recuperación** con RTO/RPO acordados con el negocio · clase [283](../classes/parte-14-grc-riesgo-y-cumplimiento/283-continuidad-de-negocio-y-plan-de-recuperacion-ante-desastres/README.md)
6. **Plan de respuesta a incidentes** con matriz de escalamiento y guion de comunicación · clases [202](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/202-el-ciclo-de-respuesta-a-incidentes-nist-y-sans/README.md) y [215](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/215-playbooks-de-respuesta-a-incidentes/README.md)
7. **Programa de gestión de vulnerabilidades** con SLA por criticidad y métricas de cierre · clase [318](../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md)
8. **Marco de gestión de terceros**: criticidad, cuestionario, cláusulas y plan de salida · clase [284](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md)
9. **Programa anual de concienciación** con métricas de resultado, no de asistencia · clase [286](../classes/parte-14-grc-riesgo-y-cumplimiento/286-concienciacion-y-cultura-de-seguridad/README.md)
10. **Informe ejecutivo mensual de una página** con KPIs/KRIs · clases [287](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md) y [321](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md)

## 📚 Tu ruta en el programa

**Este cargo no se estudia desde cero.** Se llega con recorrido previo —normalmente desde
[jefe de seguridad](ciso-jefe-seguridad.md), [GRC](grc.md), [SOC](soc-blue-team.md), infraestructura
o arquitectura—. Si vienes de cero, haz primero una de esas rutas: aquí se estudia **la capa de
dirección**, no la base.

1. 📚 [**Parte 0 — Fundamentos**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md)
   · **002** (panorama de amenazas: quién te ataca y por qué), **003** (NIST/ISO/MITRE) y **025**
   (ética y legalidad).
2. 📚 [**Parte 14 — GRC, riesgo y cumplimiento**](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md)
   (276–290) · **el núcleo del cargo, entera y sin recortes**.
3. 📚 [**Parte 17 — Profundización**](../classes/parte-17-profundizacion-para-certificaciones/README.md)
   · **320** gobierno y regulación · **328** riesgo cuantitativo y continuidad avanzada · **329**
   arquitectura empresarial y zero trust · **316** modelos de seguridad · **313**/**315** identidad y
   PAM · **318** programa de vulnerabilidades · **324** hardening · **321** comunicación y reporte.
4. 📚 [**Parte 8 — Blue Team y SOC**](../classes/parte-8-blue-team-deteccion-y-soc/README.md)
   · **181** (cómo se organiza un SOC), **183** (qué es y qué no un SIEM), **195** (inteligencia de
   amenazas) y **197** (métricas y madurez): supervisar la operación sin operarla.
5. 📚 [**Parte 9 — DFIR**](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/README.md)
   · **202** (ciclo de respuesta), **215** (playbooks) y **219** (ejercicios de mesa): la crisis que
   vas a dirigir.
6. 📚 [**Partes 10 y 11 — Nube y DevSecOps**](../classes/parte-10-seguridad-en-la-nube-y-contenedores/README.md)
   · **221** responsabilidad compartida · **234** logging y detección en la nube · **236** secure
   SDLC · **245** vulnerabilidades a escala · **248** cultura DevSecOps: dónde viven hoy tus
   servicios digitales.
7. 📚 [**Parte 15 — Seguridad de IA**](../classes/parte-15-seguridad-de-ia-y-machine-learning/README.md)
   · **291** y **300** (gobernanza y ética de la IA): el punto de agenda que ya te están pidiendo.
8. 📚 [**Partes 1, 3 y 4**](../classes/parte-1-redes-y-seguridad-de-redes/README.md) · la base
   técnica que gobiernas: **034** firewalls, **042** segmentación y zero trust, **071** Nessus y
   **087** OWASP Top 10 (el porqué del WAF).

Clases concretas por las que empezar:

- 🏛️ [276 · Gobernanza de la seguridad de la información](../classes/parte-14-grc-riesgo-y-cumplimiento/276-gobernanza-de-la-seguridad-de-la-informacion/README.md) — el mandato: quién decide qué, y de dónde sale tu autoridad.
- ⚖️ [320 · Gobierno, aspectos legales, regulatorios y gestión del programa](../classes/parte-17-profundizacion-para-certificaciones/320-gobierno-aspectos-legales-regulatorios-y-gestion-del-programa/README.md) — regulador, auditoría externa y responsabilidad legal del cargo.
- 📊 [277 · Gestión de riesgos cuantitativa y cualitativa](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md) y [328 · Riesgo cuantitativo y continuidad avanzada](../classes/parte-17-profundizacion-para-certificaciones/328-gestion-de-riesgos-cuantitativa-y-continuidad-avanzada/README.md) — el idioma con el que se pide presupuesto.
- 📕 [278 · ISO/IEC 27001 e implantación de un SGSI](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md), [279 · NIST CSF](../classes/parte-14-grc-riesgo-y-cumplimiento/279-nist-cybersecurity-framework/README.md) y [280 · Controles CIS](../classes/parte-14-grc-riesgo-y-cumplimiento/280-controles-cis/README.md) — el sistema de gestión y los controles que lo materializan.
- 🔁 [283 · Continuidad de negocio y recuperación ante desastres](../classes/parte-14-grc-riesgo-y-cumplimiento/283-continuidad-de-negocio-y-plan-de-recuperacion-ante-desastres/README.md) — la **continuidad operacional**, que es media definición del cargo.
- 🗄️ [311 · Clasificación y ciclo de vida de los datos](../classes/parte-17-profundizacion-para-certificaciones/311-clasificacion-y-ciclo-de-vida-de-los-datos/README.md), [312 · Retención, destrucción segura y DLP](../classes/parte-17-profundizacion-para-certificaciones/312-retencion-destruccion-segura-de-datos-y-dlp/README.md) y [289 · Privacidad y protección de datos](../classes/parte-14-grc-riesgo-y-cumplimiento/289-privacidad-y-proteccion-de-datos/README.md) — la protección **del dato**, con su capa legal.
- 🏗️ [329 · Arquitectura de seguridad empresarial y zero trust](../classes/parte-17-profundizacion-para-certificaciones/329-arquitectura-de-seguridad-empresarial-y-zero-trust/README.md) y [316 · Modelos de seguridad y arquitectura](../classes/parte-17-profundizacion-para-certificaciones/316-modelos-de-seguridad-y-arquitectura/README.md) — la foto de a dónde llevas la organización.
- 🤝 [284 · Riesgo de terceros y proveedores](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md) y [288 · Seguros cibernéticos](../classes/parte-14-grc-riesgo-y-cumplimiento/288-seguros-ciberneticos/README.md) — transferir riesgo, no solo mitigarlo.
- 📈 [287 · Métricas de seguridad: KPIs y KRIs](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md) y [321 · Comunicación y reporte](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md) — tu producto más visible.
- 🎲 [219 · Ejercicios de mesa (tabletop)](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md) y [202 · Ciclo de respuesta a incidentes](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/202-el-ciclo-de-respuesta-a-incidentes-nist-y-sans/README.md) — la crisis, ensayada antes de que ocurra.
- 🤖 [300 · Gobernanza y ética de la IA segura](../classes/parte-15-seguridad-de-ia-y-machine-learning/300-gobernanza-y-etica-de-la-ia-segura/README.md) — la política de uso de IA que te van a pedir este año.

### Laboratorio y práctica

La práctica de este cargo **no es un laboratorio de hacking**, y conviene decirlo sin rodeos:

- 🎲 [219 · Ejercicios de mesa](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md) — **tu ejercicio principal**: dirige una crisis simulada con roles, reloj y comunicación a dirección. Es lo más parecido al trabajo real que hay en el programa.
- 📋 **Construye los diez entregables** de la sección anterior sobre una organización ficticia. En una entrevista de CISO pesan más que cualquier certificación.
- 💰 **Haz el ejercicio del presupuesto:** defiende una inversión de seguridad con riesgo cuantificado —pérdida esperada con y sin control, coste del control— ante alguien que no es técnico. Si no consigues la decisión, el problema no fue del oyente.
- 🧪 [`blue-team-soc`](../labs/blue-team-soc/README.md) y [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md) — para **no perder el contacto técnico**: el día que dejas de entender lo que hace tu equipo, empiezas a decidir a ciegas y a comprar humo.
- ☁️ [`cloud-security`](../labs/cloud-security/README.md) — el tipo de informe de postura que vas a revisar y cuestionar cada trimestre.
- 🎩 **[`labs/ciso-leadership`](../labs/ciso-leadership/README.md) — el laboratorio ejecutivo del programa.** Catorce escenarios sobre organizaciones ficticias con plantillas y rúbricas; los siete primeros son de este cargo: informe al directorio, registro de riesgos con aceptaciones firmadas, plan director, defensa de presupuesto, ejercicio de mesa, proveedor crítico y plan de 90 días. Trae además las [quince plantillas](../labs/ciso-leadership/PLANTILLAS.md) que producen los diez entregables de la sección anterior.

## 🗓️ Tus primeros 30, 60 y 90 días

Es la pregunta clásica de la entrevista, y también un buen plan de estudio. La
[plantilla completa](../labs/ciso-leadership/PLANTILLAS.md#6--plan-de-306090-días) está en el
laboratorio ejecutivo, y el [escenario 7](../labs/ciso-leadership/README.md#7--plan-de-90-días) te
hace construirla sobre una organización ficticia:

- **Días 1–30 · Entender y escuchar.** Reuniones con negocio, TI, legal, riesgo y auditoría. Qué
  procesos son críticos, qué datos existen, qué incidentes hubo, qué hallazgos de auditoría siguen
  abiertos, qué contratos aprietan. **No prometas nada todavía.**
- **Días 31–60 · Medir y priorizar.** Evaluación honesta contra un marco (NIST CSF o ISO 27001):
  dónde está la organización y dónde debería estar. Registro de riesgos inicial con los 10 riesgos
  que de verdad importan, con dueño y cifra.
- **Días 61–90 · Proponer y comprometerse.** Plan director con presupuesto e hitos, política
  general para aprobación, gobierno del comité de seguridad y las **primeras dos o tres victorias
  rápidas** que demuestren que el área entrega (MFA donde falta, copias verificadas, un hallazgo
  crítico cerrado).

Un error frecuente en esa ventana: llegar anunciando la compra de una plataforma. Lo que da
credibilidad no es el producto, es el diagnóstico.

Y un criterio de cierre que conviene fijarse antes de empezar: **el día 90 debe terminar con una
decisión pedida a la dirección**, no con un informe. Un plan de 90 días que acaba en diagnóstico ha
producido conocimiento, pero no ha conseguido mandato — y sin mandato el año siguiente será una
sucesión de recomendaciones sin dueño.

## 📏 Cómo se te mide

Ninguna organización seria mide a su CISO por "número de ataques bloqueados". Los indicadores que
sí sostienen una conversación de directorio:

| Indicador | Qué dice |
|---|---|
| Riesgos críticos abiertos y su **antigüedad** | Si el programa reduce exposición o solo la documenta |
| **Tiempo medio de remediación** por criticidad vs SLA | Si la organización sabe arreglar lo que encuentra |
| Cobertura real de controles (EDR, MFA, parches, copias) | Cuánto del parque está de verdad protegido |
| **MTTD / MTTR** de incidentes | Si la detección y la respuesta funcionan |
| **Prueba de restauración** superada y RTO real vs comprometido | Si la continuidad es real o es un documento |
| Hallazgos de auditoría cerrados en plazo | Salud regulatoria |
| Riesgo de terceros críticos evaluado | Dónde está el riesgo que no controlas |
| Presupuesto ejecutado vs plan | Si sabes gestionar recursos |

## 🎓 Certificaciones

En este cargo la certificación es **credencial de credibilidad** ante comités de selección,
auditores, reguladores y aseguradoras. No sustituyen la experiencia, pero sin ellas hay puertas
que no se abren.

Con archivo en el programa:

- 🏛️ [**CISSP**](../certificaciones/cissp.md) — la certificación faro: gobernanza, riesgo,
  arquitectura y gestión de la seguridad como disciplina de organización. Exige 5 años acreditados
  (4 con titulación); es un sello de seniority, no solo de conocimiento.
- 📋 [**CompTIA CySA+**](../certificaciones/comptia-cysa-plus-cs0-003.md) y
  [**Security+**](../certificaciones/comptia-security-plus-sy0-701.md) — la base técnica. Si llegas
  desde gestión pura y te falta músculo de detección y vulnerabilidades, cubren ese hueco.

Fuera del programa, y decisivas para este cargo: **CISM** (ISACA), que probablemente sea la que
mejor describe el puesto; **ISO 27001 Lead Implementer / Lead Auditor**, estándar de facto donde hay
SGSI certificado; **CRISC** si el peso se inclina a riesgo; y **CCISO** (EC-Council) como opción
específica de dirección. El programa cubre **el contenido** de ISO 27001 en la
[clase 278](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md)
y la preparación de CISSP en la
[clase 304](../classes/parte-16-capstones-y-preparacion-de-certificaciones/304-preparacion-cissp-los-8-dominios/README.md),
pero no los exámenes. Ver el [mapeo completo](../certificaciones/README.md) y la
[clase 290](../classes/parte-14-grc-riesgo-y-cumplimiento/290-certificaciones-y-desarrollo-de-carrera/README.md).

## 📈 Progresión de carrera y salario

Se llega por dos vías, y las dos funcionan: **la técnica** (analista → especialista → jefe de
seguridad → CISO), que aporta credibilidad ante el equipo y suele flojear en la sala de juntas; y
**la de gestión** (auditoría, riesgo operacional, [GRC](grc.md), consultoría), que aporta el idioma
del directorio y tiene que ganarse el respeto técnico. Quien combina ambas es quien se queda con el
puesto.

Hacia arriba y hacia los lados: **CISO → CISO de grupo → Director de Riesgo Tecnológico / CRO**, o
salida a **consultoría estratégica, asesoría de directorios (board advisor), CISO fraccional** para
varias empresas medianas, o **vCISO** en una firma de servicios. El CISO fraccional es hoy una de
las salidas mejor pagadas por hora y una vía realista tras el primer cargo corporativo.

Rangos **orientativos y aproximados** (brutos anuales; varían enormemente por tamaño, sector y
línea de reporte — referencia, no promesa):

```text
Región                      CISO (mediana empresa)   CISO corporativo / de grupo
--------------------------  -----------------------  ---------------------------
LATAM                       USD 60k – 110k / año     USD 110k – 200k+ / año
Chile (financiero/regulado) USD 70k – 130k / año     USD 130k – 220k+ / año
España                      EUR 70k – 110k / año     EUR 110k – 180k+ / año
Remoto / EE. UU. (USD)      USD 150k – 250k / año    USD 250k – 450k+ / año
```

Tres factores mueven el número más que el título: **a quién reportas** (directorio o CIO), **el
sector** (regulado paga más y exige más) y **si hay presupuesto y equipo propios** o el cargo es
nominal. Pregúntalo en la entrevista: define el puesto entero.

## ⚠️ Mitos y errores comunes

- **"El CISO evita los hackeos."** No: **gestiona el riesgo de que ocurran y su impacto cuando
  ocurran**. Prometer que no habrá incidentes es la forma más rápida de perder el cargo con el
  primero.
- **"El CISO decide la seguridad de la empresa."** La **propone**. Quien acepta el riesgo residual
  es el negocio, **por escrito**. Sin esa firma acabas respondiendo por decisiones que no tomaste.
- **"Es un puesto de TI."** Si depende de TI y solo mira TI, deja fuera personas, procesos,
  proveedores, legal y continuidad — que es donde se materializan la mayoría de los incidentes
  caros.
- **"Cumplir la norma es estar seguro."** ISO 27001 certifica que tienes un sistema de gestión, no
  que no te van a entrar. Y al revés: estar razonablemente seguro sin evidencia no te salva del
  regulador.
- **"Ya no necesito saber de tecnología."** El error caro del otro lado. Si no entiendes qué puede
  darte un SIEM o qué no cubre un WAF, firmas arquitecturas y contratos a ciegas.
- **"Con más herramientas estaré más seguro."** La mayoría de las organizaciones tienen más
  productos de los que saben operar. La madurez está en los procesos, no en el catálogo.
- **"Si hay brecha, me despiden."** No necesariamente. Lo que hunde a un CISO no es el incidente:
  es **no poder demostrar** que había un programa razonable, riesgos documentados y decisiones
  trazables. La trazabilidad es tu red de seguridad — y a veces tu defensa legal.
- **"El curso me convierte en CISO."** No. Aquí menos que en ninguna otra ruta.

> **Honestidad, sin marketing:** este programa te da **el cuerpo de conocimiento** del cargo —ISO
> 27001, NIST CSF, controles CIS, riesgo cuantitativo y cualitativo, continuidad, privacidad,
> terceros, arquitectura, programa de vulnerabilidades, SOC, respuesta a incidentes, nube,
> DevSecOps, IA, métricas y reporte—. Lo que **no** te da, y es exactamente lo que se evalúa para
> este puesto: los **años de trayectoria** y el historial de haber sostenido decisiones; la
> experiencia real **defendiendo un presupuesto** y un número incómodo ante un directorio; el trato
> con **reguladores, auditores y aseguradoras**; el **inglés** de negocio; la red de contactos del
> sector; y el temple que solo da haber gestionado una crisis de verdad. Nada de eso se aprende
> leyendo. El curso te hace **técnicamente creíble y normativamente solvente**; el mandato, la sala
> de juntas y las cicatrices los pones tú.

## 🚀 Siguientes pasos

1. **Ten recorrido antes del título.** Si no vienes de un rol de seguridad con responsabilidad, haz
   antes [jefe de seguridad](ciso-jefe-seguridad.md), [GRC](grc.md) o [SOC](soc-blue-team.md). Este
   cargo no se ocupa desde cero, y el equipo lo detecta la primera semana.
2. **Haz la Parte 14 completa.** Es el núcleo del puesto y la única parte del programa que aquí no
   puedes recortar.
3. **Añade la capa de dirección con la Parte 17:** gobierno y regulación (**320**), riesgo
   cuantitativo (**328**), arquitectura empresarial (**329**), datos (**311**, **312**) e identidad
   (**313**, **315**).
4. **Construye los diez entregables** sobre una organización ficticia y llévalos a la entrevista.
   Demuestran el cargo mejor que cualquier examen.
5. **Ensaya la crisis.** Dirige un [tabletop](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md)
   con gente real y cronómetro. Anota qué decisiones te costaron y por qué.
6. **Practica la conversación de presupuesto.** Cinco minutos, un riesgo, una cifra, una decisión
   pedida. Si tu interlocutor no sabe qué tiene que decidir al terminar, repítelo.
7. **Planifica CISSP y CISM**, e **ISO 27001 Lead Implementer** si tu organización va hacia un SGSI
   certificado. Y rinde el [examen final de este rol](../docs/examen-final-por-rol.md).
8. **Sitúate en el ecosistema.** Antes de aceptar cualquier cargo con «CISO» en el nombre, lee
   [El ecosistema CISO](ecosistema-ciso.md) y aplícale el
   [test del mandato](ecosistema-ciso.md#-el-test-del-mandato-cómo-comprobar-un-cargo-real). Después
   resuelve la [evaluación del ecosistema](../labs/ciso-leadership/EVALUACION.md): comprueba que
   distingues quién decide, quién asesora y quién responde.

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🗂️ **[El ecosistema CISO](ecosistema-ciso.md)** — mapa de cargos, matriz comparativa y test del mandato
- 👔 [Ruta vecina: Jefe de Seguridad de la Información](ciso-jefe-seguridad.md) · 🏛️ [GRC / Gestión de seguridad](grc.md)
- 🛰️ [Field CISO](field-ciso.md) · 🧾 [vCISO](vciso.md) · 🔗 [BISO](biso.md) · 📦 [Product CISO](product-ciso.md) · 🤖 [AI CISO](ai-ciso.md) · 🏭 [OT CISO](ot-ciso.md)
- 🧪 [Laboratorio ejecutivo CISO](../labs/ciso-leadership/README.md)
- 🏠 [Inicio del programa](../README.md)
