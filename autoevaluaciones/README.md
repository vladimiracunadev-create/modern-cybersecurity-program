# 📝 Autoevaluaciones

Batería de preguntas por parte para comprobar lo aprendido. Esta es la versión de lectura (con respuestas plegadas). Para la versión **interactiva** con puntuación, abre [`quiz.html`](quiz.html) desde el [sitio del curso](https://vladimiracunadev-create.github.io/modern-cybersecurity-program/autoevaluaciones/quiz.html).

> 🧭 ¿No sabes por dónde empezar? Mira las [rutas por rol](../rutas/README.md).

<a id="progreso"></a>

## Seguimiento de progreso

Lleva la cuenta de todas las clases del programa en [`progreso.html`](progreso.html) (se guarda en tu navegador).

---

## Parte 0 — Fundamentos y prerrequisitos

**1. ¿Qué representa la 'I' de la tríada CIA?**

- a) Identidad
- b) Integridad
- c) Interoperabilidad
- d) Infraestructura

<details><summary>Ver respuesta</summary>

**Correcta: b) Integridad.** CIA = Confidencialidad, Integridad, Disponibilidad (Availability).

</details>

**2. ¿En qué capa del modelo OSI opera TCP?**

- a) Enlace de datos
- b) Red
- c) Transporte
- d) Aplicación

<details><summary>Ver respuesta</summary>

**Correcta: c) Transporte.** TCP y UDP son protocolos de la capa 4 (Transporte).

</details>

**3. ¿Cuál es la principal diferencia entre codificar (Base64) y cifrar?**

- a) Ninguna, son sinónimos
- b) Codificar requiere clave; cifrar no
- c) Cifrar aporta confidencialidad con una clave; codificar es reversible sin clave
- d) Base64 es más seguro que AES

<details><summary>Ver respuesta</summary>

**Correcta: c) Cifrar aporta confidencialidad con una clave; codificar es reversible sin clave.** Base64/hex/ROT no protegen: se revierten sin clave. Cifrar exige una clave secreta.

</details>

**4. El principio de 'mínimo privilegio' consiste en…**

- a) Dar a cada entidad solo los permisos que necesita
- b) Usar contraseñas cortas
- c) Deshabilitar todos los logs
- d) Compartir credenciales de admin

<details><summary>Ver respuesta</summary>

**Correcta: a) Dar a cada entidad solo los permisos que necesita.** Menos privilegios = menor superficie de ataque e impacto ante un compromiso.

</details>

**5. ¿Qué comando/entorno es el adecuado para practicar técnicas ofensivas?**

- a) La red corporativa de producción
- b) Un laboratorio aislado y propio (VMs/red aislada)
- c) Cualquier servidor de Internet
- d) El wifi del vecino

<details><summary>Ver respuesta</summary>

**Correcta: b) Un laboratorio aislado y propio (VMs/red aislada).** Solo en entornos propios o con autorización explícita: lo contrario es delito.

</details>

## Parte 1 — Redes y seguridad de redes

**1. ¿Qué hace `nmap -sS`?**

- a) Escaneo UDP
- b) Escaneo SYN (half-open)
- c) Detección de versión
- d) Escaneo de vulnerabilidades

<details><summary>Ver respuesta</summary>

**Correcta: b) Escaneo SYN (half-open).** -sS es el SYN scan: envía SYN y no completa el handshake.

</details>

**2. El ARP spoofing permite principalmente…**

- a) Cifrar el tráfico
- b) Interceptar tráfico de la LAN (MitM)
- c) Acelerar la red
- d) Bloquear DNS

<details><summary>Ver respuesta</summary>

**Correcta: b) Interceptar tráfico de la LAN (MitM).** Envenena la caché ARP para situarse en medio del tráfico de capa 2.

</details>

**3. Diferencia entre IDS e IPS:**

- a) El IDS bloquea; el IPS solo alerta
- b) El IDS detecta/alerta; el IPS además puede bloquear en línea
- c) Son idénticos
- d) El IPS solo funciona en la nube

<details><summary>Ver respuesta</summary>

**Correcta: b) El IDS detecta/alerta; el IPS además puede bloquear en línea.** IPS está en línea y puede cortar el tráfico; el IDS observa y alerta.

</details>

**4. ¿En qué puerto opera DNS habitualmente?**

- a) 22
- b) 53
- c) 80
- d) 443

<details><summary>Ver respuesta</summary>

**Correcta: b) 53.** DNS usa el 53 (UDP y TCP). Su apertura casi universal habilita el tunneling.

</details>

**5. Un objetivo Windows suele no responder a escaneos FIN/NULL/Xmas porque…**

- a) Tiene el firewall apagado
- b) No sigue estrictamente el RFC 793 en ese comportamiento
- c) Usa IPv6
- d) Nmap no soporta Windows

<details><summary>Ver respuesta</summary>

**Correcta: b) No sigue estrictamente el RFC 793 en ese comportamiento.** Esos escaneos dependen del comportamiento RFC 793 que Windows no implementa igual.

</details>

## Parte 2 — Criptografía aplicada

**1. ¿Cuál es una propiedad esperada de una función hash criptográfica?**

- a) Ser reversible
- b) Resistencia a colisiones
- c) Requerir una clave
- d) Comprimir sin pérdida

<details><summary>Ver respuesta</summary>

**Correcta: b) Resistencia a colisiones.** Debe ser unidireccional y resistente a colisiones; no usa clave (a diferencia de HMAC).

</details>

**2. ¿Por qué el modo ECB es inseguro para datos con patrones?**

- a) Es muy lento
- b) Bloques de texto idénticos producen bloques cifrados idénticos
- c) No usa clave
- d) Solo cifra texto ASCII

<details><summary>Ver respuesta</summary>

**Correcta: b) Bloques de texto idénticos producen bloques cifrados idénticos.** ECB filtra patrones; usa modos con IV (CBC/CTR) o AEAD (GCM).

</details>

**3. Para almacenar contraseñas, ¿qué es lo recomendado hoy?**

- a) MD5 sin sal
- b) SHA-1
- c) Argon2 / bcrypt / scrypt con sal
- d) Base64

<details><summary>Ver respuesta</summary>

**Correcta: c) Argon2 / bcrypt / scrypt con sal.** Funciones de derivación lentas y con sal frenan el crackeo masivo.

</details>

**4. En criptografía asimétrica (RSA), lo que cifra con la clave pública se descifra con…**

- a) La misma clave pública
- b) La clave privada correspondiente
- c) Un hash
- d) Una sal

<details><summary>Ver respuesta</summary>

**Correcta: b) La clave privada correspondiente.** Par de claves: lo cifrado con la pública solo lo abre la privada.

</details>

**5. ¿Qué garantiza principalmente TLS en una conexión HTTPS?**

- a) Solo velocidad
- b) Confidencialidad, integridad y autenticación del servidor
- c) Que el sitio no tenga bugs
- d) Anonimato total

<details><summary>Ver respuesta</summary>

**Correcta: b) Confidencialidad, integridad y autenticación del servidor.** TLS cifra el canal, verifica integridad y autentica al servidor vía certificado.

</details>

## Parte 3 — Hacking ético y pentesting: metodología

**1. ¿Qué documento define el alcance y lo permitido en un pentest?**

- a) El reporte final
- b) Las reglas de engagement (RoE) / contrato
- c) El exploit
- d) El README

<details><summary>Ver respuesta</summary>

**Correcta: b) Las reglas de engagement (RoE) / contrato.** Las RoE fijan alcance, ventanas, límites y autorización por escrito.

</details>

**2. En la metodología PTES, el reconocimiento va…**

- a) Al final
- b) Antes de la explotación
- c) Nunca
- d) Solo en web

<details><summary>Ver respuesta</summary>

**Correcta: b) Antes de la explotación.** Recon y enumeración preceden a la explotación y post-explotación.

</details>

**3. Meterpreter se usa típicamente en la fase de…**

- a) Reconocimiento pasivo
- b) Post-explotación
- c) Redacción del informe
- d) Escaneo de puertos

<details><summary>Ver respuesta</summary>

**Correcta: b) Post-explotación.** Es un payload de post-explotación de Metasploit.

</details>

**4. ¿Qué NO debe hacer un pentester ético durante un engagement?**

- a) Documentar hallazgos
- b) Respetar el alcance
- c) Borrar los logs para ocultar su actividad
- d) Reportar vulnerabilidades

<details><summary>Ver respuesta</summary>

**Correcta: c) Borrar los logs para ocultar su actividad.** El consultor preserva evidencia y trazabilidad; no destruye registros.

</details>

**5. Lo más importante del entregable final es…**

- a) La cantidad de comandos
- b) El resumen ejecutivo y hallazgos priorizados por riesgo
- c) El color del PDF
- d) El número de páginas

<details><summary>Ver respuesta</summary>

**Correcta: b) El resumen ejecutivo y hallazgos priorizados por riesgo.** Debe permitir a negocio decidir y a los técnicos remediar.

</details>

## Parte 4 — Seguridad de aplicaciones web

**1. La inyección SQL ocurre cuando…**

- a) El servidor es lento
- b) La entrada del usuario se concatena sin parametrizar en la consulta
- c) Se usa HTTPS
- d) El sitio usa cookies

<details><summary>Ver respuesta</summary>

**Correcta: b) La entrada del usuario se concatena sin parametrizar en la consulta.** La defensa principal son las consultas parametrizadas (prepared statements).

</details>

**2. ¿Qué tipo de XSS persiste en el servidor y afecta a otros usuarios?**

- a) Reflejado
- b) Almacenado
- c) Basado en DOM
- d) Ninguno

<details><summary>Ver respuesta</summary>

**Correcta: b) Almacenado.** El XSS almacenado guarda el payload y se sirve a cada visitante.

</details>

**3. SSRF permite a un atacante…**

- a) Cifrar la base de datos
- b) Hacer que el servidor haga peticiones a destinos internos
- c) Acelerar la app
- d) Cambiar el CSS

<details><summary>Ver respuesta</summary>

**Correcta: b) Hacer que el servidor haga peticiones a destinos internos.** Server-Side Request Forgery abusa del servidor como proxy hacia recursos internos.

</details>

**4. IDOR es un fallo de…**

- a) Cifrado
- b) Control de acceso (referencia directa a objetos sin autorización)
- c) Rendimiento
- d) Configuración de DNS

<details><summary>Ver respuesta</summary>

**Correcta: b) Control de acceso (referencia directa a objetos sin autorización).** Cambiar un identificador accede a datos de otro usuario por falta de verificación.

</details>

**5. La mejor defensa contra CSRF es…**

- a) Ocultar el formulario
- b) Tokens anti-CSRF y SameSite en cookies
- c) Usar GET para todo
- d) Deshabilitar JavaScript

<details><summary>Ver respuesta</summary>

**Correcta: b) Tokens anti-CSRF y SameSite en cookies.** Token por sesión/petición y cookies SameSite frenan la petición forjada.

</details>

**6. Un servicio construye `ping -c 1 <host>` con un valor externo. ¿Por qué pasar los argumentos como lista (argv) protege más que escapar metacaracteres?**

- a) Porque la lista es más rápida
- b) Porque no hay shell que reinterprete el texto: cada elemento llega al programa como un argumento y no como sintaxis
- c) Porque elimina la necesidad de validar el valor
- d) Porque solo funciona en Linux

<details><summary>Ver respuesta</summary>

**Correcta: b) Porque no hay shell que reinterprete el texto: cada elemento llega al programa como un argumento y no como sintaxis.** El escapado intenta predecir cómo un intérprete leerá el texto; con argv no hay intérprete que lo reinterprete. Aun así conviene validar con lista blanca y rechazar valores que empiecen por guion, que podrían tomarse como opciones.

</details>

**7. En un SSRF de octubre de 2026 un parámetro pensado para el esquema («protocolo») aceptaba una URL completa. ¿Qué defecto de diseño ilustra?**

- a) Falta de cifrado en tránsito
- b) El campo no tiene un dominio de valores acotado: debería ser una enumeración (http o https), no una cadena libre
- c) Uso de HTTP en lugar de HTTPS
- d) Ausencia de un límite de peticiones

<details><summary>Ver respuesta</summary>

**Correcta: b) El campo no tiene un dominio de valores acotado: debería ser una enumeración (http o https), no una cadena libre.** Validar el tipo de valor (enumeración) evita que el cliente decida el destino. Después sigue haciendo falta validar el destino resuelto contra rangos privados y metadatos.

</details>

**8. Un registro CVE indica que las versiones 7.0.0 a 7.1.2 de un producto tienen el mismo error que las 6.3.0 a 6.5.4, pero «no son explotables» por cambios en el marco subyacente. ¿Qué conclusión es correcta?**

- a) Las 7.x no necesitan ninguna acción
- b) Que un error exista y que sea explotable son hechos distintos; se actualiza igualmente, pero la urgencia difiere
- c) El registro está equivocado
- d) Solo importa la versión más antigua

<details><summary>Ver respuesta</summary>

**Correcta: b) Que un error exista y que sea explotable son hechos distintos; se actualiza igualmente, pero la urgencia difiere.** Distinguir existencia de explotabilidad evita tanto el pánico como la complacencia. Una versión no explotable hoy puede serlo si cambia el componente del que depende.

</details>

**9. ¿Qué comprobación protege realmente frente a un path traversal, incluidas las formas codificadas?**

- a) Buscar la cadena `..` en el nombre recibido
- b) Rechazar todos los nombres con barras
- c) Normalizar la ruta final y comprobar que sigue dentro del directorio base
- d) Convertir el nombre a minúsculas

<details><summary>Ver respuesta</summary>

**Correcta: c) Normalizar la ruta final y comprobar que sigue dentro del directorio base.** Las demás comprobaciones fallan ante codificaciones (`%2e%2e`, doble codificación), separadores alternativos o bytes nulos. Solo la ruta resuelta dice dónde se va a operar.

</details>

## Parte 5 — Explotación de sistemas y binarios

**1. Un buffer overflow en el stack puede sobrescribir…**

- a) El BIOS
- b) La dirección de retorno guardada
- c) El disco duro
- d) El DNS

<details><summary>Ver respuesta</summary>

**Correcta: b) La dirección de retorno guardada.** Al desbordar, se pisa la saved return address y se desvía el flujo.

</details>

**2. ¿Qué protección aleatoriza las direcciones de memoria?**

- a) DEP/NX
- b) ASLR
- c) Stack canary
- d) PIE

<details><summary>Ver respuesta</summary>

**Correcta: b) ASLR.** ASLR randomiza el mapa de memoria; DEP/NX marca zonas no ejecutables.

</details>

**3. ROP (Return-Oriented Programming) sirve para…**

- a) Compilar más rápido
- b) Ejecutar código reutilizando 'gadgets' cuando NX impide shellcode
- c) Cifrar el binario
- d) Depurar sin GDB

<details><summary>Ver respuesta</summary>

**Correcta: b) Ejecutar código reutilizando 'gadgets' cuando NX impide shellcode.** Encadena gadgets que terminan en `ret` para eludir NX/DEP.

</details>

**4. ¿Qué herramienta es de ingeniería inversa?**

- a) Nmap
- b) Ghidra
- c) Wireshark
- d) Hydra

<details><summary>Ver respuesta</summary>

**Correcta: b) Ghidra.** Ghidra (y IDA/radare2) desensamblan y decompilan binarios.

</details>

**5. El fuzzing busca vulnerabilidades…**

- a) Leyendo el manual
- b) Enviando entradas malformadas/aleatorias para provocar fallos
- c) Cifrando el binario
- d) Escaneando puertos

<details><summary>Ver respuesta</summary>

**Correcta: b) Enviando entradas malformadas/aleatorias para provocar fallos.** AFL++/libFuzzer mutan entradas para encontrar crashes explotables.

</details>

## Parte 6 — Análisis de malware

**1. El análisis estático se diferencia del dinámico en que…**

- a) Ejecuta la muestra
- b) Examina la muestra SIN ejecutarla
- c) Requiere Internet
- d) Solo aplica a Linux

<details><summary>Ver respuesta</summary>

**Correcta: b) Examina la muestra SIN ejecutarla.** Estático = sin ejecutar (strings, PE, desensamblado); dinámico = observar en ejecución.

</details>

**2. ¿Dónde se debe ejecutar malware para analizarlo?**

- a) En tu equipo principal
- b) En una VM aislada sin acceso a la red productiva
- c) En un servidor de producción
- d) En el móvil

<details><summary>Ver respuesta</summary>

**Correcta: b) En una VM aislada sin acceso a la red productiva.** Sandbox/VM aislada con snapshots; nunca en equipos reales o con red abierta.

</details>

**3. Las reglas YARA sirven para…**

- a) Cifrar malware
- b) Detectar/clasificar muestras por patrones
- c) Acelerar el disco
- d) Compilar exploits

<details><summary>Ver respuesta</summary>

**Correcta: b) Detectar/clasificar muestras por patrones.** YARA describe patrones (strings/bytes) para cazar familias de malware.

</details>

**4. El 'packing' de un binario busca…**

- a) Reducir su tamaño y/o ofuscar su contenido
- b) Firmarlo digitalmente
- c) Documentarlo
- d) Traducirlo

<details><summary>Ver respuesta</summary>

**Correcta: a) Reducir su tamaño y/o ofuscar su contenido.** Comprime/cifra el código; hay que 'unpackear' para analizarlo.

</details>

**5. El tráfico C2 de un malware es…**

- a) Su interfaz gráfica
- b) El canal de comando y control con el atacante
- c) Un antivirus
- d) Un instalador

<details><summary>Ver respuesta</summary>

**Correcta: b) El canal de comando y control con el atacante.** Command & Control: recibe órdenes y exfiltra datos; su beaconing es detectable.

</details>

## Parte 7 — Red Team y operaciones ofensivas

**1. MITRE ATT&CK es…**

- a) Un antivirus
- b) Una base de conocimiento de tácticas y técnicas de adversarios
- c) Un lenguaje de programación
- d) Un firewall

<details><summary>Ver respuesta</summary>

**Correcta: b) Una base de conocimiento de tácticas y técnicas de adversarios.** Mapea el comportamiento del adversario; sirve para ofensiva y defensa.

</details>

**2. El Kerberoasting ataca…**

- a) Certificados TLS
- b) Cuentas de servicio pidiendo tickets TGS crackeables offline
- c) El BIOS
- d) El DNS

<details><summary>Ver respuesta</summary>

**Correcta: b) Cuentas de servicio pidiendo tickets TGS crackeables offline.** Solicita TGS de cuentas con SPN y crackea su hash fuera de línea.

</details>

**3. Pass-the-Hash permite autenticarse…**

- a) Con la contraseña en claro
- b) Usando el hash NTLM sin conocer la contraseña
- c) Solo con biometría
- d) Con un OTP

<details><summary>Ver respuesta</summary>

**Correcta: b) Usando el hash NTLM sin conocer la contraseña.** Reutiliza el hash como credencial para moverse lateralmente.

</details>

**4. BloodHound se usa para…**

- a) Cifrar el dominio
- b) Graficar rutas de ataque en Active Directory
- c) Escanear puertos
- d) Analizar malware

<details><summary>Ver respuesta</summary>

**Correcta: b) Graficar rutas de ataque en Active Directory.** Modela relaciones AD y encuentra caminos hacia Domain Admins.

</details>

**5. Un Golden Ticket se forja con el hash de…**

- a) Administrator local
- b) La cuenta krbtgt
- c) El usuario invitado
- d) La cuenta SYSTEM

<details><summary>Ver respuesta</summary>

**Correcta: b) La cuenta krbtgt.** Con el hash de krbtgt se firman TGTs arbitrarios (control total del dominio).

</details>

## Parte 8 — Blue Team, detección y SOC

**1. Un SIEM sirve principalmente para…**

- a) Cifrar discos
- b) Centralizar, correlacionar y alertar sobre logs/telemetría
- c) Escanear puertos
- d) Compilar exploits

<details><summary>Ver respuesta</summary>

**Correcta: b) Centralizar, correlacionar y alertar sobre logs/telemetría.** Agrega eventos de múltiples fuentes y dispara detecciones.

</details>

**2. Sigma es…**

- a) Un SIEM propietario
- b) Un formato genérico de reglas de detección portable entre SIEMs
- c) Un malware
- d) Un protocolo de red

<details><summary>Ver respuesta</summary>

**Correcta: b) Un formato genérico de reglas de detección portable entre SIEMs.** Describe detecciones en YAML y se traduce a la query de cada SIEM.

</details>

**3. El 'threat hunting' es…**

- a) Esperar alertas pasivamente
- b) Buscar proactivamente amenazas no detectadas por las alertas
- c) Apagar el SIEM
- d) Instalar parches

<details><summary>Ver respuesta</summary>

**Correcta: b) Buscar proactivamente amenazas no detectadas por las alertas.** Hipótesis + datos para hallar lo que las reglas no marcaron.

</details>

**4. Un exceso de falsos positivos en detección provoca…**

- a) Mejor seguridad siempre
- b) Fatiga de alertas y riesgo de ignorar lo importante
- c) Menos logs
- d) Más CPU en el atacante

<details><summary>Ver respuesta</summary>

**Correcta: b) Fatiga de alertas y riesgo de ignorar lo importante.** Hay que afinar reglas para no saturar al analista.

</details>

**5. El Event ID 1102 de Windows indica…**

- a) Inicio de sesión correcto
- b) Que se limpió el registro de auditoría (Security log)
- c) Actualización del sistema
- d) Cambio de contraseña

<details><summary>Ver respuesta</summary>

**Correcta: b) Que se limpió el registro de auditoría (Security log).** Es una señal fuerte de anti-forense: borrado del log de seguridad.

</details>

**6. Una regla detecta que se añade una credencial a una aplicación y alerta cuando el actor no figura como propietario. Sin el inventario de propietarios, ¿qué ocurre?**

- a) La regla deja de funcionar
- b) Alerta también sobre el cambio legítimo de un administrador: la calidad depende del dato de contexto
- c) Detecta más ataques reales
- d) Se vuelve más rápida

<details><summary>Ver respuesta</summary>

**Correcta: b) Alerta también sobre el cambio legítimo de un administrador: la calidad depende del dato de contexto.** La condición por sí sola no distingue un cambio autorizado de uno hostil; el inventario es parte de la regla. Medir con datos sintéticos lo hace visible.

</details>

## Parte 9 — Forense digital y respuesta a incidentes

**1. Según el orden de volatilidad, ¿qué se adquiere primero?**

- a) El disco duro
- b) La memoria RAM y el estado volátil
- c) Los backups
- d) El CD-ROM

<details><summary>Ver respuesta</summary>

**Correcta: b) La memoria RAM y el estado volátil.** Lo más volátil (RAM, conexiones) se captura antes de apagar.

</details>

**2. La cadena de custodia garantiza…**

- a) Que la evidencia se pueda alterar
- b) La trazabilidad e integridad de la evidencia desde su recolección
- c) Mayor velocidad de análisis
- d) Cifrado del disco

<details><summary>Ver respuesta</summary>

**Correcta: b) La trazabilidad e integridad de la evidencia desde su recolección.** Documenta quién, cuándo y cómo manipuló la evidencia (validez legal).

</details>

**3. Volatility es una herramienta de…**

- a) Escaneo de red
- b) Análisis forense de memoria RAM
- c) Cracking de contraseñas
- d) Fuzzing

<details><summary>Ver respuesta</summary>

**Correcta: b) Análisis forense de memoria RAM.** Analiza volcados de memoria para procesos, conexiones, inyecciones, etc.

</details>

**4. El ciclo de respuesta a incidentes (NIST/SANS) incluye, entre otras, las fases de…**

- a) Compilación y linkeo
- b) Preparación, detección, contención, erradicación y recuperación
- c) Escaneo y explotación
- d) Diseño y despliegue

<details><summary>Ver respuesta</summary>

**Correcta: b) Preparación, detección, contención, erradicación y recuperación.** Es el flujo estándar de IR, más lecciones aprendidas.

</details>

**5. El 'timestomping' consiste en…**

- a) Sincronizar relojes
- b) Manipular las marcas de tiempo de archivos para despistar
- c) Acelerar el disco
- d) Cifrar timestamps

<details><summary>Ver respuesta</summary>

**Correcta: b) Manipular las marcas de tiempo de archivos para despistar.** Se detecta comparando $STANDARD_INFORMATION vs $FILE_NAME en NTFS.

</details>

**6. Tras el compromiso del plano de gestión de un entorno, ¿qué copias de seguridad cuentan como un plan de recuperación?**

- a) Todas las que existen
- b) Solo las fuera del alcance del atacante, inmutables y con restauración probada recientemente
- c) Las más recientes
- d) Las que están en el mismo proveedor, por su rapidez

<details><summary>Ver respuesta</summary>

**Correcta: b) Solo las fuera del alcance del atacante, inmutables y con restauración probada recientemente.** Si faltan alcance, inmutabilidad o prueba de restauración, la copia es una esperanza y no un plan. El RPO que importa es el realmente alcanzable, no el configurado.

</details>

## Parte 10 — Seguridad en la nube y contenedores

**1. El modelo de responsabilidad compartida dice que…**

- a) El proveedor es responsable de todo
- b) El cliente es responsable de todo
- c) El proveedor asegura la nube y el cliente la seguridad EN la nube
- d) Nadie es responsable

<details><summary>Ver respuesta</summary>

**Correcta: c) El proveedor asegura la nube y el cliente la seguridad EN la nube.** El reparto varía según IaaS/PaaS/SaaS, pero el cliente siempre configura su parte.

</details>

**2. Una causa muy común de brechas en la nube es…**

- a) Cifrado fuerte
- b) Configuraciones erróneas (p. ej. buckets públicos, IAM laxo)
- c) Usar MFA
- d) Rotar claves

<details><summary>Ver respuesta</summary>

**Correcta: b) Configuraciones erróneas (p. ej. buckets públicos, IAM laxo).** El misconfiguration domina los incidentes cloud.

</details>

**3. En Kubernetes, RBAC controla…**

- a) El ancho de banda
- b) Quién puede hacer qué sobre los recursos del clúster
- c) El cifrado de disco
- d) La CPU de los pods

<details><summary>Ver respuesta</summary>

**Correcta: b) Quién puede hacer qué sobre los recursos del clúster.** Role-Based Access Control define permisos por sujeto y recurso.

</details>

**4. Un 'container escape' es…**

- a) Reiniciar el contenedor
- b) Salir del aislamiento del contenedor hacia el host
- c) Borrar una imagen
- d) Exportar logs

<details><summary>Ver respuesta</summary>

**Correcta: b) Salir del aislamiento del contenedor hacia el host.** Abusa de configuraciones (privileged, mounts) para llegar al host.

</details>

**5. Para IAM en la nube, la buena práctica es…**

- a) Usar siempre la cuenta root
- b) Permisos amplios por comodidad
- c) Mínimo privilegio y roles temporales
- d) Claves compartidas por equipo

<details><summary>Ver respuesta</summary>

**Correcta: c) Mínimo privilegio y roles temporales.** Menos privilegio + credenciales efímeras reducen el impacto.

</details>

**6. Ante el abuso de una aplicación de un proveedor con consentimiento en tu inquilino, ¿por qué se recomienda deshabilitarla y no eliminarla?**

- a) Porque eliminar es ilegal
- b) Porque deshabilitar corta el acceso y conserva la evidencia y el estado; eliminar destruye ambos y obliga a un nuevo consentimiento
- c) Porque la eliminación tarda más
- d) Porque deshabilitar borra los permisos

<details><summary>Ver respuesta</summary>

**Correcta: b) Porque deshabilitar corta el acceso y conserva la evidencia y el estado; eliminar destruye ambos y obliga a un nuevo consentimiento.** Se conserva la configuración y los registros para la investigación y se evita reconceder permisos sin saber si el proveedor restableció sus credenciales.

</details>

## Parte 11 — DevSecOps y seguridad del SDLC

**1. 'Shift-left' significa…**

- a) Mover la seguridad al final
- b) Integrar la seguridad temprano en el ciclo de desarrollo
- c) Eliminar las pruebas
- d) Desplegar sin revisar

<details><summary>Ver respuesta</summary>

**Correcta: b) Integrar la seguridad temprano en el ciclo de desarrollo.** Detectar y corregir antes = más barato y seguro.

</details>

**2. SAST vs DAST:**

- a) SAST prueba en ejecución; DAST lee el código
- b) SAST analiza el código fuente; DAST prueba la app en ejecución
- c) Son lo mismo
- d) Ambos requieren producción

<details><summary>Ver respuesta</summary>

**Correcta: b) SAST analiza el código fuente; DAST prueba la app en ejecución.** SAST = estático (código); DAST = dinámico (app corriendo).

</details>

**3. SCA (Software Composition Analysis) se enfoca en…**

- a) El estilo del código
- b) Vulnerabilidades en dependencias/terceros
- c) El diseño de la UI
- d) La velocidad de compilación

<details><summary>Ver respuesta</summary>

**Correcta: b) Vulnerabilidades en dependencias/terceros.** Clave contra ataques de cadena de suministro; complementa con SBOM.

</details>

**4. STRIDE es un método de…**

- a) Cifrado
- b) Modelado de amenazas
- c) Escaneo de puertos
- d) Gestión de logs

<details><summary>Ver respuesta</summary>

**Correcta: b) Modelado de amenazas.** Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation.

</details>

**5. Los secretos (API keys, contraseñas) en el código se deben…**

- a) Commitear al repo
- b) Gestionar en un vault/secret manager y escanear con pre-commit
- c) Poner en el README
- d) Enviar por chat

<details><summary>Ver respuesta</summary>

**Correcta: b) Gestionar en un vault/secret manager y escanear con pre-commit.** gitleaks/detect-secrets + gestores de secretos evitan filtraciones.

</details>

**6. Una plataforma informa que variables de entorno cifradas pudieron descifrarse sin precisar cuáles. ¿Cuál es la respuesta proporcionada?**

- a) Esperar el informe final
- b) Rotar todos los secretos que estuvieron almacenados en la plataforma, empezando por los de mayor impacto
- c) Rotar solo las claves de pago
- d) Eliminar la cuenta

<details><summary>Ver respuesta</summary>

**Correcta: b) Rotar todos los secretos que estuvieron almacenados en la plataforma, empezando por los de mayor impacto.** Si no se puede saber qué secretos se vieron, se asume compromiso de todos los que pudieron verse. Recibir un aviso de revocación de un proveedor no prueba que tu clave fuera robada.

</details>

## Parte 12 — OSINT e ingeniería social

**1. OSINT es…**

- a) Hackear con exploits
- b) Inteligencia a partir de fuentes abiertas y públicas
- c) Un tipo de malware
- d) Un firewall

<details><summary>Ver respuesta</summary>

**Correcta: b) Inteligencia a partir de fuentes abiertas y públicas.** Open Source Intelligence: recolección y análisis de información pública.

</details>

**2. Shodan es útil para…**

- a) Editar fotos
- b) Buscar dispositivos y servicios expuestos en Internet
- c) Cifrar correos
- d) Compilar código

<details><summary>Ver respuesta</summary>

**Correcta: b) Buscar dispositivos y servicios expuestos en Internet.** Indexa banners de servicios expuestos (cámaras, ICS, servidores).

</details>

**3. El pretexting en ingeniería social es…**

- a) Un exploit de kernel
- b) Construir un escenario/identidad falsa creíble para manipular
- c) Un algoritmo de hash
- d) Un escaneo de red

<details><summary>Ver respuesta</summary>

**Correcta: b) Construir un escenario/identidad falsa creíble para manipular.** Base de vishing y muchos fraudes; explota la confianza.

</details>

**4. Los metadatos EXIF de una foto pueden revelar…**

- a) Nada relevante
- b) Coordenadas GPS, dispositivo y fecha
- c) La contraseña del autor
- d) El código fuente

<details><summary>Ver respuesta</summary>

**Correcta: b) Coordenadas GPS, dispositivo y fecha.** Antes de publicar conviene eliminarlos.

</details>

**5. La ingeniería social solo debe practicarse…**

- a) Contra cualquiera
- b) Con autorización explícita y por escrito (engagement)
- c) En redes sociales ajenas
- d) Sin límites

<details><summary>Ver respuesta</summary>

**Correcta: b) Con autorización explícita y por escrito (engagement).** Sin permiso es fraude/acoso; en pentest va acotada en las RoE.

</details>

## Parte 13 — Seguridad móvil, IoT e inalámbrica

**1. Un APK de Android se puede analizar estáticamente con…**

- a) Volatility
- b) apktool / jadx / MobSF
- c) Hashcat
- d) Snort

<details><summary>Ver respuesta</summary>

**Correcta: b) apktool / jadx / MobSF.** Descompilan y revisan el manifest, permisos y código.

</details>

**2. Un ataque 'Evil Twin' de WiFi consiste en…**

- a) Clonar una tarjeta SIM
- b) Levantar un punto de acceso falso que imita a uno legítimo
- c) Cifrar el router
- d) Bloquear el 5G

<details><summary>Ver respuesta</summary>

**Correcta: b) Levantar un punto de acceso falso que imita a uno legítimo.** La víctima se conecta al AP del atacante, que intercepta el tráfico.

</details>

**3. El análisis de firmware de un dispositivo IoT suele empezar por…**

- a) Pintar la carcasa
- b) Extraer y descomprimir la imagen del firmware para buscar binarios/credenciales
- c) Cambiar el color del LED
- d) Actualizar el reloj

<details><summary>Ver respuesta</summary>

**Correcta: b) Extraer y descomprimir la imagen del firmware para buscar binarios/credenciales.** binwalk y similares extraen sistemas de archivos y secretos embebidos.

</details>

**4. Interfaces de hardware como UART/JTAG sirven para…**

- a) Cargar el móvil
- b) Acceder a consola/depuración del dispositivo
- c) Conectar a WiFi
- d) Enviar SMS

<details><summary>Ver respuesta</summary>

**Correcta: b) Acceder a consola/depuración del dispositivo.** Dan acceso de bajo nivel muy útil para el hacking de hardware.

</details>

**5. BLE (Bluetooth Low Energy) es relevante en seguridad porque…**

- a) No existe
- b) Muchos dispositivos lo usan y puede tener emparejamiento/cifrado débil
- c) Solo lo usan impresoras
- d) Es imposible de interceptar

<details><summary>Ver respuesta</summary>

**Correcta: b) Muchos dispositivos lo usan y puede tener emparejamiento/cifrado débil.** Wearables/IoT lo usan; hay ataques de sniffing y suplantación.

</details>

**6. Un dispositivo supera la attestation de su secure element. ¿Qué se puede concluir?**

- a) Que todo el dispositivo es original e íntegro
- b) Que ese chip es original; la integridad física del resto no queda demostrada
- c) Que no hay implantes posibles
- d) Que la cadena de custodia es continua

<details><summary>Ver respuesta</summary>

**Correcta: b) Que ese chip es original; la integridad física del resto no queda demostrada.** La attestation responde por el componente, no por lo que lo rodea ni por su recorrido.

</details>

**7. ¿Por qué un sello antimanipulación intacto no prueba que nadie abrió el dispositivo?**

- a) Porque nunca se rompe
- b) Porque puede reproducirse o reabrirse sin rastro y solo sirve si alguien lo inspecciona
- c) Porque el fabricante no los usa
- d) Porque solo protege el firmware

<details><summary>Ver respuesta</summary>

**Correcta: b) Porque puede reproducirse o reabrirse sin rastro y solo sirve si alguien lo inspecciona.** Sirve como trazabilidad, no como garantía de integridad.

</details>

**8. En una comparación de placa aparece una pantalla de otro lote. ¿Cuál es la conclusión más defendible?**

- a) Hay un implante
- b) Es una diferencia sin explicar que exige contrastar con una orden de servicio o un cambio de proveedor
- c) No importa
- d) El dispositivo es falso

<details><summary>Ver respuesta</summary>

**Correcta: b) Es una diferencia sin explicar que exige contrastar con una orden de servicio o un cambio de proveedor.** Una diferencia no es un componente añadido; hay que formular una hipótesis comprobable.

</details>

**9. Tras un incidente de implante en el canal de pantalla, ¿qué remedio resuelve la exposición de la frase de recuperación?**

- a) Reiniciar de fábrica el dispositivo
- b) Actualizar el firmware
- c) Generar un secreto nuevo en un dispositivo de confianza y migrar los activos
- d) Cambiar la contraseña de la aplicación

<details><summary>Ver respuesta</summary>

**Correcta: c) Generar un secreto nuevo en un dispositivo de confianza y migrar los activos.** La electrónica añadida no depende del firmware: se rota el secreto expuesto.

</details>

## Parte 14 — GRC, riesgo y cumplimiento

**1. En términos simples, el riesgo se estima como…**

- a) Solo el impacto
- b) Probabilidad × impacto
- c) Número de servidores
- d) Cantidad de logs

<details><summary>Ver respuesta</summary>

**Correcta: b) Probabilidad × impacto.** Se prioriza combinando la probabilidad de ocurrencia y su impacto.

</details>

**2. ISO/IEC 27001 define…**

- a) Un lenguaje de programación
- b) Requisitos para un Sistema de Gestión de Seguridad de la Información (SGSI)
- c) Un antivirus
- d) Un protocolo de red

<details><summary>Ver respuesta</summary>

**Correcta: b) Requisitos para un Sistema de Gestión de Seguridad de la Información (SGSI).** Marco certificable de gestión de la seguridad basado en riesgos.

</details>

**3. GDPR regula principalmente…**

- a) El cifrado militar
- b) La protección de datos personales en la UE
- c) Los puertos TCP
- d) El diseño web

<details><summary>Ver respuesta</summary>

**Correcta: b) La protección de datos personales en la UE.** Derechos de los titulares y obligaciones de quien trata datos personales.

</details>

**4. Un plan de continuidad de negocio (BCP) busca…**

- a) Vender más
- b) Mantener/recuperar las operaciones críticas ante una disrupción
- c) Instalar juegos
- d) Cifrar correos

<details><summary>Ver respuesta</summary>

**Correcta: b) Mantener/recuperar las operaciones críticas ante una disrupción.** El DRP es su componente tecnológico de recuperación.

</details>

**5. Un control 'compensatorio' es…**

- a) Un control que elimina el activo
- b) Una medida alternativa cuando el control principal no es viable
- c) Un ataque
- d) Un tipo de malware

<details><summary>Ver respuesta</summary>

**Correcta: b) Una medida alternativa cuando el control principal no es viable.** Reduce el riesgo cuando no se puede aplicar el control ideal.

</details>

## Parte 15 — Seguridad de IA y machine learning

**1. La 'prompt injection' en una app con LLM consiste en…**

- a) Cifrar el prompt
- b) Introducir instrucciones que manipulan el comportamiento del modelo
- c) Acelerar la inferencia
- d) Entrenar más rápido

<details><summary>Ver respuesta</summary>

**Correcta: b) Introducir instrucciones que manipulan el comportamiento del modelo.** Es el riesgo #1 del OWASP Top 10 para LLM; incluye inyección indirecta.

</details>

**2. El envenenamiento de datos (data poisoning) ataca…**

- a) La GPU
- b) Los datos de entrenamiento para sesgar/backdoorear el modelo
- c) El firewall
- d) El DNS

<details><summary>Ver respuesta</summary>

**Correcta: b) Los datos de entrenamiento para sesgar/backdoorear el modelo.** Datos maliciosos en el entrenamiento comprometen el modelo resultante.

</details>

**3. Un ejemplo adversarial es…**

- a) Un dataset limpio
- b) Una entrada perturbada sutilmente para engañar al modelo
- c) Un modelo más grande
- d) Un optimizador

<details><summary>Ver respuesta</summary>

**Correcta: b) Una entrada perturbada sutilmente para engañar al modelo.** Pequeñas perturbaciones causan clasificaciones erróneas.

</details>

**4. OWASP mantiene un Top 10 específico para…**

- a) Impresoras
- b) Aplicaciones con LLM
- c) Routers
- d) Bases de datos

<details><summary>Ver respuesta</summary>

**Correcta: b) Aplicaciones con LLM.** Cataloga los riesgos típicos de apps que integran modelos de lenguaje.

</details>

**5. Al integrar un LLM con herramientas/agentes, un riesgo clave es…**

- a) Que responda rápido
- b) Que una inyección logre ejecutar acciones no deseadas
- c) Que use poca RAM
- d) Que hable español

<details><summary>Ver respuesta</summary>

**Correcta: b) Que una inyección logre ejecutar acciones no deseadas.** Hay que limitar permisos del agente y validar entradas/salidas.

</details>

**6. ¿Qué distingue al LLMjacking de la prompt injection?**

- a) El LLMjacking abusa del acceso (credenciales o endpoints) para consumir inferencia ajena; la injection manipula el comportamiento del modelo con texto
- b) Son sinónimos
- c) La injection exige robar una clave de API
- d) El LLMjacking solo afecta a modelos open source

<details><summary>Ver respuesta</summary>

**Correcta: a) El LLMjacking abusa del acceso (credenciales o endpoints) para consumir inferencia ajena; la injection manipula el comportamiento del modelo con texto.** Uno explota el acceso y la factura; el otro, el canal de instrucciones del modelo. Los controles son distintos.

</details>

**7. ¿Por qué una alerta de presupuesto no equivale a un límite de gasto?**

- a) Porque nunca se envía
- b) Porque informa con retraso y no detiene el consumo; el gasto puede superar el umbral antes del aviso
- c) Porque solo funciona con modelos propios
- d) Porque el proveedor la ignora

<details><summary>Ver respuesta</summary>

**Correcta: b) Porque informa con retraso y no detiene el consumo; el gasto puede superar el umbral antes del aviso.** La documentación de AWS Budgets indica actualización hasta tres veces al día y retraso entre cargo y notificación. Detener exige cuotas, límites en línea o acciones automáticas.

</details>

**8. Un barrido de cientos de solicitudes con max_tokens=1 sobre varios modelos desde un origen nuevo es mejor interpretado como…**

- a) Una prueba concluyente de ataque atribuible a un actor
- b) Una anomalía compatible con validación de credenciales que requiere correlación
- c) Tráfico normal de un modelo pequeño
- d) Un fallo del proveedor

<details><summary>Ver respuesta</summary>

**Correcta: b) Una anomalía compatible con validación de credenciales que requiere correlación.** Es un indicador, no una atribución: se confirma correlando identidad, origen, API invocada y facturación.

</details>

**9. ¿Qué riesgo introduce un tope duro de gasto por identidad?**

- a) Ninguno
- b) Puede denegar tráfico legítimo, incluso porque el atacante agote la cuota
- c) Aumenta el gasto
- d) Impide registrar eventos

<details><summary>Ver respuesta</summary>

**Correcta: b) Puede denegar tráfico legítimo, incluso porque el atacante agote la cuota.** Un control preventivo tiene coste colateral: debe decidirse y aceptarse explícitamente.

</details>

## Parte 16 — Capstones y preparación de certificaciones

**1. La certificación OSCP es conocida por…**

- a) Ser 100% teórica
- b) Su examen práctico de 24h con mentalidad 'Try Harder'
- c) No tener examen
- d) Ser solo defensiva

<details><summary>Ver respuesta</summary>

**Correcta: b) Su examen práctico de 24h con mentalidad 'Try Harder'.** Evalúa explotación práctica en un laboratorio bajo tiempo.

</details>

**2. El CISSP se estructura en…**

- a) 3 laboratorios
- b) 8 dominios de conocimiento
- c) 1 examen práctico de pwn
- d) Solo criptografía

<details><summary>Ver respuesta</summary>

**Correcta: b) 8 dominios de conocimiento.** Cubre seguridad de forma amplia y gerencial (8 dominios).

</details>

**3. Un buen 'home lab' permanente sirve para…**

- a) Nada útil
- b) Practicar de forma continua y segura sin depender de terceros
- c) Solo ver películas
- d) Minar cripto

<details><summary>Ver respuesta</summary>

**Correcta: b) Practicar de forma continua y segura sin depender de terceros.** Es la base del aprendizaje continuo y del portafolio.

</details>

**4. Para construir portafolio, es recomendable…**

- a) Copiar writeups ajenos
- b) Documentar tus propios labs, CTFs y proyectos
- c) No mostrar nada
- d) Solo listar cursos

<details><summary>Ver respuesta</summary>

**Correcta: b) Documentar tus propios labs, CTFs y proyectos.** Evidencia práctica > lista de certificados sin contexto.

</details>

**5. En ciberseguridad, el aprendizaje…**

- a) Termina con una cert
- b) Es continuo: el panorama de amenazas cambia constantemente
- c) No es necesario
- d) Solo importa la teoría

<details><summary>Ver respuesta</summary>

**Correcta: b) Es continuo: el panorama de amenazas cambia constantemente.** Comunidad, práctica y actualización constante son parte del oficio.

</details>

## Parte 17 — Profundización para certificaciones

**1. En la clasificación de datos, ¿quién define el nivel de clasificación de un activo?**

- a) El custodio (custodian)
- b) El propietario del dato (data owner)
- c) Cualquier usuario
- d) El proveedor de nube

<details><summary>Ver respuesta</summary>

**Correcta: b) El propietario del dato (data owner).** El data owner clasifica y define requisitos; el custodio los implementa/mantiene.

</details>

**2. Según NIST SP 800-88, 'purge' frente a 'clear' implica…**

- a) Lo mismo
- b) Un borrado más resistente a ataques de laboratorio (p. ej. criptoborrado)
- c) Solo borrar la papelera
- d) Cifrar el disco

<details><summary>Ver respuesta</summary>

**Correcta: b) Un borrado más resistente a ataques de laboratorio (p. ej. criptoborrado).** Clear resiste ataques simples; purge resiste incluso recuperación de laboratorio; destroy es físico.

</details>

**3. En IAM, el patrón 'joiner-mover-leaver' se refiere a…**

- a) Un ataque de fuerza bruta
- b) El ciclo de vida de una identidad (alta, cambios, baja)
- c) Un tipo de MFA
- d) Un modelo de cifrado

<details><summary>Ver respuesta</summary>

**Correcta: b) El ciclo de vida de una identidad (alta, cambios, baja).** Gestiona aprovisionamiento, cambios de rol y desaprovisionamiento oportuno de accesos.

</details>

**4. SAML y OpenID Connect se usan para…**

- a) Cifrar discos
- b) Federación de identidad y single sign-on (SSO)
- c) Escanear puertos
- d) Analizar malware

<details><summary>Ver respuesta</summary>

**Correcta: b) Federación de identidad y single sign-on (SSO).** SAML (XML) y OIDC (sobre OAuth2) permiten autenticación federada entre dominios.

</details>

**5. El modelo Bell-LaPadula se enfoca en proteger la…**

- a) Integridad
- b) Disponibilidad
- c) Confidencialidad (no leer arriba, no escribir abajo)
- d) Velocidad

<details><summary>Ver respuesta</summary>

**Correcta: c) Confidencialidad (no leer arriba, no escribir abajo).** Bell-LaPadula = confidencialidad; Biba y Clark-Wilson se enfocan en integridad.

</details>

**6. Para priorizar la remediación de vulnerabilidades, además de CVSS conviene usar…**

- a) El orden alfabético
- b) EPSS y la lista KEV de CISA (explotación real)
- c) El tamaño del archivo
- d) El color del reporte

<details><summary>Ver respuesta</summary>

**Correcta: b) EPSS y la lista KEV de CISA (explotación real).** CVSS mide severidad; EPSS estima probabilidad de exploit y KEV marca lo explotado activamente.

</details>

**7. En el análisis de un correo de phishing, SPF, DKIM y DMARC sirven para…**

- a) Cifrar el cuerpo
- b) Autenticar el origen del correo y detectar suplantación
- c) Comprimir adjuntos
- d) Acelerar la entrega

<details><summary>Ver respuesta</summary>

**Correcta: b) Autenticar el origen del correo y detectar suplantación.** Validan que el remitente esté autorizado y que el mensaje no fue alterado; DMARC define la política.

</details>

## Parte 18 — IA aplicada a la ciberseguridad

**1. ¿Cuál es el mayor riesgo operativo al usar un LLM en seguridad?**

- a) Que sea lento
- b) Las alucinaciones (salidas falsas con aplomo) sin verificación
- c) Que use mucha RAM
- d) Que no tenga interfaz gráfica

<details><summary>Ver respuesta</summary>

**Correcta: b) Las alucinaciones (salidas falsas con aplomo) sin verificación.** Un LLM genera lo plausible, no lo cierto; hay que verificar toda salida.

</details>

**2. El Model Context Protocol (MCP) sirve para…**

- a) Cifrar prompts
- b) Estandarizar cómo un agente de IA usa herramientas externas
- c) Entrenar modelos
- d) Escanear puertos

<details><summary>Ver respuesta</summary>

**Correcta: b) Estandarizar cómo un agente de IA usa herramientas externas.** MCP conecta clientes de IA con servidores que exponen tools/resources/prompts.

</details>

**3. En kali-mcp, las herramientas de Kali se ejecutan…**

- a) En tu host directamente
- b) Dentro de un contenedor Docker aislado
- c) En la nube de OpenAI
- d) En el navegador

<details><summary>Ver respuesta</summary>

**Correcta: b) Dentro de un contenedor Docker aislado.** kali-mcp aísla las herramientas en un contenedor; el agente habla con un gateway MCP.

</details>

**4. En un pentest asistido por IA, ¿quién decide y autoriza las acciones con impacto?**

- a) El agente de IA de forma autónoma
- b) El humano (el agente propone, la persona aprueba)
- c) El servidor MCP
- d) Nadie, se automatiza todo

<details><summary>Ver respuesta</summary>

**Correcta: b) El humano (el agente propone, la persona aprueba).** Human-in-the-loop: la IA propone y acelera; la autorización y responsabilidad son humanas.

</details>

**5. La 'prompt injection' contra tu propio agente de seguridad consiste en…**

- a) Un ataque de fuerza bruta
- b) Contenido malicioso en los datos que el agente procesa que intenta secuestrar sus instrucciones
- c) Un fallo de red
- d) Un cifrado débil

<details><summary>Ver respuesta</summary>

**Correcta: b) Contenido malicioso en los datos que el agente procesa que intenta secuestrar sus instrucciones.** Datos no confiables (banners, webs) pueden manipular al agente; por eso mínimo privilegio y aislamiento.

</details>

## Parte 19 — Seguridad de videojuegos, cheats y anti-cheat

**1. ¿Qué distingue mejor a un servidor autoritativo de uno client-authoritative?**

- a) El servidor cifra todos los paquetes
- b) El servidor valida intenciones y deriva el estado canónico
- c) El cliente no renderiza
- d) El servidor elimina la latencia

<details><summary>Ver respuesta</summary>

**Correcta: b) El servidor valida intenciones y deriva el estado canónico.** El cliente solicita acciones; el servidor comprueba precondiciones e invariantes antes de producir el resultado.

</details>

**2. Un radar educativo funciona principalmente porque…**

- a) Rompe siempre el depth buffer
- b) El cliente conoce posiciones suficientes para reconstruirlo
- c) UDP carece de cifrado
- d) ASLR está desactivado

<details><summary>Ver respuesta</summary>

**Correcta: b) El cliente conoce posiciones suficientes para reconstruirlo.** El problema fundamental suele ser la información excesiva replicada, aunque el overlay sea el síntoma visible.

</details>

**3. En world-to-screen, ¿por qué se divide por w después de la proyección?**

- a) Para cifrar coordenadas
- b) Para obtener coordenadas normalizadas de dispositivo
- c) Para medir latencia
- d) Para aplicar recoil

<details><summary>Ver respuesta</summary>

**Correcta: b) Para obtener coordenadas normalizadas de dispositivo.** La división perspectiva lleva coordenadas clip a NDC antes del escalado al viewport.

</details>

**4. Con FOV total de 60°, ¿qué ángulo máximo respecto al forward queda dentro?**

- a) 60°
- b) 120°
- c) 30°
- d) 15°

<details><summary>Ver respuesta</summary>

**Correcta: c) 30°.** Se compara la distancia angular con el semiancho del FOV: 30°.

</details>

**5. ¿Qué control evita mejor aceptar una cadencia de disparo imposible?**

- a) Ocultar ammo en la UI
- b) Cooldown y máquina de estados en el servidor
- c) Comprimir snapshots
- d) Cambiar el shader

<details><summary>Ver respuesta</summary>

**Correcta: b) Cooldown y máquina de estados en el servidor.** La autoridad del servidor valida tiempo, estado del arma y munición.

</details>

**6. ¿Qué relación es correcta entre prediction y reconciliation?**

- a) Prediction da autoridad permanente al cliente
- b) El cliente predice para responder y luego corrige/reaplica contra el estado del servidor
- c) Ambas eliminan packet loss
- d) Solo se usan con TCP

<details><summary>Ver respuesta</summary>

**Correcta: b) El cliente predice para responder y luego corrige/reaplica contra el estado del servidor.** La experiencia puede ser inmediata sin ceder la verdad canónica.

</details>

**7. Una alerta de snap aim con reacción sub-100 ms significa…**

- a) Culpabilidad concluyente
- b) Una hipótesis que requiere secuencia, contexto y alternativas legítimas
- c) Que el kernel fue comprometido
- d) Que la precisión es 100%

<details><summary>Ver respuesta</summary>

**Correcta: b) Una hipótesis que requiere secuencia, contexto y alternativas legítimas.** Anomalía no significa culpabilidad; habilidad, input, FPS y accesibilidad pueden solaparse.

</details>

**8. ¿Por qué accuracy es mala métrica única con clases desbalanceadas?**

- a) No admite porcentajes
- b) Puede ser alta prediciendo siempre la clase mayoritaria
- c) Solo sirve para regresión
- d) Exige datos personales

<details><summary>Ver respuesta</summary>

**Correcta: b) Puede ser alta prediciendo siempre la clase mayoritaria.** Precision, recall, F1 y PR deben leerse con prevalencia y costo de error.

</details>

**9. ¿Cuándo aporta ML frente a reglas deterministas?**

- a) Siempre
- b) Cuando generaliza patrones multivariados con evaluación, drift y explicación mejores que el baseline
- c) Cuando no hay labels ni objetivo
- d) Cuando se quiere ocultar el criterio

<details><summary>Ver respuesta</summary>

**Correcta: b) Cuando generaliza patrones multivariados con evaluación, drift y explicación mejores que el baseline.** ML debe superar un baseline simple y justificar complejidad, mantenimiento y gobernanza.

</details>

**10. ¿Qué principio limita telemetría anti-cheat a campos que cambian una decisión?**

- a) Data augmentation
- b) Minimización de datos
- c) Client prediction
- d) Delayed ban

<details><summary>Ver respuesta</summary>

**Correcta: b) Minimización de datos.** La minimización reduce exposición y obliga a definir propósito, retención y acceso.

</details>

**11. ¿Qué diferencia causa raíz de señal?**

- a) La señal es el control definitivo
- b) La causa raíz es la condición sistémica que permitió recurrencia; la señal es una observación
- c) No hay diferencia
- d) La causa raíz siempre es el jugador

<details><summary>Ver respuesta</summary>

**Correcta: b) La causa raíz es la condición sistémica que permitió recurrencia; la señal es una observación.** Impossible fire rate puede ser señal; ausencia de validación autoritativa puede ser causa raíz.

</details>

**12. ¿Qué debe acompañar una sanción revisable?**

- a) Solo una puntuación del modelo
- b) Evidencia, versión del detector, política, auditabilidad y appeal
- c) El nombre del cheat
- d) Acceso kernel obligatorio

<details><summary>Ver respuesta</summary>

**Correcta: b) Evidencia, versión del detector, política, auditabilidad y appeal.** Las consecuencias requieren trazabilidad y una vía proporcional de revisión.

</details>

## Parte 20 — Debilidades y vulnerabilidades: CWE, CVE, CVSS y su gestión

**1. ¿Qué identifica un CVE y qué identifica un CWE?**

- a) CVE: un tipo de defecto; CWE: una ocurrencia concreta
- b) CVE: una ocurrencia concreta en un producto; CWE: un tipo de defecto
- c) Ambos identifican el tipo de defecto, uno en software y otro en hardware
- d) CVE: la severidad; CWE: la probabilidad de explotación

<details><summary>Ver respuesta</summary>

**Correcta: b) CVE: una ocurrencia concreta en un producto; CWE: un tipo de defecto.** El CVE nombra una vulnerabilidad concreta (producto y versiones afectadas); el CWE nombra la clase de debilidad de la que es ejemplo. Severidad y probabilidad son CVSS y EPSS.

</details>

**2. Bandit etiqueta una llamada a eval con CWE-78. ¿Qué CWE describe mejor el defecto?**

- a) La vista 1000, que es la raíz del catálogo
- b) CWE-78, porque eval ejecuta comandos del sistema operativo
- c) CWE-95, porque eval evalúa código a partir de entrada no confiable
- d) CWE-20, porque todo fallo es de validación

<details><summary>Ver respuesta</summary>

**Correcta: c) CWE-95, porque eval evalúa código a partir de entrada no confiable.** eval ejecuta código del propio lenguaje, no comandos del sistema operativo. Copiar la etiqueta de la herramienta clasifica con el CWE de otro defecto; el correcto sale de leer la ficha oficial (CWE-95).

</details>

**3. Para clasificar una inyección SQL concreta, ¿qué entrada del catálogo es la preferida?**

- a) Una agrupación (Grouping) de inyecciones
- b) CWE-707, un Pillar
- c) CWE-74, la clase abstracta de inyección
- d) CWE-89, de nivel Base, que describe la causa con la precisión adecuada

<details><summary>Ver respuesta</summary>

**Correcta: d) CWE-89, de nivel Base, que describe la causa con la precisión adecuada.** La guía de mapeo por causa raíz prefiere entradas de nivel Base o Variant. Las clases y los Pillar son demasiado generales y las agrupaciones no se usan para mapear.

</details>

**4. ¿Qué describe la cadena con nombre CWE-680?**

- a) Un XSS (CWE-79) seguido de un CSRF (CWE-352)
- b) Un uso después de liberar (CWE-416) seguido de una doble liberación (CWE-415)
- c) Un path traversal (CWE-22) seguido de una inyección de comandos (CWE-78)
- d) Un desbordamiento de enteros (CWE-190) que produce una escritura fuera de límites (CWE-787)

<details><summary>Ver respuesta</summary>

**Correcta: d) Un desbordamiento de enteros (CWE-190) que produce una escritura fuera de límites (CWE-787).** CWE-680 es la cadena «desbordamiento de enteros a desbordamiento de buffer». Se corrige en el eslabón raíz: el cálculo del tamaño.

</details>

**5. La comprobación «la ruta empieza por /var/data» no corrige CWE-22. ¿Por qué?**

- a) Python no permite comparar rutas como texto
- b) Un directorio hermano como /var/data-secretos empieza igual y los «..» no se normalizan con una comparación de texto
- c) El sistema operativo ignora los prefijos
- d) Solo afecta a Windows

<details><summary>Ver respuesta</summary>

**Correcta: b) Un directorio hermano como /var/data-secretos empieza igual y los «..» no se normalizan con una comparación de texto.** La defensa correcta resuelve la ruta canónica y comprueba que queda dentro del directorio permitido; la prueba debe incluir el directorio hermano y las rutas absolutas.

</details>

**6. ¿Qué distingue a CWE-862 de CWE-863?**

- a) 862 afecta a memoria y 863 a red
- b) 862: no existe comprobación de autorización; 863: existe pero es incorrecta
- c) 862 es de autenticación y 863 de autorización
- d) Son sinónimos

<details><summary>Ver respuesta</summary>

**Correcta: b) 862: no existe comprobación de autorización; 863: existe pero es incorrecta.** Missing Authorization frente a Incorrect Authorization. Para ambas se prueba la política completa con una matriz de usuarios y recursos.

</details>

**7. Un código guarda contraseñas con MD5 sin sal. ¿Qué CWE es más específico que CWE-327?**

- a) CWE-259, contraseña embebida
- b) CWE-20, validación de entrada
- c) CWE-916, uso de un hash de contraseña con esfuerzo computacional insuficiente
- d) CWE-798, credenciales embebidas

<details><summary>Ver respuesta</summary>

**Correcta: c) CWE-916, uso de un hash de contraseña con esfuerzo computacional insuficiente.** CWE-327 es una clase general sobre algoritmos arriesgados; CWE-916 nombra la causa concreta. Se corrige con un algoritmo de coste ajustable y sal (scrypt, Argon2, bcrypt).

</details>

**8. NVD puntúa un CVE con 9,8 y CISA-ADP con 7,5. ¿Cómo se interpreta?**

- a) Cada fuente asumió supuestos distintos: se conserva la fuente de cada cifra y se valida la puntuación contra su vector
- b) Se promedian: 8,65
- c) La de NVD prevalece siempre
- d) Una de las dos se equivoca necesariamente

<details><summary>Ver respuesta</summary>

**Correcta: a) Cada fuente asumió supuestos distintos: se conserva la fuente de cada cifra y se valida la puntuación contra su vector.** Las discrepancias suelen venir de supuestos sobre privilegios, alcance o configuración. Lo que sí es un error mecánico es una puntuación que no coincide con su propio vector.

</details>

**9. ¿Qué mide la puntuación base de CVSS?**

- a) La probabilidad de explotación en 30 días
- b) La severidad intrínseca bajo los supuestos del evaluador, no el riesgo
- c) Si el CVE está en KEV
- d) El valor del activo afectado

<details><summary>Ver respuesta</summary>

**Correcta: b) La severidad intrínseca bajo los supuestos del evaluador, no el riesgo.** Las métricas ambientales y de amenaza existen para contextualizar. Sin ellas, CVSS-B no conoce tu entorno ni la explotación.

</details>

**10. ¿Qué expresa una puntuación EPSS?**

- a) Que existe un parche disponible
- b) Que la vulnerabilidad se explotará con certeza
- c) Una probabilidad estimada de que se observe explotación en los próximos 30 días, recalculada a diario
- d) El daño máximo posible

<details><summary>Ver respuesta</summary>

**Correcta: c) Una probabilidad estimada de que se observe explotación en los próximos 30 días, recalculada a diario.** EPSS es un pronóstico de la amenaza. No incorpora el daño ni el entorno, y no existe un umbral universal.

</details>

**11. ¿Cuál de estos hechos no cumple por sí solo el criterio de explotación para entrar en KEV?**

- a) Un exploit público de prueba de concepto sin uso hostil observado
- b) Un identificador CVE
- c) Evidencia fiable de explotación activa
- d) Una acción de corrección clara

<details><summary>Ver respuesta</summary>

**Correcta: a) Un exploit público de prueba de concepto sin uso hostil observado.** KEV exige identificador, evidencia fiable de explotación activa y una vía de corrección. Los escaneos, la investigación y las pruebas de concepto no cuentan como explotación.

</details>

**12. Con los 14 casos de la clase 369, ¿qué ocurre al corregir solo lo que tiene CVSS ≥ 9,0?**

- a) Se dejan fuera cuatro CVE de KEV (como Heartbleed, 7,5) y se incluyen tres sin evidencia de explotación
- b) Es la política oficial de CISA
- c) Equivale a usar EPSS ≥ 0,10
- d) Se cubren todos los CVE de KEV

<details><summary>Ver respuesta</summary>

**Correcta: a) Se dejan fuera cuatro CVE de KEV (como Heartbleed, 7,5) y se incluyen tres sin evidencia de explotación.** Nueve casos pasan el corte: seis están en KEV y tres no; y cuatro casos de KEV quedan por debajo. La severidad no ordena por explotación.

</details>

**13. Según BOD 26-04 (usada como referencia), el mismo CVE de KEV, no automatizable y con impacto total, ¿qué plazo tiene?**

- a) El mismo en cualquier activo
- b) Más corto si el activo está expuesto que si es interno
- c) Más largo si está expuesto
- d) No depende de KEV

<details><summary>Ver respuesta</summary>

**Correcta: b) Más corto si el activo está expuesto que si es interno.** La exposición es una de las cuatro variables de la tabla: en el caso de libwebp el plazo pasa de 3 días y triaje forense (expuesto) a 14 días (interno).

</details>

**14. En el Top 25 de 2025, CWE-79 es la nº 1 y CWE-78 la nº 9. ¿Qué enseña su número de CVE en KEV (7 y 20)?**

- a) Que el Top 25 solo cuenta CVE de KEV
- b) Que la frecuencia de una debilidad equivale a su nivel de explotación
- c) Que una debilidad menos frecuente puede explotarse más, así que el puesto no sustituye a KEV ni a EPSS
- d) Que CWE-79 no tiene corrección

<details><summary>Ver respuesta</summary>

**Correcta: c) Que una debilidad menos frecuente puede explotarse más, así que el puesto no sustituye a KEV ni a EPSS.** El Top 25 puntúa por frecuencia y severidad; el recuento de KEV muestra la explotación observada. Son señales distintas.

</details>

**15. ¿Qué convierte una corrección en una corrección verificada?**

- a) Que la herramienta SAST deje de avisar
- b) Que el equipo la apruebe en una reunión
- c) Haber instalado la versión parcheada
- d) Una prueba de ataque que funciona contra el original y falla contra el corregido, más casos legítimos y de borde

<details><summary>Ver respuesta</summary>

**Correcta: d) Una prueba de ataque que funciona contra el original y falla contra el corregido, más casos legítimos y de borde.** Sin una prueba que falle antes y pase después es un parche asumido. Y conviene repetirla tras el parche: hay correcciones incompletas, como la que siguió a CVE-2021-41773.

</details>

**16. Un servicio descarga la URL que le indica el usuario (CWE-918). ¿Qué defensa cierra el caso de un nombre permitido cuyo DNS apunta a 127.0.0.1?**

- a) Resolver el nombre, exigir que todas las direcciones sean públicas y conectar a la dirección ya validada
- b) Comprobar solo que el esquema sea http o https
- c) Convertir la URL a minúsculas
- d) Bloquear la cadena «127.0.0.1» en el texto de la URL

<details><summary>Ver respuesta</summary>

**Correcta: a) Resolver el nombre, exigir que todas las direcciones sean públicas y conectar a la dirección ya validada.** Hay que validar el destino final, no el texto: lista de nombres permitidos, todas las direcciones públicas y conexión a la dirección comprobada para que un DNS cambiante no sirva. Cada salto de una redirección se valida igual.

</details>

**17. ¿Por qué validar solo la extensión de un archivo subido no corrige CWE-434?**

- a) La extensión la elige el cliente y no demuestra qué contiene el archivo: hay que validar el contenido, limitar el tamaño y guardar con un nombre generado por el servidor
- b) Porque las extensiones no existen en Linux
- c) Porque CWE-434 solo ocurre con archivos PDF
- d) Porque el tamaño del archivo no importa

<details><summary>Ver respuesta</summary>

**Correcta: a) La extensión la elige el cliente y no demuestra qué contiene el archivo: hay que validar el contenido, limitar el tamaño y guardar con un nombre generado por el servidor.** La defensa es en capas: lista de extensiones, firma del contenido, tamaño máximo, nombre generado y almacenamiento sin ejecución. En la clase 363 la subida cae en A06 Insecure Design: es también un problema de diseño.

</details>

**18. ¿Qué diferencia hay entre CWE-78 y CWE-94?**

- a) CWE-78 solo afecta a las bases de datos
- b) CWE-78 inyecta comandos del sistema operativo; CWE-94 inyecta código del propio lenguaje o de una plantilla
- c) Son idénticas
- d) CWE-94 es una categoría de OWASP

<details><summary>Ver respuesta</summary>

**Correcta: b) CWE-78 inyecta comandos del sistema operativo; CWE-94 inyecta código del propio lenguaje o de una plantilla.** Ambas son inyección (cuelgan de CWE-74; CWE-78 lo hace a través de CWE-77, la inyección de comandos en general). La corrección cambia: argumentos como lista y sin shell para CWE-78, y no evaluar entrada ni construir plantillas con ella para CWE-94.

</details>

**19. Un panel de administración responde sin pedir autenticación. ¿Qué entrada describe el defecto y qué dato de 2025 la hace prioritaria?**

- a) CWE-79, con 7 CVE en KEV
- b) CWE-20, una clase desaconsejada para mapear
- c) CWE-306, que figura en el Top 25 de 2025 con 11 CVE en KEV
- d) CWE-352, con 0 CVE en KEV

<details><summary>Ver respuesta</summary>

**Correcta: c) CWE-306, que figura en el Top 25 de 2025 con 11 CVE en KEV.** CWE-306 (falta de autenticación en una función crítica) es una de las debilidades con más presencia en KEV. Su hija CWE-288 (autenticación evitada por una ruta alternativa) también está en el Top 10 de debilidades de KEV.

</details>

**20. Heartbleed (CVE-2014-0160) está clasificado como CWE-125. ¿Qué tipo de defecto es?**

- a) Una escritura fuera de límites que ejecuta código
- b) Una inyección SQL
- c) Un desbordamiento de enteros
- d) Una lectura fuera de límites que filtra memoria

<details><summary>Ver respuesta</summary>

**Correcta: d) Una lectura fuera de límites que filtra memoria.** CWE-125 es la lectura fuera de límites: afecta sobre todo a la confidencialidad (su CVSS 3.1 es 7,5 con impacto alto solo en confidencialidad) y, aun así, está en KEV con EPSS cercano a 1.

</details>

**21. ¿Qué distingue CWE-120, CWE-121 y CWE-122?**

- a) CWE-120 describe la causa (copiar sin comprobar el tamaño) y CWE-121 y CWE-122 indican dónde ocurre (pila y montón); las tres cuelgan de la escritura fuera de límites CWE-787
- b) Son tres nombres del mismo CVE
- c) CWE-121 y CWE-122 son categorías de OWASP
- d) CWE-120 es un defecto de red

<details><summary>Ver respuesta</summary>

**Correcta: a) CWE-120 describe la causa (copiar sin comprobar el tamaño) y CWE-121 y CWE-122 indican dónde ocurre (pila y montón); las tres cuelgan de la escritura fuera de límites CWE-787.** Las protecciones del sistema (canario, ASLR, DEP) reducen la explotabilidad pero no eliminan la debilidad: la corrección es comprobar el límite.

</details>

**22. ¿Por qué MITRE desaconseja usar CWE-20 (validación de entrada incorrecta) para mapear una vulnerabilidad?**

- a) Porque OWASP la prohíbe
- b) Es una clase tan general que casi cualquier debilidad podría describirse así; se prefieren entradas de nivel Base o Variant que describan la causa concreta
- c) Porque está obsoleta
- d) Porque solo existe en C

<details><summary>Ver respuesta</summary>

**Correcta: b) Es una clase tan general que casi cualquier debilidad podría describirse así; se prefieren entradas de nivel Base o Variant que describan la causa concreta.** La validación es un complemento, no la corrección en el punto de uso (la consulta parametrizada, la codificación de salida). Que CWE-20 aparezca en el Top 25 no la convierte en una buena etiqueta.

</details>

**23. Un CVE tiene EPSS 0,03 y percentil 0,90. ¿Cómo se lee?**

- a) Está en el catálogo KEV
- b) Su CVSS es 3
- c) Se espera que se explote 3 de cada 100 CVE como este en 30 días, y su probabilidad es mayor que la del 90 % de los CVE puntuados
- d) Hay un 90 % de probabilidad de que se explote

<details><summary>Ver respuesta</summary>

**Correcta: c) Se espera que se explote 3 de cada 100 CVE como este en 30 días, y su probabilidad es mayor que la del 90 % de los CVE puntuados.** La probabilidad estima la amenaza y el percentil ordena. No hay un umbral universal: el 0,10 que se usa a menudo no tiene autoridad especial.

</details>

**24. Un token JWT se acepta con la cabecera alg:none o con otro algoritmo que elige el cliente. ¿Qué entrada del catálogo describe el defecto?**

- a) CWE-89
- b) CWE-434
- c) CWE-79
- d) CWE-347, verificación incorrecta de una firma criptográfica

<details><summary>Ver respuesta</summary>

**Correcta: d) CWE-347, verificación incorrecta de una firma criptográfica.** CWE-347 cuelga de CWE-345, una clase desaconsejada para mapear. La corrección es verificar siempre con el algoritmo y la clave que fija el servidor.

</details>

**25. ¿En qué categoría de OWASP Top 10:2025 está ahora la falsificación de peticiones del lado del servidor (CWE-918)?**

- a) A01 Broken Access Control
- b) A10 Server-Side Request Forgery
- c) A05 Injection
- d) A03 Software Supply Chain Failures

<details><summary>Ver respuesta</summary>

**Correcta: a) A01 Broken Access Control.** En 2021 era la categoría propia A10; en 2025 se integró en A01. La A10 de 2025 es ahora Mishandling of Exceptional Conditions.

</details>

**26. Un CVE tiene registro publicado el 23 de septiembre y entra a KEV el 20 de octubre. ¿Qué afirmación es correcta?**

- a) Fue descubierto el 20 de octubre
- b) La entrada a KEV marca la incorporación al catálogo, no la primera explotación ni el descubrimiento; esa fecha puede ser desconocida
- c) KEV registra siempre la fecha de la primera explotación
- d) El identificador contiene el año de publicación

<details><summary>Ver respuesta</summary>

**Correcta: b) La entrada a KEV marca la incorporación al catálogo, no la primera explotación ni el descubrimiento; esa fecha puede ser desconocida.** KEV publica `dateAdded`. El año del identificador es el de reserva. La fecha de explotación solo la dan, a veces, las descripciones del fabricante.

</details>

**27. Un CVE de VMware ESX con CVSS 3,1 de 2,7 y EPSS de 0,7 % figura en KEV. ¿Cómo debe tratarlo quien prioriza?**

- a) Ignorarlo, por su severidad
- b) KEV prevalece: hay explotación confirmada; se decide el plazo según exposición y SSVC, y se valora su papel en la cadena (borrar el rastro)
- c) Esperar a que EPSS suba
- d) Tratarlo como crítico solo por estar en KEV, sin mirar nada más

<details><summary>Ver respuesta</summary>

**Correcta: b) KEV prevalece: hay explotación confirmada; se decide el plazo según exposición y SSVC, y se valora su papel en la cadena (borrar el rastro).** La severidad aislada subestima un control que permite operar sin registro. EPSS es un pronóstico y KEV es evidencia; cuando existe evidencia manda.

</details>

**28. Dos CVE de memoria aparecen en KEV la misma semana: uno en PHP y otro en el kernel de Linux. ¿Se puede afirmar que forman una cadena?**

- a) Sí, por coincidir en el tiempo
- b) No: los registros no los vinculan; viven en capas distintas y compartir semana de KEV no es compartir causa
- c) Sí, porque PHP corre sobre Linux
- d) Depende de su CVSS

<details><summary>Ver respuesta</summary>

**Correcta: b) No: los registros no los vinculan; viven en capas distintas y compartir semana de KEV no es compartir causa.** Una cadena es una hipótesis que exige una fuente que la sostenga. Sin ella se estudian por separado, y se declara la incertidumbre.

</details>
