# Soluciones — Parte 17: Profundización para certificaciones

> Estas son **claves de referencia** para el instructor y para autoevaluación. **Intenta resolver cada reto y ejercicio por tu cuenta antes de mirar aquí**: el valor está en el proceso, no en la respuesta. Puede haber más de una solución correcta; lo que sigue es una guía técnicamente válida.
>
> Volver al índice de la parte: [../classes/parte-17-profundizacion-para-certificaciones/README.md](../classes/parte-17-profundizacion-para-certificaciones/README.md)

Esta parte es mayoritariamente de **gobierno, arquitectura y evaluación (GRC/DFIR)**: los "entregables" son políticas, matrices, mapeos y pipelines documentados, no comandos. Donde hay laboratorio técnico (clases 325–327, 330) todo se hace en **entorno aislado y sobre activos propios o autorizados por escrito**.

---

## Clase 311 — Clasificación y ciclo de vida de los datos

### Solución del reto verificable

La **Política de Clasificación de Datos** de NovaSalud se construye con cinco piezas encadenadas:

1. **Esquema de 4 niveles** (`Público`, `Interno`, `Confidencial`, `Restringido`). Cada nivel se define con: criterio objetivo de asignación, ejemplos concretos, impacto de una fuga y controles mínimos. La clave es que el criterio sea **objetivo** (no "lo que parezca sensible") para que dos personas clasifiquen igual.
2. **Tabla de roles**: `owner` (negocio, rinde cuentas, clasifica y aprueba accesos), `custodian` (TI, implementa cifrado/backups/parches) y `processor` (trata datos por instrucción del controlador). Regla de verificación: el propietario nunca es de TI.
3. **Guía de etiquetado y manejo por nivel**: cómo se marca (encabezado/pie en documentos, metadatos en archivos, banner en sistemas, etiqueta física en soportes) y cómo se maneja en transmisión, almacenamiento, impresión y descarte.
4. **Ciclo de vida** con controles por fase (crear → almacenar → usar → compartir → archivar → destruir).
5. **Regla de agregación**: datos `Interno` que agregados se vuelven `Confidencial`.

**Qué demuestra el criterio de aceptación:** que la política es *autoexplicativa*. Si un revisor externo puede clasificar 5 activos nuevos y decir qué controles aplicarles sin preguntar nada, la política tiene criterios objetivos y una guía de manejo operable, no solo etiquetas bonitas.

### Claves de los ejercicios

1. Para cada tipo de dato: nombra el nivel y **justifica con el daño de la divulgación** (confidencialidad), no con quién lo usa. Ej.: historia clínica → `Restringido` (daño legal/personal alto); folleto de marketing → `Público`.
2. **Propietario** = rol de negocio que decide la clasificación y rinde cuentas (accountable); **custodio** = rol técnico que ejecuta los controles. Ej.: el jefe médico posee las historias clínicas; TI las respalda y cifra.
3. FIPS 199 sobre reservas de hotel: C=Moderado (datos personales de huéspedes), I=Moderado (una reserva alterada daña operación), D=Alto (sistema caído = no hay ventas). Categoría = **máximo (high-water mark) = Alto**.
4. Sección "Manejo" de `Restringido`: transmisión solo cifrada (TLS/GPG), almacenamiento cifrado en reposo con acceso mínimo y registrado, impresión prohibida o con marca de agua y retirada inmediata, descarte por sanitización certificada (enlaza con clase 312).
5. Reclasificación `Confidencial → Público`: cuando desaparece el daño de la divulgación (p. ej. resultados financieros ya anunciados oficialmente). Criterios: hecho público por fuente autorizada, vencimiento del embargo temporal, aprobación del propietario documentada.
6. Matriz nivel × estado: filas = niveles, columnas = reposo/tránsito/uso; cada celda el control exigido (ej.: `Restringido`+tránsito = TLS 1.2+ y mutual auth; `Interno`+reposo = cifrado de disco).

---

## Clase 312 — Retención, destrucción segura de datos y DLP

### Solución del reto verificable

El **Procedimiento de Retención y Destrucción Segura** se arma con cuatro componentes:

1. **Cronograma de retención**: tabla `Tipo de dato · Base legal · Período · Acción al vencer · Responsable`. Incluye retención **mínima** (ley) y **máxima** (privacidad/minimización), y resuelve el conflicto cuando chocan.
2. **Árbol de decisión de sanitización (NIST 800-88)**: entrada = (medio + clasificación + destino del medio) → salida = **Clear** (reutilización interna, impacto bajo), **Purge** (el medio sale del control) o **Destroy** (alto impacto / medio se retira).
3. **Plantilla de certificado de destrucción**: identificador del medio, método, fecha, operador, testigo y firma → evidencia de auditoría.
4. **Tres reglas DLP** (reposo: descubrimiento de PAN sin cifrar; tránsito: bloqueo de correo con >1 tarjeta a dominios externos; uso: bloqueo de copia a USB), cada una con modo de respuesta (auditar/alertar/cifrar/bloquear).

**Qué demuestra el criterio:** dado el lote de 4 medios (HDD interno, SSD donado, cinta, teléfono), un técnico elige el método correcto, lo ejecuta y emite el certificado sin consultar otra fuente → el árbol cubre todos los tipos de medio y la evidencia queda trazada.

### Claves de los ejercicios

1. Cronograma de 8 tipos con base legal: cada fila cita la norma (ej.: historia clínica según ley sanitaria local, datos de tarjeta bajo PCI DSS Req. 3 —no almacenar CVV—, logs de seguridad por política interna).
2. Los 5 escenarios: HDD reutilizado interno → **Clear** (sobrescritura 1 pasada verificada); SSD donado → **Purge** (Secure Erase de firmware o criptoborrado); disco `Restringido` retirado → **Destroy** (trituración); cinta de backup → Purge por desmagnetización (degauss) o Destroy; móvil corporativo → criptoborrado + factory reset.
3. Criptoborrado > sobrescritura en SSD: la **FTL** (capa de traducción flash) y el **over-provisioning** dejan bloques físicos fuera del alcance de la escritura lógica; destruir la clave de cifrado inutiliza *todo* el contenido de golpe.
4. Tres reglas DLP: una por estado, cada una con patrón de detección (ej.: regex de PAN con validación Luhn) y acción proporcional.
5. Retirada de servidor: baja lógica en IAM → respaldo/transferencia de datos necesarios → sanitización según clasificación (Purge/Destroy) → certificado → actualización del inventario de activos.
6. Backup en la nube conserva datos "borrados": falló el **alcance de retención** (no incluyó réplicas/snapshots). Corrección: aplicar la política a copias y nube, y usar criptoborrado de la clave que cubra todas las copias.

---

## Clase 313 — Gestión del ciclo de vida de identidades (IAM empresarial)

### Solución del reto verificable

El **Manual de Gestión del Ciclo de Vida de Identidades** se construye así:

1. **RR. HH. como fuente autoritativa**: toda alta/cambio/baja nace allí y se propaga (idealmente por SCIM).
2. **Tres flujos JML con SLA**: *Joiner* (cuenta + roles por puesto + MFA listo el día 1), *Mover* (retirar roles previos **y** asignar nuevos — "restar antes de sumar"), *Leaver* (deshabilitar —no borrar— el mismo día, revocar sesiones/tokens, transferir propiedad de datos).
3. **Matriz RBAC** `Rol × Permiso` con la marca de acceso **mínimo** por rol.
4. **Reglas de SoD**: pares de permisos incompatibles prohibidos en una misma persona (ej.: "crear proveedor" y "aprobar pago").
5. **Campaña de recertificación** trimestral para accesos privilegiados y a datos `Restringido`, con aprobador (el manager) y revocación por defecto si no responde.

**Qué demuestra el criterio:** ante "enfermera → facturación → renuncia", el manual permite ejecutar Mover (retira permisos de enfermería, asigna facturación) y luego Leaver (deshabilita) indicando qué permisos, cuándo y quién aprueba, sin ambigüedad → prueba que el modelo evita el *privilege creep* y automatiza la baja.

### Claves de los ejercicios

1. Ciclo con disparadores: alta ← contrato firmado; cambio ← orden de traslado de RR. HH.; suspensión ← licencia; baja ← fecha de cese. Cada transición dispara un cambio de acceso.
2. **Autenticación** = probar quién eres (contraseña/MFA); **autorización** = qué puedes hacer una vez autenticado (permisos del rol). Ej.: entras con passkey (autN); solo ves facturación porque tu rol lo permite (autZ).
3. RBAC de 4 roles: agrupar accesos individuales repetidos en roles (ej.: Recepción, Clínico, Facturación, Admin), asignar permisos al rol y personas al rol.
4. SoD en compras: (1) quien crea proveedor ≠ quien lo aprueba; (2) quien emite orden ≠ quien autoriza pago; (3) quien recibe mercancía ≠ quien concilia factura.
5. Leaver de despido inmediato (primeros 15 min): deshabilitar cuenta y forzar cierre de sesión, revocar tokens/MFA, cambiar contraseñas de cuentas compartidas que conociera, bloquear acceso físico (badge), notificar a seguridad.
6. Regla ABAC que RBAC no expresa: "permitir acceso solo si `hora ∈ 08–18` **y** `red = corporativa` **y** `dispositivo = gestionado`" — depende de atributos de contexto, no solo del rol.

---

## Clase 314 — Federación, SSO, SAML y OpenID Connect

### Solución del reto verificable

El **Diseño de Arquitectura de SSO Federado** para NovaSalud contiene:

1. **Mapa de actores**: IdP corporativo + dos confiantes (portal web interno vía **SAML**, app móvil vía **OIDC**).
2. **Flujo SAML SP-initiated** paso a paso: SP redirige con `SAMLRequest` → IdP autentica → devuelve `SAMLResponse` con aserción **firmada** → SP valida firma y crea sesión (se firma la aserción para garantizar integridad y origen).
3. **Flujo OIDC Authorization Code**: authorization request → login → `code` → intercambio en el token endpoint por `id_token` (JWT) + `access_token` → validación del JWT.
4. **Tabla de metadatos/confianza**: EntityID, endpoints ACS/SSO y certificado público de firma; qué ocurre si el certificado caduca (falla la validación → rotar y actualizar metadatos).
5. **Modelo de amenazas** (≥4): robo/replay de aserción (mitiga `NotOnOrAfter`, `nonce`, TLS), XML Signature Wrapping (validación estricta de firma y referencia), IdP comprometido (MFA fuerte + monitorización), phishing del IdP.
6. **Regla de aprovisionamiento JIT**: mapeo de claims → roles RBAC de la clase 313.

**Qué demuestra el criterio:** un arquitecto que lo lea sabe qué sistema autentica, qué token viaja en cada flujo, qué se valida para aceptarlo y cómo se mitiga el robo → el diseño distingue autenticación (OIDC/ID Token) de autorización (OAuth/access token) y no confía un token sin validar.

### Claves de los ejercicios

1. OAuth 2.0 solo no sirve para "login" porque **autoriza el acceso a un recurso, no prueba la identidad del usuario**: el access token dice "este cliente puede llamar a esta API", no "este usuario es X". Para identidad se usa el ID Token de OIDC.
2. Orden SAML SP-initiated: (1) usuario va al SP → (2) SP genera `SAMLRequest` y redirige al IdP → (3) IdP autentica → (4) IdP emite `SAMLResponse` firmada → (5) SP valida firma y establece sesión.
3. Claims del ID Token: `iss` (emisor), `sub` (identificador del usuario), `aud` (cliente destinatario), `exp` (expiración), `iat` (emitido), `nonce` (anti-replay). El RP valida `iss`, `aud`, `exp` y `nonce`.
4. Tabla SAML vs OIDC: XML/firma vs JSON/JWT; POST/redirect vs REST; web empresarial legada vs móvil/SPA/API. Recomendación: portal interno legado → SAML; app móvil → OIDC; API pública → OAuth/OIDC.
5. **XML Signature Wrapping**: el atacante duplica/reubica nodos XML para que el SP valide una firma legítima pero procese una aserción maliciosa. Mitigación: validar que la firma cubra exactamente el elemento procesado (referencia por ID, esquema estricto).
6. Trust 1 IdP + 3 SP: con cada SP se comparte metadatos (EntityID, ACS, certificado) y los **claims mínimos** que ese SP necesita (minimización), no todos los atributos.

---

## Clase 315 — MFA y gestión de accesos privilegiados (PAM)

### Solución del reto verificable

El **Plan de MFA y PAM** para NovaSalud incluye:

1. **Clasificación de factores** por categoría (sabes/tienes/eres) y por **resistencia al phishing** (SMS < TOTP/push < FIDO2/passkey).
2. **Política MFA por riesgo**: apps internas → contraseña + TOTP/push; datos `Restringido` o red no confiable → **FIDO2/passkey**; administradores → **AAL3** (FIDO2 de hardware), con autenticación adaptativa (ubicación imposible, dispositivo nuevo, hora atípica elevan el factor).
3. **Inventario de cuentas privilegiadas** (≥5).
4. **Flujo PAM de checkout**: solicitud → aprobación → bóveda entrega credencial **JIT** por tiempo limitado → sesión **grabada** → contraseña **rotada** al terminar → **zero standing privilege**.
5. **Política break-glass**: cuenta de emergencia sellada, alerta en cada uso, revisión obligatoria posterior.

**Qué demuestra el criterio:** ante "admin necesita acceso urgente a la BD clínica a las 3 a. m.", el plan describe el factor MFA exigido (AAL3), cómo obtiene la credencial (checkout con aprobación on-call), por cuánto tiempo (JIT), qué queda registrado y cuándo se revoca — **sin credenciales privilegiadas permanentes** → prueba que el diseño minimiza la ventana de exposición.

### Claves de los ejercicios

1. Clasificación: contraseña (sabes, phishable), SMS-OTP (tienes, débil: SIM swap), TOTP (tienes, phishable), push (tienes, MFA fatigue), FIDO2/passkey (tienes, resistente al phishing), biometría (eres, resistente pero local).
2. "Contraseña + PIN" no es MFA porque ambos son de la **misma categoría** ("algo que sabes"); MFA exige combinar categorías distintas.
3. WebAuthn impide phishing porque la credencial criptográfica está ligada al **origen (dominio) real**: en un sitio falso la firma no se genera para ese dominio, así que no hay nada reutilizable; el TOTP, en cambio, el usuario lo teclea en la web fraudulenta.
4. Política de 3 niveles: bajo → contraseña + TOTP; medio (datos sensibles) → FIDO2/passkey; alto (admin) → FIDO2 de hardware (AAL3).
5. Flujo checkout: solicitud → aprobación → entrega JIT desde bóveda → grabación de sesión → rotación de la credencial al cierre.
6. Zero standing privilege reduce la superficie porque **no hay privilegio permanente que robar**: si comprometen una cuenta admin, no tiene poder elevado hasta que un flujo aprobado lo concede temporalmente.

---

## Clase 316 — Modelos de seguridad y arquitectura (Bell-LaPadula, Biba, Clark-Wilson)

### Solución del reto verificable

La matriz multinivel (4 niveles × 4 sujetos) que cumple **Bell-LaPadula** se construye con dos matrices:

- **Retículo**: `Público < Interno < Confidencial < Secreto`. Sujetos con *clearance*, objetos con *clasificación*.
- **Matriz de lectura (ss-property, "no read up")**: ✔ solo si `clearance(sujeto) ≥ clasificacion(objeto)`. Un `Confidencial` **no** puede leer un `Secreto`.
- **Matriz de escritura (\*-property, "no write down")**: ✔ solo si `clearance(sujeto) ≤ clasificacion(objeto)`. Un `Secreto` **no** puede escribir en un `Público` (evita fuga hacia abajo).
- **Versión Biba** (integridad): invierte ambas reglas → *no read down* (`i(sujeto) ≤ i(objeto)` para leer) y *no write up* (`i(sujeto) ≥ i(objeto)` para escribir).
- **Regla Clark-Wilson**: un TP `aprobar_pago` ejecutable solo por un rol distinto al que crea la solicitud (separación de deberes), con su IVP que verifica la integridad del CDI.

**Qué demuestra el criterio:** ninguna celda viola su regla; la versión Biba invierte correctamente; se nombra qué propiedad protege cada versión (BLP = confidencialidad, Biba = integridad) → prueba que el alumno no confunde la **dirección** de los modelos (el error clásico del examen).

### Claves de los ejercicios

1. Retículo con TLP: `CLEAR < GREEN < AMBER < RED`; clasifica documentos por daño de divulgación.
2. Sujeto `Confidencial`, objeto `Secreto`: **BLP** permite *escribir* (no write down no lo prohíbe: escribe hacia arriba) pero **no leer** (no read up); **Biba** lo invierte (permite leer hacia arriba está prohibido; permite leer hacia abajo prohibido...) — el punto es que protegen objetivos opuestos.
3. Clark-Wilson en "solicitud → aprobación → pago": la solicitud y el pago son **CDI**, los datos externos sin validar son **UDI**, cada paso es un **TP** certificado, y un **IVP** verifica la consistencia; nadie toca el CDI salvo por un TP.
4. Brewer-Nash es dinámico porque lo permitido **depende del historial de accesos** del sujeto (si accediste al cliente A de un sector, se te bloquea su competidor B); BLP es estático (las etiquetas no cambian por lo ya accedido).
5. Monitor de referencia: **tamperproof** (fallo: un driver que modifica el kernel), **non-bypassable/siempre invocado** (fallo: una ruta de acceso que lo salta), **verificable/pequeño** (fallo: TCB inflada imposible de auditar).
6. Reducir la TCB mejora la verificabilidad: un **microkernel** deja fuera de la frontera de confianza drivers y servicios, así hay menos código que auditar y menos superficie; un kernel monolítico mete todo dentro y es inverificable.

---

## Clase 317 — Seguridad física y ambiental

### Solución del reto verificable

El **informe de evaluación física** de la sala de servidores se construye con:

1. **Mapa de capas** (defensa en profundidad, ≥4): perímetro exterior → control de acceso al edificio → pasillo → puerta de sala → gabinete/rack, marcando dónde hay control y dónde no.
2. **Tabla de hallazgos** con: control evaluado, estado, riesgo (probabilidad × impacto: Alto/Medio/Bajo), recomendación accionable y referencia a un control **NIST 800-53 familia PE**.
3. **Tres dimensiones ambientales**: acceso (badge+PIN, esclusa, tailgating), clima (temperatura/humedad vs ASHRAE 18–27 °C / 40–60 %) y energía (UPS, generador probado, PDUs A/B redundantes).

**Qué demuestra el criterio:** el mapa muestra ≥4 capas, cada hallazgo tiene P×I y recomendación, se evalúan las tres dimensiones y cada recomendación cita un control PE-x → prueba una evaluación sistemática, no una lista de impresiones sueltas.

### Claves de los ejercicios

1. CPTED en estacionamiento: vigilancia natural (iluminación, líneas de visión), control natural de accesos (una entrada canalizada), refuerzo territorial (señalización, jardinería que delimita) y mantenimiento (sin zonas descuidadas que inviten al delito).
2. Capas de un Tier III: cerca perimetral + CCTV → recepción/torniquete → pasillo controlado → puerta de sala con esclusa → rack cerrado; redundancia N+1 concurrentemente mantenible.
3. Tres controles anti-tailgating: esclusa/mantrap (alto costo/fricción), torniquete de altura completa (medio), concienciación + política de "no dejar pasar" (bajo costo, menor fiabilidad).
4. Autonomía UPS: `minutos ≈ (capacidad batería Wh × eficiencia) / carga W × 60`. Con carga 6 kW, un banco que entregue 3 kWh útiles → ~30 min. (Calcula con los datos dados del banco.)
5. Supresión: agua (barata, **destruye electrónica**, riesgo a personas nulo por electrocución si se corta energía); gas inerte (desplaza O₂, riesgo a personas presentes); clean agent FM-200/Novec (no daña equipos, seguro para personal a concentración de diseño). Para sala con personal: clean agent o pre-action.
6. Tier IV usa **2N+1** para tolerar el fallo único de cualquier componente sin caída (redundancia activa duplicada + reserva); tolera perder una ruta/UPS/generador completo manteniendo servicio.

---

## Clase 318 — Gestión del programa de vulnerabilidades

### Solución del reto verificable

El **pipeline de priorización de VM** se construye cruzando tres señales:

1. **Inventario y descubrimiento**: escaneo autenticado (más preciso, menos falsos positivos) sobre activos propios.
2. **Enriquecimiento**: para cada CVE se añade `CVSS_base` (severidad), `EPSS` (probabilidad de explotación a 30 días, vía API de FIRST) y `en_kev` (explotación activa confirmada, JSON de CISA).
3. **Fórmula de priorización**: `P1` si `en_kev = sí` (máxima urgencia **sin importar el CVSS**); `P2` si `CVSS ≥ 7 y EPSS ≥ 0.1`; `P3` si `CVSS ≥ 7`; `P4` el resto.
4. **SLAs**: P1 → 48 h, P2 → 15 días, P3 → 30 días, P4 → 90 días, con fecha límite calculada desde la detección.
5. **Métricas**: MTTR, % remediado dentro de SLA, densidad de vulnerabilidades.

**Qué demuestra el criterio:** toda CVE en KEV queda como máxima prioridad independientemente del CVSS, se usan las tres señales (no solo CVSS), cada prioridad tiene SLA numérico con fecha, y se reportan MTTR y % en SLA → prueba priorización **basada en riesgo real**, no en el número más alto.

### Claves de los ejercicios

1. Ordenar 5 CVEs: EPSS puede **subir** una CVSS media con explotación probable por encima de una CVSS alta improbable, y **bajar** una CVSS 9.8 teórica sin exploit observado.
2. Una CVSS 6.5 en KEV > una CVSS 9.8 fuera de KEV porque la primera **se está explotando activamente ahora**; el riesgo real integra probabilidad de explotación, no solo severidad técnica.
3. Tabla de SLAs criticidad × prioridad: activo crítico acorta plazos (P1 24 h) vs estándar (P1 72 h); cada celda un número.
4. Plantilla de excepción: dueño, justificación, controles compensatorios, fecha de revisión/caducidad, riesgo residual aceptado y aprobador. **Nunca "para siempre".**
5. MTTR = promedio de (fecha de cierre − fecha de detección) de los tickets cerrados.
6. Tres métricas para el comité: exposición a KEV (habilita decisión de urgencia), MTTR por criticidad (mide eficiencia), % dentro de SLA (mide cumplimiento del compromiso).

---

## Clase 319 — Análisis avanzado de phishing y correo malicioso

### Solución del reto verificable

El **informe de análisis** de un correo de phishing de muestra se construye:

1. **Cabeceras**: reconstruir los saltos `Received` (de abajo hacia arriba → el inferior es el origen), identificar la IP real y contrastar `From:` visible vs `Return-Path`.
2. **Autenticación**: interpretar `Authentication-Results` — SPF (valida IP frente al `Return-Path`), DKIM (firma criptográfica), DMARC (**alineación** del `From:` visible con SPF/DKIM). Explicar el caso "SPF pass pero DMARC fail" (el atacante controla un dominio con SPF válido pero falsifica el `From:` visible).
3. **URLs y adjuntos** analizados en entorno aislado, con IOCs **defanged** (`hxxp://…[.]…`); compartir hash, no el archivo.
4. **Plan de respuesta**: contención (purga multi-buzón por Message-ID/asunto), bloqueo de IOCs en gateway/proxy/EDR, reseteo de credenciales si hubo clic, aviso a usuarios.

**Qué demuestra el criterio:** determina la IP/origen real, interpreta SPF/DKIM/DMARC (incluido "SPF pass, DMARC fail"), presenta todos los IOCs defanged, incluye contención + bloqueo + acción sobre usuarios, y documenta que el análisis fue aislado → prueba un triaje SOC completo y seguro.

### Claves de los ejercicios

1. IP de origen real = la del salto `Received` **inferior** (el primer MTA que recibió); si `From:` no coincide con el dominio autenticado, hubo suplantación.
2. SPF pasa pero DMARC falla: SPF valida el `Return-Path` (dominio del atacante, con SPF válido) pero DMARC exige que ese dominio **se alinee con el `From:` visible**; si el `From:` visible es otro, DMARC falla.
3. Defang: `hxxp://malo[.]com`, `1.2.3[.]4`; decodificar Base64 en la URL con CyberChef ("From Base64").
4. `microsoft.com` vs lookalikes: `rnicrosoft.com` (rn≈m), `micros0ft.com` (0 por o), IDN cirílico → convertir a **punycode** (`xn--`) y comparar carácter por carácter.
5. Playbook BEC de cambio de datos bancarios: **no** actuar por correo; verificar por canal fuera de banda (teléfono conocido del proveedor), congelar el cambio, escalar a finanzas/seguridad, revisar reglas de reenvío del buzón por compromiso.
6. Tabla de IOCs lista para bloqueo: remitente, IP, dominios, URLs, hashes — en formato defanged, con columna de tipo y acción.

---

## Clase 320 — Gobierno, aspectos legales/regulatorios y gestión del programa

### Solución del reto verificable

El **paquete de gobierno** de la organización ficticia contiene:

1. **Política madre** de Seguridad de la Información: propósito, alcance, roles, principios CIA, cumplimiento y sanciones, aprobador y **cadencia de revisión anual**.
2. **Jerarquía documental** de un dominio (ej. control de acceso): **política** (declaración de alto nivel) → **estándar** (MFA obligatorio para privilegiados) → **procedimiento** (pasos de alta/baja) → **guía** (recomendaciones de contraseñas).
3. **Matriz de mapeo** que conecta cada requisito con un control de marco (ej. NIST CSF `PR.AA`) **y** un requisito regulatorio (PCI DSS 8.x, HIPAA §164.312), señalando huecos.
4. **Registro de riesgos**: probabilidad × impacto, dueño y tratamiento (mitigar/transferir/aceptar/evitar) coherente con el apetito de riesgo.
5. **Cuadro de métricas**: ≥3 KPIs y ≥2 KRIs con umbral y frecuencia, más evaluación de madurez (CMMI) con acción de mejora.

**Qué demuestra el criterio:** la política tiene aprobador y cadencia, se distinguen los cuatro niveles documentales, el mapeo liga cada obligación legal a un control **y** una regulación (marco ≠ ley), y hay KPIs+KRIs → prueba un programa gobernable y auditable, no controles sueltos.

### Claves de los ejercicios

1. Clasificar enunciados: "usar AES-256" = estándar; "proteger la información" = política; "pasos para crear una cuenta" = procedimiento; "se recomienda frases largas" = guía. Corrige los mal ubicados por nivel de generalidad.
2. Mapear 3 controles a NIST CSF 2.0 y a la regulación (ej.: cifrado → `PR.DS` → PCI DSS 3 / HIPAA §164.312(a)(2)(iv)).
3. **Due care** = implementar controles razonables (actuar como persona prudente); **due diligence** = investigar y verificar continuamente que funcionan. Ambas reducen la responsabilidad por negligencia.
4. RACI de gestión de cambios: R (analista), A (dueño del cambio/CAB), C (seguridad, operaciones), I (usuarios afectados).
5. Dos KRIs con umbral: "nº de cuentas privilegiadas sin MFA > 0" y "nº de sistemas críticos sin parchear por encima del SLA > 5" — anticipan un incidente de accesos.
6. Situar en CMMI: si los procesos son ad hoc → nivel 1 (Inicial); documentados y repetibles → 3 (Definido); medidos con métricas → 4 (Cuantitativo). Justificar con evidencia de repetibilidad/medición.

---

## Clase 321 — Comunicación y reporte para analistas de seguridad

### Solución del reto verificable

El **paquete de comunicación** del incidente de ransomware contenido se arma con:

1. **Línea de tiempo** (columna vertebral): hora, evento, actor, evidencia verificable (ID de alerta EDR, hash, host).
2. **Informe técnico**: IOCs, hosts, técnica MITRE ATT&CK (ej. `T1486` cifrado de datos), contención/erradicación y recomendaciones con dueño.
3. **Resumen ejecutivo (BLUF)**: ≤1 página, sin jerga ni CVE crudos, con qué pasó, impacto en negocio y **decisiones requeridas** al inicio.
4. **Matriz de escalado**: quién se entera y cuándo, canal primario y **canal fuera de banda** (por si el atacante controla el correo).
5. **Decisión de notificación** documentada con base legal y marca temporal (el reloj de las 72 h de GDPR corre desde que se *conoce* la brecha).
6. **MTTD/MTTR** vs objetivo y ≥3 lecciones aprendidas con dueño y fecha.

**Qué demuestra el criterio:** el resumen ejecutivo cabe en 1 página sin jerga y termina en decisiones; el informe técnico tiene timeline + ATT&CK + recomendaciones; hay matriz de escalado con canal fuera de banda; la decisión de notificación está fechada con su base legal → prueba que el analista traduce el mismo hecho a **tres audiencias** distintas.

### Claves de los ejercicios

1. "SMBv1 en 40 hosts (CVE-2017-0144)" para dirección: "40 equipos usan un protocolo obsoleto explotado por WannaCry; los actualizamos esta semana para evitar propagación de ransomware."
2. Resumen ejecutivo ≤150 palabras: qué pasó, impacto (3 equipos parados 4 h, sin fuga confirmada), estado actual, qué se pide decidir.
3. Matriz de escalado con **roles, no nombres**, canal primario + fuera de banda y umbral de tiempo por rol.
4. Cinco KPIs de SOC con umbral: MTTD, MTTR, cobertura de detección, backlog de alertas, tasa de falsos positivos — cada uno con objetivo y por qué le importa a dirección.
5. Árbol de notificación: interna (siempre) → clientes (si hay riesgo a sus datos) → reguladores (si la ley lo exige, GDPR 72 h) → fuerzas del orden (si hay delito/extorsión). Disparador por rama.
6. Top-5 desde 20 hallazgos: criterio explícito CVSS + explotabilidad (EPSS/KEV) + exposición.

---

## Clase 322 — Threat intelligence operacional avanzada

### Solución del reto verificable

El **playbook de threat intelligence** convierte un informe en detecciones y productos:

1. **Dirección**: un requisito de inteligencia explícito ("¿estamos expuestos a las técnicas del grupo APT-X?").
2. **IOCs vs IOAs** separados y clasificados en la **Pyramid of Pain** (hash < IP < dominio < artefactos < herramientas < **TTPs**); se prioriza detectar comportamiento (arriba) porque cuesta más al adversario.
3. **Evento MISP** con atributos, taxonomías (`tlp:amber`) y galaxia de ATT&CK.
4. **Capa de ATT&CK** (≥6 técnicas, ej. `T1566`, `T1059.001`, `T1486`) cruzada con la **fuente de log** que la detectaría, señalando huecos de cobertura.
5. **Diamond Model** (adversario, capacidad, infraestructura, víctima) con un pivote propuesto.
6. **Tres productos** por nivel: táctico (IOCs para el SOC), operacional (TTPs para IR), estratégico (riesgo del sector para dirección).

**Qué demuestra el criterio:** parte de un requisito, separa IOC/IOA con prioridad justificada, tiene evento MISP etiquetado, capa ATT&CK con fuentes de detección y huecos, Diamond con pivote y tres productos → prueba que se produce **inteligencia accionable**, no una lista de indicadores.

### Claves de los ejercicios

1. Diez indicadores IOC/IOA: hash/IP/dominio/mutex = **IOC**; "Word lanza PowerShell codificado", "creación de tarea programada por proceso raro" = **IOA**.
2. Pyramid of Pain: bloquear hashes es barato de evadir; detectar TTPs obliga al adversario a rediseñar su operación → invertir arriba.
3. Evento MISP: ≥5 atributos (dominios, hashes, IPs), ≥2 taxonomías (TLP, kill-chain) y una galaxia ATT&CK.
4. Mapear informe a 6 técnicas ATT&CK y construir la capa en Navigator con colores por confianza.
5. Diamond Model: rellenar los 4 vértices; pivote por infraestructura = buscar otros eventos que usen el mismo C2/dominio → descubre campaña.
6. Producto estratégico (½ página): riesgo del sector y tendencia, **sin hashes crudos** (audiencia directiva).

---

## Clase 323 — Pruebas de seguridad del software y evaluación

### Solución del reto verificable

El **informe de evaluación** de la app de práctica se construye combinando técnicas y gestionando hallazgos:

1. **≥3 técnicas** sobre software propio/autorizado en entorno aislado: **SCA** (dependencias con CVE), **SAST** (código sin ejecutar, con triaje de falsos positivos), **DAST** (app en ejecución) y **revisión manual** (lógica de negocio que ninguna herramienta ve).
2. **Registro de hallazgos** consolidado y **deduplicado**, cada uno con severidad, CWE, dueño y SLA.
3. **Triaje documentado** de falsos positivos con su criterio.
4. **Verificación ASVS** de un conjunto de requisitos L1/L2 (V2 autenticación, V5 validación, V6 criptografía) con evidencia cumple/no cumple.
5. **Informe** con resumen ejecutivo sin jerga y tabla priorizada.

**Qué demuestra el criterio:** se combinaron ≥3 técnicas, el registro está deduplicado con severidad/CWE/dueño/SLA, hay triaje de FP y verificación ASVS con evidencia → prueba una evaluación de **aseguramiento** (encontrar y gestionar defectos), no una corrida de herramienta sin criterio.

### Claves de los ejercicios

1. En el SDLC: **SAST** (código, temprano, en cada commit), **SCA** (dependencias, continuo), **IAST** (durante pruebas funcionales), **DAST** (app corriendo, en QA/preprod).
2. Dos fallos de validación con CWE: entrada sin sanitizar en query → **CWE-89** (SQLi); reflejo de input en HTML → **CWE-79** (XSS).
3. Triaje de 10 hallazgos SAST: marcar FP con justificación (ej.: "el `eval` está sobre constante interna, no sobre input").
4. Mapear 5 hallazgos a ASVS: SQLi → V5; contraseñas sin hash → V2; TLS débil → V9/V6; según nivel L1/L2/L3 que incumplan.
5. Política de SLA por severidad: crítico 7 días, alto 30, medio 90, bajo backlog — justificada por riesgo/explotabilidad.
6. Correlacionar SAST+DAST: SAST marca la ruta de código vulnerable; DAST confirma que se explota desde fuera → demuestra explotabilidad real (reduce falso positivo).

---

## Clase 324 — Operaciones de seguridad: hardening y gestión de configuración

### Solución del reto verificable

El **paquete de hardening** controlado por gestión del cambio contiene:

1. **Medición inicial y final** contra un **CIS Benchmark** (con CIS-CAT/OpenSCAP/Lynis), con mejora demostrada del % de cumplimiento.
2. **Hardening repetible** (Ansible/GPO/DSC/IaC, **no manual**) y baseline **versionada** en el repositorio de configuración.
3. **RFC** con riesgo, ventana, pruebas y **plan de rollback** (restaurar snapshot), más lista de **excepciones justificadas** con control compensatorio.
4. **Detección y corrección de drift**: cambiar un ajuste a mano, detectarlo con el escáner y reaplicar la configuración canónica.
5. **Gestión de parches** (NIST 800-40) con priorización por riesgo y ventana documentada.

**Qué demuestra el criterio:** hay cumplimiento inicial vs final con mejora, hardening repetible y versionado, RFC con rollback y excepciones, drift detectado/corregido y ciclo de parches priorizado → prueba que el estado seguro se **sostiene en el tiempo** y se cambia sin romper el negocio.

### Claves de los ejercicios

1. L1 (servidor de propósito general: controles prudentes que no rompen), L2 (servidor sensible/expuesto: defensa en profundidad aunque impacte compatibilidad).
2. RFC para desactivar SMBv1 en la flota: cambio, riesgo (apps legadas), ventana de mantenimiento, plan de pruebas (verificar compartidos), rollback (reactivar por GPO), aprobación CAB.
3. Tarea Ansible idempotente: usar módulos declarativos (`ansible.windows.win_feature`, `lineinfile`/`win_security_policy`) que solo cambian si el estado difiere.
4. Flujo de drift: escanear la baseline con OpenSCAP/Lynis a diario, comparar contra la fuente de verdad, reaplicar IaC al detectar divergencia.
5. Priorizar 5 parches: KEV/explotación activa → vía rápida; luego CVSS × exposición; ventana según criticidad.
6. Excepción justificada: recomendación que rompe app crítica → documentar riesgo aceptado + control compensatorio (segmentación, monitoreo) + aprobador + caducidad.

---

## Clase 325 — Forense de memoria avanzado

### Solución del reto verificable

Sobre `incidente.raw` (host con malware *fileless*), el informe reproducible se construye con Volatility 3:

1. **Preservar evidencia**: `sha256sum incidente.raw` antes de tocar nada (cadena de custodia).
2. **Contexto**: `windows.info` para versión de kernel, arquitectura y hora del sistema.
3. **Proceso inyectado (a)**: `windows.malfind` localiza regiones privadas `PAGE_EXECUTE_READWRITE` con cabecera `MZ`/shellcode → identifica **PID y nombre** del proceso inyectado. Corroborar con `pstree` (padre anómalo tipo `winword.exe → powershell.exe`).
4. **Prueba (b)**: la salida de `malfind` con los bytes ejecutables en RWX privada.
5. **C2 (c)**: `windows.netscan` correlacionando la IP/puerto remoto con el PID sospechoso.
6. **Artefacto (d)**: `windows.dumpfiles --pid <PID>` y `sha256sum` del binario extraído.

**Qué demuestra el criterio:** otro analista, con los mismos comandos sobre el mismo volcado, reproduce el PID inyectado, la salida de malfind, la IP de C2 y el SHA-256 → prueba hallazgos **reproducibles y trazables**, base de la admisibilidad forense.

### Claves de los ejercicios

1. Adquirir con WinPmem y verificar hash antes y después de copiar (mismo SHA-256 = copia íntegra). Si difieren, la transferencia corrompió el volcado.
2. Tres padres sospechosos con `pstree`: relaciones padre-hijo imposibles (Office/navegador lanzando intérpretes, `services.exe` con hijos raros).
3. `malfind`: clasificar cada hit — probable inyección (RWX privada + `MZ`/shellcode en proceso que no debería) vs falso positivo (JIT de navegadores/.NET).
4. Proceso oculto: `psscan` (barre el pool) muestra un PID ausente de `pslist` (lista enlazada) → candidato a **DKOM**; documentar el PID.
5. `dumpfiles --pid` extrae el binario; `sha256sum` para buscar en VirusTotal **por hash** (sin subir la muestra si es confidencial).
6. `timeliner.Timeliner` genera marcas; correlacionar una conexión de `netscan` con su PID y hora de creación del proceso ubica el momento de la inyección.

---

## Clase 326 — Análisis de malware para respuesta a incidentes

### Solución del reto verificable

Sobre `dropper.exe`, el **mini-informe DFIR** de una página se construye en tres fases:

1. **Triaje estático (a)**: `file`, `sha256sum`, y detección de empaquetado (entropía > 7.0 + imports casi vacíos con DIE/pefile) → hash SHA-256 + veredicto de packer.
2. **IOCs (b)**: análisis dinámico en VM aislada con snapshot y red simulada (INetSim/FakeNet-NG): Regshot antes/después para persistencia (`Run`, servicios, tareas), Procmon para archivos/mutex, Wireshark para dominio/IP de C2 → ≥4 IOCs accionables.
3. **TTPs (c)**: `capa` infiere capacidades y las mapea a ATT&CK; traducir a ≥3 técnicas con ID (ej.: persistencia `T1547`, C2 `T1071`) justificadas por el comportamiento observado.
4. **Contención (d)**: recomendación concreta (bloquear el dominio/IP de C2 en proxy/EDR, aislar hosts con el mutex/clave de persistencia).

**Qué demuestra el criterio:** un analista de contención puede actuar directamente con los IOCs sin volver a analizar → prueba un **triaje rápido orientado a la acción** (IOCs + persistencia + TTPs), no ingeniería inversa completa.

### Claves de los ejercicios

1. Empaquetada vs no: entropía alta (>7) por sección + pocos imports = empaquetada; imports ricos y strings legibles = no empaquetada.
2. Cinco IOCs (2 red: dominio C2, IP; 3 host: mutex, clave `Run`, ruta de archivo soltado) en tabla.
3. Regla YARA simple: `strings: $a = "cadena_única" condition: $a` y validar contra la muestra.
4. Persistencia con evidencia de Regshot: diff muestra la clave `HKCU\...\Run` o el servicio creado.
5. `capa` → 3 capacidades → ATT&CK: "persist via registry run key" → `T1547.001`; "create service" → `T1543.003`; "HTTP C2" → `T1071.001`.
6. Correlacionar la hora del archivo soltado con un evento **Sysmon ID 11** (creación de archivo) / **ID 1** (proceso) para situarlo en la timeline.

---

## Clase 327 — Ingeniería de detección avanzada y validación

### Solución del reto verificable

La detección de **T1547.001 (persistencia por clave Run)** lista para producción se entrega:

1. **Regla Sigma versionada en Git** que pasa `sigma check` — logsource `registry_set` o `process_creation`, selección de escritura en `...\CurrentVersion\Run`, con `tags: attack.persistence, attack.t1547.001`.
2. **Evidencia de disparo (b)**: ejecutar `Invoke-AtomicTest T1547.001` en la VM aislada y capturar la alerta en el SIEM con su timestamp; si no dispara, revisar que la telemetría (Sysmon ID 13 / EDR) capture el campo usado.
3. **Exclusión de FP (c)** justificada con datos (ej.: `not filter` para el instalador legítimo que escribe esa clave), midiendo la tasa de FP antes/después.
4. **Cobertura validada (d)**: marcar la técnica como validada en ATT&CK Navigator **solo tras** la prueba atómica.

**Qué demuestra el criterio:** otro ingeniero clona el repo, despliega la regla y reproduce la validación → prueba **detection-as-code**: reglas versionadas, validadas con emulación real y afinadas con datos, no "tener reglas" sin comprobar que disparan.

### Claves de los ejercicios

1. Regla Sigma para `T1059.001` (PowerShell `-enc`): selección `Image endswith \powershell.exe` + `CommandLine contains '-enc'`; traducir con `sigma convert -t esql` y `-t splunk`.
2. CI: workflow que corre `sigma check` sobre `detections/` en cada commit y falla si hay sintaxis inválida.
3. Tres pruebas Atomic Red Team: anotar cuáles disparan (telemetría presente) y cuáles no (hueco de cobertura o campo no capturado).
4. Reducir FP: añadir contexto (proceso padre, usuario, ruta) — **no** bajar la severidad — y medir el antes/después.
5. Capa en ATT&CK Navigator con las técnicas validadas coloreadas.
6. Tres métricas: cobertura ATT&CK validada, tasa de FP y MTTD — juntas dan la imagen equilibrada.

---

## Clase 328 — Gestión de riesgos cuantitativa y continuidad avanzada

### Solución del reto verificable

El **análisis de riesgo cuantitativo** que termina en continuidad se construye:

1. **ALE clásico**: `SLE = AV × EF`, `ALE = SLE × ARO`, con supuestos documentados.
2. **Modelo FAIR** de los mismos factores: `Riesgo = LEF (frecuencia de eventos de pérdida) × LM (magnitud)`, separando **pérdida primaria** (respuesta, restauración) de **secundaria** (multas, reputación).
3. **Incertidumbre**: distribuciones calibradas (triangular/PERT) y **Monte Carlo** (10.000 iteraciones), reportando al menos el **percentil 90** de pérdida anual (no un número único).
4. **ROSI**: `(ALE_antes − ALE_después − coste_control) / coste_control` para decidir el control.
5. **BIA** que deriva **RTO, RPO y MTD**, verificando **RTO ≤ MTD**.
6. **Estrategia continuidad/DR** (tipo de sitio frío/tibio/caliente, backup 3-2-1 inmutable, orden de recuperación) coherente con los RTO/RPO.

**Qué demuestra el criterio:** hay ALE clásico **y** FAIR de los mismos factores, la incertidumbre se modela con Monte Carlo (percentil 90), hay ROSI con recomendación, el BIA cumple RTO ≤ MTD y la DR es coherente con RTO/RPO → prueba que el riesgo se mide en **dinero y rangos**, no en colores.

### Claves de los ejercicios

1. ALE = SLE × ARO; si el **ARO se duplica**, el ALE se duplica (el SLE no cambia).
2. Fuga de datos en FAIR: primaria (investigación, notificación, contención); secundaria (multas regulatorias, pérdida de clientes, daño reputacional).
3. Un número único es engañoso porque ignora las **colas**; el percentil 90 muestra el escenario adverso que preocupa al comité.
4. Mini Monte Carlo: muestrear una triangular (mín, moda, máx) N veces y promediar / extraer percentiles (`numpy.random.triangular`).
5. Proceso con MTD 24 h: RTO < 24 h (ej. 8 h), RPO según tolerancia de datos (ej. 1 h → replicación frecuente); sitio tibio si el RTO lo permite, caliente si es más ajustado.
6. Comparar tres controles por ROSI y financiar primero el de mayor retorno (mayor reducción de ALE por unidad de coste).

---

## Clase 329 — Arquitectura de seguridad empresarial y Zero Trust

### Solución del reto verificable

El **rediseño Zero Trust** trazable al negocio se construye:

1. **Antes/después**: del modelo "castillo y foso" (VPN → red plana → app, con **confianza implícita**) a acceso por recurso y sesión.
2. **Defensa en profundidad**: capas de identidad, dispositivo, red, aplicación y datos; **segmentación** macro (aislar la app de la red general) y micro (aislar la carga de trabajo de su BD).
3. **Flujo Zero Trust (SP 800-207)**: sujeto+dispositivo → **PEP** → consulta al **PE** (decide) / **PA** (establece/termina sesión) evaluando identidad + MFA + postura del dispositivo + contexto → concede sesión **por recurso** y cifrada. PE/PA/PEP marcados explícitamente.
4. **Políticas basadas en atributos** (no por IP): "grupo Finanzas + dispositivo gestionado + MFA reciente → app de facturación por 8 h".
5. **VPN → ZTNA** (acceso al recurso, no a la red) situado en un modelo **SASE** (SWG, CASB, ZTNA, FWaaS), con una **fila SABSA** que traza el requisito de negocio hasta el control.

**Qué demuestra el criterio:** el antes/después elimina la confianza implícita, aplica defensa en profundidad + segmentación, identifica PE/PA/PEP, usa políticas por atributos y justifica ZTNA/SASE con trazabilidad SABSA → prueba que Zero Trust es una **arquitectura**, no un producto.

### Claves de los ejercicios

1. Fila SABSA para "proteger datos de clientes en la app web": contextual (requisito de negocio/regulatorio) → conceptual (confidencialidad) → lógica (control de acceso + cifrado) → física (TLS, cifrado en reposo) → componentes (WAF, IdP, KMS) → operacional (monitoreo).
2. Macrosegmentación = zonas/VLAN (separa la DMZ de la interna); microsegmentación = política por carga de trabajo (el servidor web solo habla con su BD en el puerto exacto).
3. Siete principios de SP 800-207: (1) recursos definidos, (2) toda comunicación asegurada sin importar la red, (3) acceso por sesión, (4) política dinámica por identidad/dispositivo/contexto, (5) monitoreo de integridad de activos, (6) autenticación/autorización dinámica antes de cada acceso, (7) recolección de telemetría para mejorar la política. Cada uno con un control (MFA, EDR de postura, PEP, etc.).
4. Flujo PE/PA/PEP para una API: el **PEP** intercepta la llamada, consulta al **PE** (decide según política), el **PA** emite/termina la sesión; se **decide** en PE, se **aplica** en PEP.
5. VPN vs ZTNA: VPN expone la red entera (todo o nada), ZTNA da acceso granular al recurso con política por sesión y mejor experiencia (sin túnel completo).
6. Componentes SASE: SWG (tráfico web saliente), CASB (control de SaaS), ZTNA (acceso a apps privadas), FWaaS (firewall en la nube), SD-WAN (transporte optimizado).

---

## Clase 330 — Análisis de código y automatización de seguridad

### Solución del reto verificable

El **pipeline de análisis de código** que detecta, tría y verifica se construye:

1. **Revisión manual** documentada (antes/después) guiada por OWASP Code Review/ASVS, con al menos un fallo de lógica corregido (ej.: SQLi por concatenación → consulta parametrizada, ASVS V5).
2. **CI con SAST + SCA** en cada PR (Semgrep con salida **SARIF** subida a Code Scanning, Trivy/Dependency-Check), que **falla el build** por encima de un umbral de severidad justificado (quality gate).
3. **Triaje** por hallazgo: corregir (verdadero positivo) / suprimir de forma trazable (`nosemgrep`/baseline con comentario, solo falsos positivos) / riesgo aceptado con caducidad y responsable.
4. **Corrección verificada**: al menos una **inyección** y una **dependencia vulnerable** desaparecen **por arreglo, no por supresión** (reejecutar el pipeline y confirmar).
5. **Script de automatización** que lee JSON/SARIF, deduplica, cuenta por severidad y emite un informe accionable.

**Qué demuestra el criterio:** hay revisión manual con fallo de lógica corregido, CI que emite SARIF y rompe por umbral, triaje con decisión explícita, inyección + dependencia corregidas y verificadas, y script de normalización → prueba un enfoque **defensivo, shift-left y automatizado**, donde suprimir ≠ corregir.

### Claves de los ejercicios

1. Concatenación SQL → consulta parametrizada (prepared statement / binding); regla ASVS **V5.3** (Output Encoding / Injection Prevention).
2. Tabla SAST/DAST/IAST/SCA: qué ven (código / app corriendo / app instrumentada / dependencias), cuándo (commit / QA / pruebas funcionales / continuo), FP típicos (SAST alto, DAST bajo) y FN típicos (SAST no ve config runtime, DAST no ve rutas no ejercitadas).
3. Workflow GitHub Actions: paso que corre `semgrep --config p/owasp-top-ten --error` y falla si hay hallazgos `ERROR`.
4. Triaje de 5 hallazgos: marcar verdadero/falso positivo, severidad y acción con justificación (explotabilidad, alcance real).
5. Suprimir un FP de forma trazable (`# nosemgrep: regla` con comentario del porqué, o baseline) **no es "ignorar"** porque queda documentado, revisable y limitado a esa línea/regla.
6. Script que parsea SARIF (`results[].level` / `ruleId`) y cuenta hallazgos por severidad y por regla.

---

> Fin de las soluciones de la Parte 17. Recuerda: en gobierno y arquitectura no hay un único "resultado correcto" sino un diseño **defendible y trazable**; el criterio de aceptación siempre mide si otra persona puede *usar* tu entregable sin preguntarte nada.
