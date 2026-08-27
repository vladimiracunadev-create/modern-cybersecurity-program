# 🎓 Evaluación del ecosistema CISO

Esta evaluación **no comprueba que te sepas las definiciones**. Comprueba que, ante una situación
concreta, sabes decir **quién decide, quién asesora y quién responde** — y que no confundes un
consejo interesado con un dictamen independiente.

> **Cómo se aprueba.** La evaluación tiene dos partes:
>
> - **Parte A · Escenarios** (18 preguntas, 54 puntos). Se aprueba con 38.
> - **Parte B · Ejercicios prácticos** (5 ejercicios, 46 puntos). Se aprueba con 32.
>
> Hay que aprobar **las dos partes por separado**. Sumar 70 puntos con la Parte B suspensa no
> aprueba: los ejercicios son el objeto de la evaluación y las preguntas son el filtro previo.
>
> Requisito previo: haber leído [el ecosistema CISO](../../rutas/ecosistema-ciso.md) y haber hecho
> al menos cuatro escenarios del [laboratorio](README.md).

---

## Parte A · Escenarios de selección múltiple

Cada pregunta vale **3 puntos**. Todas se responden con la información del enunciado; ninguna
requiere memorizar una norma. Las respuestas están plegadas: intenta las dieciocho antes de abrir
ninguna.

### Bloque 1 — Quién decide, quién asesora, quién responde

**1.** El CISO de una empresa determina que un sistema heredado no puede parchearse y que
sustituirlo cuesta más de lo que la empresa quiere gastar este año. ¿Quién debe firmar la
aceptación del riesgo residual?

- a) El CISO, porque es el responsable de la seguridad de la información.
- b) El gerente de la unidad de negocio que usa ese sistema.
- c) El jefe de TI, porque el sistema es suyo.
- d) El auditor interno, porque valida los controles.

<details><summary>Ver respuesta</summary>

**Correcta: b).** La aceptación de un riesgo residual es una **decisión de negocio**: la firma
quien responde por el proceso que se beneficia de no gastar ese dinero. El CISO toma conocimiento
y deja constancia; TI ejecuta; auditoría no decide, verifica. Si el CISO firma, la organización ha
trasladado una decisión de negocio a una función asesora, que es el error estructural más común de
todo este ecosistema.

</details>

**2.** Un Field CISO de un fabricante entrega a su cliente una «evaluación de madurez frente a NIST
CSF» con puntuaciones por función. El cliente quiere adjuntarla a su expediente de auditoría como
evidencia de evaluación independiente. ¿Qué corresponde hacer?

- a) Aceptar: el marco es público y la metodología es la misma que usaría un auditor.
- b) Aceptar si el Field CISO tiene CISSP y CISM.
- c) Advertir por escrito que la evaluación **no es independiente** y recomendar un auditor externo
  si se necesita un dictamen.
- d) Aceptar, pero quitando el logotipo del fabricante del documento.

<details><summary>Ver respuesta</summary>

**Correcta: c).** La independencia no depende del marco usado ni de las credenciales de quien
evalúa: depende de **quién paga y de qué se vende después**. Un Field CISO trabaja para un
proveedor con interés comercial en el resultado. Puede entregar un insumo valiosísimo; lo que no
puede es que se presente como dictamen independiente. Quitar el logotipo (d) empeora las cosas:
oculta el conflicto en lugar de declararlo.

</details>

**3.** Una empresa contrata un vCISO fractional por dos días al mes. A los cuatro meses, el gerente
general le pide que «decida» si se acepta el riesgo de no cifrar una base de datos histórica.
¿Cuál es la respuesta profesional?

- a) Decidir, porque para eso lo contrataron.
- b) Negarse a opinar: no tiene información suficiente.
- c) Preparar la decisión —opciones, coste, riesgo residual y recomendación— y pedir que la firme
  un responsable de la empresa.
- d) Escalar al directorio directamente, sin pasar por el gerente general.

<details><summary>Ver respuesta</summary>

**Correcta: c).** Es la respuesta que separa asesorar de decidir. El vCISO aporta criterio, no
mandato: su trabajo es dejar la decisión lista y trazable. Negarse a opinar (b) es abandonar el
encargo; decidir (a) es asumir una responsabilidad de negocio sin autoridad ni información
completa; saltarse al gerente (d) rompe la línea acordada sin motivo.

</details>

**4.** Durante un incidente de ransomware, ¿quién debe tener la **A** (*accountable*) en la fila
«decidir si se paga el rescate» de un RACI de crisis?

- a) El CISO.
- b) El jefe de respuesta a incidentes.
- c) El CEO o el órgano de administración, con asesoría legal obligatoria.
- d) El proveedor de respuesta a incidentes contratado.

<details><summary>Ver respuesta</summary>

**Correcta: c).** No es una decisión técnica: compromete a la organización financiera, legal y
reputacionalmente, y puede tener implicaciones que exceden a la empresa. El CISO informa y
recomienda; legal es consultado obligatoriamente; el proveedor ejecuta lo que se le contrate.
Poner esa **A** en el CISO es un error que se ve en muchos ejercicios de mesa reales.

</details>

**5.** Un BISO detecta que su unidad de negocio no podrá cumplir un control corporativo en el plazo
fijado. ¿Qué corresponde?

- a) Aplicar el control igualmente: la política es la política.
- b) Conceder una excepción indefinida para no frenar a la unidad.
- c) Documentar una excepción con control compensatorio, fecha de vencimiento y firma del
  responsable de la unidad, y comunicarla al programa central.
- d) Informar al CISO y esperar instrucciones sin hacer nada más.

<details><summary>Ver respuesta</summary>

**Correcta: c).** La excepción gestionada es la herramienta característica del BISO. Sin fecha se
convierte en política de facto (b); sin compensación deja el riesgo desnudo; sin comunicación al
centro rompe la coherencia del programa. La opción (a) ignora que a veces la política es la que
está mal dimensionada, y la (d) convierte al BISO en un buzón.

</details>

**6.** ¿Quién responde legalmente por las obligaciones de ciberseguridad de una organización?

- a) El CISO, en todos los casos.
- b) La organización y, según el marco aplicable, sus órganos de administración; el reparto interno
  es una decisión de la empresa.
- c) El DPO, porque es la figura que la ley reconoce.
- d) El proveedor de seguridad contratado.

<details><summary>Ver respuesta</summary>

**Correcta: b).** Las obligaciones recaen sobre la organización. Que el CISO las ejecute y las
firme internamente es un reparto interno, no una imposición automática de la norma. Afirmar (a)
sin citar el artículo concreto es exactamente el tipo de afirmación que este programa evita. El
DPO tiene un mandato específico de protección de datos, no la responsabilidad general.

</details>

### Bloque 2 — CISO frente a Field CISO

**7.** ¿Cuál de estas afirmaciones distingue mejor a un CISO de un Field CISO?

- a) El CISO es más técnico.
- b) El Field CISO gana más.
- c) El CISO tiene mandato, presupuesto y responde ante el directorio de su organización; el Field
  CISO asesora a clientes desde un proveedor y no controla nada de eso.
- d) El Field CISO trabaja en remoto y el CISO en la oficina.

<details><summary>Ver respuesta</summary>

**Correcta: c).** La diferencia es de **mandato**, no de conocimiento, de retribución ni de
modalidad de trabajo. Un Field CISO puede saber más que el CISO al que asesora y seguir sin poder
decidir nada en esa organización.

</details>

**8.** El equipo comercial pide al Field CISO que use en una reunión dos incidentes recientes del
sector del cliente como argumento de urgencia. Él no conoce sus causas. ¿Qué hace?

- a) Usarlos: son públicos.
- b) Usarlos, pero aclarando que no conoce los detalles.
- c) No usarlos como argumento de urgencia, y sustituirlos por hechos verificables del propio
  cliente; explicar internamente por qué.
- d) Negarse a asistir a la reunión.

<details><summary>Ver respuesta</summary>

**Correcta: c).** Citar incidentes ajenos cuyas causas se desconocen es meter miedo, no asesorar; y
además es más débil que un hecho del propio cliente, que es incontestable. La opción (b) es una
media medida que sigue apoyando la decisión en algo que no se puede sostener. La (d) es abandonar
la responsabilidad de defender una posición profesional dentro de la propia empresa.

</details>

**9.** El mayor riesgo del cliente no lo resuelve el producto del Field CISO. ¿Qué debe contener
la recomendación?

- a) Solo lo que el producto resuelve: para lo demás ya buscarán a otro.
- b) El riesgo real, la recomendación correcta aunque no incluya el producto propio, y la propuesta
  comercial claramente etiquetada como tal.
- c) El riesgo real, pero enmarcado de modo que el producto parezca la solución.
- d) Una lista de opciones sin recomendación, para no sesgar.

<details><summary>Ver respuesta</summary>

**Correcta: b).** Etiquetar es lo que hace compatible asesorar y vender. La opción (d) suena
prudente pero es una renuncia: al cliente lo que le sirve es tu criterio, siempre que sepa desde
dónde lo emites.

</details>

**10.** Un cliente comparte con el Field CISO su arquitectura y sus brechas. Seis meses después,
otro cliente del mismo sector le describe un problema idéntico. ¿Puede usar lo aprendido?

- a) Sí, es su experiencia profesional.
- b) Sí, si anonimiza el nombre del primer cliente.
- c) Puede usar el **patrón general**, nunca detalles reconocibles; y si el sector y el tamaño
  hacen identificable al primer cliente, tampoco el patrón.
- d) No puede usar nada de lo que aprende con clientes.

<details><summary>Ver respuesta</summary>

**Correcta: c).** La anonimización (b) no basta cuando hay tres empresas de ese tamaño en ese
sector en el país. La opción (d) haría imposible el puesto: aportar patrones es justamente su
valor. El criterio operativo es la **identificabilidad**, no el nombre.

</details>

### Bloque 3 — vCISO, fractional, interim y CISO as a Service

**11.** Una empresa necesita a alguien que ocupe el cargo a jornada completa durante seis meses,
mientras busca al titular, y que dirija una auditoría en curso. ¿Qué figura es?

- a) vCISO.
- b) Fractional CISO.
- c) Interim CISO.
- d) CISO as a Service.

<details><summary>Ver respuesta</summary>

**Correcta: c).** «Interim» describe la **temporalidad** y suele implicar dedicación completa y más
autoridad. Podría prestarse además en remoto (y ser también «virtual») o a través de una firma (y
ser también «as a service»), pero lo que define este encargo es que cubre una vacante con fecha de
fin.

</details>

**12.** ¿Qué describe exactamente el término «fractional»?

- a) Que el servicio se presta en remoto.
- b) Que la dedicación es parcial y se reparte entre varios clientes.
- c) Que el contrato es temporal.
- d) Que lo presta una empresa y no una persona.

<details><summary>Ver respuesta</summary>

**Correcta: b).** «Virtual» es el cómo (a), «interim» el hasta cuándo (c) y «CISO as a Service» el
quién responde (d). Un encargo puede ser las cuatro cosas a la vez, y por eso el término suelto no
informa: informa el contrato.

</details>

**13.** ¿Cuál es la diferencia práctica más importante entre contratar a un vCISO individual y
contratar «CISO as a Service» a una firma?

- a) El precio.
- b) Que en el servicio hay un equipo detrás y continuidad si la persona asignada se va.
- c) Que el servicio incluye herramientas.
- d) Ninguna: son sinónimos comerciales.

<details><summary>Ver respuesta</summary>

**Correcta: b).** La continuidad contractual es la diferencia estructural. Puede incluir
herramientas o no, y el precio depende del alcance. Tratarlos como sinónimos (d) lleva a firmar
contratos que no cubren lo que el cliente creía comprar.

</details>

**14.** El contrato de un vCISO no dice nada sobre su capacidad de detener un despliegue. El
vCISO detecta un despliegue con un fallo crítico y lo detiene. ¿Qué ha ocurrido?

- a) Ha hecho su trabajo.
- b) Ha ejercido una autoridad que no tiene; debía escalar a quien sí puede detenerlo y dejar
  constancia.
- c) Da igual: el resultado es el correcto.
- d) Ha incumplido su deber de confidencialidad.

<details><summary>Ver respuesta</summary>

**Correcta: b).** La autoridad del vCISO nace del contrato. Ejercer una que no se tiene crea
exposición para él y confusión para el cliente, aunque la decisión de fondo sea acertada (c). Lo
correcto es escalar de inmediato, por escrito, a quien tenga la potestad — y añadir esa cláusula
en la siguiente renovación.

</details>

### Bloque 4 — Especializaciones y cargos vecinos

**15.** Una empresa nombra «Cloud CISO» a una persona que trabaja en un proveedor de nube y viaja
a reuniones con clientes para asesorarlos sobre su adopción. Funcionalmente, ¿qué es?

- a) Un CISO con especialidad en nube.
- b) Un Field CISO con especialidad en nube.
- c) Un BISO de la unidad de nube.
- d) Un arquitecto de soluciones.

<details><summary>Ver respuesta</summary>

**Correcta: b).** Cobra de un proveedor, asesora a clientes y no controla el presupuesto, el equipo
ni el riesgo de esos clientes: esa es la definición de Field CISO. Un arquitecto de soluciones (d)
trabaja la solución técnica; aquí la conversación es de riesgo y de decisión ejecutiva.

</details>

**16.** ¿Por qué el DPO no debe absorberse dentro de la función del CISO?

- a) Porque tiene más antigüedad en la organización.
- b) Porque su función incluye **supervisar el cumplimiento** en protección de datos y debe poder
  discrepar del negocio y del propio CISO sin represalia.
- c) Porque el CISO no entiende de datos personales.
- d) Porque el DPO reporta al regulador.

<details><summary>Ver respuesta</summary>

**Correcta: b).** La razón es la **independencia funcional**: quien supervisa no puede depender de
quien es supervisado. No es una cuestión de conocimiento (c) ni de jerarquía (a), y el DPO no es un
funcionario del regulador (d), aunque sea su interlocutor.

</details>

**17.** Un OT CISO propone instalar un agente de detección en las estaciones de operador de una
sala de control. Ingeniería de proceso advierte que podría retrasar la respuesta del operador ante
una alarma. ¿Qué corresponde?

- a) Instalarlo: la política corporativa lo exige en todos los endpoints.
- b) Instalarlo solo en horario de baja producción.
- c) No instalarlo y buscar un control alternativo, documentando el descarte y su motivo.
- d) Instalarlo y aceptar el riesgo firmando el CISO corporativo.

<details><summary>Ver respuesta</summary>

**Correcta: c).** En tecnología operacional la seguridad de las personas está por encima de
cualquier control de ciberseguridad. El monitoreo pasivo de red es la alternativa habitual.
Documentar el descarte forma parte del entregable: sin esa constancia, en la siguiente auditoría
parecerá un olvido.

</details>

**18.** Un registro de riesgos de IA contiene la entrada «riesgo de alucinación del modelo». ¿Qué
falla?

- a) Nada: es un riesgo reconocido del dominio.
- b) Que no es un escenario: falta la causa, el evento concreto, la consecuencia y cómo se
  comprobaría.
- c) Que debería estar en el registro de riesgos general, no en el de IA.
- d) Que le falta la puntuación CVSS.

<details><summary>Ver respuesta</summary>

**Correcta: b).** Una categoría no permite estimar impacto, asignar dueño ni decidir tratamiento.
El escenario equivalente útil sería: «el asistente afirma una condición de cobertura que la póliza
no incluye, el cliente actúa en consecuencia y la aseguradora recibe una reclamación; se
comprobaría con un banco de preguntas de cobertura contrastado contra el clausulado». CVSS (d) no
aplica a este tipo de riesgo.

</details>

---

## Parte B · Ejercicios prácticos

Cinco ejercicios, 46 puntos. Se aprueban con 32 **y** cumpliendo el criterio de aceptación de cada
uno. Usa las [plantillas](PLANTILLAS.md) y las
[organizaciones ficticias](ORGANIZACIONES.md).

### Ejercicio 1 · RACI de crisis (10 puntos)

**Situación.** *Andes Retail* sufre el incidente del [escenario 5](README.md#5--dirigir-un-ejercicio-de-mesa-de-ransomware):
el punto de venta de 41 tiendas deja de responder un viernes por la noche y el proveedor no
contesta.

**Qué entregas.** Un [RACI](PLANTILLAS.md#1--raci) con estas ocho filas, completo:

1. Declarar el incidente como grave.
2. Detener el canal digital.
3. Decidir si se paga un rescate.
4. Evaluar si se cumple el umbral de notificación a la autoridad.
5. Notificar a la autoridad.
6. Comunicar a clientes.
7. Contratar un proveedor externo de respuesta a incidentes.
8. Autorizar la restauración desde copia y declarar el servicio limpio.

Añade, para las filas 2, 3 y 5, **dos líneas de justificación** de por qué la **A** está donde
está.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Una sola **A** por fila, y en todas las filas hay al menos una **R** | 3 |
| La **A** de la fila 3 está fuera del área de seguridad | 3 |
| Legal aparece como **C** en las filas 3, 4, 5 y 6 | 2 |
| Las justificaciones distinguen decisión de ejecución | 2 |

**Criterio de aceptación.** Ninguna fila puede tener al CISO como **A** en las filas 2, 3 y 5. El
CISO recomienda y ejecuta la parte técnica; no decide detener el negocio, pagar ni notificar.

### Ejercicio 2 · Aceptación de riesgo (10 puntos)

**Situación.** El Gerente de Operaciones de *Andes Retail* decide no renovar los sistemas de las
22 tiendas más antiguas este año: el coste supera el presupuesto disponible y prefiere destinarlo
a la temporada alta. El riesgo queda vivo.

**Qué entregas.** El [acta de aceptación de riesgo](PLANTILLAS.md#3--aceptación-formal-de-riesgo)
completa, más una respuesta razonada a esta pregunta: *«¿Qué haces si el gerente se niega a
firmar?»*

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| El escenario de riesgo tiene causa, evento y consecuencia, y una estimación con supuestos | 3 |
| Se evalúan al menos dos opciones de tratamiento además de aceptar | 2 |
| Hay vigencia, condiciones, controles compensatorios y hechos que reabren la decisión | 3 |
| La respuesta a la negativa a firmar es escalar y dejar constancia, no aceptar por él | 2 |

**Criterio de aceptación.** La firma de «acepta el riesgo» debe ser del Gerente de Operaciones. El
CISO solo puede aparecer como «toma conocimiento». Si el ejercicio resuelve la negativa a firmar
aceptando el riesgo el propio CISO, está suspenso.

### Ejercicio 3 · Conflicto de interés en preventa (10 puntos)

**Situación.** Eres el Field CISO de *Cumbre Security*. Debes entregar la recomendación a *Andes
Retail* sabiendo que **(a)** su mayor riesgo no lo resuelve tu producto, **(b)** tu producto tiene
una limitación conocida con su punto de venta y **(c)** comercial quiere usar los incidentes del
sector como palanca.

**Qué entregas.** Una recomendación de una página con las **cuatro etiquetas**
—`[HECHO]`, `[HIPÓTESIS]`, `[OPINIÓN PROFESIONAL]`, `[PROPUESTA DEL PROVEEDOR]`— más la
declaración de interés y la respuesta interna que le das a comercial.

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Las cuatro etiquetas están presentes y correctamente aplicadas | 3 |
| Aparece al menos una recomendación que **no** incluye el producto propio | 3 |
| La limitación del producto se declara con plazo y coste | 2 |
| La respuesta a comercial sostiene la posición y ofrece una alternativa mejor | 2 |

**Criterio de aceptación.** Un lector que no sepa para quién trabajas debe poder separar, sin
ayuda, los hechos de la propuesta comercial. Además, cada `[HIPÓTESIS]` debe indicar **qué la
refutaría**.

### Ejercicio 4 · Informe ejecutivo (10 puntos)

**Situación.** Comité de Auditoría de *Andes Retail*. Quince minutos, una página.

**Qué entregas.** El [informe ejecutivo de una página](PLANTILLAS.md#5--informe-ejecutivo-de-una-página)
con dos decisiones, cuatro indicadores y la sección «lo que no estamos haciendo».

**Rúbrica.**

| Criterio | Puntos |
|---|---|
| Las dos decisiones llevan plazo, coste y consecuencia de no decidir | 3 |
| Cabe en una página y es legible por alguien sin formación técnica | 2 |
| Cada indicador tiene una decisión asociada | 3 |
| La sección de lo que no se hace es concreta y honesta | 2 |

**Criterio de aceptación.** Un lector no técnico debe poder decirte qué dos cosas tiene que
decidir el comité. Si no puede, está suspenso, por muy bien escrito que esté.

### Ejercicio 5 · Clasificar seis cargos reales (6 puntos)

**Situación.** Te llegan seis descripciones de puesto. Clasifícalas.

| # | Descripción del puesto |
|---|---|
| 1 | «Responsable de seguridad para la región andina de un grupo multinacional. Ejecuta la política global, presupuesto regional, dos personas a cargo, reporta al Global CISO y a la dirección de país.» |
| 2 | «Asesor ejecutivo de seguridad. Acompaña a los clientes estratégicos en su hoja de ruta, participa en la definición del producto y representa a la compañía en eventos del sector. Objetivos ligados a la actividad de la cartera asignada.» |
| 3 | «Responsable de seguridad de la información. Ocho horas al mes. Contrato de doce meses renovable. Prepara el comité, mantiene el registro de riesgos y acompaña la auditoría.» |
| 4 | «Enlace de seguridad para la división de banca minorista. Traduce el riesgo del programa central al negocio, prioriza remediaciones y gestiona excepciones. Sin presupuesto propio.» |
| 5 | «Responsable de la seguridad de la plataforma que la compañía comercializa: requisitos, modelado de amenazas, respuesta a vulnerabilidades reportadas y paquete de confianza para clientes.» |
| 6 | «Responsable del cumplimiento en materia de protección de datos personales. Independencia funcional garantizada. Punto de contacto con la autoridad e interlocutor de los titulares de datos.» |

**Qué entregas.** Para cada uno: **familia** (A, B, C o D del
[ecosistema](../../rutas/ecosistema-ciso.md#-las-cuatro-familias)), **nombre del cargo**, y **la
señal del enunciado** que te lo dice.

**Rúbrica.** 1 punto por cargo correctamente clasificado **con su señal identificada**. Acertar el
nombre sin señalar la evidencia vale 0,5.

<details><summary>Ver respuesta</summary>

| # | Familia | Cargo | Señal decisiva |
|---|---|---|---|
| 1 | A | **Regional CISO** | «Ejecuta la política global», presupuesto regional, doble línea al Global CISO y al país |
| 2 | B | **Field CISO** (o Customer CISO) | Asesora a **clientes**, participa en el producto **de su empresa** y tiene objetivos ligados a la cartera |
| 3 | B | **vCISO fractional** | Dedicación parcial medida en horas al mes, por contrato renovable |
| 4 | C | **BISO** | «Enlace», una división, gestiona excepciones, **sin presupuesto propio** |
| 5 | C | **Product CISO** | Responde por «la plataforma que la compañía **comercializa**» y por el paquete de confianza |
| 6 | D | **DPO** — no es un tipo de CISO | «Independencia funcional» y punto de contacto con la autoridad |

</details>

---

## 🏁 Capstone por ruta

Esta evaluación es transversal. **Cada ruta independiente tiene además su propio capstone**, con
el entregable que produce ese puesto y que no se puede aprobar con el de otro:

| Ruta | Capstone | Dónde está |
|---|---|---|
| [🎩 CISO](../../rutas/ciso.md) | Paquete de gobierno + tabletop dirigido + informe al directorio | [Examen final por rol](../../docs/examen-final-por-rol.md) |
| [🛰️ Field CISO](../../rutas/field-ciso.md) | Ciclo completo de una cuenta con el conflicto de interés a la vista | [Ruta](../../rutas/field-ciso.md#capstone) · [Examen](../../docs/examen-final-por-rol.md) |
| [🧾 vCISO](../../rutas/vciso.md) | Encargo completo, de la declaración de trabajo al traspaso | [Ruta](../../rutas/vciso.md#capstone) · [Examen](../../docs/examen-final-por-rol.md) |
| [🔗 BISO](../../rutas/biso.md) | Un año de la unidad, con el mismo mes informado dos veces | [Ruta](../../rutas/biso.md#capstone) · [Examen](../../docs/examen-final-por-rol.md) |
| [📦 Product CISO](../../rutas/product-ciso.md) | Paquete de confianza y crisis del producto | [Ruta](../../rutas/product-ciso.md#capstone) · [Examen](../../docs/examen-final-por-rol.md) |
| [🤖 AI CISO](../../rutas/ai-ciso.md) | Programa mínimo viable de gobierno de IA | [Ruta](../../rutas/ai-ciso.md#capstone) · [Examen](../../docs/examen-final-por-rol.md) |
| [🏭 OT CISO](../../rutas/ot-ciso.md) | Incidente en planta con la jerarquía de prioridades correcta | [Ruta](../../rutas/ot-ciso.md#capstone) · [Examen](../../docs/examen-final-por-rol.md) |

## 🔗 Relacionado

- 🗂️ [El ecosistema CISO](../../rutas/ecosistema-ciso.md)
- 🧪 [Laboratorio ejecutivo CISO](README.md) · 🏢 [Organizaciones](ORGANIZACIONES.md) · 🧾 [Plantillas](PLANTILLAS.md)
- 🎓 [Examen final por rol](../../docs/examen-final-por-rol.md)
- 📝 [Autoevaluaciones por parte](../../autoevaluaciones/README.md)
