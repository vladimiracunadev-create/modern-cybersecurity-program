# ðŸ“ Autoevaluaciones

BaterÃ­a de preguntas por parte para comprobar lo aprendido. Esta es la versiÃ³n de lectura (con respuestas plegadas). Para la versiÃ³n **interactiva** con puntuaciÃ³n, abre [`quiz.html`](quiz.html) desde el [sitio del curso](https://vladimiracunadev-create.github.io/modern-cybersecurity-program/autoevaluaciones/quiz.html).

> ðŸ§­ Â¿No sabes por dÃ³nde empezar? Mira las [rutas por rol](../rutas/README.md).

<a id="progreso"></a>

## Seguimiento de progreso

Lleva la cuenta de todas las clases del programa en [`progreso.html`](progreso.html) (se guarda en tu navegador).

---

## Parte 0 â€” Fundamentos y prerrequisitos

**1. Â¿QuÃ© representa la 'I' de la trÃ­ada CIA?**

- a) Identidad
- b) Integridad
- c) Interoperabilidad
- d) Infraestructura

<details><summary>Ver respuesta</summary>

**Correcta: b) Integridad.** CIA = Confidencialidad, Integridad, Disponibilidad (Availability).

</details>

**2. Â¿En quÃ© capa del modelo OSI opera TCP?**

- a) Enlace de datos
- b) Red
- c) Transporte
- d) AplicaciÃ³n

<details><summary>Ver respuesta</summary>

**Correcta: c) Transporte.** TCP y UDP son protocolos de la capa 4 (Transporte).

</details>

**3. Â¿CuÃ¡l es la principal diferencia entre codificar (Base64) y cifrar?**

- a) Ninguna, son sinÃ³nimos
- b) Codificar requiere clave; cifrar no
- c) Cifrar aporta confidencialidad con una clave; codificar es reversible sin clave
- d) Base64 es mÃ¡s seguro que AES

<details><summary>Ver respuesta</summary>

**Correcta: c) Cifrar aporta confidencialidad con una clave; codificar es reversible sin clave.** Base64/hex/ROT no protegen: se revierten sin clave. Cifrar exige una clave secreta.

</details>

**4. El principio de 'mÃ­nimo privilegio' consiste enâ€¦**

- a) Dar a cada entidad solo los permisos que necesita
- b) Usar contraseÃ±as cortas
- c) Deshabilitar todos los logs
- d) Compartir credenciales de admin

<details><summary>Ver respuesta</summary>

**Correcta: a) Dar a cada entidad solo los permisos que necesita.** Menos privilegios = menor superficie de ataque e impacto ante un compromiso.

</details>

**5. Â¿QuÃ© comando/entorno es el adecuado para practicar tÃ©cnicas ofensivas?**

- a) La red corporativa de producciÃ³n
- b) Un laboratorio aislado y propio (VMs/red aislada)
- c) Cualquier servidor de Internet
- d) El wifi del vecino

<details><summary>Ver respuesta</summary>

**Correcta: b) Un laboratorio aislado y propio (VMs/red aislada).** Solo en entornos propios o con autorizaciÃ³n explÃ­cita: lo contrario es delito.

</details>

## Parte 1 â€” Redes y seguridad de redes

**1. Â¿QuÃ© hace `nmap -sS`?**

- a) Escaneo UDP
- b) Escaneo SYN (half-open)
- c) DetecciÃ³n de versiÃ³n
- d) Escaneo de vulnerabilidades

<details><summary>Ver respuesta</summary>

**Correcta: b) Escaneo SYN (half-open).** -sS es el SYN scan: envÃ­a SYN y no completa el handshake.

</details>

**2. El ARP spoofing permite principalmenteâ€¦**

- a) Cifrar el trÃ¡fico
- b) Interceptar trÃ¡fico de la LAN (MitM)
- c) Acelerar la red
- d) Bloquear DNS

<details><summary>Ver respuesta</summary>

**Correcta: b) Interceptar trÃ¡fico de la LAN (MitM).** Envenena la cachÃ© ARP para situarse en medio del trÃ¡fico de capa 2.

</details>

**3. Diferencia entre IDS e IPS:**

- a) El IDS bloquea; el IPS solo alerta
- b) El IDS detecta/alerta; el IPS ademÃ¡s puede bloquear en lÃ­nea
- c) Son idÃ©nticos
- d) El IPS solo funciona en la nube

<details><summary>Ver respuesta</summary>

**Correcta: b) El IDS detecta/alerta; el IPS ademÃ¡s puede bloquear en lÃ­nea.** IPS estÃ¡ en lÃ­nea y puede cortar el trÃ¡fico; el IDS observa y alerta.

</details>

**4. Â¿En quÃ© puerto opera DNS habitualmente?**

- a) 22
- b) 53
- c) 80
- d) 443

<details><summary>Ver respuesta</summary>

**Correcta: b) 53.** DNS usa el 53 (UDP y TCP). Su apertura casi universal habilita el tunneling.

</details>

**5. Un objetivo Windows suele no responder a escaneos FIN/NULL/Xmas porqueâ€¦**

- a) Tiene el firewall apagado
- b) No sigue estrictamente el RFC 793 en ese comportamiento
- c) Usa IPv6
- d) Nmap no soporta Windows

<details><summary>Ver respuesta</summary>

**Correcta: b) No sigue estrictamente el RFC 793 en ese comportamiento.** Esos escaneos dependen del comportamiento RFC 793 que Windows no implementa igual.

</details>

## Parte 2 â€” CriptografÃ­a aplicada

**1. Â¿CuÃ¡l es una propiedad esperada de una funciÃ³n hash criptogrÃ¡fica?**

- a) Ser reversible
- b) Resistencia a colisiones
- c) Requerir una clave
- d) Comprimir sin pÃ©rdida

<details><summary>Ver respuesta</summary>

**Correcta: b) Resistencia a colisiones.** Debe ser unidireccional y resistente a colisiones; no usa clave (a diferencia de HMAC).

</details>

**2. Â¿Por quÃ© el modo ECB es inseguro para datos con patrones?**

- a) Es muy lento
- b) Bloques de texto idÃ©nticos producen bloques cifrados idÃ©nticos
- c) No usa clave
- d) Solo cifra texto ASCII

<details><summary>Ver respuesta</summary>

**Correcta: b) Bloques de texto idÃ©nticos producen bloques cifrados idÃ©nticos.** ECB filtra patrones; usa modos con IV (CBC/CTR) o AEAD (GCM).

</details>

**3. Para almacenar contraseÃ±as, Â¿quÃ© es lo recomendado hoy?**

- a) MD5 sin sal
- b) SHA-1
- c) Argon2 / bcrypt / scrypt con sal
- d) Base64

<details><summary>Ver respuesta</summary>

**Correcta: c) Argon2 / bcrypt / scrypt con sal.** Funciones de derivaciÃ³n lentas y con sal frenan el crackeo masivo.

</details>

**4. En criptografÃ­a asimÃ©trica (RSA), lo que cifra con la clave pÃºblica se descifra conâ€¦**

- a) La misma clave pÃºblica
- b) La clave privada correspondiente
- c) Un hash
- d) Una sal

<details><summary>Ver respuesta</summary>

**Correcta: b) La clave privada correspondiente.** Par de claves: lo cifrado con la pÃºblica solo lo abre la privada.

</details>

**5. Â¿QuÃ© garantiza principalmente TLS en una conexiÃ³n HTTPS?**

- a) Solo velocidad
- b) Confidencialidad, integridad y autenticaciÃ³n del servidor
- c) Que el sitio no tenga bugs
- d) Anonimato total

<details><summary>Ver respuesta</summary>

**Correcta: b) Confidencialidad, integridad y autenticaciÃ³n del servidor.** TLS cifra el canal, verifica integridad y autentica al servidor vÃ­a certificado.

</details>

## Parte 3 â€” Hacking Ã©tico y pentesting: metodologÃ­a

**1. Â¿QuÃ© documento define el alcance y lo permitido en un pentest?**

- a) El reporte final
- b) Las reglas de engagement (RoE) / contrato
- c) El exploit
- d) El README

<details><summary>Ver respuesta</summary>

**Correcta: b) Las reglas de engagement (RoE) / contrato.** Las RoE fijan alcance, ventanas, lÃ­mites y autorizaciÃ³n por escrito.

</details>

**2. En la metodologÃ­a PTES, el reconocimiento vaâ€¦**

- a) Al final
- b) Antes de la explotaciÃ³n
- c) Nunca
- d) Solo en web

<details><summary>Ver respuesta</summary>

**Correcta: b) Antes de la explotaciÃ³n.** Recon y enumeraciÃ³n preceden a la explotaciÃ³n y post-explotaciÃ³n.

</details>

**3. Meterpreter se usa tÃ­picamente en la fase deâ€¦**

- a) Reconocimiento pasivo
- b) Post-explotaciÃ³n
- c) RedacciÃ³n del informe
- d) Escaneo de puertos

<details><summary>Ver respuesta</summary>

**Correcta: b) Post-explotaciÃ³n.** Es un payload de post-explotaciÃ³n de Metasploit.

</details>

**4. Â¿QuÃ© NO debe hacer un pentester Ã©tico durante un engagement?**

- a) Documentar hallazgos
- b) Respetar el alcance
- c) Borrar los logs para ocultar su actividad
- d) Reportar vulnerabilidades

<details><summary>Ver respuesta</summary>

**Correcta: c) Borrar los logs para ocultar su actividad.** El consultor preserva evidencia y trazabilidad; no destruye registros.

</details>

**5. Lo mÃ¡s importante del entregable final esâ€¦**

- a) La cantidad de comandos
- b) El resumen ejecutivo y hallazgos priorizados por riesgo
- c) El color del PDF
- d) El nÃºmero de pÃ¡ginas

<details><summary>Ver respuesta</summary>

**Correcta: b) El resumen ejecutivo y hallazgos priorizados por riesgo.** Debe permitir a negocio decidir y a los tÃ©cnicos remediar.

</details>

## Parte 4 â€” Seguridad de aplicaciones web

**1. La inyecciÃ³n SQL ocurre cuandoâ€¦**

- a) El servidor es lento
- b) La entrada del usuario se concatena sin parametrizar en la consulta
- c) Se usa HTTPS
- d) El sitio usa cookies

<details><summary>Ver respuesta</summary>

**Correcta: b) La entrada del usuario se concatena sin parametrizar en la consulta.** La defensa principal son las consultas parametrizadas (prepared statements).

</details>

**2. Â¿QuÃ© tipo de XSS persiste en el servidor y afecta a otros usuarios?**

- a) Reflejado
- b) Almacenado
- c) Basado en DOM
- d) Ninguno

<details><summary>Ver respuesta</summary>

**Correcta: b) Almacenado.** El XSS almacenado guarda el payload y se sirve a cada visitante.

</details>

**3. SSRF permite a un atacanteâ€¦**

- a) Cifrar la base de datos
- b) Hacer que el servidor haga peticiones a destinos internos
- c) Acelerar la app
- d) Cambiar el CSS

<details><summary>Ver respuesta</summary>

**Correcta: b) Hacer que el servidor haga peticiones a destinos internos.** Server-Side Request Forgery abusa del servidor como proxy hacia recursos internos.

</details>

**4. IDOR es un fallo deâ€¦**

- a) Cifrado
- b) Control de acceso (referencia directa a objetos sin autorizaciÃ³n)
- c) Rendimiento
- d) ConfiguraciÃ³n de DNS

<details><summary>Ver respuesta</summary>

**Correcta: b) Control de acceso (referencia directa a objetos sin autorizaciÃ³n).** Cambiar un identificador accede a datos de otro usuario por falta de verificaciÃ³n.

</details>

**5. La mejor defensa contra CSRF esâ€¦**

- a) Ocultar el formulario
- b) Tokens anti-CSRF y SameSite en cookies
- c) Usar GET para todo
- d) Deshabilitar JavaScript

<details><summary>Ver respuesta</summary>

**Correcta: b) Tokens anti-CSRF y SameSite en cookies.** Token por sesiÃ³n/peticiÃ³n y cookies SameSite frenan la peticiÃ³n forjada.

</details>

## Parte 5 â€” ExplotaciÃ³n de sistemas y binarios

**1. Un buffer overflow en el stack puede sobrescribirâ€¦**

- a) El BIOS
- b) La direcciÃ³n de retorno guardada
- c) El disco duro
- d) El DNS

<details><summary>Ver respuesta</summary>

**Correcta: b) La direcciÃ³n de retorno guardada.** Al desbordar, se pisa la saved return address y se desvÃ­a el flujo.

</details>

**2. Â¿QuÃ© protecciÃ³n aleatoriza las direcciones de memoria?**

- a) DEP/NX
- b) ASLR
- c) Stack canary
- d) PIE

<details><summary>Ver respuesta</summary>

**Correcta: b) ASLR.** ASLR randomiza el mapa de memoria; DEP/NX marca zonas no ejecutables.

</details>

**3. ROP (Return-Oriented Programming) sirve paraâ€¦**

- a) Compilar mÃ¡s rÃ¡pido
- b) Ejecutar cÃ³digo reutilizando 'gadgets' cuando NX impide shellcode
- c) Cifrar el binario
- d) Depurar sin GDB

<details><summary>Ver respuesta</summary>

**Correcta: b) Ejecutar cÃ³digo reutilizando 'gadgets' cuando NX impide shellcode.** Encadena gadgets que terminan en `ret` para eludir NX/DEP.

</details>

**4. Â¿QuÃ© herramienta es de ingenierÃ­a inversa?**

- a) Nmap
- b) Ghidra
- c) Wireshark
- d) Hydra

<details><summary>Ver respuesta</summary>

**Correcta: b) Ghidra.** Ghidra (y IDA/radare2) desensamblan y decompilan binarios.

</details>

**5. El fuzzing busca vulnerabilidadesâ€¦**

- a) Leyendo el manual
- b) Enviando entradas malformadas/aleatorias para provocar fallos
- c) Cifrando el binario
- d) Escaneando puertos

<details><summary>Ver respuesta</summary>

**Correcta: b) Enviando entradas malformadas/aleatorias para provocar fallos.** AFL++/libFuzzer mutan entradas para encontrar crashes explotables.

</details>

## Parte 6 â€” AnÃ¡lisis de malware

**1. El anÃ¡lisis estÃ¡tico se diferencia del dinÃ¡mico en queâ€¦**

- a) Ejecuta la muestra
- b) Examina la muestra SIN ejecutarla
- c) Requiere Internet
- d) Solo aplica a Linux

<details><summary>Ver respuesta</summary>

**Correcta: b) Examina la muestra SIN ejecutarla.** EstÃ¡tico = sin ejecutar (strings, PE, desensamblado); dinÃ¡mico = observar en ejecuciÃ³n.

</details>

**2. Â¿DÃ³nde se debe ejecutar malware para analizarlo?**

- a) En tu equipo principal
- b) En una VM aislada sin acceso a la red productiva
- c) En un servidor de producciÃ³n
- d) En el mÃ³vil

<details><summary>Ver respuesta</summary>

**Correcta: b) En una VM aislada sin acceso a la red productiva.** Sandbox/VM aislada con snapshots; nunca en equipos reales o con red abierta.

</details>

**3. Las reglas YARA sirven paraâ€¦**

- a) Cifrar malware
- b) Detectar/clasificar muestras por patrones
- c) Acelerar el disco
- d) Compilar exploits

<details><summary>Ver respuesta</summary>

**Correcta: b) Detectar/clasificar muestras por patrones.** YARA describe patrones (strings/bytes) para cazar familias de malware.

</details>

**4. El 'packing' de un binario buscaâ€¦**

- a) Reducir su tamaÃ±o y/o ofuscar su contenido
- b) Firmarlo digitalmente
- c) Documentarlo
- d) Traducirlo

<details><summary>Ver respuesta</summary>

**Correcta: a) Reducir su tamaÃ±o y/o ofuscar su contenido.** Comprime/cifra el cÃ³digo; hay que 'unpackear' para analizarlo.

</details>

**5. El trÃ¡fico C2 de un malware esâ€¦**

- a) Su interfaz grÃ¡fica
- b) El canal de comando y control con el atacante
- c) Un antivirus
- d) Un instalador

<details><summary>Ver respuesta</summary>

**Correcta: b) El canal de comando y control con el atacante.** Command & Control: recibe Ã³rdenes y exfiltra datos; su beaconing es detectable.

</details>

## Parte 7 â€” Red Team y operaciones ofensivas

**1. MITRE ATT&CK esâ€¦**

- a) Un antivirus
- b) Una base de conocimiento de tÃ¡cticas y tÃ©cnicas de adversarios
- c) Un lenguaje de programaciÃ³n
- d) Un firewall

<details><summary>Ver respuesta</summary>

**Correcta: b) Una base de conocimiento de tÃ¡cticas y tÃ©cnicas de adversarios.** Mapea el comportamiento del adversario; sirve para ofensiva y defensa.

</details>

**2. El Kerberoasting atacaâ€¦**

- a) Certificados TLS
- b) Cuentas de servicio pidiendo tickets TGS crackeables offline
- c) El BIOS
- d) El DNS

<details><summary>Ver respuesta</summary>

**Correcta: b) Cuentas de servicio pidiendo tickets TGS crackeables offline.** Solicita TGS de cuentas con SPN y crackea su hash fuera de lÃ­nea.

</details>

**3. Pass-the-Hash permite autenticarseâ€¦**

- a) Con la contraseÃ±a en claro
- b) Usando el hash NTLM sin conocer la contraseÃ±a
- c) Solo con biometrÃ­a
- d) Con un OTP

<details><summary>Ver respuesta</summary>

**Correcta: b) Usando el hash NTLM sin conocer la contraseÃ±a.** Reutiliza el hash como credencial para moverse lateralmente.

</details>

**4. BloodHound se usa paraâ€¦**

- a) Cifrar el dominio
- b) Graficar rutas de ataque en Active Directory
- c) Escanear puertos
- d) Analizar malware

<details><summary>Ver respuesta</summary>

**Correcta: b) Graficar rutas de ataque en Active Directory.** Modela relaciones AD y encuentra caminos hacia Domain Admins.

</details>

**5. Un Golden Ticket se forja con el hash deâ€¦**

- a) Administrator local
- b) La cuenta krbtgt
- c) El usuario invitado
- d) La cuenta SYSTEM

<details><summary>Ver respuesta</summary>

**Correcta: b) La cuenta krbtgt.** Con el hash de krbtgt se firman TGTs arbitrarios (control total del dominio).

</details>

## Parte 8 â€” Blue Team, detecciÃ³n y SOC

**1. Un SIEM sirve principalmente paraâ€¦**

- a) Cifrar discos
- b) Centralizar, correlacionar y alertar sobre logs/telemetrÃ­a
- c) Escanear puertos
- d) Compilar exploits

<details><summary>Ver respuesta</summary>

**Correcta: b) Centralizar, correlacionar y alertar sobre logs/telemetrÃ­a.** Agrega eventos de mÃºltiples fuentes y dispara detecciones.

</details>

**2. Sigma esâ€¦**

- a) Un SIEM propietario
- b) Un formato genÃ©rico de reglas de detecciÃ³n portable entre SIEMs
- c) Un malware
- d) Un protocolo de red

<details><summary>Ver respuesta</summary>

**Correcta: b) Un formato genÃ©rico de reglas de detecciÃ³n portable entre SIEMs.** Describe detecciones en YAML y se traduce a la query de cada SIEM.

</details>

**3. El 'threat hunting' esâ€¦**

- a) Esperar alertas pasivamente
- b) Buscar proactivamente amenazas no detectadas por las alertas
- c) Apagar el SIEM
- d) Instalar parches

<details><summary>Ver respuesta</summary>

**Correcta: b) Buscar proactivamente amenazas no detectadas por las alertas.** HipÃ³tesis + datos para hallar lo que las reglas no marcaron.

</details>

**4. Un exceso de falsos positivos en detecciÃ³n provocaâ€¦**

- a) Mejor seguridad siempre
- b) Fatiga de alertas y riesgo de ignorar lo importante
- c) Menos logs
- d) MÃ¡s CPU en el atacante

<details><summary>Ver respuesta</summary>

**Correcta: b) Fatiga de alertas y riesgo de ignorar lo importante.** Hay que afinar reglas para no saturar al analista.

</details>

**5. El Event ID 1102 de Windows indicaâ€¦**

- a) Inicio de sesiÃ³n correcto
- b) Que se limpiÃ³ el registro de auditorÃ­a (Security log)
- c) ActualizaciÃ³n del sistema
- d) Cambio de contraseÃ±a

<details><summary>Ver respuesta</summary>

**Correcta: b) Que se limpiÃ³ el registro de auditorÃ­a (Security log).** Es una seÃ±al fuerte de anti-forense: borrado del log de seguridad.

</details>

## Parte 9 â€” Forense digital y respuesta a incidentes

**1. SegÃºn el orden de volatilidad, Â¿quÃ© se adquiere primero?**

- a) El disco duro
- b) La memoria RAM y el estado volÃ¡til
- c) Los backups
- d) El CD-ROM

<details><summary>Ver respuesta</summary>

**Correcta: b) La memoria RAM y el estado volÃ¡til.** Lo mÃ¡s volÃ¡til (RAM, conexiones) se captura antes de apagar.

</details>

**2. La cadena de custodia garantizaâ€¦**

- a) Que la evidencia se pueda alterar
- b) La trazabilidad e integridad de la evidencia desde su recolecciÃ³n
- c) Mayor velocidad de anÃ¡lisis
- d) Cifrado del disco

<details><summary>Ver respuesta</summary>

**Correcta: b) La trazabilidad e integridad de la evidencia desde su recolecciÃ³n.** Documenta quiÃ©n, cuÃ¡ndo y cÃ³mo manipulÃ³ la evidencia (validez legal).

</details>

**3. Volatility es una herramienta deâ€¦**

- a) Escaneo de red
- b) AnÃ¡lisis forense de memoria RAM
- c) Cracking de contraseÃ±as
- d) Fuzzing

<details><summary>Ver respuesta</summary>

**Correcta: b) AnÃ¡lisis forense de memoria RAM.** Analiza volcados de memoria para procesos, conexiones, inyecciones, etc.

</details>

**4. El ciclo de respuesta a incidentes (NIST/SANS) incluye, entre otras, las fases deâ€¦**

- a) CompilaciÃ³n y linkeo
- b) PreparaciÃ³n, detecciÃ³n, contenciÃ³n, erradicaciÃ³n y recuperaciÃ³n
- c) Escaneo y explotaciÃ³n
- d) DiseÃ±o y despliegue

<details><summary>Ver respuesta</summary>

**Correcta: b) PreparaciÃ³n, detecciÃ³n, contenciÃ³n, erradicaciÃ³n y recuperaciÃ³n.** Es el flujo estÃ¡ndar de IR, mÃ¡s lecciones aprendidas.

</details>

**5. El 'timestomping' consiste enâ€¦**

- a) Sincronizar relojes
- b) Manipular las marcas de tiempo de archivos para despistar
- c) Acelerar el disco
- d) Cifrar timestamps

<details><summary>Ver respuesta</summary>

**Correcta: b) Manipular las marcas de tiempo de archivos para despistar.** Se detecta comparando $STANDARD_INFORMATION vs $FILE_NAME en NTFS.

</details>

## Parte 10 â€” Seguridad en la nube y contenedores

**1. El modelo de responsabilidad compartida dice queâ€¦**

- a) El proveedor es responsable de todo
- b) El cliente es responsable de todo
- c) El proveedor asegura la nube y el cliente la seguridad EN la nube
- d) Nadie es responsable

<details><summary>Ver respuesta</summary>

**Correcta: c) El proveedor asegura la nube y el cliente la seguridad EN la nube.** El reparto varÃ­a segÃºn IaaS/PaaS/SaaS, pero el cliente siempre configura su parte.

</details>

**2. Una causa muy comÃºn de brechas en la nube esâ€¦**

- a) Cifrado fuerte
- b) Configuraciones errÃ³neas (p. ej. buckets pÃºblicos, IAM laxo)
- c) Usar MFA
- d) Rotar claves

<details><summary>Ver respuesta</summary>

**Correcta: b) Configuraciones errÃ³neas (p. ej. buckets pÃºblicos, IAM laxo).** El misconfiguration domina los incidentes cloud.

</details>

**3. En Kubernetes, RBAC controlaâ€¦**

- a) El ancho de banda
- b) QuiÃ©n puede hacer quÃ© sobre los recursos del clÃºster
- c) El cifrado de disco
- d) La CPU de los pods

<details><summary>Ver respuesta</summary>

**Correcta: b) QuiÃ©n puede hacer quÃ© sobre los recursos del clÃºster.** Role-Based Access Control define permisos por sujeto y recurso.

</details>

**4. Un 'container escape' esâ€¦**

- a) Reiniciar el contenedor
- b) Salir del aislamiento del contenedor hacia el host
- c) Borrar una imagen
- d) Exportar logs

<details><summary>Ver respuesta</summary>

**Correcta: b) Salir del aislamiento del contenedor hacia el host.** Abusa de configuraciones (privileged, mounts) para llegar al host.

</details>

**5. Para IAM en la nube, la buena prÃ¡ctica esâ€¦**

- a) Usar siempre la cuenta root
- b) Permisos amplios por comodidad
- c) MÃ­nimo privilegio y roles temporales
- d) Claves compartidas por equipo

<details><summary>Ver respuesta</summary>

**Correcta: c) MÃ­nimo privilegio y roles temporales.** Menos privilegio + credenciales efÃ­meras reducen el impacto.

</details>

## Parte 11 â€” DevSecOps y seguridad del SDLC

**1. 'Shift-left' significaâ€¦**

- a) Mover la seguridad al final
- b) Integrar la seguridad temprano en el ciclo de desarrollo
- c) Eliminar las pruebas
- d) Desplegar sin revisar

<details><summary>Ver respuesta</summary>

**Correcta: b) Integrar la seguridad temprano en el ciclo de desarrollo.** Detectar y corregir antes = mÃ¡s barato y seguro.

</details>

**2. SAST vs DAST:**

- a) SAST prueba en ejecuciÃ³n; DAST lee el cÃ³digo
- b) SAST analiza el cÃ³digo fuente; DAST prueba la app en ejecuciÃ³n
- c) Son lo mismo
- d) Ambos requieren producciÃ³n

<details><summary>Ver respuesta</summary>

**Correcta: b) SAST analiza el cÃ³digo fuente; DAST prueba la app en ejecuciÃ³n.** SAST = estÃ¡tico (cÃ³digo); DAST = dinÃ¡mico (app corriendo).

</details>

**3. SCA (Software Composition Analysis) se enfoca enâ€¦**

- a) El estilo del cÃ³digo
- b) Vulnerabilidades en dependencias/terceros
- c) El diseÃ±o de la UI
- d) La velocidad de compilaciÃ³n

<details><summary>Ver respuesta</summary>

**Correcta: b) Vulnerabilidades en dependencias/terceros.** Clave contra ataques de cadena de suministro; complementa con SBOM.

</details>

**4. STRIDE es un mÃ©todo deâ€¦**

- a) Cifrado
- b) Modelado de amenazas
- c) Escaneo de puertos
- d) GestiÃ³n de logs

<details><summary>Ver respuesta</summary>

**Correcta: b) Modelado de amenazas.** Spoofing, Tampering, Repudiation, Info disclosure, DoS, Elevation.

</details>

**5. Los secretos (API keys, contraseÃ±as) en el cÃ³digo se debenâ€¦**

- a) Commitear al repo
- b) Gestionar en un vault/secret manager y escanear con pre-commit
- c) Poner en el README
- d) Enviar por chat

<details><summary>Ver respuesta</summary>

**Correcta: b) Gestionar en un vault/secret manager y escanear con pre-commit.** gitleaks/detect-secrets + gestores de secretos evitan filtraciones.

</details>

## Parte 12 â€” OSINT e ingenierÃ­a social

**1. OSINT esâ€¦**

- a) Hackear con exploits
- b) Inteligencia a partir de fuentes abiertas y pÃºblicas
- c) Un tipo de malware
- d) Un firewall

<details><summary>Ver respuesta</summary>

**Correcta: b) Inteligencia a partir de fuentes abiertas y pÃºblicas.** Open Source Intelligence: recolecciÃ³n y anÃ¡lisis de informaciÃ³n pÃºblica.

</details>

**2. Shodan es Ãºtil paraâ€¦**

- a) Editar fotos
- b) Buscar dispositivos y servicios expuestos en Internet
- c) Cifrar correos
- d) Compilar cÃ³digo

<details><summary>Ver respuesta</summary>

**Correcta: b) Buscar dispositivos y servicios expuestos en Internet.** Indexa banners de servicios expuestos (cÃ¡maras, ICS, servidores).

</details>

**3. El pretexting en ingenierÃ­a social esâ€¦**

- a) Un exploit de kernel
- b) Construir un escenario/identidad falsa creÃ­ble para manipular
- c) Un algoritmo de hash
- d) Un escaneo de red

<details><summary>Ver respuesta</summary>

**Correcta: b) Construir un escenario/identidad falsa creÃ­ble para manipular.** Base de vishing y muchos fraudes; explota la confianza.

</details>

**4. Los metadatos EXIF de una foto pueden revelarâ€¦**

- a) Nada relevante
- b) Coordenadas GPS, dispositivo y fecha
- c) La contraseÃ±a del autor
- d) El cÃ³digo fuente

<details><summary>Ver respuesta</summary>

**Correcta: b) Coordenadas GPS, dispositivo y fecha.** Antes de publicar conviene eliminarlos.

</details>

**5. La ingenierÃ­a social solo debe practicarseâ€¦**

- a) Contra cualquiera
- b) Con autorizaciÃ³n explÃ­cita y por escrito (engagement)
- c) En redes sociales ajenas
- d) Sin lÃ­mites

<details><summary>Ver respuesta</summary>

**Correcta: b) Con autorizaciÃ³n explÃ­cita y por escrito (engagement).** Sin permiso es fraude/acoso; en pentest va acotada en las RoE.

</details>

## Parte 13 â€” Seguridad mÃ³vil, IoT e inalÃ¡mbrica

**1. Un APK de Android se puede analizar estÃ¡ticamente conâ€¦**

- a) Volatility
- b) apktool / jadx / MobSF
- c) Hashcat
- d) Snort

<details><summary>Ver respuesta</summary>

**Correcta: b) apktool / jadx / MobSF.** Descompilan y revisan el manifest, permisos y cÃ³digo.

</details>

**2. Un ataque 'Evil Twin' de WiFi consiste enâ€¦**

- a) Clonar una tarjeta SIM
- b) Levantar un punto de acceso falso que imita a uno legÃ­timo
- c) Cifrar el router
- d) Bloquear el 5G

<details><summary>Ver respuesta</summary>

**Correcta: b) Levantar un punto de acceso falso que imita a uno legÃ­timo.** La vÃ­ctima se conecta al AP del atacante, que intercepta el trÃ¡fico.

</details>

**3. El anÃ¡lisis de firmware de un dispositivo IoT suele empezar porâ€¦**

- a) Pintar la carcasa
- b) Extraer y descomprimir la imagen del firmware para buscar binarios/credenciales
- c) Cambiar el color del LED
- d) Actualizar el reloj

<details><summary>Ver respuesta</summary>

**Correcta: b) Extraer y descomprimir la imagen del firmware para buscar binarios/credenciales.** binwalk y similares extraen sistemas de archivos y secretos embebidos.

</details>

**4. Interfaces de hardware como UART/JTAG sirven paraâ€¦**

- a) Cargar el mÃ³vil
- b) Acceder a consola/depuraciÃ³n del dispositivo
- c) Conectar a WiFi
- d) Enviar SMS

<details><summary>Ver respuesta</summary>

**Correcta: b) Acceder a consola/depuraciÃ³n del dispositivo.** Dan acceso de bajo nivel muy Ãºtil para el hacking de hardware.

</details>

**5. BLE (Bluetooth Low Energy) es relevante en seguridad porqueâ€¦**

- a) No existe
- b) Muchos dispositivos lo usan y puede tener emparejamiento/cifrado dÃ©bil
- c) Solo lo usan impresoras
- d) Es imposible de interceptar

<details><summary>Ver respuesta</summary>

**Correcta: b) Muchos dispositivos lo usan y puede tener emparejamiento/cifrado dÃ©bil.** Wearables/IoT lo usan; hay ataques de sniffing y suplantaciÃ³n.

</details>

## Parte 14 â€” GRC, riesgo y cumplimiento

**1. En tÃ©rminos simples, el riesgo se estima comoâ€¦**

- a) Solo el impacto
- b) Probabilidad Ã— impacto
- c) NÃºmero de servidores
- d) Cantidad de logs

<details><summary>Ver respuesta</summary>

**Correcta: b) Probabilidad Ã— impacto.** Se prioriza combinando la probabilidad de ocurrencia y su impacto.

</details>

**2. ISO/IEC 27001 defineâ€¦**

- a) Un lenguaje de programaciÃ³n
- b) Requisitos para un Sistema de GestiÃ³n de Seguridad de la InformaciÃ³n (SGSI)
- c) Un antivirus
- d) Un protocolo de red

<details><summary>Ver respuesta</summary>

**Correcta: b) Requisitos para un Sistema de GestiÃ³n de Seguridad de la InformaciÃ³n (SGSI).** Marco certificable de gestiÃ³n de la seguridad basado en riesgos.

</details>

**3. GDPR regula principalmenteâ€¦**

- a) El cifrado militar
- b) La protecciÃ³n de datos personales en la UE
- c) Los puertos TCP
- d) El diseÃ±o web

<details><summary>Ver respuesta</summary>

**Correcta: b) La protecciÃ³n de datos personales en la UE.** Derechos de los titulares y obligaciones de quien trata datos personales.

</details>

**4. Un plan de continuidad de negocio (BCP) buscaâ€¦**

- a) Vender mÃ¡s
- b) Mantener/recuperar las operaciones crÃ­ticas ante una disrupciÃ³n
- c) Instalar juegos
- d) Cifrar correos

<details><summary>Ver respuesta</summary>

**Correcta: b) Mantener/recuperar las operaciones crÃ­ticas ante una disrupciÃ³n.** El DRP es su componente tecnolÃ³gico de recuperaciÃ³n.

</details>

**5. Un control 'compensatorio' esâ€¦**

- a) Un control que elimina el activo
- b) Una medida alternativa cuando el control principal no es viable
- c) Un ataque
- d) Un tipo de malware

<details><summary>Ver respuesta</summary>

**Correcta: b) Una medida alternativa cuando el control principal no es viable.** Reduce el riesgo cuando no se puede aplicar el control ideal.

</details>

## Parte 15 â€” Seguridad de IA y machine learning

**1. La 'prompt injection' en una app con LLM consiste enâ€¦**

- a) Cifrar el prompt
- b) Introducir instrucciones que manipulan el comportamiento del modelo
- c) Acelerar la inferencia
- d) Entrenar mÃ¡s rÃ¡pido

<details><summary>Ver respuesta</summary>

**Correcta: b) Introducir instrucciones que manipulan el comportamiento del modelo.** Es el riesgo #1 del OWASP Top 10 para LLM; incluye inyecciÃ³n indirecta.

</details>

**2. El envenenamiento de datos (data poisoning) atacaâ€¦**

- a) La GPU
- b) Los datos de entrenamiento para sesgar/backdoorear el modelo
- c) El firewall
- d) El DNS

<details><summary>Ver respuesta</summary>

**Correcta: b) Los datos de entrenamiento para sesgar/backdoorear el modelo.** Datos maliciosos en el entrenamiento comprometen el modelo resultante.

</details>

**3. Un ejemplo adversarial esâ€¦**

- a) Un dataset limpio
- b) Una entrada perturbada sutilmente para engaÃ±ar al modelo
- c) Un modelo mÃ¡s grande
- d) Un optimizador

<details><summary>Ver respuesta</summary>

**Correcta: b) Una entrada perturbada sutilmente para engaÃ±ar al modelo.** PequeÃ±as perturbaciones causan clasificaciones errÃ³neas.

</details>

**4. OWASP mantiene un Top 10 especÃ­fico paraâ€¦**

- a) Impresoras
- b) Aplicaciones con LLM
- c) Routers
- d) Bases de datos

<details><summary>Ver respuesta</summary>

**Correcta: b) Aplicaciones con LLM.** Cataloga los riesgos tÃ­picos de apps que integran modelos de lenguaje.

</details>

**5. Al integrar un LLM con herramientas/agentes, un riesgo clave esâ€¦**

- a) Que responda rÃ¡pido
- b) Que una inyecciÃ³n logre ejecutar acciones no deseadas
- c) Que use poca RAM
- d) Que hable espaÃ±ol

<details><summary>Ver respuesta</summary>

**Correcta: b) Que una inyecciÃ³n logre ejecutar acciones no deseadas.** Hay que limitar permisos del agente y validar entradas/salidas.

</details>

## Parte 16 â€” Capstones y preparaciÃ³n de certificaciones

**1. La certificaciÃ³n OSCP es conocida porâ€¦**

- a) Ser 100% teÃ³rica
- b) Su examen prÃ¡ctico de 24h con mentalidad 'Try Harder'
- c) No tener examen
- d) Ser solo defensiva

<details><summary>Ver respuesta</summary>

**Correcta: b) Su examen prÃ¡ctico de 24h con mentalidad 'Try Harder'.** EvalÃºa explotaciÃ³n prÃ¡ctica en un laboratorio bajo tiempo.

</details>

**2. El CISSP se estructura enâ€¦**

- a) 3 laboratorios
- b) 8 dominios de conocimiento
- c) 1 examen prÃ¡ctico de pwn
- d) Solo criptografÃ­a

<details><summary>Ver respuesta</summary>

**Correcta: b) 8 dominios de conocimiento.** Cubre seguridad de forma amplia y gerencial (8 dominios).

</details>

**3. Un buen 'home lab' permanente sirve paraâ€¦**

- a) Nada Ãºtil
- b) Practicar de forma continua y segura sin depender de terceros
- c) Solo ver pelÃ­culas
- d) Minar cripto

<details><summary>Ver respuesta</summary>

**Correcta: b) Practicar de forma continua y segura sin depender de terceros.** Es la base del aprendizaje continuo y del portafolio.

</details>

**4. Para construir portafolio, es recomendableâ€¦**

- a) Copiar writeups ajenos
- b) Documentar tus propios labs, CTFs y proyectos
- c) No mostrar nada
- d) Solo listar cursos

<details><summary>Ver respuesta</summary>

**Correcta: b) Documentar tus propios labs, CTFs y proyectos.** Evidencia prÃ¡ctica > lista de certificados sin contexto.

</details>

**5. En ciberseguridad, el aprendizajeâ€¦**

- a) Termina con una cert
- b) Es continuo: el panorama de amenazas cambia constantemente
- c) No es necesario
- d) Solo importa la teorÃ­a

<details><summary>Ver respuesta</summary>

**Correcta: b) Es continuo: el panorama de amenazas cambia constantemente.** Comunidad, prÃ¡ctica y actualizaciÃ³n constante son parte del oficio.

</details>

## Parte 17 â€” ProfundizaciÃ³n para certificaciones

**1. En la clasificaciÃ³n de datos, Â¿quiÃ©n define el nivel de clasificaciÃ³n de un activo?**

- a) El custodio (custodian)
- b) El propietario del dato (data owner)
- c) Cualquier usuario
- d) El proveedor de nube

<details><summary>Ver respuesta</summary>

**Correcta: b) El propietario del dato (data owner).** El data owner clasifica y define requisitos; el custodio los implementa/mantiene.

</details>

**2. SegÃºn NIST SP 800-88, 'purge' frente a 'clear' implicaâ€¦**

- a) Lo mismo
- b) Un borrado mÃ¡s resistente a ataques de laboratorio (p. ej. criptoborrado)
- c) Solo borrar la papelera
- d) Cifrar el disco

<details><summary>Ver respuesta</summary>

**Correcta: b) Un borrado mÃ¡s resistente a ataques de laboratorio (p. ej. criptoborrado).** Clear resiste ataques simples; purge resiste incluso recuperaciÃ³n de laboratorio; destroy es fÃ­sico.

</details>

**3. En IAM, el patrÃ³n 'joiner-mover-leaver' se refiere aâ€¦**

- a) Un ataque de fuerza bruta
- b) El ciclo de vida de una identidad (alta, cambios, baja)
- c) Un tipo de MFA
- d) Un modelo de cifrado

<details><summary>Ver respuesta</summary>

**Correcta: b) El ciclo de vida de una identidad (alta, cambios, baja).** Gestiona aprovisionamiento, cambios de rol y desaprovisionamiento oportuno de accesos.

</details>

**4. SAML y OpenID Connect se usan paraâ€¦**

- a) Cifrar discos
- b) FederaciÃ³n de identidad y single sign-on (SSO)
- c) Escanear puertos
- d) Analizar malware

<details><summary>Ver respuesta</summary>

**Correcta: b) FederaciÃ³n de identidad y single sign-on (SSO).** SAML (XML) y OIDC (sobre OAuth2) permiten autenticaciÃ³n federada entre dominios.

</details>

**5. El modelo Bell-LaPadula se enfoca en proteger laâ€¦**

- a) Integridad
- b) Disponibilidad
- c) Confidencialidad (no leer arriba, no escribir abajo)
- d) Velocidad

<details><summary>Ver respuesta</summary>

**Correcta: c) Confidencialidad (no leer arriba, no escribir abajo).** Bell-LaPadula = confidencialidad; Biba y Clark-Wilson se enfocan en integridad.

</details>

**6. Para priorizar la remediaciÃ³n de vulnerabilidades, ademÃ¡s de CVSS conviene usarâ€¦**

- a) El orden alfabÃ©tico
- b) EPSS y la lista KEV de CISA (explotaciÃ³n real)
- c) El tamaÃ±o del archivo
- d) El color del reporte

<details><summary>Ver respuesta</summary>

**Correcta: b) EPSS y la lista KEV de CISA (explotaciÃ³n real).** CVSS mide severidad; EPSS estima probabilidad de exploit y KEV marca lo explotado activamente.

</details>

**7. En el anÃ¡lisis de un correo de phishing, SPF, DKIM y DMARC sirven paraâ€¦**

- a) Cifrar el cuerpo
- b) Autenticar el origen del correo y detectar suplantaciÃ³n
- c) Comprimir adjuntos
- d) Acelerar la entrega

<details><summary>Ver respuesta</summary>

**Correcta: b) Autenticar el origen del correo y detectar suplantaciÃ³n.** Validan que el remitente estÃ© autorizado y que el mensaje no fue alterado; DMARC define la polÃ­tica.

</details>

## Parte 18 â€” IA aplicada a la ciberseguridad

**1. Â¿CuÃ¡l es el mayor riesgo operativo al usar un LLM en seguridad?**

- a) Que sea lento
- b) Las alucinaciones (salidas falsas con aplomo) sin verificaciÃ³n
- c) Que use mucha RAM
- d) Que no tenga interfaz grÃ¡fica

<details><summary>Ver respuesta</summary>

**Correcta: b) Las alucinaciones (salidas falsas con aplomo) sin verificaciÃ³n.** Un LLM genera lo plausible, no lo cierto; hay que verificar toda salida.

</details>

**2. El Model Context Protocol (MCP) sirve paraâ€¦**

- a) Cifrar prompts
- b) Estandarizar cÃ³mo un agente de IA usa herramientas externas
- c) Entrenar modelos
- d) Escanear puertos

<details><summary>Ver respuesta</summary>

**Correcta: b) Estandarizar cÃ³mo un agente de IA usa herramientas externas.** MCP conecta clientes de IA con servidores que exponen tools/resources/prompts.

</details>

**3. En kali-mcp, las herramientas de Kali se ejecutanâ€¦**

- a) En tu host directamente
- b) Dentro de un contenedor Docker aislado
- c) En la nube de OpenAI
- d) En el navegador

<details><summary>Ver respuesta</summary>

**Correcta: b) Dentro de un contenedor Docker aislado.** kali-mcp aÃ­sla las herramientas en un contenedor; el agente habla con un gateway MCP.

</details>

**4. En un pentest asistido por IA, Â¿quiÃ©n decide y autoriza las acciones con impacto?**

- a) El agente de IA de forma autÃ³noma
- b) El humano (el agente propone, la persona aprueba)
- c) El servidor MCP
- d) Nadie, se automatiza todo

<details><summary>Ver respuesta</summary>

**Correcta: b) El humano (el agente propone, la persona aprueba).** Human-in-the-loop: la IA propone y acelera; la autorizaciÃ³n y responsabilidad son humanas.

</details>

**5. La 'prompt injection' contra tu propio agente de seguridad consiste enâ€¦**

- a) Un ataque de fuerza bruta
- b) Contenido malicioso en los datos que el agente procesa que intenta secuestrar sus instrucciones
- c) Un fallo de red
- d) Un cifrado dÃ©bil

<details><summary>Ver respuesta</summary>

**Correcta: b) Contenido malicioso en los datos que el agente procesa que intenta secuestrar sus instrucciones.** Datos no confiables (banners, webs) pueden manipular al agente; por eso mÃ­nimo privilegio y aislamiento.

</details>
