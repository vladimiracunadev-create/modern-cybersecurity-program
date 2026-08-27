# 🏢 Jefe de Infraestructura y Ciberseguridad

> El cargo donde **la misma persona responde por que los sistemas funcionen y por que estén
> seguros**. Diriges la operación de infraestructura —servidores, redes, Microsoft 365, Active
> Directory, virtualización, respaldos y nube— y, a la vez, el gobierno de la seguridad —SGSI
> ISO 27001, monitoreo y respuesta a incidentes, vulnerabilidades, perímetro y concientización—
> en una organización regulada, reportando a la dirección de tecnología.
>
> **Nivel de entrada:** senior; ~5 años de infraestructura TI corporativa, de ellos ≥2 con responsabilidad formal en ciberseguridad, y experiencia coordinando equipos o proveedores · **Foco:** disponibilidad y continuidad, identidad (M365/AD), perímetro, SGSI ISO 27001, incidentes y cumplimiento sectorial · **Certificación faro:** CISSP (+ ISO 27001 Lead Implementer / CISM)
>
> 👔 **¿Buscabas el cargo solo de seguridad?** El [Jefe de Seguridad de la
> Información](ciso-jefe-seguridad.md) dirige el programa de seguridad y **supervisa** la
> infraestructura desde fuera. Aquí la infraestructura **es tuya**: con su presupuesto, su SLA,
> su ventana de cambios y su guardia.

## 🧭 Qué es y por qué importa

> 🗂️ **Una jefatura que opera y protege a la vez.** No es un CISO —respondes por la
> disponibilidad además de por la seguridad—, y esa doble responsabilidad tiene su propia tensión.
> Para situarla frente al resto del ecosistema, incluido el
> [OT CISO](ot-ciso.md) si tu empresa tiene planta, lee
> **[🗂️ El ecosistema CISO](ecosistema-ciso.md)**. Los siete primeros escenarios del
> **[laboratorio ejecutivo](../labs/ciso-leadership/README.md)** son directamente tu trabajo.

En el organigrama de los libros, infraestructura y seguridad son dos áreas distintas: una construye y
opera, la otra define controles y verifica que se cumplan. En una empresa mediana —cien, doscientas,
quinientas personas— **esas dos áreas son una jefatura y un presupuesto**. Este rol es esa jefatura:
el punto donde la disponibilidad y la seguridad dejan de ser dos conversaciones y pasan a ser una
sola persona decidiendo entre ambas con recursos finitos.

El cargo se sostiene sobre tres bloques, y los tres se evalúan:

- **Infraestructura y operación.** Disponibilidad, rendimiento y estabilidad de servidores, redes y
  equipamiento crítico. La administración del entorno **Microsoft 365 y Active Directory** —usuarios,
  accesos, licencias y políticas—, la virtualización, el almacenamiento, los **respaldos y la
  recuperación ante desastres con RTO y RPO acordados**, y la plataforma cloud con la conectividad
  corporativa. Es la parte que se nota cuando falla y que nadie menciona cuando funciona.
- **Ciberseguridad.** Mantener y hacer evolucionar el **SGSI alineado a ISO 27001**, con su análisis
  de riesgos; operar el monitoreo y la detección de amenazas y **liderar la respuesta a incidentes**;
  coordinar la gestión de vulnerabilidades y las pruebas de penetración; administrar el perímetro
  —firewall, segmentación, VPN, accesos remotos—; y ejecutar la concientización, incluidas las
  **simulaciones de phishing** al propio equipo.
- **Cumplimiento y continuidad.** El procedimiento de **notificación de incidentes** ante el
  regulador, las respuestas a auditoría interna, externa y de contrapartes, la **gestión de
  proveedores técnicos** (alcance, SLA, cumplimiento y escalamiento) y la documentación viva de
  políticas, procedimientos y configuraciones.

Hay una tensión estructural que conviene nombrar desde el principio, porque define el oficio: **operas
los controles que después tienes que evidenciar**. Quien administra el firewall y quien certifica que
la regla es correcta son la misma persona. La teoría de control interno llama a eso un problema de
segregación de funciones, y no se resuelve fingiendo que no existe: se gestiona con evidencia
trazable, revisión de terceros —auditoría interna, el auditor externo, la contraparte financiera— y
un comité donde las decisiones de riesgo se aprueban por encima de ti. Por eso la
[clase 285](../classes/parte-14-grc-riesgo-y-cumplimiento/285-auditoria-de-seguridad/README.md) y la
[276](../classes/parte-14-grc-riesgo-y-cumplimiento/276-gobernanza-de-la-seguridad-de-la-informacion/README.md)
pesan más en este cargo que en muchos puestos que suenan más técnicos.

En qué se diferencia de las rutas vecinas de este programa:

- Frente al [Jefe de Seguridad de la Información](ciso-jefe-seguridad.md): ese cargo dirige **solo**
  seguridad, con un equipo de seguridad, y mira la infraestructura desde el otro lado de la mesa. Aquí
  la mitad de tu semana es disponibilidad, licencias, ventanas de cambio y proveedores; la otra mitad,
  riesgo y controles. Si te gusta la seguridad pero no quieres responder por que el correo funcione,
  tu ruta es la otra.
- Frente al [Analista de Seguridad de Infraestructura](seguridad-infraestructura.md): comparten
  terreno técnico casi exacto, y esa ruta es la **antesala natural** de esta. La diferencia es el
  mandato: el analista **ejecuta y propone**; tú **decides, firmas y respondes** —presupuesto,
  contrato de proveedor, aceptación formal de un riesgo, notificación al regulador—.
- Frente al [Arquitecto de Ciberseguridad IT/OT](arquitecto-it-ot.md): el arquitecto **diseña** y
  entrega una memoria; tú vives con lo diseñado a las tres de la madrugada. Cuando este cargo dibuja
  arquitectura, la dibuja sabiendo quién la va a operar y con cuánta gente.
- Frente al [CISO](ciso.md): el CISO tiene mandato del directorio, presupuesto propio e independencia
  de la operación —justamente para poder auditarla—. Este cargo **reporta a tecnología** (en la oferta
  que origina esta guía, al CTO) y opera. Son escalones distintos de la misma escalera, no sinónimos.
- Frente al [Ingeniero SecOps](secops-engineer.md): ese perfil **automatiza con código**. Aquí el
  scripting es una herramienta ocasional; lo que se te paga es criterio, coordinación y respuesta.

Importa porque es **el cargo real de la mayoría de las empresas medianas**, y porque la regulación lo
está volviendo obligatorio. En el sector financiero chileno conviven hoy dos leyes que empujan a que
alguien tenga nombre y apellido detrás de esto: la **Ley 21.663**, marco de ciberseguridad que crea la
Agencia Nacional de Ciberseguridad (ANCI) e impone deberes de reporte de incidentes, y la **Ley
21.719** de protección de datos personales, con su propia autoridad, régimen sancionatorio y entrada
en vigencia diferida. Verifica siempre el texto y el calendario vigentes antes de construir un
procedimiento sobre ellas: el punto para tu carrera es que **el puesto existe por norma, no por moda**,
y que su parte menos técnica —el procedimiento de notificación, el plazo, quién firma— es la que más
rápido se convierte en un problema legal si no está escrita.

> **De dónde sale esta guía.** Está calcada de una oferta real de empleo
> ([Financia Capital, *Jefe de Infraestructura y Ciberseguridad*, Santiago de Chile — Get on Board,
> agosto de 2026](https://www.getonbrd.com/empleos/cybersecurity/jefe-de-infraestructura-y-ciberseguridad-financia-capital-santiago-1e91)):
> empresa de **factoring** y soluciones financieras; el cargo asegura la estabilidad y seguridad de la
> plataforma tecnológica liderando la operación de infraestructura y el gobierno de la seguridad **en
> un entorno financiero regulado (ISO 27001, Ley 21.663, Ley 21.719)**, y **reporta directamente al
> CTO**. Funciones declaradas: disponibilidad y estabilidad de servidores, redes y equipamiento
> crítico; administración de **Microsoft 365 y Active Directory**; virtualización, almacenamiento,
> **respaldos y recuperación ante desastres (RTO/RPO)**; plataforma cloud y conectividad corporativa;
> mantención y evolución del **SGSI ISO 27001** con análisis de riesgos; operación del monitoreo y
> detección de amenazas y liderazgo de la **respuesta a incidentes**; coordinación de **gestión de
> vulnerabilidades y pruebas de penetración**; administración de **firewall, segmentación, VPN y
> accesos remotos**; **campañas de concientización y simulaciones de phishing**; procedimiento de
> **notificación de incidentes conforme a la Ley 21.663 (ANCI)**; respuesta a auditoría interna,
> externa y de contrapartes financieras; **gestión de proveedores técnicos** (alcance, SLA,
> cumplimiento y escalamiento); y documentación de políticas, procedimientos y configuraciones.
> Requisitos: ingeniería en informática, redes, telecomunicaciones o afín; **mínimo 5 años en
> infraestructura TI corporativa, con al menos 2 con responsabilidad formal en ciberseguridad**;
> experiencia **liderando o coordinando equipos o proveedores técnicos**; administración avanzada de
> **M365 y Active Directory**; **firewalls corporativos (Fortinet o equivalente)**; **Windows Server y
> virtualización (VMware, Hyper-V u otro)**; redes aplicadas (**TCP/IP, VLAN, ruteo, DNS/DHCP, WiFi
> corporativa**); y **gestión de respaldos con validación efectiva de restauraciones**. Opcionales:
> implementación de un SGSI ISO 27001, operación de **SIEM** con incidentes reales, **AWS y/o Azure**,
> gestión de vulnerabilidades y coordinación de pentesting, conocimiento de las leyes 21.663 y 21.719,
> administración de Linux y bases de datos, y certificaciones **CISSP, CISM, CEH, ISO 27001 Lead
> Implementer o AWS Security Specialty**. Condiciones publicadas: contrato indefinido, modalidad
> **presencial** en Santiago, nivel **senior**, **USD 2.000–2.500 brutos mensuales**.

## 🗓️ Un día en el puesto

Es un trabajo de **dos relojes a la vez**: el corto —lo que se cayó, lo que hay que aprobar hoy— y el
largo —el plan del SGSI, la auditoría de octubre, el proyecto de segmentación—. La habilidad central
del cargo es que el primero no se coma al segundo.

- **Revisión de la mañana:** estado de los servicios críticos, alertas de la noche, **el resultado de
  los respaldos** y cualquier trabajo que no terminó. Lo primero que se mira no es el firewall: es si
  el respaldo de anoche existe.
- **Cola de accesos:** altas, bajas y cambios en **Microsoft 365 y Active Directory**. Una baja mal
  hecha es un acceso vivo de alguien que ya no trabaja aquí, y es el hallazgo más repetido de todas
  las auditorías del mundo.
- **Cambios en el perímetro:** una regla de firewall que pide un proyecto, una VPN para un proveedor,
  un acceso remoto temporal. Cada uno con su justificación, su vigencia y su registro; el "temporal"
  sin fecha de caducidad es la deuda de seguridad que más crece.
- **Algo del monitoreo:** una alerta que investigar, un patrón raro, un equipo que empezó a autenticar
  desde donde no debería. Decides si es ruido, si se contiene o si se abre incidente.
- **Reunión con un proveedor:** el del datacenter, el del enlace, el del SOC gestionado o el del ERP.
  Se revisa cumplimiento de SLA, tickets abiertos y escalamientos, y se documenta.
- **Un bloque del plan:** el avance del SGSI, un hallazgo de auditoría que cerrar con evidencia, la
  política que falta redactar, el análisis de riesgos que toca actualizar.
- **Una decisión con dinero:** renovar licencias, dimensionar el respaldo, comprar el EDR o estirar un
  año más el equipamiento. Casi siempre con menos presupuesto del que el riesgo justificaría, y
  siempre teniendo que explicarlo por escrito.
- **Lo que nadie ve:** la **prueba de restauración**. Un respaldo que nunca se restauró es una
  hipótesis, no un control; probarlo es la tarea más fácil de postergar y la más cara de no haber
  hecho.

Y el ritmo largo: **mensual**, el reporte a la dirección de tecnología con indicadores y estado del
plan; **trimestral**, la revisión de accesos, la campaña de phishing y el escaneo de vulnerabilidades
con su plan de remediación; **anual**, la auditoría, el pentest contratado, el simulacro de
continuidad y la revisión del análisis de riesgos. Cuando entra un incidente serio, todo eso se
detiene y **tú diriges**: contención, comunicación interna, decisión de notificar al regulador y,
después, causa raíz.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Redes corporativas de verdad.** TCP/IP y subnetting ([010](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md),
  [014](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md)),
  **DNS y DHCP** ([012](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md),
  [041](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md)),
  VLAN y sus límites reales ([039](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md))
  y **WiFi corporativa** ([038](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md)).
- **Perímetro y acceso remoto.** Firewalls ([034](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md)),
  **VPN e IPsec/WireGuard** ([036](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md)),
  IDS/IPS ([035](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md)) y
  **segmentación con criterio zero trust** ([042](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md),
  [329](../classes/parte-17-profundizacion-para-certificaciones/329-arquitectura-de-seguridad-empresarial-y-zero-trust/README.md)).
- **Identidad, que es el perímetro real.** Ciclo de vida de identidades ([313](../classes/parte-17-profundizacion-para-certificaciones/313-gestion-del-ciclo-de-vida-de-identidades-iam-empresarial/README.md)),
  **MFA y accesos privilegiados** ([315](../classes/parte-17-profundizacion-para-certificaciones/315-mfa-y-gestion-de-accesos-privilegiados-pam/README.md))
  e **IAM en la nube** ([222](../classes/parte-10-seguridad-en-la-nube-y-contenedores/222-iam-en-la-nube-identidades-roles-y-permisos/README.md)).
  Y saber **cómo se ataca un Active Directory** —enumeración, Kerberoasting, Pass-the-Hash—
  ([170](../classes/parte-7-red-team-y-operaciones-ofensivas/170-active-directory-enumeracion/README.md),
  [171](../classes/parte-7-red-team-y-operaciones-ofensivas/171-active-directory-kerberoasting-y-ataques-a-kerberos/README.md),
  [172](../classes/parte-7-red-team-y-operaciones-ofensivas/172-active-directory-pass-the-hash-y-pass-the-ticket/README.md)):
  no para atacarlo, sino porque **administras el objetivo número uno** de cualquier intrusión.
- **Windows y sus registros.** Arquitectura, registro y servicios ([008](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md)),
  PowerShell ([009](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md))
  y **Event Logs y Sysmon** ([190](../classes/parte-8-blue-team-deteccion-y-soc/190-analisis-de-logs-de-windows-event-logs-y-sysmon/README.md)).
  Linux y bases de datos aparecen como deseables y, en la práctica, siempre acaban dentro del alcance
  ([005](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md)).
- **Continuidad, no solo respaldo.** BIA, RTO y RPO, plan de recuperación y su prueba
  ([283](../classes/parte-14-grc-riesgo-y-cumplimiento/283-continuidad-de-negocio-y-plan-de-recuperacion-ante-desastres/README.md),
  [328](../classes/parte-17-profundizacion-para-certificaciones/328-gestion-de-riesgos-cuantitativa-y-continuidad-avanzada/README.md)).
  La oferta lo dice con todas las letras: **validación efectiva de restauraciones**.
- **Nube híbrida.** Responsabilidad compartida ([221](../classes/parte-10-seguridad-en-la-nube-y-contenedores/221-fundamentos-de-seguridad-en-la-nube-y-responsabilidad-compartida/README.md)),
  **Azure** ([224](../classes/parte-10-seguridad-en-la-nube-y-contenedores/224-seguridad-en-azure/README.md)) y AWS
  ([223](../classes/parte-10-seguridad-en-la-nube-y-contenedores/223-seguridad-en-aws/README.md)), postura
  ([231](../classes/parte-10-seguridad-en-la-nube-y-contenedores/231-cloud-security-posture-management-cspm/README.md)),
  secretos ([233](../classes/parte-10-seguridad-en-la-nube-y-contenedores/233-gestion-de-secretos-en-la-nube/README.md))
  y **logging y respuesta en la nube** ([234](../classes/parte-10-seguridad-en-la-nube-y-contenedores/234-logging-y-deteccion-en-la-nube/README.md),
  [235](../classes/parte-10-seguridad-en-la-nube-y-contenedores/235-respuesta-a-incidentes-en-la-nube/README.md)).
- **Monitoreo y respuesta.** Telemetría ([182](../classes/parte-8-blue-team-deteccion-y-soc/182-logging-y-fuentes-de-telemetria/README.md)),
  **arquitectura del SIEM** ([183](../classes/parte-8-blue-team-deteccion-y-soc/183-siem-arquitectura-y-componentes/README.md)),
  EDR ([189](../classes/parte-8-blue-team-deteccion-y-soc/189-analisis-de-endpoints-con-edr/README.md)),
  métricas ([197](../classes/parte-8-blue-team-deteccion-y-soc/197-metricas-y-madurez-del-soc/README.md)) y el
  **ciclo completo de incidentes** ([202](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/202-el-ciclo-de-respuesta-a-incidentes-nist-y-sans/README.md),
  [215](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/215-playbooks-de-respuesta-a-incidentes/README.md),
  [216](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/216-contencion-erradicacion-y-recuperacion/README.md),
  [217](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/217-analisis-de-causa-raiz/README.md)).
- **Vulnerabilidades y pentest, coordinados.** El programa completo
  ([318](../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md)),
  el escaneo ([071](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md)),
  el **hardening y la gestión de configuración** ([324](../classes/parte-17-profundizacion-para-certificaciones/324-operaciones-de-seguridad-hardening-y-gestion-de-configuracion/README.md))
  y, del lado del contrato, **alcance y reglas de engagement** ([067](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md))
  y cómo se lee un informe de pentest ([085](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md)).
- **SGSI y cumplimiento.** ISO 27001 e implantación ([278](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md)),
  análisis de riesgos ([277](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md)),
  políticas y procedimientos ([282](../classes/parte-14-grc-riesgo-y-cumplimiento/282-politicas-estandares-y-procedimientos/README.md)),
  **riesgo de terceros** ([284](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md)),
  auditoría ([285](../classes/parte-14-grc-riesgo-y-cumplimiento/285-auditoria-de-seguridad/README.md)),
  privacidad ([289](../classes/parte-14-grc-riesgo-y-cumplimiento/289-privacidad-y-proteccion-de-datos/README.md))
  y el marco legal y regulatorio del programa ([320](../classes/parte-17-profundizacion-para-certificaciones/320-gobierno-aspectos-legales-regulatorios-y-gestion-del-programa/README.md)).
- **Factor humano.** Cultura y concientización ([286](../classes/parte-14-grc-riesgo-y-cumplimiento/286-concienciacion-y-cultura-de-seguridad/README.md)),
  análisis de phishing ([319](../classes/parte-17-profundizacion-para-certificaciones/319-analisis-avanzado-de-phishing-y-correo-malicioso/README.md))
  y **cómo se monta una simulación** ([258](../classes/parte-12-osint-e-ingenieria-social/258-campanas-de-phishing-con-gophish/README.md),
  [259](../classes/parte-12-osint-e-ingenieria-social/259-defensa-contra-la-ingenieria-social/README.md)),
  con la ética y los límites por delante ([025](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)):
  una campaña interna mal comunicada destruye la confianza que pretendía construir.

### Herramientas del oficio

| Familia | Lo típico en el puesto | Qué te da el programa |
|---|---|---|
| Directorio e identidad | Active Directory, Entra ID, Microsoft 365, PAM | El **modelo** (313, 315) y **cómo se ataca AD** (170–172, 190); no la consola |
| Perímetro | Fortinet, Palo Alto, Cisco; VPN y accesos remotos | Los conceptos con práctica real en iptables/nftables (034), VPN (036) y segmentación (042) |
| Virtualización y servidores | VMware, Hyper-V, Windows Server | Virtualización de laboratorio (004) y Windows a fondo (008, 009) |
| Respaldo y DR | Veeam u equivalente, réplicas, sitio alterno | El **marco de continuidad** con RTO/RPO y su prueba (283, 328) |
| Monitoreo | Sentinel, Wazuh, Elastic, Splunk; EDR/XDR | Arquitectura del SIEM y dos implementaciones montables (183–185), EDR (189) |
| Vulnerabilidades | Nessus, Qualys, Tenable | Escaneo real (071) y el programa que lo ordena (318) |
| Nube | Azure y AWS, CSPM | 221–224, 231, 233–235 |
| Concientización | GoPhish, plataformas de formación | Campaña completa (258) y defensa (259, 286, 319) |
| Gobierno | Registro de riesgos, SoA, políticas, matriz de proveedores | 276–289 y 320: el cuerpo documental entero |

### Habilidades no técnicas

Son la mitad del cargo, y la mitad por la que se descarta a candidatos técnicamente buenos:

- **Liderar sin ser quien ejecuta.** Un equipo pequeño, o ninguno, y varios proveedores. Delegar,
  revisar y sostener la calidad ajena es una habilidad distinta a hacerlo tú.
- **Contratos y SLA.** Definir alcance, medir cumplimiento, escalar y —cuando toca— cambiar de
  proveedor. La [clase 284](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md)
  es la teoría; la práctica es una reunión mensual con una tabla de incumplimientos delante.
- **Escribir.** Políticas, procedimientos, runbooks, informes a dirección y respuestas a auditoría. En
  este cargo, **lo que no está escrito no existe** para el auditor ni para el regulador.
- **Traducir riesgo a decisión.** Explicar en cinco minutos qué se compra, qué se acepta y qué pasa si
  no se hace nada, en el idioma de quien firma el presupuesto
  ([321](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md),
  [287](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md)).
- **Dirigir una crisis.** Coordinar, decidir con información incompleta, comunicar hacia arriba y
  hacia el negocio, y saber **cuándo hay que notificar** al regulador. Se entrena con el
  [tabletop (219)](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md).
- **Decir que no, con alternativa.** El "no" sin propuesta convierte la seguridad en el área que
  estorba, y a la tercera vez el negocio deja de preguntar.

## 📚 Tu ruta en el programa

**No es una ruta de entrada.** Se llega desde infraestructura —administración de sistemas y redes— o
desde el [Analista de Seguridad de Infraestructura](seguridad-infraestructura.md), y se le añaden la
capa de gobierno y la de respuesta. Si vienes de sistemas, la mitad técnica es repaso y tu esfuerzo va
a las Partes 14 y 17; si vienes de seguridad, ocurre al revés.

1. 📚 [**Parte 0 — Fundamentos**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md) (001–025)
   · el cimiento común: **003 frameworks (NIST CSF, ISO 27001)**, virtualización (004), Linux (005),
   **Windows (008)** y PowerShell (009), redes (010–014), criptografía con intuición (021) y **ética y
   límites (025)** para las simulaciones internas.
2. 📚 [**Parte 1 — Redes y seguridad de redes**](../classes/parte-1-redes-y-seguridad-de-redes/README.md)
   (026–045) · lo que administras a diario: **034 firewalls**, **036 VPN**, **042 segmentación y zero
   trust**, 035 IDS/IPS, 039 capa 2 y VLAN, 041 DNS, 038 WiFi corporativa, 043 NSM.
3. 📚 [**Parte 14 — GRC, riesgo y cumplimiento**](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md)
   (276–290) · **el bloque de gobierno, casi entero**: **278 ISO 27001** (el SGSI que mantienes), 277
   riesgos, 276 gobernanza, 279 NIST CSF, 280 CIS, 282 políticas, **283 continuidad y DRP**, **284
   proveedores**, **285 auditoría**, 286 cultura, 287 KPI/KRI y 289 privacidad.
4. 📚 [**Parte 17 — Profundización**](../classes/parte-17-profundizacion-para-certificaciones/README.md)
   · la capa de jefatura: **320 gobierno y regulación** (el terreno del regulador y del auditor),
   **318 programa de vulnerabilidades**, **324 hardening y configuración**, **313/315 identidades, MFA
   y PAM**, **319 phishing**, **321 reporte**, **328 continuidad avanzada**, **329 arquitectura y zero
   trust**, 317 seguridad física.
5. 📚 [**Partes 8 y 9 — Detección y respuesta**](../classes/parte-8-blue-team-deteccion-y-soc/README.md)
   · **182 telemetría**, **183 SIEM**, 186 Sigma, **189 EDR**, **190 logs de Windows**, 196 SOAR, 197
   métricas · y el ciclo que diriges: **202**, **215 playbooks**, **216 contención**, **217 causa
   raíz**, **219 tabletop**, 220 caso completo.
6. 📚 [**Parte 10 — Nube**](../classes/parte-10-seguridad-en-la-nube-y-contenedores/README.md) · 221
   responsabilidad compartida, **222 IAM**, **224 Azure** (el terreno de M365/Entra), 223 AWS, 231
   CSPM, 233 secretos, **234 logging** y **235 respuesta a incidentes en la nube**.
7. 📚 [**Partes 3, 7 y 12 — Lo que contratas y lo que te atacan**](../classes/parte-3-hacking-etico-y-pentesting-metodologia/README.md)
   · **067 alcance y contratos** y **085 reporte** (para comprar y leer un pentest), **071 Nessus** ·
   **170–172 ataques a Active Directory** (para hardenizar con criterio) · **258 GoPhish** y **259
   defensa** (para la campaña interna).

Clases concretas por las que empezar:

- 📕 [278 · ISO/IEC 27001 e implantación de un SGSI](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md) — el marco que la oferta nombra literalmente y el que sostiene todo lo demás.
- 🔁 [283 · Continuidad de negocio y recuperación ante desastres](../classes/parte-14-grc-riesgo-y-cumplimiento/283-continuidad-de-negocio-y-plan-de-recuperacion-ante-desastres/README.md) — RTO/RPO, y la diferencia entre tener respaldos y poder volver.
- 🔐 [313 · Ciclo de vida de identidades](../classes/parte-17-profundizacion-para-certificaciones/313-gestion-del-ciclo-de-vida-de-identidades-iam-empresarial/README.md) y [315 · MFA y PAM](../classes/parte-17-profundizacion-para-certificaciones/315-mfa-y-gestion-de-accesos-privilegiados-pam/README.md) — el alta, la baja y el privilegio: ahí vive la mitad de los hallazgos de auditoría.
- 🧱 [034 · Firewalls](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md), [036 · VPN y túneles](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md) y [042 · Segmentación y zero trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md) — el perímetro que administras, con el criterio de por qué una VLAN no es una frontera.
- 🎯 [170 · Enumeración de Active Directory](../classes/parte-7-red-team-y-operaciones-ofensivas/170-active-directory-enumeracion/README.md) y [172 · Pass-the-Hash y Pass-the-Ticket](../classes/parte-7-red-team-y-operaciones-ofensivas/172-active-directory-pass-the-hash-y-pass-the-ticket/README.md) — ver tu propio dominio como lo ve quien entra.
- 🔎 [182 · Telemetría](../classes/parte-8-blue-team-deteccion-y-soc/182-logging-y-fuentes-de-telemetria/README.md) y [183 · SIEM](../classes/parte-8-blue-team-deteccion-y-soc/183-siem-arquitectura-y-componentes/README.md) — para exigirle a la plataforma de monitoreo lo que puede dar, la operes tú o un SOC gestionado.
- 🚨 [215 · Playbooks](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/215-playbooks-de-respuesta-a-incidentes/README.md) y [219 · Ejercicios de mesa](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md) — el procedimiento escrito y el ensayo con reloj, incluido el punto en que se decide notificar.
- ⚖️ [320 · Gobierno, aspectos legales y regulatorios](../classes/parte-17-profundizacion-para-certificaciones/320-gobierno-aspectos-legales-regulatorios-y-gestion-del-programa/README.md) y [289 · Privacidad y protección de datos](../classes/parte-14-grc-riesgo-y-cumplimiento/289-privacidad-y-proteccion-de-datos/README.md) — el andamiaje conceptual sobre el que se apoyan las leyes locales.
- 🤝 [284 · Riesgo de terceros y proveedores](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md) — porque buena parte de tu infraestructura la opera alguien más.
- 🩹 [318 · Programa de vulnerabilidades](../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md) y [324 · Hardening y gestión de configuración](../classes/parte-17-profundizacion-para-certificaciones/324-operaciones-de-seguridad-hardening-y-gestion-de-configuracion/README.md) — el ciclo que coordinas y la línea base que defiendes.

### Laboratorio y práctica

La práctica de este rol mezcla consola y carpeta: la mitad se demuestra montando, la otra mitad
escribiendo.

- 🧪 [`blue-team-soc`](../labs/blue-team-soc/README.md) — **conecta tú las fuentes** (Windows, Linux, un
  dispositivo de red), verifica la ingesta y lleva una alerta hasta el cierre. Es lo más cercano a la
  plataforma de monitoreo que vas a supervisar.
- 🧪 [`redes-nmap`](../labs/redes-nmap/README.md) — inventario y superficie expuesta de tu propia red:
  el ejercicio que descubre el servicio publicado que nadie recordaba.
- 🧪 [`rootcause-windows`](../labs/rootcause-windows/README.md) — el endpoint Windows por dentro:
  controles, EDR, artefactos y causa raíz.
- 🧪 [`cloud-security`](../labs/cloud-security/README.md) — postura de nube y CSPM, el tipo de informe
  que revisarás cada trimestre.
- 🎲 [219 · Tabletop](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md)
  — **dirige** un simulacro de ransomware con roles, reloj y el punto de decisión de notificar al
  regulador. En este cargo es un examen, no un juego.
- 📋 **Los entregables del puesto**, construidos sobre una organización ficticia: análisis de riesgos,
  declaración de aplicabilidad, política de accesos, **procedimiento de notificación de incidentes**,
  plan de continuidad con RTO/RPO, matriz de proveedores con SLA y un informe mensual de una página.
  En una entrevista de este nivel pesan más que cualquier laboratorio.
- 💾 **La prueba que casi nadie hace:** monta un respaldo en el laboratorio, **restáuralo en una
  máquina limpia y cronometra**. Ese número —cuánto tardaste y qué faltó— es la respuesta a lo que la
  oferta llama "validación efectiva de restauraciones".

## 🎓 Certificaciones

La oferta las lista como **opcionales**, y conviene leer eso con precisión: no filtran la candidatura,
pero desempatan y sostienen tu credibilidad ante auditoría.

- **CISSP** — la que mejor describe el cargo por amplitud (seguridad, operaciones, arquitectura,
  continuidad, gobierno). El programa la mapea dominio a dominio en
  [`certificaciones/cissp.md`](../certificaciones/cissp.md). Exige experiencia acreditada, así que es
  una meta de medio plazo, no un atajo.
- **CompTIA Security+** → **CySA+** — la base y el escalón intermedio si vienes de infraestructura y
  te falta el vocabulario formal de seguridad. Mapeadas en
  [`certificaciones/comptia-security-plus-sy0-701.md`](../certificaciones/comptia-security-plus-sy0-701.md)
  y [`certificaciones/comptia-cysa-plus-cs0-003.md`](../certificaciones/comptia-cysa-plus-cs0-003.md).
- **Fuera del programa, pero nombradas en la oferta:** **ISO 27001 Lead Implementer** (la más alineada
  con "mantener y evolucionar el SGSI"), **CISM** (gestión, si tu carrera apunta a CISO), **CEH**
  (funciona sobre todo como filtro de recursos humanos) y **AWS Security Specialty** si el entorno
  cloud pesa.
- **Del fabricante, según tu stack:** Fortinet (NSE/FCP), Microsoft **AZ-800** (infraestructura Windows
  Server híbrida), **SC-300** (identidad) y **MS-102** (administración de M365). Ninguna la cubre este
  programa, y son las que más rápido se notan en el día a día.

## 📈 Progresión de carrera y salario

Ruta habitual: **Administrador de sistemas o redes → Coordinador o Jefe de Infraestructura → Jefe de
Infraestructura y Ciberseguridad → Subgerencia de TI / [CISO](ciso.md) / dirección de tecnología**. Es
un cargo de doble salida: si te tira el gobierno, el paso siguiente es
[Jefe de Seguridad de la Información](ciso-jefe-seguridad.md) y después CISO; si te tira la
tecnología, es jefatura o gerencia de TI. Desde aquí también se cruza con facilidad a
[Cloud Security](cloud-security.md) cuando el entorno híbrido acaba pesando más que el datacenter.

**Dato verificable, no estimación:** la oferta que origina esta guía publica **USD 2.000–2.500 brutos
mensuales** (≈ USD 24k–30k anuales) para un cargo **senior presencial en Santiago**, en agosto de
2026. Sirve como ancla concreta; el resto son rangos **orientativos**, que varían por sector, tamaño,
madurez y si el cargo lleva guardia:

```text
Contexto                               Jefatura de infraestructura   Jefatura de infra + ciberseguridad
-------------------------------------  ---------------------------   ----------------------------------
Chile (empresa mediana)                USD 20k - 30k / anio          USD 24k - 36k / anio
Chile (banca, seguros, retail grande)  USD 28k - 45k / anio          USD 34k - 55k+ / anio
Espana                                 EUR 38k - 50k / anio          EUR 45k - 65k+ / anio
Remoto (USD)                           USD 55k - 90k / anio          USD 70k - 120k+ / anio
```

Dos variables mueven el rango más que la antigüedad: **el tamaño del equipo y del presupuesto que
gestionas**, y **la regulación del sector** —un cargo que responde ante un regulador y ante
contrapartes financieras se paga por encima del mismo cargo en una empresa no regulada, a cambio de
una carga de evidencia constante—.

## ⚠️ Mitos y errores comunes

- **"Es una jefatura de soporte con un firewall encima."** No: es responsabilidad formal sobre
  continuidad y sobre cumplimiento. Cuando hay incidente, la pregunta de la dirección no es cuántos
  tickets se cerraron, sino cuánto se tardó en volver y a quién hubo que notificar.
- **"Tengo respaldos, tengo continuidad."** Un respaldo no probado es una hipótesis. La continuidad se
  demuestra con una **restauración cronometrada** contra un RTO acordado; sin ese número, no hay plan.
- **"El SGSI es papeleo."** El papeleo es el síntoma de hacerlo mal. Bien hecho, el SGSI es el
  inventario de lo que tienes, de quién accede y de qué controles existen — exactamente lo que te
  falta la noche de un incidente.
- **"Con MFA ya está resuelto."** El MFA corta el robo de credenciales simple; no el token robado, ni
  la cuenta de servicio sin segundo factor, ni el privilegio excesivo acumulado durante años.
- **"Yo administro y yo audito."** Es el conflicto estructural del cargo. No se resuelve con
  confianza: se resuelve con evidencia, revisión independiente y decisiones de riesgo aprobadas por
  encima de ti.
- **"La nube ya viene segura."** El proveedor responde por la infraestructura; la configuración, las
  identidades y los datos son tuyos
  ([221](../classes/parte-10-seguridad-en-la-nube-y-contenedores/221-fundamentos-de-seguridad-en-la-nube-y-responsabilidad-compartida/README.md)).
- **"Contratamos un pentest, estamos cubiertos."** Un pentest es una foto con fecha y alcance. Sin
  remediación verificada y sin repetición, es un documento caro
  ([067](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md),
  [085](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md)).
- **"Lo opera el proveedor, así que es su problema."** La operación se delega; la responsabilidad, no
  ([284](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md)).
- **"La simulación de phishing es para pillar a la gente."** Si el equipo la vive como una trampa,
  dejará de reportar lo real. Se diseña para medir y enseñar, con el programa comunicado de antemano y
  sin exponer nombres.

> **Honestidad, sin marketing:** este programa te da **el criterio completo del cargo** —redes y
> perímetro, identidad y PAM, ataque y defensa de Active Directory, telemetría y SIEM, EDR, ciclo de
> incidentes y tabletop, vulnerabilidades y hardening, nube en Azure y AWS, ISO 27001 y el SGSI,
> riesgos, continuidad con RTO/RPO, proveedores, auditoría, privacidad, métricas y reporte—. Lo que
> **no** te da: la **administración de Microsoft 365, Entra ID y Active Directory como consola** (el
> programa mira AD desde el ataque y desde el log, no desde la operación diaria); **VMware y
> Hyper-V**; la operación de una **plataforma de respaldo** comercial; **Fortinet u otro firewall como
> producto**; el texto y el calendario concretos de la **Ley 21.663 y la Ley 21.719** —se enseña el
> marco de cumplimiento y de privacidad, no la norma chilena artículo por artículo—; la **titulación**
> que se exige como requisito formal; y los **5 años de infraestructura corporativa con 2 de
> responsabilidad en seguridad**, que no los sustituye ningún curso. El programa te hace capaz de
> **dirigir y de defender tus decisiones**; el producto concreto y los años los pones tú.

## 🚀 Siguientes pasos

1. **Sitúa tu punto de partida.** Si vienes de sistemas, tu déficit está en las Partes 14 y 17; si
   vienes de seguridad, en la operación de infraestructura y en el trato con proveedores. Empieza por
   el lado que te falta, no por el que disfrutas.
2. **Haz la Parte 14 casi entera**, con **278 (ISO 27001)** y **283 (continuidad)** como prioridad:
   son las dos que la oferta menciona de forma explícita.
3. **Cierra el perímetro y la identidad**: 034, 036 y 042 por un lado; 313 y 315 por el otro. Después
   mira tu propio dominio con 170–172 y anota lo que encuentres.
4. **Monta [`blue-team-soc`](../labs/blue-team-soc/README.md) y conecta las fuentes tú.** Rompe una a
   propósito y mide cuánto tardas en notarlo: esa cifra es la salud real de tu monitoreo.
5. **Haz la prueba de restauración completa** y escribe el runbook con el tiempo real que tardaste. Es
   el entregable más convincente que puedes llevar a una entrevista de este cargo.
6. **Escribe el paquete documental** sobre una organización ficticia: análisis de riesgos, política de
   accesos, **procedimiento de notificación de incidentes** y matriz de proveedores con SLA. Cuatro
   documentos, no cuarenta.
7. **Dirige un [tabletop (219)](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/219-ejercicios-de-mesa-tabletop/README.md)**
   con gente real —aunque sean colegas— y cronometra las decisiones, incluido el momento de notificar.
8. **Súmale la nube** (221, 222, 224, 234) y planifica después la certificación según hacia dónde
   crezcas: **ISO 27001 Lead Implementer** si tu norte es el SGSI, **CISSP o CISM** si es la jefatura
   de seguridad, **AZ-800 / SC-300** si es la infraestructura Microsoft.

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🧱 [Escalón previo: Analista de Seguridad de Infraestructura](seguridad-infraestructura.md) · 👔 [Rol hermano, solo seguridad: Jefe de Seguridad de la Información](ciso-jefe-seguridad.md) · 🎩 [Techo de carrera: CISO](ciso.md)
- 🎓 [Examen final de este rol](../docs/examen-final-por-rol.md) · 🏠 [Inicio del programa](../README.md)
