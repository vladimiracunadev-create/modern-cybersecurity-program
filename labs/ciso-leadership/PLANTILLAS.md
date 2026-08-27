# 🧾 Plantillas reutilizables del laboratorio ejecutivo

Quince plantillas para los [catorce escenarios](README.md). Están escritas para **copiarse y
rellenarse**: cópialas a tu propio documento y sustituye los campos. Cada una lleva una nota de
uso que explica el error que esa plantilla existe para evitar.

> ⚖️ **Ninguna de estas plantillas es un documento legal.** Son material de estudio. Un acta de
> aceptación de riesgo o una declaración de trabajo reales deben revisarse con el área legal de tu
> organización.

## 📇 Índice

| # | Plantilla | Escenarios que la usan |
|---|---|---|
| 1 | [RACI](#1--raci) | 1, 5, 7, 11, 14 |
| 2 | [Registro de riesgos](#2--registro-de-riesgos) | 2, 3, 4, 10, 11, 14 |
| 3 | [Aceptación formal de riesgo](#3--aceptación-formal-de-riesgo) | 2, 10, 11, 14 |
| 4 | [Cuadro de KPI y KRI](#4--cuadro-de-kpi-y-kri) | 1, 3, 4 |
| 5 | [Informe ejecutivo de una página](#5--informe-ejecutivo-de-una-página) | 1, 4, 5, 9, 11 |
| 6 | [Plan de 30/60/90 días](#6--plan-de-306090-días) | 7, 10 |
| 7 | [Análisis de impacto al negocio con RTO y RPO](#7--análisis-de-impacto-al-negocio-bia-con-rto-y-rpo) | 3, 5, 14 |
| 8 | [Guion de ejercicio de mesa](#8--guion-de-ejercicio-de-mesa-tabletop) | 5, 14 |
| 9 | [Evaluación de terceros](#9--evaluación-de-terceros) | 6, 12 |
| 10 | [Declaración de trabajo para vCISO](#10--declaración-de-trabajo-para-vciso) | 10 |
| 11 | [Formulario de descubrimiento para Field CISO](#11--formulario-de-descubrimiento-para-field-ciso) | 8, 9 |
| 12 | [Informe y paquete de confianza de producto](#12--informe-y-paquete-de-confianza-de-producto) | 12 |
| 13 | [Inventario de sistemas de IA](#13--inventario-de-sistemas-de-ia) | 13 |
| 14 | [Registro de riesgos de IA](#14--registro-de-riesgos-de-ia) | 13 |
| 15 | [Roadmap de seguridad OT](#15--roadmap-de-seguridad-ot) | 14 |

## 1 · RACI

**Para qué:** dejar por escrito quién hace, quién responde, a quién se consulta y a quién se
informa. **El error que evita:** que dos personas crean que la decisión es de la otra.

> **R** — *Responsible*: quien ejecuta la tarea.
> **A** — *Accountable*: quien responde por el resultado. **Solo puede haber uno por fila.**
> **C** — *Consulted*: se le consulta antes de decidir.
> **I** — *Informed*: se le informa después.

| Actividad o decisión | CEO / Gerencia | Dueño del proceso | CISO | TI / Operaciones | Legal | Comunicaciones | Proveedor |
|---|---|---|---|---|---|---|---|
| Aprobar la política de seguridad |  |  |  |  |  |  |  |
| Aceptar un riesgo residual |  |  |  |  |  |  |  |
| Declarar un incidente grave |  |  |  |  |  |  |  |
| Decidir el pago de un rescate |  |  |  |  |  |  |  |
| Detener un servicio en producción |  |  |  |  |  |  |  |
| Notificar a la autoridad |  |  |  |  |  |  |  |
| Comunicar a clientes |  |  |  |  |  |  |  |
| Autorizar acceso remoto de un proveedor |  |  |  |  |  |  |  |

**Reglas de validación de la plantilla:**

1. Exactamente **una A** por fila. Si hay dos, la fila está mal.
2. La **A de «aceptar un riesgo residual» nunca es el CISO** ni un asesor externo.
3. Si una fila no tiene ninguna **R**, esa actividad no va a ocurrir.
4. Si alguien es **A y R** en todas las filas, no tienes un RACI: tienes una lista de tareas de
   una persona.

## 2 · Registro de riesgos

**Para qué:** la herramienta central del oficio. **El error que evita:** riesgos sin dueño, sin
fecha y sin residual, que es lo mismo que no tenerlos.

| Campo | Qué escribir |
|---|---|
| **ID** | Identificador estable (R-001) |
| **Escenario de riesgo** | Una frase con **causa, evento y consecuencia**: «Un proveedor con acceso remoto compartido es comprometido y se despliega ransomware en las 78 tiendas, deteniendo la venta presencial» |
| **Activo o proceso afectado** | Qué se daña |
| **Probabilidad** | Escala declarada (alta/media/baja o frecuencia anual estimada) |
| **Impacto** | En dinero, tiempo de indisponibilidad, personas afectadas o incumplimiento |
| **Riesgo inherente** | Antes de controles |
| **Controles existentes** | Los que ya operan, con su eficacia observada |
| **Riesgo residual** | Después de los controles actuales |
| **Tratamiento** | Mitigar / transferir / evitar / **aceptar** |
| **Dueño del riesgo** | **Nombre y cargo de una persona del negocio.** Nunca «TI» ni «Seguridad» |
| **Responsable del tratamiento** | Quién ejecuta |
| **Fecha comprometida** | Día concreto |
| **Estado** | Abierto / en tratamiento / aceptado / cerrado |
| **Fecha de revisión** | Cuándo se vuelve a mirar |
| **Supuestos** | Lo que asumiste para estimar; sin esto no se puede discutir el número |

**Fila de ejemplo:**

| ID | Escenario | Residual | Tratamiento | Dueño del riesgo | Fecha |
|---|---|---|---|---|---|
| R-004 | Sin prueba de restauración documentada, un ransomware podría dejar el canal digital caído más de 72 h; pérdida estimada 4,1 MUSD/día en temporada alta | Alto | Mitigar: prueba de restauración completa y copias inmutables | Gerente Digital | 30/11 |

## 3 · Aceptación formal de riesgo

**Para qué:** dejar constancia de que **el negocio decidió** no tratar un riesgo. **El error que
evita:** que el CISO o un asesor externo cargue con una decisión que no le corresponde.

```text
ACTA DE ACEPTACIÓN DE RIESGO

Identificador del riesgo:  R-___
Fecha de la aceptación:    ___/___/______
Vigencia de la aceptación: hasta ___/___/______  (máximo 12 meses)

1. ESCENARIO DE RIESGO
   [Causa, evento y consecuencia, en una frase comprensible sin jerga técnica]

2. IMPACTO ESTIMADO Y SUPUESTOS
   Impacto: [dinero / horas de indisponibilidad / personas / incumplimiento]
   Supuestos usados: [los que sostienen la cifra]
   Probabilidad estimada y en qué se basa: [___]

3. OPCIONES DE TRATAMIENTO EVALUADAS
   Opción A: [descripción] — coste [___] — riesgo residual [___] — plazo [___]
   Opción B: [descripción] — coste [___] — riesgo residual [___] — plazo [___]
   Opción C: no tratar — riesgo residual [___]

4. DECISIÓN
   Se acepta el riesgo residual [alto/medio/bajo] por el siguiente motivo de negocio:
   [___]

5. CONDICIONES DE LA ACEPTACIÓN
   Controles compensatorios que se mantendrán: [___]
   Indicadores que se vigilarán: [___]
   Hechos que obligan a reabrir esta decisión antes del vencimiento: [___]

6. FIRMAS
   Acepta el riesgo (dueño del proceso de negocio):  Nombre / Cargo / Firma / Fecha
   Toma conocimiento (CISO o responsable de seguridad): Nombre / Cargo / Firma / Fecha
   Toma conocimiento (Legal o Cumplimiento, si aplica): Nombre / Cargo / Firma / Fecha
```

**Reglas:** la aceptación **caduca**; quien acepta es del negocio; el CISO «toma conocimiento», no
acepta; y un riesgo aceptado sigue en el registro, no desaparece.

## 4 · Cuadro de KPI y KRI

**Para qué:** que la dirección vea el estado del programa en una pantalla. **El error que evita:**
tableros con cuarenta métricas que nadie mira y ninguna que obligue a decidir.

| Indicador | Tipo | Valor actual | Objetivo | Tendencia | Umbral de alerta | Dueño | Qué decisión dispara |
|---|---|---|---|---|---|---|---|
| Cobertura de autenticación multifactor | KPI |  |  |  |  |  |  |
| Vulnerabilidades críticas abiertas > 30 días | KRI |  |  |  |  |  |  |
| Antigüedad de la vulnerabilidad crítica más antigua | KRI |  |  |  |  |  |  |
| Tiempo medio de detección (MTTD) | KPI |  |  |  |  |  |  |
| Tiempo medio de respuesta (MTTR) | KPI |  |  |  |  |  |  |
| Última prueba de restauración superada | KRI |  |  |  |  |  |  |
| Proveedores críticos evaluados en los últimos 12 meses | KPI |  |  |  |  |  |  |
| Riesgos aceptados con vigencia vencida | KRI |  |  |  |  |  |  |
| Hallazgos de auditoría cerrados en plazo | KPI |  |  |  |  |  |  |
| Presupuesto ejecutado frente a plan | KPI |  |  |  |  |  |  |

**Reglas:** máximo diez indicadores en la vista ejecutiva; cada uno con **una decisión asociada**;
si un indicador no cambia ninguna decisión, sácalo del tablero.

## 5 · Informe ejecutivo de una página

**Para qué:** que alguien sin formación técnica termine de leer **sabiendo qué tiene que decidir**.
**El error que evita:** informes técnicos disfrazados de ejecutivos.

```text
INFORME EJECUTIVO DE SEGURIDAD — [Organización] — [Periodo]

1. LO QUE NECESITA SABER (3 líneas)
   [Estado general en lenguaje llano. Sin siglas sin definir. Sin nombres de herramientas.]

2. LO QUE NECESITA DECIDIR HOY
   Decisión 1: [___]  ·  Plazo: [___]  ·  Coste: [___]  ·  Si no se decide: [___]
   Decisión 2: [___]  ·  Plazo: [___]  ·  Coste: [___]  ·  Si no se decide: [___]

3. LOS TRES RIESGOS QUE MÁS PESAN
   [Riesgo] — impacto en [dinero/servicio/clientes] — dueño — estado

4. QUÉ MEJORÓ Y QUÉ EMPEORÓ DESDE EL INFORME ANTERIOR
   Mejoró: [___]        Empeoró: [___]

5. CUATRO NÚMEROS
   [Indicador y valor]  ·  [Indicador y valor]  ·  [Indicador y valor]  ·  [Indicador y valor]

6. LO QUE NO ESTAMOS HACIENDO Y POR QUÉ
   [Honestidad explícita: qué queda fuera del alcance actual y qué haría falta para cubrirlo]
```

**Reglas:** una página de verdad; cada sigla se define la primera vez; el punto 6 no es opcional
—es lo que separa un informe de una campaña de autopromoción—.

## 6 · Plan de 30/60/90 días

**Para qué:** los primeros meses en un cargo nuevo. **El error que evita:** llegar cambiando cosas
antes de entender la organización, o pasar noventa días «escuchando» sin producir nada.

| Fase | Objetivo dominante | Entregables | Cómo se verifica |
|---|---|---|---|
| **Días 1–30 · Entender** | No romper nada y construir el mapa | Mapa de partes interesadas · inventario de lo que existe (personas, contratos, herramientas, deudas) · lectura de auditorías e incidentes previos · **una** mejora visible y barata | Documento de diagnóstico con lo que **no** sabes todavía |
| **Días 31–60 · Priorizar** | Convertir el diagnóstico en decisiones | Evaluación contra un marco (perfil actual y objetivo) · registro de riesgos inicial con dueños · borrador del plan director · propuesta de gobierno (comité, periodicidad, quién decide qué) | Registro de riesgos con dueños **aceptados por ellos** |
| **Días 61–90 · Comprometer** | Conseguir mandato y presupuesto | Plan director priorizado y costeado · presentación a la dirección con dos o tres decisiones concretas · cuadro de indicadores acordado · primer comité celebrado | Acta con las decisiones tomadas y el presupuesto aprobado o rechazado por escrito |

**Reglas:** una mejora visible en los primeros 30 días compra credibilidad para los otros 60; no
prometas resultados de seguridad en 90 días, promete **capacidad de decidir**.

## 7 · Análisis de impacto al negocio (BIA) con RTO y RPO

**Para qué:** saber qué hay que levantar primero y cuánto se puede perder. **El error que evita:**
tiempos de recuperación fijados por TI en lugar de por el negocio.

| Campo | Qué escribir |
|---|---|
| **Proceso de negocio** | El proceso, no el sistema |
| **Responsable del proceso** | Nombre y cargo |
| **Sistemas y datos que lo sostienen** | Incluidos los de terceros |
| **Impacto a las 4 h / 24 h / 72 h / 1 semana** | En dinero, clientes, personas y obligaciones |
| **Punto de mayor exposición** | Cierre de mes, temporada alta, turno de noche |
| **RTO acordado** | Tiempo máximo de indisponibilidad **acordado con el negocio** |
| **RPO acordado** | Pérdida máxima de datos aceptable |
| **RTO real medido** | El que se obtuvo en la última prueba, con fecha |
| **RPO real medido** | Ídem |
| **Brecha** | Diferencia entre acordado y medido, con el coste de cerrarla |
| **Dependencias externas** | Proveedores, con su propio compromiso de servicio |
| **Fecha de la última prueba** | Sin esto, el resto de la fila es una intención |

> Una fila con **RTO acordado** pero sin **RTO real medido** no es un BIA: es una lista de deseos.

## 8 · Guion de ejercicio de mesa (tabletop)

**Para qué:** ensayar la crisis antes de vivirla. **El error que evita:** ejercicios donde todo el
mundo acierta porque nadie tiene información incompleta ni reloj.

```text
EJERCICIO DE MESA — [Nombre] — [Fecha] — Duración: [90–150 min]

OBJETIVOS DE APRENDIZAJE (3 máximo)
  1. [___]   2. [___]   3. [___]

PARTICIPANTES Y ROLES
  Facilitador · Anotador · Dirección · CISO · TI/Operaciones · Legal · Comunicaciones ·
  Recursos Humanos · [Prevención de Riesgos, si es OT] · Observadores

REGLAS
  - Se juega con la información que hay, no con la que se desearía.
  - No se resuelve por «llamamos al proveedor y lo arregla».
  - Las decisiones se anotan con la hora.
  - No se busca culpables: se buscan huecos de proceso.

INYECTOS

  T+00  [Hecho inicial]
        Preguntas: ¿esto es un incidente? ¿quién lo declara? ¿a quién se avisa?
  T+20  [Escalada: aparece un dato que cambia la gravedad]
        Preguntas: ¿se detiene el servicio? ¿quién autoriza?
  T+45  [Presión externa: un cliente, un periodista o un plazo regulatorio]
        Preguntas: ¿qué se comunica, a quién, quién lo firma?
  T+70  [Decisión incómoda: coste alto, información incompleta]
        Preguntas: ¿quién decide? ¿con qué criterio? ¿queda registrado?
  T+90  [Recuperación: qué se restaura primero y cómo se verifica que está limpio]

CIERRE
  - Cronología de decisiones reconstruida.
  - Tres cosas que funcionaron · tres que no · tres acciones con dueño y fecha.
  - Qué documento faltaba y quién lo escribe.
```

## 9 · Evaluación de terceros

**Para qué:** el riesgo que entra por contrato. **El error que evita:** cuestionarios de 200
preguntas idénticos para el proveedor de café y para el que tiene acceso remoto a producción.

| Campo | Qué escribir |
|---|---|
| **Proveedor y servicio** | Qué hace exactamente |
| **Criticidad** | Alta / media / baja, según **qué pasa si falla o si es comprometido** |
| **Datos a los que accede** | Tipo, volumen, si hay datos personales o de salud |
| **Accesos que tiene** | Remoto, permanente o bajo demanda, con qué privilegios |
| **Concentración** | ¿Hay alternativa? ¿En cuánto tiempo se sustituye? |
| **Evidencia solicitada** | Certificaciones, informes de auditoría, resultados de pruebas, con su **alcance y fecha** |
| **Hallazgos** | Lo que falta o preocupa |
| **Cláusulas exigidas** | Notificación de incidentes con plazo, derecho de auditoría, subencargados, devolución y borrado de datos, niveles de servicio |
| **Riesgo residual y quién lo acepta** | Nombre y cargo del negocio |
| **Fecha de reevaluación** | Y qué la adelanta (un incidente, un cambio de control societario) |

**Regla de proporcionalidad:** la profundidad de la evaluación la fija la criticidad, no el tamaño
del proveedor.

## 10 · Declaración de trabajo para vCISO

**Para qué:** delimitar un encargo externo. **El error que evita:** que la autoridad, la
dedicación y la responsabilidad queden implícitas y se descubran durante una crisis.

```text
DECLARACIÓN DE TRABAJO — SERVICIOS DE DIRECCIÓN DE SEGURIDAD (vCISO)

1. PARTES Y VIGENCIA
   Cliente: [___]   Prestador: [___]   Del [___] al [___]   Modalidad: [virtual/presencial/mixta]
   Tipo de encargo: [fractional / interim / servicio gestionado]

2. FUNCIONES INCLUIDAS
   [Lista cerrada. Ejemplos: estrategia y plan director; registro de riesgos; redacción de
   políticas para aprobación; dirección del comité de seguridad; evaluación de terceros;
   preparación de auditorías; dirección de la respuesta a incidentes graves.]

3. FUNCIONES EXCLUIDAS EXPRESAMENTE
   [Ejemplos: operación de herramientas; soporte a usuarios; auditoría independiente del propio
   trabajo; representación legal.]

4. AUTORIDAD CONCEDIDA
   ¿Puede detener un despliegue?           [Sí / No]  Condiciones: [___]
   ¿Puede vetar la contratación de un proveedor? [Sí / No]  Condiciones: [___]
   ¿Puede aprobar políticas?               [No, propone. Aprueba: ___]
   ¿Puede comprometer gasto?               [Hasta ___ , con visto bueno de ___]

5. QUIÉN DECIDE EN EL CLIENTE
   Aprueba políticas:            [Nombre / Cargo]
   Acepta riesgos residuales:    [Nombre / Cargo]   ← nunca el prestador
   Autoriza gasto:               [Nombre / Cargo]
   Declara un incidente grave:   [Nombre / Cargo]

6. DEDICACIÓN Y DISPONIBILIDAD
   Dedicación pactada: [___ horas/días al mes]   Medición: [___]
   Comités y reuniones fijas: [___]
   Disponibilidad para crisis: [___]  Tarifa y condiciones fuera de dedicación: [___]

7. ACCESOS Y CONFIDENCIALIDAD
   Accesos concedidos: [___]  Controles sobre esos accesos: [___]
   Confidencialidad: [alcance y duración, en ambos sentidos]
   Exclusividad sectorial: [Sí / No]  Alcance: [___]

8. ENTREGABLES Y PERIODICIDAD
   [Registro de riesgos · plan director · actas · informe mensual · evaluación de terceros …]

9. RESPONSABILIDAD Y SEGURO
   Límite de responsabilidad: [___]   Seguro de responsabilidad profesional: [___]

10. TRASPASO Y SALIDA
    Contenido del paquete de traspaso: [___]
    Plazo de preaviso: [___]
    Cláusula de salida si las recomendaciones críticas se ignoran de forma reiterada: [___]

11. FIRMAS
    Por el cliente: [___]        Por el prestador: [___]
```

## 11 · Formulario de descubrimiento para Field CISO

**Para qué:** entender antes de proponer. **El error que evita:** llegar a la primera reunión con
una demostración de producto en lugar de con preguntas.

```text
SESIÓN DE DESCUBRIMIENTO — [Cliente] — [Fecha] — [Asistentes]

DECLARACIÓN DE INTERÉS (se lee en voz alta al empezar)
  "Trabajo para [proveedor], que vende [tipo de solución]. Lo que les traiga puede estar sesgado
   por eso. En el documento voy a separar hechos, hipótesis, opinión y propuesta comercial."

A. EL NEGOCIO
   1. ¿De qué servicio digital depende más el ingreso?
   2. ¿Cuál es la ventana del año en que una caída duele más y cuánto cuesta una hora?
   3. ¿Qué proyecto se juega la organización este año?

B. LA OBLIGACIÓN
   4. ¿Qué regulador o contrato les impone requisitos de seguridad? ¿Quién los firma?
   5. ¿Qué auditoría o certificación tienen encima en los próximos doce meses?
   6. ¿Han tenido que reportar un incidente? ¿Cómo fue?

C. EL RIESGO DECLARADO (con sus palabras)
   7. ¿Qué es lo que más les quita el sueño? (anotar literal)
   8. ¿Qué creen que pasaría hoy si les cifraran todo un viernes por la noche?
   9. ¿Qué han intentado y no funcionó?

D. LA REALIDAD OPERATIVA
   10. ¿Cuántas personas tiene el equipo y en qué se les va el día?
   11. ¿Qué está externalizado y bajo qué acuerdo de servicio?
   12. ¿Cuándo fue la última prueba de restauración y qué resultado dio?

E. LA DECISIÓN
   13. ¿Quién aprueba una compra de este tamaño y con qué criterio?
   14. ¿Qué presupuesto existe y cuándo se define?
   15. ¿Qué tendría que ser cierto para que dijeran que no?

CIERRE
   - Resumen devuelto en voz alta, con sus palabras, para confirmar que entendí.
   - Compromiso concreto: qué envío, cuándo y qué necesito de ustedes.
```

## 12 · Informe y paquete de confianza de producto

**Para qué:** responder de una vez y bien a lo que preguntan todos los clientes. **El error que
evita:** un folleto que solo dice cosas buenas.

| Sección | Qué contiene |
|---|---|
| **Descripción del producto** | Qué hace, para quién, en qué modalidad |
| **Arquitectura y alojamiento** | Dónde se ejecuta, regiones, proveedor de infraestructura |
| **Datos** | Qué se recoge, con qué fin, cuánto se conserva, cómo se borra |
| **Aislamiento entre clientes** | **Cómo se consigue exactamente**, no «se garantiza» |
| **Cifrado** | En tránsito y en reposo; dónde están las claves y quién puede usarlas |
| **Identidad y accesos** | Autenticación, roles, acceso del personal del proveedor y su registro |
| **Ciclo de desarrollo** | Análisis, revisión, modelado de amenazas, criterios de publicación |
| **Cadena de suministro** | Dependencias, SBOM, política de componentes |
| **Registro y trazabilidad** | Qué queda registrado, cuánto tiempo y qué ve el cliente |
| **Continuidad** | RTO y RPO **del servicio**, con la fecha de la última prueba |
| **Respuesta a incidentes** | Cómo y en qué plazo se avisa al cliente |
| **Divulgación de vulnerabilidades** | Canal, plazos, política, crédito |
| **Certificaciones** | Cuáles, con **el alcance exacto** y la fecha del informe |
| **Subencargados** | Lista y qué hace cada uno |
| **Responsabilidad compartida** | Qué protege el producto y **qué debe hacer el cliente** |
| **Lo que el producto NO hace** | Al menos tres afirmaciones negativas verificables |

## 13 · Inventario de sistemas de IA

**Para qué:** el primer entregable de cualquier programa de gobierno de IA. **El error que evita:**
discutir política de IA sin saber cuántos sistemas hay.

| Campo | Qué escribir |
|---|---|
| **ID y nombre** | Identificador estable |
| **Propósito** | Qué decisión o tarea apoya, en lenguaje de negocio |
| **Dueño de negocio** | Nombre y cargo. Sin esto, el sistema no debería estar en producción |
| **Tipo** | Clasificación, generación, recuperación aumentada, agente con herramientas |
| **Proveedor y modelo** | Propio, de terceros, versión y quién controla los cambios |
| **Datos de entrada** | Qué entra, incluidos datos personales o sujetos a contrato |
| **Datos de entrenamiento o ajuste** | Origen, base para usarlos, quién los aprobó |
| **Autonomía** | ¿Recomienda o actúa? ¿Qué acciones puede ejecutar? ¿Cuáles son irreversibles? |
| **Personas afectadas** | ¿Decide sobre clientes, empleados o pacientes? |
| **Criticidad** | Según impacto si se equivoca o es manipulado |
| **Controles** | Validación de entrada y salida, límites, registro, aprobación humana |
| **Estado de evaluación** | Fecha, resultado, condiciones impuestas |
| **Fecha de reevaluación** | Y qué la adelanta (cambio de modelo, de proveedor o de uso) |
| **Cómo se descubrió** | Declarado por el equipo, hallado en la factura, detectado en la red… |

> La columna **«cómo se descubrió»** es la más informativa del inventario: dice cuánto de tu
> organización está fuera de tu vista.

## 14 · Registro de riesgos de IA

**Para qué:** caracterizar el riesgo de IA con escenarios comprobables. **El error que evita:**
registros llenos de categorías abstractas («sesgo», «alucinación») que no permiten decidir nada.

| Campo | Qué escribir |
|---|---|
| **ID y sistema** | Enlaza con el inventario |
| **Escenario concreto** | «Un usuario introduce en el chat un documento con instrucciones ocultas y el asistente revela el contenido de otro caso» — **no** «riesgo de inyección» |
| **Categoría** | Manipulación de entrada, fuga de datos, envenenamiento, extracción de modelo, uso indebido, error con impacto en personas, dependencia del proveedor |
| **Cómo se comprobaría** | La prueba que confirmaría que el escenario es posible |
| **Impacto** | En personas, dinero, obligación legal o confianza |
| **Controles existentes** | Y su eficacia observada, no la prometida |
| **Riesgo residual** | Después de los controles |
| **Tratamiento** | Incluido «no desplegar» como opción legítima |
| **Dueño del riesgo** | **Del negocio**, no de datos ni de seguridad |
| **Condiciones de despliegue** | Qué debe cumplirse para que el sistema siga en producción |
| **Vigilancia** | Qué se mide en continuo y qué umbral obliga a revisar |

## 15 · Roadmap de seguridad OT

**Para qué:** planificar en un entorno donde solo hay una ventana de intervención al año. **El
error que evita:** planes de TI trasplantados a una planta.

| Campo | Qué escribir |
|---|---|
| **Iniciativa** | Qué se hace |
| **Zona afectada** | Corporativa, supervisión, control, seguridad de proceso, campo |
| **Riesgo que reduce** | Enlazado al registro de riesgos OT |
| **¿Requiere parada?** | Sí / No. Si sí, **en qué parada programada entra** |
| **Impacto potencial en el proceso** | Qué podría salir mal al implantarlo |
| **Revisión con seguridad de proceso** | Fecha, participantes y conclusión. **Obligatoria** si toca la zona de control |
| **Acuerdo con Operaciones** | Quién lo firmó y cuándo |
| **Coste y origen del presupuesto** | Seguridad, mantenimiento o proyecto industrial |
| **Control compensatorio mientras tanto** | Qué protege hasta que la iniciativa se ejecute |
| **Criterio de verificación** | Cómo se comprueba que quedó bien, sin interrumpir el proceso |
| **Plan de reversión** | Cómo se deshace si algo falla en la ventana |

> **Regla dura:** ninguna iniciativa que pueda interferir con una función instrumentada de
> seguridad entra en el roadmap sin la revisión conjunta con seguridad de proceso, y si queda
> duda razonable, no entra.

## 🔗 Relacionado

- 🧪 [Laboratorio ejecutivo CISO](README.md)
- 🏢 [Organizaciones ficticias](ORGANIZACIONES.md)
- 🎓 [Evaluación del ecosistema CISO](EVALUACION.md)
- 🗂️ [El ecosistema CISO](../../rutas/ecosistema-ciso.md)
