# 🏢 Organizaciones ficticias del laboratorio ejecutivo

> Todo lo que hay en esta página es **inventado**. Los nombres, las cifras, los incidentes y los
> proveedores no corresponden a ninguna organización real; cualquier parecido es casualidad. Los
> datos están construidos para que los ejercicios tengan una respuesta defendible, no para
> reproducir un caso real.
>
> **Úsalos como datos de entrada.** Cuando un escenario dice «para *Andes Retail*», ven aquí,
> toma el contexto y trabaja con él. Si necesitas un dato que no está, **invéntalo y decláralo
> como supuesto**: hacerlo explícito es parte del ejercicio y de la rúbrica.

## 📇 Índice rápido

| Organización | Sector | Tamaño | Por qué existe en este laboratorio |
|---|---|---|---|
| [Andes Retail](#-andes-retail) | Comercio minorista y comercio electrónico | 4.200 personas | La organización grande con unidades de negocio: sirve para CISO, BISO y AI CISO |
| [NovaPay](#-novapay) | Software de pagos (vende a bancos) | 180 personas | Empresa que **vende** software: Product CISO y Field CISO |
| [Minera Alto Cobre](#-minera-alto-cobre) | Minería | 2.600 personas + contratistas | Entorno industrial: OT CISO y continuidad de proceso |
| [Clínica Los Cipreses](#-clínica-los-cipreses) | Salud privada | 640 personas | Empresa mediana regulada sin CISO: vCISO y fractional |
| [Cumbre Security](#-cumbre-security) | Proveedor de seguridad | 900 personas | El **proveedor**: desde aquí trabaja el Field CISO |

## 🛒 Andes Retail

**Sector:** comercio minorista con red física y canal digital.
**Tamaño:** 4.200 personas. 78 tiendas. Operación en Chile, Perú y Colombia.
**Ingresos anuales (ficticios):** equivalentes a 480 millones de dólares, de los cuales el 31 %
proviene del canal digital y crece un 18 % interanual.

### Estructura

| Unidad de negocio | Qué hace | Responsable |
|---|---|---|
| **Tiendas** | Red física, punto de venta, logística de última milla | Gerencia de Operaciones |
| **Comercio electrónico** | Sitio web, aplicación móvil, marketplace de terceros | Gerencia Digital |
| **Servicios financieros** | Tarjeta propia de la casa comercial, crédito al consumo | Gerencia de Servicios Financieros |
| **Logística** | Dos centros de distribución con automatización | Gerencia de Cadena de Suministro |

### Gobierno y seguridad

- Existe un **CISO** que reporta al Gerente de Tecnología (CIO) y presenta al Comité de Auditoría
  dos veces al año.
- Equipo de seguridad: 6 personas (2 en operación, 2 en gestión de vulnerabilidades, 1 en GRC,
  1 en identidad). Sin SOC propio: monitoreo contratado a un proveedor externo, 12 × 5.
- Presupuesto anual de seguridad (ficticio): 1,4 millones de dólares, de los cuales el 68 % son
  licencias y contratos ya comprometidos.
- Certificaciones: ninguna. La unidad de Servicios Financieros está sujeta a exigencias de su
  regulador y a requisitos de las marcas de tarjetas.
- **No hay BISO.** La Gerencia Digital ha pedido «alguien de seguridad dedicado» tres veces.

### Situación actual (los hechos que te dan los escenarios)

1. La evaluación interna contra NIST CSF 2.0 da un perfil actual bajo en **Gobernar** e
   **Identificar**, medio en **Proteger** y bajo en **Detectar** y **Responder**.
2. El inventario de activos está desactualizado: la última revisión fue hace 19 meses.
3. La autenticación multifactor cubre el 61 % de los usuarios; no cubre a los usuarios de las
   tiendas ni a las cuentas de servicio.
4. Hay **312 vulnerabilidades críticas** abiertas; la más antigua tiene 14 meses.
5. Las copias de seguridad se ejecutan a diario. **La última prueba de restauración completa fue
   hace 2 años y no se documentó.**
6. El proveedor del sistema de punto de venta —*RapidPOS*— tiene acceso remoto permanente a las
   78 tiendas, con una cuenta compartida y sin registro de sesiones.
7. La Gerencia Digital ha desplegado, sin pasar por seguridad: un **asistente de atención al
   cliente** con un modelo de lenguaje de un proveedor externo, un **modelo de detección de
   fraude** entrenado con datos históricos de compra, y un **agente interno** con acceso de
   lectura al repositorio documental. Un cuarto sistema —resumen automático de reclamos— apareció
   en la factura de la nube y nadie sabe quién lo activó.
8. En el sector se han conocido dos incidentes de ransomware con detención de operaciones en los
   últimos doce meses.
9. El seguro cibernético se renueva en cuatro meses y la aseguradora ha pedido evidencia de
   autenticación multifactor, copias inmutables y formación del personal.

### Servicio crítico

El canal digital durante el periodo de mayores ventas del año. Una caída de 24 horas en esa
ventana equivale, según Finanzas, a **4,1 millones de dólares** de ingreso no recuperable, más el
efecto sobre la reputación.

## 💳 NovaPay

**Sector:** software de pagos. Vende una plataforma de procesamiento a bancos, cooperativas y
comercios grandes.
**Tamaño:** 180 personas, de las cuales 110 en ingeniería.
**Modelo:** software como servicio, multiinquilino, alojado en un proveedor de nube pública.
**Clientes:** 34 instituciones, cuatro de ellas bancos supervisados por su regulador financiero.

### Gobierno y seguridad

- Existe un **CISO corporativo** (1 persona, con un analista) que responde por la seguridad
  interna: identidad, endpoint, correo, cumplimiento.
- Existe un **Head of Product Security** con un equipo de 4 personas dentro de ingeniería, que
  reporta al Director de Ingeniería. La empresa está evaluando renombrar ese cargo como **Product
  CISO** y darle línea al comité ejecutivo.
- El ciclo de desarrollo tiene análisis estático y de dependencias en el pipeline; no hay
  modelado de amenazas sistemático ni criterios escritos de puerta de publicación.
- Certificación: la empresa está en el primer año de implantación de un SGSI y aún no ha
  certificado.

### Situación actual

1. Cada cliente grande envía su propio cuestionario de seguridad. Ingeniería dedicó **el
   equivalente a 1,3 personas a tiempo completo** el año pasado a responderlos.
2. No existe una política de divulgación publicada. Dos investigadores externos han reportado
   fallos por el formulario genérico de contacto en los últimos ocho meses; uno de ellos esperó
   siete semanas sin respuesta.
3. El aislamiento entre inquilinos se apoya en un identificador de organización aplicado en la
   capa de aplicación, no en la base de datos. La arquitectura lo sabe; los clientes no lo
   preguntan.
4. La plataforma incorpora **47 dependencias directas** de código abierto. Tres de ellas no
   registran cambios desde hace más de dos años.
5. Comercial ha afirmado por escrito, en al menos una propuesta, que la plataforma «cumple con los
   principales estándares internacionales de seguridad».
6. Se ha detectado una vulnerabilidad crítica en el componente que valida las peticiones de
   liquidación. Afecta a todas las versiones publicadas en los últimos 14 meses. Existe una
   mitigación de configuración. La corrección tarda dos semanas.

### Servicio crítico

El procesamiento de liquidaciones diarias de sus 34 clientes. Un fallo de integridad no detectado
propagaría el error a los libros contables de todos ellos.

## 🪨 Minera Alto Cobre

**Sector:** minería de cobre, faena a rajo abierto con planta concentradora.
**Tamaño:** 2.600 personas propias y aproximadamente 1.900 de empresas contratistas.
**Ubicación:** faena en zona cordillerana; oficinas corporativas en la capital.

### Entorno técnico

| Zona | Qué hay | Notas |
|---|---|---|
| **Corporativa** | Ofimática, correo, sistema de gestión empresarial | Conectada a Internet |
| **Supervisión** | Historizador, servidores de reportes de producción, escritorios de ingeniería | Conectada a la corporativa por un cortafuegos con **12 reglas de origen desconocido** |
| **Control** | Sistema de control distribuido de la planta concentradora, 40 autómatas programables, interfaces de operador | Dos autómatas quedaron sin responder tras un escaneo de red en 2023 |
| **Seguridad de proceso** | Sistema instrumentado de seguridad de la planta | Independiente del control por diseño |
| **Campo** | Sensores, básculas, sistemas de despacho de camiones | Enlaces inalámbricos propietarios |

### Gobierno y seguridad

- Hay un **Jefe de Ciberseguridad corporativo** que reporta al Gerente de TI. La planta **no**
  está dentro de su alcance formal.
- Operaciones tiene un jefe de automatización con tres ingenieros de control. No hay nadie con
  seguridad en su descripción de puesto.
- La empresa está evaluando crear un **OT CISO** con doble reporte a Tecnología y a Operaciones.
- Prevención de Riesgos es una función fuerte, con autoridad reconocida para detener trabajos.

### Situación actual

1. **No existe inventario de activos OT.** El último intento se abandonó tras el incidente del
   escaneo de 2023.
2. Tres fabricantes tienen acceso remoto permanente para mantenimiento. Uno de ellos condiciona la
   garantía del sistema de control a que no se instale software adicional en sus servidores.
3. La parada mayor de planta es **una vez al año, en octubre, y dura once días**. Es la única
   ventana real para intervenir el sistema de control.
4. Existen copias de la configuración del sistema de control en un disco externo en la sala de
   control. Nunca se ha probado una restauración.
5. Una campaña de ransomware afectó a la red corporativa de una empresa del rubro el trimestre
   pasado, con detención de la planta durante seis días.
6. La producción de la planta concentradora equivale, según Finanzas, a **1,8 millones de dólares
   diarios**. Una detención no planificada de un día tiene además un coste de arranque de dos días
   adicionales de rampa.
7. La empresa presta un servicio que podría ser calificado por la autoridad como esencial; la
   calificación no se ha verificado formalmente.

## 🏥 Clínica Los Cipreses

**Sector:** salud privada. Un establecimiento principal y tres centros ambulatorios.
**Tamaño:** 640 personas, de las cuales 40 en tecnología y soporte.
**Ingresos anuales (ficticios):** equivalentes a 62 millones de dólares.

### Gobierno y seguridad

- **No hay CISO.** Hay un Jefe de Informática que responde por todo: infraestructura, sistemas
  clínicos, soporte y —de hecho— seguridad.
- El directorio pidió hace seis meses «un plan de ciberseguridad» tras leer sobre un incidente en
  otra clínica.
- Está evaluando contratar un **vCISO fractional**: presupuesto aprobado para **cuatro días al
  mes durante doce meses**.

### Situación actual

1. La ficha clínica electrónica es de un proveedor externo, alojada en la nube de ese proveedor.
   El contrato no menciona notificación de incidentes.
2. Equipamiento médico conectado a la red general: dos equipos de imagen y un sistema de
   monitorización, todos con sistemas operativos sin soporte del fabricante.
3. La red es plana: la ofimática, los sistemas clínicos y el equipamiento médico comparten
   segmento.
4. Hay 190 usuarios con acceso al sistema clínico; **31 de ellos ya no trabajan en la clínica**.
5. Las copias se hacen en cinta y se llevan a la casa del Jefe de Informática los fines de semana.
6. Un profesional envió por correo personal un listado con datos de 400 pacientes para trabajar
   desde casa. Nadie lo detectó; se supo por un comentario en una reunión.
7. Un cliente institucional (una aseguradora) ha enviado un cuestionario de seguridad de 120
   preguntas como condición para renovar el convenio.

## 🔐 Cumbre Security

**Sector:** proveedor de seguridad. Vende una plataforma de detección y respuesta gestionada, y
servicios profesionales.
**Tamaño:** 900 personas en la región.
**Estructura relevante:** existe una **Oficina del CISO** con cuatro personas, entre ellas dos
**Field CISO** que atienden a las cuentas mayores.

### Cómo se organiza el trabajo del Field CISO

- Reporta a la Oficina del CISO, con línea punteada a la Dirección Comercial.
- Objetivos: 60 % de indicadores de asesoría y contenido, 40 % ligados a la actividad de las
  cuentas asignadas.
- Cartera: entre seis y diez cuentas activas.
- Tiene acceso a la hoja de ruta del producto y participa en su priorización trimestral.

### Situación actual

1. *Andes Retail* es una cuenta objetivo. Cumbre Security vende exactamente el servicio de
   monitoreo gestionado que Andes ya tiene contratado con un competidor.
2. El equipo comercial quiere usar los dos incidentes de ransomware conocidos en el sector como
   argumento de urgencia en la próxima reunión con el CISO de Andes.
3. La evaluación preliminar de Cumbre sobre Andes indica que su mayor riesgo no es la detección
   —que ya tiene, aunque limitada— sino **la ausencia de una prueba de restauración** y la
   cobertura incompleta de autenticación multifactor. Ninguna de las dos cosas la resuelve el
   producto de Cumbre.
4. El producto de Cumbre tiene una limitación conocida: no ingiere los registros del sistema de
   punto de venta que usa Andes sin un desarrollo a medida de seis semanas.

## 🔗 Relacionado

- 🧪 [Laboratorio ejecutivo CISO](README.md) — los catorce escenarios que usan estos datos
- 🧾 [Plantillas reutilizables](PLANTILLAS.md)
- 🎓 [Evaluación del ecosistema CISO](EVALUACION.md)
- 🗂️ [El ecosistema CISO](../../rutas/ecosistema-ciso.md)
