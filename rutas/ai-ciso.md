# 🤖 AI CISO / Responsable de seguridad y gobierno de la IA

> El cargo que responde por los **sistemas de inteligencia artificial** de una organización: los
> que construye, los que compra, los que sus empleados usan sin avisar y los que sus proveedores
> han incorporado sin decírselo. Es, con diferencia, **el título menos consolidado de todo el
> ecosistema CISO** —y el que tiene el trabajo más urgente detrás.
>
> **Nivel de entrada:** ninguno; se llega desde seguridad, riesgo o gobierno del dato ·
> **Foco:** inventario, gobierno, evaluación previa al despliegue y riesgo de modelos y agentes ·
> **Certificación faro:** ninguna consolidada todavía; CISM o CRISC como base de gestión y los
> marcos de IA como instrumental

**Alias y variantes:** *AI CISO*, *Chief AI Security Officer*, *Head of AI Security*, *AI Risk
Officer*, *Responsible AI Lead* (con más peso en ética y sesgo que en seguridad), *AI Governance
Lead*. En muchas organizaciones **no es un cargo**: es un encargo añadido al
[CISO](ciso.md), al responsable de riesgo o al de datos.

**Fecha de consulta de las fuentes: 26 de agosto de 2026.**

## 🧭 Qué es y por qué importa

### Definición

El responsable de que la organización **sepa qué sistemas de IA tiene, qué riesgo introduce cada
uno y bajo qué condiciones se permiten**, y de que existan controles proporcionados en todo su
ciclo de vida: datos de entrenamiento, modelo, aplicación que lo consume, agentes que actúan con
él y proveedores que lo suministran.

### Nivel de consolidación del título: emergente, y hay que decirlo

Esta guía es explícita al respecto porque la honestidad importa más aquí que en ninguna otra ruta:

- **El trabajo existe y es real.** Inventariar modelos, gobernar datos, evaluar antes de
  desplegar, controlar agentes con permisos y responder por el uso de IA de terceros son tareas
  que alguien está haciendo hoy en muchas organizaciones.
- **El título no está estandarizado.** Su contenido varía enormemente entre empresas y hay
  organizaciones que lo usan como etiqueta de marketing.
- **Con frecuencia no hay mandato ejecutivo detrás**: es una función normativa —escribe la
  política, evalúa, recomienda— sin presupuesto ni capacidad de detener un despliegue.
- **No hay certificación consolidada** que acredite el puesto. Quien te venda una como requisito
  te está vendiendo algo.

**Conclusión práctica: antes de aceptar el cargo, aplica el
[test del mandato](ecosistema-ciso.md#-el-test-del-mandato-cómo-comprobar-un-cargo-real).** Si no
puedes detener un despliegue y no tienes inventario, no tienes un cargo: tienes una expectativa.

### Qué problema resuelve

| Problema | Por qué es nuevo | Qué aporta este rol |
|---|---|---|
| Nadie sabe cuántos sistemas de IA hay en la empresa | Se adoptan sin pasar por compras ni por arquitectura | **Inventario**: el primer entregable, siempre |
| Un modelo decide sobre personas y nadie puede explicar por qué | El riesgo no es solo técnico: es legal y reputacional | Evaluación previa al despliegue con criterios documentados |
| Datos sensibles salen de la organización dentro de un aviso a un servicio externo | El canal de fuga es conversacional, no un fichero | Política de uso, controles y alternativas viables |
| Un agente con permisos hace algo que nadie autorizó | El sistema **actúa**, no solo responde | Límites de permisos, aprobación humana y trazabilidad |
| El proveedor incorporó IA a su producto y no lo dijo | El riesgo entra por la cadena de suministro | Cláusulas y reevaluación de terceros |
| El modelo se degrada o cambia sin aviso | Los modelos no son estáticos | Vigilancia continua y criterio de reevaluación |

### Qué hace y qué no hace

| Sí hace | No hace |
|---|---|
| Mantener el inventario de sistemas de IA, propios y de terceros | Construir los modelos: eso es de ciencia de datos e ingeniería |
| Definir la política de uso aceptable de IA y sus excepciones | Decidir la estrategia de negocio de IA |
| Evaluar el riesgo antes del despliegue y periódicamente después | Aprobar el uso: lo aprueba el dueño del negocio o el comité |
| Fijar los controles de datos de entrenamiento y de datos de entrada | Sustituir al [DPO](ecosistema-ciso.md#d-cargos-vecinos-que-no-son-tipos-de-ciso) en protección de datos |
| Probar los sistemas frente a ataques específicos de IA | Ser el único responsable del sesgo y la equidad: eso es un equipo |
| Definir límites y trazabilidad de agentes con permisos | Frenar la adopción por precaución genérica |
| Evaluar proveedores que incorporan IA | Certificar el cumplimiento de una norma de IA |
| Integrar la IA en la respuesta a incidentes | Prometer que un modelo no puede ser manipulado |

### Dónde existe

Empresas que construyen productos con IA, organizaciones reguladas que usan modelos para decidir
sobre personas (crédito, seguros, salud, empleo), grandes tecnológicas, y cualquier organización
con un despliegue masivo de asistentes internos. En una empresa mediana, este trabajo lo absorbe el
[CISO](ciso.md) o un [vCISO](vciso.md) con el apoyo de legal.

## 🏛️ Mandato, autoridad y responsabilidad

### Línea de reporte

| Reporta a | Consecuencia |
|---|---|
| **CISO** | Modelo más frecuente; hereda gobierno y controles ya montados. Riesgo: la IA queda como un apéndice |
| **Chief Data / Analytics Officer** | Cerca de donde se construyen los modelos. Riesgo: juez y parte |
| **CRO o riesgo operacional** | Buen encaje en sectores regulados. Riesgo: lejos de la ingeniería |
| **Comité de IA multidisciplinar** | El modelo más sano cuando existe: seguridad, legal, datos, negocio y ética |

En organizaciones serias, el punto de decisión no es una persona sino un **comité de IA** que
aprueba despliegues; el AI CISO es quien prepara y sostiene ese comité.

### Autoridad, presupuesto, equipo y riesgo

- **Autoridad:** normativa más que ejecutiva. Su palanca característica es la **evaluación previa
  obligatoria**: ningún sistema de IA entra en producción sin pasar por ella. Si esa obligación no
  existe por escrito, el rol no tiene palanca.
- **Presupuesto:** rara vez propio al principio; suele salir del programa de seguridad o del de
  datos.
- **Equipo:** pequeño. A menudo una o dos personas y una red de referentes en los equipos de
  datos.
- **Riesgo:** responde por el **riesgo de los sistemas de IA**. La aceptación de un riesgo residual
  —desplegar un modelo con una limitación conocida— la firma el dueño del proceso de negocio
  afectado, no seguridad.

### Conflictos de interés y límites éticos

Esta ruta tiene un componente ético más denso que las demás, porque los sistemas de IA afectan a
personas de forma directa.

| Situación | Riesgo | Cómo se maneja |
|---|---|---|
| Presión por desplegar rápido «porque la competencia ya lo tiene» | Evaluación convertida en trámite | Criterios y plazos de evaluación acordados **antes** y proporcionados al riesgo |
| Un modelo funciona peor para un grupo de personas | Daño real y riesgo legal | Métricas desagregadas, umbral acordado y escalamiento a un comité, no una decisión técnica |
| El equipo de datos evalúa su propio modelo | Falta de independencia | La evaluación de riesgo la coordina alguien fuera del equipo que construyó |
| Se promete explicabilidad que el modelo no tiene | Tergiversación | Documentar qué se puede explicar y qué no, y decidir en consecuencia |
| Un agente puede ejecutar acciones irreversibles | Daño sin intención | Aprobación humana obligatoria para acciones irreversibles, y trazabilidad completa |
| Datos personales usados para entrenar sin base para ello | Incumplimiento y daño | Coordinación **formal** con el DPO; su independencia no se absorbe en tu función |
| Vigilancia de empleados disfrazada de productividad | Ético antes que legal | Transparencia, proporcionalidad y una conversación explícita, no una decisión de seguridad |

## 🗓️ El día, el mes y el año

**Un día típico.** Revisión de tres solicitudes de uso de un servicio de IA externo; sesión con un
equipo de producto sobre un agente que quiere permisos de escritura sobre la base de datos;
actualización del inventario tras descubrir dos herramientas nuevas en la factura de la nube;
lectura del cambio de condiciones de un proveedor de modelos.

**Un mes típico.** Un comité de IA con decisiones registradas; una evaluación completa previa al
despliegue de un sistema relevante; una prueba adversarial sobre una aplicación con modelo de
lenguaje; revisión de la política de uso a la luz de lo que se descubrió; formación a un equipo.

**Un año típico.** El inventario completo y su verificación; el ciclo de reevaluación de los
sistemas ya desplegados —que **no** es opcional, porque los modelos y sus proveedores cambian—;
un ejercicio de mesa de «el modelo hizo algo que no debía y el cliente se enteró antes que
nosotros»; la actualización del marco a medida que la regulación de IA avanza; y la conversación
de presupuesto, que en este rol es sobre todo una conversación sobre plantilla.

### Interlocutores

| Internos | Externos |
|---|---|
| [CISO](ciso.md) y su equipo | Proveedores de modelos y plataformas |
| Ciencia de datos e ingeniería de ML | Auditores y evaluadores externos |
| Producto y negocio (los dueños del proceso) | Reguladores sectoriales |
| Legal, cumplimiento y el **DPO** | Investigadores de seguridad de IA |
| Arquitectura y plataforma | Comunidad y estándares abiertos |
| Recursos humanos, cuando el sistema afecta a empleados | Clientes que preguntan si usas IA con sus datos |

## 🧾 Entregables verificables

| Entregable | Qué demuestra | Cómo se verifica |
|---|---|---|
| **Inventario de sistemas de IA** | Que sabes qué tienes | Sistema, dueño, propósito, datos que usa, modelo, proveedor, criticidad, fecha de última revisión |
| **Registro de riesgos de IA** | Que el riesgo está caracterizado | Riesgo, escenario concreto, impacto, controles, residual, dueño **del negocio** |
| **Política de uso aceptable de IA** | Que hay reglas conocidas y aplicables | Qué se puede, qué no, con qué datos, con qué aprobación y qué alternativa se ofrece |
| **Evaluación previa al despliegue** | Que nada entra sin revisión | Criterios, evidencia, decisión, condiciones y fecha de reevaluación |
| **Informe de pruebas adversariales** | Que el sistema se probó, no se supuso | Escenarios, resultados, mitigaciones y lo que quedó sin resolver |
| **Ficha del sistema** (propósito, límites, datos, métricas) | Transparencia interna y hacia el cliente | Incluye **limitaciones conocidas**, no solo capacidades |
| **Criterios y límites de agentes** | Control de sistemas que actúan | Permisos, acciones irreversibles, aprobación humana, registro y reversión |
| **Cláusulas de IA para proveedores** | Control del riesgo que entra por contrato | Aviso de cambios de modelo, uso de datos, subencargados, auditabilidad |
| **Plan de respuesta a incidentes de IA** | Que hay un cauce antes de necesitarlo | Quién decide desconectar el sistema y con qué criterio |

## 📏 KPI y KRI

| Indicador | Tipo | Qué dice |
|---|---|---|
| Cobertura del inventario (sistemas conocidos frente a descubiertos) | KPI | Lo primero que hay que ganar |
| Sistemas desplegados **con** evaluación previa | KPI | Si el control existe o se elude |
| Tiempo medio de evaluación por nivel de riesgo | KPI | Si el control es viable o empuja a saltárselo |
| Sistemas críticos reevaluados dentro de plazo | KPI | Que el gobierno es continuo |
| Proveedores con cláusulas de IA firmadas | KPI | Control de la cadena de suministro |
| Cobertura de pruebas adversariales en sistemas de alto riesgo | KPI | Rigor técnico del programa |
| **Sistemas de IA en producción descubiertos fuera del inventario** | **KRI** | El indicador más honesto del estado real |
| **Agentes con permisos para acciones irreversibles sin aprobación humana** | **KRI** | El riesgo estructural de los sistemas que actúan |
| Incidentes de fuga de datos por uso de servicios externos | **KRI** | La política no funciona o no ofrece alternativa |
| Decisiones automatizadas sobre personas sin revisión | **KRI** | Exposición legal y ética |
| Modelos en producción sin dueño de negocio identificado | **KRI** | Nadie responde por lo que ese sistema decide |

## 🧠 Qué necesitas saber

### Competencias técnicas

- **Cómo funciona un sistema de IA lo suficiente para evaluarlo**: datos, entrenamiento,
  inferencia, ajuste fino, recuperación aumentada, agentes y herramientas. No necesitas entrenar
  modelos; necesitas saber dónde puede fallar cada pieza.
- **Ataques específicos**: adversariales, envenenamiento de datos y de modelos, extracción de
  modelo, inyección de instrucciones directa e indirecta, fuga por el contexto, abuso de
  herramientas de un agente.
- **Controles**: aislamiento, mínimo privilegio para agentes, validación de entradas y salidas,
  registro completo de interacciones, límites de tasa, aprobación humana en el bucle.
- **Gobierno del dato**: procedencia, clasificación, retención y qué datos pueden entrar en un
  contexto o en un entrenamiento.
- **Seguridad de aplicaciones**, porque la mayoría de los fallos reales están en la aplicación que
  rodea al modelo, no en el modelo.
- **Vigilancia y evaluación continua**: los modelos y sus proveedores cambian bajo tus pies.

### Competencias de negocio

- Entender **qué decisión de negocio automatiza** cada sistema y qué pasa si se equivoca.
- Poner precio al riesgo y al control, en un dominio donde la incertidumbre es alta y hay que
  decirlo.
- Evitar los dos extremos que matan el puesto: bloquear todo (te ignoran) y aprobar todo (no
  aportas).

### Comunicación y negociación

- Explicar a un directorio qué puede y qué no puede hacer un modelo, sin exageración en ninguna
  dirección.
- Sostener una conversación técnica con un equipo de ciencia de datos que sabe más que tú del
  modelo y menos que tú del riesgo.
- Escribir una política que la gente pueda cumplir: si prohíbes sin ofrecer alternativa, la
  organización usará IA a tus espaldas y perderás el inventario.

### Competencias regulatorias

El terreno regulatorio de la IA está en construcción y avanza a distinta velocidad según la
jurisdicción. **No afirmes que algo «cumple» sin verificar la norma aplicable y su fecha de
entrada en vigor**, y trabaja siempre con legal. Lo que sí puedes hacer hoy:

- Apoyarte en marcos voluntarios reconocidos: el **NIST AI Risk Management Framework** para
  estructurar el trabajo y la **ISO/IEC 42001** para el sistema de gestión.
- Cumplir lo que ya te aplica **con independencia de la IA**: protección de datos personales,
  normativa sectorial y obligaciones contractuales.
- Seguir la regulación específica de IA en las jurisdicciones donde operas, con fecha de consulta.
  En Chile, revisa el estado en la [BCN](https://www.bcn.cl/leychile) y el
  [contexto del ecosistema](ecosistema-ciso.md#-contexto-chileno-y-latinoamericano).

### Componente comercial

Ninguno. Si tu organización **vende** productos con IA, la parte comercial de esa conversación
pertenece al [Product CISO](product-ciso.md); tú aportas la evaluación que la sostiene.

## 📚 Tu ruta en el programa

1. **Fundamentos y ética** — [**001**](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md) · [**003** · Frameworks](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md) · [**025** · Ética y legalidad](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)
2. **[Parte 15 · Seguridad de IA y machine learning](../classes/parte-15-seguridad-de-ia-y-machine-learning/README.md) — el núcleo del cargo, entera**
   - [**291** · Introducción a la seguridad de IA y ML](../classes/parte-15-seguridad-de-ia-y-machine-learning/291-introduccion-a-la-seguridad-de-ia-y-ml/README.md) · [**292** · Ataques adversariales](../classes/parte-15-seguridad-de-ia-y-machine-learning/292-ataques-adversariales-a-modelos/README.md) · [**293** · Envenenamiento de datos y modelos](../classes/parte-15-seguridad-de-ia-y-machine-learning/293-envenenamiento-de-datos-y-modelos/README.md) · [**294** · Robo y extracción de modelos](../classes/parte-15-seguridad-de-ia-y-machine-learning/294-robo-y-extraccion-de-modelos/README.md)
   - [**295** · OWASP Top 10 para aplicaciones con LLM](../classes/parte-15-seguridad-de-ia-y-machine-learning/295-owasp-top-10-para-aplicaciones-con-llm/README.md) · [**296** · Prompt injection y jailbreaks](../classes/parte-15-seguridad-de-ia-y-machine-learning/296-prompt-injection-y-jailbreaks/README.md) · [**297** · RAG y agentes](../classes/parte-15-seguridad-de-ia-y-machine-learning/297-seguridad-de-aplicaciones-con-llm-rag-y-agentes/README.md)
   - [**298** · IA aplicada a la defensa](../classes/parte-15-seguridad-de-ia-y-machine-learning/298-ia-aplicada-a-la-defensa-deteccion-y-soc/README.md) · [**299** · IA ofensiva y deepfakes](../classes/parte-15-seguridad-de-ia-y-machine-learning/299-ia-ofensiva-y-deepfakes/README.md) · [**300** · Gobernanza y ética de la IA segura](../classes/parte-15-seguridad-de-ia-y-machine-learning/300-gobernanza-y-etica-de-la-ia-segura/README.md) — **la clase que define esta ruta**
3. **Los agentes, que son la parte que actúa** — [Parte 18](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/README.md)
   - [**331** · IA generativa y LLM en ciberseguridad: capacidades y límites](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/331-ia-generativa-y-llms-en-ciberseguridad-panorama-y-limites/README.md) · [**332** · Agentes de IA y el Model Context Protocol](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/332-agentes-de-ia-y-el-model-context-protocol-mcp-para-seguridad/README.md)
   - [**337** · IA para el lado defensivo](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/337-ia-para-el-lado-defensivo-soc-triaje-y-forense/README.md) · [**339** · Riesgos, guardrails, OPSEC y ética](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/339-riesgos-guardrails-opsec-y-etica-del-hacking-con-ia/README.md) — **léela como el catálogo de lo que tienes que gobernar**
4. **Gobierno y riesgo: el esqueleto** — [Parte 14](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md)
   - [**276** · Gobernanza](../classes/parte-14-grc-riesgo-y-cumplimiento/276-gobernanza-de-la-seguridad-de-la-informacion/README.md) · [**277** · Gestión de riesgos](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md) · [**282** · Políticas](../classes/parte-14-grc-riesgo-y-cumplimiento/282-politicas-estandares-y-procedimientos/README.md) · [**284** · Terceros](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md) · [**287** · KPI y KRI](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md) · [**289** · Privacidad y protección de datos](../classes/parte-14-grc-riesgo-y-cumplimiento/289-privacidad-y-proteccion-de-datos/README.md)
5. **El dato, que es la materia prima del riesgo**
   - [**311** · Clasificación y ciclo de vida de los datos](../classes/parte-17-profundizacion-para-certificaciones/311-clasificacion-y-ciclo-de-vida-de-los-datos/README.md) · [**312** · Retención, destrucción y DLP](../classes/parte-17-profundizacion-para-certificaciones/312-retencion-destruccion-segura-de-datos-y-dlp/README.md) · [**320** · Gobierno y regulación](../classes/parte-17-profundizacion-para-certificaciones/320-gobierno-aspectos-legales-regulatorios-y-gestion-del-programa/README.md) · [**321** · Comunicación y reporte](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md)
6. **La aplicación que rodea al modelo, donde están casi todos los fallos**
   - [**236** · Secure SDLC](../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md) · [**237** · Modelado de amenazas](../classes/parte-11-devsecops-y-seguridad-del-sdlc/237-modelado-de-amenazas-stride-y-dread/README.md) · [**247** · Seguridad de APIs](../classes/parte-11-devsecops-y-seguridad-del-sdlc/247-seguridad-de-apis-en-el-ciclo-de-desarrollo/README.md) · [**222** · IAM en la nube](../classes/parte-10-seguridad-en-la-nube-y-contenedores/222-iam-en-la-nube-identidades-roles-y-permisos/README.md)
7. **La crisis** — [**202** · Ciclo de respuesta](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/202-el-ciclo-de-respuesta-a-incidentes-nist-y-sans/README.md) · [**215** · Playbooks](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/215-playbooks-de-respuesta-a-incidentes/README.md) · [**219** · Ejercicios de mesa](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md)

### Laboratorio y práctica

- 🧪 **[`labs/ciso-leadership`](../labs/ciso-leadership/README.md)** — el escenario **13**
  (inventario y registro de riesgos de IA) es el de esta ruta.
- 🧪 [`kali-mcp-ia`](../labs/kali-mcp-ia/README.md) — un agente de IA con herramientas reales.
  Recórrelo **desde el lado del que tiene que gobernarlo**: qué permisos pide, qué puede hacer sin
  supervisión, qué queda registrado y qué no.
- 🧪 [`appsec-web`](../labs/appsec-web/README.md) — porque la mayoría de los fallos de una
  aplicación con IA son fallos de aplicación.

### Capstone

**El programa mínimo viable de gobierno de IA.** Sobre *Andes Retail* del laboratorio, que ha
desplegado un asistente de atención al cliente, un modelo de detección de fraude y un agente
interno con acceso a documentos:

1. **Inventario** de los tres sistemas más los que descubras en el material del escenario, con
   dueño de negocio, datos que usan, proveedor y criticidad.
2. **Registro de riesgos de IA**: para cada sistema, al menos tres riesgos con **escenario
   concreto** (no «riesgo de sesgo», sino «el modelo rechaza X con más frecuencia que Y, y el
   cliente reclama»), control propuesto y residual.
3. **Política de uso aceptable** de una página, con la alternativa que ofreces para el caso que
   prohíbes.
4. **Evaluación previa al despliegue** completa del agente interno, incluidos los límites de
   permisos y qué acciones exigen aprobación humana.
5. **Informe de pruebas adversariales** sobre el asistente de atención al cliente: al menos tres
   escenarios de inyección de instrucciones, con resultado y mitigación.
6. **Nota de una página** para el comité de dirección: qué se aprueba, qué se condiciona y qué se
   detiene.

**Criterio de aceptación:** cada riesgo debe tener un **escenario concreto y comprobable** y un
dueño de negocio con nombre. Un registro de riesgos de IA lleno de categorías abstractas no está
aprobado: es exactamente el error que este puesto debe evitar.

### Portafolio

- El inventario, con la columna de «cómo lo descubrí».
- El registro de riesgos con escenarios concretos.
- La política de uso aceptable que ofrece alternativas.
- La evaluación del agente con sus límites de permisos.
- El informe adversarial, incluido lo que **no** conseguiste mitigar.

## 🎤 Preguntas de entrevista

1. ¿Cuántos sistemas de IA hay hoy en esta organización? ¿Cómo lo sabemos?
2. ¿Puedo detener un despliegue? ¿Está escrito?
3. Un equipo quiere un agente con permisos de escritura en producción. ¿Cuál es tu proceso?
4. ¿Qué diferencia hay entre tu función y la del DPO? ¿Dónde se solapan y dónde no?
5. ¿Cómo evalúas un modelo de un proveedor que no te deja ver nada?
6. Descubres que el proveedor cambió el modelo sin avisar. ¿Qué haces?
7. ¿Cómo escribes una política de uso que la gente cumpla en lugar de esquivar?
8. Dame un escenario de riesgo concreto de inyección indirecta de instrucciones en esta empresa.
9. ¿Qué haces si el modelo funciona peor para un grupo de clientes?
10. ¿Qué parte de este trabajo crees que no debería llamarse «AI CISO»?

## 🎓 Certificaciones

**No existe todavía una certificación consolidada de referencia para este puesto, y esta guía no
va a inventar una.** Lo que hay son credenciales de gestión que sirven de base y marcos que se
usan como instrumental.

| Credencial o marco | Qué aporta | Dónde lo cubre el programa |
|---|---|---|
| **CISM** (ISACA) | Base de gestión del programa y del riesgo | [Parte 14](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md) |
| **CRISC** (ISACA) | Riesgo, útil en sectores regulados | [**277**](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md) |
| **CISSP** (ISC2) | Amplitud y credibilidad general | [Parte 17](../classes/parte-17-profundizacion-para-certificaciones/README.md) |
| **CIPP / CIPM** (IAPP) | Privacidad, que es la mitad del riesgo de IA en la práctica | [**289**](../classes/parte-14-grc-riesgo-y-cumplimiento/289-privacidad-y-proteccion-de-datos/README.md) |
| **NIST AI RMF** (marco) | Estructura del trabajo: gobernar, mapear, medir, gestionar | [**300**](../classes/parte-15-seguridad-de-ia-y-machine-learning/300-gobernanza-y-etica-de-la-ia-segura/README.md) |
| **ISO/IEC 42001** (norma) | Sistema de gestión de IA; certificable por organismos acreditados | [**300**](../classes/parte-15-seguridad-de-ia-y-machine-learning/300-gobernanza-y-etica-de-la-ia-segura/README.md) |
| **OWASP Top 10 para LLM** (referencia) | Vocabulario común de fallos en aplicaciones con modelos | [**295**](../classes/parte-15-seguridad-de-ia-y-machine-learning/295-owasp-top-10-para-aplicaciones-con-llm/README.md) |

Han aparecido certificaciones comerciales de «seguridad de IA» de reciente creación. Antes de
pagar una, comprueba quién la reconoce, qué evalúa y desde cuándo existe: en un dominio joven, la
credencial vale lo que valga quien la emite.

## 📈 Progresión de carrera y salario

### Cargos de entrada y experiencia previa razonable

| Vía de origen | Qué traes | Qué te falta |
|---|---|---|
| Seguridad (CISO, [GRC](grc.md), [AppSec](appsec.md)) | Gobierno, riesgo, controles y credibilidad | El dominio de ML: hay que estudiarlo de verdad, no por encima |
| Ciencia de datos o ingeniería de ML | Entender el sistema por dentro | Riesgo, gobierno, política y la conversación ejecutiva |
| Gobierno del dato o privacidad | Procedencia, clasificación, base legal | Seguridad ofensiva y evaluación técnica |
| Riesgo operacional | Marco, comité, cuantificación | Todo el dominio técnico |

**Ninguna vía llega completa**, y esa es una característica del puesto, no un defecto tuyo. Se
compensa con un equipo mixto y con reconocer en voz alta lo que no sabes.

### Hacia dónde sigue

AI CISO → [**CISO**](ciso.md) con una especialidad muy demandada · → **Chief AI Officer** o
dirección de riesgo de IA · → [**Product CISO**](product-ciso.md) si la empresa vende IA · →
consultoría y [vCISO](vciso.md) especializado en gobierno de IA · → auditoría y evaluación
independiente de sistemas de IA, un mercado que está naciendo.

### Sobre la remuneración

Este programa **no publica cifras para este puesto**, y aquí la razón es más fuerte que en las
demás rutas: el título es tan nuevo y tan poco estandarizado que cualquier rango sería un dato
inventado con apariencia de estudio. Si negocias este cargo:

1. Pregunta si es **un cargo o un encargo añadido**. Cambia el número y cambia el puesto.
2. Compara con la banda de tu organización para roles de riesgo o seguridad senior, y con la
   [ruta CISO](ciso.md#-progresión-de-carrera-y-salario) como techo orientativo.
3. Negocia el mandato antes que el sueldo: sin evaluación previa obligatoria y sin inventario, el
   cargo no es sostenible a ningún precio.

## ⚠️ Mitos y errores comunes

- **«AI CISO es un cargo consolidado.»** No lo es. Es un título emergente con un trabajo real
  detrás. Decirlo claro es parte de hacer bien este trabajo.
- **«La seguridad de la IA es la seguridad del modelo.»** La mayoría de los incidentes reales
  ocurren en la aplicación, en los permisos del agente y en el dato, no en los pesos del modelo.
- **«Prohibir las herramientas de IA resuelve el riesgo.»** Lo desplaza a la sombra y destruye tu
  inventario, que es tu único activo. Ofrece una alternativa segura.
- **«Un modelo con guardrails no puede ser manipulado.»** Ninguna mitigación conocida elimina la
  inyección de instrucciones; se reduce la probabilidad y se limita el daño mediante permisos.
- **«Lo cubre el DPO.»** El DPO cubre datos personales, con independencia propia. Ni te sustituye
  ni lo sustituyes.
- **«Es un problema de ética, no de seguridad.»** Es de los dos, y separarlos produce comités que
  no deciden nada.
- **Señal de cargo decorativo:** te nombran responsable de IA, no hay inventario, no hay
  evaluación obligatoria, no tienes presupuesto y el primer entregable que te piden es una
  política de dos páginas para enseñar a un cliente.

## ↔️ Diferencias con los cargos vecinos

| Frente a | Se parecen en | Se separan en |
|---|---|---|
| [**CISO**](ciso.md) | Gobierno, riesgo, política, comités | El CISO responde por toda la seguridad; el AI CISO por un dominio nuevo dentro de ella. En la mayoría de las organizaciones, hoy, son la misma persona |
| [**Product CISO**](product-ciso.md) | Se solapan si el producto lleva IA | El Product CISO responde por lo que se vende; el AI CISO por los sistemas de IA que la organización usa y construye |
| **DPO** | Datos personales, evaluaciones de impacto | El DPO tiene independencia protegida y un mandato de privacidad; no se absorbe en esta función |
| **Chief Data Officer** | El dato como activo | El CDO maximiza el valor del dato; el AI CISO gobierna su riesgo. Tensión sana y necesaria |
| **Responsible AI Lead** | Comités, evaluaciones, políticas | El foco de aquel es sesgo, equidad y transparencia; el tuyo, seguridad y riesgo. Se necesitan mutuamente |
| **Ingeniero de ML** | El sistema | El ingeniero construye y optimiza; tú evalúas y condicionas |
| [**Analista SOC**](soc-blue-team.md) usando IA | Ambos tocan IA | El SOC **usa** IA para defender; tú **gobiernas** la IA que la organización despliega |

## 📎 Fuentes y fecha de consulta

Consultadas el **26 de agosto de 2026**.

- [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/itl/ai-risk-management-framework)
  — marco voluntario que estructura las cuatro funciones (gobernar, mapear, medir, gestionar) y del
  que toma su forma el registro de riesgos propuesto en esta guía.
- [ISO/IEC 42001](https://www.iso.org/standard/81230.html) — sistema de gestión de inteligencia
  artificial. Norma de pago: este programa explica sus conceptos, no reproduce su texto.
- [OWASP Top 10 para aplicaciones con LLM](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
  — vocabulario común de fallos en aplicaciones con modelos de lenguaje.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — la base de gobierno
  sobre la que se apoya el programa de IA.
- [CISA](https://www.cisa.gov/) y [ENISA](https://www.enisa.europa.eu/) — orientación sobre
  adopción segura de IA y panorama de amenazas.
- [IAPP](https://iapp.org/) — cuerpo de conocimiento de privacidad, imprescindible para separar
  bien esta función de la del DPO.
- [Biblioteca del Congreso Nacional de Chile](https://www.bcn.cl/leychile) — para verificar el
  estado de la regulación chilena aplicable, incluida la
  [Ley 21.719](https://www.bcn.cl/leychile/navegar?idNorma=1209272) sobre datos personales, cuya
  entrada en vigencia está fijada para el 1 de diciembre de 2026.
- [Ecosistema CISO de este programa](ecosistema-ciso.md) — taxonomía, matriz comparativa y contexto
  chileno.

## 🚀 Siguientes pasos

1. Lee el [ecosistema CISO](ecosistema-ciso.md) y aplica el test del mandato: en esta ruta es
   obligatorio antes de aceptar el cargo.
2. Haz el escenario **13** del [laboratorio ejecutivo](../labs/ciso-leadership/README.md).
3. Recorre [`kali-mcp-ia`](../labs/kali-mcp-ia/README.md) desde el lado del gobierno, no del uso.
4. Rinde el [examen final de AI CISO](../docs/examen-final-por-rol.md).
5. Si tu organización **vende** IA, sigue por [Product CISO](product-ciso.md); si buscas el mandato
   completo, por [CISO](ciso.md).

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🗂️ [El ecosistema CISO](ecosistema-ciso.md) — mapa de cargos, matriz comparativa y test del mandato
- 🎩 [CISO](ciso.md) · 📦 [Product CISO](product-ciso.md) · 🏛️ [GRC](grc.md)
- 🧪 [Laboratorio ejecutivo CISO](../labs/ciso-leadership/README.md) · 🎓 [Evaluación del ecosistema](../labs/ciso-leadership/EVALUACION.md)
- 🏠 [Inicio del programa](../README.md)
