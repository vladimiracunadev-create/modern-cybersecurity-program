# 📦 Product CISO

> El responsable de la seguridad y la confianza de **lo que la empresa vende**, no de lo que la
> empresa usa. Su cliente no es el empleado: es el cliente que compra el producto y que, cada vez
> más, exige garantías antes de firmar. Convive con el [CISO](ciso.md) corporativo y se separa de
> él en una línea clara: **el CISO protege a la organización; el Product CISO protege a los
> clientes de la organización — y, por tanto, a la organización de sus clientes.**
>
> **Nivel de entrada:** ninguno; se llega desde ingeniería, AppSec o arquitectura de producto ·
> **Foco:** seguridad del ciclo de vida del producto, confianza demostrable y riesgo trasladado al
> cliente · **Certificación faro:** CSSLP o CISSP, con OWASP SAMM y ASVS como instrumental diario

**Alias y variantes:** *Product CISO*, *Head of Product Security*, *VP of Product Security*,
*Chief Product Security Officer (CPSO)*, *Director of Product Security*, *Chief Trust Officer*
cuando el énfasis se desplaza a la comunicación y la certificación. En dispositivos médicos y
automoción el cargo equivalente suele llamarse *Product Security Officer* y está más regulado.

**Fecha de consulta de las fuentes: 26 de agosto de 2026.**

## 🧭 Qué es y por qué importa

### Definición

Un Product CISO es el responsable ejecutivo de que **el producto o servicio que la empresa vende
sea seguro por diseño, lo demuestre y siga siéndolo durante toda su vida**, incluida la respuesta
cuando aparece una vulnerabilidad. Su alcance abarca requisitos, diseño, construcción, entrega,
operación y fin de vida del producto, más todo lo que rodea a la confianza del cliente:
certificaciones, cuestionarios, divulgación y comunicación de incidentes que afectan al producto.

### Nivel de consolidación del título

**Emergente como título, consolidado como función.** «Head of Product Security» y «VP Product
Security» son mucho más frecuentes que «Product CISO»; el título con CISO dentro aparece sobre
todo en empresas donde la seguridad del producto es un argumento de venta central o donde hay dos
programas claramente separados (corporativo y de producto). El trabajo, en cambio, existe en
prácticamente cualquier empresa que venda software o dispositivos conectados. **Cuando veas el
título, comprueba si designa la función completa o solo a un jefe de AppSec con nombre grande.**

### Qué problema resuelve

| Problema | Consecuencia si no hay nadie | Qué aporta el Product CISO |
|---|---|---|
| La seguridad del producto se decide en el último sprint | Deuda que se paga en incidentes y en ventas perdidas | Requisitos de seguridad desde la definición del producto |
| Cada cliente grande envía su propio cuestionario de seguridad | Ingeniería paralizada respondiendo formularios | Un **paquete de confianza** reutilizable y honesto |
| Aparece una vulnerabilidad en el producto y nadie sabe qué decir | Improvisación, filtración, pérdida de confianza | Política de divulgación, aviso de seguridad y proceso ensayado |
| El riesgo se traslada al cliente sin que nadie lo mida | La empresa se convierte en el riesgo de tercero de otros | Modelo de amenazas y responsabilidad compartida documentada |
| Ventas promete controles que el producto no tiene | Incumplimiento contractual | Una única fuente de verdad sobre qué hace y qué no hace el producto |

### Qué hace y qué no hace

| Sí hace | No hace |
|---|---|
| Definir los requisitos de seguridad del producto y las puertas de publicación | Gestionar la seguridad corporativa: correo, endpoint, red interna |
| Dirigir el modelado de amenazas y la revisión de arquitectura | Escribir todo el código seguro: eso lo hacen los equipos, con apoyo |
| Sostener el programa de AppSec y de seguridad de la cadena de suministro del producto | Sustituir al [CISO](ciso.md) en el riesgo de la organización |
| Ser el dueño de la política de divulgación y del proceso de avisos de seguridad | Decidir precios ni el plan comercial |
| Responder por el paquete de confianza y por las certificaciones del producto | Firmar la certificación: eso lo hace un organismo acreditado |
| Coordinar la respuesta a un incidente **del producto** con los clientes afectados | Dirigir la respuesta a un incidente corporativo |
| Gestionar el programa de recompensas o de divulgación coordinada | Ser el único punto de contacto técnico de cada cliente |

### Dónde existe

Empresas de software (especialmente las que venden a clientes grandes o regulados), plataformas y
SaaS, fabricantes de dispositivos conectados, dispositivos médicos, automoción, industria y
cualquier organización cuyo producto sea un vector de riesgo para terceros. En una empresa que
solo **consume** tecnología, este cargo no tiene sentido: allí la función es
[AppSec](appsec.md) dentro del programa del CISO.

## 🏛️ Mandato, autoridad y responsabilidad

### Línea de reporte

| Reporta a | Consecuencia |
|---|---|
| **CTO o VP de Ingeniería** | Máxima capacidad de ejecución; riesgo de que la seguridad ceda ante la fecha de entrega |
| **CISO corporativo** | Coherencia con el programa; riesgo de quedar lejos de la ingeniería y perder tracción |
| **CEO o dirección de producto** | Máxima visibilidad; suele ocurrir cuando la seguridad es argumento de venta |
| **Chief Trust Officer** | Foco en confianza y certificaciones; riesgo de derivar hacia lo comunicacional |

Ninguna es incorrecta; cada una impone un contrapeso distinto. La pregunta que hay que hacer es
**quién puede detener una publicación** y si esa capacidad está escrita.

### Autoridad, presupuesto, equipo y riesgo

- **Autoridad:** su palanca característica es la **puerta de publicación**. Un Product CISO sin
  capacidad de bloquear una versión con un fallo crítico conocido no tiene el puesto, tiene el
  título.
- **Presupuesto:** habitualmente dentro de ingeniería: herramientas de análisis, pruebas,
  programas de recompensas, auditorías externas y certificaciones.
- **Equipo:** sí. AppSec, seguridad de producto, a veces un equipo de respuesta a
  vulnerabilidades del producto (PSIRT) y una red de *security champions* en los equipos.
- **Riesgo:** responde por el **riesgo del producto**. La aceptación de un riesgo que se traslada
  al cliente debe firmarla la dirección de producto o de la empresa, no seguridad, y debe quedar
  registrada: es un riesgo que ya no es solo tuyo.

> ⚠️ **La decisión más difícil del puesto.** Publicar con un fallo conocido y mitigado, o retrasar
> la versión. Se resuelve con criterios acordados **antes**, no en la reunión de la noche anterior:
> qué severidad bloquea, qué mitigación es aceptable, quién puede levantar el bloqueo y con qué
> firma. Ese documento es tu principal entregable de gobierno.

### Conflictos de interés y límites éticos

| Situación | Riesgo | Cómo se maneja |
|---|---|---|
| Ventas pide afirmar que el producto «cumple» un estándar que no cumple | Tergiversación con efecto contractual | Una única fuente de verdad sobre capacidades, y tu firma en el paquete de confianza |
| El programa de recompensas recibe un hallazgo grave y comercial pide silencio | Ocultación con daño a clientes | Política de divulgación pública, escrita antes, con plazos |
| Un investigador externo amenaza con publicar | Presión y riesgo de reacción defensiva | Divulgación coordinada: canal, acuse, plazos y crédito |
| El cliente pide una excepción de seguridad para adoptar el producto | Traslado silencioso del riesgo | Documentar quién asume qué, en el contrato |
| Certificas el producto con un alcance recortado y se comunica como si fuera total | Engaño por omisión | Publicar el alcance de la certificación junto al logotipo |
| Tu bono depende de la fecha de lanzamiento | Incentivo perverso | Que parte de tus objetivos dependan de indicadores de seguridad y de la ausencia de regresiones |

## 🗓️ El día, el mes y el año

**Un día típico.** Revisión de arquitectura de una funcionalidad nueva; triaje de la cola de
hallazgos de análisis estático y de la plataforma de recompensas; una llamada con un cliente
grande que pregunta por el cifrado y por el aislamiento entre inquilinos; media hora escribiendo
la respuesta a un cuestionario de seguridad para reutilizarla cien veces.

**Un mes típico.** Uno o dos modelados de amenazas; revisión de métricas de deuda de seguridad por
equipo; el comité donde se decide si una versión sale; la actualización del inventario de
componentes de terceros y del SBOM; un aviso de seguridad, si toca.

**Un año típico.** El ciclo de certificación o de auditoría del producto; una prueba de intrusión
externa con un alcance decidido por ti; la revisión anual de la política de divulgación; el
ejercicio de mesa de «vulnerabilidad crítica del producto un viernes»; y la conversación de
presupuesto donde defiendes que la seguridad del producto es una inversión comercial, no un coste
de ingeniería.

### Interlocutores

| Internos | Externos |
|---|---|
| Producto y dirección de producto | Clientes y sus equipos de seguridad y compras |
| Ingeniería y arquitectura | Investigadores de seguridad y plataformas de recompensas |
| [CISO](ciso.md) corporativo | Auditores y organismos de certificación |
| Legal y contratos | Reguladores sectoriales, cuando el producto lo está |
| Ventas y preventa | Proveedores de componentes y bibliotecas críticas |
| Soporte y éxito del cliente | La comunidad de código abierto de la que depende el producto |

## 🧾 Entregables verificables

| Entregable | Qué demuestra | Cómo se verifica |
|---|---|---|
| **Paquete de confianza del producto** | Que la confianza es demostrable y reutilizable | Arquitectura, datos, cifrado, aislamiento, retención, subencargados, certificaciones, alcance y **lo que el producto no hace** |
| **Criterios de puerta de publicación** | Que la decisión de publicar no se improvisa | Severidad que bloquea, mitigaciones válidas, quién levanta el bloqueo y con qué firma |
| **Modelo de amenazas** de los componentes críticos | Que el diseño se pensó, no solo se probó | Activos, actores, superficie, mitigaciones y supuestos |
| **SBOM y política de componentes** | Control de la cadena de suministro | Inventario actualizado, criterio de adopción y de retirada |
| **Política de divulgación** y proceso de aviso | Que hay un cauce antes de necesitarlo | Publicada, con canal, plazos y compromiso de crédito |
| **Avisos de seguridad publicados** | Honestidad operativa | Producto, versiones, impacto, mitigación y solución |
| **Respuestas maestras a cuestionarios** | Que ingeniería no responde formularios | Una fuente de verdad versionada y con dueño |
| **Matriz de responsabilidad compartida** del producto | Que el cliente sabe qué le toca a él | Qué protege el producto y qué debe hacer el cliente |
| **Plan de fin de vida** | Que la seguridad no termina con la venta | Fechas, migración y último parche |

## 📏 KPI y KRI

| Indicador | Tipo | Qué dice |
|---|---|---|
| Cobertura de modelado de amenazas en funcionalidades críticas | KPI | Si la seguridad entra por diseño |
| Tiempo medio de corrección de vulnerabilidades **del producto** por severidad | KPI | Capacidad real de respuesta hacia el cliente |
| Vulnerabilidades encontradas antes de publicar frente a después | KPI | Eficacia del desplazamiento a la izquierda |
| Deuda de seguridad por equipo y su tendencia | KPI | Si el problema mejora o se acumula |
| Cuestionarios respondidos con material reutilizable | KPI | Fricción comercial evitada |
| Componentes de terceros con soporte vigente | KPI | Salud de la cadena de suministro |
| Tiempo desde el reporte externo hasta el acuse | KPI | Salud del canal de divulgación |
| **Versiones publicadas con fallos críticos conocidos sin firma** | **KRI** | La puerta de publicación no funciona |
| **Vulnerabilidades explotadas en clientes** | **KRI** | El indicador que importa de verdad |
| Investigadores que publican sin coordinarse contigo | **KRI** | Tu canal no funciona o no genera confianza |
| Afirmaciones comerciales que el producto no sostiene | **KRI** | Riesgo contractual y reputacional |
| Componentes críticos sin mantenedor activo | **KRI** | Riesgo de cadena de suministro latente |

## 🧠 Qué necesitas saber

### Competencias técnicas

Es la ruta más técnica del ecosistema CISO. No puedes dirigir lo que no entiendes.

- **Ciclo de desarrollo seguro**: requisitos, diseño, construcción, pruebas, despliegue y
  operación; qué aporta cada tipo de análisis y qué no puede encontrar ninguno.
- **Modelado de amenazas** con un método reproducible y aplicable por los equipos, no solo por ti.
- **Seguridad de aplicaciones y de APIs**: las clases de fallo, no la lista de moda.
- **Cadena de suministro de software**: dependencias, procedencia, firma, SBOM y sus límites.
- **Nube y arquitectura multiinquilino**: el aislamiento entre clientes es el riesgo estructural
  de casi cualquier producto SaaS.
- **Criptografía aplicada**: qué se cifra, con qué, dónde están las claves y quién puede usarlas.
- **Respuesta a vulnerabilidades**: triaje, puntuación, corrección, versiones afectadas y aviso.
- Si el producto es **físico o embebido**: firmware, arranque seguro, actualización remota y el
  hecho incómodo de que un dispositivo instalado no se parchea igual que un servidor.

### Competencias de negocio

- Entender cómo se vende el producto y a quién: el ciclo de venta a empresas grandes está lleno de
  puertas de seguridad, y tú eres quien las abre.
- Traducir seguridad a **velocidad comercial**: cuántos acuerdos se destrabaron, cuántos días se
  ahorraron.
- Priorizar con criterio de producto, no solo de riesgo: qué funcionalidad se retrasa y qué cuesta.
- Construir el caso de inversión de un programa de seguridad de producto en términos de ingresos
  protegidos y acuerdos habilitados.

### Comunicación y negociación

- Escribir un **aviso de seguridad** claro, honesto y que no cause pánico ni oculte.
- Sostener una conversación técnica con el equipo de seguridad de un cliente grande.
- Negociar con ingeniería sin ser el freno permanente, y con producto sin ser el que siempre cede.
- Hablar con investigadores externos con respeto: son la mejor fuente de hallazgos que tendrás.

### Competencias regulatorias

Depende por completo del producto y del sector: protección de datos personales si el producto los
trata; normativa sectorial si vende a banca, salud o infraestructura crítica; obligaciones de
notificación de incidentes que puedan alcanzar a tus clientes. **No inventes obligaciones y no
las descartes:** identifica el marco aplicable con legal y documenta la conclusión. Ver el
[contexto chileno del ecosistema](ecosistema-ciso.md#-contexto-chileno-y-latinoamericano).

### Componente comercial

**Indirecto pero constante.** La seguridad del producto habilita ventas, y eso es legítimo. El
límite es no dejar que el argumento comercial deforme la afirmación técnica: si el paquete de
confianza dice algo que el producto no hace, has dejado de hacer tu trabajo y has creado un riesgo
contractual.

## 📚 Tu ruta en el programa

1. **Fundamentos** — [**001**](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md) · [**003** · Frameworks](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md) · [**025** · Ética y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md) — **la clase que sostiene tu política de divulgación**
2. **[Parte 11 · DevSecOps y seguridad del SDLC](../classes/parte-11-devsecops-y-seguridad-del-sdlc/README.md) — el núcleo del cargo, entera**
   - [**236** · Secure SDLC y shift-left](../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md) · [**237** · Modelado de amenazas STRIDE y DREAD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/237-modelado-de-amenazas-stride-y-dread/README.md) — **las dos clases centrales**
   - [**238** · SAST](../classes/parte-11-devsecops-y-seguridad-del-sdlc/238-sast-analisis-estatico-de-codigo/README.md) · [**239** · DAST](../classes/parte-11-devsecops-y-seguridad-del-sdlc/239-dast-analisis-dinamico-de-aplicaciones/README.md) · [**240** · SCA y dependencias](../classes/parte-11-devsecops-y-seguridad-del-sdlc/240-sca-dependencias-y-riesgo-de-terceros/README.md) · [**241** · Secretos en el código](../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md)
   - [**242** · Pipelines CI/CD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/242-seguridad-en-pipelines-ci-cd/README.md) · [**243** · Imágenes y contenedores](../classes/parte-11-devsecops-y-seguridad-del-sdlc/243-imagenes-y-contenedores-seguros-en-el-pipeline/README.md) · [**244** · Políticas como código](../classes/parte-11-devsecops-y-seguridad-del-sdlc/244-politicas-como-codigo-con-opa/README.md)
   - [**245** · Vulnerabilidades a escala](../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md) · [**246** · SBOM y SLSA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md) · [**247** · Seguridad de APIs](../classes/parte-11-devsecops-y-seguridad-del-sdlc/247-seguridad-de-apis-en-el-ciclo-de-desarrollo/README.md) · [**248** · Cultura y security champions](../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md)
3. **El producto visto desde el ataque** — [Parte 4](../classes/parte-4-seguridad-de-aplicaciones-web/README.md)
   - [**086** · Arquitectura web y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md) · [**087** · OWASP Top 10](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md) · [**115** · Secure coding y defensa](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md)
   - [**114** · Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md) — **léela desde el lado del que recibe los reportes**
4. **Donde se ejecuta tu producto** — [Parte 10](../classes/parte-10-seguridad-en-la-nube-y-contenedores/README.md)
   - [**221** · Responsabilidad compartida](../classes/parte-10-seguridad-en-la-nube-y-contenedores/221-fundamentos-de-seguridad-en-la-nube-y-responsabilidad-compartida/README.md) — el modelo que tú tendrás que escribir para tus clientes
   - [**222** · IAM](../classes/parte-10-seguridad-en-la-nube-y-contenedores/222-iam-en-la-nube-identidades-roles-y-permisos/README.md) · [**227** · Contenedores](../classes/parte-10-seguridad-en-la-nube-y-contenedores/227-seguridad-de-contenedores-docker/README.md) · [**233** · Gestión de secretos](../classes/parte-10-seguridad-en-la-nube-y-contenedores/233-gestion-de-secretos-en-la-nube/README.md) · [**234** · Logging y detección](../classes/parte-10-seguridad-en-la-nube-y-contenedores/234-logging-y-deteccion-en-la-nube/README.md)
5. **Gobierno, confianza y el cliente**
   - [**284** · Riesgo de terceros](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md) — **el tercero eres tú para tus clientes**
   - [**278** · ISO/IEC 27001](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md) · [**281** · GDPR, HIPAA y PCI-DSS](../classes/parte-14-grc-riesgo-y-cumplimiento/281-cumplimiento-gdpr-hipaa-y-pci-dss/README.md) · [**289** · Privacidad](../classes/parte-14-grc-riesgo-y-cumplimiento/289-privacidad-y-proteccion-de-datos/README.md) · [**287** · KPI y KRI](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md)
   - [**323** · Pruebas de seguridad del software y evaluación](../classes/parte-17-profundizacion-para-certificaciones/323-pruebas-de-seguridad-del-software-y-evaluacion/README.md) · [**330** · Análisis de código y automatización](../classes/parte-17-profundizacion-para-certificaciones/330-analisis-de-codigo-y-automatizacion-de-seguridad/README.md) · [**321** · Comunicación y reporte](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md)
6. **Si tu producto lleva IA dentro** — [**295** · OWASP Top 10 para aplicaciones con LLM](../classes/parte-15-seguridad-de-ia-y-machine-learning/295-owasp-top-10-para-aplicaciones-con-llm/README.md) · [**297** · Seguridad de aplicaciones con LLM, RAG y agentes](../classes/parte-15-seguridad-de-ia-y-machine-learning/297-seguridad-de-aplicaciones-con-llm-rag-y-agentes/README.md) · y la ruta de [AI CISO](ai-ciso.md)
7. **Si tu producto es un dispositivo** — [**266** · Seguridad de IoT](../classes/parte-13-seguridad-movil-iot-e-inalambrica/266-seguridad-de-iot-panorama-y-superficie-de-ataque/README.md) · [**267** · Hacking de firmware](../classes/parte-13-seguridad-movil-iot-e-inalambrica/267-hacking-de-firmware/README.md) · [**274** · Automotriz y bus CAN](../classes/parte-13-seguridad-movil-iot-e-inalambrica/274-seguridad-automotriz-y-bus-can/README.md) · [**275** · Dispositivos médicos](../classes/parte-13-seguridad-movil-iot-e-inalambrica/275-seguridad-de-dispositivos-medicos/README.md)

### Laboratorio y práctica

- 🧪 **[`labs/ciso-leadership`](../labs/ciso-leadership/README.md)** — el escenario **12**
  (paquete de confianza de producto) es el de esta ruta.
- 🧪 [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md) — tu laboratorio técnico
  principal; el [trayecto de Ingeniero DevSecOps](../labs/devsecops-pipeline/TRAYECTO-INGENIERO-DEVSECOPS.md)
  construye las puertas que tú vas a gobernar.
- 🧪 [`appsec-code`](../labs/appsec-code/README.md) y [`appsec-web`](../labs/appsec-web/README.md)
  — para no perder la mano en el código y en el fallo real.

### Capstone

**El paquete de confianza y la crisis del producto.** Sobre *NovaPay* —la plataforma de pagos
ficticia del laboratorio—:

1. **Modelo de amenazas** del componente que procesa pagos, con supuestos y mitigaciones.
2. **Criterios de puerta de publicación**, acordados por escrito con ingeniería y producto.
3. **Paquete de confianza completo**, incluida la sección de **lo que el producto no hace** y la
   matriz de responsabilidad compartida con el cliente.
4. **Política de divulgación** publicable, con canal, plazos y crédito.
5. **Aviso de seguridad** para una vulnerabilidad crítica ficticia: versiones afectadas, impacto,
   mitigación temporal, solución y cronología.
6. **Comunicación a un cliente grande** que pregunta si le afecta, escrita para su equipo de
   seguridad y para su dirección.

**Criterio de aceptación:** el paquete de confianza debe contener al menos tres afirmaciones
**negativas** verificables («el producto no cifra X», «el aislamiento entre inquilinos se apoya en
Y», «no se conservan registros más allá de Z»). Un paquete que solo dice cosas buenas no es un
paquete de confianza: es un folleto.

### Portafolio

- El modelo de amenazas con sus supuestos explícitos.
- Los criterios de puerta de publicación firmados.
- El paquete de confianza, con la sección negativa.
- El aviso de seguridad y la cronología.
- Un análisis de un aviso de seguridad público real, con qué harías igual y qué distinto.

## 🎤 Preguntas de entrevista

1. ¿Puedes detener una publicación? ¿Está escrito y quién puede revertirlo?
2. Enséñame los criterios con los que decides publicar con un fallo conocido.
3. ¿Qué contiene tu paquete de confianza y qué dice que el producto **no** hace?
4. Llega un reporte externo un viernes por la tarde con prueba de concepto pública. ¿Qué ocurre en
   las primeras cuatro horas?
5. ¿Cómo decides el alcance de una prueba de intrusión externa?
6. ¿Cuál es tu política con los investigadores? ¿Pagas, das crédito, pones plazos?
7. ¿Cómo evitas que ventas afirme lo que el producto no cumple?
8. ¿Qué haces con una dependencia crítica sin mantenedor?
9. ¿En qué se diferencia tu trabajo del CISO corporativo de tu empresa? ¿Dónde se solapan?
10. ¿Cómo mides que el producto es más seguro este año que el anterior?

## 🎓 Certificaciones

| Certificación | Para qué sirve en este puesto | Dónde la cubre el programa |
|---|---|---|
| **CSSLP** (ISC2) | Ciclo de vida seguro del software: la más alineada con el puesto | [Parte 11](../classes/parte-11-devsecops-y-seguridad-del-sdlc/README.md) |
| **CISSP** (ISC2) | Amplitud y credibilidad ejecutiva | [Parte 17](../classes/parte-17-profundizacion-para-certificaciones/README.md) y [**304**](../classes/parte-16-capstones-y-preparacion-de-certificaciones/304-preparacion-cissp-los-8-dominios/README.md) |
| **CISM** (ISACA) | Cuando el cargo pesa más en gestión que en ingeniería | [Parte 14](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md) |
| **OWASP SAMM** (marco, no certificación) | Medir y hacer crecer el programa de seguridad de producto | [**236**](../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md) y [**248**](../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md) |
| **OWASP ASVS** (estándar, no certificación) | Convertir «seguro» en requisitos verificables | [**115**](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md) y [**323**](../classes/parte-17-profundizacion-para-certificaciones/323-pruebas-de-seguridad-del-software-y-evaluacion/README.md) |
| **PenTest+ / OSCP** | Credibilidad técnica frente a tus equipos y a investigadores | [Partes 3 y 4](../classes/parte-3-hacking-etico-y-pentesting-metodologia/README.md) |

Ninguna garantiza el puesto: en esta ruta lo que se evalúa es lo que has construido y cómo
respondiste a una vulnerabilidad real.

## 📈 Progresión de carrera y salario

### Cargos de entrada y experiencia previa razonable

| Vía de origen | Qué traes | Qué te falta |
|---|---|---|
| [AppSec Engineer](appsec.md) o líder de AppSec | Profundidad en fallo y en código | Gobierno, confianza del cliente y conversación comercial |
| [Ingeniero DevSecOps](devsecops-engineer.md) | Pipeline, cadena de suministro, automatización | Modelado de amenazas de producto y trato con clientes |
| Arquitecto de producto o ingeniería senior | Diseño y credibilidad interna | Todo el dominio de seguridad ofensiva y de respuesta |
| [Pentester](pentester.md) senior con experiencia de producto | Saber cómo se rompe de verdad | Construir un programa y sostenerlo en el tiempo |

Lo que se comprueba no son los años, sino si has **cerrado el ciclo**: diseñaste, publicaste,
recibiste un hallazgo grave y respondiste con un aviso público.

### Hacia dónde sigue

Product CISO → **CISO corporativo** (es una vía cada vez más frecuente en empresas de software) ·
→ **Chief Trust Officer** · → CTO en empresas donde la seguridad es el producto · →
[Field CISO](field-ciso.md) en un fabricante de seguridad · → asesoría y consejo técnico.

### Sobre la remuneración

Este programa no publica cifras propias para este puesto: en empresas de software la retribución
suele incluir participación accionaria, lo que hace incomparables los números entre organizaciones
y entre países. Como orientación, se sitúa en la franja de dirección de ingeniería o de seguridad
—consulta los rangos de la [ruta CISO](ciso.md#-progresión-de-carrera-y-salario) con la advertencia
que allí se hace— y contrasta con estudios de remuneración que publiquen fecha y metodología.

## ⚠️ Mitos y errores comunes

- **«Es el jefe de AppSec con otro nombre.»** AppSec es una parte. El puesto incluye confianza del
  cliente, divulgación, certificaciones, cadena de suministro y fin de vida del producto.
- **«El CISO corporativo ya cubre esto.»** Rara vez. El CISO protege la organización; el riesgo de
  producto se traslada a terceros y tiene otra audiencia, otras métricas y otro reloj.
- **«Seguridad del producto es pasar el escáner en el pipeline.»** El escáner encuentra una clase
  de fallo. El diseño equivocado no lo encuentra ninguna herramienta.
- **«Publicar un aviso de seguridad daña la marca.»** Lo que daña la marca es que lo publique otro
  antes que tú. La divulgación ordenada es una señal de madurez y los clientes grandes lo saben.
- **«Un programa de recompensas sustituye al programa de seguridad.»** Es un complemento: te dice
  lo que se te escapó, no construye lo que falta.
- **«Certificado quiere decir seguro.»** Certificado quiere decir que un alcance concreto pasó una
  revisión en una fecha concreta. Publica el alcance junto al logotipo.
- **Señal de cargo decorativo:** no puedes bloquear una versión, el paquete de confianza lo
  escribe marketing y te enteras de los hallazgos externos por el equipo de soporte.

## ↔️ Diferencias con los cargos vecinos

| Frente a | Se parecen en | Se separan en |
|---|---|---|
| [**CISO**](ciso.md) | Gobierno, riesgo, comités, respuesta a incidentes | El CISO protege a la organización; el Product CISO protege a los clientes de la organización. Distinta audiencia, distintas métricas |
| [**AppSec Engineer**](appsec.md) | Código, fallos, revisión | AppSec ejecuta dentro del ciclo; el Product CISO **gobierna el programa** y responde ante clientes |
| [**Ingeniero DevSecOps**](devsecops-engineer.md) | Pipeline, SBOM, firma, puertas | El ingeniero **construye** las puertas; el Product CISO **define el criterio** y firma la excepción |
| **Chief Trust Officer** | Confianza del cliente y certificaciones | El Trust Officer comunica y representa; el Product CISO responde por la ingeniería que lo sostiene |
| [**Cloud Security Engineer**](cloud-security.md) | La plataforma donde corre el producto | El ingeniero de nube asegura la infraestructura; el Product CISO, lo que se ejecuta encima y lo que ve el cliente |
| **PSIRT / respuesta a vulnerabilidades** | Avisos, triaje, coordinación | El PSIRT opera el proceso; el Product CISO responde por su existencia y por lo que se comunica |
| [**AI CISO**](ai-ciso.md) | Se solapan si el producto lleva IA | El AI CISO gobierna los sistemas de IA de la organización; el Product CISO, el producto entero, IA incluida |

## 📎 Fuentes y fecha de consulta

Consultadas el **26 de agosto de 2026**.

- [OWASP SAMM](https://owaspsamm.org/) — modelo de madurez con el que se mide y se hace crecer un
  programa de seguridad de producto.
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) —
  convierte «seguro» en requisitos verificables; es la base de los criterios de puerta de
  publicación propuestos en esta guía.
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — clases de fallo de aplicación.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — estructura de gobierno
  y gestión de riesgo aplicable también al riesgo de producto.
- [CISA](https://www.cisa.gov/) — guías de seguridad por diseño y de divulgación coordinada de
  vulnerabilidades.
- [ISO/IEC 27001](https://www.iso.org/standard/27001) — SGSI, base de buena parte de las
  certificaciones que tus clientes te exigirán. Norma de pago: no se reproduce su texto.
- [ISC2](https://www.isc2.org/) — CSSLP y CISSP.
- [Ecosistema CISO de este programa](ecosistema-ciso.md) — taxonomía, matriz comparativa y contexto
  chileno con sus fuentes normativas.

## 🚀 Siguientes pasos

1. Lee el [ecosistema CISO](ecosistema-ciso.md) para situar tu cargo frente al CISO corporativo.
2. Haz el escenario **12** del [laboratorio ejecutivo](../labs/ciso-leadership/README.md).
3. Recorre el [trayecto de Ingeniero DevSecOps](../labs/devsecops-pipeline/TRAYECTO-INGENIERO-DEVSECOPS.md)
   para construir con tus manos las puertas que después gobernarás.
4. Rinde el [examen final de Product CISO](../docs/examen-final-por-rol.md).
5. Si tu producto lleva IA dentro, sigue por [AI CISO](ai-ciso.md); si quieres el mandato
   corporativo completo, por [CISO](ciso.md).

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🗂️ [El ecosistema CISO](ecosistema-ciso.md) — mapa de cargos, matriz comparativa y test del mandato
- 🕸️ [AppSec](appsec.md) · 🏗️ [Ingeniero DevSecOps](devsecops-engineer.md) · 🤖 [AI CISO](ai-ciso.md)
- 🧪 [Laboratorio ejecutivo CISO](../labs/ciso-leadership/README.md) · 🎓 [Evaluación del ecosistema](../labs/ciso-leadership/EVALUACION.md)
- 🏠 [Inicio del programa](../README.md)
