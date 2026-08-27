# 🏭 OT CISO / CISO industrial

> El responsable de la seguridad de la **tecnología operacional**: la planta, el proceso, los
> autómatas, el SCADA, la subestación, la línea de producción, la red de agua. Es la única ruta
> del ecosistema CISO donde un fallo puede **herir a una persona o dañar el medio ambiente**, y
> eso cambia la jerarquía de prioridades por completo: primero la seguridad de las personas,
> después la continuidad del proceso, y solo entonces la confidencialidad.
>
> **Nivel de entrada:** ninguno; se llega desde automatización, infraestructura o seguridad con
> experiencia industrial · **Foco:** inventario pasivo, zonas y conductos, continuidad de proceso
> y convivencia con Operaciones · **Certificación faro:** CISSP como base y las credenciales
> IEC 62443 o GICSP como especialización

**Alias y variantes:** *OT CISO*, *Industrial CISO*, *ICS Security Manager*, *OT Security Lead*,
*Head of OT Security*, *Plant Security Officer*, *Responsable de Ciberseguridad Industrial*.

**Fecha de consulta de las fuentes: 26 de agosto de 2026.**

## 🧭 Qué es y por qué importa

### Definición

El responsable ejecutivo de la ciberseguridad de los sistemas que **miden y controlan procesos
físicos**: sistemas de control industrial (ICS), SCADA, autómatas programables (PLC), sistemas
instrumentados de seguridad (SIS), sensores, historizadores y todo lo que hoy los conecta con el
mundo de la tecnología de la información. Trabaja **con** Operaciones y con Prevención de Riesgos,
no por encima de ellos.

### Nivel de consolidación del título

**Especialización consolidada, con nombres variables.** La función es reconocible y madura en
energía, minería, agua, petróleo y gas, manufactura, transporte y servicios sanitarios. El título
concreto varía; lo que no varía es el contenido: inventario, segmentación, acceso remoto de
proveedores, continuidad de proceso y convivencia con la ingeniería de planta.

Existen dos modelos organizativos habituales, y hay que saber en cuál estás:

| Modelo | Cómo se organiza | Riesgo |
|---|---|---|
| **OT CISO dentro del programa corporativo** | Reporta al [CISO](ciso.md); lleva el dominio OT | Que las políticas de TI se apliquen tal cual a la planta y rompan el proceso |
| **OT CISO dentro de Operaciones** | Reporta a la dirección industrial | Que el programa OT quede desconectado del corporativo y sin visibilidad de amenazas |

El modelo sano es un **doble reporte real**, con objetivos compartidos entre el CISO corporativo y
la dirección de operaciones.

### Qué problema resuelve

| Problema | Por qué es específico de OT | Qué aporta el OT CISO |
|---|---|---|
| Nadie sabe qué hay en la planta | Equipos de veinte años, instalados por proveedores distintos, sin inventario | **Inventario construido de forma pasiva**, sin escanear |
| El escaneo activo tumba un PLC | Muchos autómatas no toleran tráfico inesperado | Reglas claras: qué se puede hacer en producción y qué no |
| El proveedor pide acceso remoto permanente | El mantenimiento depende del fabricante | Acceso mediado, temporal, grabado y aprobado |
| TI parchea el martes; la planta para una vez al año | Las ventanas de mantenimiento son escasas y caras | Gestión de vulnerabilidades **con compensación**, no con parcheo inmediato |
| Un control de seguridad bloquea una parada de emergencia | El control puede matar | Análisis conjunto con seguridad de proceso: la persona manda |
| El ransomware llega a la planta desde la ofimática | La convergencia IT/OT es real | Segmentación con zonas y conductos, y continuidad probada |

### Qué hace y qué no hace

| Sí hace | No hace |
|---|---|
| Inventario y clasificación de activos OT | Operar el proceso: no es ingeniería de automatización |
| Definir zonas, conductos y niveles de seguridad | Modificar la lógica de control |
| Gobernar el acceso remoto de proveedores | Sustituir a Prevención de Riesgos ni a seguridad de proceso |
| Gestionar vulnerabilidades con controles compensatorios | Exigir el parcheo inmediato que la planta no puede absorber |
| Detección y monitoreo específicos de OT | Escanear activamente en producción sin acuerdo y sin ventana |
| Continuidad y recuperación del proceso | Decidir la parada de planta: eso es de Operaciones |
| Preparar y dirigir ejercicios de mesa industriales | Prometer que la planta no se puede detener |
| Traducir el riesgo industrial a la dirección | Aplicar la política de TI sin adaptarla |

### Dónde existe

Energía (generación, transmisión, distribución), minería, agua y saneamiento, petróleo y gas,
manufactura, alimentos y bebidas, celulosa, transporte y logística, ferrocarriles, puertos,
edificios inteligentes y salud con equipamiento crítico. En Chile es una de las especialidades con
más demanda estructural por el peso de la minería, la energía y el agua.

## 🏛️ Mandato, autoridad y responsabilidad

### La regla que ordena todo lo demás

En tecnología de la información la prioridad clásica es **confidencialidad, integridad,
disponibilidad**. En tecnología operacional el orden se invierte y se le antepone algo que en TI
no existe:

```text
1. Seguridad de las personas   (safety)
2. Continuidad del proceso     (disponibilidad)
3. Integridad de los datos de control
4. Confidencialidad
```

**Consecuencia práctica:** un control de ciberseguridad que pueda impedir una parada de
emergencia, retrasar una alarma de proceso o bloquear al operador **no se implanta**, por muy bien
que se vea en la política corporativa. Esta frase es el criterio con el que se evalúa el capstone
de esta ruta.

### Autoridad, presupuesto, equipo y riesgo

- **Autoridad: compartida, siempre.** Ningún cambio entra en la planta sin el acuerdo de
  Operaciones e Ingeniería. Tu palanca no es el veto: es la **evaluación conjunta de riesgo** y el
  hecho de que puedes escalar a la dirección un riesgo que la planta decida no tratar.
- **Presupuesto:** a veces propio, con frecuencia dentro del presupuesto de mantenimiento o de
  proyectos industriales. Es una diferencia importante: allí compites con inversiones de proceso,
  no con proyectos de TI.
- **Equipo:** sí, aunque pequeño y mixto: gente de seguridad que aprende automatización y gente de
  automatización que aprende seguridad. Los segundos son los más difíciles de encontrar y los más
  valiosos.
- **Riesgo:** responde por el riesgo cibernético del entorno OT. La aceptación de un riesgo
  residual la firma la dirección de operaciones, porque es quien responde por el proceso y por las
  personas.

### Conflictos de interés y límites éticos

| Situación | Riesgo | Cómo se maneja |
|---|---|---|
| Un control de seguridad interfiere con una función instrumentada de seguridad | **Puede causar daño físico** | Análisis conjunto con seguridad de proceso; si hay duda, no se implanta |
| Presión para escanear activamente porque «así lo hacemos en TI» | Parada de planta o daño a equipos | Inventario pasivo; escaneo activo solo en ventana, con acuerdo y con respaldo |
| El fabricante condiciona la garantía a no tocar el sistema | Bloqueo del programa de seguridad | Negociar en el contrato **antes** de comprar; documentar el riesgo si no se consigue |
| Un incidente afecta a la producción y hay presión para no reportar | Incumplimiento y riesgo para terceros | El deber de reporte no es negociable; el criterio se define antes de la crisis |
| Se minimiza un riesgo porque la solución es cara y la planta es antigua | Riesgo trasladado en el tiempo | Registrar el riesgo, cuantificarlo y hacer que alguien lo acepte por escrito |
| Se contrata al mismo proveedor para diseñar, implantar y auditar la seguridad OT | Sin independencia | Separar quién audita de quién implanta |

## 🗓️ El día, el mes y el año

**Un día típico.** Revisión de las conexiones nuevas detectadas por el monitoreo pasivo entre la
zona de control y la de supervisión; reunión con el jefe de mantenimiento por una solicitud de
acceso remoto de un fabricante alemán; validación de la lista de activos tras una parada
programada; conversación con TI corporativa para explicar por qué el agente de seguridad de la
estación de ingeniería no puede desplegarse todavía.

**Un mes típico.** Una evaluación de riesgo de un proyecto industrial nuevo; la revisión de la
matriz de conductos tras un cambio; el informe de estado a la dirección de operaciones y al CISO;
una sesión de formación con operadores, que es la actividad con mejor retorno de todo el programa.

**Un año típico.** La revisión completa del modelo de zonas y conductos; la evaluación de riesgo
de la parada mayor de planta, que es tu única ventana real para actuar; un ejercicio de mesa con
Operaciones, Prevención de Riesgos y Comunicaciones; la prueba de recuperación de un sistema de
control desde copia; la reevaluación de los proveedores críticos; y el ciclo presupuestario, donde
peleas contra inversiones de proceso con retorno demostrable.

### Interlocutores

| En planta y operaciones | Corporativos y externos |
|---|---|
| Jefes de planta y de turno | [CISO](ciso.md) corporativo y su equipo |
| Ingeniería de automatización y control | [SOC](soc-blue-team.md) corporativo |
| Mantenimiento | Auditoría interna y riesgo |
| **Prevención de riesgos y seguridad de proceso** | Reguladores y coordinadores sectoriales |
| Operadores: tu mejor fuente de información | Fabricantes de equipos e integradores |
| Compras y contratos de proyectos industriales | Otros operadores del sector: la comunidad OT comparte mucho |

## 🧾 Entregables verificables

| Entregable | Qué demuestra | Cómo se verifica |
|---|---|---|
| **Inventario de activos OT** | Que sabes qué hay | Activo, función, criticidad de proceso, protocolo, versión, dueño y **cómo se descubrió** |
| **Modelo de zonas y conductos** | Que la red está diseñada, no crecida | Por cada conducto: protocolo, sentido, inspección, quién lo aprueba y por qué existe |
| **Matriz de flujos permitidos** | Que la segmentación es aplicable | Contrastable con las reglas de firewall reales |
| **Procedimiento de acceso remoto de proveedores** | Control del vector más usado | Salto, autenticación multifactor, sesión grabada, vigencia y aprobación por operación |
| **Programa de vulnerabilidades con compensación** | Que gestionas lo que no puedes parchear | Por cada vulnerabilidad no parcheable: control compensatorio, dueño y revisión |
| **Análisis de impacto y continuidad de proceso** | Que sabes qué pasa si se cae | Tiempos de recuperación acordados con Operaciones y **probados** |
| **Prueba de recuperación de un sistema de control** | Que la continuidad es real | Cronometrada, desde copia, en equipo limpio |
| **Guion y retrospectiva de un ejercicio de mesa industrial** | Que la crisis se ensayó | Con Operaciones y Prevención de Riesgos en la sala |
| **Registro de riesgos OT** aceptado por Operaciones | Que la responsabilidad está donde debe | Firmas, vigencia y revisión |

## 📏 KPI y KRI

| Indicador | Tipo | Qué dice |
|---|---|---|
| Cobertura del inventario y su antigüedad | KPI | La base de todo lo demás |
| Conductos documentados y contrastados con las reglas reales | KPI | Si la segmentación existe o está en un diagrama |
| Accesos remotos de proveedores mediados y grabados | KPI | Control del vector principal |
| Vulnerabilidades críticas con control compensatorio y dueño | KPI | Gestión realista de lo no parcheable |
| Tiempo de recuperación **probado** frente al acordado | KPI | Continuidad real |
| Cobertura de monitoreo pasivo por zona | KPI | Visibilidad |
| Personal de planta formado | KPI | El control más barato y más eficaz |
| **Conexiones directas entre la red corporativa y la de control** | **KRI** | El fallo estructural clásico |
| **Accesos remotos permanentes de fabricantes** | **KRI** | Puerta trasera contractual |
| Activos sin dueño identificado | **KRI** | Nadie responde por ellos |
| Cambios en planta sin evaluación de riesgo | **KRI** | El programa no está en el proceso de gestión de cambios |
| **Controles de seguridad que interfirieron con una función de seguridad de proceso** | **KRI crítico** | Cualquier valor distinto de cero exige revisión inmediata del programa |

## 🧠 Qué necesitas saber

### Competencias técnicas

- **El proceso industrial de tu sector.** No a nivel de ingeniero, pero sí lo suficiente para saber
  qué pasa si un valor se altera. Sin esto no puedes priorizar nada.
- **Arquitectura de control**: niveles del modelo Purdue, PLC, DCS, SCADA, historizador, HMI,
  estación de ingeniería y sistemas instrumentados de seguridad.
- **Protocolos industriales** y por qué casi ninguno nació con autenticación.
- **Zonas, conductos y niveles de seguridad** según IEC 62443, y cómo se llevan a reglas de
  firewall reales.
- **Descubrimiento pasivo**: captura de tráfico y análisis, porque el escaneo activo no es una
  opción por defecto.
- **Detección específica de OT**: qué es normal en una red de control y qué no; por qué las reglas
  de TI producen ruido inútil aquí.
- **Continuidad y recuperación** de sistemas de control, incluidas las copias de la lógica y de la
  configuración, que es lo que casi nadie respalda.
- **Seguridad física**, porque en OT el acceso al armario es un vector real.

### Competencias de negocio

- Hablar de **producción**: toneladas, megavatios, disponibilidad de línea, coste de parada por
  hora. Es el idioma en el que se toman las decisiones en tu entorno.
- Encajar la seguridad en el **ciclo de inversión industrial**, que es largo y se planifica con
  años de antelación.
- Aprovechar la parada mayor: la mitad de tu plan anual depende de esa ventana.
- Construir el caso económico frente a inversiones de proceso con retorno demostrable, que es una
  competencia mucho más dura que en TI.

### Comunicación y negociación

- Ganarte a los operadores y al jefe de turno. Sin ellos no hay programa; con ellos, casi todo es
  posible.
- Hablar con Prevención de Riesgos en su marco, no en el tuyo.
- Explicar a la dirección un riesgo cibernético en términos de producción, personas y medio
  ambiente.
- Negociar con TI corporativa qué política se adapta y cuál no aplica, sin convertirlo en una
  guerra de territorios.
- Negociar con fabricantes: es donde se gana o se pierde el acceso remoto y la capacidad de
  parchear.

### Competencias regulatorias

Depende del sector y del país: energía, agua, transporte y salud suelen tener reguladores propios
con exigencias específicas, y muchas organizaciones industriales quedan dentro del alcance de la
normativa de servicios esenciales. En Chile, revisa la calificación como **operador de importancia
vital** y los deberes de reporte de la Ley 21.663 en el
[contexto del ecosistema](ecosistema-ciso.md#-contexto-chileno-y-latinoamericano), y comprueba
además lo que exija tu regulador sectorial. **No atribuyas obligaciones a tu cargo sin la norma
delante.**

### Componente comercial

Ninguno. Si compras sistemas de control, el conflicto que sí debes gestionar es el del proveedor
que diseña, instala y luego audita su propia instalación: separa esos papeles por contrato.

## 📚 Tu ruta en el programa

1. **Fundamentos** — [**001**](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md) · [**002** · Panorama de amenazas](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md) · [**003** · Frameworks](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md) · [**025** · Ética y legalidad](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)
2. **El dominio industrial** — [**273** · Seguridad de sistemas de control industrial (ICS/SCADA)](../classes/parte-13-seguridad-movil-iot-e-inalambrica/273-seguridad-de-sistemas-de-control-industrial-ics-scada/README.md) — **la clase central de esta ruta**
   - [**266** · Seguridad de IoT y superficie de ataque](../classes/parte-13-seguridad-movil-iot-e-inalambrica/266-seguridad-de-iot-panorama-y-superficie-de-ataque/README.md) · [**267** · Hacking de firmware](../classes/parte-13-seguridad-movil-iot-e-inalambrica/267-hacking-de-firmware/README.md) · [**268** · Análisis de hardware: UART, JTAG y SPI](../classes/parte-13-seguridad-movil-iot-e-inalambrica/268-analisis-de-hardware-uart-jtag-y-spi/README.md) · [**269** · Radio definida por software](../classes/parte-13-seguridad-movil-iot-e-inalambrica/269-radio-definida-por-software-sdr/README.md)
   - Según tu sector: [**274** · Automotriz y bus CAN](../classes/parte-13-seguridad-movil-iot-e-inalambrica/274-seguridad-automotriz-y-bus-can/README.md) · [**275** · Dispositivos médicos](../classes/parte-13-seguridad-movil-iot-e-inalambrica/275-seguridad-de-dispositivos-medicos/README.md)
3. **La red, que es donde se implementa la segmentación** — [Parte 1](../classes/parte-1-redes-y-seguridad-de-redes/README.md)
   - [**034** · Firewalls](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md) · [**042** · Segmentación y Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md) — **el par que convierte las zonas y conductos en reglas reales**
   - [**036** · VPN y túneles](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md) · [**043** · Network Security Monitoring](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md) · [**044** · Zeek](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md) — **la base del inventario pasivo**
   - [**026** · Wireshark](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md) · [**039** · Ataques de capa 2](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md)
4. **Gobierno, riesgo y continuidad** — [Parte 14](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md)
   - [**283** · Continuidad de negocio y recuperación ante desastres](../classes/parte-14-grc-riesgo-y-cumplimiento/283-continuidad-de-negocio-y-plan-de-recuperacion-ante-desastres/README.md) — **la clase que más pesa en OT**
   - [**277** · Gestión de riesgos](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md) · [**278** · ISO/IEC 27001](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md) · [**279** · NIST CSF](../classes/parte-14-grc-riesgo-y-cumplimiento/279-nist-cybersecurity-framework/README.md) · [**284** · Riesgo de terceros](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md) · [**287** · KPI y KRI](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md)
5. **La capa de dirección** — [Parte 17](../classes/parte-17-profundizacion-para-certificaciones/README.md)
   - [**316** · Modelos de seguridad y arquitectura](../classes/parte-17-profundizacion-para-certificaciones/316-modelos-de-seguridad-y-arquitectura/README.md) · [**329** · Arquitectura empresarial y Zero Trust](../classes/parte-17-profundizacion-para-certificaciones/329-arquitectura-de-seguridad-empresarial-y-zero-trust/README.md) · [**317** · Seguridad física y ambiental](../classes/parte-17-profundizacion-para-certificaciones/317-seguridad-fisica-y-ambiental/README.md)
   - [**315** · MFA y accesos privilegiados](../classes/parte-17-profundizacion-para-certificaciones/315-mfa-y-gestion-de-accesos-privilegiados-pam/README.md) — la base del acceso remoto de proveedores
   - [**318** · Programa de vulnerabilidades](../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md) · [**324** · Hardening y gestión de configuración](../classes/parte-17-profundizacion-para-certificaciones/324-operaciones-de-seguridad-hardening-y-gestion-de-configuracion/README.md) · [**320** · Gobierno y regulación](../classes/parte-17-profundizacion-para-certificaciones/320-gobierno-aspectos-legales-regulatorios-y-gestion-del-programa/README.md) · [**328** · Riesgo cuantitativo y continuidad avanzada](../classes/parte-17-profundizacion-para-certificaciones/328-gestion-de-riesgos-cuantitativa-y-continuidad-avanzada/README.md)
6. **Detección y respuesta**
   - [**182** · Telemetría](../classes/parte-8-blue-team-deteccion-y-soc/182-logging-y-fuentes-de-telemetria/README.md) · [**183** · SIEM](../classes/parte-8-blue-team-deteccion-y-soc/183-siem-arquitectura-y-componentes/README.md) · [**191** · Logs de red y proxy](../classes/parte-8-blue-team-deteccion-y-soc/191-analisis-de-logs-de-red-y-proxy/README.md) · [**197** · Métricas y madurez](../classes/parte-8-blue-team-deteccion-y-soc/197-metricas-y-madurez-del-soc/README.md)
   - [**202** · Ciclo de respuesta](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/202-el-ciclo-de-respuesta-a-incidentes-nist-y-sans/README.md) · [**215** · Playbooks](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/215-playbooks-de-respuesta-a-incidentes/README.md) · [**216** · Contención y recuperación](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/216-contencion-erradicacion-y-recuperacion/README.md) · [**219** · Ejercicios de mesa](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md)
7. **Lo que te va a llegar desde el lado corporativo** — [**170** · Active Directory: enumeración](../classes/parte-7-red-team-y-operaciones-ofensivas/170-active-directory-enumeracion/README.md) · [**258** · Campañas de phishing](../classes/parte-12-osint-e-ingenieria-social/258-campanas-de-phishing-con-gophish/README.md) · [**259** · Defensa contra la ingeniería social](../classes/parte-12-osint-e-ingenieria-social/259-defensa-contra-la-ingenieria-social/README.md)

### Laboratorio y práctica

- 🧪 **[`labs/ciso-leadership`](../labs/ciso-leadership/README.md)** — el escenario **14**
  (incidente OT con continuidad y seguridad física) es el de esta ruta; el **5** (tabletop de
  ransomware) y el **6** (proveedor crítico) son directamente aplicables.
- 🧪 [`redes-nmap`](../labs/redes-nmap/README.md) — úsalo para entender exactamente **qué hace un
  escaneo activo**, que es justo lo que no debes lanzar contra un PLC en producción.
- 🧪 [`blue-team-soc`](../labs/blue-team-soc/README.md) — para diseñar la telemetría que sí puedes
  llevarte de la planta al SOC corporativo.
- 🏗️ La ruta hermana de [**Arquitecto de Ciberseguridad IT/OT**](arquitecto-it-ot.md) incluye el
  montaje de un **PLC simulado** en red aislada y la construcción del modelo Purdue: hazla si
  vienes de seguridad y te falta la planta.

### Capstone

**Un incidente en planta, resuelto con la jerarquía correcta.** Sobre *Minera Alto Cobre* del
laboratorio:

1. **Inventario pasivo** de los activos del escenario, indicando **cómo** se obtuvo cada dato sin
   escaneo activo.
2. **Modelo de zonas y conductos** con la matriz de flujos: por cada conducto, protocolo, sentido,
   inspección y quién lo aprueba.
3. **Procedimiento de acceso remoto** para el fabricante que mantiene el sistema de control.
4. **Registro de riesgos OT** con al menos ocho riesgos, dueño de Operaciones y residual.
5. **Dirección del incidente**: ransomware que llega desde la red corporativa. Documenta las
   decisiones con reloj: qué se aísla, en qué orden, quién autoriza detener o mantener el proceso,
   qué se comunica y **en qué momento se activa el deber de reporte**.
6. **Análisis posterior**: qué control se implantará, cuál se descarta **porque interferiría con la
   seguridad de las personas**, y qué se acepta como riesgo.

**Criterio de aceptación:** (a) ninguna medida propuesta puede interferir con una función
instrumentada de seguridad, y debes demostrar que lo comprobaste; (b) la decisión de detener o
mantener el proceso debe estar tomada por Operaciones, no por ti; (c) el inventario debe ser
íntegramente pasivo. Fallar cualquiera de los tres invalida el capstone, aunque el resto sea
impecable.

### Portafolio

- El inventario pasivo con su método.
- El modelo de zonas y conductos con la matriz de flujos.
- El procedimiento de acceso remoto de proveedores.
- La cronología del incidente con las decisiones y quién las tomó.
- La prueba de recuperación cronometrada de un sistema de control.

## 🎤 Preguntas de entrevista

1. ¿Cómo construyes el inventario de una planta sin escanear?
2. Un control de seguridad podría retrasar una alarma de proceso. ¿Qué haces?
3. El fabricante exige acceso remoto permanente o retira la garantía. ¿Cómo lo resuelves?
4. ¿Quién decide detener la planta durante un incidente?
5. ¿Cómo gestionas una vulnerabilidad crítica en un PLC que no se puede parchear hasta la parada
   anual?
6. ¿Qué respaldos de un sistema de control tienes y cuándo probaste la restauración?
7. ¿Cómo convences al jefe de turno de que esto le sirve?
8. ¿Qué política corporativa de TI has tenido que rechazar y con qué argumento?
9. ¿Cómo diferencias tráfico anómalo de tráfico simplemente inusual en una red de control?
10. ¿Qué obligación de reporte tiene esta organización y quién la firma?

## 🎓 Certificaciones

| Certificación | Para qué sirve en este puesto | Dónde la cubre el programa |
|---|---|---|
| **CISSP** (ISC2) | Base de gestión y credibilidad ejecutiva | [Parte 17](../classes/parte-17-profundizacion-para-certificaciones/README.md) y [**304**](../classes/parte-16-capstones-y-preparacion-de-certificaciones/304-preparacion-cissp-los-8-dominios/README.md) |
| **Credenciales ISA/IEC 62443** | La especialización de referencia del dominio industrial | Conceptos en [**273**](../classes/parte-13-seguridad-movil-iot-e-inalambrica/273-seguridad-de-sistemas-de-control-industrial-ics-scada/README.md); el examen, fuera del programa |
| **GICSP** (GIAC) | Perfil mixto ingeniería-seguridad, muy reconocida en el sector | [**273**](../classes/parte-13-seguridad-movil-iot-e-inalambrica/273-seguridad-de-sistemas-de-control-industrial-ics-scada/README.md) y [Parte 1](../classes/parte-1-redes-y-seguridad-de-redes/README.md) |
| **CISM** (ISACA) | Si el cargo pesa más en gestión del programa | [Parte 14](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md) |
| **ISO/IEC 27001 Lead Implementer** | Si el grupo exige SGSI también en planta | [**278**](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md) |
| Certificación **del fabricante** de tu DCS o SCADA | Requisito práctico frecuente | Fuera del programa |

Ninguna garantiza empleo. En este dominio, lo que más pesa en una entrevista es haber estado en
una planta y saber por qué no se escanea en producción.

## 📈 Progresión de carrera y salario

### Cargos de entrada y experiencia previa razonable

| Vía de origen | Qué traes | Qué te falta |
|---|---|---|
| **Automatización y control** | El proceso, la planta y la confianza de Operaciones | Todo el dominio de seguridad; es la vía más valorada y la que más hay que estudiar |
| [Seguridad de infraestructura](seguridad-infraestructura.md) o redes | Segmentación, monitoreo, hardening | La realidad industrial: protocolos, ventanas, seguridad de proceso |
| [Arquitecto IT/OT](arquitecto-it-ot.md) | El diseño completo | El mandato y la gestión del programa |
| [SOC](soc-blue-team.md) o [DFIR](dfir.md) con casos industriales | Detección y respuesta | Ingeniería de planta y gobierno |

**No existe un número universal de años.** Lo que se comprueba es si has convivido con una planta
en producción y si entiendes por qué una parada cuesta lo que cuesta.

### Hacia dónde sigue

OT CISO → **CISO corporativo** en una empresa industrial, con una especialidad escasa · →
dirección de riesgo operacional industrial · → [arquitecto IT/OT](arquitecto-it-ot.md) principal ·
→ consultoría especializada o [vCISO industrial](vciso.md) · → [Field CISO](field-ciso.md) en un
fabricante de seguridad OT.

### Sobre la remuneración

Este programa no publica cifras propias para este puesto: en el mundo industrial la retribución
depende del sector (minería y energía pagan por encima de manufactura), de la localización de la
faena y de si el cargo incluye disponibilidad permanente. Como referencia orientativa, se sitúa en
la franja de jefatura o dirección técnica industrial; consulta los rangos de la
[ruta CISO](ciso.md#-progresión-de-carrera-y-salario) con su advertencia, y contrasta con estudios
de remuneración con fecha y metodología publicadas. Pregunta siempre por el régimen de turnos y la
disponibilidad: definen el puesto tanto como el sueldo.

## ⚠️ Mitos y errores comunes

- **«OT es como TI pero con máquinas viejas.»** No: la prioridad es distinta, el ciclo de vida es
  de décadas y un error puede herir a alguien.
- **«Hay que parchearlo todo.»** En OT se **gestiona** la vulnerabilidad: se compensa, se segmenta,
  se vigila y se parchea en la ventana. Exigir parcheo inmediato demuestra que no conoces el
  entorno.
- **«Basta con separar la red.»** El aislamiento total ya no existe: hay mantenimiento remoto,
  historizadores, sistemas de gestión y memorias USB. Lo que existe es **segmentación gobernada**.
- **«El escaneo no hace daño.»** Sí lo hace. Hay autómatas que dejan de responder ante tráfico
  inesperado. El inventario se construye de forma pasiva.
- **«La ciberseguridad manda sobre la seguridad de las personas.»** Nunca. Si un control puede
  interferir con una función de seguridad, no se implanta.
- **«Operaciones es el obstáculo.»** Operaciones es tu socio y responde por el proceso y por la
  gente. Un programa OT que se impone contra ellos fracasa siempre.
- **Señal de cargo decorativo:** te nombran responsable de ciberseguridad industrial, no tienes
  acceso a la planta, no participas en la gestión de cambios y tu primer entregable es una política
  copiada de TI.

## ↔️ Diferencias con los cargos vecinos

| Frente a | Se parecen en | Se separan en |
|---|---|---|
| [**CISO**](ciso.md) | Gobierno, riesgo, comités, presupuesto | La jerarquía de prioridades: en OT manda la seguridad de las personas y la continuidad del proceso |
| [**Arquitecto IT/OT**](arquitecto-it-ot.md) | Purdue, zonas y conductos, segmentación | El arquitecto **diseña**; el OT CISO **responde por el programa**, el presupuesto y el riesgo aceptado |
| **Ingeniero de automatización** | La planta y el proceso | El ingeniero opera y modifica el control; tú lo proteges sin tocarlo |
| **Prevención de riesgos / seguridad de proceso** | Ambos protegen a las personas | Aquella disciplina cubre el riesgo físico del proceso; tú, el riesgo cibernético que puede provocarlo. Se coordinan, no se sustituyen |
| [**Seguridad de infraestructura**](seguridad-infraestructura.md) | Redes, firewalls, monitoreo | El alcance IT no tolera lo que el OT sí exige: ventanas escasas, equipos sin parche y protocolos sin autenticación |
| [**SOC corporativo**](soc-blue-team.md) | Detección y respuesta | El SOC de TI no sabe qué es normal en una red de control; hace falta telemetría y reglas propias |
| **Jefe de planta** | Continuidad, producción | El jefe de planta decide detener el proceso; tú aportas el criterio de riesgo para esa decisión |

## 📎 Fuentes y fecha de consulta

Consultadas el **26 de agosto de 2026**.

- [NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security*](https://csrc.nist.gov/pubs/sp/800/82/r3/final)
  — documento público de referencia del dominio: arquitectura, controles y particularidades de OT
  frente a TI.
- [IEC](https://www.iec.ch/) — serie **IEC 62443** sobre seguridad de sistemas de automatización y
  control industrial; de ella provienen los conceptos de zona, conducto y nivel de seguridad usados
  en esta guía. Normas de pago: se explican sus conceptos, no se reproduce su texto.
- [CISA](https://www.cisa.gov/) — avisos de sistemas de control industrial y objetivos de
  desempeño intersectoriales.
- [ENISA](https://www.enisa.europa.eu/) — panorama de amenazas y guías para infraestructura
  crítica.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) — marco de gobierno y de
  evaluación de brecha usado en el capstone.
- [ISO/IEC 27001](https://www.iso.org/standard/27001) — SGSI, cuando el grupo lo exige también en
  planta. Norma de pago.
- Chile: [ANCI](https://anci.gob.cl/) y [CSIRT Nacional](https://www.csirt.gob.cl) para los deberes
  de la [Ley 21.663](https://www.bcn.cl/leychile/navegar?i=1202434) y la calificación como operador
  de importancia vital; más el regulador sectorial que corresponda.
- [Ecosistema CISO de este programa](ecosistema-ciso.md) — taxonomía, matriz comparativa y contexto
  chileno.

## 🚀 Siguientes pasos

1. Lee el [ecosistema CISO](ecosistema-ciso.md) para situar este cargo frente al CISO corporativo.
2. Haz el escenario **14** del [laboratorio ejecutivo](../labs/ciso-leadership/README.md).
3. Si vienes de seguridad y te falta la planta, recorre la ruta de
   [Arquitecto IT/OT](arquitecto-it-ot.md) y monta el PLC simulado.
4. Rinde el [examen final de OT CISO](../docs/examen-final-por-rol.md).
5. Si quieres el mandato corporativo completo, tu página es [CISO](ciso.md).

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🗂️ [El ecosistema CISO](ecosistema-ciso.md) — mapa de cargos, matriz comparativa y test del mandato
- 🏭 [Arquitecto de Ciberseguridad IT/OT](arquitecto-it-ot.md) · 🧱 [Seguridad de Infraestructura](seguridad-infraestructura.md) · 🎩 [CISO](ciso.md)
- 🧪 [Laboratorio ejecutivo CISO](../labs/ciso-leadership/README.md) · 🎓 [Evaluación del ecosistema](../labs/ciso-leadership/EVALUACION.md)
- 🏠 [Inicio del programa](../README.md)
