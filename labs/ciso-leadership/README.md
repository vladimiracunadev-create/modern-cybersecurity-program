# 🎩 Laboratorio ejecutivo CISO

Catorce escenarios de **dirección de seguridad** sobre organizaciones ficticias, con plantillas
reutilizables, rúbricas y criterios de aceptación. Es el laboratorio del
[ecosistema CISO](../../rutas/ecosistema-ciso.md): aquí se practica lo que no se practica en una
consola —decidir, priorizar, defender un presupuesto, dirigir una crisis, aceptar o rechazar un
riesgo y comunicarlo a quien tiene que decidir—.

> 🧯 **Este laboratorio no tiene Docker y no ataca nada.** Es el único del repositorio que no
> levanta contenedores: su material de trabajo son documentos, decisiones y conversaciones. Todo
> lo que se practica aquí es **no ofensivo** y se realiza sobre organizaciones inventadas.

## 🎯 Para quién es

| Ruta | Escenarios propios | Escenarios que también le sirven |
|---|---|---|
| [🎩 CISO](../../rutas/ciso.md) | 1 · 2 · 3 · 4 · 5 · 6 · 7 | Todos: es la ruta que los recorre enteros |
| [🛰️ Field CISO / Customer CISO](../../rutas/field-ciso.md) | 8 · 9 | 1 · 2 · 6 |
| [🧾 vCISO / Fractional / Interim](../../rutas/vciso.md) | 10 | 2 · 3 · 4 · 5 · 6 · 7 |
| [🔗 BISO](../../rutas/biso.md) | 11 | 2 · 5 · 6 |
| [📦 Product CISO](../../rutas/product-ciso.md) | 12 | 6 · 9 |
| [🤖 AI CISO](../../rutas/ai-ciso.md) | 13 | 2 · 6 |
| [🏭 OT CISO](../../rutas/ot-ciso.md) | 14 | 5 · 6 |
| [👔 Jefe de Seguridad](../../rutas/ciso-jefe-seguridad.md) · [🏢 Jefe de Infraestructura](../../rutas/jefe-infraestructura-ciberseguridad.md) | — | 1 · 2 · 3 · 4 · 5 · 6 · 7 |
| [🏛️ GRC](../../rutas/grc.md) | — | 1 · 2 · 6 · 11 |

## 🧰 Qué necesitas

- Un procesador de texto o un editor de Markdown. Nada más.
- Los [datos de las organizaciones ficticias](ORGANIZACIONES.md).
- Las [quince plantillas](PLANTILLAS.md).
- Tiempo: cada escenario está dimensionado entre 60 y 180 minutos.

## 🚦 Cómo se trabaja

1. **Lee la organización completa** antes del escenario. La mitad de los errores vienen de no
   haber leído el contexto.
2. **Declara tus supuestos.** Si falta un dato, invéntalo, márcalo como supuesto y sigue. Un
   entregable sin supuestos declarados no se puede discutir.
3. **Usa la plantilla que corresponde.** Están para eso, y las rúbricas evalúan que las hayas
   completado de verdad, no que las hayas copiado.
4. **Autoevalúate con la rúbrica antes de mirar el ejemplo de referencia.** El ejemplo está
   plegado a propósito.
5. **Guarda el entregable.** Casi todos sirven de evidencia de portafolio y de insumo del
   [examen final de tu rol](../../docs/examen-final-por-rol.md).

### Escala común de las rúbricas

Cada escenario se puntúa sobre **100**, repartidos entre cuatro criterios. La misma escala en
todos:

| Nivel | Puntos del criterio | Qué significa |
|---|---|---|
| **Ausente** | 0 % | No está |
| **Insuficiente** | 25 % | Está, pero no sostiene una decisión |
| **Aceptable** | 60 % | Serviría en una organización real con retoques |
| **Sólido** | 85 % | Se puede presentar tal cual |
| **Ejemplar** | 100 % | Además anticipa la objeción y la responde |

**Aprobado: 70 puntos**, siempre que se cumpla el **criterio de aceptación** del escenario. El
criterio de aceptación no es negociable: si falla, el escenario está suspenso aunque la suma dé
90.

## 📋 Catálogo de escenarios

| # | Escenario | Organización | Ruta principal | Duración |
|---|---|---|---|---|
| 1 | [Informe ejecutivo de una página para el directorio](#1--informe-ejecutivo-de-una-página-para-el-directorio) | Andes Retail | CISO | 90 min |
| 2 | [Registro de riesgos con dueños y riesgo residual](#2--registro-de-riesgos-con-dueños-y-riesgo-residual) | Andes Retail | CISO | 150 min |
| 3 | [Plan director de seguridad a tres años](#3--plan-director-de-seguridad-a-tres-años) | Andes Retail | CISO | 180 min |
| 4 | [Defender un presupuesto limitado](#4--defender-un-presupuesto-limitado) | Andes Retail | CISO | 120 min |
| 5 | [Dirigir un ejercicio de mesa de ransomware](#5--dirigir-un-ejercicio-de-mesa-de-ransomware) | Andes Retail | CISO | 150 min |
| 6 | [Gestionar un proveedor crítico](#6--gestionar-un-proveedor-crítico) | Andes Retail | CISO | 120 min |
| 7 | [Plan de 90 días](#7--plan-de-90-días) | Clínica Los Cipreses | CISO | 90 min |
| 8 | [Sesión de descubrimiento como Field CISO](#8--sesión-de-descubrimiento-como-field-ciso) | Cumbre → Andes | Field CISO | 90 min |
| 9 | [Recomendación técnico-comercial transparente](#9--recomendación-técnico-comercial-transparente) | Cumbre → Andes | Field CISO | 120 min |
| 10 | [Alcance contractual de un vCISO](#10--alcance-contractual-de-un-vciso) | Clínica Los Cipreses | vCISO | 120 min |
| 11 | [Roadmap de seguridad de una unidad de negocio](#11--roadmap-de-seguridad-de-una-unidad-de-negocio) | Andes Retail | BISO | 150 min |
| 12 | [Paquete de confianza de producto](#12--paquete-de-confianza-de-producto) | NovaPay | Product CISO | 150 min |
| 13 | [Inventario y registro de riesgos de IA](#13--inventario-y-registro-de-riesgos-de-ia) | Andes Retail | AI CISO | 150 min |
| 14 | [Incidente OT con continuidad y seguridad de las personas](#14--incidente-ot-con-continuidad-y-seguridad-de-las-personas) | Minera Alto Cobre | OT CISO | 180 min |

## 1 · Informe ejecutivo de una página para el directorio

**Contexto.** Eres el CISO de *Andes Retail*. El Comité de Auditoría se reúne en dos semanas.
Tienes quince minutos y una página. Nadie en esa sala es técnico.

**Datos de entrada.** [Andes Retail](ORGANIZACIONES.md#-andes-retail), completa. Presta atención
al perfil NIST CSF, a los 312 críticos abiertos, a la prueba de restauración de hace dos años, a
la cobertura de autenticación multifactor y a la renovación del seguro.

**Instrucciones.**

1. Elige **las dos decisiones** que el comité debe tomar en esa sesión. Solo dos.
2. Rellena la [plantilla 5 · Informe ejecutivo](PLANTILLAS.md#5--informe-ejecutivo-de-una-página).
3. Elige **cuatro** indicadores de la [plantilla 4](PLANTILLAS.md#4--cuadro-de-kpi-y-kri) y
   justifica cada uno con la decisión que dispara.
4. Escribe la sección «lo que no estamos haciendo y por qué» sin suavizarla.
5. Completa un [RACI](PLANTILLAS.md#1--raci) de tres filas: aprobar la política, aceptar un riesgo
   residual y declarar un incidente grave.

**Entregable esperado.** Una página (informe) + un cuadro de cuatro indicadores + un RACI de tres
filas.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Las dos decisiones están formuladas con plazo, coste y consecuencia de no decidir | 30 |
| El texto es comprensible para un lector sin formación técnica; toda sigla se define | 25 |
| Los cuatro indicadores tienen una decisión asociada, no son decorativos | 25 |
| La sección «lo que no estamos haciendo» es honesta y concreta | 20 |

**Criterio de aceptación.** Dáselo a leer a alguien sin formación técnica. Al terminar debe poder
decirte, sin ayuda, **qué dos cosas tiene que decidir el comité**. Si no puede, no está aprobado.

<details>
<summary>Ejemplo de referencia</summary>

Un informe sólido para este caso elige como decisiones **(a) aprobar la prueba de restauración
completa con copias inmutables antes de la temporada alta** —porque es la brecha que la
aseguradora exige y la que convierte un ransomware en una parada de días— y **(b) cerrar la
cobertura de autenticación multifactor en tiendas y cuentas de servicio**, que es el 39 % de
usuarios sin proteger y el vector más usado.

Los cuatro indicadores: cobertura de MFA (dispara la decisión b), antigüedad de la vulnerabilidad
crítica más antigua (dispara la conversación de capacidad del equipo), fecha de la última prueba
de restauración superada (dispara la decisión a) y proveedores críticos evaluados (dispara el
escenario 6).

La sección honesta dice, en una frase: *«No tenemos monitoreo fuera del horario laboral. Un
ataque que empiece un viernes a las 20:00 se detectará el lunes.»* Eso es un hecho del contexto,
no una opinión, y es exactamente lo que un comité necesita saber.

El RACI: la **A** de «aceptar un riesgo residual» es del Gerente de la unidad afectada, **nunca**
del CISO. La **A** de «declarar un incidente grave» conviene que sea del CEO o de un rol de
guardia designado, no de quien está resolviendo el incidente.

</details>

**Límites éticos y legales.** No inventes cifras de pérdida sin declarar el supuesto que las
sostiene. No presentes una estimación como un dato medido. Un informe al directorio que exagera
para conseguir presupuesto destruye la credibilidad del cargo la primera vez que se comprueba.

## 2 · Registro de riesgos con dueños y riesgo residual

**Contexto.** El Comité de Auditoría te pidió «el mapa de riesgos». Hasta ahora existe una hoja
de cálculo con 47 filas técnicas sin dueño ni fecha.

**Datos de entrada.** [Andes Retail](ORGANIZACIONES.md#-andes-retail), completa.

**Instrucciones.**

1. Construye **diez riesgos** con la [plantilla 2](PLANTILLAS.md#2--registro-de-riesgos).
2. Cada escenario de riesgo debe tener **causa, evento y consecuencia** en una sola frase.
3. Cuantifica el impacto de al menos cuatro de ellos, declarando los supuestos.
4. Asigna a cada riesgo un **dueño con nombre y cargo del negocio**. No vale «TI» ni «Seguridad».
5. Decide el tratamiento. **Al menos uno debe ser «aceptar»**, y para ese redacta el
   [acta de aceptación](PLANTILLAS.md#3--aceptación-formal-de-riesgo) completa.
6. Ordena la lista por riesgo residual y explica en tres líneas por qué ese orden y no otro.

**Entregable esperado.** Registro de diez riesgos + un acta de aceptación firmada (con firmas
ficticias identificadas como tales).

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Los escenarios tienen causa, evento y consecuencia, y son comprobables | 30 |
| Todos los riesgos tienen dueño de negocio con nombre y cargo | 25 |
| La cuantificación declara sus supuestos y es defendible | 20 |
| El acta de aceptación está completa, con vigencia, condiciones y firmas correctas | 25 |

**Criterio de aceptación.** **Ningún riesgo puede figurar aceptado por el CISO ni por el área de
seguridad.** Un solo caso invalida el escenario.

<details>
<summary>Ejemplo de referencia</summary>

Un mal escenario de riesgo: *«Vulnerabilidades sin parchear.»* No tiene causa, ni evento, ni
consecuencia, ni permite estimar nada.

Un buen escenario: *«El proveedor RapidPOS mantiene acceso remoto permanente a las 78 tiendas con
una cuenta compartida y sin registro de sesiones; si esa cuenta se compromete, un atacante puede
desplegar código en todos los puntos de venta a la vez y detener la venta presencial durante días,
con un impacto estimado en [X] por día según el supuesto de que la venta presencial representa el
69 % del ingreso.»*

El riesgo aceptable de este contexto suele ser el de los sistemas de las tiendas más antiguas: el
coste de renovarlos supera el impacto estimado dentro del horizonte del plan. Se acepta, con
vigencia de doce meses, con control compensatorio (segmentación de la red de tienda) y con la
firma del Gerente de Operaciones. Se acepta **porque él responde por la operación de tiendas**, no
porque seguridad lo consienta.

</details>

**Límites éticos y legales.** Un registro de riesgos es un documento que puede pedirse en una
auditoría o en un litigio. No escribas en él nada que no puedas sostener, y no lo uses para dejar
constancia de culpas: se registran riesgos, no personas.

## 3 · Plan director de seguridad a tres años

**Contexto.** Tienes el registro de riesgos del escenario 2 y la evaluación contra NIST CSF. La
gerencia pide un plan «que se entienda y que se pueda pagar».

**Datos de entrada.** [Andes Retail](ORGANIZACIONES.md#-andes-retail) y tu propio registro de
riesgos del escenario 2.

**Instrucciones.**

1. Fija el **perfil objetivo** por función de NIST CSF a 12, 24 y 36 meses. No pongas «alto» en
   todas: justifica por qué unas suben antes que otras.
2. Define entre ocho y doce **iniciativas**, cada una con: riesgo que reduce, entregable, dueño,
   coste estimado, dependencia y trimestre.
3. Construye la **hoja de ruta** por trimestres, respetando que el 68 % del presupuesto ya está
   comprometido.
4. Rellena la [plantilla 7 · BIA](PLANTILLAS.md#7--análisis-de-impacto-al-negocio-bia-con-rto-y-rpo)
   para el canal digital y para el punto de venta, con RTO y RPO **acordados** y la brecha frente
   a lo medido.
5. Escribe explícitamente **qué no se hará** en estos tres años y qué riesgo queda vivo por ello.

**Entregable esperado.** Plan director (perfil objetivo + iniciativas + hoja de ruta) + dos fichas
de BIA + la lista de lo que queda fuera.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Cada iniciativa está trazada a un riesgo del registro | 30 |
| La secuencia es defendible: las dependencias y la capacidad del equipo se respetan | 25 |
| El BIA tiene RTO y RPO acordados con el negocio y la brecha está cuantificada | 25 |
| La lista de lo que no se hará es explícita y su riesgo está asumido por alguien | 20 |

**Criterio de aceptación.** El plan debe caber en el equipo y en el presupuesto declarados. Si
propones doce iniciativas simultáneas para un equipo de seis personas con el 68 % del presupuesto
comprometido, el plan es una carta a los Reyes Magos y no está aprobado.

<details>
<summary>Ejemplo de referencia</summary>

El orden que suele resistir el escrutinio en este contexto: **primero lo que evita la catástrofe**
(restauración probada y copias inmutables; cierre de MFA; control del acceso del proveedor de
punto de venta), **después lo que da visibilidad** (inventario, telemetría, extensión del
monitoreo a 24 × 7), **y solo entonces lo que da madurez** (gobierno formal, SGSI, certificación).

Poner la certificación en el año uno es el error clásico: consume el presupuesto y la atención del
equipo, y no reduce el riesgo que hoy puede detener la compañía.

El BIA del canal digital: RTO acordado con la Gerencia Digital, RPO acordado, y la brecha honesta
—«no tenemos RTO medido porque nunca se ha probado»— que a su vez justifica la primera iniciativa.

</details>

**Límites éticos y legales.** No prometas «cumplimiento» de una norma como resultado de una
iniciativa si no has verificado el alcance y quién lo certifica. No comprometas fechas que
dependen de terceros sin haberlo hablado con ellos.

## 4 · Defender un presupuesto limitado

**Contexto.** La gerencia recorta: en lugar del incremento que pediste, te ofrecen mantener el
presupuesto actual. Tienes cinco minutos ante el comité.

**Datos de entrada.** [Andes Retail](ORGANIZACIONES.md#-andes-retail) y tu plan director del
escenario 3.

**Instrucciones.**

1. Construye tres escenarios presupuestarios: **actual**, **actual + 20 %** y **actual − 15 %**.
2. Para cada uno: qué se hace, qué no se hace y **qué riesgo queda vivo**, con su dueño.
3. Elige un riesgo y presenta el caso económico: coste del control frente a pérdida esperada, con
   los supuestos a la vista y el rango de incertidumbre.
4. Prepara la respuesta a las tres objeciones que te van a hacer: «nunca nos ha pasado», «el
   seguro lo cubre» y «el proveedor ya se encarga».
5. Escribe el guion de cinco minutos. Cronométralo.

**Entregable esperado.** Tabla de tres escenarios + un caso económico + el guion cronometrado.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Los tres escenarios muestran consecuencias, no solo cifras | 25 |
| El caso económico declara supuestos y reconoce su incertidumbre | 30 |
| Las tres objeciones están respondidas con hechos del contexto | 25 |
| El guion cabe en cinco minutos y termina pidiendo una decisión concreta | 20 |

**Criterio de aceptación.** El escenario de recorte debe presentar **qué riesgo queda vivo y quién
lo acepta**, con nombre. Un recorte sin dueño del riesgo resultante no es una defensa de
presupuesto: es una rendición.

<details>
<summary>Ejemplo de referencia</summary>

La respuesta a «el seguro lo cubre» es la más instructiva: en este contexto la aseguradora **ya ha
pedido** evidencia de MFA, copias inmutables y formación como condición de renovación. Es decir:
el seguro no cubre lo que no se controla, y la póliza es una razón adicional para invertir, no una
alternativa a hacerlo. Ese es un hecho del contexto, no una opinión, y por eso funciona.

Sobre la incertidumbre: presentar «la pérdida esperada es de 2,3 millones» es débil. Presentar «con
los supuestos A, B y C, la pérdida esperada está entre 1,1 y 4,0 millones; el control cuesta 180
mil y reduce la probabilidad del escenario a la mitad» es defendible, porque muestra el trabajo y
admite lo que no se sabe.

</details>

**Límites éticos y legales.** No uses el miedo como técnica: exagerar una probabilidad para
conseguir presupuesto es una falta profesional y, además, funciona una sola vez. No cites cifras
de incidentes ajenos sin fuente y sin fecha.

## 5 · Dirigir un ejercicio de mesa de ransomware

**Contexto.** Diriges tú el ejercicio. En la sala: gerencia, TI, legal, comunicaciones y recursos
humanos. Nadie ha hecho esto antes en la organización.

**Datos de entrada.** [Andes Retail](ORGANIZACIONES.md#-andes-retail). Situación inicial: viernes,
21:40. El sistema de punto de venta de 41 tiendas deja de responder. El proveedor *RapidPOS* no
contesta el teléfono de guardia.

**Instrucciones.**

1. Escribe el guion completo con la
   [plantilla 8](PLANTILLAS.md#8--guion-de-ejercicio-de-mesa-tabletop): cinco inyectos con reloj.
2. Al menos un inyecto debe forzar la decisión de **detener o no** el canal digital, y otro debe
   introducir el **punto de decisión de notificar a la autoridad**.
3. Prepara el [RACI](PLANTILLAS.md#1--raci) de crisis antes del ejercicio, incluida la fila del
   pago de un rescate.
4. Dirige el ejercicio (o simúlalo por escrito, respondiendo tú los cinco inyectos con la
   cronología).
5. Cierra con la retrospectiva: tres cosas que funcionaron, tres que no y tres acciones con dueño
   y fecha.
6. Redacta el informe ejecutivo de una página con el resultado.

**Entregable esperado.** Guion + RACI de crisis + cronología de decisiones + retrospectiva +
informe de una página.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Los inyectos aportan información incompleta y presionan con el reloj | 25 |
| El RACI de crisis tiene una sola A por fila y la decisión de pago está asignada fuera de seguridad | 25 |
| La cronología registra cada decisión con hora y con quién la tomó | 25 |
| La retrospectiva produce acciones con dueño y fecha, no conclusiones generales | 25 |

**Criterio de aceptación.** La cronología debe mostrar **quién** tomó cada decisión. Un ejercicio
donde todas las decisiones las toma el CISO no ha ensayado la crisis real: ha ensayado el
monólogo.

<details>
<summary>Ejemplo de referencia</summary>

El inyecto más útil de este escenario es el de T+45: *«Un periodista pregunta en redes sociales por
qué las tiendas de la zona norte no pueden cobrar.»* Fuerza a comunicaciones y a legal a decidir
qué se dice **antes** de saber qué pasó, que es exactamente la situación real.

Sobre el pago del rescate: la fila del RACI debe tener la **A** en el CEO o en el directorio, con
legal como **C** obligatorio. Colocar esa A en el CISO es uno de los errores más frecuentes y más
graves del ejercicio: no es una decisión técnica.

Sobre la notificación: el guion no debe preguntar «¿hay que notificar?», sino **«¿quién decide si
esto cumple el umbral de notificación, con qué información y en qué plazo?»**. La segunda pregunta
revela si el procedimiento existe.

</details>

**Límites éticos y legales.** Un ejercicio de mesa no busca culpables: si se convierte en eso,
nadie volverá a contar lo que de verdad pasa. Sobre el pago de rescates, no formules
recomendaciones legales: registra que la decisión requiere asesoría legal y que puede tener
implicaciones que exceden a la organización.

## 6 · Gestionar un proveedor crítico

**Contexto.** *RapidPOS* tiene acceso remoto permanente a las 78 tiendas con una cuenta compartida
y sin registro de sesiones. El contrato se renueva en cinco meses. Cambiar de proveedor tomaría,
según Operaciones, entre nueve y catorce meses.

**Datos de entrada.** [Andes Retail](ORGANIZACIONES.md#-andes-retail).

**Instrucciones.**

1. Completa la [plantilla 9 · Evaluación de terceros](PLANTILLAS.md#9--evaluación-de-terceros).
2. Evalúa la **concentración**: qué pasa si el proveedor desaparece, sube el precio o sufre un
   incidente.
3. Define las cláusulas mínimas que exigirás en la renovación, con plazos concretos de
   notificación de incidentes.
4. Diseña el **control compensatorio** que se implanta ya, sin esperar a la renovación.
5. Redacta la **posición de negociación**: qué es irrenunciable, qué es negociable y cuál es tu
   alternativa si dicen que no.
6. Registra el riesgo residual y consigue que lo acepte quien corresponde.

**Entregable esperado.** Evaluación del proveedor + cláusulas exigidas + control compensatorio +
posición de negociación + entrada en el registro de riesgos.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| La evaluación es proporcional a la criticidad y no un cuestionario genérico | 25 |
| El control compensatorio es implantable ya y reduce el riesgo de forma verificable | 30 |
| Las cláusulas son concretas: plazos, alcance, evidencia y consecuencias | 25 |
| La posición de negociación reconoce la asimetría real y propone una alternativa | 20 |

**Criterio de aceptación.** El control compensatorio debe poder implantarse **sin la cooperación
del proveedor**. Si tu única medida depende de que el proveedor acepte, no has gestionado el
riesgo: lo has delegado en quien lo causa.

<details>
<summary>Ejemplo de referencia</summary>

El control compensatorio que funciona aquí no requiere permiso de nadie: **mediar el acceso**. En
lugar de que el proveedor entre directo a las tiendas, se le hace pasar por un punto de salto
controlado por Andes, con cuenta nominal por técnico, autenticación multifactor, ventana horaria y
grabación de sesión. El proveedor conserva su capacidad de dar servicio; Andes recupera la
trazabilidad. Se puede implantar en semanas.

Sobre la asimetría: reconocerla mejora la negociación. «Sabemos que cambiar de proveedor nos
tomaría más de un año, así que no vamos a amenazar con eso. Lo que sí vamos a hacer es mediar el
acceso desde nuestro lado, y lo que les pedimos es que sus técnicos usen cuentas nominales.» Es
una posición honesta y difícil de rechazar.

</details>

**Límites éticos y legales.** No exijas al proveedor evidencia que tú no serías capaz de entregar.
No difundas los hallazgos de una evaluación de terceros fuera de quien los necesita: son
información sensible del proveedor.

## 7 · Plan de 90 días

**Contexto.** Acabas de ser contratado como responsable de seguridad de *Clínica Los Cipreses*.
El directorio pidió «un plan de ciberseguridad» hace seis meses y nadie lo ha escrito. Es tu
primer día.

**Datos de entrada.** [Clínica Los Cipreses](ORGANIZACIONES.md#-clínica-los-cipreses).

**Instrucciones.**

1. Completa la [plantilla 6 · Plan de 30/60/90](PLANTILLAS.md#6--plan-de-306090-días).
2. Elige **una** mejora visible que puedas entregar en los primeros 30 días con lo que ya existe.
3. Identifica las cinco conversaciones que tienes que tener en la primera semana y con quién.
4. Define qué gobierno propones: qué comité, cada cuánto, quién asiste y qué decide.
5. Escribe qué **no** vas a hacer en 90 días y por qué, para que nadie lo espere.

**Entregable esperado.** Plan de 30/60/90 + la mejora rápida + el mapa de conversaciones + la
propuesta de gobierno.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Los primeros 30 días priorizan entender por encima de cambiar | 25 |
| La mejora rápida es real, barata y no requiere presupuesto nuevo | 25 |
| La propuesta de gobierno define **quién decide qué**, no solo quién se reúne | 30 |
| Las expectativas están gestionadas: lo que no se hará está dicho | 20 |

**Criterio de aceptación.** El plan debe terminar en el día 90 con **una decisión pedida a la
dirección**, no con un diagnóstico. Un plan de 90 días que acaba en un informe no ha conseguido
mandato.

<details>
<summary>Ejemplo de referencia</summary>

La mejora rápida evidente en este contexto: **desactivar los 31 accesos de personas que ya no
trabajan en la clínica**. No cuesta dinero, se hace en días, reduce riesgo real y demuestra a la
organización que la nueva función produce resultados. Es el tipo de victoria que compra permiso
para las conversaciones difíciles del mes dos.

Las cinco conversaciones: Dirección Médica (porque sin ella no hay nada), Jefe de Informática
(porque es quien lo sostiene todo y puede vivir tu llegada como una amenaza), Finanzas (el
presupuesto y el contrato de la ficha clínica), Calidad o Cumplimiento (las obligaciones reales) y
un jefe de servicio clínico (para entender qué pasa si un sistema no está disponible a las tres de
la mañana).

Lo que **no** se hará: la segmentación completa de la red no cabe en 90 días. Decirlo el primer mes
evita que en el día 89 alguien pregunte por qué no está hecha.

</details>

**Límites éticos y legales.** En salud, la disponibilidad de un sistema clínico puede afectar a la
atención de pacientes. Ninguna medida de seguridad de este plan puede introducirse sin evaluar su
efecto sobre la asistencia, y esa evaluación la hace la Dirección Médica, no tú.

## 8 · Sesión de descubrimiento como Field CISO

**Contexto.** Trabajas en la Oficina del CISO de *Cumbre Security*. Tienes la primera reunión con
el CISO de *Andes Retail*, una cuenta objetivo. Comercial quiere que lleves una demostración del
producto. Tú tienes noventa minutos y una sola oportunidad de que te vuelvan a recibir.

**Datos de entrada.** [Cumbre Security](ORGANIZACIONES.md#-cumbre-security) y lo que es **público**
de [Andes Retail](ORGANIZACIONES.md#-andes-retail): sector, tamaño, canal digital, presencia
regional. Los datos internos de Andes **todavía no los conoces**: solo puedes usar los que
obtengas preguntando.

**Instrucciones.**

1. Prepara la reunión: qué lees antes y qué tres hipótesis llevas.
2. Adapta la [plantilla 11 · Formulario de descubrimiento](PLANTILLAS.md#11--formulario-de-descubrimiento-para-field-ciso)
   a este cliente concreto.
3. Redacta la **declaración de interés** que vas a leer al empezar, con tus palabras.
4. Simula la sesión por escrito: pregunta, respuesta plausible del cliente y **la repregunta**.
   La repregunta es donde se ve el oficio.
5. Escribe el acta con las respuestas **en las palabras del cliente**, separando lo que te dijeron
   de lo que tú infieres.
6. Cierra con un compromiso concreto: qué envías, cuándo y qué necesitas de ellos.

**Entregable esperado.** Preparación + formulario adaptado + declaración de interés + transcripción
simulada + acta + compromiso de cierre.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| La declaración de interés es explícita y se hace al inicio, no al final | 25 |
| Las preguntas van al negocio y a la obligación, no al producto | 30 |
| El acta separa lo dicho por el cliente de lo inferido por ti | 25 |
| El compromiso de cierre es concreto y no es «te mando una propuesta» | 20 |

**Criterio de aceptación.** En toda la sesión **no puede aparecer el producto de Cumbre**. Si
aparece, no es una sesión de descubrimiento: es una demostración con preguntas de cortesía.

<details>
<summary>Ejemplo de referencia</summary>

La pregunta que más rendimiento da en este contexto es la 12 del formulario: *«¿Cuándo fue la
última prueba de restauración y qué resultado dio?»* Es concreta, no acusatoria, y la respuesta
—«hace dos años, y no se documentó»— abre la conversación que de verdad importa para Andes, aunque
no lleve a vender nada de Cumbre.

La repregunta que separa a un asesor de un vendedor: cuando el cliente dice «lo que más me quita
el sueño es el ransomware», la mala respuesta es hablar de detección. La buena es: *«¿Qué crees que
pasaría exactamente el lunes por la mañana? Cuéntame el orden en que intentarían levantar las
cosas.»* Ahí es donde el cliente descubre, solo, dónde está su problema.

</details>

**Límites éticos y legales.** No uses información de otros clientes de Cumbre, ni siquiera
anonimizada, si el cliente es reconocible por el sector y el tamaño. No pidas datos que no
necesitas para asesorar: cuanta más información sensible del cliente acumules, mayor es tu propia
responsabilidad de custodia.

## 9 · Recomendación técnico-comercial transparente

**Contexto.** Tras el descubrimiento, tienes que entregar tu recomendación a *Andes Retail*. El
mayor riesgo de Andes **no lo resuelve el producto de Cumbre**. Además, tu producto tiene una
limitación conocida con el sistema de punto de venta que Andes usa. Comercial quiere usar los dos
incidentes de ransomware del sector como argumento de urgencia.

**Datos de entrada.** [Cumbre Security](ORGANIZACIONES.md#-cumbre-security) y
[Andes Retail](ORGANIZACIONES.md#-andes-retail), ya completas: ahora conoces lo interno.

**Instrucciones.**

1. Redacta la recomendación separando y **etiquetando** cuatro tipos de contenido:
   **hecho observado**, **hipótesis**, **opinión profesional** y **propuesta del proveedor**.
2. Presenta **tres opciones**, una de ellas explícitamente **sin producto de Cumbre**.
3. Declara la limitación conocida de tu producto con el punto de venta de Andes, con su plazo y su
   coste.
4. Decide qué haces con la petición de comercial sobre los incidentes del sector, y escribe la
   respuesta interna que le das.
5. Redacta la nota ejecutiva de una página para el comité de Andes con la
   [plantilla 5](PLANTILLAS.md#5--informe-ejecutivo-de-una-página).
6. Escribe el informe interno de retroalimentación a producto.

**Entregable esperado.** Recomendación etiquetada + tres opciones + declaración de limitación +
respuesta interna a comercial + nota ejecutiva + informe a producto.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Las cuatro etiquetas están presentes y bien aplicadas en todo el documento | 30 |
| La opción sin producto propio está desarrollada en serio, no como coartada | 25 |
| La limitación del producto se declara con plazo y coste, sin eufemismos | 25 |
| La respuesta a comercial sostiene una posición profesional y ofrece alternativa | 20 |

**Criterio de aceptación.** Entrega el documento a alguien que **no sepa para quién trabajas**.
Debe poder señalar, sin ayuda, qué párrafos son hechos y cuáles son propuesta comercial. Si no
puede, no está aprobado.

<details>
<summary>Ejemplo de referencia</summary>

La estructura que funciona:

> **[HECHO]** La última prueba de restauración completa fue hace 24 meses y no está documentada.
> **[HECHO]** La cobertura de autenticación multifactor es del 61 % y no alcanza a las cuentas de
> servicio ni a los usuarios de tienda.
> **[HIPÓTESIS]** Con esa cobertura y sin restauración probada, un ransomware que entre por la
> cuenta compartida del proveedor de punto de venta produciría una interrupción de más de 72 horas.
> *Lo que refutaría esta hipótesis: una prueba de restauración exitosa cronometrada.*
> **[OPINIÓN PROFESIONAL]** Las dos prioridades de los próximos seis meses deberían ser la
> restauración probada y el cierre de MFA. **Ninguna de las dos requiere comprar nada a Cumbre.**
> **[PROPUESTA DE CUMBRE]** Para el año siguiente, y solo una vez cubierto lo anterior, nuestro
> servicio gestionado 24 × 7 cubriría la brecha de monitoreo nocturno. Coste: [X]. **Limitación
> conocida: no ingiere los registros de RapidPOS sin un desarrollo de seis semanas, que no está
> comprometido en la hoja de ruta.**

La respuesta interna a comercial: *«No voy a usar los incidentes del sector como argumento de
urgencia, porque no conozco sus causas y no puedo afirmar que sean comparables. Sí voy a usar dos
hechos del propio cliente —restauración no probada y MFA incompleta— que son más urgentes y que
además puedo demostrar. Si quieren un argumento de cierre, ese es más fuerte y no nos deja
expuestos.»*

</details>

**Límites éticos y legales.** No presentes esta recomendación como una auditoría ni uses la palabra
«auditoría» para describirla. No cites incidentes de terceros como si conocieras sus causas. Si
comercial insiste en una afirmación que no sostienes, no la firmes.

## 10 · Alcance contractual de un vCISO

**Contexto.** *Clínica Los Cipreses* ha aprobado presupuesto para un vCISO fractional: cuatro días
al mes durante doce meses. Eres tú quien va a prestar el servicio y quien redacta el alcance.

**Datos de entrada.** [Clínica Los Cipreses](ORGANIZACIONES.md#-clínica-los-cipreses).

**Instrucciones.**

1. Completa la [plantilla 10 · Declaración de trabajo](PLANTILLAS.md#10--declaración-de-trabajo-para-vciso)
   entera. Ningún campo en blanco.
2. Dimensiona: reparte los cuatro días al mes entre comité, trabajo de fondo y disponibilidad. Si
   algo no cabe, sácalo del alcance y dilo.
3. Redacta la cláusula de **crisis fuera de dedicación**: qué pasa un sábado con un incidente
   grave.
4. Redacta la cláusula de **salida por recomendaciones ignoradas**.
5. Define el **paquete de traspaso** que entregarás al terminar.
6. Escribe media página dirigida al directorio explicando **qué no compra** con este contrato.

**Entregable esperado.** Declaración de trabajo completa + dimensionamiento + las dos cláusulas +
definición del paquete de traspaso + la media página de expectativas.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Autoridad y decisión están definidas: quién aprueba, quién acepta, quién autoriza gasto | 30 |
| El dimensionamiento es realista y lo que no cabe está excluido explícitamente | 25 |
| Las cláusulas de crisis y de salida son concretas y aplicables | 25 |
| El paquete de traspaso permitiría continuar a otro profesional sin entrevistarte | 20 |

**Criterio de aceptación.** El campo «acepta riesgos residuales» debe estar ocupado por **una
persona de la clínica**, con cargo. Si aparece tu nombre, el escenario está suspenso.

<details>
<summary>Ejemplo de referencia</summary>

El dimensionamiento honesto de cuatro días al mes: **un día** de comité y seguimiento, **dos días**
de trabajo de fondo (riesgos, políticas, evaluación del proveedor de la ficha clínica) y **un día**
repartido en disponibilidad y coordinación. Con eso, en doce meses cabe un ciclo de riesgo, un
conjunto básico de políticas, la evaluación del proveedor crítico, la revisión de accesos y un
ejercicio de mesa. **No cabe** un SGSI certificable, y decirlo por escrito antes de firmar evita el
conflicto del mes nueve.

La cláusula de crisis: *«La dirección de un incidente grave fuera de la dedicación pactada se
factura a [tarifa] con un mínimo de [X] horas, y el prestador se compromete a estar disponible en
un plazo de [Y] horas. Si el cliente prefiere no contratar esa disponibilidad, se documenta como
riesgo aceptado antes de la firma.»* Lo importante no es la tarifa: es que la conversación ocurra
en enero y no durante el incidente.

</details>

**Límites éticos y legales.** Una declaración de trabajo real debe revisarla el área legal de
ambas partes. No prometas por contrato resultados de seguridad («no habrá incidentes»): compromete
actividades y entregables. En salud, cualquier acceso a sistemas con datos de pacientes exige
condiciones específicas que debes acordar antes de recibir el acceso.

## 11 · Roadmap de seguridad de una unidad de negocio

**Contexto.** Eres el primer BISO de *Andes Retail*, asignado a la unidad de **comercio
electrónico**. La Gerencia Digital te recibe con una frase: «espero que no vengas a frenarnos».

**Datos de entrada.** [Andes Retail](ORGANIZACIONES.md#-andes-retail), con foco en el canal
digital (31 % del ingreso, creciendo al 18 %) y en los tres sistemas de IA desplegados sin pasar
por seguridad.

**Instrucciones.**

1. Construye el **perfil de riesgo de la unidad**: ocho riesgos con la
   [plantilla 2](PLANTILLAS.md#2--registro-de-riesgos), cada uno con dueño **dentro de la unidad**.
2. Diseña el **roadmap a doce meses** alineado con el plan corporativo y con el plan comercial de
   la unidad. Indica explícitamente **qué no se hará** este año.
3. Negocia **una excepción**: elige un control corporativo que no cabe en esta unidad, y
   documéntala con control compensatorio, vencimiento y firma.
4. Escribe el mismo mes **dos veces**: una página para la Gerencia Digital y una página para el
   CISO, con los mismos datos.
5. Completa un [RACI](PLANTILLAS.md#1--raci) de cinco filas para la unidad, incluida «aceptar un
   riesgo residual» y «desplegar un sistema de IA».

**Entregable esperado.** Perfil de riesgo + roadmap + excepción documentada + dos informes de una
página + RACI de la unidad.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Los riesgos están expresados en impacto de negocio y tienen dueño en la unidad | 30 |
| El roadmap respeta el plan comercial y dice qué queda fuera | 25 |
| La excepción tiene compensación, vencimiento y firma de quien corresponde | 25 |
| Los dos informes son consistentes entre sí | 20 |

**Criterio de aceptación.** Un lector que vea **los dos informes a la vez** no debe encontrar
ninguna contradicción. Si la encuentra, el escenario demuestra el fallo característico del puesto
—la captura por una de las dos partes— y está suspenso.

<details>
<summary>Ejemplo de referencia</summary>

La diferencia legítima entre los dos informes es de **énfasis y de vocabulario**, nunca de hechos.
Para la Gerencia Digital: *«El despliegue del asistente sin evaluación previa nos expone a que un
cliente reciba datos de otro; lo estamos probando esta semana y, si se confirma, hay que
desactivar la función de resumen hasta corregirla.»* Para el CISO: *«Sistema de IA en producción
sin evaluación previa; riesgo de fuga entre sesiones bajo verificación; propuesta de control
compensatorio y fecha.»* Mismos hechos, mismo riesgo, misma fecha.

Una contradicción típica —y suspensa— sería informar a la unidad de que «el riesgo está controlado»
y al CISO de que «el riesgo es alto». Ocurre cuando el BISO intenta agradar a las dos mesas.

La excepción razonable en este contexto: la política corporativa exige autenticación multifactor
para todo acceso administrativo; el sistema del marketplace de terceros no la soporta hasta su
próxima versión. Compensación: red restringida por origen, cuentas nominales, sesión registrada y
revisión mensual. Vencimiento: seis meses. Firma: Gerente Digital.

</details>

**Límites éticos y legales.** No maquilles el informe hacia arriba ni hacia abajo. Si detectas un
problema que afecta a otra unidad, tu obligación es que el programa central lo sepa, aunque
perjudique a la tuya.

## 12 · Paquete de confianza de producto

**Contexto.** Eres el Product CISO de *NovaPay*. Hay una vulnerabilidad crítica en el componente
que valida las peticiones de liquidación, que afecta a todas las versiones de los últimos 14
meses. Hay mitigación de configuración; la corrección tarda dos semanas. Y encima, ingeniería
sigue gastando el equivalente a 1,3 personas al año respondiendo cuestionarios.

**Datos de entrada.** [NovaPay](ORGANIZACIONES.md#-novapay).

**Instrucciones.**

1. Construye el **paquete de confianza** con la
   [plantilla 12](PLANTILLAS.md#12--informe-y-paquete-de-confianza-de-producto), incluida la
   sección de **lo que el producto no hace**.
2. Escribe los **criterios de puerta de publicación**: qué severidad bloquea, qué mitigación es
   aceptable, quién puede levantar el bloqueo y con qué firma.
3. Redacta la **política de divulgación** publicable: canal, acuse, plazos, crédito.
4. Redacta el **aviso de seguridad** de la vulnerabilidad crítica: versiones afectadas, impacto,
   mitigación temporal, solución y cronología.
5. Escribe la **comunicación a un banco cliente** que pregunta si le afecta, en dos capas: una
   para su equipo de seguridad y un párrafo para su dirección.
6. Redacta la corrección de la afirmación comercial («cumple con los principales estándares
   internacionales»): qué se puede decir y qué no.

**Entregable esperado.** Paquete de confianza, criterios de publicación, política de divulgación,
aviso de seguridad, comunicación al cliente y corrección de la afirmación comercial.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| El paquete describe **cómo** se consigue el aislamiento entre clientes, no que «se garantiza» | 30 |
| El aviso de seguridad es completo, fechado y sin eufemismos | 25 |
| Los criterios de publicación son aplicables y asignan la firma a alguien concreto | 25 |
| La política de divulgación es publicable tal cual | 20 |

**Criterio de aceptación.** El paquete debe contener **al menos tres afirmaciones negativas
verificables** sobre el producto. Un paquete que solo dice cosas buenas es un folleto y está
suspenso.

<details>
<summary>Ejemplo de referencia</summary>

Las tres afirmaciones negativas de este contexto casi se escriben solas:

1. *«El aislamiento entre clientes se aplica en la capa de aplicación mediante un identificador de
   organización; no existe separación a nivel de esquema ni de base de datos. Un fallo de
   autorización en la aplicación podría exponer datos entre inquilinos. Este es el riesgo
   arquitectónico principal de la plataforma y hay trabajo en curso para reducirlo.»*
2. *«NovaPay no está certificada bajo ninguna norma de seguridad de la información a esta fecha;
   la implantación del sistema de gestión está en su primer año.»*
3. *«Tres de las 47 dependencias directas no registran actividad de mantenimiento desde hace más
   de dos años; se listan en el SBOM adjunto con su plan de sustitución.»*

Cuesta escribirlas. Y son exactamente las que hacen que un banco confíe: cualquier equipo de
seguridad competente descubrirá la primera en la evaluación técnica, y encontrarla después de
haber leído un documento que la ocultaba destruye la relación.

Sobre la afirmación comercial: lo que sí se puede decir es *«NovaPay aplica los controles de
[marco], y está implantando un SGSI conforme a ISO/IEC 27001, con auditoría de certificación
prevista para [fecha]»*. Lo que no se puede decir es «cumple con los principales estándares
internacionales», porque no significa nada verificable y, en un contrato, puede leerse como una
declaración.

</details>

**Límites éticos y legales.** Un aviso de seguridad puede tener consecuencias contractuales:
redáctalo con legal. No publiques detalles explotables antes de que exista una corrección o una
mitigación disponible. No demores el aviso a los clientes afectados por conveniencia comercial: el
plazo se define en la política, antes de necesitarla.

## 13 · Inventario y registro de riesgos de IA

**Contexto.** Eres el responsable de gobierno de IA de *Andes Retail*. La Gerencia Digital ha
desplegado tres sistemas sin pasar por seguridad y ha aparecido un cuarto en la factura de la nube
que nadie reclama.

**Datos de entrada.** [Andes Retail](ORGANIZACIONES.md#-andes-retail), punto 7 de su situación
actual.

**Instrucciones.**

1. Construye el **inventario** con la [plantilla 13](PLANTILLAS.md#13--inventario-de-sistemas-de-ia),
   incluida la columna «cómo se descubrió».
2. Construye el **registro de riesgos de IA** con la
   [plantilla 14](PLANTILLAS.md#14--registro-de-riesgos-de-ia): al menos tres riesgos por sistema,
   **cada uno con un escenario concreto y comprobable**.
3. Escribe la **política de uso aceptable** de una página, que incluya la **alternativa** que
   ofreces para el caso que prohíbes.
4. Haz la **evaluación previa al despliegue** del agente interno: permisos, acciones irreversibles,
   qué exige aprobación humana, qué queda registrado.
5. Diseña tres escenarios de prueba adversarial para el asistente de atención al cliente, con lo
   que buscarías y cómo lo mitigarías.
6. Escribe la nota de una página para el comité: qué se aprueba, qué se condiciona y qué se
   detiene.

**Entregable esperado.** Inventario + registro de riesgos + política + evaluación del agente +
plan de pruebas adversariales + nota al comité.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Cada riesgo tiene un escenario concreto y una forma de comprobarlo | 30 |
| Todos los sistemas tienen dueño de negocio con nombre y cargo | 25 |
| La política prohíbe **y ofrece alternativa**; es cumplible | 25 |
| La evaluación del agente delimita permisos y acciones irreversibles | 20 |

**Criterio de aceptación.** **Ningún riesgo puede estar formulado como categoría abstracta.**
«Riesgo de sesgo» o «riesgo de alucinación» no son escenarios: no permiten comprobar nada ni
decidir nada. Un solo riesgo así invalida el escenario.

<details>
<summary>Ejemplo de referencia</summary>

Escenario abstracto (suspenso): *«Riesgo de inyección de prompt en el asistente.»*

Escenario concreto (aprobado): *«Un cliente pega en el chat el texto de un correo que contiene
instrucciones ocultas; el asistente las interpreta como órdenes y devuelve el historial de compras
de otro cliente cuyo caso quedó en el contexto de la sesión anterior. Se comprobaría enviando un
mensaje con instrucciones embebidas tras una sesión previa y verificando si se filtra contenido
ajeno. Impacto: datos personales de clientes, con obligación de notificación.»*

El cuarto sistema —el resumen automático de reclamos que apareció en la factura— es el más
interesante del escenario: su fila del inventario tendrá «dueño de negocio: **desconocido**» y su
primer riesgo será precisamente ese. La recomendación defendible al comité es **suspenderlo hasta
que aparezca un dueño**, no evaluarlo: un sistema en producción del que nadie responde no puede
gobernarse.

La política que funciona no dice «prohibido usar herramientas de IA». Dice: *«No se pueden
introducir datos de clientes en servicios de IA no aprobados. Para ese uso está disponible
[alternativa aprobada], y para incorporar una herramienta nueva el proceso tarda [X] días.»* Una
prohibición sin alternativa destruye el inventario, que es el único activo real de esta función.

</details>

**Límites éticos y legales.** Las pruebas adversariales se hacen **sobre sistemas propios y con
autorización**, en entornos que no afecten a clientes reales. Si un sistema decide sobre personas,
la evaluación debe incluir a legal y a quien responda por privacidad; no la resuelvas solo desde
seguridad.

## 14 · Incidente OT con continuidad y seguridad de las personas

**Contexto.** Eres el OT CISO recién nombrado de *Minera Alto Cobre*, con doble reporte a
Tecnología y a Operaciones. Es martes, 03:20. El sistema de gestión empresarial de la red
corporativa está cifrado. El historizador de la zona de supervisión no responde. La planta
concentradora sigue operando. Hay doce reglas de origen desconocido en el cortafuegos que separa
la zona corporativa de la de supervisión.

**Datos de entrada.** [Minera Alto Cobre](ORGANIZACIONES.md#-minera-alto-cobre).

**Instrucciones.**

1. Construye el **inventario pasivo** de los activos del escenario, indicando **cómo** obtendrías
   cada dato sin escaneo activo.
2. Define el **modelo de zonas y conductos** y la matriz de flujos: por cada conducto, protocolo,
   sentido, inspección y quién lo aprueba.
3. Redacta el **procedimiento de acceso remoto** para los tres fabricantes, incluido el que
   condiciona la garantía.
4. Construye el **registro de riesgos OT** con al menos ocho riesgos, con dueño de Operaciones.
5. **Dirige el incidente**: cronología con reloj. Qué se aísla, en qué orden, quién autoriza
   detener o mantener el proceso, qué se comunica, cuándo se evalúa el deber de reporte y con qué
   información.
6. Construye el **roadmap OT** con la [plantilla 15](PLANTILLAS.md#15--roadmap-de-seguridad-ot),
   señalando qué entra en la parada de octubre.
7. Escribe el análisis posterior: qué se implanta, **qué se descarta porque interferiría con la
   seguridad de las personas** y qué se acepta como riesgo.

**Entregable esperado.** Inventario pasivo + zonas y conductos + procedimiento de acceso remoto +
registro de riesgos OT + cronología del incidente + roadmap + análisis posterior.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| El inventario es íntegramente pasivo y explica el método de cada dato | 25 |
| La cronología muestra quién autorizó cada decisión, con hora | 25 |
| El roadmap respeta la ventana de parada y lleva la revisión con seguridad de proceso | 25 |
| El análisis posterior descarta al menos un control por su efecto sobre las personas | 25 |

**Criterio de aceptación.** Tres condiciones, todas obligatorias: **(a)** ninguna medida propuesta
puede interferir con una función instrumentada de seguridad, y debes demostrar que lo comprobaste;
**(b)** la decisión de detener o mantener el proceso la toma **Operaciones**, no tú; **(c)** el
inventario no puede incluir ningún escaneo activo en producción. Fallar una sola invalida el
escenario completo.

<details>
<summary>Ejemplo de referencia</summary>

La primera decisión del incidente **no** es «aislar la planta». Es preguntar a Operaciones qué
significa aislar en ese momento: si el historizador alimenta un reporte de producción, cortarlo es
inocuo; si el enlace se usa para una función de proceso, cortarlo puede provocar una parada no
controlada, que es justamente el daño que se quiere evitar. La cronología correcta empieza con
*«03:25 — Contacto con jefe de turno. Pregunta: ¿qué depende del enlace supervisión–control en
este momento?»*

Las doce reglas de origen desconocido son el hallazgo más valioso del escenario y **no se borran
durante el incidente**: se registran, se documenta qué tráfico cursan y se cierran en una ventana
acordada. Eliminarlas a las 03:30 sin saber qué sostienen puede detener la planta.

El control que se descarta por seguridad de las personas: la propuesta de instalar un agente de
detección en las estaciones de operador de la sala de control. Introduce carga, requiere reinicios
y podría retrasar la respuesta del operador ante una alarma. Se descarta y se sustituye por
monitoreo pasivo de red en esa zona. **Documentar ese descarte es parte del entregable**, no una
omisión.

Sobre el deber de reporte: el guion no debe resolver «hay que reportar» sino identificar el punto
de decisión —quién evalúa si se cumple el umbral, con qué información y en qué plazo—, y que ese
procedimiento exista **antes** del incidente.

</details>

**Límites éticos y legales.** En un entorno industrial la seguridad de las personas está por
encima de cualquier control de ciberseguridad, sin excepción. No propongas medidas sobre sistemas
instrumentados de seguridad sin la participación de la ingeniería de proceso. Las obligaciones de
reporte de incidentes dependen de la calificación de la organización y de su sector: verifícalas
en la fuente oficial ([contexto chileno](../../rutas/ecosistema-ciso.md#-contexto-chileno-y-latinoamericano))
y con asesoría legal, no de memoria.

## 🎓 Después del laboratorio

- Resuelve la **[evaluación del ecosistema CISO](EVALUACION.md)**: preguntas de escenario,
  ejercicio RACI, aceptación de riesgo, conflicto de interés e informe ejecutivo.
- Rinde el **[examen final de tu rol](../../docs/examen-final-por-rol.md)**.
- Guarda los entregables: son la evidencia de portafolio que piden todas las rutas del
  [ecosistema CISO](../../rutas/ecosistema-ciso.md).

## 🔗 Relacionado

- 🗂️ [El ecosistema CISO](../../rutas/ecosistema-ciso.md) — el mapa completo de cargos
- 🏢 [Organizaciones ficticias](ORGANIZACIONES.md) · 🧾 [Plantillas](PLANTILLAS.md) · 🎓 [Evaluación](EVALUACION.md)
- 🧪 [Índice de laboratorios](../README.md)
- 📚 [Parte 14 — GRC, riesgo y cumplimiento](../../classes/parte-14-grc-riesgo-y-cumplimiento/README.md) ·
  [219 · Ejercicios de mesa](../../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md)
