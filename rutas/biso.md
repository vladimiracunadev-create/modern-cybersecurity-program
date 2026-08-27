# 🔗 BISO / Business Information Security Officer

> El **traductor bidireccional** entre una unidad de negocio y el programa central de seguridad.
> Se sienta en la mesa donde se decide el producto, la campaña o la fusión, y lleva allí el riesgo
> de seguridad en el idioma en que esa mesa toma decisiones; después vuelve al programa central con
> lo que esa unidad necesita de verdad. **No es un CISO pequeño: es el enlace que hace que el
> programa del CISO ocurra donde se gana el dinero.**
>
> **Nivel de entrada:** ninguno; es un cargo intermedio-senior · **Foco:** contexto de negocio,
> priorización, traducción de riesgo y ejecución dentro de una unidad · **Certificación faro:**
> CISM (gestión) o CISSP, según de dónde vengas

**Alias y variantes:** *BISO*, *Business Information Security Officer*, *Business Unit Security
Officer*, *Divisional Security Officer*, *Security Business Partner*, *Embedded Security Lead*.
Algunas organizaciones lo llaman *Divisional CISO*; si la persona tiene presupuesto propio y
responde ante la dirección de esa división, entonces es un
[Divisional CISO de verdad](ecosistema-ciso.md#a-dirección-interna-y-jerarquía) y no un BISO.

**Fecha de consulta de las fuentes: 26 de agosto de 2026.**

## 🧭 Qué es y por qué importa

### Definición

Un BISO es un **profesional de seguridad asignado a una unidad de negocio concreta** —banca
minorista, seguros de vida, una línea de producto, una región comercial, una filial— cuyo trabajo
es que la seguridad de esa unidad sea coherente con el programa corporativo **y** viable dentro de
su realidad. Suele reportar al [CISO](ciso.md) (línea sólida) y trabajar día a día con la
dirección de su unidad (línea punteada), o al revés.

### El problema que resuelve

El programa central de seguridad falla siempre por el mismo sitio: **se escribe lejos de donde se
ejecuta**. Una política corporativa que en la casa matriz es razonable puede ser inaplicable en la
unidad que vende por terreno con tablets sin conexión. Y a la inversa: la unidad toma decisiones
—lanzar un producto, integrar a un socio, abrir una API— sin saber qué riesgo está creando para
todo el grupo.

| Sin BISO | Con BISO |
|---|---|
| La política llega por correo y nadie la aplica | La política llega con el «cómo» adaptado a esa unidad |
| Seguridad se entera del proyecto cuando ya está en producción | Seguridad está en la reunión de definición |
| La unidad pide excepciones permanentes | La unidad pide excepciones **con vencimiento y compensación** |
| El riesgo se reporta en jerga técnica y la dirección lo ignora | El riesgo se reporta en pérdida potencial, cliente afectado y plazo |
| El CISO no sabe qué le duele a cada unidad | El CISO prioriza el presupuesto con información real |

### Nivel de consolidación del título

**Especialización con práctica establecida**, sobre todo en banca, seguros, salud y grandes
tecnológicas. El acrónimo es reconocible y el contenido del puesto es razonablemente consistente
entre organizaciones. Lo que varía —y mucho— es **la línea de reporte** y si tiene o no
presupuesto: eso convierte el mismo título en dos trabajos distintos.

### Qué hace y qué no hace

| Sí hace | No hace |
|---|---|
| Traducir el riesgo técnico a impacto de negocio para su unidad | Definir la política corporativa (eso es del programa central) |
| Traducir la realidad de la unidad al programa central | Operar controles: no es SOC, ni SecOps, ni administrador |
| Priorizar qué se remedia primero **dentro** de su unidad | Aceptar el riesgo residual: lo acepta la dirección de la unidad |
| Acompañar proyectos desde el inicio | Ser la firma que desbloquea el proyecto sin condiciones |
| Gestionar el registro de riesgos de la unidad | Sustituir al equipo de gestión de riesgos corporativo |
| Preparar a su unidad para auditorías | Auditar: no puede revisar con independencia lo que ayudó a construir |
| Negociar excepciones razonables con vencimiento | Repartir excepciones indefinidas para evitar conflicto |
| Dirigir la parte de negocio de un incidente que afecta a su unidad | Dirigir la respuesta técnica |

### Dónde existe

Organizaciones grandes con **unidades de negocio diferenciadas** y suficiente autonomía: banca y
seguros, grupos industriales, retail multiformato, telecomunicaciones, salud privada con varias
clínicas, tecnológicas con líneas de producto separadas. En una empresa de doscientas personas no
tiene sentido: ahí la figura es el
[Jefe de Seguridad de la Información](ciso-jefe-seguridad.md).

## 🏛️ Mandato, autoridad y responsabilidad

### Línea de reporte

Tres modelos, cada uno con su patología:

| Modelo | Cómo funciona | Fortaleza | Patología |
|---|---|---|---|
| **Reporte sólido al CISO**, punteado al negocio | El BISO forma parte del equipo de seguridad y está desplegado en la unidad | Coherencia del programa, independencia de criterio | Puede ser visto como «el fiscalizador» y quedar fuera de las decisiones |
| **Reporte sólido al negocio**, punteado al CISO | El BISO es de la unidad y la seguridad es su especialidad | Acceso total al negocio y credibilidad interna | **Captura**: acaba defendiendo a su unidad frente al programa |
| **Doble reporte real** | Objetivos y evaluación compartidos entre ambos | El equilibrio correcto | Exige que CISO y dirección de la unidad se hablen; si no, el BISO queda partido |

Pregunta esto en la entrevista: **«¿Quién escribe mi evaluación de desempeño y con qué
objetivos?»** La respuesta define el cargo mejor que la descripción del puesto.

### Autoridad, presupuesto y riesgo

- **Autoridad:** alta influencia, decisión limitada. Puede exigir que un riesgo se registre, que
  una excepción tenga fecha y que la dirección firme; rara vez puede detener un proyecto por sí
  mismo, aunque sí puede **escalar** para que lo detenga quien corresponde.
- **Presupuesto:** rara vez propio. A veces gestiona una partida de seguridad dentro del
  presupuesto de la unidad.
- **Equipo:** pequeño o ninguno. Su palanca es la red de personas de la unidad, no la jerarquía.
- **Riesgo:** **no lo acepta**. Lo identifica, lo cuantifica, propone tratamiento y consigue que la
  dirección de la unidad firme la aceptación cuando decide no tratarlo.

> 🎯 **La palanca real del BISO.** No es la autoridad: es **estar antes**. Un BISO que se entera de
> los proyectos en el comité de arquitectura ya llegó tarde. El puesto se gana entrando en la
> reunión donde la unidad decide qué va a hacer, y para eso hay que aportar algo distinto de una
> lista de controles.

### Conflictos de interés y límites éticos

| Situación | Riesgo | Cómo se maneja |
|---|---|---|
| Tu bono depende de los resultados de la unidad | Te incentiva a minimizar riesgos | Que parte de tus objetivos los fije el CISO, y que se documente |
| La unidad te pide firmar una excepción indefinida | Convierte una excepción en política de facto | Toda excepción con fecha, control compensatorio y dueño que la firma |
| Te piden que no escales un hallazgo «para no alarmar» | Ocultación | Escalar es tu obligación; lo que se negocia es el tono, no el hecho |
| Te piden auditar lo que tú ayudaste a diseñar | No hay independencia | Derivar a auditoría interna o a un tercero |
| La unidad y el programa central tienen criterios contradictorios | Parálisis o arbitrariedad | Levantar la contradicción por escrito y forzar la decisión arriba; no resolverla en silencio |
| Conoces una brecha que afecta a otra unidad | Compartimentación mal entendida | El programa central debe saberlo: tu lealtad de fondo es a la organización |

## 🗓️ El día, el mes y el año

**Un día típico.** Comité de producto de la unidad (donde tu papel es hacer las tres preguntas
correctas, no leer una política); revisión con el equipo de proyecto de una integración con un
socio externo; media hora traduciendo un hallazgo del escáner al lenguaje de «cuántos clientes y
cuánto dinero»; llamada con el programa central para negociar el plazo de un control que en tu
unidad no cabe en el trimestre.

**Un mes típico.** Actualización del registro de riesgos de la unidad; revisión de excepciones que
vencen; una evaluación de un tercero que tu unidad quiere contratar; el informe mensual a la
dirección de la unidad y al CISO; una sesión de sensibilización con un equipo concreto, no un
correo masivo.

**Un año típico.** El ciclo de planificación de la unidad, donde peleas el presupuesto de
seguridad **dentro** de su plan, no fuera; una auditoría; al menos un ejercicio de mesa con la
dirección de tu unidad; la revisión anual del riesgo y de la tolerancia; y la conversación difícil:
qué riesgo va a aceptar tu unidad este año, quién lo firma y hasta cuándo.

### Interlocutores

| Dentro de tu unidad | Fuera de tu unidad |
|---|---|
| Dirección de la unidad y su comité | El [CISO](ciso.md) y su equipo de programa |
| Producto, comercial, operaciones | Arquitectura y [SOC](soc-blue-team.md) corporativos |
| Tecnología de la unidad | Riesgo operacional y auditoría interna |
| Legal y cumplimiento de la unidad | El [DPO](ecosistema-ciso.md#d-cargos-vecinos-que-no-son-tipos-de-ciso) |
| Los responsables de proceso que firman riesgos | Otros BISO: la red horizontal es la mitad del trabajo |

## 🧾 Entregables verificables

| Entregable | Qué demuestra | Cómo se verifica |
|---|---|---|
| **Registro de riesgos de la unidad** | Que el riesgo está identificado y tiene dueño **del negocio** | Cada riesgo con dueño nominal, tratamiento, plazo y residual |
| **Roadmap de seguridad de la unidad** | Que hay un plan que la unidad reconoce como suyo | Priorizado, costeado y aprobado por la dirección de la unidad |
| **Traducción de riesgo a negocio** | La competencia central del puesto | Un director no técnico entiende el impacto y la decisión |
| **Registro de excepciones** | Que las desviaciones están controladas | Todas con vencimiento, compensación y firma |
| **Actas de aceptación de riesgo** | Que la responsabilidad quedó donde debe | Firmadas por la dirección de la unidad, con vigencia |
| **Evaluaciones de terceros de la unidad** | Control del riesgo que entra por contrato | Con criticidad, hallazgos y cláusulas exigidas |
| **Informe mensual doble** (unidad y CISO) | Que ambas mesas ven lo mismo | Mismos datos, dos lenguajes |
| **Aportación al plan corporativo** | Que la traducción va en los dos sentidos | Necesidades de la unidad reflejadas en el plan del CISO |

## 📏 KPI y KRI

| Indicador | Tipo | Qué dice |
|---|---|---|
| Proyectos de la unidad con seguridad **desde el diseño** | KPI | Si llegas a tiempo o siempre tarde |
| Riesgos de la unidad con dueño de negocio asignado | KPI | Si la responsabilidad está donde corresponde |
| Tiempo medio de remediación por criticidad frente al SLA corporativo | KPI | Capacidad de ejecución de la unidad |
| Cobertura de controles corporativos en la unidad | KPI | Alineamiento con el programa |
| Excepciones **vigentes y dentro de plazo** | KPI | Gestión sana de las desviaciones |
| Terceros críticos de la unidad evaluados | KPI | Riesgo que entra por contrato |
| **Excepciones vencidas y no renovadas ni cerradas** | **KRI** | La deuda de seguridad que la unidad acumula |
| **Riesgos que aceptaste tú en lugar del negocio** | **KRI** | Fallo estructural del puesto |
| Proyectos que llegaron a producción sin revisión | **KRI** | Estás fuera de la mesa donde se decide |
| Hallazgos repetidos entre auditorías | **KRI** | Se remedia el síntoma, no la causa |
| Divergencia entre lo que informas a la unidad y al CISO | **KRI** | Estás capturado por una de las dos partes |

## 🧠 Qué necesitas saber

### Competencias técnicas

No necesitas ser el más profundo del equipo de seguridad; necesitas **entender lo suficiente para
no ser engañable en ninguna de las dos direcciones**: ni por un proveedor que exagera, ni por un
equipo de producto que minimiza.

- Gestión de riesgos y su cuantificación, para poder poner un número al lado de la conversación.
- Los controles del programa corporativo: identidad, datos, endpoint, red, nube, SDLC. Qué
  protegen y qué cuestan de implantar.
- Gestión de vulnerabilidades y su priorización real, no solo por CVSS.
- Riesgo de terceros: en una unidad de negocio, gran parte del riesgo entra por un contrato.
- Respuesta a incidentes: lo suficiente para dirigir la parte de negocio de una crisis.
- El dominio técnico específico de tu unidad: si vende software, el SDLC; si opera una planta,
  [OT](ot-ciso.md); si mueve datos personales a escala, privacidad.

### Competencias de negocio

Es la mitad del puesto y la que decide si te invitan a las reuniones:

- Conocer el **modelo de negocio de tu unidad**: de dónde viene el ingreso, cuál es su margen, cuál
  es su temporada crítica, qué proyecto se juega el año.
- Leer un caso de negocio y saber dónde está el riesgo que nadie miró.
- Hablar de coste de oportunidad: un control que retrasa un lanzamiento tiene un precio, y hay que
  ponerlo sobre la mesa en lugar de fingir que es gratis.
- Entender los indicadores con los que se mide a la dirección de tu unidad y conectar los tuyos a
  ellos.

### Comunicación y negociación

- **Traducir en los dos sentidos**, que es más difícil que en uno solo.
- Decir «no» de forma que el proyecto siga avanzando con otra opción.
- Negociar plazos con el programa central sin convertirte en el abogado defensor de tu unidad.
- Escalar sin quemar la relación: hacerlo temprano, por escrito y avisando antes.
- Construir una red de aliados en la unidad: sin ella no tienes poder, porque no tienes jerarquía.

### Competencias regulatorias

Las que apliquen **a tu unidad**, que a menudo no son las mismas que a las demás: una filial
financiera dentro de un grupo industrial arrastra la normativa de su regulador. Debes saber qué
obligaciones tiene tu unidad, qué evidencia produce y quién la firma. Ver el
[contexto chileno del ecosistema](ecosistema-ciso.md#-contexto-chileno-y-latinoamericano).

### Componente comercial

Ninguno hacia fuera. **Sí hay un componente comercial interno**: tienes que «vender» la seguridad
dentro de tu unidad todos los días, sin autoridad, compitiendo por presupuesto con proyectos que
generan ingresos. Ese es, en la práctica, el oficio.

## 📚 Tu ruta en el programa

1. **Fundamentos** — [**001**](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md) · [**002** · Panorama de amenazas](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md) · [**003** · Frameworks](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md) · [**025** · Ética y legalidad](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)
2. **Riesgo y gobierno: tu materia prima** — [Parte 14](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md)
   - [**277** · Gestión de riesgos cuantitativa y cualitativa](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md) — **la clase central de esta ruta**
   - [**276** · Gobernanza](../classes/parte-14-grc-riesgo-y-cumplimiento/276-gobernanza-de-la-seguridad-de-la-informacion/README.md) · [**278** · ISO/IEC 27001](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md) · [**279** · NIST CSF](../classes/parte-14-grc-riesgo-y-cumplimiento/279-nist-cybersecurity-framework/README.md) · [**282** · Políticas](../classes/parte-14-grc-riesgo-y-cumplimiento/282-politicas-estandares-y-procedimientos/README.md)
   - [**284** · Riesgo de terceros](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md) · [**285** · Auditoría](../classes/parte-14-grc-riesgo-y-cumplimiento/285-auditoria-de-seguridad/README.md) · [**286** · Cultura de seguridad](../classes/parte-14-grc-riesgo-y-cumplimiento/286-concienciacion-y-cultura-de-seguridad/README.md) · [**287** · KPI y KRI](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md) · [**289** · Privacidad](../classes/parte-14-grc-riesgo-y-cumplimiento/289-privacidad-y-proteccion-de-datos/README.md)
3. **La capa que te hace creíble arriba** — [Parte 17](../classes/parte-17-profundizacion-para-certificaciones/README.md)
   - [**321** · Comunicación y reporte](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md) — **la competencia que define el puesto**
   - [**328** · Riesgo cuantitativo y continuidad avanzada](../classes/parte-17-profundizacion-para-certificaciones/328-gestion-de-riesgos-cuantitativa-y-continuidad-avanzada/README.md) · [**320** · Gobierno y regulación](../classes/parte-17-profundizacion-para-certificaciones/320-gobierno-aspectos-legales-regulatorios-y-gestion-del-programa/README.md)
   - [**318** · Programa de vulnerabilidades](../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md) · [**311** · Clasificación del dato](../classes/parte-17-profundizacion-para-certificaciones/311-clasificacion-y-ciclo-de-vida-de-los-datos/README.md) · [**313** · Ciclo de vida de identidades](../classes/parte-17-profundizacion-para-certificaciones/313-gestion-del-ciclo-de-vida-de-identidades-iam-empresarial/README.md) · [**329** · Arquitectura empresarial y Zero Trust](../classes/parte-17-profundizacion-para-certificaciones/329-arquitectura-de-seguridad-empresarial-y-zero-trust/README.md)
4. **Lo que tu unidad va a construir**
   - [**236** · Secure SDLC](../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md) · [**237** · Modelado de amenazas](../classes/parte-11-devsecops-y-seguridad-del-sdlc/237-modelado-de-amenazas-stride-y-dread/README.md) — para entrar temprano en los proyectos
   - [**245** · Gestión de vulnerabilidades a escala](../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md) · [**248** · Cultura DevSecOps y security champions](../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md) — tu red de aliados tiene nombre
   - [**221** · Responsabilidad compartida en la nube](../classes/parte-10-seguridad-en-la-nube-y-contenedores/221-fundamentos-de-seguridad-en-la-nube-y-responsabilidad-compartida/README.md) · [**231** · CSPM](../classes/parte-10-seguridad-en-la-nube-y-contenedores/231-cloud-security-posture-management-cspm/README.md)
5. **La crisis que vas a acompañar**
   - [**202** · Ciclo de respuesta a incidentes](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/202-el-ciclo-de-respuesta-a-incidentes-nist-y-sans/README.md) · [**215** · Playbooks](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/215-playbooks-de-respuesta-a-incidentes/README.md) · [**219** · Ejercicios de mesa](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md)
   - [**197** · Métricas y madurez del SOC](../classes/parte-8-blue-team-deteccion-y-soc/197-metricas-y-madurez-del-soc/README.md) — para leer los informes del SOC corporativo con criterio

### Laboratorio y práctica

- 🧪 **[`labs/ciso-leadership`](../labs/ciso-leadership/README.md)** — el escenario **11**
  (roadmap de seguridad para una unidad de negocio) es el de esta ruta. Los escenarios **2**
  (registro de riesgos), **6** (proveedor crítico) y **5** (tabletop) son tu trabajo habitual.
- 🧪 [`blue-team-soc`](../labs/blue-team-soc/README.md) — para entender qué recibe y qué no ve el
  SOC corporativo que cubre a tu unidad.
- 🧪 [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md) — si tu unidad construye
  software, el [trayecto de Analista DevSecOps](../labs/devsecops-pipeline/TRAYECTO-ANALISTA-DEVSECOPS.md)
  te da el criterio de priorización que tendrás que defender.

### Capstone

**Un año de la unidad, en cuatro entregables.** Toma *Andes Retail* del laboratorio y trabaja sobre
su unidad de comercio electrónico:

1. **Perfil de riesgo de la unidad**: los ocho riesgos principales, cuantificados, **cada uno con
   un dueño con nombre y cargo dentro de la unidad**.
2. **Roadmap de seguridad a doce meses** priorizado y costeado, alineado con el plan corporativo y
   con el plan comercial de la unidad; incluye qué **no** se hará este año y por qué.
3. **Una excepción negociada**: un control corporativo que en tu unidad no cabe. Documenta el
   control compensatorio, el vencimiento y quién firma.
4. **El mismo mes informado dos veces**: una página para la dirección de tu unidad y una página
   para el CISO, con los mismos datos y distinto énfasis.

**Criterio de aceptación:** las dos versiones del informe deben ser **consistentes entre sí** —un
lector que vea ambas no debe encontrar una contradicción— y ningún riesgo puede figurar aceptado
por ti. Si aparece una contradicción, el capstone demuestra exactamente el fallo que este puesto
debe evitar.

### Portafolio

- El perfil de riesgo con dueños de negocio.
- El roadmap con la lista explícita de lo que no se hará.
- La excepción negociada con su compensación.
- Las dos versiones del informe mensual.
- Una retrospectiva: qué proyecto de tu unidad se hizo más seguro porque tú estabas en la sala.

## 🎤 Preguntas de entrevista

1. ¿A quién reporto y quién escribe mi evaluación de desempeño?
2. Cuéntame la última vez que tradujiste un riesgo técnico a una decisión de negocio. ¿Qué
   decidieron?
3. La unidad quiere lanzar en seis semanas y el control tarda diez. ¿Qué haces?
4. ¿Cómo evitas convertirte en el abogado defensor de tu unidad frente al programa central?
5. ¿Qué haces con una excepción que lleva tres años renovándose?
6. Un proyecto llegó a producción sin revisión. ¿De quién es el fallo y qué cambias?
7. ¿Cómo mides si tu presencia mejora la seguridad de la unidad?
8. ¿Cuál es la diferencia entre tu puesto y el de un Divisional CISO?
9. ¿Cómo consigues que te inviten a las reuniones donde se decide, no a las de revisión?
10. ¿Qué haces si descubres un problema que afecta a otra unidad y la tuya sale perjudicada al
    contarlo?

## 🎓 Certificaciones

| Certificación | Para qué sirve en este puesto | Dónde la cubre el programa |
|---|---|---|
| **CISM** (ISACA) | Gestión del programa y del riesgo: el examen más cercano al puesto | [Parte 14](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md) (examen fuera del programa) |
| **CRISC** (ISACA) | Riesgo, sobre todo si tu unidad es financiera | [**277**](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md) y [**328**](../classes/parte-17-profundizacion-para-certificaciones/328-gestion-de-riesgos-cuantitativa-y-continuidad-avanzada/README.md) |
| **CISSP** (ISC2) | Amplitud técnica y credibilidad general | [Parte 17](../classes/parte-17-profundizacion-para-certificaciones/README.md) y [**304**](../classes/parte-16-capstones-y-preparacion-de-certificaciones/304-preparacion-cissp-los-8-dominios/README.md) |
| **CySA+** (CompTIA) | Si vienes de operación y necesitas el aval intermedio | [Partes 8 y 17](../classes/parte-8-blue-team-deteccion-y-soc/README.md) |
| **ISO/IEC 27001 Lead Implementer** | Si tu unidad va a certificarse | [**278**](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md) |

Ninguna garantiza el puesto. Lo que se evalúa en la entrevista es si sabes hablar el idioma de una
dirección de negocio sin dejar de ser de seguridad.

## 📈 Progresión de carrera y salario

### Cargos de entrada y experiencia previa razonable

Se llega desde tres sitios, y cada uno tiene su déficit:

| Vía de origen | Qué traes | Qué te falta |
|---|---|---|
| [Analista SecOps](secops-analista.md) o [SOC](soc-blue-team.md) senior | Criterio técnico y credibilidad con el equipo | El idioma del negocio y la paciencia política |
| [GRC](grc.md) o riesgo operacional | Marco, riesgo y trato con auditoría | Profundidad técnica: te la van a probar |
| Gestión de proyectos o producto **dentro de la unidad** | Conocimiento del negocio y red interna | Todo el dominio de seguridad; es la vía más larga pero produce excelentes BISO |

Una trayectoria razonable combina experiencia en un rol de seguridad con exposición real al
negocio. **No hay un número universal de años**, y desconfía de quien lo afirme.

### Hacia dónde sigue

BISO → **BISO de una unidad mayor o de varias** → [**CISO**](ciso.md) (es una de las mejores
escuelas para el cargo) · → [**Divisional CISO**](ecosistema-ciso.md#a-dirección-interna-y-jerarquía)
si la unidad crece y el puesto gana presupuesto · → riesgo operacional o dirección de riesgo
tecnológico · → [vCISO](vciso.md) para empresas medianas, donde tu experiencia de traducción vale
mucho.

### Sobre la remuneración

Este programa no publica cifras específicas para este puesto: la retribución del BISO varía según
si es un cargo del programa de seguridad o de la unidad, y en el segundo caso suele incluir el
variable de la unidad —lo que a su vez es el conflicto de interés descrito más arriba—. Como
referencia orientativa, se sitúa **entre un rol senior de seguridad y una jefatura**; consulta los
rangos de la [ruta CISO](ciso.md#-progresión-de-carrera-y-salario) y de la
[ruta de Jefe de Seguridad](ciso-jefe-seguridad.md) con la advertencia que allí se hace, y
contrasta con estudios de remuneración con fecha y metodología publicadas.

## ⚠️ Mitos y errores comunes

- **«El BISO es el CISO de la unidad.»** No: no tiene el mandato, y en la mayoría de los casos ni
  presupuesto ni equipo. Si los tiene, entonces sí es un
  [Divisional CISO](ecosistema-ciso.md#a-dirección-interna-y-jerarquía) y hay que llamarlo así.
- **«Es un puesto de cumplimiento.»** El cumplimiento es una parte. El puesto es de **decisión de
  negocio informada por riesgo**.
- **«Su trabajo es conseguir que la unidad cumpla la política.»** Su trabajo es conseguir que la
  unidad **gestione su riesgo**; a veces eso implica cambiar la política, no solo aplicarla.
- **«Si la unidad está contenta, el BISO lo hace bien.»** Sospechoso. Un BISO que nunca genera
  fricción probablemente no está levantando lo que hay que levantar.
- **«El BISO acepta riesgos por la unidad.»** Nunca. Los prepara y consigue la firma de quien
  responde.
- **Señal de cargo decorativo:** te llaman para «revisar» un mes antes del lanzamiento, tu única
  herramienta es un formulario y nadie de la dirección de la unidad sabe quién eres. Ese puesto no
  es un BISO: es un trámite.

## ↔️ Diferencias con los cargos vecinos

| Frente a | Se parecen en | Se separan en |
|---|---|---|
| [**CISO**](ciso.md) | Vocabulario, riesgo, comités | El CISO responde por toda la organización, con presupuesto y equipo; el BISO por una unidad, con influencia |
| **Divisional / BU CISO** | Ambos viven en una unidad | El Divisional CISO **tiene mandato y presupuesto** de esa división; el BISO es un enlace |
| [**GRC Manager**](grc.md) | Ambos manejan riesgo y controles | El GRC mide y asesora de forma transversal; el BISO está **incrustado** en un negocio y prioriza dentro de él |
| [**Analista SecOps**](secops-analista.md) | Ambos priorizan vulnerabilidades | El analista trabaja el control y el ticket; el BISO trabaja la decisión de negocio |
| [**Field CISO**](field-ciso.md) | Ambos traducen entre mundos | El BISO traduce **dentro** de su organización; el Field CISO **entre** organizaciones, y vende |
| **Auditoría interna** | Ambos revisan la unidad | El auditor es independiente y dictamina; el BISO ayuda a construir y por eso no puede dictaminar |
| **Security champion** | Ambos están dentro del equipo de negocio | El champion es un rol añadido a un puesto técnico; el BISO es un puesto de seguridad a tiempo completo |

## 📎 Fuentes y fecha de consulta

Consultadas el **26 de agosto de 2026**.

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — la función *Gobernar*
  incluye roles, responsabilidades y autoridades, que es el marco público más útil para justificar
  por qué el dueño del riesgo debe ser del negocio y no de seguridad.
- [ISO/IEC 27001](https://www.iso.org/standard/27001) — asignación de responsabilidades dentro del
  SGSI. Norma de pago: aquí se explican conceptos, no se reproduce texto.
- [ISACA](https://www.isaca.org/) — CISM y CRISC, cuerpos de conocimiento de gestión y riesgo.
- [ISC2](https://www.isc2.org/) — CISSP.
- [CISA](https://www.cisa.gov/) — objetivos de desempeño intersectoriales, útiles para acordar un
  mínimo común entre unidades muy distintas.
- [Ecosistema CISO de este programa](ecosistema-ciso.md) — taxonomía, matriz comparativa y contexto
  chileno con sus fuentes normativas.

## 🚀 Siguientes pasos

1. Lee el [ecosistema CISO](ecosistema-ciso.md), en especial la diferencia entre BISO y Divisional
   CISO.
2. Haz el escenario **11** del [laboratorio ejecutivo](../labs/ciso-leadership/README.md).
3. Resuelve la [evaluación del ecosistema](../labs/ciso-leadership/EVALUACION.md), con foco en el
   ejercicio RACI: es exactamente la habilidad que este puesto ejerce a diario.
4. Rinde el [examen final de BISO](../docs/examen-final-por-rol.md).
5. Si lo que quieres es el mandato completo, tu página es [CISO](ciso.md); si quieres el enfoque
   transversal sin unidad asignada, es [GRC](grc.md).

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🗂️ [El ecosistema CISO](ecosistema-ciso.md) — mapa de cargos, matriz comparativa y test del mandato
- 🎩 [CISO](ciso.md) · 🏛️ [GRC](grc.md) · 📟 [Analista SecOps](secops-analista.md)
- 🧪 [Laboratorio ejecutivo CISO](../labs/ciso-leadership/README.md) · 🎓 [Evaluación del ecosistema](../labs/ciso-leadership/EVALUACION.md)
- 🏠 [Inicio del programa](../README.md)
