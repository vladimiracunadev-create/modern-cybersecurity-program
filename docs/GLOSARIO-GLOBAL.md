# 📚 Glosario global

Referencia alfabética generada desde los glosarios locales de las clases. Consolida
siglas y aliases sin borrar su contexto: cada término indica en qué clases aparece.
Los conceptos transversales y plataformas se completan con metadatos mantenidos por
el generador; la modalidad y disponibilidad pueden cambiar en sus sitios oficiales.

> **Archivo generado.** No lo edites a mano. Ejecuta
> `python scripts/generar_glosario_global.py` y valida con `--check`.

**Cobertura:** 2424 términos consolidados · 345 clases con glosario.

## Cómo usarlo

- Busca la sigla o el nombre completo: ambos apuntan a la misma entrada cuando son aliases.
- Abre las clases de procedencia para recuperar mecanismo, límites, laboratorio y referencias.
- Para elegir un entorno autorizado, consulta [Plataformas de práctica](PLATAFORMAS-DE-PRACTICA.md).
- Para documentar una resolución, usa la [plantilla de writeup](../templates/writeup-ctf.md).

## Índice alfabético

[0](#0) · [1](#1) · [2](#2) · [4](#4) · [5](#5) · [8](#8) · [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [Otros](#otros) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [X](#x) · [Y](#y) · [Z](#z)

## 0

### 0-day

Vulnerabilidad sin parche disponible

**Aparece en 1 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).

### 0-RTT

Datos en el primer mensaje; sin forward secrecy y con riesgo de replay

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

## 1

### 1-RTT

Handshake completo en una sola vuelta

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

## 2

### 2>&1

Fusiona stderr con stdout hacia el mismo destino

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

## 4

### 4-way handshake

Intercambio que confirma claves y deriva claves de sesión.

**Aparece en 2 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md), [Clase 272 — Ataques WiFi avanzados: Evil Twin y PMKID](../classes/parte-13-seguridad-movil-iot-e-inalambrica/272-ataques-wifi-avanzados-evil-twin-y-pmkid/README.md).

## 5

### 5-tupla

IP origen, IP destino, puerto origen, puerto destino y protocolo

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

## 8

### 802.1Q

Estándar de etiquetado de VLAN

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

## A

### A01 Broken Access Control

Acceder a lo que no corresponde; el nº1 de 2021

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### A02 Cryptographic Failures

Datos sensibles mal protegidos

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### A03 Injection

Datos interpretados como código; incluye XSS desde 2021

**Aparece en 2 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md), [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md).

### A04 Insecure Design

Fallo de diseño, no de implementación

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### A05 Security Misconfiguration

Inseguro por defecto o mal configurado

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### A06 Componentes vulnerables

Dependencias con fallos conocidos

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### A07 Fallos de autenticación

Identificación y gestión de sesión débiles

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### A08 Fallos de integridad

Software o datos sin verificar

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### A09 Fallos de registro

Falta de logging y monitorización

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### A10 SSRF

Server-Side Request Forgery; añadido por la comunidad

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### AAA

Autenticación, Autorización y Accounting; el modelo de gobierno del acceso

**Aparece en 2 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md), [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### AAD

Datos asociados: se autentican pero no se cifran

**Aparece en 1 clase(s):** [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### ABAC

Control de acceso basado en atributos

**Aparece en 1 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md).

### Abierto

Una aplicación acepta conexiones en ese puerto

**Aparece en 1 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### Abuso de cupones

Apilar o reutilizar descuentos excluyentes

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### Acceso no autorizado

Interacción con un sistema sin permiso, delito común

**Aparece en 1 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).

### Acceso remoto

Túnel de un usuario individual hacia la red de la organización

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### Access-Control-Allow-Origin

Cabecera que dice qué orígenes pueden leer la respuesta

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### Accessibility

API abusada para leer pantalla y simular toques

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### accesstoken

Token que dice qué puede hacer el cliente

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### Acción que cambia estado

Requisito: transferir, cambiar correo, borrar

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### Aceleración por GPU

Miles de millones de candidatos por segundo

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### ACK

Flag que confirma la recepción de datos hasta un número de secuencia.

**Aparece en 1 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md).

### ACK scan (-sA)

No determina apertura: mapea si hay firewall con estado

**Aparece en 1 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### ACL

Permisos granulares por usuario o grupo (`setfacl`/`getfacl`)

**Aparece en 2 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md), [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md).

### Activo

Información, capacidad o servicio cuyo daño importa al negocio o usuario.

**Aparece en 1 clase(s):** [Clase 237 — Modelado de amenazas: STRIDE y DREAD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/237-modelado-de-amenazas-stride-y-dread/README.md).

### Activo candidato

Recurso relacionado que aún requiere validar propiedad y vigencia.

**Aparece en 2 clase(s):** [Clase 251 — OSINT de empresas y dominios](../classes/parte-12-osint-e-ingenieria-social/251-osint-de-empresas-y-dominios/README.md), [Clase 254 — OSINT técnico: Shodan y Censys](../classes/parte-12-osint-e-ingenieria-social/254-osint-tecnico-shodan-y-censys/README.md).

### Activo de IA

Componente o resultado cuyo daño importa.

**Aparece en 1 clase(s):** [Clase 291 — Introducción a la seguridad de IA y ML](../classes/parte-15-seguridad-de-ia-y-machine-learning/291-introduccion-a-la-seguridad-de-ia-y-ml/README.md).

### Activos,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 341 — Introducción a Game Security y modelo de amenazas](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/341-introduccion-game-security-modelo-amenazas/README.md).

### Addresses,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 344 — Estado del juego, memoria y manipulación controlada](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/344-estado-juego-memoria-manipulacion-controlada/README.md).

### AddressSanitizer (ASan)

Detecta UAF y double free durante las pruebas

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### Administrador local

Nivel intermedio; puente hacia SYSTEM

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### Admisión

Decisión previa a ejecutar basada en identidad y política del artefacto.

**Aparece en 1 clase(s):** [Clase 243 — Imágenes y contenedores seguros en el pipeline](../classes/parte-11-devsecops-y-seguridad-del-sdlc/243-imagenes-y-contenedores-seguros-en-el-pipeline/README.md).

### Adversary emulation

Reproducción fiel del comportamiento de un actor real, basada en CTI

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### Adversary simulation

Uso de comportamientos adversariales genéricos, sin atarse a un actor

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### Advertencia de certificado

Aviso del navegador que, ignorado, reabre el MitM

**Aparece en 1 clase(s):** [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md).

### Advertising

Emisión BLE para descubrimiento y datos breves.

**Aparece en 1 clase(s):** [Clase 271 — Seguridad de Bluetooth y BLE](../classes/parte-13-seguridad-movil-iot-e-inalambrica/271-seguridad-de-bluetooth-y-ble/README.md).

### AEAD

Cifrado autenticado: confidencialidad **e** integridad juntas

**Aparece en 3 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md), [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md), [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### AES

Cifrado por bloques simétrico estándar, claves de 128/192/256 bits

**Aparece en 2 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md), [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md).

### AES-GCM

AEAD dominante; muy rápido con AES-NI

**Aparece en 1 clase(s):** [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### AES-NI

Instrucciones de CPU que implementan AES en hardware

**Aparece en 1 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md).

### Afiliado

Quien despliega el ransomware a cambio de un porcentaje

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Afinado (tuning)

Reducir el ruido para que las alertas sean investigables

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### AFINET

Familia de direcciones IPv4

**Aparece en 1 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### afl

Lista las funciones encontradas

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### AFL / AFL++

Fuzzer estándar guiado por cobertura

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### Aislamiento

VM dedicada con snapshots para ejecutar con seguridad

**Aparece en 1 clase(s):** [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md).

### Aislamiento de red

Host-only o interna, sin ruta a Internet real

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### AJAX Spider

Ejecuta JS con un navegador real para descubrir rutas de SPA

**Aparece en 1 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md).

### Alcance

Frontera organizativa, tecnológica y física del SGSI.

**Aparece en 2 clase(s):** [Clase 278 — ISO/IEC 27001 e implantación de un SGSI](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md), [Clase 281 — Cumplimiento: GDPR, HIPAA y PCI-DSS](../classes/parte-14-grc-riesgo-y-cumplimiento/281-cumplimiento-gdpr-hipaa-y-pci-dss/README.md).

### Alcance autorizado

Conjunto de sistemas y acciones permitidos por escrito

**Aparece en 1 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md).

### Alcance (scope)

Lista de sistemas y acciones permitidos; negación por defecto

**Aparece en 2 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md), [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### Aleatorización de puerto

Mitigación que amplió el espacio a adivinar del atacante

**Aparece en 1 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md).

### Alerta

Hallazgo del escáner, con nivel de riesgo

**Aparece en 1 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md).

### Alertas

Salida de los IDS/IPS

**Aparece en 1 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md).

### alg:none

Algoritmo "ninguno"; aceptarlo permite tokens sin firma

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### Algoritmo de Grover

Acelera búsqueda; reduce la simétrica a la mitad de bits

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### Algoritmo de Shor

Factoriza y resuelve logaritmos discretos; rompe RSA, DH y ECC

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### Alias

Repetir operaciones con nombres distintos para evadir límites

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### Alineación a 16 bytes

RSP alineado en el `call`; su ausencia crashea libc

**Aparece en 3 clase(s):** [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md), [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md), [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md).

### Allocator

Gestor que decide dónde colocar cada asignación

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### Allow-Credentials

Permite enviar cookies en la petición cross-origin

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### AllowedIPs

En WireGuard, destinos enrutados y orígenes aceptados por par

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### Allowlist

Lista de valores permitidos cuando hay que llamar a un programa

**Aparece en 2 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md), [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### Allowlist de campos

Definir qué campos entran y cuáles salen

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### Allowlist de clases

Restringir qué clases se pueden deserializar

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### Allowlist de destinos

Solo destinos permitidos; la defensa correcta

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### Almacenamiento append-only

Inmutable: no permite modificar ni borrar

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### Almacenamiento sin ejecución

Guardar donde el fichero no se pueda ejecutar

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### Alternativas acotadas

`strncpy`, `snprintf`, `fgets` reciben el tamaño

**Aparece en 1 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md).

### AlwaysInstallElevated

Política que instala MSI como SYSTEM

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### AMSI

Interfaz que inspecciona el script desofuscado

**Aparece en 2 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md), [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### Análisis de comportamiento

Entender el malware como sistema con ciclo de vida

**Aparece en 1 clase(s):** [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### Análisis de frecuencias

Romper una sustitución explotando la estadística del idioma

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### Análisis de JavaScript

Extraer endpoints y secretos del código cliente

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### Análisis de vulnerabilidades

Identificar debilidades sin explotarlas; amplitud

**Aparece en 1 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### Análisis dinámico

Ejecutar el binario y observar su comportamiento

**Aparece en 3 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md), [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md), [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### Análisis estático

Examinar el binario sin ejecutarlo

**Aparece en 3 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md), [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md), [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md).

### Análisis estático avanzado

Desensamblar y decompilar la muestra

**Aparece en 1 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### Análisis manual

Lo que ningún escáner sustituye

**Aparece en 1 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md).

### Ancho (%100c)

Controla cuántos bytes se imprimen antes de `%n`

**Aparece en 1 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### Ancla

Posición sin consumir (`^`, `$`, `\b`)

**Aparece en 1 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md).

### Anclaje de confianza

Raíz en la que se confía por decisión, no por criptografía

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### AndroidManifest.xml

Declara permisos y componentes de la app

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### Anexo A

Catálogo de 93 controles de referencia (versión 2022)

**Aparece en 1 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md).

### Anillo de privilegio

Nivel del procesador: ring 3 usuario, ring 0 kernel

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### Announced / unannounced

Si el equipo azul sabe o no del test

**Aparece en 1 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### Anomalía PE

Sección rara, entropía alta, IAT mínima: delata malware

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### Anonimato

Dificultad de vincular una acción con una identidad dentro de un conjunto.

**Aparece en 1 clase(s):** [Clase 260 — OPSEC personal y anonimato](../classes/parte-12-osint-e-ingenieria-social/260-opsec-personal-y-anonimato/README.md).

### Anti-análisis dinámico

Malware que detecta el sandbox y se inhibe

**Aparece en 1 clase(s):** [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### Anti-debug / anti-VM

Defensas del packer que hay que evadir

**Aparece en 1 clase(s):** [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Anti-debugging

Detecta la presencia de un depurador

**Aparece en 1 clase(s):** [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md).

### Anti-emulación

Malware que detecta el entorno emulado

**Aparece en 1 clase(s):** [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Anti-forense

Técnicas para borrar o falsear las huellas de una intrusión

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### Anti-reversing

Medidas que impiden o encarecen la RE

**Aparece en 1 clase(s):** [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md).

### Anti-rollback

Control que rechaza versiones anteriores aun si están firmadas.

**Aparece en 1 clase(s):** [Clase 267 — Hacking de firmware](../classes/parte-13-seguridad-movil-iot-e-inalambrica/267-hacking-de-firmware/README.md).

### Anti-VM

El malware detecta el entorno de análisis y se inhibe

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### Anti-VM / anti-sandbox

Detecta el entorno de análisis y se inhibe

**Aparece en 1 clase(s):** [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md).

### Anticolisión

Procedimiento para seleccionar tags presentes simultáneamente.

**Aparece en 1 clase(s):** [Clase 270 — Ataques a RFID y NFC](../classes/parte-13-seguridad-movil-iot-e-inalambrica/270-ataques-a-rfid-y-nfc/README.md).

### APC injection

Inyección mediante colas de procedimientos asíncronos

**Aparece en 1 clase(s):** [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### Apetito de riesgo

Cantidad y tipo de riesgo que la organización está dispuesta a perseguir o retener.

**Aparece en 1 clase(s):** [Clase 276 — Gobernanza de la seguridad de la información](../classes/parte-14-grc-riesgo-y-cumplimiento/276-gobernanza-de-la-seguridad-de-la-informacion/README.md).

### API de alto nivel

Biblioteca que no deja elegir modo, relleno ni IV

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### API de Windows

Interfaz por la que el malware habla con el SO

**Aparece en 1 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### API hashing

Buscar la API por un hash de su nombre

**Aparece en 1 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### API hooking

Interceptar llamadas para filtrar los resultados

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### API hooking en Linux

Redefinir funciones de libc para ocultar

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### API REST

Backend que expone datos y lógica en endpoints estructurados

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### API REST / GraphQL

Backend que devuelve datos estructurados, no HTML

**Aparece en 1 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### API Security Top 10

Lista OWASP específica de riesgos de API

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### APIPA

169.254.0.0/16; autoasignación cuando falla DHCP.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### APK

Archivo ZIP que empaqueta una app Android

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### APKTool

Desempaqueta el APK y decodifica el manifiesto

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### Aplicabilidad

Razón documentada por la que una norma obliga a una entidad o flujo.

**Aparece en 1 clase(s):** [Clase 281 — Cumplimiento: GDPR, HIPAA y PCI-DSS](../classes/parte-14-grc-riesgo-y-cumplimiento/281-cumplimiento-gdpr-hipaa-y-pci-dss/README.md).

### AppSec — Application Security

Práctica de reducir y verificar riesgos de seguridad durante el diseño, desarrollo, despliegue y operación de aplicaciones.

**Claves de búsqueda normalizadas:** `appsec`.

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### Aprender haciendo

La explotación se domina resolviendo retos

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### APT

Advanced Persistent Threat: adversario sofisticado, persistente y con recursos

**Aparece en 1 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md).

### APT29

Actor estatal (Cozy Bear) frecuente en planes de emulación

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### Arbitration ID

Identificador usado para prioridad y significado, no identidad segura.

**Aparece en 1 clase(s):** [Clase 274 — Seguridad automotriz y bus CAN](../classes/parte-13-seguridad-movil-iot-e-inalambrica/274-seguridad-automotriz-y-bus-can/README.md).

### Archivo canario

Fichero señuelo para probar el riesgo sin datos reales

**Aparece en 1 clase(s):** [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md).

### Arena

Región del heap que atiende a un conjunto de hilos

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### Argon2 / Argon2id

KDF recomendada actual; memoria, iteraciones y paralelismo

**Aparece en 1 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md).

### argparse

Módulo estándar para crear CLIs.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### Arista

Relación tipada entre nodos, con fuente y tiempo.

**Aparece en 1 clase(s):** [Clase 255 — Automatización de OSINT: SpiderFoot y Maltego](../classes/parte-12-osint-e-ingenieria-social/255-automatizacion-de-osint-spiderfoot-y-maltego/README.md).

### Aritmética segura

Comprobar límites antes de operar

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### ARP

Traduce una IP en la MAC correspondiente; sin autenticación por diseño

**Aparece en 3 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md), [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md), [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### ARP discovery

Descubrimiento en la LAN mediante consultas ARP; el más fiable

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### ARP spoofing

Envenenamiento de la tabla IP-a-MAC en la red local

**Aparece en 1 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md).

### ARP spoofing / poisoning

Respuestas ARP falsas para interceptar tráfico en la LAN

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### Artefacto

Evidencia concreta de capacidad, contextualizada y sanitizada.

**Aparece en 3 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md), [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md), [Clase 309 — Construcción de portafolio y home lab permanente](../classes/parte-16-capstones-y-preparacion-de-certificaciones/309-construccion-de-portafolio-y-home-lab-permanente/README.md).

### Artefacto detectable

Rastro que cada técnica deja para el defensor

**Aparece en 1 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md).

### ARX

Suma, rotación y XOR; rápidas y en tiempo constante

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### ASCII

Mapeo de caracteres a 7 bits

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### ASCII / ORD

Compara un carácter por su valor numérico

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### ASLR

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 5 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md), [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md), [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md), [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md), [Clase 344 — Estado del juego, memoria y manipulación controlada](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/344-estado-juego-memoria-manipulacion-controlada/README.md).

### ASN

Identificador de un sistema autónomo que anuncia prefijos, no sinónimo de empresa.

**Aparece en 1 clase(s):** [Clase 251 — OSINT de empresas y dominios](../classes/parte-12-osint-e-ingenieria-social/251-osint-de-empresas-y-dominios/README.md).

### Assumed breach

Empezar con un punto de apoyo ya concedido para evaluar la post-explotación

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### Assurance

Confianza sustentada en evidencia sobre diseño y operación.

**Aparece en 1 clase(s):** [Clase 276 — Gobernanza de la seguridad de la información](../classes/parte-14-grc-riesgo-y-cumplimiento/276-gobernanza-de-la-seguridad-de-la-informacion/README.md).

### AST

Árbol que representa la estructura sintáctica del código.

**Aparece en 1 clase(s):** [Clase 238 — SAST: análisis estático de código](../classes/parte-11-devsecops-y-seguridad-del-sdlc/238-sast-analisis-estatico-de-codigo/README.md).

### Ataque de complejidad

Consultas anidadas o recursivas que provocan DoS

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### Ataque de diccionario

Probar listas de contraseñas conocidas

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### Ataque de Kaminsky

Técnica que multiplicó las opciones de envenenar una caché

**Aparece en 1 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md).

### Ataque de máscara

Fuerza bruta dirigida por un patrón conocido

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### Ataque de timing

Explota que el tiempo dependa de datos secretos

**Aparece en 1 clase(s):** [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### Ataque híbrido

Combina diccionario y máscara

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### Ataque por caché

Recuperar claves observando accesos a memoria

**Aparece en 1 clase(s):** [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### Ataque por diccionario

Prueba de contraseñas frecuentes y sus mutaciones

**Aparece en 1 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md).

### Ataques Potato

Familia que abusa de la suplantación para llegar a SYSTEM

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### Atomic Red Team

Biblioteca de pruebas atómicas para simular TTPs

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### Atribución

Determinar quién está detrás; con niveles de confianza

**Aparece en 1 clase(s):** [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md).

### ATT&CK

Base de conocimiento de tácticas y técnicas adversarias observadas

**Aparece en 3 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md), [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md), [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### ATT&CK Navigator

Herramienta para colorear la matriz y visualizar cobertura

**Aparece en 1 clase(s):** [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### Attack-defense

Formato de parchear los servicios propios y atacar los ajenos

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### Attestation

Declaración firmable sobre una propiedad o proceso.

**Aparece en 1 clase(s):** [Clase 246 — Supply chain security: SBOM y SLSA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md).

### Audiencia

Lector con necesidades específicas

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### Audit mode

Evaluación y registro sin bloqueo, útil para adopción gradual.

**Aparece en 1 clase(s):** [Clase 244 — Políticas como código con OPA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/244-politicas-como-codigo-con-opa/README.md).

### Audit trail

Registro ordenado de solicitudes, decisiones, ejecuciones y resultados.

**Aparece en 10 clase(s):** [Clase 331 — IA generativa y LLMs en ciberseguridad: panorama, capacidades y límites](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/331-ia-generativa-y-llms-en-ciberseguridad-panorama-y-limites/README.md), [Clase 332 — Agentes de IA y el Model Context Protocol (MCP) para seguridad](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/332-agentes-de-ia-y-el-model-context-protocol-mcp-para-seguridad/README.md), [Clase 333 — kali-mcp: orquestar herramientas de Kali desde un agente de IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/333-kali-mcp-orquestar-herramientas-de-kali-desde-un-agente-de-ia/README.md), [Clase 334 — Reconocimiento y escaneo asistidos por IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/334-reconocimiento-y-escaneo-asistidos-por-ia/README.md), [Clase 335 — Explotación y post-explotación autorizada asistida por IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/335-explotacion-y-post-explotacion-autorizada-asistida-por-ia/README.md), [Clase 336 — OSINT y auditoría web con agentes de IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/336-osint-y-auditoria-web-con-agentes-de-ia/README.md), [Clase 337 — IA para el lado defensivo: SOC, triaje y forense](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/337-ia-para-el-lado-defensivo-soc-triaje-y-forense/README.md), [Clase 338 — Generación de informes y flujos de trabajo con IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/338-generacion-de-informes-y-flujos-de-trabajo-con-ia/README.md), [Clase 339 — Riesgos, guardrails, OPSEC y ética del hacking con IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/339-riesgos-guardrails-opsec-y-etica-del-hacking-con-ia/README.md), [Clase 340 — Capstone: pentest autorizado asistido por IA con MCP](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/340-capstone-pentest-autorizado-asistido-por-ia-con-mcp/README.md).

### Autenticación

Control que verifica la identidad del usuario

**Aparece en 1 clase(s):** [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### Autenticación de transacción

Verificación específica de la acción, no solo de la persona.

**Aparece en 1 clase(s):** [Clase 257 — Pretexting y vishing](../classes/parte-12-osint-e-ingenieria-social/257-pretexting-y-vishing/README.md).

### Autenticación del acuerdo

Firma o certificado que ata el DH a una identidad

**Aparece en 1 clase(s):** [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### Autenticación por cookie

Requisito: la sesión depende solo de la cookie

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### Autenticidad

Garantía de que el mensaje viene de quien dice

**Aparece en 1 clase(s):** [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

### Auth bypass con $ne

`password: {$ne: ""}` entra sin conocer la contraseña

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### Authorization Code

Flujo recomendado: código canjeado por token

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### Authorization server

Autentica y emite tokens

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### authorizedkeys

Clave SSH que da acceso sin contraseña

**Aparece en 2 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md), [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### Auto-análisis

Analizadores que identifican funciones y generan la decompilación

**Aparece en 2 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md), [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### Auto-binding

Mapeo automático de la petición al objeto

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### Automation Framework

Escaneos reproducibles definidos en fichero

**Aparece en 1 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md).

### Automatización

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 343 — Taxonomía técnica de cheats](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/343-taxonomia-tecnica-cheats/README.md).

### AutoOpen / DocumentOpen

Macros que se ejecutan al abrir el documento

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### Autoritativo

Servidor que posee los datos oficiales de una zona DNS.

**Aparece en 1 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md).

### Autorización

Comprobar si una identidad puede hacer una acción

**Aparece en 2 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md), [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### Autorización ≠ autenticación

OAuth da acceso; no prueba identidad por sí solo

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### Autorización en servidor

Por objeto y denegando por defecto

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### Autorización escrita

Permiso firmado; la línea que separa el pentest del delito

**Aparece en 1 clase(s):** [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### Autorización granular

Comprobar permiso por objeto y función en el servidor

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### Autorización por resolver

Comprobar el permiso en cada campo, no solo el endpoint

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### autoroute

Ruta de Metasploit hacia una subred vía Meterpreter

**Aparece en 1 clase(s):** [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### Autoruns

Herramienta de Sysinternals que lista puntos de auto-arranque

**Aparece en 1 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md).

### Auxiliary

Módulo de escaneo, enumeración o fuzzing sin explotar

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### AXFR

Transferencia de zona DNS; entrega la zona completa

**Aparece en 1 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md).

## B

### Backdoor

Deja una puerta abierta para volver a entrar

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### Backend

Servidor de aplicación y sus servicios internos

**Aparece en 1 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### Backlog

Cola de conexiones pendientes que fija `listen()`

**Aparece en 1 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### Backport

Parche aplicado sin subir el número de versión; falsea el cruce con CVE

**Aparece en 1 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md).

### Backup offline / inmutable

La defensa que el ransomware no puede alcanzar

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Bad character (-b)

Byte que rompe el payload en cierto contexto

**Aparece en 1 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### Badchars

Bytes prohibidos que el shellcode debe esquivar

**Aparece en 1 clase(s):** [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### Balanceador

Reparte la carga entre servidores

**Aparece en 1 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### Banner

Respuesta o metadato de servicio; puede ser incompleto o engañoso.

**Aparece en 3 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md), [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md), [Clase 254 — OSINT técnico: Shodan y Censys](../classes/parte-12-osint-e-ingenieria-social/254-osint-tecnico-shodan-y-censys/README.md).

### Bans,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 359 — Privacidad, gobernanza, sanciones y seguridad del propio Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/359-privacidad-gobernanza-sanciones-seguridad-anticheat/README.md).

### BApp Store

Catálogo de extensiones de Burp

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### Base

Sistema de numeración (2, 8, 10, 16)

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### Base de firmas

Catálogo de problemas conocidos que el escáner busca

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### Base de libc

Dirección de carga; leak menos offset conocido

**Aparece en 1 clase(s):** [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md).

### Base de región

Dirección de inicio; las distancias internas son fijas

**Aparece en 1 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### Base de una región

Dirección de inicio; las distancias internas son fijas

**Aparece en 1 clase(s):** [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md).

### Base64

Binario como 64 caracteres imprimibles

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### Baseline

Estado del sistema limpio para comparar

**Aparece en 1 clase(s):** [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### Baseline scan

Escaneo rápido y no intrusivo para CI/CD

**Aparece en 1 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md).

### Batching

Muchas operaciones en una sola petición

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### bcrypt

KDF clásica con coste ajustable; memoria fija y límite de 72 bytes

**Aparece en 1 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md).

### bcrypt/scrypt/argon2

Algoritmos de hash de contraseñas con factor de coste

**Aparece en 1 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md).

### BCryptGenRandom

API equivalente en Windows

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### Beacon

Implante que llama a casa a intervalos configurables

**Aparece en 3 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md), [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md), [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### Beaconing

Conexiones periódicas a un mismo destino; firma de C2

**Aparece en 2 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md), [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md).

### BEAST / POODLE

Ataques sobre CBC y sobre el relleno de SSL 3.0

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### BEC

Compromiso o suplantación de correo para inducir acciones de negocio.

**Aparece en 1 clase(s):** [Clase 256 — Fundamentos de ingeniería social](../classes/parte-12-osint-e-ingenieria-social/256-fundamentos-de-ingenieria-social/README.md).

### Bejtlich

Autor que formalizó la disciplina de NSM

**Aparece en 1 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md).

### BFLA (API5)

Forced browsing; llamar a funciones de nivel superior

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### BIA

Análisis de impacto y dependencias del negocio.

**Aparece en 1 clase(s):** [Clase 283 — Continuidad de negocio y plan de recuperación ante desastres](../classes/parte-14-grc-riesgo-y-cumplimiento/283-continuidad-de-negocio-y-plan-de-recuperacion-ante-desastres/README.md).

### Bin

Lista de chunks libres para reutilizar

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### Binario firmado de confianza

Su uso no levanta las alarmas de un binario nuevo

**Aparece en 1 clase(s):** [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### BinaryFormatter

Serializador .NET peligroso, desaconsejado

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### Bind mount

Montaje de una ruta del host en el contenedor

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### Bind shell

El objetivo abre un puerto; el atacante se conecta

**Aparece en 1 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md).

### Binder

Mecanismo principal de IPC en Android.

**Aparece en 1 clase(s):** [Clase 261 — Seguridad de Android: arquitectura](../classes/parte-13-seguridad-movil-iot-e-inalambrica/261-seguridad-de-android-arquitectura/README.md).

### Bit

Dígito binario, 0 o 1

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### Bit-flipping

Voltear bits del cifrado para cambiar el claro de forma predecible

**Aparece en 1 clase(s):** [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### Bit SUID

El binario corre con los privilegios de su propietario

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### Bits de seguridad

Coste real del mejor ataque conocido, en potencias de 2

**Aparece en 2 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md), [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### Black box

El equipo no recibe información previa

**Aparece en 1 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### Black hat

Hacker malicioso sin autorización

**Aparece en 1 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).

### BLAKE2 / BLAKE3

Hashes modernos orientados a velocidad

**Aparece en 1 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md).

### Bleichenbacher

Oráculo análogo sobre el relleno PKCS#1 v1.5 de RSA

**Aparece en 1 clase(s):** [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### Blocklist

Filtrar caracteres prohibidos; siempre evadible

**Aparece en 3 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md), [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md), [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### BloodHound

Grafo de AD que calcula rutas hacia Domain Admin

**Aparece en 1 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### Bloque básico

Secuencia de instrucciones sin saltos

**Aparece en 2 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md), [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### Bloqueo de cuenta

Defensa que congela la cuenta tras N fallos

**Aparece en 1 clase(s):** [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md).

### Bloqueo de cuentas

Efecto colateral de la fuerza bruta contra un directorio

**Aparece en 1 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md).

### Blueprint

Temario oficial vigente del examen.

**Aparece en 1 clase(s):** [Clase 301 — Roadmap de certificaciones: CompTIA, OSCP, CISSP y más](../classes/parte-16-capstones-y-preparacion-de-certificaciones/301-roadmap-de-certificaciones-comptia-oscp-cissp-y-mas/README.md).

### Body of knowledge

Alcance publicado de conocimientos evaluados.

**Aparece en 1 clase(s):** [Clase 290 — Certificaciones y desarrollo de carrera](../classes/parte-14-grc-riesgo-y-cumplimiento/290-certificaciones-y-desarrollo-de-carrera/README.md).

### BOLA

Acceso indebido a objetos por faltar una comprobación contextual.

**Aparece en 1 clase(s):** [Clase 247 — Seguridad de APIs en el ciclo de desarrollo](../classes/parte-11-devsecops-y-seguridad-del-sdlc/247-seguridad-de-apis-en-el-ciclo-de-desarrollo/README.md).

### BOLA (API1)

IDOR de las APIs; acceder al objeto de otro usuario

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### BOLA en GraphQL

Acceder a datos de otro navegando relaciones

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### Bonding

Conservación de claves para conexiones futuras.

**Aparece en 1 clase(s):** [Clase 271 — Seguridad de Bluetooth y BLE](../classes/parte-13-seguridad-movil-iot-e-inalambrica/271-seguridad-de-bluetooth-y-ble/README.md).

### Booleana

Deducir datos por la diferencia entre condición verdadera y falsa

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### Bootkit

Se carga antes que el SO durante el arranque

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### Bootloader

Código inicial que prepara y carga etapas posteriores.

**Aparece en 1 clase(s):** [Clase 267 — Hacking de firmware](../classes/parte-13-seguridad-movil-iot-e-inalambrica/267-hacking-de-firmware/README.md).

### Borrado de logs (T1070)

Eliminar registros; deja un hueco detectable

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### Bot / botnet

Máquina enrolada en una red controlada en masa

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### Botnet de IoT

Red de dispositivos infectados para DDoS

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### Bounding

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 346 — Información expuesta, radar, ESP y world-to-screen](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/346-informacion-expuesta-radar-esp-world-to-screen/README.md).

### BPDU Guard

Protege STP desactivando puertos con anuncios indebidos

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### BPF

Berkeley Packet Filter: lenguaje de filtrado en captura

**Aparece en 3 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md), [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md), [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### BRE

Basic Regular Expressions (modo por defecto de grep)

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### Breakpoint

Pausa la ejecución al llegar a un punto

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### Brecha de datos

Volcado de credenciales previo reutilizable

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### Brecha previa

Indicio de compromiso anterior; se escala de inmediato

**Aparece en 1 clase(s):** [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### Bridged

Modo de red: la VM es un equipo más de la LAN

**Aparece en 1 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md).

### Broadcast

Última dirección del bloque; alcanza a todos los hosts.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### Broker de herramientas

Capa que valida y media cada ejecución.

**Aparece en 1 clase(s):** [Clase 333 — kali-mcp: orquestar herramientas de Kali desde un agente de IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/333-kali-mcp-orquestar-herramientas-de-kali-desde-un-agente-de-ia/README.md).

### BSS

Segmento de globales sin inicializar

**Aparece en 1 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md).

### BSSID

Dirección MAC del punto de acceso

**Aparece en 1 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md).

### Buffer

Región de tamaño fijo reservada para datos

**Aparece en 1 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md).

### Buffer de protocolo

Campo concreto donde buscar (`http.uri`, `tls.sni`, `dns.query`)

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### Buffer overflow

Escribir más datos de los que caben en el buffer

**Aparece en 1 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md).

### Bug bounty

Programa que recompensa reportes autorizados

**Aparece en 2 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md), [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### builtinmuloverflow

Multiplicación con detección de overflow

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Burp Suite

Proxy de pentesting web estándar de la industria

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### Búsqueda binaria

Acota el carácter con comparaciones `>`/`<`

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### BYOVD

Cargar un driver vulnerable firmado y explotarlo

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### Bypass con negativo

Un valor firmado negativo que se vuelve enorme sin signo

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Bypass de login

`admin' --` para entrar sin contraseña

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### Bypass en caliente

Alterar una comprobación cambiando el retorno en vivo

**Aparece en 1 clase(s):** [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md).

### Bypass encadenado

Combinar leak + ROP + ataque a GOT/heap

**Aparece en 1 clase(s):** [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md).

### Byte

Grupo de 8 bits

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### Byte nulo

`shell.php%00.jpg`; truco histórico de bypass

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### Byte nulo (0x00)

Bad character que trunca cadenas; hay que evitarlo

**Aparece en 2 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md), [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### Bytecode Dalvik

Código compilado que corre en ART/Dalvik

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### bytes

Secuencia de octetos crudos (datos binarios).

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### Bytes prohibidos (badchars)

Bytes que rompen el payload (p. ej. el nulo en strcpy)

**Aparece en 1 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md).

## C

### C2 / C&C

Command and Control: canal de órdenes entre implante y atacante

**Aparece en 1 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md).

### C2 (command and control)

Canal por el que el operador controla el malware

**Aparece en 2 clase(s):** [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md), [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md).

### C2 framework

Plataforma que genera implantes y gestiona sesiones

**Aparece en 1 clase(s):** [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### C2 profile

Plantilla que define cómo se ve el tráfico C2

**Aparece en 1 clase(s):** [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### CA

Autoridad de certificación que firma certificados de confianza.

**Aparece en 2 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md), [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### CA de Burp

Certificado propio que hay que instalar para interceptar HTTPS

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### CA de ZAP

Certificado propio para interceptar HTTPS

**Aparece en 1 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md).

### CA intermedia

Firma los certificados finales; protege la clave raíz

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### CA maliciosa

Autoridad instalada en el dispositivo que legitima certificados falsos

**Aparece en 1 clase(s):** [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md).

### CA raíz

Certificado autofirmado preinstalado; anclaje de confianza

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### CaaS

Mercado de capacidades criminales especializadas; aquí, Cybercrime-as-a-Service

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Cabecera

Par clave-valor con metadatos de una petición o respuesta.

**Aparece en 1 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md).

### Cabecera de regla

Acción, protocolo, origen, dirección y destino

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### Cabecera HTTP

Metadato de la petición; también es entrada del usuario

**Aparece en 1 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### Caché ARP

Tabla local de correspondencias IP-MAC aprendidas.

**Aparece en 2 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md), [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### Cache poisoning

Inyectar una respuesta falsa en la caché de un resolver

**Aparece en 2 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md), [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Caché web

Guarda respuestas y las sirve a muchos usuarios

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Cadena de ataque

Acceso, lateral, exfiltración y cifrado final

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Cadena de comunidad

"Contraseña" de SNMP; `public` y `private` son los valores por defecto

**Aparece en 2 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md), [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md).

### Cadena de confianza

Recorrido de firmas desde el certificado hasta una raíz

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### Cadena de entrega

Secuencia que lleva de abrir el doc a la carga final

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### Cadena de texto

Literal, con `nocase`, `wide`, `ascii`

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Cadena en la pila

Construir "/bin/sh" con instrucciones para evitar nulos

**Aparece en 1 clase(s):** [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### Cadena hexadecimal

Secuencia de bytes con comodines `??`

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Cadena ROP

Secuencia ordenada de gadgets y valores en la pila

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### Cadena SEH

Lista de manejadores registrados, en la pila

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### Cadenas cifradas

Textos descifrados solo en ejecución; evaden `strings`

**Aparece en 1 clase(s):** [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md).

### Cálculo dinámico de direcciones

Derivar direcciones a partir de un leak

**Aparece en 1 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### Calentamiento de dominio

Enviar tráfico legítimo creciente para construir reputación de envío

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### Call graph

Grafo de qué función llama a qué

**Aparece en 1 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### call / ret

Llamar (apila retorno) / volver (desapila a RIP)

**Aparece en 2 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md), [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### Callback

Devolución por un número obtenido de una fuente confiable.

**Aparece en 3 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md), [Clase 257 — Pretexting y vishing](../classes/parte-12-osint-e-ingenieria-social/257-pretexting-y-vishing/README.md), [Clase 259 — Defensa contra la ingeniería social](../classes/parte-12-osint-e-ingenieria-social/259-defensa-contra-la-ingenieria-social/README.md).

### Cámara,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 342 — Arquitectura de videojuegos desde la perspectiva de seguridad](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/342-arquitectura-videojuegos-perspectiva-seguridad/README.md).

### Camino ejecutado

El dinámico solo ve los caminos que corren

**Aparece en 1 clase(s):** [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md).

### Camino nuevo

Entrada que alcanza código no visto; se guarda como semilla

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### Campo de protocolo

Dato direccionable de una cabecera (`ip.src`, `tcp.flags.syn`)

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### Campo finito

Aritmética modular sobre un primo, donde vive la curva

**Aparece en 1 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md).

### Canal encubierto

Vía de comunicación no prevista por el diseño

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### Canal HTTP(S)

Se mezcla con la navegación; oculta contenido con TLS

**Aparece en 1 clase(s):** [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md).

### Canal independiente

Medio de verificación no proporcionado por la propia solicitud.

**Aparece en 1 clase(s):** [Clase 256 — Fundamentos de ingeniería social](../classes/parte-12-osint-e-ingenieria-social/256-fundamentos-de-ingenieria-social/README.md).

### Canal lateral

Fuga por tiempo, consumo o caché al ejecutar la operación

**Aparece en 2 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md), [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### Canal lateral temporal

Tiempo de respuesta distinto que filtra si la cuenta existe

**Aparece en 1 clase(s):** [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### Canal OOB

Los logs del servidor del atacante reciben el dato

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### Canario

Centinela que detecta overflow de pila

**Aparece en 1 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md).

### Canonicalización de ruta

Normalizar la ruta antes de usarla

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### Cantidad negativa

Valor que un cálculo mal hecho convierte en abono

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### Capa

Nivel del paquete (Ether/IP/TCP/UDP/ICMP) como objeto

**Aparece en 1 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md).

### Capa (layer)

Unidad incremental de una imagen, cacheable

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### Capability

Operación concreta que un componente ofrece bajo permisos.

**Aparece en 1 clase(s):** [Clase 332 — Agentes de IA y el Model Context Protocol (MCP) para seguridad](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/332-agentes-de-ia-y-el-model-context-protocol-mcp-para-seguridad/README.md).

### Capability baseline

Conjunto adaptable de capacidades, no lista de aprobación.

**Aparece en 1 clase(s):** [Clase 266 — Seguridad de IoT: panorama y superficie de ataque](../classes/parte-13-seguridad-movil-iot-e-inalambrica/266-seguridad-de-iot-panorama-y-superficie-de-ataque/README.md).

### Capacidad

Cantidad de datos que un portador puede ocultar

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### Capacidad Linux

Privilegio granular que puede retirarse del proceso.

**Aparece en 1 clase(s):** [Clase 243 — Imágenes y contenedores seguros en el pipeline](../classes/parte-11-devsecops-y-seguridad-del-sdlc/243-imagenes-y-contenedores-seguros-en-el-pipeline/README.md).

### Capital One

Brecha de 2019 causada por SSRF al metadata de AWS

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### capstone / pyelftools

Librerías para construir herramientas de análisis

**Aparece en 1 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### Carga de archivos

Funcionalidad de subir ficheros; superficie de ataque frecuente

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### Cargador

Primera etapa que descarga o despliega la carga real

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### Cargador de pruebas

Programa que ejecuta el shellcode para validarlo

**Aparece en 1 clase(s):** [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### Catálogo de detección

El mapa de dónde mirar que se entrega al cliente

**Aparece en 1 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md).

### Categoría de riesgo

Agrupación de fallos por naturaleza, no un bug concreto

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### Categoría default

Conjunto que ejecutan `-sC` y `-A`

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### Categoría intrusive / dos / exploit

Pueden degradar, tumbar o explotar el objetivo

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### Categoría safe

Scripts que no afectan al objetivo de forma apreciable

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### Categoría vuln

Comprobación de vulnerabilidades conocidas; a menudo intrusiva

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### Categorización de dominio

Clasificar un dominio (business/health) para pasar filtros

**Aparece en 1 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### CBC

Encadenamiento por XOR con el cifrado anterior

**Aparece en 1 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md).

### CBK

Cuerpo de conocimiento, no sustituto del esquema oficial vigente.

**Aparece en 1 clase(s):** [Clase 304 — Preparación CISSP: los 8 dominios](../classes/parte-16-capstones-y-preparacion-de-certificaciones/304-preparacion-cissp-los-8-dominios/README.md).

### CCA

Puede pedir descifrados y observar el resultado

**Aparece en 1 clase(s):** [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### cdecl / stdcall

Convenciones de x86; pasan argumentos por la pila

**Aparece en 1 clase(s):** [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### CDN

Red de distribución que cachea contenido cerca del usuario

**Aparece en 1 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### Centro,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 357 — Estadística, anomalías y falsos positivos](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/357-estadistica-anomalias-falsos-positivos/README.md).

### Cerrado

El host responde pero nadie escucha; prueba que el host existe

**Aparece en 1 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### Certificado

Documento firmado por una CA que prueba la identidad del servidor.

**Aparece en 1 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md).

### Certificado X.509

Documento con clave pública, identidad y firma de la CA

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### Certificate pinning

Restricción adicional de confianza TLS; no sustituye autorización.

**Aparece en 2 clase(s):** [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md), [Clase 262 — Pentest de aplicaciones Android](../classes/parte-13-seguridad-movil-iot-e-inalambrica/262-pentest-de-aplicaciones-android/README.md).

### Certificate Transparency

Registros públicos auditables de certificados emitidos.

**Aparece en 3 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md), [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md), [Clase 251 — OSINT de empresas y dominios](../classes/parte-12-osint-e-ingenieria-social/251-osint-de-empresas-y-dominios/README.md).

### certutil / mshta / regsvr32

LOLBins comunes

**Aparece en 1 clase(s):** [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### CFAA

Ley estadounidense de fraude y abuso informático

**Aparece en 1 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).

### CFG

Grafo de flujo de control de una función

**Aparece en 1 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### cgroup

Límite de recursos del kernel por contenedor

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### ChaCha20

Cifrado de flujo moderno basado en operaciones ARX

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### ChaCha20-Poly1305

AEAD para software y móviles sin aceleración AES

**Aparece en 1 clase(s):** [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### Challenge-response

Autenticación que prueba conocimiento sin repetir una respuesta fija.

**Aparece en 1 clase(s):** [Clase 270 — Ataques a RFID y NFC](../classes/parte-13-seguridad-movil-iot-e-inalambrica/270-ataques-a-rfid-y-nfc/README.md).

### check

Verifica la condición vulnerable sin ejecutar el ataque

**Aparece en 1 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md).

### checksec

Herramienta que reporta las mitigaciones activas

**Aparece en 1 clase(s):** [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md).

### Checksum offloading

La NIC calcula el checksum tras la captura; produce falsos rojos

**Aparece en 1 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md).

### Checksum / SHA-256

Hash para verificar integridad de una descarga

**Aparece en 1 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md).

### Chi-cuadrado / RS analysis

Pruebas estadísticas que detectan LSB

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### chisel / ligolo-ng

Túneles sobre HTTP(S) cuando no hay SSH

**Aparece en 1 clase(s):** [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### chmod / chown

Cambian permisos / propietario de archivos

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

### Chunk

Bloque de memoria con metadatos delante

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### Chunking

Fragmentar el dato en trozos pequeños

**Aparece en 1 clase(s):** [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md).

### CI/CD

Integración continua donde encaja el escaneo automatizado

**Aparece en 1 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md).

### CIA

Confidencialidad, Integridad y Disponibilidad; las tres propiedades base a proteger

**Aparece en 1 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md).

### Ciclo de vida

Ejecución, persistencia, evasión, objetivo, C2

**Aparece en 1 clase(s):** [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### Ciclo estático↔dinámico

Alternar entre ambos para reconstruir el comportamiento

**Aparece en 1 clase(s):** [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md).

### CIDR

Notación IP/prefijo que indica cuántos bits son de red.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### Cierre del engagement

Fin formal: informe entregado y correcciones verificadas

**Aparece en 1 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md).

### Cifrado

Transformación reversible con clave

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### Cifrado de César

Sustitución por desplazamiento fijo del alfabeto

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### Cifrado de flujo

Genera keystream y lo combina con XOR con el mensaje

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### Cifrado extremo a extremo

Confidencialidad entre los extremos; ni la red ni el servidor leen

**Aparece en 1 clase(s):** [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md).

### Cifrado híbrido

RSA transporta una clave AES que cifra los datos

**Aparece en 2 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md), [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md).

### Cifrado por bloques

Primitiva que transforma bloques de tamaño fijo (AES: 128 bits)

**Aparece en 1 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md).

### Cifrado sin autenticar

Deja el mensaje maleable; usar AEAD

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### Cipher suite

Conjunto de algoritmos negociados; en TLS 1.3 solo AEAD y hash

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### CL.TE / TE.CL / TE.TE

Variantes según qué servidor prioriza qué cabecera

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Claim

Dato del payload: `sub`, `exp`, `iss`, `aud`, roles

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### Clase negada

`[^...]`: casa todo salvo lo listado

**Aparece en 1 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md).

### Clasificación,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 358 — Machine Learning aplicado a Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/358-machine-learning-aplicado-anticheat/README.md).

### classes.dex

Fichero con el bytecode de la app

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### Classic McEliece

Esquema basado en códigos; claves muy grandes

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### Clave de caché

URL y cabeceras que identifican qué respuesta corresponde

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Clave incrustada

Credencial escrita en el código fuente

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### Clave privada RSA

La tiene solo el atacante; hace irreversible el cifrado

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Clave pública / privada

Par relacionado: una se publica, la otra se guarda

**Aparece en 1 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md).

### Clave simétrica compartida

La misma clave genera y verifica el MAC

**Aparece en 1 clase(s):** [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

### Client

La aplicación que solicita acceso

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### Client-authoritative

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 351 — Multiplayer y autoridad: nunca confiar en el cliente](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/351-multiplayer-autoridad-nunca-confiar-cliente/README.md).

### Cliente,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 341 — Introducción a Game Security y modelo de amenazas](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/341-introduccion-game-security-modelo-amenazas/README.md).

### Cliente-servidor

El navegador pide, el servidor responde sobre HTTP/HTTPS

**Aparece en 1 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### ClientHello / ServerHello

Primeros mensajes del handshake

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### CLM

Constrained Language Mode: limita APIs peligrosas

**Aparece en 1 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md).

### Clúster Zeek

Despliegue con workers, proxy y manager para gran escala

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### Cmdlet

Comando `Verbo-Nombre` que devuelve objetos .NET

**Aparece en 1 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md).

### cmp / jmp

Comparar ajustando flags / saltar

**Aparece en 1 clase(s):** [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### CNAME

Alias que apunta un nombre a otro nombre canónico.

**Aparece en 1 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md).

### COA

El adversario solo ve texto cifrado

**Aparece en 1 clase(s):** [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### Cobalt Strike

C2 comercial de referencia; Beacon y Malleable

**Aparece en 2 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md), [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### Cobertura

Alcance demostrado frente a comportamientos y fuentes definidos.

**Aparece en 4 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md), [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md), [Clase 280 — Controles CIS](../classes/parte-14-grc-riesgo-y-cumplimiento/280-controles-cis/README.md), [Clase 306 — Capstone: detección Blue Team end-to-end](../classes/parte-16-capstones-y-preparacion-de-certificaciones/306-capstone-deteccion-blue-team-end-to-end/README.md).

### Cobertura de detección

Porcentaje de técnicas ejecutadas que generaron alerta

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### CodeQL

Consultar el código como una base de datos

**Aparece en 1 clase(s):** [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Codicioso

Casa lo máximo y retrocede

**Aparece en 1 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md).

### Codificación

Transformación reversible sin secreto

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### Codificación de payload

`%2e%2e%2f` para saltar filtros de traversal

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### Codificación de salida

Codificar el dato según su contexto; defensa primaria del XSS

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### Código de estado

Número que resume el resultado de una respuesta HTTP.

**Aparece en 1 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md).

### Código de respuesta

200, 403, 401… revelan la existencia y protección de una ruta

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### Colector

Servidor que recibe, almacena e indexa los flujos

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### Colisión

Dos entradas distintas que producen el mismo hash

**Aparece en 2 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md), [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md).

### Colisión y firmas

Dos mensajes con el mismo digest comparten firma válida

**Aparece en 1 clase(s):** [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### Collection

Reunir los datos dentro de la red objetivo

**Aparece en 1 clase(s):** [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md).

### Colocación de sensores

Dónde se observa el tráfico; determina la visibilidad

**Aparece en 1 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md).

### Colorización

Reglas que pintan filas según una condición, para triaje visual

**Aparece en 1 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md).

### Comentario SQL

`--`, `#`, `/* */`; corta el resto de la consulta

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### Command and control (C2)

Canal por el que el malware recibe órdenes

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### Commit

Snapshot inmutable del proyecto con hash único

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### commitcreds(preparekernelcred(0))

Patrón para darse root desde el kernel

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### Comparación

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 345 — Trainers e instrumentación del cliente](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/345-trainers-instrumentacion-cliente/README.md).

### Comparación con ==

Fuga por timing en etiquetas y tokens

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### Comparación de estado

Diferencial antes/después que aísla la actividad

**Aparece en 1 clase(s):** [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### Comparación en tiempo constante

Recorre toda la longitud sin salir antes

**Aparece en 1 clase(s):** [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### comparedigest

Función de comparación segura en la stdlib de Python

**Aparece en 1 clase(s):** [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

### Comparer

Resalta diferencias entre dos respuestas

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### Compartición (share)

Recurso publicado por SMB; puede contener secretos

**Aparece en 2 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md), [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md).

### Compartimentación

Separación consistente para limitar correlación e impacto.

**Aparece en 2 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md), [Clase 260 — OPSEC personal y anonimato](../classes/parte-12-osint-e-ingenieria-social/260-opsec-personal-y-anonimato/README.md).

### Complejidad inútil

Endurecer reglas solo produce variantes predecibles

**Aparece en 1 clase(s):** [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md).

### Complementa el análisis

La emulación escala, no reemplaza el manual

**Aparece en 1 clase(s):** [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Componente exportado

Punto de entrada accesible desde otras aplicaciones según manifiesto y permisos.

**Aparece en 2 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md), [Clase 261 — Seguridad de Android: arquitectura](../classes/parte-13-seguridad-movil-iot-e-inalambrica/261-seguridad-de-android-arquitectura/README.md).

### Componentes vulnerables

A06; heredar CVE de las dependencias

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### Compose

Orquestador declarativo multi-servicio

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### Comprensión

Expresión que construye una colección filtrando y transformando.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### Concatenación

Construir la consulta pegando entrada con texto; la causa raíz

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### Concentración

Dependencia común capaz de afectar múltiples servicios.

**Aparece en 1 clase(s):** [Clase 284 — Gestión de riesgo de terceros y proveedores](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md).

### condition

Expresión booleana que dispara la regla

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Conducta objetivo

Acción observable que reduce un escenario de riesgo.

**Aparece en 1 clase(s):** [Clase 286 — Concienciación y cultura de seguridad](../classes/parte-14-grc-riesgo-y-cumplimiento/286-concienciacion-y-cultura-de-seguridad/README.md).

### Confianza analítica

Juicio explicado sobre la solidez de una conclusión.

**Aparece en 1 clase(s):** [Clase 249 — Fundamentos de OSINT](../classes/parte-12-osint-e-ingenieria-social/249-fundamentos-de-osint/README.md).

### Confirmación por tiempo

`sleep`/`timeout` para detectar sin ver la salida

**Aparece en 1 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### Conflicto

Choque de ediciones en la misma línea

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### Confusión de algoritmos

Firmar HS256 con la clave pública RS256 como secreto

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### Confusión de tipo

Enviar un objeto donde se espera una cadena

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### Confusión de tokens/scopes

Usar un token fuera de su propósito o audiencia

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### Confusión / difusión

Ocultar la relación con la clave / propagar cada bit de entrada

**Aparece en 1 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md).

### conn.log

Registro maestro: una línea por conexión con su 5-tupla y bytes

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### Connect scan

Escaneo que completa el handshake TCP para detectar puertos abiertos

**Aparece en 1 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### Connect scan (-sT)

Usa `connect()`; sin privilegios, pero visible en los logs

**Aparece en 2 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md), [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### conntrack

Subsistema del kernel Linux que sigue el estado de las conexiones

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### Conocido

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 347 — Rendering, visibilidad, occlusion y wallhack](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/347-rendering-visibilidad-occlusion-wallhack/README.md).

### Consulta parametrizada

Marcadores + datos aparte; la BD no interpreta el dato

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### Contacto de emergencia

Persona a la que escalar un incidente durante el test

**Aparece en 1 clase(s):** [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### contains / matches

Operadores de subcadena y de expresión regular

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### Contención

Dos dispositivos conducen una línea de manera incompatible.

**Aparece en 2 clase(s):** [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md), [Clase 268 — Análisis de hardware: UART, JTAG y SPI](../classes/parte-13-seguridad-movil-iot-e-inalambrica/268-analisis-de-hardware-uart-jtag-y-spi/README.md).

### Contenedor

Instancia en ejecución de una imagen

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### Contenedor (ISO/VHD)

Formato de disco cuyo contenido interno puede no heredar el MOTW

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### Contenido completo

Captura íntegra de paquetes; máxima fidelidad, alto coste

**Aparece en 1 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md).

### content

Búsqueda de cadena literal; rápida

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### Content discovery / dirbusting

Adivinar rutas no enlazadas con diccionarios

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### Content-Disposition

Forzar descarga en lugar de interpretación

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### Content-Length (CL)

Cabecera que indica la longitud del cuerpo en bytes

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Content-Type

Cabecera puesta por el cliente; se falsea

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### context

Vista de pwndbg con registros, pila y desensamblado

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### Contexto

Alcance, autenticación y reglas usadas para explorar una aplicación.

**Aparece en 2 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md), [Clase 239 — DAST: análisis dinámico de aplicaciones](../classes/parte-11-devsecops-y-seguridad-del-sdlc/239-dast-analisis-dinamico-de-aplicaciones/README.md).

### Contexto conversacional

Publicaciones y respuestas necesarias para interpretar un mensaje.

**Aparece en 1 clase(s):** [Clase 252 — OSINT en redes sociales](../classes/parte-12-osint-e-ingenieria-social/252-osint-en-redes-sociales/README.md).

### Contexto de inyección

Dónde cae la entrada: HTML, atributo, script, URL

**Aparece en 1 clase(s):** [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md).

### Contradicción

Evidencia que reduce la plausibilidad de una hipótesis de identidad.

**Aparece en 1 clase(s):** [Clase 250 — OSINT de personas](../classes/parte-12-osint-e-ingenieria-social/250-osint-de-personas/README.md).

### Contramedida dinámica

El código acaba ejecutándose y ahí se observa

**Aparece en 1 clase(s):** [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md).

### Contraseña contextual

`Empresa2024!` y similares; cumplen la política pero son obvias

**Aparece en 1 clase(s):** [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md).

### Contrato

Descripción interoperable de operaciones y mensajes; no prueba autorización.

**Aparece en 1 clase(s):** [Clase 247 — Seguridad de APIs en el ciclo de desarrollo](../classes/parte-11-devsecops-y-seguridad-del-sdlc/247-seguridad-de-apis-en-el-ciclo-de-desarrollo/README.md).

### Control compensatorio

Medida alternativa que reduce riesgo sin eliminar la causa.

**Aparece en 1 clase(s):** [Clase 245 — Gestión de vulnerabilidades a escala](../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md).

### Control de acceso roto

No verificar bien los permisos; A01 de OWASP

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### Control de flujo

Primitiva de fijar RIP

**Aparece en 1 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### Control de RIP

Objetivo: fijar la dirección a la que salta `ret`

**Aparece en 1 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md).

### Control en el servidor

La autorización no se delega al cliente

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### Control-flow flattening

Aplana la lógica en una máquina de estados

**Aparece en 1 clase(s):** [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md).

### Convención de llamada

Contrato de paso de argumentos (System V)

**Aparece en 2 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md), [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### Convenciones CARO

Estándar de nombres poco seguido por los vendors

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### Conversations

Estadística por pares de interlocutores (bytes, paquetes, duración)

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### Cookie

Dato guardado por el navegador y reenviado al servidor.

**Aparece en 2 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md), [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### Cookies / autenticación

Contexto que `-r` preserva para atacar zonas logueadas

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### Coordinación

Comportamiento conjunto que requiere más evidencia que contenido parecido.

**Aparece en 1 clase(s):** [Clase 252 — OSINT en redes sociales](../classes/parte-12-osint-e-ingenieria-social/252-osint-en-redes-sociales/README.md).

### Core

Taxonomía de resultados del CSF.

**Aparece en 1 clase(s):** [Clase 279 — NIST Cybersecurity Framework](../classes/parte-14-grc-riesgo-y-cumplimiento/279-nist-cybersecurity-framework/README.md).

### Corpus semilla

Entradas válidas de ejemplo desde las que mutar

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### Correlación

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 2 clase(s):** [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md), [Clase 355 — Telemetría para Game Security](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/355-telemetria-game-security/README.md).

### Corroboración

Apoyo mediante evidencia con origen suficientemente independiente.

**Aparece en 1 clase(s):** [Clase 249 — Fundamentos de OSINT](../classes/parte-12-osint-e-ingenieria-social/249-fundamentos-de-osint/README.md).

### CORS

Mecanismo que relaja la SOP de forma controlada

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### CPA

Puede elegir qué textos se cifran; exigencia mínima moderna

**Aparece en 1 clase(s):** [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### CPE

Identificador normalizado de plataforma (`cpe:/a:apache:tomcat:9.0.30`)

**Aparece en 2 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md), [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### CPE/CE

Desarrollo continuo requerido para mantener algunas credenciales.

**Aparece en 1 clase(s):** [Clase 290 — Certificaciones y desarrollo de carrera](../classes/parte-14-grc-riesgo-y-cumplimiento/290-certificaciones-y-desarrollo-de-carrera/README.md).

### cppcheck / clang / Semgrep

Herramientas SAST por patrones

**Aparece en 1 clase(s):** [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### CPU

Unidad de procesamiento que ejecuta instrucciones

**Aparece en 1 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md).

### Crackeo offline

Prueba de contraseñas contra una captura, sin tocar la red

**Aparece en 1 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md).

### Cracking

Recuperar la contraseña en claro a partir de su hash

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### crackmapexec / NetExec

Valida credenciales y privilegios a escala en una subred

**Aparece en 2 clase(s):** [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md), [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### crackmes.one

Repositorio de crackmes para practicar ingeniería inversa sobre binarios creados con ese propósito.

**Sitio oficial:** [crackmes.one](https://crackmes.one/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### Crash

Fallo que suele indicar una corrupción de memoria explotable

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### Crawler

Componente que descubre rutas y transiciones accesibles.

**Aparece en 1 clase(s):** [Clase 239 — DAST: análisis dinámico de aplicaciones](../classes/parte-11-devsecops-y-seguridad-del-sdlc/239-dast-analisis-dinamico-de-aplicaciones/README.md).

### CreateRemoteThread

Import típico de inyección de código

**Aparece en 1 clase(s):** [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md).

### Crece hacia abajo

Apilar resta de RSP; desapilar le suma

**Aparece en 1 clase(s):** [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### Credencial efímera

Autorización de corta duración emitida para un contexto concreto.

**Aparece en 1 clase(s):** [Clase 241 — Secretos en el código y pre-commit hooks](../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md).

### Credenciales por defecto

Vector de infección de IoT

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### Credential stuffing

Reutilizar credenciales filtradas de otras brechas

**Aparece en 2 clase(s):** [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md), [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### CRIME / BREACH

Deducción de secretos mediante la compresión

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### Criptoagilidad

Diseñar para poder cambiar de algoritmo sin rehacer el sistema

**Aparece en 2 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md), [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### Criptoanálisis

Estudio de cómo romper sistemas criptográficos

**Aparece en 1 clase(s):** [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### Criptoanálisis diferencial

Estudia la propagación de diferencias entre entradas

**Aparece en 1 clase(s):** [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### Criptoanálisis lineal

Busca aproximaciones lineales sesgadas

**Aparece en 1 clase(s):** [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### Criptografía

Ocultar el **contenido** del mensaje

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### Criptografía asimétrica

Par de claves: pública y privada

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### Criptografía simétrica

La misma clave cifra y descifra

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### Criterio

Requisito contra el que se compara evidencia.

**Aparece en 1 clase(s):** [Clase 285 — Auditoría de seguridad](../classes/parte-14-grc-riesgo-y-cumplimiento/285-auditoria-de-seguridad/README.md).

### CRL

Lista de certificados revocados

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### Cron job

Tarea programada; si es editable y la corre root, es escalada

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### cron / systemd timer

Reejecución programada en Linux

**Aparece en 1 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md).

### Cronolocalización

Inferencia de fecha o periodo de captura.

**Aparece en 1 clase(s):** [Clase 253 — Geolocalización y análisis de imágenes](../classes/parte-12-osint-e-ingenieria-social/253-geolocalizacion-y-analisis-de-imagenes/README.md).

### Crown jewels

Activos críticos cuyo compromiso define el éxito del ejercicio

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### crt.sh

Buscador de CT usado para enumerar subdominios

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### Cryptominer

Malware que mina criptomoneda con recursos de la víctima

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### CSP

Cabecera que restringe qué scripts puede ejecutar el navegador

**Aparece en 3 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md), [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md), [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### CSP / HSTS

Cabeceras que restringen scripts y fuerzan HTTPS

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### CSPRNG

Generador apto para criptografía: impredecible hacia delante

**Aparece en 2 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md), [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### CSR

Petición de firma con la clave pública y los datos del sujeto

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### CSRF

Forzar al navegador de la víctima a hacer una acción autenticada

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### CSRF en APIs JSON

Posible si el endpoint acepta formularios o ignora el Content-Type

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### CTF — Capture The Flag

Competición de seguridad basada en retos y flags

**Claves de búsqueda normalizadas:** `capture the flag`, `ctf`.

**Relacionados:** Flag, Writeup, Jeopardy, Attack-Defense, KOTH — King of the Hill.

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### CTFtime

Directorio comunitario de eventos CTF, equipos, resultados y writeups; no es por sí mismo una ruta guiada.

**Sitio oficial:** [CTFtime](https://ctftime.org/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### CTI

Cyber Threat Intelligence: información sobre actores, campañas y TTPs

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### CTID

Center for Threat-Informed Defense, impulsor de las micro-emulaciones

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### CTR

Cifra un contador para generar keystream; convierte AES en flujo

**Aparece en 1 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md).

### Cuantificador

Nº de repeticiones (`*`, `+`, `?`, `{n,m}`)

**Aparece en 1 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md).

### Cuarta parte

Proveedor utilizado por el tercero.

**Aparece en 1 clase(s):** [Clase 284 — Gestión de riesgo de terceros y proveedores](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md).

### Cuckoo / CAPE / Any.Run

Sandboxes de análisis de malware

**Aparece en 1 clase(s):** [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### Cuerpo técnico

Sección para TI y desarrollo; hallazgos y remediación

**Aparece en 1 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md).

### Culpa a la víctima

Enfoque que atribuye el fallo a la persona e ignora controles del sistema.

**Aparece en 1 clase(s):** [Clase 256 — Fundamentos de ingeniería social](../classes/parte-12-osint-e-ingenieria-social/256-fundamentos-de-ingenieria-social/README.md).

### Curva elíptica

Conjunto de puntos que cumplen `y² = x³ + ax + b` sobre un campo finito

**Aparece en 1 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md).

### Curvas NIST (P-256…)

Estándares extendidos; parámetros de origen discutido

**Aparece en 1 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md).

### Curve25519

Curva de Bernstein con parámetros verificablemente rígidos

**Aparece en 1 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md).

### Custodia de credenciales

Responsabilidad de proteger y destruir lo extraído

**Aparece en 1 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### Cutter

GUI construida sobre rizin

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### CVD

Divulgación coordinada de vulnerabilidades.

**Aparece en 2 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md), [Clase 275 — Seguridad de dispositivos médicos](../classes/parte-13-seguridad-movil-iot-e-inalambrica/275-seguridad-de-dispositivos-medicos/README.md).

### CVE

Identificador público de una vulnerabilidad conocida

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### CVSS

Puntuación que ayuda a fijar la recompensa

**Aparece en 2 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md), [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### Cyber device

Categoría legal estadounidense definida por FD&C Act; no todo dispositivo mundial.

**Aparece en 1 clase(s):** [Clase 275 — Seguridad de dispositivos médicos](../classes/parte-13-seguridad-movil-iot-e-inalambrica/275-seguridad-de-dispositivos-medicos/README.md).

### Cyber Kill Chain

Modelo lineal de fases de intrusión (Lockheed Martin)

**Aparece en 1 clase(s):** [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### CyberChef

Herramienta web para encadenar operaciones

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### CyberDefenders

Cyber range orientado a investigaciones defensivas, SOC y DFIR.

**Sitio oficial:** [CyberDefenders](https://cyberdefenders.org/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### cyclic

Genera un patrón de De Bruijn para hallar offsets

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### cyclic -l

Calcula el offset a partir del valor en RIP

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### CyLab Security Academy

Plataforma educativa gratuita de Carnegie Mellon que continúa el ecosistema de picoCTF.

**Claves de búsqueda normalizadas:** `picoctf`, `picoctf cylab`.

**Sitio oficial:** [CyLab Security Academy](https://cylabacademy.org/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

## D

### d (exponente privado)

Inverso de `e` módulo φ(n)

**Aparece en 1 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md).

### DAI

Dynamic ARP Inspection: valida respuestas ARP contra concesiones DHCP.

**Aparece en 2 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md), [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### dangerouslySetInnerHTML

Desactiva el escape de React; punto caliente

**Aparece en 1 clase(s):** [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### Daño clínico

Consecuencia sobre paciente, diagnóstico, terapia o continuidad.

**Aparece en 1 clase(s):** [Clase 275 — Seguridad de dispositivos médicos](../classes/parte-13-seguridad-movil-iot-e-inalambrica/275-seguridad-de-dispositivos-medicos/README.md).

### DAST

Análisis dinámico de la aplicación en ejecución

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### Data

Información auxiliar confiable usada por las reglas.

**Aparece en 1 clase(s):** [Clase 244 — Políticas como código con OPA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/244-politicas-como-codigo-con-opa/README.md).

### Data flow

Seguir de dónde viene y a dónde va un valor

**Aparece en 1 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### Data lineage

Procedencia y transformaciones de datos.

**Aparece en 1 clase(s):** [Clase 293 — Envenenamiento de datos y modelos](../classes/parte-15-seguridad-de-ia-y-machine-learning/293-envenenamiento-de-datos-y-modelos/README.md).

### Data Protection class

Política que liga acceso a archivos con claves y estado del dispositivo.

**Aparece en 1 clase(s):** [Clase 263 — Seguridad de iOS: arquitectura](../classes/parte-13-seguridad-movil-iot-e-inalambrica/263-seguridad-de-ios-arquitectura/README.md).

### Data Source

Telemetría que permite observar una técnica

**Aparece en 1 clase(s):** [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### Dataset,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 360 — Capstone: incidente completo de Game Security](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/360-capstone-incidente-completo-game-security/README.md).

### Datasets

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 356 — Detección de aimbot y automatización por comportamiento](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/356-deteccion-aimbot-automatizacion-comportamiento/README.md).

### Datastore

Almacén de parámetros del módulo

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### Dato contaminado (tainted)

Valor que procede de una fuente no confiable

**Aparece en 1 clase(s):** [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Dato → información → inteligencia

Jerarquía de valor de la CTI

**Aparece en 1 clase(s):** [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md).

### Datos de sesión / flujo

Metadatos por conexión (5-tupla, bytes, duración); baratos

**Aparece en 1 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md).

### Datos de transacción

Resumen estructurado de la actividad; la aportación de Zeek a NSM

**Aparece en 2 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md), [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### Datos estadísticos

Descripción agregada de la forma del tráfico

**Aparece en 1 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md).

### Datos sensibles hallados

Se documentan, no se descargan

**Aparece en 1 clase(s):** [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### DBC

Descripción de señales y codificación de mensajes CAN.

**Aparece en 1 clase(s):** [Clase 274 — Seguridad automotriz y bus CAN](../classes/parte-13-seguridad-movil-iot-e-inalambrica/274-seguridad-automotriz-y-bus-can/README.md).

### DBIR

Verizon Data Breach Investigations Report, informe anual de brechas

**Aparece en 1 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md).

### dbnmap / dbimport

Integran el reconocimiento con la base de datos

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### DDoS-for-hire

Capacidad de denegación ofrecida a clientes; no prueba quién la contrató

**Aparece en 2 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md), [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### Dead drop resolver

Config del C2 oculta en un sitio legítimo

**Aparece en 1 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md).

### Deauth

Trama de gestión que expulsa a un cliente y fuerza reconexión

**Aparece en 1 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md).

### Debian OpenSSL

Fallo que redujo el espacio de claves a 32 768

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### Debrief

Explicación posterior que conecta señales, proceso y aprendizaje.

**Aparece en 1 clase(s):** [Clase 258 — Campañas de phishing con GoPhish](../classes/parte-12-osint-e-ingenieria-social/258-campanas-de-phishing-con-gophish/README.md).

### Decisión

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 350 — Triggerbot, macros, input automation y bots](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/350-triggerbot-macros-input-automation-bots/README.md).

### Decision log

Registro cronológico de opciones, responsables y fundamentos.

**Aparece en 1 clase(s):** [Clase 307 — Capstone: respuesta a incidentes DFIR end-to-end](../classes/parte-16-capstones-y-preparacion-de-certificaciones/307-capstone-respuesta-a-incidentes-dfir-end-to-end/README.md).

### Decode As

Forzar un disector concreto cuando el puerto no es el estándar

**Aparece en 1 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md).

### Decoder

Codifica y descodifica (URL, Base64, hex, HTML)

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### Decompilar

Reconstruir pseudo-C del código original

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### Decompiler

Vista de pseudo-C legible

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### Deconfliction

Proceso para distinguir una alerta del ejercicio de un incidente real

**Aparece en 3 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md), [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md), [Clase 305 — Capstone: operación Red Team end-to-end](../classes/parte-16-capstones-y-preparacion-de-certificaciones/305-capstone-operacion-red-team-end-to-end/README.md).

### Deep link

URI que puede activar una ruta o componente de la aplicación.

**Aparece en 1 clase(s):** [Clase 262 — Pentest de aplicaciones Android](../classes/parte-13-seguridad-movil-iot-e-inalambrica/262-pentest-de-aplicaciones-android/README.md).

### Deepfake

Medio sintético o manipulado que imita atributos humanos.

**Aparece en 1 clase(s):** [Clase 299 — IA ofensiva y deepfakes](../classes/parte-15-seguridad-de-ia-y-machine-learning/299-ia-ofensiva-y-deepfakes/README.md).

### Defensa

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 353 — Arquitecturas Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/353-arquitecturas-anticheat/README.md).

### Defensa en profundidad

AEAD + error único + tiempo constante + límites

**Aparece en 1 clase(s):** [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### Defensa por vector

Cada mecanismo se protege de forma específica

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### defusedxml

Librería Python segura frente a XXE

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### DEK

Clave de datos que cifra el contenido; se guarda cifrada

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### Demodulación

Recuperación de símbolos o información desde una portadora modulada.

**Aparece en 1 clase(s):** [Clase 269 — Radio definida por software (SDR)](../classes/parte-13-seguridad-movil-iot-e-inalambrica/269-radio-definida-por-software-sdr/README.md).

### Demostración

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 347 — Rendering, visibilidad, occlusion y wallhack](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/347-rendering-visibilidad-occlusion-wallhack/README.md).

### Denegar por defecto

El acceso se concede explícitamente, nunca se asume

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### DEP / NX

Marca los datos como no ejecutables (bit NX)

**Aparece en 3 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md), [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md), [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md).

### Dependencia del motor

Las funciones OOB y de tiempo varían por base de datos

**Aparece en 2 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md), [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### Dependencia externa

Servicio de un tercero que soporta una función de la organización.

**Aparece en 1 clase(s):** [Clase 251 — OSINT de empresas y dominios](../classes/parte-12-osint-e-ingenieria-social/251-osint-de-empresas-y-dominios/README.md).

### Dependencia transitiva

Componente incorporado por otra dependencia, no declarado directamente.

**Aparece en 1 clase(s):** [Clase 240 — SCA: dependencias y riesgo de terceros](../classes/parte-11-devsecops-y-seguridad-del-sdlc/240-sca-dependencias-y-riesgo-de-terceros/README.md).

### Depurar cadenas ROP

Avanzar con stepi viendo cada salto y registro

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### Derrota a NX

Reutiliza código ya ejecutable; no inyecta nada

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### DES

Cifrado de los setenta, endurecido contra diferencial en secreto

**Aparece en 1 clase(s):** [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### Desarrollo de exploits

Convertir un crash en un exploit fiable

**Aparece en 1 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### Descarrilamiento

Interpretar datos como instrucciones

**Aparece en 1 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### Descarte (drop)

Paquete perdido por saturación del buffer de captura

**Aparece en 1 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### Descifrador gratuito

Existe solo si el ransomware tuvo un fallo

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Descontextualización

Uso de material auténtico con fecha, lugar o significado incorrecto.

**Aparece en 1 clase(s):** [Clase 252 — OSINT en redes sociales](../classes/parte-12-osint-e-ingenieria-social/252-osint-en-redes-sociales/README.md).

### Descubrimiento de hosts

Determinar qué direcciones están vivas (`-sn`)

**Aparece en 1 clase(s):** [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### Descubrimiento de parámetros

Encontrar campos de entrada no documentados

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### Descubrimiento de vulnerabilidades

Encontrar fallos analizando el código

**Aparece en 1 clase(s):** [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Desempaquetado en memoria

El binario revela su código real al ejecutarse

**Aparece en 1 clase(s):** [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md).

### Desensamblado lineal

Recorre los bytes en orden; se descarrila con datos

**Aparece en 1 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### Desensamblado recursivo

Sigue el flujo de control; pierde saltos indirectos

**Aparece en 1 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### Desensamblar

Mostrar el ensamblador del binario

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### Deserialización

Reconstruir el objeto a partir de los bytes

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### Deserialización insegura

Reconstruir datos del usuario que ejecutan código

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### Deshabilitar AMSI

Intento del malware de cegar la inspección; es un IOC

**Aparece en 1 clase(s):** [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### Deshabilitar DTD

La defensa: apagar entidades externas y DOCTYPE

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### Desofuscación en lote

Aplicar la rutina de descifrado a muchas cadenas

**Aparece en 1 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### Desofuscación segura

Imprimir en vez de ejecutar cada capa

**Aparece en 1 clase(s):** [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### Detección de funciones

Reconocer límites de función en un binario stripped

**Aparece en 1 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### Detección de patrones

Fallos masivos por IP o accesos geográficamente imposibles

**Aparece en 1 clase(s):** [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md).

### Detección de versión (-sV)

Identifica servicio y versión exactos

**Aparece en 1 clase(s):** [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### Detección esperada

Evento que un TTP debería generar y quién debería verlo

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### Detección por comportamiento

Basada en qué se hace, no en qué fichero hay

**Aparece en 1 clase(s):** [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### Detección por familiaridad

El AV caza patrones conocidos, no "maldad"

**Aparece en 1 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### Detección por indicadores

Reglas y firmas sobre lo conocido; reactiva

**Aparece en 1 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md).

### Detección temprana

Cazar la intrusión antes del cifrado

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Detonar

Ejecutar la muestra para observar su comportamiento

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### DEX

Bytecode ejecutado por Android Runtime.

**Aparece en 1 clase(s):** [Clase 265 — Ingeniería inversa de aplicaciones móviles](../classes/parte-13-seguridad-movil-iot-e-inalambrica/265-ingenieria-inversa-de-aplicaciones-moviles/README.md).

### DFD

Representación de entidades, procesos, almacenes y flujos de datos.

**Aparece en 1 clase(s):** [Clase 237 — Modelado de amenazas: STRIDE y DREAD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/237-modelado-de-amenazas-stride-y-dread/README.md).

### DFIR — Digital Forensics and Incident Response

Disciplina que combina preservación y análisis forense con contención, erradicación, recuperación y aprendizaje de incidentes.

**Claves de búsqueda normalizadas:** `dfir`.

**Relacionados:** Triage, IOC — Indicador de compromiso, RCA — Análisis de causa raíz.

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### DGA

Algoritmo que genera miles de dominios por día

**Aparece en 1 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md).

### DH estático

Secreto fijo reutilizado; sin forward secrecy

**Aparece en 1 clase(s):** [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### DHCP

Protocolo de asignación automática de direcciones y parámetros de red.

**Aparece en 1 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md).

### DHCP snooping

Control de switch que solo confía en puertos DHCP autorizados.

**Aparece en 1 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md).

### DHE / ECDHE

Diffie-Hellman efímero: par nuevo por sesión

**Aparece en 1 clase(s):** [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### Diamond Model

Análisis de intrusión por adversario, capacidad, infraestructura y víctima

**Aparece en 2 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md), [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md).

### Diccionario

Tokens del formato que el fuzzer combina

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### dict

Mapa clave-valor con acceso rápido.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### DIE / PEiD

Herramientas que identifican el packer

**Aparece en 1 clase(s):** [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Diferencias Linux/Windows

Comandos y sintaxis distintos según el SO

**Aparece en 1 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### Diffie-Hellman

Acuerdo de clave secreta mediante mensajes públicos

**Aparece en 1 clase(s):** [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### Digest

Identificador criptográfico del contenido exacto de una imagen.

**Aparece en 2 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md), [Clase 243 — Imágenes y contenedores seguros en el pipeline](../classes/parte-11-devsecops-y-seguridad-del-sdlc/243-imagenes-y-contenedores-seguros-en-el-pipeline/README.md).

### DigiNotar

CA comprometida en 2011; caso canónico del fallo del modelo

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### Dirección

Necesita impacto de negocio y riesgo

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### Dirección de red

Primera dirección del bloque; identifica el segmento.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### Dirección de retorno

Valor que `ret` carga en RIP; objetivo del overflow

**Aparece en 2 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md), [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### Dirección privada

Dirección que rota para reducir seguimiento, con límites.

**Aparece en 1 clase(s):** [Clase 271 — Seguridad de Bluetooth y BLE](../classes/parte-13-seguridad-movil-iot-e-inalambrica/271-seguridad-de-bluetooth-y-ble/README.md).

### Directorio .git expuesto

Permite descargar el código fuente completo

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### Dirigido por eventos

Arquitectura en que cada actividad dispara un evento programable

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### Dirigido por objetivos

Buscar responder una pregunta, no leer todo

**Aparece en 1 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### Disclosure

Revelación no autorizada de información (rompe confidencialidad)

**Aparece en 1 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md).

### Disector

Módulo que interpreta los bytes de un protocolo como campos con nombre

**Aparece en 1 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md).

### Diseño seguro

Modelar amenazas antes de programar (A04)

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### Distroless

Imagen de runtime sin distribución de propósito general; no implica invulnerabilidad.

**Aparece en 1 clase(s):** [Clase 243 — Imágenes y contenedores seguros en el pipeline](../classes/parte-11-devsecops-y-seguridad-del-sdlc/243-imagenes-y-contenedores-seguros-en-el-pipeline/README.md).

### Divulgación responsable

Reportar en privado y dar tiempo a corregir

**Aparece en 1 clase(s):** [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### DKIM

Firma criptográfica del correo que prueba que no se alteró en tránsito

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### DKOM

Modificar directamente las estructuras del kernel

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### DLL hijacking

Cargar una DLL maliciosa desde una ubicación escribible

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### DLP

Inspección de contenido para detectar datos sensibles

**Aparece en 1 clase(s):** [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md).

### DMARC

Política que indica al receptor qué hacer si SPF o DKIM fallan

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### DMZ

Zona aislada para los servicios expuestos a Internet

**Aparece en 1 clase(s):** [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md).

### DNAT

Reescribe la dirección de destino (*port forwarding*)

**Aparece en 1 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md).

### DNS

Servicio que traduce nombres de dominio a direcciones IP.

**Aparece en 1 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md).

### DNS rebinding

Un dominio que resuelve a una IP interna

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### DNS tunneling

Codificar datos en los nombres para crear un canal encubierto

**Aparece en 2 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md), [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md).

### DNSKEY / RRSIG / DS

Clave, firma y enlace de confianza de DNSSEC

**Aparece en 1 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md).

### DNSSEC

Firma de registros: aporta integridad y autenticidad, no confidencialidad

**Aparece en 2 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md), [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md).

### Doble control

Participación de dos autorizadores en una acción crítica.

**Aparece en 1 clase(s):** [Clase 259 — Defensa contra la ingeniería social](../classes/parte-12-osint-e-ingenieria-social/259-defensa-contra-la-ingenieria-social/README.md).

### Doble extensión

`archivo.php.jpg` en servidores mal configurados

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### Doble extorsión

Exfiltrar y amenazar con publicar además de cifrar

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Doble pivote

Encadenar dos saltos para redes doblemente segmentadas

**Aparece en 1 clase(s):** [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### Dockerfile

Receta declarativa para construir una imagen

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### Documento malicioso (maldoc)

Documento que contiene y ejecuta código

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### DoH

DNS over HTTPS; cifra y se mezcla con el tráfico web del 443

**Aparece en 1 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md).

### DoH / DoT

DNS cifrado sobre HTTPS o TLS para proteger la confidencialidad.

**Aparece en 1 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md).

### DOM Invader

Herramienta de Burp para sources, sinks y gadgets

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### DOM XSS

Vulnerabilidad enteramente en el JavaScript del cliente

**Aparece en 1 clase(s):** [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### Domain fronting

Ocultar el destino real tras el SNI de un CDN legítimo

**Aparece en 1 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### Dominio recién registrado

Señal frecuente de infraestructura maliciosa

**Aparece en 1 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md).

### DOMPurify

Librería estándar de sanitización de HTML

**Aparece en 1 clase(s):** [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### DORA

Discover, Offer, Request, Acknowledge: el intercambio DHCP.

**Aparece en 1 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md).

### DoS / DDoS

Denegación de servicio (distribuida): ataque contra la disponibilidad

**Aparece en 1 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md).

### DOS header / MZ

Cabecera inicial con los bytes mágicos `MZ`

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### DoT

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 2 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md), [Clase 348 — Matemática de un aimbot](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/348-matematica-aimbot/README.md).

### Double free

Liberar el mismo chunk dos veces

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### Double tagging

Insertar dos etiquetas 802.1Q para alcanzar otra VLAN

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### Downgrade

Forzar un protocolo o cifrado más débil

**Aparece en 2 clase(s):** [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md), [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### Download cradle

Descarga y ejecución en memoria de un payload, típica de PowerShell

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### Downloader / dropper

Descarga / deposita la carga maliciosa real

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### DPIA

Evaluación estructurada de impacto de privacidad según aplicabilidad.

**Aparece en 1 clase(s):** [Clase 289 — Privacidad y protección de datos](../classes/parte-14-grc-riesgo-y-cumplimiento/289-privacidad-y-proteccion-de-datos/README.md).

### DRBG

Generador determinista normalizado (NIST SP 800-90A)

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### Drift,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 358 — Machine Learning aplicado a Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/358-machine-learning-aplicado-anticheat/README.md).

### Driver

Mayor fuente de bugs de kernel

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### DROP vs. REJECT

Descartar en silencio o responder con un error explícito

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### DSE / HVCI

Firma de drivers / integridad de código por hipervisor

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### DTD

Definición de tipo de documento; donde se declaran entidades

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### DTD externa maliciosa

Cargada del servidor del atacante para exfiltrar

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### DTP

Protocolo de negociación de trunk; conviene desactivarlo

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### DualECDRBG

Generador retirado por sospecha de puerta trasera

**Aparece en 1 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md).

### Dueño de riesgo

Persona con autoridad para tratar o aceptar un riesgo dentro de límites.

**Aparece en 1 clase(s):** [Clase 276 — Gobernanza de la seguridad de la información](../classes/parte-14-grc-riesgo-y-cumplimiento/276-gobernanza-de-la-seguridad-de-la-informacion/README.md).

### Dump de memoria

Capturar el código ya desempaquetado

**Aparece en 2 clase(s):** [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md), [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Dup ACK

ACK repetido que señala un hueco en la secuencia recibida

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### Duplicado

Bug ya reportado; no se recompensa

**Aparece en 1 clase(s):** [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### DV / OV / EV

Niveles de validación: dominio, organización, extendida

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### DVWA

Damn Vulnerable Web Application, lab de práctica

**Aparece en 2 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md), [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### Dynamic forwarding (-D)

Proxy SOCKS: acceso a toda la subred por un túnel

**Aparece en 1 clase(s):** [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

## E

### e (exponente público)

Coprimo con φ(n); habitualmente 65537

**Aparece en 1 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md).

### ECB

Cada bloque por separado; filtra la estructura. No usar

**Aparece en 1 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md).

### ECC

Criptografía de curva elíptica; misma seguridad con claves más pequeñas

**Aparece en 1 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md).

### ECDLP

Hallar `k` conocidos `G` y `k·G`; base de la seguridad

**Aparece en 1 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md).

### ECDSA

Firma sobre curvas NIST; el nonce filtrado revela la clave

**Aparece en 2 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md), [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### Economía,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 341 — Introducción a Game Security y modelo de amenazas](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/341-introduccion-game-security-modelo-amenazas/README.md).

### ECS

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 342 — Arquitectura de videojuegos desde la perspectiva de seguridad](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/342-arquitectura-videojuegos-perspectiva-seguridad/README.md).

### ECU

Unidad electrónica que controla una función vehicular.

**Aparece en 1 clase(s):** [Clase 274 — Seguridad automotriz y bus CAN](../classes/parte-13-seguridad-movil-iot-e-inalambrica/274-seguridad-automotriz-y-bus-can/README.md).

### Ed25519

Firma con nonce determinista; elimina ese riesgo

**Aparece en 2 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md), [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### Edición Community

Versión gratuita con Intruder limitado en velocidad

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### EDR

Endpoint Detection and Response: detección y respuesta en el host

**Aparece en 3 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md), [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md), [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### Efecto avalancha

Un cambio mínimo en la entrada altera medio hash de salida

**Aparece en 2 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md), [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md).

### Efecto físico

Cambio sobre entorno o seguridad causado por el producto.

**Aparece en 1 clase(s):** [Clase 266 — Seguridad de IoT: panorama y superficie de ataque](../classes/parte-13-seguridad-movil-iot-e-inalambrica/266-seguridad-de-iot-panorama-y-superficie-de-ataque/README.md).

### Egress filtering

Restringir el tráfico saliente; la defensa más eficaz

**Aparece en 1 clase(s):** [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md).

### Ejecución en memoria

No escribe en disco; reduce la huella forense

**Aparece en 2 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md), [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### Elegibilidad

Experiencia u otros requisitos para obtener una credencial.

**Aparece en 1 clase(s):** [Clase 290 — Certificaciones y desarrollo de carrera](../classes/parte-14-grc-riesgo-y-cumplimiento/290-certificaciones-y-desarrollo-de-carrera/README.md).

### ELF

Formato de ejecutable de Linux

**Aparece en 2 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md), [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### ELF / ROP / DynELF

Instrumental avanzado de pwntools

**Aparece en 1 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### elf.symbols / elf.got

pwntools: direcciones de funciones y GOT

**Aparece en 1 clase(s):** [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md).

### Emparejamiento exploit-vulnerabilidad

El exploit debe coincidir con la versión y arquitectura exactas

**Aparece en 1 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md).

### Emulación

Ejecutar código en un CPU virtual, con control y sin riesgo

**Aparece en 2 clase(s):** [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md), [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Emulación incompleta

No toda la API está implementada

**Aparece en 1 clase(s):** [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Emulación parcial

Ejecución aproximada que no reproduce todo el hardware.

**Aparece en 1 clase(s):** [Clase 267 — Hacking de firmware](../classes/parte-13-seguridad-movil-iot-e-inalambrica/267-hacking-de-firmware/README.md).

### Emulación vs ejecución vs depuración

Simulada vs real vs manual

**Aparece en 1 clase(s):** [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Emulador / Frida

Entorno y herramienta de análisis dinámico

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### Emular un fragmento

Ejecutar una rutina aislada (descifrado, DGA)

**Aparece en 1 clase(s):** [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Emulation Library

Colección pública de planes validados por MITRE/CTID

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### Emulation Plan

Documento paso a paso que reproduce a un actor

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### Encadenar primitivas

Combinar capacidades para escalar el exploit

**Aparece en 1 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### Encapsulación

Añadir la cabecera de cada capa al bajar la pila

**Aparece en 1 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md).

### encode / decode

Conversión entre texto y bytes eligiendo codificación.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### EncodedCommand

Comando PowerShell codificado en Base64

**Aparece en 1 clase(s):** [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### Encoder (-e, -i)

Transforma el payload; **no** ofusca contra AV moderno

**Aparece en 1 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### Encoder / nop

Transforma y rellena payloads

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### Encrypt-and-MAC

Orden que puede filtrar información del texto claro

**Aparece en 1 clase(s):** [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

### Encrypt-then-MAC

Cifrar y luego autenticar el cifrado; la composición segura

**Aparece en 2 clase(s):** [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md), [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### Endianness

Orden de bytes en memoria (x86 = little-endian)

**Aparece en 2 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md), [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### Endpoints

Estadística por host individual; delata escaneos

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### Endurecer la VM

Hacer que la VM parezca un sistema real

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### Enigma

Máquina de rotores alemana; rota por fallos de operación

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### Ensamblador

Representación legible del código máquina

**Aparece en 1 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md).

### Entidad externa

Entidad que apunta a un fichero o URL

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### Entidad XML

Variable definida en la DTD que se expande en el cuerpo

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### Entidades

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 346 — Información expuesta, radar, ESP y world-to-screen](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/346-informacion-expuesta-radar-esp-world-to-screen/README.md).

### Entitlement

Capacidad firmada que autoriza acceso a determinados servicios.

**Aparece en 1 clase(s):** [Clase 263 — Seguridad de iOS: arquitectura](../classes/parte-13-seguridad-movil-iot-e-inalambrica/263-seguridad-de-ios-arquitectura/README.md).

### Entity resolution

Evaluación de si registros representan la misma entidad.

**Aparece en 1 clase(s):** [Clase 336 — OSINT y auditoría web con agentes de IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/336-osint-y-auditoria-web-con-agentes-de-ia/README.md).

### Entrada como dato

La defensa: pasar la entrada a una plantilla fija

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### Entregable

Producto de cada fase; el informe es el final

**Aparece en 1 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### Entregables

Formatos adaptados a cada destinatario

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### Entropía

Medida estadística usada como señal, no prueba de que un valor sea secreto.

**Aparece en 4 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md), [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md), [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md), [Clase 241 — Secretos en el código y pre-commit hooks](../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md).

### Entropía anómala

Indicio de que un plano de bits contiene datos cifrados

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### Entropía del ID

Longitud y aleatoriedad; impide adivinarlo

**Aparece en 1 clase(s):** [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### Entropía del nombre

Aleatoriedad de un subdominio; indicio de tunneling

**Aparece en 1 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md).

### Entry point

Dirección donde empieza la ejecución

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### enum4linux / smbclient

Herramientas de enumeración y navegación SMB

**Aparece en 1 clase(s):** [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md).

### Enumeración

Extraer información detallada de un servicio ya identificado

**Claves de búsqueda normalizadas:** `enumeration`.

**Aparece en 3 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md), [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md), [Clase 302 — Preparación OSCP: mentalidad Try Harder](../classes/parte-16-capstones-y-preparacion-de-certificaciones/302-preparacion-oscp-mentalidad-try-harder/README.md).

### Enumeración de endpoints

Descubrir rutas por docs, versiones y JS

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### Enumeración de esquema

Descubrir tablas y columnas existentes

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### Enumeración de ficheros

Selección por extensión de qué cifrar

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Enumeración de subdominios

Descubre entornos dev/staging/api peor protegidos

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### Enumeración de usuarios

Descubrir qué cuentas existen por respuestas o tiempos

**Aparece en 1 clase(s):** [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### Enumeración post-explotación

Inspeccionar el sistema en busca de vectores

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### Envelope encryption

Cifrar datos con la DEK y la DEK con la KEK

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### Envío automático de cookies

El navegador adjunta la cookie sin importar el origen

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### EPSS

Estimación probabilística de explotación; no mide impacto propio.

**Aparece en 1 clase(s):** [Clase 240 — SCA: dependencias y riesgo de terceros](../classes/parte-11-devsecops-y-seguridad-del-sdlc/240-sca-dependencias-y-riesgo-de-terceros/README.md).

### Equivalencia de tamaños

ECC 256 bits ≈ RSA 3072 bits

**Aparece en 1 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md).

### ERE

Extended Regular Expressions (activadas con `grep -E`)

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### Error aritmético

Bug de enteros que habilita otra vulnerabilidad

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Error genérico

Respuesta única ante fallo, para no dar información

**Aparece en 2 clase(s):** [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md), [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### Escalada a RCE

Navegar a objetos del lenguaje hasta ejecutar comandos

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### Escalada de privilegios

Pasar de un usuario limitado a root

**Claves de búsqueda normalizadas:** `privesc`, `privilege escalation`.

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### Escalada horizontal

Acceder a datos de otro usuario del mismo nivel

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### Escalada vertical

Acceder a funciones de un nivel superior

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### Escaneo activo

Pruebas que modifican deliberadamente entradas y pueden alterar el objetivo.

**Aparece en 2 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md), [Clase 239 — DAST: análisis dinámico de aplicaciones](../classes/parte-11-devsecops-y-seguridad-del-sdlc/239-dast-analisis-dinamico-de-aplicaciones/README.md).

### Escaneo autenticado

Con credenciales; audita desde dentro, menos falsos positivos

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### Escaneo interno

Sondear puertos internos por tiempos o errores

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### Escaneo intrusivo

El que puede alterar datos o disparar acciones

**Aparece en 1 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md).

### Escaneo no autenticado

Sin credenciales; vista de atacante externo

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### Escaneo pasivo

Análisis del tráfico observado sin enviar cargas de ataque.

**Aparece en 2 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md), [Clase 239 — DAST: análisis dinámico de aplicaciones](../classes/parte-11-devsecops-y-seguridad-del-sdlc/239-dast-analisis-dinamico-de-aplicaciones/README.md).

### Escaneo UDP (-sU)

Cubre DNS, SNMP, NTP; lento y ambiguo

**Aparece en 1 clase(s):** [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### Escáner automático

Sistema que puede abrir enlaces y contaminar métricas.

**Aparece en 1 clase(s):** [Clase 258 — Campañas de phishing con GoPhish](../classes/parte-12-osint-e-ingenieria-social/258-campanas-de-phishing-con-gophish/README.md).

### Escáner de vulnerabilidades

Herramienta que compara el objetivo con firmas conocidas

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### Escape

Ruptura del aislamiento del contenedor hacia el host

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### Escape de contexto

Cerrar comillas o etiquetas para salir del contexto

**Aparece en 1 clase(s):** [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md).

### Escape por defecto

React/Angular/Vue codifican lo que insertan

**Aparece en 1 clase(s):** [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### Escenario de amenaza

Cadena concreta de precondición, acción, activo e impacto.

**Aparece en 1 clase(s):** [Clase 237 — Modelado de amenazas: STRIDE y DREAD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/237-modelado-de-amenazas-stride-y-dread/README.md).

### Escenario de pérdida

Cadena concreta que conecta amenaza, activo y consecuencia.

**Aparece en 1 clase(s):** [Clase 277 — Gestión de riesgos: cuantitativa y cualitativa](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md).

### Escenarios

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 357 — Estadística, anomalías y falsos positivos](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/357-estadistica-anomalias-falsos-positivos/README.md).

### Escritura arbitraria

Escribir cualquier valor en cualquier dirección

**Aparece en 3 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md), [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md), [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### Escritura fuera de límites

El exceso sobrescribe memoria adyacente

**Aparece en 1 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md).

### ESP / AH

Cifrado+autenticación / solo autenticación en IPsec

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### Especificador

`%x`, `%p`, `%s`, `%n` de la familia printf

**Aparece en 1 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### Esquema

Todos los tipos, campos y operaciones disponibles

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### Esquema alternativo

`file://`, `gopher://`, `dict://` amplían el ataque

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### Esquema de validación

Mongoose u otros que fuerzan el tipo de cada campo

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### Esquema híbrido

AES por fichero + RSA para la clave AES

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Estabilidad de sesión

Evitar perder el acceso si el proceso original muere

**Aparece en 1 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### ESTABLISHED

Paquete perteneciente a una conexión ya aceptada

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### Estado,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 2 clase(s):** [Clase 343 — Taxonomía técnica de cheats](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/343-taxonomia-tecnica-cheats/README.md), [Clase 344 — Estado del juego, memoria y manipulación controlada](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/344-estado-juego-memoria-manipulacion-controlada/README.md).

### Estado interno

Datos del generador cuyo conocimiento predice las salidas

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### Estándar

Requisito obligatorio y verificable.

**Aparece en 1 clase(s):** [Clase 282 — Políticas, estándares y procedimientos](../classes/parte-14-grc-riesgo-y-cumplimiento/282-politicas-estandares-y-procedimientos/README.md).

### Esteganografía

Ocultar la **existencia** del mensaje

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### Estego-objeto

Portador con la carga ya oculta dentro

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### Estegoanálisis

Detección de contenido oculto

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### ET Open

Conjunto de reglas abierto de Emerging Threats

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### ETW

Event Tracing for Windows; telemetría profunda

**Aparece en 1 clase(s):** [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### eval / setTimeout

Sinks que interpretan JavaScript

**Aparece en 1 clase(s):** [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### Evaluación

Experimento reproducible ligado a un riesgo y criterio.

**Aparece en 10 clase(s):** [Clase 291 — Introducción a la seguridad de IA y ML](../classes/parte-15-seguridad-de-ia-y-machine-learning/291-introduccion-a-la-seguridad-de-ia-y-ml/README.md), [Clase 292 — Ataques adversariales a modelos](../classes/parte-15-seguridad-de-ia-y-machine-learning/292-ataques-adversariales-a-modelos/README.md), [Clase 293 — Envenenamiento de datos y modelos](../classes/parte-15-seguridad-de-ia-y-machine-learning/293-envenenamiento-de-datos-y-modelos/README.md), [Clase 294 — Robo y extracción de modelos](../classes/parte-15-seguridad-de-ia-y-machine-learning/294-robo-y-extraccion-de-modelos/README.md), [Clase 295 — OWASP Top 10 para aplicaciones con LLM](../classes/parte-15-seguridad-de-ia-y-machine-learning/295-owasp-top-10-para-aplicaciones-con-llm/README.md), [Clase 296 — Prompt injection y jailbreaks](../classes/parte-15-seguridad-de-ia-y-machine-learning/296-prompt-injection-y-jailbreaks/README.md), [Clase 297 — Seguridad de aplicaciones con LLM: RAG y agentes](../classes/parte-15-seguridad-de-ia-y-machine-learning/297-seguridad-de-aplicaciones-con-llm-rag-y-agentes/README.md), [Clase 298 — IA aplicada a la defensa: detección y SOC](../classes/parte-15-seguridad-de-ia-y-machine-learning/298-ia-aplicada-a-la-defensa-deteccion-y-soc/README.md), [Clase 299 — IA ofensiva y deepfakes](../classes/parte-15-seguridad-de-ia-y-machine-learning/299-ia-ofensiva-y-deepfakes/README.md), [Clase 300 — Gobernanza y ética de la IA segura](../classes/parte-15-seguridad-de-ia-y-machine-learning/300-gobernanza-y-etica-de-la-ia-segura/README.md).

### Evasión de defensas

Deshabilitar AV, borrar logs, detectar análisis

**Aparece en 1 clase(s):** [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### Evasión de filtros

Payloads alternativos que saltan el filtro

**Aparece en 1 clase(s):** [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md).

### Evasión de rate limiting

Rotar IPs, spraying, o atacar la API sin límite

**Aparece en 1 clase(s):** [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### Evasión de WAF

Codificar el payload para no coincidir con sus firmas

**Aparece en 1 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### Evasión por diseño

No hay fichero que escanear

**Aparece en 1 clase(s):** [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### EVE JSON

Salida estructurada de Suricata: alertas y transacciones, una por línea

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### event.origin

Origen del mensaje; hay que validarlo siempre

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### Evento

Señal que emite el motor (conexión, petición HTTP, handshake TLS…)

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### Evento 4104

Registro que contiene el bloque de script ejecutado

**Aparece en 1 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md).

### Evento privilegiado

Disparador cuyo token o secretos tienen más autoridad que la entrada evaluada.

**Aparece en 1 clase(s):** [Clase 242 — Seguridad en pipelines CI/CD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/242-seguridad-en-pipelines-ci-cd/README.md).

### Evidence pointer

Referencia estable al artefacto original que sustenta una frase.

**Aparece en 1 clase(s):** [Clase 337 — IA para el lado defensivo: SOC, triaje y forense](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/337-ia-para-el-lado-defensivo-soc-triaje-y-forense/README.md).

### Evidencia

Información cuya procedencia y relación con un criterio pueden revisarse.

**Aparece en 31 clase(s):** [Clase 301 — Roadmap de certificaciones: CompTIA, OSCP, CISSP y más](../classes/parte-16-capstones-y-preparacion-de-certificaciones/301-roadmap-de-certificaciones-comptia-oscp-cissp-y-mas/README.md), [Clase 302 — Preparación OSCP: mentalidad Try Harder](../classes/parte-16-capstones-y-preparacion-de-certificaciones/302-preparacion-oscp-mentalidad-try-harder/README.md), [Clase 303 — Capstone: laboratorio completo de pentest](../classes/parte-16-capstones-y-preparacion-de-certificaciones/303-capstone-laboratorio-completo-de-pentest/README.md), [Clase 304 — Preparación CISSP: los 8 dominios](../classes/parte-16-capstones-y-preparacion-de-certificaciones/304-preparacion-cissp-los-8-dominios/README.md), [Clase 305 — Capstone: operación Red Team end-to-end](../classes/parte-16-capstones-y-preparacion-de-certificaciones/305-capstone-operacion-red-team-end-to-end/README.md), [Clase 306 — Capstone: detección Blue Team end-to-end](../classes/parte-16-capstones-y-preparacion-de-certificaciones/306-capstone-deteccion-blue-team-end-to-end/README.md), [Clase 307 — Capstone: respuesta a incidentes DFIR end-to-end](../classes/parte-16-capstones-y-preparacion-de-certificaciones/307-capstone-respuesta-a-incidentes-dfir-end-to-end/README.md), [Clase 308 — Capstone: campaña de bug bounty](../classes/parte-16-capstones-y-preparacion-de-certificaciones/308-capstone-campana-de-bug-bounty/README.md), [Clase 309 — Construcción de portafolio y home lab permanente](../classes/parte-16-capstones-y-preparacion-de-certificaciones/309-construccion-de-portafolio-y-home-lab-permanente/README.md), [Clase 310 — Plan de aprendizaje continuo y comunidad](../classes/parte-16-capstones-y-preparacion-de-certificaciones/310-plan-de-aprendizaje-continuo-y-comunidad/README.md) y 21 más.

### Evidencia con marca de tiempo

Registro del recon exigido por el método

**Aparece en 1 clase(s):** [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### Evidencia reproducible

Registro de la orden exacta que produjo cada hallazgo

**Aparece en 2 clase(s):** [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md), [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md).

### Evil twin

AP falso que imita un SSID legítimo para captar clientes

**Aparece en 2 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md), [Clase 272 — Ataques WiFi avanzados: Evil Twin y PMKID](../classes/parte-13-seguridad-movil-iot-e-inalambrica/272-ataques-wifi-avanzados-evil-twin-y-pmkid/README.md).

### Excepción

Error (acceso inválido, división por cero) que dispara el manejo

**Aparece en 2 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md), [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### Exclusión

Circunstancia que la póliza no cubre.

**Aparece en 1 clase(s):** [Clase 288 — Seguros cibernéticos](../classes/parte-14-grc-riesgo-y-cumplimiento/288-seguros-ciberneticos/README.md).

### Exclusiones

Dominios o técnicas explícitamente prohibidos

**Aparece en 1 clase(s):** [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### execFile / subprocess

APIs que separan programa y argumentos

**Aparece en 1 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### execstack

Marca la pila como ejecutable para probar shellcode

**Aparece en 1 clase(s):** [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### Execution Policy

Ajuste que limita la ejecución de scripts (no es seguridad)

**Aparece en 1 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md).

### execve

Syscall que reemplaza el proceso por otro (`/bin/sh`)

**Aparece en 1 clase(s):** [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### Exfiltración

Salida anómala de datos hacia un destino externo

**Aparece en 2 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md), [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md).

### Exfiltración por DNS

Sacar datos usando consultas DNS que casi nadie bloquea

**Aparece en 2 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md), [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md).

### EXIF

Metadatos de captura que pueden faltar o modificarse.

**Aparece en 1 clase(s):** [Clase 253 — Geolocalización y análisis de imágenes](../classes/parte-12-osint-e-ingenieria-social/253-geolocalizacion-y-analisis-de-imagenes/README.md).

### Exit plan

Ruta probada para terminar relación y recuperar capacidad.

**Aparece en 1 clase(s):** [Clase 284 — Gestión de riesgo de terceros y proveedores](../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md).

### exp / iss / aud

Claims que hay que validar además de la firma

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### Expert Information

Anomalías detectadas por Wireshark, agrupadas por severidad

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### Expiración

Caducidad por inactividad y por tiempo absoluto

**Aparece en 1 clase(s):** [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### exploit -j

Lanza el handler como job en segundo plano

**Aparece en 1 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md).

### exploit/multi/handler

Listener que debe coincidir con el payload generado

**Aparece en 1 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### Exploit suggester

Módulo que propone rutas de escalada para el objetivo

**Aparece en 1 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### Explotación

Módulo que aprovecha una vulnerabilidad para lograr ejecución

**Claves de búsqueda normalizadas:** `exploit`, `exploitation`.

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### Export Directory

Funciones que ofrece una DLL

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### Exportador

Dispositivo que observa el tráfico y emite los registros de flujo

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### Exposición

Servicio accesible desde una posición de red determinada.

**Aparece en 1 clase(s):** [Clase 254 — OSINT técnico: Shodan y Censys](../classes/parte-12-osint-e-ingenieria-social/254-osint-tecnico-shodan-y-censys/README.md).

### Exposición excesiva de datos

La API devuelve más campos de los que la UI muestra

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### Expresión regular

Patrón flexible en la regla

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Extensión de longitud

Extender un hash con secreto sin conocer el secreto

**Aparece en 2 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md), [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

### Extracción carácter a carácter

Reconstruir el dato preguntando bit a bit

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### Extracción de configuración

Recuperar dominios y claves embebidos en la muestra

**Aparece en 2 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md), [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Extracción de IOCs

URLs, comandos y hashes obtenidos del análisis

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### Extractor de configuración

Script que localiza y descifra el bloque de config

**Aparece en 2 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md), [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

## F

### Factor de coste

Parámetro que encarece cada intento; se sube con el tiempo

**Aparece en 1 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md).

### Fail closed

Comportamiento que niega la operación cuando falta validación.

**Aparece en 1 clase(s):** [Clase 339 — Riesgos, guardrails, OPSEC y ética del hacking con IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/339-riesgos-guardrails-opsec-y-etica-del-hacking-con-ia/README.md).

### Fallo de lógica

Abuso permitido por la lógica; el código funciona "bien"

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### False flag

Pista plantada para desviar la atribución

**Aparece en 1 clase(s):** [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md).

### Falsificación de tag

Consecuencia de repetir nonce en GCM: permite escribir

**Aparece en 1 clase(s):** [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### Falso negativo de descubrimiento

Host activo descartado por no responder; se corrige con `-Pn`

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### Falso positivo

Hallazgo reportado que no se sostiene al verificarlo

**Aparece en 4 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md), [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md), [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md), [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Falso positivo / negativo

Alerta falsa / bug real no detectado

**Aparece en 1 clase(s):** [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Familia / variante / campaña

Linaje / versión / operación concreta

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### Fan-in / fan-out

Concentración hacia un destino / dispersión desde un origen

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### Fase

Etapa del plan que agrupa TTPs con una meta común

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### Fases de Nmap

Objetivos → descubrimiento → DNS → puertos → versión/OS → NSE

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### fastbins

Listas LIFO de chunks pequeños

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### Fatiga de MFA

Bombardear con push hasta que la víctima acepte

**Aparece en 1 clase(s):** [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### Features

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 358 — Machine Learning aplicado a Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/358-machine-learning-aplicado-anticheat/README.md).

### ffuf / feroxbuster / gobuster

Herramientas de fuzzing de rutas

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### FHS

Estándar que define el propósito de cada directorio en Linux

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

### FIDO2 / passkeys

Factores resistentes a phishing

**Aparece en 1 clase(s):** [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### Fijar el algoritmo

El servidor decide el algoritmo, no el token

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### file

Identifica tipo, arquitectura y si está stripped

**Aparece en 1 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md).

### File Header

Arquitectura, nº de secciones, marca de tiempo

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### Fileless

Sin artefacto en disco; se busca en memoria y configuración

**Aparece en 3 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md), [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md), [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### Filtrado

Sin respuesta o error ICMP: un filtro descarta el tráfico

**Aparece en 1 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### Filtro de visualización

Expresión booleana sobre campos disecados; oculta paquetes

**Aparece en 2 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md), [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### FIN

Flag que solicita cerrar la conexión de forma ordenada.

**Aparece en 1 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md).

### Fin de vida

Momento y proceso en que cesa soporte y se gestiona retiro.

**Aparece en 1 clase(s):** [Clase 266 — Seguridad de IoT: panorama y superficie de ataque](../classes/parte-13-seguridad-movil-iot-e-inalambrica/266-seguridad-de-iot-panorama-y-superficie-de-ataque/README.md).

### FIN / NULL / Xmas

Escaneos con flags atípicos para eludir filtros simples

**Aparece en 1 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### FIN7

Actor con motivación financiera y TTPs bien documentados

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### Fingerprinting del motor

Identificar el motor por que sintaxis evalua

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### finish

Ejecutar hasta que la función actual retorna

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### Firewall con estado

Recuerda las conexiones vistas y permite sus respuestas

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### Firewall sin estado

Juzga cada paquete de forma aislada; exige reglas de vuelta inseguras

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### Firma de código

Firma de binarios y paquetes para verificar procedencia

**Aparece en 1 clase(s):** [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### Firma de módulos

Defensa que restringe qué LKM se cargan

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### Firma del dato

HMAC que impide alterar el objeto serializado

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### Firma digital

Se genera con clave privada y se verifica con la pública

**Aparece en 1 clase(s):** [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### Firma / regla

Descripción de un patrón de tráfico considerado malicioso

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### Flag

Meta técnica verificable derivada del objetivo de negocio

**Claves de búsqueda normalizadas:** `bandera`.

**Aparece en 2 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md), [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### Flag TCP

Bit de control (SYN, ACK, RST, FIN...) del segmento TCP

**Aparece en 1 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md).

### Flags de cookie

HttpOnly, Secure, SameSite

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### FLARE VM

Distribución Windows con el instrumental de análisis

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### FLIRT / firmas

Reconocer funciones de librería enlazadas

**Aparece en 1 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### flow

Acota dirección y estado de la conexión en la que aplica la regla

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### Flow bypass

Saltarse pasos obligatorios de un proceso

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### flowbits

Marca de estado que encadena condiciones entre paquetes

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### Flujo

Secuencia unidireccional de paquetes con una 5-tupla común

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### Flujo de control

Estructura de decisiones y bucles de una función

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### Flujo de datos

Rastro del dato guardado hasta donde se usa sin sanear

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### fmtstrpayload

pwntools genera el payload de escritura automáticamente

**Aparece en 1 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### Follow Stream

Reensamblado de una conversación completa en orden

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### Forced browsing

Acceder a funciones ocultas que no validan el rol

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### Forense de memoria

Detecta rootkits comparando listas del kernel

**Aparece en 3 clase(s):** [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md), [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md), [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### Format string

Vulnerabilidad por pasar entrada como cadena de formato

**Aparece en 1 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### Formato de datos

JSON u otros que transportan datos sin instanciar clases

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### Formato grepable

Salida de una línea por host, pensada para `grep`/`awk`

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### Formato sin pérdida

PNG, BMP, WAV; necesarios para que el LSB sobreviva

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### Formatos con XML

DOCX, XLSX, SVG, SAML, RSS lo llevan por dentro

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### Formulario auto-enviado

PoC clásica alojada en la página del atacante

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### FORTIFY / -Wformat

Mitigaciones del compilador contra format string

**Aparece en 1 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### Forward secrecy

Robar la clave a largo plazo no descifra sesiones pasadas

**Aparece en 3 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md), [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md), [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### Fragmentación

División de un paquete IP en fragmentos según el MTU del enlace.

**Aparece en 1 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md).

### Framework de notices

Mecanismo para elevar algo a "merece atención"

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### FREAK / Logjam

Explotación de cifrados de exportación debilitados

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### Freemarker

Motor Java con sintaxis de dolar y llaves

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### Frida

Instrumentación dinámica; inyecta código en un proceso vivo

**Aparece en 1 clase(s):** [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md).

### Frontend vs backend

Proxy/CDN y servidor de aplicación que interpretan distinto

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Frontera de confianza

Punto donde cambia quién controla o valida una interacción.

**Aparece en 1 clase(s):** [Clase 237 — Modelado de amenazas: STRIDE y DREAD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/237-modelado-de-amenazas-stride-y-dread/README.md).

### Frontera pasivo/activo

Cruzarla es enviar la primera consulta al objetivo

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### FS

Variable de awk: separador de campos de entrada

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### FSM,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 350 — Triggerbot, macros, input automation y bots](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/350-triggerbot-macros-input-automation-bots/README.md).

### FTP anónimo

Acceso sin credenciales con el usuario `anonymous`

**Aparece en 1 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md).

### Fuente

Origen potencial de datos no confiables.

**Aparece en 1 clase(s):** [Clase 238 — SAST: análisis estático de código](../classes/parte-11-devsecops-y-seguridad-del-sdlc/238-sast-analisis-estatico-de-codigo/README.md).

### Fuente primaria

Material cercano al hecho; no garantiza neutralidad ni autenticidad.

**Aparece en 1 clase(s):** [Clase 249 — Fundamentos de OSINT](../classes/parte-12-osint-e-ingenieria-social/249-fundamentos-de-osint/README.md).

### Fuente (source)

Origen de un dato controlable (`recv`, `read`, `argv`)

**Aparece en 1 clase(s):** [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Fuerza bruta

Prueba masiva de credenciales; **fuera** de la enumeración pasiva

**Aparece en 3 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md), [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md), [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### Fuerza bruta en línea

Muchas contraseñas contra una cuenta; se bloquea

**Aparece en 1 clase(s):** [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md).

### Fuga de DNS

Resolver nombres fuera del túnel, revelando los dominios visitados

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### Función

Bloque reutilizable con nombre que encapsula lógica.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### Función hash criptográfica

Salida de tamaño fijo, determinista y no invertible

**Aparece en 1 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md).

### Función unidireccional con trampilla

Fácil de calcular, difícil de invertir salvo con un secreto

**Aparece en 1 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md).

### Funciones peligrosas

`gets`, `strcpy`, `strcat`, `sprintf`, `scanf("%s")`

**Aparece en 1 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md).

### Fuzzing

Alimentar el programa con muchas entradas para provocar crashes

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### Fuzzy hashing (ssdeep)

Hash de similitud; agrupa variantes parecidas

**Aparece en 1 clase(s):** [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md).

## G

### Gadget

Método que se ejecuta al deserializar y es útil al atacante

**Aparece en 4 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md), [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md), [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md), [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### Gadget chain

Encadenar gadgets ya presentes para lograr RCE

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### Gadget ret de relleno

Un `ret` extra que realinea la pila

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Game

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 342 — Arquitectura de videojuegos desde la perspectiva de seguridad](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/342-arquitectura-videojuegos-perspectiva-seguridad/README.md).

### Gate

Regla de decisión del flujo, con evidencia, umbral y tratamiento de excepciones.

**Aparece en 1 clase(s):** [Clase 236 — Secure SDLC y filosofía shift-left](../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md).

### Gateway

Componente que media tráfico entre dominios de red.

**Aparece en 1 clase(s):** [Clase 274 — Seguridad automotriz y bus CAN](../classes/parte-13-seguridad-movil-iot-e-inalambrica/274-seguridad-automotriz-y-bus-can/README.md).

### GATT

Modelo de servicios, características y operaciones BLE.

**Aparece en 1 clase(s):** [Clase 271 — Seguridad de Bluetooth y BLE](../classes/parte-13-seguridad-movil-iot-e-inalambrica/271-seguridad-de-bluetooth-y-ble/README.md).

### gcc -S

Genera el ensamblador de un fuente C, para aprender a leerlo

**Aparece en 1 clase(s):** [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### GDB

Depurador estándar de Linux

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### gdb.attach()

Engancha GDB al proceso para depurar el exploit

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### GDB scripting

Automatizar breakpoints y volcado de argumentos

**Aparece en 1 clase(s):** [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md).

### Geolocalización

Inferencia del lugar representado.

**Aparece en 1 clase(s):** [Clase 253 — Geolocalización y análisis de imágenes](../classes/parte-12-osint-e-ingenieria-social/253-geolocalizacion-y-analisis-de-imagenes/README.md).

### Gestión de secretos

Fuera del código, con escaneo automático

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### Get-Member

Revela propiedades y métodos reales de un objeto

**Aparece en 1 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md).

### Get out of jail letter

Autorización que el pentester lleva encima durante el test

**Aparece en 1 clase(s):** [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### getopts

Parser incorporado de opciones de línea de comandos

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### GetProcAddress

Resuelve la dirección de una función por nombre

**Aparece en 1 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### getrandom()

Llamada al sistema recomendada en Linux

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### gets

Lee sin límite; eliminada del estándar de C

**Aparece en 1 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md).

### getsystem

Eleva de administrador local a SYSTEM

**Aparece en 1 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### Ghidra

Suite de RE libre de la NSA, con decompilador

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### GhidraScript

Scripting para automatizar tareas de RE

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### GhidraScript / IDAPython

Scripting para tareas repetitivas

**Aparece en 1 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### GIL

Cerrojo del intérprete CPython que serializa el bytecode

**Aparece en 1 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### git add

Mueve cambios al área de staging

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### git rm --cached

Deja de rastrear un fichero sin borrarlo

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### gitleaks

Escáner de secretos en el historial

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### gitleaks / detect-secrets

Escáneres de secretos en repositorios y CI

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### Globbing

Expansión de comodines (`*`, `?`) a nombres de archivo

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### Goodhart

Riesgo de degradar una medida al convertirla en objetivo rígido.

**Aparece en 1 clase(s):** [Clase 287 — Métricas de seguridad: KPIs y KRIs](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md).

### Goodware

Software legítimo; hay que evitar cazarlo

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### GoPhish

Plataforma para lanzar y medir campañas de phishing controladas

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### GOT

Tabla de punteros resueltos a funciones de librería

**Aparece en 2 clase(s):** [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md), [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md).

### Govern

Función de gobernanza, novedad del CSF 2.0

**Aparece en 1 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md).

### Grafo observado

Red limitada por la muestra y las relaciones disponibles.

**Aparece en 1 clase(s):** [Clase 252 — OSINT en redes sociales](../classes/parte-12-osint-e-ingenieria-social/252-osint-en-redes-sociales/README.md).

### GraphiQL / InQL

Herramientas que reconstruyen el esquema

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### GraphQL

API de un solo endpoint con lenguaje de consulta

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### Gravedad

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 349 — Aimbot avanzado, predicción, smoothing y recoil](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/349-aimbot-avanzado-prediccion-smoothing-recoil/README.md).

### Gray box

Información parcial, como un usuario estándar

**Aparece en 1 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### Grey hat

Hacker sin permiso pero sin intención dañina clara

**Aparece en 1 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).

### Grounding

Vinculación de una salida con evidencia accesible.

**Aparece en 1 clase(s):** [Clase 331 — IA generativa y LLMs en ciberseguridad: panorama, capacidades y límites](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/331-ia-generativa-y-llms-en-ciberseguridad-panorama-y-limites/README.md).

### Grupo con nombre

`(?P<n>...)` en Python

**Aparece en 1 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md).

### Grupo de captura

`(...)` guarda lo coincidido

**Aparece en 1 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md).

### Grupo débil

Parámetros pequeños o reutilizados que permiten precomputación

**Aparece en 1 clase(s):** [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### Grupo (Gxxxx)

Actor de amenaza catalogado con sus técnicas atribuidas

**Aparece en 1 clase(s):** [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### GTFOBins

Catálogo de binarios abusables para escalar privilegios

**Aparece en 2 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md), [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### Guardrail

Capa que reduce una capacidad o detecta su uso; no garantía absoluta.

**Aparece en 10 clase(s):** [Clase 331 — IA generativa y LLMs en ciberseguridad: panorama, capacidades y límites](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/331-ia-generativa-y-llms-en-ciberseguridad-panorama-y-limites/README.md), [Clase 332 — Agentes de IA y el Model Context Protocol (MCP) para seguridad](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/332-agentes-de-ia-y-el-model-context-protocol-mcp-para-seguridad/README.md), [Clase 333 — kali-mcp: orquestar herramientas de Kali desde un agente de IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/333-kali-mcp-orquestar-herramientas-de-kali-desde-un-agente-de-ia/README.md), [Clase 334 — Reconocimiento y escaneo asistidos por IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/334-reconocimiento-y-escaneo-asistidos-por-ia/README.md), [Clase 335 — Explotación y post-explotación autorizada asistida por IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/335-explotacion-y-post-explotacion-autorizada-asistida-por-ia/README.md), [Clase 336 — OSINT y auditoría web con agentes de IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/336-osint-y-auditoria-web-con-agentes-de-ia/README.md), [Clase 337 — IA para el lado defensivo: SOC, triaje y forense](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/337-ia-para-el-lado-defensivo-soc-triaje-y-forense/README.md), [Clase 338 — Generación de informes y flujos de trabajo con IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/338-generacion-de-informes-y-flujos-de-trabajo-con-ia/README.md), [Clase 339 — Riesgos, guardrails, OPSEC y ética del hacking con IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/339-riesgos-guardrails-opsec-y-etica-del-hacking-con-ia/README.md), [Clase 340 — Capstone: pentest autorizado asistido por IA con MCP](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/340-capstone-pentest-autorizado-asistido-por-ia-con-mcp/README.md).

### Guiado por cobertura

El fuzzer usa qué código se ejecuta como brújula

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### Gusano (worm)

Se propaga solo, sin intervención humana

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### Gusano XSS

Payload que se propaga publicándose a sí mismo

**Aparece en 1 clase(s):** [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

## H

### Hack The Box (HTB)

Plataforma de laboratorios prácticos de ciberseguridad; sus reglas limitan la publicación de soluciones de contenido activo.

**Claves de búsqueda normalizadas:** `hack the box`, `htb`.

**Sitio oficial:** [Hack The Box (HTB)](https://www.hackthebox.com/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### HackerOne / Bugcrowd / Intigriti

Plataformas que alojan programas

**Aparece en 1 clase(s):** [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### Hacktivismo

Ataques motivados por fines políticos o sociales

**Aparece en 1 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md).

### HAL

Capa de abstracción de hardware en kernel mode

**Aparece en 1 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md).

### Half-open

Escaneo que no completa el handshake, aborta con RST

**Aparece en 1 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md).

### Half-open scan

Escaneo SYN que no completa el handshake para pasar inadvertido.

**Aparece en 1 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md).

### Hallazgo

Diferencia sustentada entre criterio y condición.

**Aparece en 2 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md), [Clase 285 — Auditoría de seguridad](../classes/parte-14-grc-riesgo-y-cumplimiento/285-auditoria-de-seguridad/README.md).

### Hallazgo reportable

Cada vector con su remediación para el informe

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### Hallazgo trazable

Afirmación respaldada por evidencia reproducible

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### Handler

Puntero a la función manejadora de esta entrada

**Aparece en 2 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md), [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### Handshake

Intercambio de tres segmentos que establece una conexión TCP.

**Aparece en 2 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md), [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### Hardening

Reducir la superficie de ataque desactivando y reforzando componentes

**Aparece en 1 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md).

### Harness

Función que conecta el fuzzer con el código objetivo

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### Harvest now, decrypt later

Capturar hoy para descifrar cuando exista la máquina

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### Hash

Huella de longitud fija de una entrada arbitraria

**Aparece en 1 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md).

### Hash criptográfico

Huella exacta (SHA-256); un byte cambia todo

**Aparece en 1 clase(s):** [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md).

### Hash / IP

IOCs triviales de cambiar (base de la pirámide)

**Aparece en 1 clase(s):** [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md).

### Hash rápido

MD5, NTLM, SHA-*; vulnerable al cracking a escala

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### Hash SHA

Identificador de contenido de un objeto Git

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### Hash-then-sign

Firmar el digest en lugar del mensaje completo

**Aparece en 1 clase(s):** [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### hashcat / John the Ripper

Herramientas de crackeo usadas para medir resistencia

**Aparece en 1 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md).

### hashdump

Extrae los hashes de cuentas locales (SAM)

**Aparece en 1 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### Hashing

Función unidireccional de longitud fija

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### hashlib

Módulo estándar de funciones hash criptográficas.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### Header / payload / firma

Las tres partes del JWT, en Base64URL

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### Heap

Región de asignación dinámica (malloc/free)

**Aparece en 2 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md), [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### Heap grooming / feng shui

Ordenar los chunks con malloc/free precisos

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### Heartbleed

Fallo de implementación de OpenSSL que filtraba memoria

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### Heurístico

El auto-análisis acierta casi siempre pero puede fallar

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### Hex dump

Vista de datos crudos en hex y ASCII

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### Hex-Rays

Decompilador de IDA, referencia de calidad

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### Hexadecimal

Base 16 (0-9, A-F), prefijo `0x`

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### Higiene del host

El anfitrión nunca ejecuta la muestra y está protegido

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### Hilo

Flujo de ejecución que comparte memoria dentro de un proceso

**Aparece en 1 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md).

### Hipervisor

Software que ejecuta máquinas virtuales

**Aparece en 1 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md).

### Historial

Cadena inmutable de commits

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### HKCU

Colmena del Registro del usuario actual

**Aparece en 1 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md).

### HKDF

KDF estándar en dos fases: extraer y expandir

**Aparece en 1 clase(s):** [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### HKLM

Colmena del Registro de ámbito de máquina

**Aparece en 1 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md).

### HMAC

MAC estándar con dos pasadas de hash anidadas

**Aparece en 2 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md), [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

### HMI

Interfaz para observar y operar el proceso.

**Aparece en 1 clase(s):** [Clase 273 — Seguridad de sistemas de control industrial (ICS/SCADA)](../classes/parte-13-seguridad-movil-iot-e-inalambrica/273-seguridad-de-sistemas-de-control-industrial-ics-scada/README.md).

### Homónimo

Persona diferente que comparte nombre u otro atributo.

**Aparece en 1 clase(s):** [Clase 250 — OSINT de personas](../classes/parte-12-osint-e-ingenieria-social/250-osint-de-personas/README.md).

### Host-only

Red VM ↔ host, sin Internet

**Aparece en 1 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md).

### Host pivote

Máquina con acceso a la subred objetivo

**Aparece en 1 clase(s):** [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### Host utilizable

Dirección asignable a una máquina dentro del rango.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### Host vivo

Objetivo que respondió a alguna sonda de descubrimiento

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### hostrule

Se ejecuta una vez por host que cumpla la condición

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### HS256

Firma simétrica; el mismo secreto firma y verifica

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### HSM

Dispositivo que guarda claves y solo expone operaciones

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### HSTS

Cabecera que fuerza al navegador a usar solo HTTPS con ese sitio

**Aparece en 2 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md), [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md).

### HSTS preload

Lista integrada en el navegador; protege incluso la primera visita

**Aparece en 1 clase(s):** [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md).

### HTA

HTML Application ejecutada por mshta con plenos privilegios

**Aparece en 1 clase(s):** [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### HTML smuggling

Reconstruir el payload en el navegador vía JS/Blob para evadir proxies

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### HTTP

Protocolo de aplicación sin estado para transferir recursos web.

**Aparece en 1 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md).

### HTTP/2 downgrade

Traducir HTTP/2 a HTTP/1.1 reintroduce ambigüedades

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### http.log / dns.log / ssl.log

Logs detallados por protocolo

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### HTTP/S como C2

Se mezcla con la navegación; el más común

**Aparece en 1 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md).

### HttpOnly

Flag que oculta la cookie a JavaScript; mitiga el robo por XSS

**Aparece en 3 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md), [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md), [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### HTTPS

HTTP transportado sobre TLS: canal cifrado y autenticado.

**Aparece en 1 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md).

### Huella de pila

Conjunto de rasgos de implementación (TTL, ventana, opciones, ISN)

**Aparece en 1 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md).

### Human checkpoint

Punto donde una persona con autoridad aprueba una transición de riesgo.

**Aparece en 1 clase(s):** [Clase 340 — Capstone: pentest autorizado asistido por IA con MCP](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/340-capstone-pentest-autorizado-asistido-por-ia-con-mcp/README.md).

### Human-in-the-loop

Diseño que asigna revisión humana con autoridad real.

**Aparece en 1 clase(s):** [Clase 298 — IA aplicada a la defensa: detección y SOC](../classes/parte-15-seguridad-de-ia-y-machine-learning/298-ia-aplicada-a-la-defensa-deteccion-y-soc/README.md).

### Hydra / Medusa

Herramientas de ataque a credenciales multiprotocolo

**Aparece en 1 clase(s):** [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md).

## I

### I/O-bound

Tarea limitada por espera de entrada/salida, no por CPU

**Aparece en 1 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### I/Q

Dos componentes ortogonales que conservan amplitud y fase.

**Aparece en 1 clase(s):** [Clase 269 — Radio definida por software (SDR)](../classes/parte-13-seguridad-movil-iot-e-inalambrica/269-radio-definida-por-software-sdr/README.md).

### IAT vacía

Síntoma de resolución dinámica

**Aparece en 1 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### ICMP

Protocolo de control y diagnóstico de IP (ping, traceroute, errores).

**Aparece en 1 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md).

### ID en la URL

Mala práctica; queda en logs e historial

**Aparece en 1 clase(s):** [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### IDA Pro

Desensamblador comercial estándar de la industria

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### IDAPython

Scripting de IDA

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### Idempotente

Operación que repetida produce el mismo efecto que una sola vez.

**Aparece en 1 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md).

### Identidad

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 355 — Telemetría para Game Security](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/355-telemetria-game-security/README.md).

### Identidad como perímetro

La verificación se centra en quién y con qué, no en dónde

**Aparece en 1 clase(s):** [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md).

### Identificación de hash

Determinar el algoritmo antes de atacar

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### Identificación por comportamiento

Reconocer un protocolo aunque use un puerto no estándar

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### Identificador

Atributo usado para relacionar registros, con fuerza y riesgo variables.

**Aparece en 1 clase(s):** [Clase 250 — OSINT de personas](../classes/parte-12-osint-e-ingenieria-social/250-osint-de-personas/README.md).

### Identificador de publicación

Clave estable de plataforma preferible a una captura aislada.

**Aparece en 1 clase(s):** [Clase 252 — OSINT en redes sociales](../classes/parte-12-osint-e-ingenieria-social/252-osint-en-redes-sociales/README.md).

### Identificador no obvio

UUID que dificulta adivinar, pero no es una defensa

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### IDOR

Referenciar un objeto sin comprobar la propiedad

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### IDS

Detecta y alerta observando una copia del tráfico

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### idtoken

JWT que prueba la identidad; se valida como tal

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### IEX (Invoke-Expression)

Ejecuta una cadena como código

**Aparece en 1 clase(s):** [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### IG

Agrupación priorizada según recursos y perfil de riesgo.

**Aparece en 1 clase(s):** [Clase 280 — Controles CIS](../classes/parte-14-grc-riesgo-y-cumplimiento/280-controles-cis/README.md).

### IKE

Protocolo de intercambio de claves de IPsec

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### Imagen

Plantilla inmutable en capas para crear contenedores

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### IMDSv2

Metadata con token que un SSRF simple no puede alcanzar

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### Immunity / WinDbg

Depuradores usados en el exploiting de Windows

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### impacket

Suite de Python con implementaciones de PsExec, WMI, etc.

**Aparece en 1 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### Impact assessment

Evaluación contextual de efectos, afectados y mitigaciones.

**Aparece en 1 clase(s):** [Clase 300 — Gobernanza y ética de la IA segura](../classes/parte-15-seguridad-de-ia-y-machine-learning/300-gobernanza-y-etica-de-la-ia-segura/README.md).

### Impacto

Lo que el bug permite; justifica la severidad

**Aparece en 3 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md), [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md), [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### Impacto y severidad

Qué significa para la organización y con qué urgencia

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### imphash

Hash de la tabla de imports; agrupa por APIs usadas

**Aparece en 1 clase(s):** [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md).

### Implante / agente

Código que corre en la víctima y llama a casa

**Aparece en 1 clase(s):** [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### Import Directory / IAT

Tabla de APIs que usa el binario

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### Incertidumbre

Falta de conocimiento representada y comunicada explícitamente.

**Aparece en 1 clase(s):** [Clase 277 — Gestión de riesgos: cuantitativa y cualitativa](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md).

### Indemnización / seguro

Reparto de responsabilidad ante daños accidentales

**Aparece en 1 clase(s):** [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### Índice de medición

Base construida con observaciones realizadas en momentos concretos.

**Aparece en 1 clase(s):** [Clase 254 — OSINT técnico: Shodan y Censys](../classes/parte-12-osint-e-ingenieria-social/254-osint-tecnico-shodan-y-censys/README.md).

### INetSim

Simula Internet (DNS, HTTP, SMTP) para el malware

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### Info leak

Filtrar una dirección de libc en tiempo de ejecución

**Aparece en 3 clase(s):** [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md), [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md), [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### Info.plist

Configuración declarativa del bundle y varias superficies.

**Aparece en 1 clase(s):** [Clase 264 — Pentest de aplicaciones iOS](../classes/parte-13-seguridad-movil-iot-e-inalambrica/264-pentest-de-aplicaciones-ios/README.md).

### Información,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 343 — Taxonomía técnica de cheats](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/343-taxonomia-tecnica-cheats/README.md).

### informationschema

Tablas de metadatos con el esquema de la BD

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### Informe

El producto real del pentest; lo que el cliente compra

**Aparece en 1 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md).

### Infostealer

Roba credenciales, cookies y carteras

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### Ingeniería de detección

Necesita TTPs para construir detecciones

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### Initial access broker

Intermediario que transfiere acceso obtenido a otro actor

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### innerHTML

Sink que interpreta HTML; peligroso con datos del usuario

**Aparece en 1 clase(s):** [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### Input

Documento evaluado en una consulta concreta.

**Aparece en 1 clase(s):** [Clase 244 — Políticas como código con OPA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/244-politicas-como-codigo-con-opa/README.md).

### INPUT / OUTPUT / FORWARD

Tráfico hacia, desde y a través del equipo

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### Insider

Actor con acceso legítimo interno, malicioso o negligente

**Aparece en 1 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md).

### Instancia

Aparición concreta de una vulnerabilidad en un activo o artefacto.

**Aparece en 1 clase(s):** [Clase 245 — Gestión de vulnerabilidades a escala](../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md).

### Instrumentación

Añadir al binario el reporte de caminos ejecutados

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### Instrumentación dinámica

Observación o modificación controlada del proceso en ejecución.

**Aparece en 1 clase(s):** [Clase 262 — Pentest de aplicaciones Android](../classes/parte-13-seguridad-movil-iot-e-inalambrica/262-pentest-de-aplicaciones-android/README.md).

### Integridad,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 2 clase(s):** [Clase 345 — Trainers e instrumentación del cliente](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/345-trainers-instrumentacion-cliente/README.md), [Clase 353 — Arquitecturas Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/353-arquitecturas-anticheat/README.md).

### Integridad, no confidencialidad

La firma protege de manipulación, no de lectura

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### interactive()

Entrega una shell interactiva tras el éxito

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Interceptación de SMS

Robo de códigos de doble factor

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### Interceptar

Pausar una petición para modificarla antes de enviarla

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### Interceptar función

Ver y modificar argumentos y retorno en caliente

**Aparece en 1 clase(s):** [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md).

### Internal,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 2 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md), [Clase 343 — Taxonomía técnica de cheats](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/343-taxonomia-tecnica-cheats/README.md).

### Intérprete de confianza

powershell/wscript/mshta, firmados por Microsoft

**Aparece en 1 clase(s):** [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### Intervención

Cambio educativo, técnico o de proceso.

**Aparece en 1 clase(s):** [Clase 286 — Concienciación y cultura de seguridad](../classes/parte-14-grc-riesgo-y-cumplimiento/286-concienciacion-y-cultura-de-seguridad/README.md).

### Introspección

Consultar el propio esquema de la API

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### Intruder

Automatiza cargas sobre posiciones marcadas

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### INVALID

Paquete que no encaja en ningún flujo conocido; se descarta

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### Invalidación en servidor

El logout debe anular el ID, no solo borrar la cookie

**Aparece en 1 clase(s):** [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### Invariants

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 354 — Server-side Anti-Cheat y diseño autoritativo](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/354-server-side-anticheat-diseno-autoritativo/README.md).

### Inventario,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 351 — Multiplayer y autoridad: nunca confiar en el cliente](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/351-multiplayer-autoridad-nunca-confiar-cliente/README.md).

### Inventario de persistencia

Registro de lo instalado para poder retirarlo

**Aparece en 1 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md).

### Inventario de superficie

Resultado del mapeo; base de las pruebas posteriores

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### Invisible a escáneres

No hay patrón que detectar automáticamente

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### Inyección ciega

El comando se ejecuta pero no se ve la salida

**Aparece en 1 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### Inyección ciega (blind)

La inyección funciona pero no se ven los datos

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### Inyección de código

VirtualAllocEx + WriteProcessMemory + CreateRemoteThread

**Aparece en 2 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md), [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### Inyección de comandos

Entrada del usuario ejecutada como comando del sistema

**Aparece en 1 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### Inyección indirecta

Instrucción hostil incorporada en contenido externo.

**Aparece en 1 clase(s):** [Clase 296 — Prompt injection y jailbreaks](../classes/parte-15-seguridad-de-ia-y-machine-learning/296-prompt-injection-y-jailbreaks/README.md).

### Inyección NoSQL

Alterar la estructura o el tipo de la consulta con operadores

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### Inyección SQL (SQLi)

Datos del usuario interpretados como parte de una consulta

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### Inyección temporal

Deducir por el tiempo de respuesta (`SLEEP`, `WAITFOR`)

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### IOC — Indicador de compromiso

*Indicator of Compromise*: dato observable de una intrusión

**Claves de búsqueda normalizadas:** `indicator of compromise`, `ioc`.

**Aparece en 6 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md), [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md), [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md), [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md), [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md), [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### IOCs estructurados

Indicadores en tablas o formato estándar

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### IP

Protocolo de red best-effort que direcciona y enruta paquetes sin garantías.

**Aparece en 2 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md), [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md).

### IPA

Paquete distribuible que contiene bundle y binarios de una app iOS.

**Aparece en 1 clase(s):** [Clase 264 — Pentest de aplicaciones iOS](../classes/parte-13-seguridad-movil-iot-e-inalambrica/264-pentest-de-aplicaciones-ios/README.md).

### ipad / opad

Constantes de relleno interno y externo de HMAC

**Aparece en 1 clase(s):** [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

### IPFIX

Estándar abierto derivado de NetFlow v9

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### IPS

Se sitúa en línea y puede descartar el tráfico

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### IPsec

Suite estándar de VPN: IKE, ESP y AH

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### IPv4

Dirección de 32 bits escrita en cuatro octetos decimales.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### IR

Respuesta a incidentes (Incident Response)

**Aparece en 1 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md).

### ISN

Número de secuencia inicial aleatorio que abre una conexión TCP.

**Aparece en 1 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md).

### ISO 27001

Estándar certificable de requisitos del SGSI

**Aparece en 1 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md).

### ISO 27002

Guía detallada de los controles del Anexo A

**Aparece en 1 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md).

### ISO/IEC 29147

Estándar de divulgación de vulnerabilidades

**Aparece en 1 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).

### ISO/IEC 30111

Estándar de gestión de vulnerabilidades

**Aparece en 1 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).

### IV

Vector de inicialización; impredecible, único y **no** secreto

**Aparece en 1 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md).

### IV predecible

Vector de inicialización fijo o adivinable en CBC

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

## J

### JA3

Huella del cliente TLS; identifica software sin descifrar el tráfico

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### JA3 / JA3S

Huella del cliente/servidor TLS; delata beacons

**Aparece en 1 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md).

### jadx

Decompilador de Dalvik a Java casi legible

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### Jailbreak

Modificación que amplía acceso; altera el modelo del dispositivo de prueba.

**Aparece en 1 clase(s):** [Clase 264 — Pentest de aplicaciones iOS](../classes/parte-13-seguridad-movil-iot-e-inalambrica/264-pentest-de-aplicaciones-ios/README.md).

### Jeopardy

Formato de tablero de retos por categorías

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### Jerarquía de protocolos

Composición porcentual del tráfico de la captura

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### Jinja2 / Twig

Motores con sintaxis de dobles llaves

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### Jitter

Variación aleatoria del intervalo de check-in

**Aparece en 2 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md), [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### Jitter / sleep

Aleatoriedad e intervalo del check-in

**Aparece en 1 clase(s):** [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### JNI/bridge

Interfaz entre código gestionado y nativo.

**Aparece en 1 clase(s):** [Clase 265 — Ingeniería inversa de aplicaciones móviles](../classes/parte-13-seguridad-movil-iot-e-inalambrica/265-ingenieria-inversa-de-aplicaciones-moviles/README.md).

### Job

Tarea gestionada por el control de trabajos de la shell

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### Job / handler

Tarea en segundo plano que espera conexiones

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### John the Ripper / Hashcat

Herramientas de cracking (CPU y GPU)

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### Journaling

Registro del sistema de ficheros que persiste cambios

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### JTAG/SWD

Interfaces de depuración y prueba de circuitos.

**Aparece en 1 clase(s):** [Clase 268 — Análisis de hardware: UART, JTAG y SPI](../classes/parte-13-seguridad-movil-iot-e-inalambrica/268-analisis-de-hardware-uart-jtag-y-spi/README.md).

### Juice Shop

Aplicación web vulnerable de OWASP para práctica

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### JWT

Token que contiene sus datos y una firma; sesión sin estado

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### JWT alg: none

Aceptar el algoritmo que declara el propio token

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### JWT (HS256)

Token web firmado con HMAC-SHA256

**Aparece en 1 clase(s):** [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

## K

### Kali Linux

Distribución con herramientas de seguridad ofensiva

**Aparece en 1 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md).

### KASLR

ASLR del kernel; exige un leak de kernel

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### KDF

Función de derivación de clave, lenta a propósito para contraseñas

**Aparece en 2 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md), [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### KDF de contraseñas

Función deliberadamente lenta para almacenar contraseñas

**Aparece en 1 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md).

### KDF lento

bcrypt, scrypt, Argon2; diseñado para resistir el cracking

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### KEK

Clave maestra que cifra otras claves; vive en el KMS/HSM

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### Kerberos

Protocolo de autenticación de AD basado en tickets

**Aparece en 1 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### Kernel exploit

Vulnerabilidad del núcleo; último recurso, puede tumbar la máquina

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### Kernel exploitation

Explotar el núcleo del sistema operativo

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### Kernel panic

Caída del sistema; riesgo de los exploits de kernel

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### KEV

Catálogo de CISA de vulnerabilidades conocidas como explotadas.

**Aparece en 1 clase(s):** [Clase 240 — SCA: dependencias y riesgo de terceros](../classes/parte-11-devsecops-y-seguridad-del-sdlc/240-sca-dependencias-y-riesgo-de-terceros/README.md).

### Keychain

Almacén de credenciales con clases de accesibilidad y controles.

**Aparece en 1 clase(s):** [Clase 263 — Seguridad de iOS: arquitectura](../classes/parte-13-seguridad-movil-iot-e-inalambrica/263-seguridad-de-ios-arquitectura/README.md).

### keyshare

Parte del ECDHE adelantada en TLS 1.3

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### Keystore

Servicio para claves y operaciones criptográficas con opciones de respaldo hardware.

**Aparece en 1 clase(s):** [Clase 261 — Seguridad de Android: arquitectura](../classes/parte-13-seguridad-movil-iot-e-inalambrica/261-seguridad-de-android-arquitectura/README.md).

### Keystream

Flujo pseudoaleatorio que se combina con XOR con el mensaje

**Aparece en 2 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md), [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### kid

Key ID del header; vector de inyección si no se valida

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### Kill Chain

Modelo de 7 fases de un ataque dirigido de Lockheed Martin

**Aparece en 1 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md).

### kiwi / Mimikatz

Recupera credenciales de la memoria de LSASS

**Aparece en 1 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### KMS

Servicio gestionado de claves en la nube

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### KOTH — King of the Hill

Formato competitivo en el que se obtiene y conserva control de un objetivo autorizado durante un intervalo.

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### KPA

Conoce pares de texto claro y su cifrado

**Aparece en 1 clase(s):** [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### KPI

Indicador de desempeño frente a objetivo.

**Aparece en 1 clase(s):** [Clase 287 — Métricas de seguridad: KPIs y KRIs](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md).

### KPTI

Aísla las tablas de páginas de usuario y kernel

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### KRI

Indicador de exposición o cambio de riesgo.

**Aparece en 1 clase(s):** [Clase 287 — Métricas de seguridad: KPIs y KRIs](../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md).

## L

### Laboratorio aislado

Entorno donde el malware no puede escapar ni dañar

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### Landing de simulación

Página controlada que educa y no captura secretos reales.

**Aparece en 1 clase(s):** [Clase 258 — Campañas de phishing con GoPhish](../classes/parte-12-osint-e-ingenieria-social/258-campanas-de-phishing-con-gophish/README.md).

### Landing page

Página controlada que captura credenciales o entrega el payload

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### LAPS

Contraseña de administrador local única por máquina

**Aparece en 1 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### Latencia por salto

Cada pivote añade retardo y fragilidad

**Aparece en 1 clase(s):** [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### Layer

Capa de Navigator que representa un plan o una cobertura

**Aparece en 1 clase(s):** [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### LDAP anónimo

Consulta al directorio sin autenticar; expone la estructura del dominio

**Aparece en 2 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md), [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md).

### LDPRELOAD

Carga una librería antes que las demás; secuestra libc

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### Leak → base → derivar

Patrón central de la explotación con ASLR

**Aparece en 1 clase(s):** [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md).

### Leak de kernel

Filtrar una dirección para derrotar KASLR

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### Leak del canario

Leer el canario para reescribirlo y evadirlo

**Aparece en 2 clase(s):** [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md), [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### Lease

Concesión temporal de una IP a un cliente DHCP.

**Aparece en 1 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md).

### leave; ret

Gadget típico de pivote de pila

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### Lectura de ficheros

`file:///etc/passwd` insertado en la respuesta

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### Legítimo,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 350 — Triggerbot, macros, input automation y bots](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/350-triggerbot-macros-input-automation-bots/README.md).

### Let's Encrypt / ACME

CA gratuita y protocolo de emisión y renovación automáticas

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### LetsDefend

Plataforma de entrenamiento SOC con investigaciones simuladas y modalidades gratuita y de pago.

**Sitio oficial:** [LetsDefend](https://letsdefend.io/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### LHOST / LPORT

Dirección y puerto de escucha del atacante

**Aparece en 2 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md), [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### libc

Biblioteca C, cargada en todo proceso; llena de código útil

**Aparece en 1 clase(s):** [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md).

### libc-database

Identifica la versión de libc por direcciones filtradas

**Aparece en 1 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### Libc del reto

La libc del servidor, que hay que usar para los offsets

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### libFuzzer

Fuzzing in-process, dirigido a una función

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### libpcap

Librería de captura sobre la que se apoyan tcpdump, Wireshark y Zeek

**Aparece en 1 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### libsodium / Tink / age

Bibliotecas con el camino fácil ya seguro

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### LIKELY VULNERABLE

Veredicto por versión, no por comprobación efectiva

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### Limitación de tasa

Encarece los ataques que necesitan muchas peticiones

**Aparece en 1 clase(s):** [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### Límite de profundidad

Restringir cuán anidada puede ser una consulta

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### Límite del estático

Ofuscación e indirección lo hacen incompleto

**Aparece en 1 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### Limpieza

Eliminar toda persistencia al cerrar el engagement

**Aparece en 1 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md).

### Line-of-sight

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 348 — Matemática de un aimbot](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/348-matematica-aimbot/README.md).

### Línea base

Conjunto heredado que se gestiona sin permitir nuevos hallazgos equivalentes.

**Aparece en 2 clase(s):** [Clase 236 — Secure SDLC y filosofía shift-left](../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md), [Clase 238 — SAST: análisis estático de código](../classes/parte-11-devsecops-y-seguridad-del-sdlc/238-sast-analisis-estatico-de-codigo/README.md).

### Línea de comandos

Revela el uso malicioso de un binario legítimo

**Aparece en 1 clase(s):** [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### LinkFinder

Herramienta que extrae URLs de ficheros JS

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### LinPEAS / LinEnum

Scripts que automatizan la detección de vectores

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### list

Secuencia ordenada y mutable.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### Lista de filtradas

Rechazar contraseñas ya comprometidas al crearlas

**Aparece en 1 clase(s):** [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md).

### Listener

Servicio que espera conexiones de implantes

**Aparece en 1 clase(s):** [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### Listing

Vista de desensamblado, dirección a dirección

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### Literal

Carácter que casa consigo mismo

**Aparece en 1 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md).

### Little-endian

El byte menos significativo se almacena primero

**Aparece en 1 clase(s):** [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### Living off the land (LotL)

Abusar de herramientas legítimas del sistema

**Aparece en 1 clase(s):** [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### LKM

Loadable Kernel Module; vía de los rootkits de kernel

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### LNK

Acceso directo de Windows usado como lanzador dentro de un contenedor

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### local

Declara una variable con ámbito de función

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### Local a remoto

Cambiar `process` por `remote` para atacar el servicio real

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Local forwarding (-L)

Expone un servicio interno concreto en el atacante

**Aparece en 1 clase(s):** [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### Local → remoto

Hacer que el exploit funcione contra el objetivo real

**Aparece en 1 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### Lockfile

Registro reproducible de versiones e integridad resueltas.

**Aparece en 1 clase(s):** [Clase 240 — SCA: dependencias y riesgo de terceros](../classes/parte-11-devsecops-y-seguridad-del-sdlc/240-sca-dependencias-y-riesgo-de-terceros/README.md).

### Logaritmo discreto

Hallar `a` conocidos `g` y `gᵃ mod p`; base de la seguridad

**Aparece en 1 clase(s):** [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### Lógica de negocio

Reglas específicas de la aplicación

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### Logjam

Ataque que explotó grupos DH de 1024 bits compartidos

**Aparece en 1 clase(s):** [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### Logon Type

Campo del evento 4624/4625 que indica el tipo de acceso

**Aparece en 1 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md).

### LOLBAS

Catálogo de LOLBins en Windows

**Aparece en 1 clase(s):** [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### LOLBin

Binario legítimo del sistema abusado por el malware

**Aparece en 3 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md), [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md), [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### Long-haul C2

Canal lento y sigiloso para persistencia

**Aparece en 1 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### Lookaround

Aserción de contexto sin consumir

**Aparece en 1 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md).

### Loopback

127.0.0.0/8; se refiere a la propia máquina.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### Loot

Evidencia recolectada, guardada en la base de datos

**Aparece en 1 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### LotL

Living off the land: abusar de herramientas legítimas

**Aparece en 1 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md).

### Low and slow

Exfiltrar despacio para evadir umbrales de volumen

**Aparece en 2 clase(s):** [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md), [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md).

### LSASS

Proceso de Windows que custodia credenciales en memoria

**Aparece en 2 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md), [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### LSB

Sustitución del bit menos significativo

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### ltrace

Registra las llamadas a funciones de librería

**Aparece en 2 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md), [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md).

### Lua

Lenguaje de scripting ligero en el que se escriben los scripts NSE

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### Lucky13

Ataque de timing sobre MAC-then-encrypt

**Aparece en 2 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md), [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

## M

### MAC

Etiqueta con clave secreta que prueba integridad y origen

**Aparece en 3 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md), [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md), [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

### MAC flooding

Saturar la CAM para degradar el switch a comportamiento de hub

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### MAC-then-encrypt

Orden inseguro usado por TLS 1.2; habilita Lucky13

**Aparece en 1 clase(s):** [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

### Mach-O

Formato de ejecutables de plataformas Apple.

**Aparece en 1 clase(s):** [Clase 265 — Ingeniería inversa de aplicaciones móviles](../classes/parte-13-seguridad-movil-iot-e-inalambrica/265-ingenieria-inversa-de-aplicaciones-moviles/README.md).

### Macro VBA

Código embebido en documentos Office

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### Macros

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 350 — Triggerbot, macros, input automation y bots](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/350-triggerbot-macros-input-automation-bots/README.md).

### Magic bytes

Primeros bytes que identifican el tipo real

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### main

Rama principal por convención

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### Maleabilidad

Poder alterar el texto claro manipulando el cifrado

**Aparece en 2 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md), [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### malfind

Plugin que detecta código inyectado en memoria

**Aparece en 1 clase(s):** [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### Malleable C2

Lenguaje de perfiles de tráfico de Cobalt Strike

**Aparece en 1 clase(s):** [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### Malleable profile

Configuración que define cómo se ve el tráfico C2

**Aparece en 1 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### Malware

Software diseñado para dañar o acceder sin autorización

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### Malware de Android

Malware móvil distribuido como APK

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### Malware de Linux

Malware dirigido a servidores e IoT

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### Malware en scripts

Malware escrito en PowerShell, JScript, VBScript

**Aparece en 1 clase(s):** [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### Man-in-the-middle

Posición entre dos partes que permite leer, alterar e inyectar

**Aparece en 1 clase(s):** [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md).

### Man-in-the-middle L2

Interposición del atacante entre dos hosts del mismo segmento

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### Manejador de eventos

`onerror`, `onload`; ejecuta JS sin la etiqueta script

**Aparece en 1 clase(s):** [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md).

### Manejo seguro

Guardar muestras cifradas (contraseña `infected`)

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### Manipulación de precio

Aceptar el precio o total que envía el cliente

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### Mapeo

Descubrir toda la estructura de la aplicación antes de atacar

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### Marca de tiempo

Prueba de que la firma existía antes de una fecha

**Aparece en 1 clase(s):** [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### Marco (stack frame)

Espacio de una función en la pila

**Aparece en 1 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md).

### Margen de seguridad

Rondas de sobra frente al mejor ataque conocido

**Aparece en 1 clase(s):** [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### Mark-of-the-Web (MOTW)

Marca que Windows pone a ficheros de internet; dispara advertencias y bloqueos

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### Máscara

Patrón que distingue los bits de red de los de host.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### Mass assignment

Modificación de campos internos al enlazar entrada sin lista permitida.

**Aparece en 2 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md), [Clase 247 — Seguridad de APIs en el ciclo de desarrollo](../classes/parte-11-devsecops-y-seguridad-del-sdlc/247-seguridad-de-apis-en-el-ciclo-de-desarrollo/README.md).

### MASTG

Guía de técnicas y casos de prueba móviles.

**Aparece en 1 clase(s):** [Clase 262 — Pentest de aplicaciones Android](../classes/parte-13-seguridad-movil-iot-e-inalambrica/262-pentest-de-aplicaciones-android/README.md).

### MASVS

Estándar de verificación para controles de aplicaciones móviles.

**Aparece en 1 clase(s):** [Clase 262 — Pentest de aplicaciones Android](../classes/parte-13-seguridad-movil-iot-e-inalambrica/262-pentest-de-aplicaciones-android/README.md).

### Matriz de comportamiento

Acciones mapeadas a tácticas y técnicas ATT&CK

**Aparece en 1 clase(s):** [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### Matriz Enterprise

ATT&CK para Windows, Linux, macOS, nube y contenedores

**Aparece en 1 clase(s):** [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### Matriz ICS

ATT&CK para entornos de control industrial

**Aparece en 1 clase(s):** [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### MBR / VBR

Código de arranque que infectan los bootkits clásicos

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### MD5 / SHA-1

Rotos para integridad; colisiones prácticas

**Aparece en 1 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md).

### Memoria virtual

Espacio de direcciones propio por proceso

**Aparece en 1 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md).

### Memory-hard

Exige mucha memoria; anula la ventaja de las GPU

**Aparece en 1 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md).

### Merge

Integra una rama en otra

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### Merkle-Damgård

Construcción por bloques encadenados; sufre extensión de longitud

**Aparece en 1 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md).

### Mersenne Twister

PRNG estadístico común; **nunca** para criptografía

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### meta

Metadatos de la regla (autor, familia, referencia)

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Metacarácter

`;` `&&` backtick `$()` y la barra vertical; encadenan o sustituyen comandos

**Aparece en 2 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md), [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### Metadato

Información sobre creación, comunicación o contexto, distinta del contenido principal.

**Aparece en 1 clase(s):** [Clase 260 — OPSEC personal y anonimato](../classes/parte-12-osint-e-ingenieria-social/260-opsec-personal-y-anonimato/README.md).

### Metadatos

Con quién, cuándo y cuánto; visibles aun con TLS

**Aparece en 1 clase(s):** [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md).

### Metadatos de documento

Usuarios, software y rutas filtrados en las propiedades

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### Metadatos de tráfico

Quién, cuándo, cuánto y con qué ritmo; sin el contenido

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### Metadatos EXIF / ID3

Campos de imagen y audio usados para ocultar

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### Metadatos vs. contenido

Barato y resistente al cifrado frente a fiel pero caro

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### Metasploit Framework

Marco de explotación que estandariza la cadena de ataque

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### Metasploitable

VM deliberadamente vulnerable para practicar

**Aparece en 1 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md).

### Meterpreter

Payload avanzado que se ejecuta en memoria

**Aparece en 1 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### Método

Verbo HTTP que declara la acción sobre un recurso.

**Aparece en 1 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md).

### Método de Kasiski

Deduce la longitud de la clave por las repeticiones del cifrado

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### Método HTTP

Cambiarlo puede saltar controles (GET protegido, DELETE no)

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### Metodología

Proceso repetible que da cobertura, defensa legal y valor

**Aparece en 1 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### Metodología por objetivos

Partir de una pregunta y navegar hacia ella

**Aparece en 1 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md).

### Métodos HTTP

Un endpoint puede proteger GET pero no DELETE/PUT

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### Métodos mágicos

`__wakeup`, `readObject`, `__reduce__` invocados al deserializar

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### Métrica agregada

Resultado grupal que reduce exposición individual.

**Aparece en 1 clase(s):** [Clase 258 — Campañas de phishing con GoPhish](../classes/parte-12-osint-e-ingenieria-social/258-campanas-de-phishing-con-gophish/README.md).

### Métrica ambiental

Ajuste por el contexto del activo; la más olvidada

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### Métrica base

Severidad intrínseca del fallo

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### Métrica de resistencia

Cuántas contraseñas caen y en cuánto tiempo

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### Métrica de resultado

Señal del cambio de riesgo o comportamiento, no mera actividad.

**Aparece en 1 clase(s):** [Clase 248 — Cultura DevSecOps y security champions](../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md).

### Métrica temporal

Ajuste por existencia y madurez de exploit

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### MFA

Autenticación multifactor: combinar dos o más factores independientes

**Aparece en 3 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md), [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md), [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### MFA fatigue

Presión mediante solicitudes repetidas de aprobación.

**Aparece en 1 clase(s):** [Clase 257 — Pretexting y vishing](../classes/parte-12-osint-e-ingenieria-social/257-pretexting-y-vishing/README.md).

### MFT

Tabla maestra de ficheros de NTFS; guarda varios timestamps

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### Micro-emulación

Emulación atómica de un comportamiento aislado y reutilizable

**Aparece en 1 clase(s):** [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### Microsegmentación

Políticas por carga de trabajo individual

**Aparece en 1 clase(s):** [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md).

### Migración híbrida

Combinar clásico y PQC; seguro si uno de los dos resiste

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### migrate

Traslada la sesión a un proceso estable

**Aparece en 1 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### Minimización

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 6 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md), [Clase 250 — OSINT de personas](../classes/parte-12-osint-e-ingenieria-social/250-osint-de-personas/README.md), [Clase 289 — Privacidad y protección de datos](../classes/parte-14-grc-riesgo-y-cumplimiento/289-privacidad-y-proteccion-de-datos/README.md), [Clase 346 — Información expuesta, radar, ESP y world-to-screen](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/346-informacion-expuesta-radar-esp-world-to-screen/README.md), [Clase 355 — Telemetría para Game Security](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/355-telemetria-game-security/README.md), [Clase 359 — Privacidad, gobernanza, sanciones y seguridad del propio Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/359-privacidad-gobernanza-sanciones-seguridad-anticheat/README.md).

### Mínimo privilegio

Cada servicio con su credencial y solo sus permisos

**Aparece en 3 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md), [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md), [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### Mínimo privilegio de BD

La cuenta de la app solo con los permisos necesarios

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### Mirai

Botnet IoT que abusa de credenciales por defecto

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### MISP

Plataforma de compartición de IOCs y CTI

**Aparece en 1 clase(s):** [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md).

### Mitigación

Cambio que reduce probabilidad o impacto y puede verificarse.

**Aparece en 2 clase(s):** [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md), [Clase 237 — Modelado de amenazas: STRIDE y DREAD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/237-modelado-de-amenazas-stride-y-dread/README.md).

### MITM

Man-in-the-middle: atacante interpuesto que intercepta el tráfico.

**Aparece en 1 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md).

### MitM en DH

Un intermediario acuerda una clave con cada parte

**Aparece en 1 clase(s):** [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### MITRE ATT&CK

Taxonomía de técnicas; táctica Lateral Movement

**Aparece en 3 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md), [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md), [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### MITRE ATT&CK Defense Evasion

Táctica que cataloga estas técnicas

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### MITRE ATT&CK Persistence

Táctica que cataloga estas técnicas

**Aparece en 1 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md).

### ML-DSA (FIPS 204)

Firma post-cuántica de propósito general

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### ML-KEM (FIPS 203)

Encapsulado de claves post-cuántico; sustituto de ECDH

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### MMU

Unidad de hardware que traduce direcciones

**Aparece en 1 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md).

### Model extraction

Construcción de un sustituto desde observaciones.

**Aparece en 1 clase(s):** [Clase 294 — Robo y extracción de modelos](../classes/parte-15-seguridad-de-ia-y-machine-learning/294-robo-y-extraccion-de-modelos/README.md).

### Modelado de amenazas

Decidir qué atacar y por qué antes de atacar

**Aparece en 2 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md), [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### Modelo de amenaza

Relación entre activos, adversarios, capacidades y consecuencias.

**Aparece en 2 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md), [Clase 260 — OPSEC personal y anonimato](../classes/parte-12-osint-e-ingenieria-social/260-opsec-personal-y-anonimato/README.md).

### Modo de operación

Receta para aplicar la primitiva a mensajes largos

**Aparece en 1 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md).

### Modo en línea

Despliegue en el camino del tráfico; un fallo corta el servicio

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### Modo kernel

Nivel de privilegio total de la CPU

**Aparece en 1 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md).

### Modo monitor

Captura de tramas 802.11 crudas sin asociarse a una red

**Aparece en 2 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md), [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md).

### Modo promiscuo

La NIC entrega todas las tramas Ethernet que ve, no solo las suyas

**Aparece en 1 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md).

### Modo real / protegido / largo

16, 32 y 64 bits; modo largo es el actual

**Aparece en 1 clase(s):** [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### Modo túnel vs. transporte

Cifrar el paquete entero o solo su carga útil

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### Modo usuario

Nivel de privilegio restringido

**Aparece en 1 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md).

### Modo visual / grafo

Navegación interactiva en r2 (`V` / `VV`)

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### Módulo

Archivo `.py` que agrupa funciones y datos relacionados.

**Aparece en 2 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md), [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### Módulo pe

Condiciones sobre la estructura del PE

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Módulo post

Automatiza enumeración local y sugerencias de escalada

**Aparece en 1 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### mona.py

Extensión que automatiza la explotación en Windows

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### Motor de plantillas

Genera HTML combinando plantilla y datos

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### Motor logic-less

Mustache y similares; solo sustituyen, no evaluan

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### mov / lea

Copiar datos / calcular una dirección sin leer memoria

**Aparece en 1 clase(s):** [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### movaps

Instrucción SSE que falla si la pila no está alineada

**Aparece en 1 clase(s):** [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### movaps SIGSEGV

Síntoma del desalineamiento de pila

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Movimiento,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 351 — Multiplayer y autoridad: nunca confiar en el cliente](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/351-multiplayer-autoridad-nunca-confiar-cliente/README.md).

### Movimiento lateral

Desplazamiento del atacante entre sistemas ya dentro de la red

**Claves de búsqueda normalizadas:** `lateral movement`.

**Aparece en 4 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md), [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md), [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md), [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### msfconsole

Interfaz principal del framework

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### msfdb / PostgreSQL

Base de datos que persiste hosts, servicios y loot

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### msfvenom

Generador de payloads autónomos de Metasploit

**Aparece en 2 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md), [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### mTLS

TLS mutuo; ambos extremos se autentican con certificado

**Aparece en 1 clase(s):** [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### MTU

Tamaño máximo de trama que un enlace puede transmitir sin fragmentar.

**Aparece en 2 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md), [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md).

### Muestra

Subconjunto seleccionado mediante método documentado.

**Aparece en 1 clase(s):** [Clase 285 — Auditoría de seguridad](../classes/parte-14-grc-riesgo-y-cumplimiento/285-auditoria-de-seguridad/README.md).

### Multi-stage build

Construcción con etapas separadas para no distribuir todas las herramientas.

**Aparece en 1 clase(s):** [Clase 243 — Imágenes y contenedores seguros en el pipeline](../classes/parte-11-devsecops-y-seguridad-del-sdlc/243-imagenes-y-contenedores-seguros-en-el-pipeline/README.md).

### Multiplicación escalar

Sumar `G` consigo mismo `k` veces; operación fundamental

**Aparece en 1 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md).

### Mutation

Operación que modifica datos

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### Mutex

Marcador que el malware crea para no reinfectar

**Aparece en 1 clase(s):** [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### Mythic

C2 modular sobre Docker con agentes y perfiles

**Aparece en 1 clase(s):** [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

## N

### n (módulo)

Producto de dos primos grandes; parte de ambas claves

**Aparece en 1 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md).

### Named pipe

Canal IPC de Windows usado por algunos implantes

**Aparece en 1 clase(s):** [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### Namespace

Aislamiento de recursos del kernel por contenedor

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### NAT

Modo de red: la VM sale, no es alcanzable desde fuera

**Aparece en 2 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md), [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md).

### NDA

Acuerdo de confidencialidad sobre lo descubierto

**Aparece en 2 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md), [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### Nessus

Escáner comercial estándar de la industria

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### netcat (nc)

Utilidad para leer/escribir en conexiones TCP/UDP

**Aparece en 1 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### netfilter

Subsistema del kernel que intercepta paquetes; el motor real

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### NetFlow v5

Formato clásico de Cisco, de campos fijos

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### NetFlow v9

Formato extensible mediante plantillas

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### Networking,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 342 — Arquitectura de videojuegos desde la perspectiva de seguridad](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/342-arquitectura-videojuegos-perspectiva-seguridad/README.md).

### NEW

Paquete que inicia una conexión nueva

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### NF

Variable de awk: número de campos de la línea

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### nfdump / SiLK

Herramientas de captura y consulta de flujos

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### nftables

Sustituto moderno y unificado de iptables/ip6tables/arptables/ebtables

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### Nibble

Grupo de 4 bits = un dígito hex

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### NIST CSF

Cybersecurity Framework del NIST, marco voluntario de gestión de riesgo

**Aparece en 1 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md).

### NIST SP 800-115

Guía oficial de pruebas de seguridad para cumplimiento

**Aparece en 1 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### NIST SP 800-207

Documento de referencia de la arquitectura zero trust

**Aparece en 1 clase(s):** [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md).

### NIST SP 800-63B

Guía moderna: listas de filtradas en vez de reglas de composición

**Aparece en 2 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md), [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md).

### Nivel de confianza

Cautela explícita en las afirmaciones de CTI

**Aparece en 1 clase(s):** [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md).

### Nivel lógico

Tensión que representa estados digitales; no asumir 5 V.

**Aparece en 1 clase(s):** [Clase 268 — Análisis de hardware: UART, JTAG y SPI](../classes/parte-13-seguridad-movil-iot-e-inalambrica/268-analisis-de-hardware-uart-jtag-y-spi/README.md).

### nmap-os-db

Base de firmas de sistemas operativos de Nmap

**Aparece en 1 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md).

### nmap-service-probes

Base de sondas y expresiones regulares de identificación

**Aparece en 1 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md).

### No filtrar, no invocar

La defensa: evitar la shell, no perseguir metacaracteres

**Aparece en 1 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### No inventes criptografía

Usar bibliotecas maduras en vez de implementaciones propias

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### No repudio

Imposibilidad de negar de forma creíble una acción realizada

**Aparece en 4 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md), [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md), [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md), [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### Nonce

*Number used once*; hace único el keystream de cada mensaje

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### Nonce en AEAD

Debe ser único por clave; repetirlo es catastrófico

**Aparece en 1 clase(s):** [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### Nonce/IV

Valor único por mensaje que aleatoriza el cifrado

**Aparece en 1 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md).

### Nonce k de ECDSA

Repetirlo o filtrarlo revela la clave privada

**Aparece en 1 clase(s):** [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### Nonce repetido

Fallo catastrófico en GCM y en cifrados de flujo

**Aparece en 2 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md), [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### Normalización

Conversión a formas comparables sin asumir identidad.

**Aparece en 1 clase(s):** [Clase 255 — Automatización de OSINT: SpiderFoot y Maltego](../classes/parte-12-osint-e-ingenieria-social/255-automatizacion-de-osint-spiderfoot-y-maltego/README.md).

### Normalizar peticiones

Defensa: rechazar peticiones ambiguas en el frontend

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### NoSQL

Bases no relacionales; MongoDB es documental (JSON)

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### NoSQLi ciega

Extraer datos con `$regex` carácter a carácter

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### Nota de rescate

Mensaje con branding que identifica la familia

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Notice

Evento destacado por un script como digno de revisión

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### NR

Variable de awk: número de registro (línea) actual

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### NSE

*Nmap Scripting Engine*: intérprete Lua embebido en Nmap

**Aparece en 2 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md), [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### nSEH

Puntero al siguiente registro de la cadena

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### NSM

Recolección y análisis de datos de red para detectar y responder

**Aparece en 1 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md).

### NT

Núcleo de las versiones modernas de Windows

**Aparece en 1 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md).

### NT headers

File Header + Optional Header; núcleo del PE

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### NTLM

Protocolo de autenticación de Windows basado en hash

**Aparece en 1 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### Número de syscall

Va en RAX (execve = 59 en x64)

**Aparece en 1 clase(s):** [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### Nunca confíes en el cliente

La validación real ocurre en el servidor

**Aparece en 1 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### NVD

Base de datos nacional de vulnerabilidades; indexa CVE por CPE

**Aparece en 1 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md).

### NX/DEP

Marca de memoria no ejecutable

**Aparece en 1 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md).

## O

### OAEP

Relleno probabilístico para **cifrar** con RSA

**Aparece en 1 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md).

### OAuth 2.0

Delegar acceso a recursos sin entregar la contraseña

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### Object.create(null)

Objeto sin prototipo; mitiga la pollution

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### Objeto

Dato tipado con propiedades y métodos que fluye por el pipeline

**Aparece en 1 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md).

### Objeto PDF

Elemento del árbol de un PDF

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### Observación,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 345 — Trainers e instrumentación del cliente](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/345-trainers-instrumentacion-cliente/README.md).

### Occlusion,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 347 — Rendering, visibilidad, occlusion y wallhack](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/347-rendering-visibilidad-occlusion-wallhack/README.md).

### OCSP

Consulta en línea del estado de un certificado

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### OCSP stapling

El servidor adjunta una respuesta OCSP firmada y reciente

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### Octal

Notación numérica de permisos (r=4, w=2, x=1)

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

### Octeto

Grupo de 8 bits; cada uno de los cuatro números de una IPv4.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### OEP

Original Entry Point; donde el stub salta al código real

**Aparece en 2 clase(s):** [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md), [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Off-by-one

Error de uno en un límite; a menudo pisa metadatos

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Offset

Bytes desde el inicio del buffer hasta la dirección de retorno

**Aparece en 1 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md).

### Offset de argumento

Índice `%N$p` que apunta a la entrada del atacante

**Aparece en 1 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### Offset en libc

Distancia fija de una función respecto a la base

**Aparece en 1 clase(s):** [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md).

### Ofuscación

Cifrar, codificar o trocear para evadir DLP por firmas

**Aparece en 3 clase(s):** [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md), [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md), [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### OIDC federation

Intercambio de identidad verificable por credenciales breves del proveedor.

**Aparece en 1 clase(s):** [Clase 242 — Seguridad en pipelines CI/CD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/242-seguridad-en-pipelines-ci-cd/README.md).

### OLE

Formato binario compuesto de Office antiguo (.doc/.xls)

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### oletools / olevba

Herramientas que extraen el VBA

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### One-time pad

Keystream verdaderamente aleatorio y de un solo uso; irrompible

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### OOXML

Formato ZIP de Office moderno (.docx/.xlsx)

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### Opcodes

Bytes en crudo de las instrucciones

**Aparece en 1 clase(s):** [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### open / filtered (ambiguo)

Estado indeterminado típico de UDP y de FIN/NULL/Xmas

**Aparece en 1 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### OpenID Connect (OIDC)

Capa de autenticación sobre OAuth

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### OpenVAS / Greenbone (GVM)

Alternativa open source

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### OpenVPN

VPN en espacio de usuario basada en TLS y PKI; muy flexible

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### Operación atómica

Comprobar y actuar sin ventana intermedia

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### Operador /

Apila una capa dentro de otra en Scapy

**Aparece en 1 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md).

### Operador de consulta

`$ne`, `$gt`, `$regex`, `$where` de MongoDB

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### Operation Charter

Documento breve que fija objetivo, flags, RoE y métricas del ejercicio

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### Optional Header

Entry point, base, subsistema, data directories

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### Oráculo

Condición observable que permite decidir si una prueba pasó o falló.

**Aparece en 2 clase(s):** [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md), [Clase 239 — DAST: análisis dinámico de aplicaciones](../classes/parte-11-devsecops-y-seguridad-del-sdlc/239-dast-analisis-dinamico-de-aplicaciones/README.md).

### Origen null

Valor que ciertos contextos envían; peligroso confiarlo

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### OSI

Modelo conceptual de referencia de 7 capas

**Aparece en 1 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md).

### OSINT — Open Source Intelligence

Recogida de información de fuentes públicas para dar verosimilitud al pretexto

**Claves de búsqueda normalizadas:** `osint`.

**Aparece en 3 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md), [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md), [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### OSS-Fuzz

Servicio de fuzzing continuo de proyectos abiertos

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### OSSTMM

Metodología con métricas (RAV) y enfoque científico

**Aparece en 1 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### Out-of-band

Exfiltrar por DNS/HTTP a un servidor del atacante

**Aparece en 1 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### Out-of-band (OOB)

Forzar a la BD a conectar fuera y exfiltrar por DNS/HTTP

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### Output encoding

Codificar el dato según contexto antes de insertarlo

**Aparece en 1 clase(s):** [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md).

### OVA / OVF

Formato de empaquetado e importación de VMs

**Aparece en 1 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md).

### Overflow de entero

Resultado que excede la capacidad del tipo

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Overflow en el tamaño

La reserva desborda y queda pequeña; copia posterior desborda

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Overlay

Datos añadidos al final, fuera de las secciones

**Aparece en 2 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md), [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### OverTheWire

Colección de wargames que comienza con Bandit para fundamentos de terminal y seguridad.

**Sitio oficial:** [OverTheWire](https://overthewire.org/wargames/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### OWASP A02

*Cryptographic Failures*: categoría del Top 10

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### OWASP ASVS

Estándar de verificación más detallado que el Top 10

**Aparece en 2 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md), [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### OWASP Top 10

Consenso de las diez categorías de riesgo web más críticas

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### OWASP WSTG

Guía de pruebas de seguridad para aplicaciones web

**Aparece en 1 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### OWASP ZAP

Proxy de pentesting web libre y gratuito de OWASP

**Aparece en 1 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md).

### OWE

Cifrado oportunista para redes abiertas

**Aparece en 1 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md).

### Ownership

Autoridad y obligación explícitas sobre decisiones y resultados.

**Aparece en 1 clase(s):** [Clase 248 — Cultura DevSecOps y security champions](../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md).

## Otros

### $(...)

Código de salida del último comando ejecutado

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### -A

Modo agresivo: versión, OS, scripts por defecto y traceroute

**Aparece en 1 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md).

### -C

Rotación por tamaño de fichero (MB)

**Aparece en 1 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### \d \w \s

Atajos: dígito, alfanumérico, espacio

**Aparece en 1 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md).

### --dbs

Lista las bases de datos

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### /dev/urandom

Fuente de aleatoriedad del kernel; equivalente en calidad

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### --dump

Vuelca el contenido de una tabla

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### /etc/group

Definición de grupos del sistema

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

### /etc/passwd

Definición de cuentas, legible por todos

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

### /etc/shadow

Hashes de contraseñas, legible solo por root

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

### /etc/sudoers

Configuración de reglas de sudo

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### -f (formato)

Envoltorio de salida: exe, elf, apk, psh, war, raw

**Aparece en 1 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### -G

Rotación por tiempo (segundos)

**Aparece en 1 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### .gitignore

Patrones de ficheros no rastreados

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### %hn / %hhn

Escriben 2 y 1 byte; para construir valores por partes

**Aparece en 1 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### -k

Intenta preservar la función del binario anfitrión

**Aparece en 1 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### --level (1-5)

Amplía dónde busca (cabeceras, cookies…); más peticiones

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### --min-rate

Fuerza un mínimo de paquetes por segundo

**Aparece en 1 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### φ(n)

No resolver nombres; evita DNS que contamina la propia captura

**Aparece en 3 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md), [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md), [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### -n / -R

Nunca resolver DNS / resolver siempre

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### $ne

"Distinto de"; con `""` coincide con cualquier valor

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### -O

Detección de sistema operativo por huella de pila TCP/IP

**Aparece en 2 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md), [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### -oA

Guarda salida en los tres formatos (normal, grepable y XML)

**Aparece en 2 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md), [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### /OpenAction

Acción que ejecuta código al abrir el PDF

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### --os-shell

Intenta ejecución de comandos; la opción más peligrosa

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### --osscan-guess

Propone la coincidencia más próxima cuando no hay una exacta

**Aparece en 1 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md).

### -p

Desactiva el modo promiscuo (captura solo lo dirigido al host)

**Aparece en 2 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md), [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### -p / -F / -p-

Selección de puertos: lista, los 100 frecuentes, todos

**Aparece en 1 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### %p / %x

Leen valores de la pila; base del info leak

**Aparece en 1 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### -PA

Sonda TCP ACK; atraviesa filtros sin estado

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### -PE / -PP / -PM

Sondas ICMP: echo, timestamp y address mask

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### -Pn

Omite el descubrimiento y trata todo objetivo como vivo

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### -PS

Sonda TCP SYN a un puerto para probar existencia del host

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### -PU

Sonda UDP; busca el ICMP *port unreachable*

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### -r

Objetivo tomado de una petición HTTP capturada

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### $regex

Coincidencia por patrón; base de la inyección ciega

**Aparece en 2 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md), [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### --risk (1-3)

Amplía qué payloads prueba; el alto puede modificar datos

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### --scan-delay

Espaciado entre sondas para evadir umbrales

**Aparece en 1 clase(s):** [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### --script

Selecciona scripts por nombre, categoría, patrón o expresión lógica

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### --script-args

Pasa parámetros a los scripts seleccionados

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### --script-help

Muestra la documentación de un script sin ejecutarlo

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### --script-updatedb

Reconstruye el índice tras añadir scripts propios

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### -sn

Solo descubrimiento de hosts; no escanea puertos

**Aparece en 1 clase(s):** [Clase 29 — Nmap: descubrimiento de hosts y técnicas de ping](../classes/parte-1-redes-y-seguridad-de-redes/029-nmap-descubrimiento-de-hosts-y-tecnicas-de-ping/README.md).

### $STANDARDINFORMATION / $FILENAME

Atributos NTFS cuya incoherencia delata manipulación

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### -sV

Detección de versión de servicio mediante banners y sondas

**Aparece en 1 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md).

### -T0…-T5

Plantillas de temporización: de sigiloso y lento a agresivo

**Aparece en 1 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### --tables / --columns

Enumera tablas y columnas

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### .text / .rodata / .data

Código / cadenas y constantes / datos inicializados

**Aparece en 1 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md).

### --top-ports

Escanea los N puertos más frecuentes según `nmap-services`

**Aparece en 1 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### -u

Objetivo indicado como URL

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### --version-intensity

Número de sondas a lanzar (0 = mínimo, 9 = exhaustivo)

**Aparece en 1 clase(s):** [Clase 31 — Nmap: detección de servicios y fingerprinting de OS](../classes/parte-1-redes-y-seguridad-de-redes/031-nmap-deteccion-de-servicios-y-fingerprinting-de-os/README.md).

### -W

Número máximo de ficheros conservados (buffer circular)

**Aparece en 1 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### -w / -r

Escribir la captura a fichero / leer un fichero existente

**Aparece en 1 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### $where

Evalúa JavaScript en el servidor; riesgo de RCE

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

## P

### p y g

Primo y generador públicos que definen el grupo

**Aparece en 1 clase(s):** [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### p64 / p32

Empaquetan un número en bytes little-endian (pwntools)

**Aparece en 2 clase(s):** [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md), [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Packer personalizado

Requiere unpacking manual o dinámico

**Aparece en 1 clase(s):** [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Packing

Comprimir/cifrar el código; un stub lo revela en memoria

**Aparece en 4 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md), [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md), [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md), [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Padding

Relleno `=` al final de un Base64

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### Padding oracle

Oráculo que revela si el relleno era válido; descifra sin clave

**Aparece en 2 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md), [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### Página

Unidad de memoria virtual (típicamente 4 KiB)

**Aparece en 1 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md).

### Pairing

Proceso que establece parámetros y claves de seguridad.

**Aparece en 1 clase(s):** [Clase 271 — Seguridad de Bluetooth y BLE](../classes/parte-13-seguridad-movil-iot-e-inalambrica/271-seguridad-de-bluetooth-y-ble/README.md).

### Paquete

PDU de la capa de red (lleva la cabecera IP)

**Aparece en 1 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md).

### Parada de emergencia

Procedimiento para detener envíos y retirar infraestructura.

**Aparece en 1 clase(s):** [Clase 258 — Campañas de phishing con GoPhish](../classes/parte-12-osint-e-ingenieria-social/258-campanas-de-phishing-con-gophish/README.md).

### Paradoja del cumpleaños

Las colisiones cuestan 2^(n/2), no 2^n

**Aparece en 2 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md), [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### Parámetros predecibles

Requisito: sin un secreto que el atacante no pueda poner

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### Parseo de parámetros

Frameworks que convierten la query string en objetos

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### Parser XML

Componente que procesa el XML; suele traer entidades activas

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### Pass-the-Hash

Autenticarse con el hash NTLM sin la contraseña en claro

**Aparece en 1 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### Pass-the-Ticket

Reutilizar tickets Kerberos robados

**Aparece en 1 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### Passive monitoring

Observación sin generar sondeo hacia activos OT.

**Aparece en 1 clase(s):** [Clase 273 — Seguridad de sistemas de control industrial (ICS/SCADA)](../classes/parte-13-seguridad-movil-iot-e-inalambrica/273-seguridad-de-sistemas-de-control-industrial-ics-scada/README.md).

### Password Hashing Competition

Concurso que seleccionó Argon2 en 2015

**Aparece en 1 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md).

### Password spraying

Una contraseña común contra muchas cuentas; evade el bloqueo

**Aparece en 2 clase(s):** [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md), [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### PAT

SNAT multiplexado por puerto; la forma doméstica habitual

**Aparece en 1 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md).

### PatchGuard

Impide modificar estructuras críticas del kernel

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### PATH

Lista de directorios donde la shell busca ejecutables

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### PATH escribible

Permite suplantar un binario invocado sin ruta absoluta

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### Path traversal

`../` para leer ficheros fuera del directorio previsto

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### Path traversal en el nombre

`../` en el nombre para colocar el fichero donde sea

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### Patrón de APIs

Combinación que revela una técnica conocida

**Aparece en 1 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### Patrón de correo

Formato `nombre.apellido@` para construir listas de usuarios

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### Patrón de De Bruijn

Secuencia con subcadenas únicas para localizar el offset

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### Patrón peligroso

Construcción con fallo conocido (strcpy, malloc(n*m)…)

**Aparece en 1 clase(s):** [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Paved road

Camino de desarrollo mantenido con controles seguros por defecto.

**Aparece en 1 clase(s):** [Clase 248 — Cultura DevSecOps y security champions](../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md).

### Payload

Carga que se prueba en una posición de inyección

**Claves de búsqueda normalizadas:** `carga util`.

**Aparece en 4 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md), [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md), [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md), [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Payload no cifrado

Solo codificado; cualquiera lo lee

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### Payload staged

Se envía en dos partes (stager + stage); notación con `/`

**Aparece en 1 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md).

### Payload stageless

Se envía completo; más grande y fiable; notación con `_`

**Aparece en 1 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md).

### pcap

Formato de archivo de captura de tráfico de red

**Aparece en 1 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md).

### pcapng

Formato de captura moderno, con metadatos y comentarios

**Aparece en 1 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md).

### PCRE

Expresión regular; precisa pero costosa, se pone tras un `content`

**Aparece en 2 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md), [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### PDCA

Ciclo de mejora continua: Plan, Do, Check, Act

**Aparece en 1 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md).

### pdf

Desensambla la función actual

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### PDP

*Policy Decision Point*: motor que decide permitir o denegar

**Aparece en 2 clase(s):** [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md), [Clase 244 — Políticas como código con OPA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/244-politicas-como-codigo-con-opa/README.md).

### PDU

Unidad de datos de protocolo (nombre por capa)

**Aparece en 2 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md), [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md).

### PE

Portable Executable; formato de ejecutables de Windows

**Aparece en 2 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md), [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### pe.imphash

Función que agrupa por tabla de imports

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### peepdf / pdfid

Herramientas de análisis de PDF

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### Pelado por capas

Revelar la ofuscación una capa cada vez

**Aparece en 1 clase(s):** [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### Penetration test

Evaluación técnica que busca demostrar el máximo de vías explotables

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### Pentest

Explotar debilidades para demostrar impacto; profundidad acotada

**Aparece en 2 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md), [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### PentesterLab

Plataforma centrada en seguridad web y revisión de código, con ejercicios guiados y contenido de pago.

**Sitio oficial:** [PentesterLab](https://pentesterlab.com/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### Pentesting

Evaluación autorizada que busca demostrar y documentar rutas de ataque dentro de un alcance, tiempo y reglas acordados.

**Claves de búsqueda normalizadas:** `penetration testing`, `prueba de penetracion`.

**Relacionados:** Reconocimiento, Enumeración, Explotación, Post-explotación.

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### PEP

*Policy Enforcement Point*: aplica la decisión en cada acceso

**Aparece en 2 clase(s):** [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md), [Clase 244 — Políticas como código con OPA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/244-politicas-como-codigo-con-opa/README.md).

### Pepper

Secreto global fuera de la base de datos; defensa adicional

**Aparece en 1 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md).

### Percent encoding

Sustitución `%XX` en URLs

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### Perezoso

Casa lo mínimo (`*?`)

**Aparece en 1 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md).

### Perfil

Estado actual frente a objetivo en las funciones del CSF

**Aparece en 3 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md), [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md), [Clase 279 — NIST Cybersecurity Framework](../classes/parte-14-grc-riesgo-y-cumplimiento/279-nist-cybersecurity-framework/README.md).

### Perímetro

Modelo que confía en todo lo que está "dentro" del firewall

**Aparece en 1 clase(s):** [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md).

### Permiso peligroso

SMS, contactos, ubicación, Accessibility

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### Permisos débiles de servicio

Permiten reconfigurar el binario del servicio

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### Persistencia

Mecanismo para sobrevivir al reinicio

**Aparece en 4 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md), [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md), [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md), [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### Persistencia Linux

cron, systemd, rc.local, .bashrc, SSH keys

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### Persistencia sin fichero

Código en el registro o en suscripciones WMI

**Aparece en 1 clase(s):** [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### Peticiones en paralelo

Enviar muchas a la vez para colarse en la ventana

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### Phishing resistance

Propiedad protocolaria que evita entregar una salida válida a un verificador impostor.

**Aparece en 1 clase(s):** [Clase 259 — Defensa contra la ingeniería social](../classes/parte-12-osint-e-ingenieria-social/259-defensa-contra-la-ingenieria-social/README.md).

### Phishing (T1566)

Envío de mensajes engañosos para inducir una acción (clic, credenciales, ejecución)

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### phpggc

Equivalente para PHP

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### pickle

Módulo de Python que ejecuta código al deserializar

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### PID

Identificador numérico único de un proceso

**Aparece en 2 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md), [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md).

### PIE

Aleatoriza la dirección de carga del propio binario

**Aparece en 2 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md), [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md).

### Pila como programa

La pila contiene la lista de direcciones de gadgets

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### Pila (stack)

Región LIFO con locales, argumentos y dirección de retorno

**Aparece en 2 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md), [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### Ping sweep

Barrido que descubre hosts activos mediante ICMP

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### Pinning

Fijación de una dependencia a una identidad inmutable, como SHA o digest.

**Aparece en 1 clase(s):** [Clase 242 — Seguridad en pipelines CI/CD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/242-seguridad-en-pipelines-ci-cd/README.md).

### pip

Gestor de paquetes de Python.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### Pipe (|)

Conecta la salida de un comando con la entrada de otro

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### pipefail

Hace fallar una tubería si cualquier etapa falla

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### Pipeline

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 347 — Rendering, visibilidad, occlusion y wallhack](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/347-rendering-visibilidad-occlusion-wallhack/README.md).

### Pipeline de triaje

Sistema que analiza muestras automáticamente

**Aparece en 1 clase(s):** [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Pirámide del dolor

Jerarquía de indicadores según lo caro que es evadirlos

**Aparece en 1 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md).

### Pista discriminante

Rasgo que diferencia candidatos de manera comprobable.

**Aparece en 1 clase(s):** [Clase 253 — Geolocalización y análisis de imágenes](../classes/parte-12-osint-e-ingenieria-social/253-geolocalizacion-y-analisis-de-imagenes/README.md).

### Pivoteo de infraestructura

Descubrir indicadores relacionados desde uno

**Aparece en 1 clase(s):** [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md).

### Pivoting

Usar un host comprometido para alcanzar redes inaccesibles

**Claves de búsqueda normalizadas:** `pivot`.

**Aparece en 2 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md), [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### PKCE

Protección del código para apps públicas

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### PKCS#1 v1.5

Relleno de firma antiguo, aún presente por compatibilidad

**Aparece en 2 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md), [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### PKCS#7

Relleno cuya validez se puede comprobar y por tanto filtrar

**Aparece en 2 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md), [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### PKI

Infraestructura que ata claves públicas a identidades vía certificados

**Aparece en 3 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md), [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md), [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### Plan de colección

Conjunto acotado de observaciones ligado a una pregunta.

**Aparece en 1 clase(s):** [Clase 334 — Reconocimiento y escaneo asistidos por IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/334-reconocimiento-y-escaneo-asistidos-por-ia/README.md).

### Plantilla como dato vs. como codigo

El fallo es construir la plantilla con entrada

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### Plantilla de política

Perfil de escaneo que acota intensidad y riesgo

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### Plantilla pwntools

Esqueleto de exploit con local/remoto conmutables

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### Plantilla (-x)

Incrustar el payload en un binario legítimo

**Aparece en 1 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### Plataforma de práctica

pwn.college, ROP Emporium, picoCTF, HackTheBox

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### PLC

Controlador que ejecuta lógica sobre entradas y salidas.

**Aparece en 1 clase(s):** [Clase 273 — Seguridad de sistemas de control industrial (ICS/SCADA)](../classes/parte-13-seguridad-movil-iot-e-inalambrica/273-seguridad-de-sistemas-de-control-industrial-ics-scada/README.md).

### PLT

Maquinaria que resuelve y llama a funciones externas

**Aparece en 1 clase(s):** [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md).

### Plugin / NVT

Comprobación individual de un escáner

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### PMF

Protección de ciertas tramas de gestión IEEE 802.11.

**Aparece en 1 clase(s):** [Clase 272 — Ataques WiFi avanzados: Evil Twin y PMKID](../classes/parte-13-seguridad-movil-iot-e-inalambrica/272-ataques-wifi-avanzados-evil-twin-y-pmkid/README.md).

### PMF (802.11w)

Autenticación de tramas de gestión; neutraliza el deauth

**Aparece en 1 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md).

### PMKID

Identificador derivado que algunas configuraciones exponen para gestión de claves.

**Aparece en 2 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md), [Clase 272 — Ataques WiFi avanzados: Evil Twin y PMKID](../classes/parte-13-seguridad-movil-iot-e-inalambrica/272-ataques-wifi-avanzados-evil-twin-y-pmkid/README.md).

### Política

Mandato de alto nivel aprobado por autoridad.

**Aparece en 1 clase(s):** [Clase 282 — Políticas, estándares y procedimientos](../classes/parte-14-grc-riesgo-y-cumplimiento/282-politicas-estandares-y-procedimientos/README.md).

### Política de contraseñas

Umbral de bloqueo; decide la estrategia de spraying

**Aparece en 2 clase(s):** [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md), [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md).

### Política del mismo origen

Impide que otro sitio lea el token

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### Política por defecto

Veredicto si ninguna regla coincide; en un firewall serio, `DROP`

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### Poly1305

Autenticador que acompaña a ChaCha20 para formar un AEAD

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### Polyglot

Fichero válido como imagen que además contiene código

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### POODLE

Downgrade a SSL 3.0 para explotar su relleno

**Aparece en 1 clase(s):** [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### POP POP RET

Gadget que salta de vuelta a nSEH controlado

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### pop rax; ret

Gadget para cargar el número de syscall

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### pop rdi; ret

Gadget que carga RDI con el argumento y continúa

**Aparece en 1 clase(s):** [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md).

### Port security

Limita las MAC aceptadas por puerto

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### Portador (cover)

Fichero o canal de apariencia inocente que aloja el mensaje

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### portrule

Se ejecuta una vez por puerto que cumpla la condición

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### Posicionamiento

Técnica para llegar a estar en medio (ARP, DNS, rogue AP…)

**Aparece en 1 clase(s):** [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md).

### Post

Módulo que opera sobre una sesión ya establecida

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### Post-explotación

Fase que demuestra el alcance real tras obtener acceso

**Claves de búsqueda normalizadas:** `post exploitation`.

**Aparece en 1 clase(s):** [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md).

### postMessage

API de comunicación entre ventanas de distinto origen

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### postrule

Se ejecuta al final para agregar resultados globales

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### Potestad para autorizar

Quien firma debe poder consentir sobre el activo (nube, SaaS)

**Aparece en 1 clase(s):** [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### powershell / mshta / certutil

LOLBins comunes en cadenas de entrega

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### PowerShell ofensivo

Acceso a la API y a .NET; carga en memoria

**Aparece en 1 clase(s):** [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### PowerSploit

Conjunto de módulos ofensivos en PowerShell

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### PPM

Error relativo de frecuencia del oscilador.

**Aparece en 1 clase(s):** [Clase 269 — Radio definida por software (SDR)](../classes/parte-13-seguridad-movil-iot-e-inalambrica/269-radio-definida-por-software-sdr/README.md).

### PPS / BPS

Paquetes y bits por segundo; miden presiones distintas frente a un baseline

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### PQC

Criptografía post-cuántica, resistente a computadores cuánticos

**Aparece en 2 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md), [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### Práctica deliberada

Ejercicio enfocado con feedback y dificultad calibrada.

**Aparece en 1 clase(s):** [Clase 310 — Plan de aprendizaje continuo y comunidad](../classes/parte-16-capstones-y-preparacion-de-certificaciones/310-plan-de-aprendizaje-continuo-y-comunidad/README.md).

### Precision,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 357 — Estadística, anomalías y falsos positivos](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/357-estadistica-anomalias-falsos-positivos/README.md).

### Predicción,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 2 clase(s):** [Clase 351 — Multiplayer y autoridad: nunca confiar en el cliente](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/351-multiplayer-autoridad-nunca-confiar-cliente/README.md), [Clase 352 — Seguridad del protocolo de juego](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/352-seguridad-protocolo-juego/README.md).

### Prefijo

Número de bits de red en notación CIDR (por ejemplo /26).

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### Preimagen

Encontrar una entrada que produzca un digest dado

**Aparece en 1 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md).

### Prepared statement

Nombre técnico de la consulta parametrizada

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### PREROUTING / POSTROUTING

Ganchos antes y después de la decisión de ruta (NAT)

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### prerule

Fase previa al escaneo; no depende de ningún host

**Aparece en 1 clase(s):** [Clase 32 — Nmap Scripting Engine (NSE)](../classes/parte-1-redes-y-seguridad-de-redes/032-nmap-scripting-engine-nse/README.md).

### Preservación de evidencia

Deber ético del consultor; no destruir huellas

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### Pretexting

Uso de una historia para legitimar identidad y solicitud.

**Aparece en 1 clase(s):** [Clase 257 — Pretexting y vishing](../classes/parte-12-osint-e-ingenieria-social/257-pretexting-y-vishing/README.md).

### Pretexto

Historia que motiva la acción del objetivo; el verdadero "exploit" de la campaña

**Aparece en 2 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md), [Clase 256 — Fundamentos de ingeniería social](../classes/parte-12-osint-e-ingenieria-social/256-fundamentos-de-ingenieria-social/README.md).

### Prevalencia

Con qué frecuencia aparece un fallo en aplicaciones reales

**Aparece en 1 clase(s):** [Clase 87 — OWASP Top 10: panorama general](../classes/parte-4-seguridad-de-aplicaciones-web/087-owasp-top-10-panorama-general/README.md).

### PREVINUSE

Flag que indica si el chunk anterior está en uso

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### Primitiva

Capacidad elemental que concede una vulnerabilidad

**Aparece en 1 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### Primitiva BPF

Pieza del filtro: tipo (`host`), dirección (`src`) o protocolo (`tcp`)

**Aparece en 1 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### Primitiva obsoleta

DES, 3DES, MD5, SHA-1, RC4, ECB

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### Principio de Kerckhoffs

Todo puede ser público salvo la clave

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### printf(entrada)

Uso vulnerable; lo correcto es `printf("%s", entrada)`

**Aparece en 1 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### PrintSpoofer / JuicyPotato

Implementaciones concretas del ataque Potato

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### Priorización

Ordenar por riesgo real para no malgastar recursos

**Aparece en 2 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md), [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md).

### Priorización por explotabilidad

Centrarse en los bugs realmente alcanzables

**Aparece en 1 clase(s):** [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Priorización por retorno

Ir donde es probable un bug pagado

**Aparece en 1 clase(s):** [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### Privacidad,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 353 — Arquitecturas Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/353-arquitecturas-anticheat/README.md).

### Privilegios

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 359 — Privacidad, gobernanza, sanciones y seguridad del propio Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/359-privacidad-gobernanza-sanciones-seguridad-anticheat/README.md).

### PRNG

Generador determinista; parece aleatorio pero es predecible

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### Problema de factorización

Base de la seguridad de RSA

**Aparece en 1 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md).

### Procedencia

Evidencia de qué proceso e insumos produjeron un artefacto.

**Aparece en 2 clase(s):** [Clase 242 — Seguridad en pipelines CI/CD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/242-seguridad-en-pipelines-ci-cd/README.md), [Clase 249 — Fundamentos de OSINT](../classes/parte-12-osint-e-ingenieria-social/249-fundamentos-de-osint/README.md).

### Procedimiento

Implementación concreta de una técnica por un actor real

**Aparece en 2 clase(s):** [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md), [Clase 282 — Políticas, estándares y procedimientos](../classes/parte-14-grc-riesgo-y-cumplimiento/282-politicas-estandares-y-procedimientos/README.md).

### Proceso

Programa en ejecución con memoria propia

**Aparece en 1 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md).

### Proceso desenlazado

Sacado de la lista del kernel; sigue ejecutándose

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### Proceso oculto

Proceso que un rootkit esconde; visible en memoria

**Aparece en 1 clase(s):** [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### process()

Lanza el binario local

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Process Hacker

Muestra el árbol de procesos, memoria y handles

**Aparece en 1 clase(s):** [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### Process hollowing

Vaciar un proceso suspendido y reemplazar su código

**Aparece en 2 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md), [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### Process Monitor (ProcMon)

Registra operaciones de ficheros, registro, procesos, red

**Aparece en 1 clase(s):** [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### process() / remote()

Ejecución local / conexión al servicio del reto

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### Producto IoT

Dispositivo y servicios necesarios para su función.

**Aparece en 1 clase(s):** [Clase 266 — Seguridad de IoT: panorama y superficie de ataque](../classes/parte-13-seguridad-movil-iot-e-inalambrica/266-seguridad-de-iot-panorama-y-superficie-de-ataque/README.md).

### Programa

Reglas y alcance de una organización

**Aparece en 1 clase(s):** [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### ProGuard / R8

Ofuscadores que renombran clases y métodos

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### Prólogo / epílogo

Código que crea/destruye el marco de función

**Aparece en 2 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md), [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### Proof of impact

Evidencia mínima suficiente del efecto autorizado.

**Aparece en 1 clase(s):** [Clase 335 — Explotación y post-explotación autorizada asistida por IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/335-explotacion-y-post-explotacion-autorizada-asistida-por-ia/README.md).

### Propagación de error

Ampliación de una asociación incorrecta a resultados posteriores.

**Aparece en 1 clase(s):** [Clase 255 — Automatización de OSINT: SpiderFoot y Maltego](../classes/parte-12-osint-e-ingenieria-social/255-automatizacion-de-osint-spiderfoot-y-maltego/README.md).

### Propiedad de seguridad

Condición verificable que debe mantenerse, incluso ante entradas hostiles.

**Aparece en 1 clase(s):** [Clase 236 — Secure SDLC y filosofía shift-left](../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md).

### Proporcionalidad

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 359 — Privacidad, gobernanza, sanciones y seguridad del propio Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/359-privacidad-gobernanza-sanciones-seguridad-anticheat/README.md).

### proto

Propiedad cuya escritura provoca la contaminación

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### proto[off:len]

Acceso directo a bytes de una cabecera dentro del filtro

**Aparece en 1 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### Protocolo de handshake

Negocia parámetros, autentica y establece claves

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### Protocolo de registro

Trocea y protege los datos ya con las claves de sesión

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### Prototype pollution

Contaminar `Object.prototype` desde el que heredan todos

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### Provenance

Evidencia de materiales, builder y pasos que produjeron un artefacto.

**Aparece en 1 clase(s):** [Clase 246 — Supply chain security: SBOM y SLSA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md).

### Provenance de informe

Relación entre afirmación, fuente, transformación y aprobador.

**Aparece en 1 clase(s):** [Clase 338 — Generación de informes y flujos de trabajo con IA](../classes/parte-18-ia-aplicada-a-la-ciberseguridad/338-generacion-de-informes-y-flujos-de-trabajo-con-ia/README.md).

### Provisioning

Incorporación inicial de identidad, claves y configuración.

**Aparece en 1 clase(s):** [Clase 266 — Seguridad de IoT: panorama y superficie de ataque](../classes/parte-13-seguridad-movil-iot-e-inalambrica/266-seguridad-de-iot-panorama-y-superficie-de-ataque/README.md).

### Provocar excepción

Forzar el fallo para que se invoque el Handler

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### Proxy

Intermediario que reenvía tráfico en nombre de otro

**Aparece en 1 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md).

### Proxy de interceptación

Se sitúa entre navegador y servidor para ver y editar el tráfico

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### Proxy hacia dentro

El servidor alcanza lo que el atacante no puede

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### Proxy transparente

Intermediario que intercepta sin que el cliente lo configure

**Aparece en 1 clase(s):** [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md).

### proxychains

Fuerza el tráfico de una herramienta a través de un proxy

**Aparece en 2 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md), [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### Proyecto

Agrupación de binarios en Ghidra

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### Prueba de concepto

`alert(1)`; demuestra la ejecución sin causar daño

**Aparece en 1 clase(s):** [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md).

### Prueba lógica

`AND 1=1` vs `AND 1=2` para confirmar sin errores

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### Prueba negativa

Caso que exige rechazar una acción inválida o no autorizada.

**Aparece en 1 clase(s):** [Clase 247 — Seguridad de APIs en el ciclo de desarrollo](../classes/parte-11-devsecops-y-seguridad-del-sdlc/247-seguridad-de-apis-en-el-ciclo-de-desarrollo/README.md).

### Pruebas de aleatoriedad

Baterías estadísticas que detectan sesgos

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### Pseudo-C

Aproximación en C que produce el decompilador

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### PsExec

Ejecución remota vía SMB creando un servicio temporal

**Aparece en 1 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### PSS

Relleno probabilístico para **firmar** con RSA

**Aparece en 1 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md).

### PTES

Estándar de facto en siete fases para estructurar un pentest

**Aparece en 1 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### ptmalloc

Allocator por defecto de glibc

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### ptrace

Syscall usada para detectar depuradores en Linux

**Aparece en 2 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md), [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md).

### Puente a heap overflow

El bug numérico habilita la corrupción de memoria

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Puerto

Identificador de aplicación dentro de un host (capa 4)

**Aparece en 1 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md).

### Puntero colgante

Puntero que sobrevive al `free` de su memoria

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### Puntero next

Enlace de la lista tcache, dentro del chunk

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### Punteros en chunks liberados

Enlaces de las listas; objetivo de la corrupción

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### Punto de entrada

Lugar por donde el atacante introduce datos

**Aparece en 1 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### Punto de estrangulamiento

Enlace por el que pasa el tráfico que interesa vigilar

**Aparece en 1 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md).

### Punto generador G

Punto base público fijado por los parámetros de la curva

**Aparece en 1 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md).

### Puntuación de riesgo

CVSS combinado con el contexto de negocio

**Aparece en 1 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md).

### Purple team

Colaboración en tiempo real de Red y Blue para mejorar detecciones

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### push / pop

Apilar y desapilar datos

**Aparece en 1 clase(s):** [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### push / pull

Sincronizan con el remoto

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### Pwn

Categoría de explotación de binarios

**Claves de búsqueda normalizadas:** `binary exploitation`.

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### pwn.college

Plataforma educativa gratuita de seguridad práctica; sus reglas restringen publicar walkthroughs de desafíos.

**Sitio oficial:** [pwn.college](https://pwn.college/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### pwndbg

Extensión de GDB orientada al exploiting

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### pwninit

Herramienta que engancha la libc del reto al binario

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### pwntools

Librería de Python para construir y lanzar exploits

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Pyramid of Pain

Modelo que jerarquiza los IOC por su coste para el adversario

**Aparece en 2 clase(s):** [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md), [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

## Q

### QEMU + módulo

Entorno de práctica aislado para kernel

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### Qiling

Emula CPU y SO; ejecuta binarios completos

**Aparece en 1 clase(s):** [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Qubit

Unidad cuántica que puede estar en superposición de estados

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### Qubit lógico

Qubit corregido de errores; hacen falta muchos físicos por cada uno

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### Quemado (burned)

Activo detectado o bloqueado por el defensor

**Aparece en 1 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### Query

Consulta que expresa un patrón de vulnerabilidad

**Aparece en 2 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md), [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### QUIC

Transporte sobre UDP que sustenta HTTP/3 y reduce latencia.

**Aparece en 1 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md).

## R

### r2pipe

API para controlar r2 desde un script

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### RaaS

Ransomware as a Service: modelo de alquiler del malware

**Aparece en 2 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md), [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### Race condition

Explotar la ventana entre comprobar y actuar

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### radare2 / rizin

Suite de RE libre, ligera y de línea de comandos

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### Rainbow table

Tabla precomputada contraseña→hash; el salt la inutiliza

**Aparece en 2 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md), [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### Rama

Puntero móvil a un commit

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### Randomización en GDB

GDB desactiva ASLR por defecto; puede falsear pruebas

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### Ransomware

Cifra los datos y exige un rescate

**Aparece en 2 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md), [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### RAT

Troyano de acceso remoto interactivo

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### Rate

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 354 — Server-side Anti-Cheat y diseño autoritativo](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/354-server-side-anticheat-diseno-autoritativo/README.md).

### Rate limit

Restricción de frecuencia; debe considerar identidad, operación y coste.

**Aparece en 1 clase(s):** [Clase 247 — Seguridad de APIs en el ciclo de desarrollo](../classes/parte-11-devsecops-y-seguridad-del-sdlc/247-seguridad-de-apis-en-el-ciclo-de-desarrollo/README.md).

### Rate limiting

Limitar llamadas; crítico en consumo programático

**Aparece en 2 clase(s):** [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md), [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### Rate limiting por operación

Contar operaciones, no peticiones HTTP

**Aparece en 1 clase(s):** [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### Raw offset

Desplazamiento en el fichero en disco

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### Raw socket

Socket que permite construir cabeceras a mano; exige privilegios

**Aparece en 2 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md), [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### RAX

Registro que suele contener el valor de retorno

**Aparece en 2 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md), [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### RAX / EAX / AX / AL

El mismo registro en 64, 32, 16 y 8 bits

**Aparece en 1 clase(s):** [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### RBAC

Control de acceso basado en roles

**Aparece en 1 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md).

### RBP

Puntero a la base del marco actual

**Aparece en 1 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md).

### RC4

Cifrado de flujo obsoleto; keystream con sesgos explotables

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### RCA — Análisis de causa raíz

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Claves de búsqueda normalizadas:** `rca`, `root cause analysis`.

**Aparece en 1 clase(s):** [Clase 360 — Capstone: incidente completo de Game Security](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/360-capstone-incidente-completo-game-security/README.md).

### RCE

Ejecución remota de código; el impacto de esta clase

**Aparece en 1 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### RDAP

Protocolo estructurado para consultar datos de registro de recursos de Internet.

**Aparece en 1 clase(s):** [Clase 251 — OSINT de empresas y dominios](../classes/parte-12-osint-e-ingenieria-social/251-osint-de-empresas-y-dominios/README.md).

### RDI, RSI, RDX, RCX, R8, R9

Los seis primeros argumentos en x64, en ese orden

**Aparece en 1 clase(s):** [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### Reachability

Evidencia de que el código vulnerable puede alcanzarse desde el producto.

**Aparece en 1 clase(s):** [Clase 240 — SCA: dependencias y riesgo de terceros](../classes/parte-11-devsecops-y-seguridad-del-sdlc/240-sca-dependencias-y-riesgo-de-terceros/README.md).

### Reaction

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 356 — Detección de aimbot y automatización por comportamiento](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/356-deteccion-aimbot-automatizacion-comportamiento/README.md).

### Reapertura

Evidencia de que la corrección no eliminó o reintrodujo el problema.

**Aparece en 1 clase(s):** [Clase 245 — Gestión de vulnerabilidades a escala](../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md).

### Reasignación

El allocator entrega el chunk liberado a otra petición

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### Reciclar el chunk

Pedir memoria del mismo tamaño para controlar el contenido

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### Recoil,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 349 — Aimbot avanzado, predicción, smoothing y recoil](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/349-aimbot-avanzado-prediccion-smoothing-recoil/README.md).

### Recolección del offset

Medir la distancia a RIP con `cyclic`

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Recomendación accionable

Acción concreta que reduce el riesgo

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### Recon iterativo

Cada dato hallado abre nuevas consultas

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### Reconciliación

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 354 — Server-side Anti-Cheat y diseño autoritativo](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/354-server-side-anticheat-diseno-autoritativo/README.md).

### Reconocimiento activo

Recolección enviando tráfico directo al objetivo

**Aparece en 1 clase(s):** [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### Reconocimiento eficiente

Subdominios, JS y endpoints con buen retorno

**Aparece en 1 clase(s):** [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### Reconocimiento pasivo

Recolección sin enviar tráfico al objetivo

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### Reconstrucción de IAT

Regenerar la tabla de imports del binario volcado

**Aparece en 1 clase(s):** [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Recuperación a userland

Volver limpio tras ganar privilegios

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### Recuperación de contraseña

Camino alternativo al login, a menudo el más débil

**Aparece en 1 clase(s):** [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### Recursos incrustados

Binarios o datos escondidos dentro del PE

**Aparece en 1 clase(s):** [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md).

### Red interna

Servicios que confían en el tráfico de dentro

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### Red team

Emulación de un adversario con objetivo para medir detección y respuesta

**Aparece en 2 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md), [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### Red zone

128 bytes bajo RSP usables por funciones hoja

**Aparece en 1 clase(s):** [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### Redirección

La URL permitida redirige a una interna

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### Redirector

Proxy sacrificable que reenvía tráfico válido y descarta el resto

**Aparece en 1 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### Redirector DNS

Redirector que reenvía tráfico C2 sobre consultas DNS

**Aparece en 1 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### redirecturi

URL de retorno; debe validarse con allowlist estricto

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### ReDoS

DoS por retroceso catastrófico de una regex

**Aparece en 1 clase(s):** [Clase 19 — Expresiones regulares para análisis de logs y datos](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md).

### Reempaquetado

Reconstrucción y firma de una copia autorizada para laboratorio.

**Aparece en 1 clase(s):** [Clase 265 — Ingeniería inversa de aplicaciones móviles](../classes/parte-13-seguridad-movil-iot-e-inalambrica/265-ingenieria-inversa-de-aplicaciones-moviles/README.md).

### Reenvío inmediato de logs

Enviar los registros fuera antes de que se borren

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### Referencia cruzada

Relación entre uso y definición en un binario.

**Aparece en 1 clase(s):** [Clase 265 — Ingeniería inversa de aplicaciones móviles](../classes/parte-13-seguridad-movil-iot-e-inalambrica/265-ingenieria-inversa-de-aplicaciones-moviles/README.md).

### Referencias

Fuentes que respaldan hallazgo y remediación

**Aparece en 1 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md).

### Reflective loading

Cargar un ensamblado en memoria sin tocar disco

**Aparece en 1 clase(s):** [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### Reflejar el Origin

Fallo: devolver el Origin recibido con credenciales

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### Refutación

Búsqueda deliberada de incompatibilidades con una hipótesis.

**Aparece en 1 clase(s):** [Clase 253 — Geolocalización y análisis de imágenes](../classes/parte-12-osint-e-ingenieria-social/253-geolocalizacion-y-analisis-de-imagenes/README.md).

### Regeneración de ID

Cambiar el ID al autenticar; anula la fixation

**Aparece en 1 clase(s):** [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### Registro

Almacenamiento interno rapidísimo de la CPU

**Aparece en 2 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md), [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md).

### Registro A

Mapeo de nombre a dirección IPv4.

**Aparece en 1 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md).

### Registro (GPR)

Celda de memoria ultrarrápida de la CPU (RAX…R15)

**Aparece en 1 clase(s):** [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### Registros de syscall

RAX (número), RDI/RSI/RDX (argumentos)

**Aparece en 1 clase(s):** [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### Registros DNS públicos

MX, TXT, SPF que revelan infraestructura

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### Regla

Unidad de YARA: meta, strings y condition

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Regla por familia

Captura lo común al linaje; caza variantes

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Regla YARA / MISP

Entregables de detección y de compartición

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### Reglas de mutación

Transforman el diccionario imitando hábitos humanos

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### Rego

Lenguaje declarativo usado por OPA.

**Aparece en 1 clase(s):** [Clase 244 — Políticas como código con OPA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/244-politicas-como-codigo-con-opa/README.md).

### Regshot

Diff del registro antes y después

**Aparece en 1 clase(s):** [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### Rehash en login

Recalcular el hash de contraseña con parámetros más fuertes

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### RELATED

Tráfico asociado a otra conexión (datos de FTP, ICMP correspondiente)

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### Relleno (padding)

Bytes de relación hasta la dirección de retorno

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### RELRO

Protege la GOT (partial: escribible; full: solo lectura)

**Aparece en 1 clase(s):** [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md).

### Remediación

Consultas parametrizadas, igual que en la inyección directa

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### Remediación accionable

Corrección concreta y realista, no genérica

**Aparece en 1 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md).

### REMnux

Distro Linux de análisis de malware

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### remote()

Conecta al servicio remoto; misma lógica que local

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Remote forwarding (-R)

Puerto de vuelta cuando el pivote no puede salir

**Aparece en 1 clase(s):** [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### Remoto

Copia del repo en otra máquina

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### Renombrar

Descartar el nombre original; anula traversal y doble ext.

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### Renombrar / comentar

Añadir el significado que el compilador borró

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### Repeater

Reenvío manual y reproducible de peticiones

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### Replay,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 2 clase(s):** [Clase 270 — Ataques a RFID y NFC](../classes/parte-13-seguridad-movil-iot-e-inalambrica/270-ataques-a-rfid-y-nfc/README.md), [Clase 352 — Seguridad del protocolo de juego](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/352-seguridad-protocolo-juego/README.md).

### Reporte

Producto que se paga; claro y reproducible

**Aparece en 1 clase(s):** [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### Reporte de análisis

Documento que comunica los resultados del análisis

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### Representación

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 344 — Estado del juego, memoria y manipulación controlada](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/344-estado-juego-memoria-manipulacion-controlada/README.md).

### Request smuggling

Colar parte de una petición en la de otro usuario

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Requisito de inteligencia

Pregunta ligada a una decisión y a un alcance.

**Aparece en 1 clase(s):** [Clase 249 — Fundamentos de OSINT](../classes/parte-12-osint-e-ingenieria-social/249-fundamentos-de-osint/README.md).

### Resistencia a manipulación

Propiedad física del HSM frente a extracción

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### Resolución de entidades

Evaluación de si registros distintos representan al mismo sujeto.

**Aparece en 1 clase(s):** [Clase 250 — OSINT de personas](../classes/parte-12-osint-e-ingenieria-social/250-osint-de-personas/README.md).

### Resolución dinámica de APIs

Obtener funciones en ejecución para ocultarlas

**Aparece en 1 clase(s):** [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### Resolver

Servidor recursivo que resuelve consultas en nombre del cliente.

**Aparece en 2 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md), [Clase 111 — Seguridad de APIs GraphQL](../classes/parte-4-seguridad-de-aplicaciones-web/111-seguridad-de-apis-graphql/README.md).

### Resolver API hashing

Emular la rutina que resuelve las APIs por hash

**Aparece en 1 clase(s):** [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Resolver recursivo

Servidor que resuelve consultas por el cliente y cachea el resultado

**Aparece en 1 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md).

### Resource owner

El usuario dueño de los datos

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### Resource server

Donde están los datos protegidos

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### Respuesta a incidentes

Necesita IOCs accionables para contener

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### Respuestas neutras

Mensaje y tiempo idénticos existan o no las cuentas

**Aparece en 1 clase(s):** [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### Resumen ejecutivo

Sección para la dirección; riesgo de negocio, sin jerga

**Aparece en 2 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md), [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### ret como pegamento

Cada `ret` salta al siguiente gadget de la pila

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### ret2dlresolve

Resolver funciones sin leak, abusando del enlazador

**Aparece en 1 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### ret2libc

Saltar a funciones de libc en vez de inyectar shellcode

**Aparece en 1 clase(s):** [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md).

### ret2syscall

Cadena que prepara y ejecuta una syscall (execve)

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### ret2usr

Ataque que SMEP bloquea

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### ret2win

Redirigir RIP a una función "ganadora" del propio binario

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Retención/deducible

Parte inicial de pérdida asumida por asegurado.

**Aparece en 1 clase(s):** [Clase 288 — Seguros cibernéticos](../classes/parte-14-grc-riesgo-y-cumplimiento/288-seguros-ciberneticos/README.md).

### Retención y destrucción

Cómo se custodia y elimina la evidencia tras el cierre

**Aparece en 1 clase(s):** [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### Retest

Volver a comprobar que las correcciones funcionan

**Aparece en 1 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md).

### Retículos

Familia matemática base de ML-KEM y ML-DSA

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### Retipar estructuras

Declarar tipos para que la decompilación sea legible

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### Retransmisión

Reenvío de un segmento no confirmado; indica pérdida

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### Retrohunt

Buscar en el histórico de VirusTotal con una regla

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Retrospectiva

Revisión de decisiones, límites y siguiente mejora.

**Aparece en 10 clase(s):** [Clase 301 — Roadmap de certificaciones: CompTIA, OSCP, CISSP y más](../classes/parte-16-capstones-y-preparacion-de-certificaciones/301-roadmap-de-certificaciones-comptia-oscp-cissp-y-mas/README.md), [Clase 302 — Preparación OSCP: mentalidad Try Harder](../classes/parte-16-capstones-y-preparacion-de-certificaciones/302-preparacion-oscp-mentalidad-try-harder/README.md), [Clase 303 — Capstone: laboratorio completo de pentest](../classes/parte-16-capstones-y-preparacion-de-certificaciones/303-capstone-laboratorio-completo-de-pentest/README.md), [Clase 304 — Preparación CISSP: los 8 dominios](../classes/parte-16-capstones-y-preparacion-de-certificaciones/304-preparacion-cissp-los-8-dominios/README.md), [Clase 305 — Capstone: operación Red Team end-to-end](../classes/parte-16-capstones-y-preparacion-de-certificaciones/305-capstone-operacion-red-team-end-to-end/README.md), [Clase 306 — Capstone: detección Blue Team end-to-end](../classes/parte-16-capstones-y-preparacion-de-certificaciones/306-capstone-deteccion-blue-team-end-to-end/README.md), [Clase 307 — Capstone: respuesta a incidentes DFIR end-to-end](../classes/parte-16-capstones-y-preparacion-de-certificaciones/307-capstone-respuesta-a-incidentes-dfir-end-to-end/README.md), [Clase 308 — Capstone: campaña de bug bounty](../classes/parte-16-capstones-y-preparacion-de-certificaciones/308-capstone-campana-de-bug-bounty/README.md), [Clase 309 — Construcción de portafolio y home lab permanente](../classes/parte-16-capstones-y-preparacion-de-certificaciones/309-construccion-de-portafolio-y-home-lab-permanente/README.md), [Clase 310 — Plan de aprendizaje continuo y comunidad](../classes/parte-16-capstones-y-preparacion-de-certificaciones/310-plan-de-aprendizaje-continuo-y-comunidad/README.md).

### Reutilización de código

ret2libc y ROP en vez de inyectar shellcode

**Aparece en 2 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md), [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md).

### Reutilización de conexión

Varias peticiones sobre la misma conexión TCP

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Reutilización de contraseñas

Motivo por el que una filtración da acceso

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### Reutilización de credenciales

Un administrador compartido abre muchas máquinas

**Aparece en 1 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### Reutilización de nonce

Cancela el keystream y destruye la confidencialidad

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### rev

Categoría de ingeniería inversa

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### Reverse shell

El objetivo conecta hacia el atacante; atraviesa NAT/firewall

**Aparece en 2 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md), [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### Reversibilidad

Volver a un estado limpio tras cada ejecución

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### Reversing

Entender un programa desde su forma compilada

**Claves de búsqueda normalizadas:** `ingenieria inversa`, `reverse engineering`.

**Aparece en 1 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md).

### Revocación

Invalidar una clave o certificado comprometido

**Aparece en 2 clase(s):** [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md), [Clase 241 — Secretos en el código y pre-commit hooks](../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md).

### Revocación de JWT

Difícil antes de expirar; exige TTL cortos o lista negra

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### RFC 1918

Rangos privados no enrutables en Internet.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### RFLAGS

Indicadores (cero, acarreo, signo) que rigen los saltos

**Aparece en 1 clase(s):** [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### RHOSTS

Objetivo del exploit

**Aparece en 1 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md).

### Riesgo de negocio

Impacto en dinero, reputación, cumplimiento, continuidad

**Aparece en 1 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md).

### Riesgo residual

Exposición que permanece después del tratamiento.

**Aparece en 31 clase(s):** [Clase 245 — Gestión de vulnerabilidades a escala](../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md), [Clase 291 — Introducción a la seguridad de IA y ML](../classes/parte-15-seguridad-de-ia-y-machine-learning/291-introduccion-a-la-seguridad-de-ia-y-ml/README.md), [Clase 292 — Ataques adversariales a modelos](../classes/parte-15-seguridad-de-ia-y-machine-learning/292-ataques-adversariales-a-modelos/README.md), [Clase 293 — Envenenamiento de datos y modelos](../classes/parte-15-seguridad-de-ia-y-machine-learning/293-envenenamiento-de-datos-y-modelos/README.md), [Clase 294 — Robo y extracción de modelos](../classes/parte-15-seguridad-de-ia-y-machine-learning/294-robo-y-extraccion-de-modelos/README.md), [Clase 295 — OWASP Top 10 para aplicaciones con LLM](../classes/parte-15-seguridad-de-ia-y-machine-learning/295-owasp-top-10-para-aplicaciones-con-llm/README.md), [Clase 296 — Prompt injection y jailbreaks](../classes/parte-15-seguridad-de-ia-y-machine-learning/296-prompt-injection-y-jailbreaks/README.md), [Clase 297 — Seguridad de aplicaciones con LLM: RAG y agentes](../classes/parte-15-seguridad-de-ia-y-machine-learning/297-seguridad-de-aplicaciones-con-llm-rag-y-agentes/README.md), [Clase 298 — IA aplicada a la defensa: detección y SOC](../classes/parte-15-seguridad-de-ia-y-machine-learning/298-ia-aplicada-a-la-defensa-deteccion-y-soc/README.md), [Clase 299 — IA ofensiva y deepfakes](../classes/parte-15-seguridad-de-ia-y-machine-learning/299-ia-ofensiva-y-deepfakes/README.md) y 21 más.

### Rigidez (rigidity)

Que los parámetros se elijan por criterios públicos y sin margen

**Aparece en 1 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md).

### Ring 0

Máximo privilegio; control total del sistema

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### RIP

Puntero de instrucción; controlarlo controla la ejecución

**Aparece en 2 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md), [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### Robo de sesión

Enviar `document.cookie` al atacante para suplantar

**Aparece en 1 clase(s):** [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md).

### robots.txt

Lista rutas que el dueño no quiere indexar

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### Robustez

Desempeño bajo variaciones definidas, no inmunidad universal.

**Aparece en 2 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md), [Clase 292 — Ataques adversariales a modelos](../classes/parte-15-seguridad-de-ia-y-machine-learning/292-ataques-adversariales-a-modelos/README.md).

### rockyou

Diccionario clásico de contraseñas filtradas

**Aparece en 1 clase(s):** [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### RoE

Reglas de engagement: ventanas, técnicas y límites operativos

**Aparece en 2 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md), [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### Rol

Posición jurídica u operativa que determina obligaciones.

**Aparece en 1 clase(s):** [Clase 281 — Cumplimiento: GDPR, HIPAA y PCI-DSS](../classes/parte-14-grc-riesgo-y-cumplimiento/281-cumplimiento-gdpr-hipaa-y-pci-dss/README.md).

### Ronda

Repetición de las operaciones internas de AES (10, 12 o 14)

**Aparece en 1 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md).

### root

Superusuario (UID 0) que ignora los permisos tradicionales

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

### Root of trust

Componente protegido en el que comienza una decisión de confianza.

**Aparece en 1 clase(s):** [Clase 267 — Hacking de firmware](../classes/parte-13-seguridad-movil-iot-e-inalambrica/267-hacking-de-firmware/README.md).

### Rootfs

Sistema de archivos raíz usado por el runtime embebido.

**Aparece en 1 clase(s):** [Clase 267 — Hacking de firmware](../classes/parte-13-seguridad-movil-iot-e-inalambrica/267-hacking-de-firmware/README.md).

### Rootkit

Malware cuyo fin es ocultarse manipulando el SO

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### Rootkit / bootkit

Oculta su presencia / se carga antes que el SO

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### Rootkit de kernel

Opera en ring 0; manipula el núcleo

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### Rootkit de usuario

Opera en ring 3; más fácil de detectar

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### Rootkit LKM

Oculta procesos y ficheros desde ring 0

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### ROP

Encadenar gadgets existentes para construir comportamiento

**Aparece en 3 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md), [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md), [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### ROP + ret2libc

Combinación típica de técnicas modernas

**Aparece en 1 clase(s):** [Clase 138 — Desarrollo de exploits moderno](../classes/parte-5-explotacion-de-sistemas-y-binarios/138-desarrollo-de-exploits-moderno/README.md).

### ROP() de pwntools

Construye cadenas localizando gadgets automáticamente

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### ROP Emporium

Serie de retos progresivos para practicar return-oriented programming en binarios deliberadamente vulnerables.

**Sitio oficial:** [ROP Emporium](https://ropemporium.com/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### ROPgadget / ropper

Herramientas que buscan gadgets en el binario

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### Rotación

Sustitución controlada de una credencial y actualización de consumidores.

**Aparece en 3 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md), [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md), [Clase 241 — Secretos en el código y pre-commit hooks](../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md).

### Rotación de claves

Renovar periódicamente la clave del MAC

**Aparece en 1 clase(s):** [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

### Rotar credencial

Invalidar y reemitir una clave expuesta

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### Roto académicamente

Existe algún ataque mejor que la fuerza bruta

**Aparece en 1 clase(s):** [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### Roto prácticamente

El ataque es alcanzable con recursos reales

**Aparece en 1 clase(s):** [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### RPO

Punto temporal máximo de pérdida de datos aceptada.

**Aparece en 1 clase(s):** [Clase 283 — Continuidad de negocio y plan de recuperación ante desastres](../classes/parte-14-grc-riesgo-y-cumplimiento/283-continuidad-de-negocio-y-plan-de-recuperacion-ante-desastres/README.md).

### RS256

Firma asimétrica; privada firma, pública verifica

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### RSA

Cifrado/firma asimétrico basado en la factorización de enteros grandes

**Aparece en 1 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md).

### RSA-PSS

Relleno probabilístico moderno para firmar con RSA

**Aparece en 1 clase(s):** [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### RSP

Puntero a la cima de la pila

**Aparece en 2 clase(s):** [Clase 24 — Arquitectura de computadores: CPU, registros y memoria](../classes/parte-0-fundamentos-y-prerrequisitos/024-arquitectura-de-computadores-cpu-registros-y-memoria/README.md), [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### RSP / RBP

Cima de la pila / base del marco actual

**Aparece en 1 clase(s):** [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### RST

Cierre abrupto de conexión: puerto cerrado, firewall o aborto

**Aparece en 2 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md), [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### RST (0x14)

Respuesta que indica puerto cerrado

**Aparece en 1 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md).

### RTO

Tiempo objetivo para restaurar una capacidad.

**Aparece en 1 clase(s):** [Clase 283 — Continuidad de negocio y plan de recuperación ante desastres](../classes/parte-14-grc-riesgo-y-cumplimiento/283-continuidad-de-negocio-y-plan-de-recuperacion-ante-desastres/README.md).

### RTT

*Round-trip time*: latencia de ida y vuelta medida sobre el flujo

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### Rules of engagement

Reglas de autorización, tiempo, objetivos y parada.

**Aparece en 1 clase(s):** [Clase 303 — Capstone: laboratorio completo de pentest](../classes/parte-16-capstones-y-preparacion-de-certificaciones/303-capstone-laboratorio-completo-de-pentest/README.md).

### Rules of Engagement (RoE)

Contrato que fija alcance, técnicas permitidas, ventanas y contactos

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### Run key

Clave del Registro que ejecuta algo al iniciar sesión

**Aparece en 1 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md).

### Run keys

Claves del registro que ejecutan en el inicio de sesión

**Aparece en 1 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md).

### Run keys / servicios / tareas / WMI

Vectores de persistencia

**Aparece en 1 clase(s):** [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### Runner

Entorno que ejecuta los pasos del workflow.

**Aparece en 1 clase(s):** [Clase 242 — Seguridad en pipelines CI/CD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/242-seguridad-en-pipelines-ci-cd/README.md).

### Ruta absoluta

Invocar un comando con su ruta completa evita el secuestro

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### RVA

Desplazamiento relativo en memoria

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### rwx

Permisos de lectura, escritura y ejecución

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

## S

### S-box

Componente no lineal cuyo diseño resiste ambas técnicas

**Aparece en 2 clase(s):** [Clase 47 — Cifrado simétrico: AES y modos de operación](../classes/parte-2-criptografia-aplicada/047-cifrado-simetrico-aes-y-modos-de-operacion/README.md), [Clase 61 — Introducción al criptoanálisis](../classes/parte-2-criptografia-aplicada/061-introduccion-al-criptoanalisis/README.md).

### s (seek)

Mueve el cursor a una dirección

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### SAE

Autenticación basada en contraseña usada por WPA3-Personal.

**Aparece en 1 clase(s):** [Clase 272 — Ataques WiFi avanzados: Evil Twin y PMKID](../classes/parte-13-seguridad-movil-iot-e-inalambrica/272-ataques-wifi-avanzados-evil-twin-y-pmkid/README.md).

### Safe harbor

Protección declarada condicionada al cumplimiento de política.

**Aparece en 2 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md), [Clase 308 — Capstone: campaña de bug bounty](../classes/parte-16-capstones-y-preparacion-de-certificaciones/308-capstone-campana-de-bug-bounty/README.md).

### safe-linking

Ofusca los punteros next del tcache

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### SafeSEH

Valida que el manejador sea legítimo

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### Sal (salt)

Valor aleatorio por contraseña contra tablas precomputadas

**Aparece en 1 clase(s):** [Clase 21 — Criptografía: conceptos fundamentales e intuición](../classes/parte-0-fundamentos-y-prerrequisitos/021-criptografia-conceptos-fundamentales-e-intuicion/README.md).

### Salt

Valor aleatorio único por usuario, almacenado en claro

**Aparece en 2 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md), [Clase 80 — Cracking de contraseñas con John y Hashcat](../classes/parte-3-hacking-etico-y-pentesting-metodologia/080-cracking-de-contrasenas-con-john-y-hashcat/README.md).

### Salto corto (jmp short)

Redirige desde nSEH al shellcode

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### Salto indirecto

Destino calculado en ejecución; invisible en estático

**Aparece en 1 clase(s):** [Clase 133 — Análisis estático de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/133-analisis-estatico-de-binarios/README.md).

### Salvaguarda

Acción específica incluida en CIS Controls.

**Aparece en 1 clase(s):** [Clase 280 — Controles CIS](../classes/parte-14-grc-riesgo-y-cumplimiento/280-controles-cis/README.md).

### Same-Origin Policy (SOP)

Aísla el JS de un origen de los datos de otro

**Aparece en 1 clase(s):** [Clase 113 — Ataques del lado del cliente: CORS, postMessage y prototype pollution](../classes/parte-4-seguridad-de-aplicaciones-web/113-ataques-del-lado-del-cliente-cors-postmessage-y-prototype-pollution/README.md).

### SameSite

Atributo que limita el envío de cookies entre orígenes.

**Aparece en 3 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md), [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md), [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### SameSite=Lax

Valor por defecto moderno; no la envía en envíos de fondo

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### SameSite=Strict

No envía la cookie en ninguna petición cross-site

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### SAML

Autenticación basada en XML firmado; candidata a XXE

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### SAN del certificado

*Subject Alternative Names*; suele filtrar nombres internos

**Aparece en 1 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md).

### Sandbox

Restricción del proceso a su contenedor e interfaces permitidas.

**Aparece en 2 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md), [Clase 263 — Seguridad de iOS: arquitectura](../classes/parte-13-seguridad-movil-iot-e-inalambrica/263-seguridad-de-ios-arquitectura/README.md).

### Sandbox automático

Entorno que genera un informe de comportamiento

**Aparece en 1 clase(s):** [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### Sanitización

Recomprimir o escalar para destruir la carga oculta

**Aparece en 2 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md), [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### Sanitizador

Transformación válida para un contexto específico; no es universal.

**Aparece en 1 clase(s):** [Clase 238 — SAST: análisis estático de código](../classes/parte-11-devsecops-y-seguridad-del-sdlc/238-sast-analisis-estatico-de-codigo/README.md).

### Sanitizer (ASan/UBSan)

Convierte corrupciones silenciosas en crashes claros

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### SAST

Análisis estático de seguridad del código

**Aparece en 2 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md), [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Saturación

Sobrecarga que distorsiona y crea señales espurias.

**Aparece en 1 clase(s):** [Clase 269 — Radio definida por software (SDR)](../classes/parte-13-seguridad-movil-iot-e-inalambrica/269-radio-definida-por-software-sdr/README.md).

### Saved RBP

Copia del RBP anterior, adyacente a la dirección de retorno

**Aparece en 1 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md).

### SBOM

Inventario de componentes que acelera evaluación, sin demostrar seguridad.

**Aparece en 2 clase(s):** [Clase 246 — Supply chain security: SBOM y SLSA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md), [Clase 275 — Seguridad de dispositivos médicos](../classes/parte-13-seguridad-movil-iot-e-inalambrica/275-seguridad-de-dispositivos-medicos/README.md).

### SCA

Análisis de las dependencias contra CVE

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### Scapy

Librería Python de forja y análisis de paquetes

**Aparece en 1 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md).

### Schema

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 355 — Telemetría para Game Security](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/355-telemetria-game-security/README.md).

### SCM

Service Control Manager (gestor de servicios)

**Aparece en 1 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md).

### Scope

Activos autorizados; fuera de él es acceso no autorizado

**Aparece en 1 clase(s):** [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### Scope creep

Ampliar el alcance sobre la marcha; riesgo legal

**Aparece en 1 clase(s):** [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### Script Block Logging

Registro del contenido de los bloques ejecutados

**Aparece en 2 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md), [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

### Script de Zeek

Código que reacciona a eventos para generar logs o detección

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### Script kiddie

Atacante de baja capacidad que reutiliza herramientas ajenas

**Aparece en 1 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md).

### Scrubbing

Limpieza upstream antes de que el volumen alcance el enlace protegido

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### scrypt

Primera KDF *memory-hard* ampliamente usada

**Aparece en 1 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md).

### Scylla / ImpREC

Herramientas de reconstrucción de la IAT

**Aparece en 1 clase(s):** [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Sección

Parte del binario con un propósito (.text, .rodata…)

**Aparece en 2 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md), [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### SecLists

Colección de referencia de rutas, parámetros y payloads

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### Secreto

Material que permite autenticar, firmar, descifrar o autorizar.

**Aparece en 1 clase(s):** [Clase 241 — Secretos en el código y pre-commit hooks](../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md).

### Secreto compartido

`gᵃᵇ mod p`, al que llegan ambas partes

**Aparece en 1 clase(s):** [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### Secreto dinámico

Credencial creada al vuelo, con TTL corto y revocación

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### Secreto en el código

Credencial en el repositorio; anti-patrón que persiste en el historial

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### Secreto HMAC débil

Crackeable offline; permite forjar tokens

**Aparece en 1 clase(s):** [Clase 103 — Ataques y seguridad de JWT](../classes/parte-4-seguridad-de-aplicaciones-web/103-ataques-y-seguridad-de-jwt/README.md).

### secrets / os.urandom

APIs seguras en Python

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### Sector/block

Organización de memoria presente en algunas familias de tarjetas.

**Aparece en 1 clase(s):** [Clase 270 — Ataques a RFID y NFC](../classes/parte-13-seguridad-movil-iot-e-inalambrica/270-ataques-a-rfid-y-nfc/README.md).

### Secuestro de petición

Robar la petición o respuesta de otro usuario

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Secuestro de vtable

Vtable falsa que redirige una llamada a método

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### Secure

Flag que restringe la cookie a HTTPS

**Aparece en 1 clase(s):** [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### Secure Boot

El firmware solo arranca código firmado

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### Secure coding

Construir software seguro por diseño, no por parche

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### Security champion

Miembro del equipo que facilita prácticas y conexión con especialistas.

**Aparece en 1 clase(s):** [Clase 248 — Cultura DevSecOps y security champions](../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md).

### Security Onion

Distribución que integra Suricata, Zeek y análisis para NSM

**Aparece en 1 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md).

### Segmentación

Separar una red en subredes para limitar el alcance de un ataque.

**Aparece en 3 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md), [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md), [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### Segmento

PDU de transporte con TCP (datagrama con UDP)

**Aparece en 1 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md).

### Segunda preimagen

Encontrar otra entrada con el mismo digest que una dada

**Aparece en 1 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md).

### Segundo orden

El payload se guarda y se ejecuta después, en otro sitio

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### Seguridad de la cadena

El riesgo nace de cómo encajan los componentes

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Seguridad por oscuridad

Confiar en el secreto del diseño; anti-patrón

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### Seguridad psicológica

Posibilidad de informar problemas temprano sin represalia improductiva.

**Aparece en 2 clase(s):** [Clase 248 — Cultura DevSecOps y security champions](../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md), [Clase 286 — Concienciación y cultura de seguridad](../classes/parte-14-grc-riesgo-y-cumplimiento/286-concienciacion-y-cultura-de-seguridad/README.md).

### SEH

Structured Exception Handling de Windows

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### SEH overwrite

Sobrescribir nSEH y Handler con un overflow

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### SEHOP

Comprueba la integridad de la cadena SEH

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

### SeImpersonatePrivilege

Privilegio que permite suplantar otro token

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### Select-Object

Selecciona propiedades o un número de objetos

**Aparece en 1 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md).

### Sellado / desellado

Arranque de Vault con claves repartidas entre personas

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### Semilla

Entidad inicial autorizada desde la que comienza la expansión.

**Aparece en 1 clase(s):** [Clase 255 — Automatización de OSINT: SpiderFoot y Maltego](../classes/parte-12-osint-e-ingenieria-social/255-automatizacion-de-osint-spiderfoot-y-maltego/README.md).

### Semilla (seed)

Valor inicial del generador; si es adivinable, todo lo es

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### send

Envía paquetes de capa 3 sin esperar respuesta

**Aparece en 1 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md).

### sendline / recvline

Enviar y recibir datos del proceso

**Aparece en 1 clase(s):** [Clase 120 — Buffer overflow en stack: explotación práctica](../classes/parte-5-explotacion-de-sistemas-y-binarios/120-buffer-overflow-en-stack-explotacion-practica/README.md).

### Sensibilidad

Cambio del resultado al variar un supuesto.

**Aparece en 1 clase(s):** [Clase 277 — Gestión de riesgos: cuantitativa y cualitativa](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md).

### Separar código y datos

Parametrizar, no invocar shell, no deserializar input

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### Serialización

Convertir un objeto en bytes para guardar o transmitir

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### Servicio

Proceso privilegiado que arranca con el sistema

**Aparece en 1 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md).

### Servicio de metadatos

`169.254.169.254`; devuelve credenciales de la instancia

**Aparece en 2 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md), [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### Servicio frágil

Dispositivo que un escaneo agresivo puede tumbar

**Aparece en 1 clase(s):** [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### Servidor autoritativo

El que tiene la verdad de una zona DNS

**Aparece en 1 clase(s):** [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md).

### Sesgo estadístico

Desviación de la uniformidad que acaba siendo explotable

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### Sesión

Asociación de peticiones al mismo usuario autenticado.

**Aparece en 5 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md), [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md), [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md), [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md), [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### Sesión nula

Conexión SMB sin credenciales que puede filtrar usuarios y shares

**Aparece en 2 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md), [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md).

### Session fixation

Imponer a la víctima un ID conocido por el atacante

**Aparece en 1 clase(s):** [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### Session hijacking

Robar el ID para suplantar la sesión

**Aparece en 1 clase(s):** [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### Session ID

Identificador que equivale a la contraseña durante la sesión

**Aparece en 1 clase(s):** [Clase 102 — Gestión de sesiones y ataques asociados](../classes/parte-4-seguridad-de-aplicaciones-web/102-gestion-de-sesiones-y-ataques-asociados/README.md).

### Session revocation

Invalidación de sesiones y tokens ya emitidos.

**Aparece en 1 clase(s):** [Clase 259 — Defensa contra la ingeniería social](../classes/parte-12-osint-e-ingenieria-social/259-defensa-contra-la-ingenieria-social/README.md).

### set

Colección de elementos únicos sin orden.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### set -e

Aborta el script si un comando falla

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### Set / mapa

Estructura de nftables que agrupa puertos o redes en una sola regla

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### set -u

Aborta si se usa una variable no definida

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### set vs setg

Variable local del módulo vs global de la sesión

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### setcap

Concede capacidades concretas a un binario sin darle root entero

**Aparece en 1 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### Seudonimato

Uso de identidad alternativa que puede mantener continuidad.

**Aparece en 1 clase(s):** [Clase 260 — OPSEC personal y anonimato](../classes/parte-12-osint-e-ingenieria-social/260-opsec-personal-y-anonimato/README.md).

### Seudonimización

Separar identificadores sin eliminar toda posibilidad de enlace.

**Aparece en 1 clase(s):** [Clase 289 — Privacidad y protección de datos](../classes/parte-14-grc-riesgo-y-cumplimiento/289-privacidad-y-proteccion-de-datos/README.md).

### sFlow

Muestreo de paquetes (uno de cada N); más ligero, menos preciso

**Aparece en 1 clase(s):** [Clase 45 — NetFlow y análisis de metadatos de tráfico](../classes/parte-1-redes-y-seguridad-de-redes/045-netflow-y-analisis-de-metadatos-de-trafico/README.md).

### SGID

Bit análogo para el grupo; en directorios, hereda el grupo

**Aparece en 2 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md), [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### SGSI

Sistema de gestión para dirigir y mejorar seguridad de información.

**Aparece en 1 clase(s):** [Clase 278 — ISO/IEC 27001 e implantación de un SGSI](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md).

### SGSI / ISMS

Sistema de Gestión de Seguridad de la Información

**Aparece en 1 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md).

### SHA-2

Familia estándar (SHA-256, SHA-512); Merkle-Damgård

**Aparece en 1 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md).

### SHA-3 / Keccak

Construcción de esponja; inmune a extensión de longitud

**Aparece en 1 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md).

### Shadow copies

Copias de Windows que el ransomware borra

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### SHAttered

Colisión real de SHA-1 demostrada por Google en 2017

**Aparece en 1 clase(s):** [Clase 51 — Funciones hash: SHA-2, SHA-3 y sus propiedades](../classes/parte-2-criptografia-aplicada/051-funciones-hash-sha-2-sha-3-y-sus-propiedades/README.md).

### Shebang

Línea `#!` inicial que fija el intérprete del script

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### Shell del sistema

Intérprete al que llega la entrada sin controlar

**Aparece en 1 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### shell=False

Ejecutar con argumentos como lista, sin invocar la shell

**Aparece en 1 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### ShellCheck

Linter estático para scripts de shell

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### Shellcode

Código máquina que se inyecta y ejecuta, típico para lanzar shell

**Aparece en 1 clase(s):** [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### shellcraft

Generador de shellcode de pwntools

**Aparece en 1 clase(s):** [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### Shift-left

Retroalimentar seguridad antes, sin prometer eliminar los fallos de producción.

**Aparece en 1 clase(s):** [Clase 236 — Secure SDLC y filosofía shift-left](../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md).

### Shift-right

Validar hipótesis mediante observación y respuesta durante la operación.

**Aparece en 1 clase(s):** [Clase 236 — Secure SDLC y filosofía shift-left](../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md).

### shikataganai

Encoder popular; su patrón está en las firmas de AV

**Aparece en 1 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### Shodan / Censys

Buscadores de servicios expuestos en Internet

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### Short-haul C2

Canal rápido para trabajo interactivo

**Aparece en 1 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### SID

Identificador único de seguridad de un principal

**Aparece en 1 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md).

### sid / rev

Identificador y versión de la regla; el rango local empieza en 1000000

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### SIEM — Security Information and Event Management

Sistema central de eventos, fuera del alcance del atacante

**Claves de búsqueda normalizadas:** `siem`.

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### SIGKILL

Señal 9: terminación forzada e inmediata

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### Signed / unsigned

Interpretación del mismo patrón de bits

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Sigstore

Infraestructura moderna de firma de artefactos de software

**Aparece en 1 clase(s):** [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### SIGTERM

Señal 15: petición ordenada de terminación

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### SIKE

Candidato de isogenias roto en 2022 con un portátil

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### Simulación

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 2 clase(s):** [Clase 256 — Fundamentos de ingeniería social](../classes/parte-12-osint-e-ingenieria-social/256-fundamentos-de-ingenieria-social/README.md), [Clase 354 — Server-side Anti-Cheat y diseño autoritativo](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/354-server-side-anticheat-diseno-autoritativo/README.md).

### Sink

Función que interpreta el dato como código o HTML

**Aparece en 1 clase(s):** [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### Sink peligroso

Punto donde un dato contaminado causa daño

**Aparece en 1 clase(s):** [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Sinkholing

Redirigir los dominios DGA a un servidor controlado

**Aparece en 1 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md).

### Sintaxis AT&T

`mov $5, %rax`; origen primero, con `%` y `$`

**Aparece en 1 clase(s):** [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### Sintaxis Intel

`mov rax, 5`; destino primero

**Aparece en 1 clase(s):** [Clase 116 — Arquitectura x86/x64 y lenguaje ensamblador](../classes/parte-5-explotacion-de-sistemas-y-binarios/116-arquitectura-x86-x64-y-lenguaje-ensamblador/README.md).

### SIS

Sistema independiente destinado a llevar el proceso a estado seguro.

**Aparece en 1 clase(s):** [Clase 273 — Seguridad de sistemas de control industrial (ICS/SCADA)](../classes/parte-13-seguridad-movil-iot-e-inalambrica/273-seguridad-de-sistemas-de-control-industrial-ics-scada/README.md).

### Site-to-site

Túnel entre dos redes completas, gateway a gateway

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### Sitemap

Árbol del contenido descubierto del objetivo

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### sitemap.xml

Enumera páginas de la aplicación

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### size / flags

Tamaño del chunk y bits de estado en la cabecera

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### SLA

Compromiso temporal condicionado por riesgo y proceso definido.

**Aparece en 1 clase(s):** [Clase 245 — Gestión de vulnerabilidades a escala](../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md).

### Slack space

Espacio sobrante de un bloque de disco

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### SLEEP / pgsleep / WAITFOR

Funciones de retardo por motor

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### SLH-DSA (FIPS 205)

Firma basada solo en hashes; opción conservadora

**Aparece en 1 clase(s):** [Clase 62 — Criptografía post-cuántica](../classes/parte-2-criptografia-aplicada/062-criptografia-post-cuantica/README.md).

### Sliver

C2 open source en Go, multiplataforma, mTLS

**Aparece en 1 clase(s):** [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### Sliver / Metasploit

Otros frameworks de C2

**Aparece en 1 clase(s):** [Clase 149 — Comunicaciones de comando y control (C2) del malware](../classes/parte-6-analisis-de-malware/149-comunicaciones-de-comando-y-control-c2-del-malware/README.md).

### SLSA track

Conjunto de garantías y niveles para un aspecto de la cadena.

**Aparece en 1 clase(s):** [Clase 246 — Supply chain security: SBOM y SLSA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md).

### Smali

Ensamblador legible de Dalvik

**Aparece en 1 clase(s):** [Clase 155 — Malware en Android](../classes/parte-6-analisis-de-malware/155-malware-en-android/README.md).

### SMAP

Impide al kernel acceder a memoria de usuario

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### SMB (139/445)

Protocolo de compartición de Windows; muy rico en datos

**Aparece en 1 clase(s):** [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md).

### SMBv1

Dialecto obsoleto e inseguro; su presencia ya es un hallazgo

**Aparece en 2 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md), [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md).

### SMEP

Impide al kernel ejecutar memoria de usuario

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### Snap,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 349 — Aimbot avanzado, predicción, smoothing y recoil](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/349-aimbot-avanzado-prediccion-smoothing-recoil/README.md).

### Snap length (-s)

Bytes que se guardan de cada paquete

**Aparece en 1 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### Snapshot

Imagen de interfaz que puede persistir al pasar a segundo plano.

**Aparece en 4 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md), [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md), [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md), [Clase 264 — Pentest de aplicaciones iOS](../classes/parte-13-seguridad-movil-iot-e-inalambrica/264-pentest-de-aplicaciones-ios/README.md).

### Snapshot de VM

Restaurar estado del generador y repetir valores

**Aparece en 1 clase(s):** [Clase 58 — Generación de aleatoriedad segura (CSPRNG)](../classes/parte-2-criptografia-aplicada/058-generacion-de-aleatoriedad-segura-csprng/README.md).

### Snapshots,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 352 — Seguridad del protocolo de juego](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/352-seguridad-protocolo-juego/README.md).

### SNAT

Reescribe la dirección de origen (salida de una red privada)

**Aparece en 1 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md).

### SNI

Server Name Indication; el host del handshake TLS

**Aparece en 1 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### Sniffing

Captura pasiva de tráfico de una interfaz

**Aparece en 1 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md).

### Sniper / Cluster bomb

Modos de Intruder según posiciones y combinaciones

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### SNMP (161/udp)

Gestión de dispositivos; filtra inventario y configuración

**Aparece en 1 clase(s):** [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md).

### SoA

Statement of Applicability: justificación de controles ISO aplicados

**Aparece en 2 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md), [Clase 278 — ISO/IEC 27001 e implantación de un SGSI](../classes/parte-14-grc-riesgo-y-cumplimiento/278-iso-iec-27001-e-implantacion-de-un-sgsi/README.md).

### Sobrescritura de la GOT

Objetivo clásico: redirigir una función de libc

**Aparece en 1 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### SOC — Security Operations Center

Función organizativa que monitorea, investiga y coordina la respuesta ante señales de seguridad.

**Claves de búsqueda normalizadas:** `soc`.

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### SOCKDGRAM

Tipo de socket de datagramas sin conexión (UDP)

**Aparece en 1 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### Socket

Extremo de comunicación (IP + puerto) gestionado por el kernel

**Aparece en 1 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### SOCKS

Protocolo de proxy genérico; transporta TCP con conexión completa

**Aparece en 2 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md), [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### socksproxy

Módulo de Metasploit que levanta un SOCKS local

**Aparece en 1 clase(s):** [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### SOCKSTREAM

Tipo de socket orientado a flujo fiable (TCP)

**Aparece en 1 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### Software (Sxxxx)

Malware o herramienta con las técnicas que implementa

**Aparece en 1 clase(s):** [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### Solapamiento

Dos malloc devuelven el mismo puntero

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### Sonda 77

Deteccion; si la expresion se evalua, hay SSTI

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### Sonda con comilla

`'` para provocar un error o cambio y detectar SQLi

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### Source

Dato controlable por el atacante (`location.hash`, referrer)

**Aparece en 1 clase(s):** [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### SOW

*Statement of Work*: servicio, plazos, precio y entregables

**Aparece en 1 clase(s):** [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### SPA

Aplicación de una página; JS en el cliente habla con una API

**Aparece en 1 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### SPAN / mirror port

Puerto del switch que copia el tráfico de otros puertos

**Aparece en 1 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md).

### Speakeasy / dumpulator

Emuladores especializados en malware de Windows

**Aparece en 1 clase(s):** [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Spear phishing

Phishing dirigido y personalizado contra personas u organizaciones concretas

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### SPF

Registro DNS que declara qué servidores pueden enviar correo en nombre del dominio

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### SPI

Bus síncrono usado por memorias y periféricos.

**Aparece en 1 clase(s):** [Clase 268 — Análisis de hardware: UART, JTAG y SPI](../classes/parte-13-seguridad-movil-iot-e-inalambrica/268-analisis-de-hardware-uart-jtag-y-spi/README.md).

### Spider tradicional

Descubre páginas siguiendo enlaces del HTML

**Aparece en 1 clase(s):** [Clase 89 — OWASP ZAP](../classes/parte-4-seguridad-de-aplicaciones-web/089-owasp-zap/README.md).

### Spidering

Descubrimiento siguiendo enlaces visibles

**Aparece en 1 clase(s):** [Clase 90 — Mapeo, spidering y descubrimiento de contenido](../classes/parte-4-seguridad-de-aplicaciones-web/090-mapeo-spidering-y-descubrimiento-de-contenido/README.md).

### Split,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 358 — Machine Learning aplicado a Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/358-machine-learning-aplicado-anticheat/README.md).

### Split tunneling

Enrutar solo parte del tráfico por el túnel

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### Spraying en AD

Contra Kerberos, SMB u OWA

**Aparece en 1 clase(s):** [Clase 81 — Ataques a credenciales: fuerza bruta y password spraying](../classes/parte-3-hacking-etico-y-pentesting-metodologia/081-ataques-a-credenciales-fuerza-bruta-y-password-spraying/README.md).

### SQLMap

Herramienta que automatiza detección y explotación de SQLi

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### sr1

Envía capa 3 y devuelve la primera respuesta

**Aparece en 1 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md).

### srp

Envía/recibe en capa 2 (Ethernet), necesario para ARP

**Aparece en 1 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md).

### SSDT hooking

Interceptar las llamadas al sistema en su raíz

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### SSH -D (dinámico)

Convierte el cliente SSH en un proxy SOCKS genérico

**Aparece en 1 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md).

### SSH -L (local)

Túnel hacia un servicio interno concreto

**Aparece en 1 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md).

### SSH -R (remoto)

Túnel de vuelta desde el servidor hacia el atacante

**Aparece en 1 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md).

### SSID

Nombre de la red inalámbrica

**Aparece en 1 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md).

### SSL stripping

Degradar HTTPS a HTTP aprovechando la primera petición en claro

**Aparece en 1 clase(s):** [Clase 40 — Man-in-the-Middle: técnicas y defensa](../classes/parte-1-redes-y-seguridad-de-redes/040-man-in-the-middle-tecnicas-y-defensa/README.md).

### SSR

Renderizado en servidor; cada acción pide una página nueva

**Aparece en 1 clase(s):** [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### SSRF

La aplicación hace una petición a una URL que controla el atacante

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### SSRF ciega

La app no devuelve el resultado; se confirma por OOB

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### SSTI

Inyeccion en la plantilla, evaluada en el servidor

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### SSTI vs XSS

SSTI ejecuta en el servidor; XSS en el navegador

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### Stack

Pila LIFO de marcos de llamada

**Aparece en 1 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md).

### Stack canary

Valor secreto que detecta la sobrescritura de la pila

**Aparece en 2 clase(s):** [Clase 119 — Buffer overflow en stack: teoría](../classes/parte-5-explotacion-de-sistemas-y-binarios/119-buffer-overflow-en-stack-teoria/README.md), [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md).

### Stack frame

Marco de pila de una función

**Aparece en 1 clase(s):** [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

### Stack pivot

Cambiar RSP a una región mayor para cadenas largas

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

### Stack smashing detected

Mensaje al fallar la comprobación del canario

**Aparece en 1 clase(s):** [Clase 122 — Protecciones modernas: ASLR, DEP/NX, stack canaries y PIE](../classes/parte-5-explotacion-de-sistemas-y-binarios/122-protecciones-modernas-aslr-dep-nx-stack-canaries-y-pie/README.md).

### Staged vs stageless

El nombre (`/` vs `_`) fija qué handler configurar

**Aparece en 1 clase(s):** [Clase 75 — msfvenom: generación de payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/075-msfvenom-generacion-de-payloads/README.md).

### Stageless

Payload que lleva el implante completo de una vez

**Aparece en 1 clase(s):** [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### Stager

Payload pequeño que descarga y lanza el implante completo

**Aparece en 3 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md), [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md), [Clase 165 — Frameworks C2: Cobalt Strike, Sliver y Mythic](../classes/parte-7-red-team-y-operaciones-ofensivas/165-frameworks-c2-cobalt-strike-sliver-y-mythic/README.md).

### Staging

Infraestructura dedicada a la entrega inicial del payload

**Aparece en 2 clase(s):** [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md), [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### Staging (índice)

Zona intermedia de cambios preparados

**Aparece en 1 clase(s):** [Clase 18 — Git y control de versiones para profesionales de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md).

### state

Valor que ata petición y respuesta; anti-CSRF

**Aparece en 1 clase(s):** [Clase 104 — Seguridad de OAuth 2.0 y OpenID Connect](../classes/parte-4-seguridad-de-aplicaciones-web/104-seguridad-de-oauth-2-0-y-openid-connect/README.md).

### stderr (fd 2)

Canal de mensajes de error y diagnóstico

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### stdin (fd 0)

Canal de entrada estándar de un proceso

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### stdlib

Librería estándar incluida con Python.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### stdout (fd 1)

Canal de salida normal de un proceso

**Aparece en 1 clase(s):** [Clase 6 — Línea de comandos Linux avanzada: grep, sed, awk, pipes y procesos](../classes/parte-0-fundamentos-y-prerrequisitos/006-linea-de-comandos-linux-avanzada-grep-sed-awk-pipes-y-procesos/README.md).

### stepi / nexti

Ejecutar una instrucción entrando / pasando por encima

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### Sticky bit

Restringe el borrado en un directorio a cada propietario

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

### STIX

Formato estándar para describir amenazas

**Aparece en 2 clase(s):** [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md), [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### STIX/TAXII

Formato y protocolo para intercambiar conocimiento de amenazas

**Aparece en 1 clase(s):** [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### STP

*Spanning Tree Protocol*; evita bucles y es manipulable

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### str

Secuencia de caracteres Unicode (texto).

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### strace

Registra las llamadas al sistema del programa

**Aparece en 2 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md), [Clase 134 — Análisis dinámico y debugging de binarios](../classes/parte-5-explotacion-de-sistemas-y-binarios/134-analisis-dinamico-y-debugging-de-binarios/README.md).

### strace / ltrace

Observan syscalls y funciones de librería

**Aparece en 1 clase(s):** [Clase 154 — Malware en Linux](../classes/parte-6-analisis-de-malware/154-malware-en-linux/README.md).

### Stream index

Identificador que Wireshark asigna a cada conversación TCP

**Aparece en 1 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md).

### strings

Cadenas legibles (ASCII y Unicode); revelan intenciones

**Aparece en 3 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md), [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md), [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Stripped

Binario sin símbolos; solo direcciones

**Aparece en 1 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md).

### Stub

Desempaquetador que revela el código en ejecución

**Aparece en 1 clase(s):** [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Stub / desempaquetador

Código que descomprime el binario real al ejecutarse

**Aparece en 1 clase(s):** [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md).

### Stub DOS

Mensaje "cannot be run in DOS mode"

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### subclasses

Via tipica de escalada en Jinja2/Python

**Aparece en 1 clase(s):** [Clase 107 — Server-Side Template Injection (SSTI)](../classes/parte-4-seguridad-de-aplicaciones-web/107-server-side-template-injection-ssti/README.md).

### Subir vs buscar por hash

Subir hace pública la muestra; buscar por hash no

**Aparece en 1 clase(s):** [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md).

### Subject / SAN

Identidad del titular; los SAN son los nombres que se validan

**Aparece en 1 clase(s):** [Clase 55 — PKI, certificados X.509 y autoridades de certificación](../classes/parte-2-criptografia-aplicada/055-pki-certificados-x-509-y-autoridades-de-certificacion/README.md).

### Sublímite

Límite específico dentro de la cobertura.

**Aparece en 1 clase(s):** [Clase 288 — Seguros cibernéticos](../classes/parte-14-grc-riesgo-y-cumplimiento/288-seguros-ciberneticos/README.md).

### Subnetting

División de una red en subredes iguales.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### Subred

Porción de una red mayor delimitada por una máscara.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### SUBSTRING / SUBSTR

Aísla un carácter del dato buscado

**Aparece en 1 clase(s):** [Clase 92 — Inyección SQL avanzada y ciega (blind)](../classes/parte-4-seguridad-de-aplicaciones-web/092-inyeccion-sql-avanzada-y-ciega-blind/README.md).

### Subtécnica

Variante específica de una técnica (`Txxxx.00x`)

**Aparece en 1 clase(s):** [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### sudo -l

Lista lo que el usuario puede ejecutar con privilegios

**Aparece en 1 clase(s):** [Clase 76 — Escalada de privilegios en Linux](../classes/parte-3-hacking-etico-y-pentesting-metodologia/076-escalada-de-privilegios-en-linux/README.md).

### SUID

Bit que ejecuta un binario con privilegios del propietario

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

### Sumidero

Operación sensible que puede convertir esos datos en impacto.

**Aparece en 1 clase(s):** [Clase 238 — SAST: análisis estático de código](../classes/parte-11-devsecops-y-seguridad-del-sdlc/238-sast-analisis-estatico-de-codigo/README.md).

### Superficie de ataque

Conjunto de todos los puntos de entrada posibles a un sistema

**Aparece en 3 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md), [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md), [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Superficie de kernel

syscalls, ioctl y drivers

**Aparece en 1 clase(s):** [Clase 139 — Kernel exploitation: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/139-kernel-exploitation-introduccion/README.md).

### Superficie humana

Empleados como vector de ingeniería social

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### Suposición del desarrollador

Premisa no verificada que el atacante viola

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### Supuesto

Condición declarada de la que depende una conclusión.

**Aparece en 20 clase(s):** [Clase 311 — Clasificación y ciclo de vida de los datos](../classes/parte-17-profundizacion-para-certificaciones/311-clasificacion-y-ciclo-de-vida-de-los-datos/README.md), [Clase 312 — Retención, destrucción segura de datos y DLP](../classes/parte-17-profundizacion-para-certificaciones/312-retencion-destruccion-segura-de-datos-y-dlp/README.md), [Clase 313 — Gestión del ciclo de vida de identidades (IAM empresarial)](../classes/parte-17-profundizacion-para-certificaciones/313-gestion-del-ciclo-de-vida-de-identidades-iam-empresarial/README.md), [Clase 314 — Federación, SSO, SAML y OpenID Connect](../classes/parte-17-profundizacion-para-certificaciones/314-federacion-sso-saml-y-openid-connect/README.md), [Clase 315 — MFA y gestión de accesos privilegiados (PAM)](../classes/parte-17-profundizacion-para-certificaciones/315-mfa-y-gestion-de-accesos-privilegiados-pam/README.md), [Clase 316 — Modelos de seguridad y arquitectura (Bell-LaPadula, Biba, Clark-Wilson)](../classes/parte-17-profundizacion-para-certificaciones/316-modelos-de-seguridad-y-arquitectura/README.md), [Clase 317 — Seguridad física y ambiental](../classes/parte-17-profundizacion-para-certificaciones/317-seguridad-fisica-y-ambiental/README.md), [Clase 318 — Gestión del programa de vulnerabilidades](../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md), [Clase 319 — Análisis avanzado de phishing y correo malicioso](../classes/parte-17-profundizacion-para-certificaciones/319-analisis-avanzado-de-phishing-y-correo-malicioso/README.md), [Clase 320 — Gobierno, aspectos legales/regulatorios y gestión del programa](../classes/parte-17-profundizacion-para-certificaciones/320-gobierno-aspectos-legales-regulatorios-y-gestion-del-programa/README.md) y 10 más.

### Sustitución

Reemplazar cada símbolo por otro

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### Sustitución de contexto

Reutilizar un cifrado válido en otro lugar; el AAD lo impide

**Aparece en 1 clase(s):** [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### SVG malicioso

XML con JavaScript; provoca XSS al visualizarse

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### Swagger / OpenAPI

Documentación que revela los endpoints

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### Switch spoofing

Negociar un trunk haciéndose pasar por switch para ver todas las VLAN

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### Symbol tree / bookmarks

Organización del trabajo en binarios grandes

**Aparece en 1 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md).

### SYN

Flag que solicita abrir una conexión TCP.

**Aparece en 1 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md).

### SYN-ACK (0x12)

Respuesta que indica puerto abierto

**Aparece en 1 clase(s):** [Clase 17 — Python para seguridad: manipulación de paquetes con Scapy](../classes/parte-0-fundamentos-y-prerrequisitos/017-python-para-seguridad-manipulacion-de-paquetes-con-scapy/README.md).

### SYN flood

Agotamiento de recursos de conexión en transporte

**Aparece en 1 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md).

### SYN scan (-sS)

Escaneo semiabierto; requiere *raw sockets* y privilegios

**Aparece en 2 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md), [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### Synchronizer token

Nombre técnico del token anti-CSRF

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### Syscall

Llamada al sistema; la vía directa al kernel

**Aparece en 2 clase(s):** [Clase 23 — Sistemas operativos: procesos, memoria y syscalls](../classes/parte-0-fundamentos-y-prerrequisitos/023-sistemas-operativos-procesos-memoria-y-syscalls/README.md), [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### Sysmon

Registra procesos, líneas de comando, red, registro

**Aparece en 1 clase(s):** [Clase 159 — Fileless malware y living-off-the-land](../classes/parte-6-analisis-de-malware/159-fileless-malware-y-living-off-the-land/README.md).

### SYSTEM

Cuenta local de máximo privilegio (`S-1-5-18`)

**Aparece en 4 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md), [Clase 74 — Meterpreter y post-explotación](../classes/parte-3-hacking-etico-y-pentesting-metodologia/074-meterpreter-y-post-explotacion/README.md), [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md), [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### system("/bin/sh")

Objetivo típico: función de libc que lanza una shell

**Aparece en 1 clase(s):** [Clase 123 — Bypass de protecciones: ret2libc](../classes/parte-5-explotacion-de-sistemas-y-binarios/123-bypass-de-protecciones-ret2libc/README.md).

### system() / exec()

Funciones que pasan una cadena a la shell; la causa raíz

**Aparece en 1 clase(s):** [Clase 95 — Inyección de comandos del sistema operativo](../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md).

### System V AMD64

ABI de Linux x64

**Aparece en 1 clase(s):** [Clase 117 — El stack, los registros y las convenciones de llamada](../classes/parte-5-explotacion-de-sistemas-y-binarios/117-el-stack-los-registros-y-las-convenciones-de-llamada/README.md).

## T

### T1041 vs T1048

Exfiltrar sobre el C2 o por un canal alternativo

**Aparece en 1 clase(s):** [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md).

### Tabla CAM

Tabla del switch que asocia cada MAC a un puerto

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### Tabla de imports (IAT)

APIs que usa el binario; mapea a capacidades

**Aparece en 1 clase(s):** [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md).

### Tabla de símbolos

Asocia direcciones con nombres de funciones

**Aparece en 1 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md).

### Tabla de traducción

Registro que asocia cada conexión interna con su puerto reescrito

**Aparece en 1 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md).

### Tabla inet

Tabla de nftables que cubre IPv4 e IPv6 con un solo conjunto de reglas

**Aparece en 1 clase(s):** [Clase 34 — Firewalls: tipos, iptables y nftables](../classes/parte-1-redes-y-seguridad-de-redes/034-firewalls-tipos-iptables-y-nftables/README.md).

### Táctica

Objetivo del adversario; el "por qué" (14 en Enterprise)

**Aparece en 2 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md), [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### Tag

Etiqueta de versión de una imagen

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### Tag de autenticación

Etiqueta que detecta cualquier manipulación

**Aparece en 1 clase(s):** [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### Taint analysis

Seguimiento de datos desde fuentes hasta sumideros.

**Aparece en 1 clase(s):** [Clase 238 — SAST: análisis estático de código](../classes/parte-11-devsecops-y-seguridad-del-sdlc/238-sast-analisis-estatico-de-codigo/README.md).

### Taint tracking

Rastrear la propagación de un dato contaminado

**Aparece en 1 clase(s):** [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Tamaño de clave

2048 bits mínimo actual; 3072–4096 recomendable

**Aparece en 1 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md).

### Tamaño fijo

Los enteros no representan cualquier valor

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Tamper script (--tamper)

Transforma payloads para evadir un WAF

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### Tampering

Alteración no autorizada de datos (rompe integridad)

**Aparece en 1 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md).

### TAP

Dispositivo pasivo que duplica el tráfico de un enlace sin participar en él

**Aparece en 1 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md).

### Tarea programada

Ejecución con privilegios al arranque en Windows

**Aparece en 1 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md).

### Target

Variante del exploit según sistema, versión y arquitectura

**Aparece en 1 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md).

### Target scope

Dominios autorizados; limita las herramientas automáticas

**Aparece en 1 clase(s):** [Clase 88 — Burp Suite: configuración y flujo de trabajo](../classes/parte-4-seguridad-de-aplicaciones-web/088-burp-suite-configuracion-y-flujo-de-trabajo/README.md).

### Tasa de clic

Porcentaje de objetivos que abrieron el enlace; métrica central de la campaña

**Aparece en 1 clase(s):** [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### Tasa de muestreo

Número de muestras por segundo y límite práctico de banda observada.

**Aparece en 1 clase(s):** [Clase 269 — Radio definida por software (SDR)](../classes/parte-13-seguridad-movil-iot-e-inalambrica/269-radio-definida-por-software-sdr/README.md).

### TAXII

Protocolo para transportar CTI (STIX)

**Aparece en 1 clase(s):** [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md).

### Taxonomía

Lenguaje común de riesgos, no veredicto.

**Aparece en 1 clase(s):** [Clase 295 — OWASP Top 10 para aplicaciones con LLM](../classes/parte-15-seguridad-de-ia-y-machine-learning/295-owasp-top-10-para-aplicaciones-con-llm/README.md).

### tcache

Caché por hilo, LIFO por tamaño (glibc ≥ 2.26)

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### tcache key

Valor que detecta el double free obvio

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### tcache poisoning

Sobrescribir el `next` del tcache para malloc arbitrario

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### TCP,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 2 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md), [Clase 352 — Seguridad del protocolo de juego](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/352-seguridad-protocolo-juego/README.md).

### TCP/IP

Modelo práctico de 4 capas que implementa Internet

**Aparece en 1 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md).

### tcp.stream

Índice que identifica cada conversación TCP de la captura

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### TCP ZeroWindow

El receptor anuncia buffer lleno; cuello de botella en la aplicación

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### tcpdump

Capturador de paquetes en línea de comandos, basado en libpcap

**Aparece en 1 clase(s):** [Clase 28 — tcpdump y captura de tráfico en línea de comandos](../classes/parte-1-redes-y-seguridad-de-redes/028-tcpdump-y-captura-de-trafico-en-linea-de-comandos/README.md).

### Team ID

Identidad del equipo firmante usada en controles de plataforma.

**Aparece en 1 clase(s):** [Clase 263 — Seguridad de iOS: arquitectura](../classes/parte-13-seguridad-movil-iot-e-inalambrica/263-seguridad-de-ios-arquitectura/README.md).

### Team server

Servidor central que gestiona implantes y operadores; nunca se expone

**Aparece en 1 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### Técnica

Manera concreta de lograr una táctica (el cómo), con ID `Txxxx`

**Aparece en 2 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md), [Clase 162 — MITRE ATT&CK como lenguaje ofensivo](../classes/parte-7-red-team-y-operaciones-ofensivas/162-mitre-att-ck-como-lenguaje-ofensivo/README.md).

### Técnica prohibida

DoS, ingeniería social, escaneo agresivo (habitual)

**Aparece en 1 clase(s):** [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md).

### Telemetría

Rastro que el recon activo deja para un SOC

**Aparece en 1 clase(s):** [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### Telemetría resistente

Registro que la manipulación local no puede alterar

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### telescope

Vuelca la pila siguiendo punteros recursivamente

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### Temporización (-T)

Equilibrio entre velocidad, sigilo y estabilidad

**Aparece en 1 clase(s):** [Clase 69 — Reconocimiento activo](../classes/parte-3-hacking-etico-y-pentesting-metodologia/069-reconocimiento-activo/README.md).

### testssl.sh / SSL Labs

Herramientas de auditoría de configuración TLS

**Aparece en 1 clase(s):** [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### Textbook RSA

Aplicar la fórmula sin relleno; determinista y maleable

**Aparece en 1 clase(s):** [Clase 49 — Cifrado asimétrico: RSA](../classes/parte-2-criptografia-aplicada/049-cifrado-asimetrico-rsa/README.md).

### Texto claro / texto cifrado

Mensaje legible / resultado de cifrarlo

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### TGT / TGS

Tickets de Kerberos (concesión y servicio)

**Aparece en 1 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### ThreadPoolExecutor

Gestor de un pool de hilos reutilizables de `concurrent.futures`

**Aparece en 1 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### Threat

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 360 — Capstone: incidente completo de Game Security](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/360-capstone-incidente-completo-game-security/README.md).

### Threat hunting

Búsqueda proactiva a partir de hipótesis, sin alerta previa

**Aparece en 1 clase(s):** [Clase 43 — Network Security Monitoring (NSM): fundamentos](../classes/parte-1-redes-y-seguridad-de-redes/043-network-security-monitoring-nsm-fundamentos/README.md).

### Threat-informed

Ejercicio guiado por la inteligencia de un adversario real

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### Threat intelligence (CTI)

Conocimiento accionable sobre los adversarios

**Aparece en 1 clase(s):** [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md).

### threshold / suppress

Limitar repeticiones y silenciar orígenes conocidos

**Aparece en 1 clase(s):** [Clase 35 — IDS/IPS con Snort y Suricata](../classes/parte-1-redes-y-seguridad-de-redes/035-ids-ips-con-snort-y-suricata/README.md).

### Tiempo constante

Comparación que no depende de dónde falla la coincidencia

**Aparece en 2 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md), [Clase 52 — HMAC y autenticación de mensajes](../classes/parte-2-criptografia-aplicada/052-hmac-y-autenticacion-de-mensajes/README.md).

### Tier

Nivel de madurez del proceso de gestión de riesgo (1 a 4)

**Aparece en 2 clase(s):** [Clase 3 — Frameworks de seguridad: NIST CSF, ISO 27001, MITRE ATT&CK y Diamond Model](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md), [Clase 279 — NIST Cybersecurity Framework](../classes/parte-14-grc-riesgo-y-cumplimiento/279-nist-cybersecurity-framework/README.md).

### Timeout

Tiempo máximo de espera de una operación de red

**Aparece en 1 clase(s):** [Clase 16 — Python para seguridad: sockets y programación de red](../classes/parte-0-fundamentos-y-prerrequisitos/016-python-para-seguridad-sockets-y-programacion-de-red/README.md).

### Timestomping

Falsear las marcas de tiempo de un fichero

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### TIMEWAIT

Estado de espera tras cerrar que evita solapamiento con conexiones nuevas.

**Aparece en 1 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md).

### Tipo 1 / bare-metal

Hipervisor que corre directo sobre el hardware

**Aparece en 1 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md).

### Tipo 2 / hosted

Hipervisor que corre sobre un sistema operativo anfitrión

**Aparece en 1 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md).

### TLS

Protocolo que da confidencialidad, integridad y autenticación al canal

**Aparece en 2 clase(s):** [Clase 13 — HTTP, HTTPS y la arquitectura de la web moderna](../classes/parte-0-fundamentos-y-prerrequisitos/013-http-https-y-la-arquitectura-de-la-web-moderna/README.md), [Clase 56 — TLS/SSL en profundidad](../classes/parte-2-criptografia-aplicada/056-tls-ssl-en-profundidad/README.md).

### TLS callback

Código ejecutado antes del entry point; anti-debug

**Aparece en 1 clase(s):** [Clase 145 — El formato PE de Windows](../classes/parte-6-analisis-de-malware/145-el-formato-pe-de-windows/README.md).

### Toggles

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 345 — Trainers e instrumentación del cliente](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/345-trainers-instrumentacion-cliente/README.md).

### Token

Estructura con la identidad y privilegios de un proceso

**Aparece en 1 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md).

### Token anti-CSRF

Valor secreto e impredecible que debe volver con la petición

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### Token de acceso

Representa el contexto de seguridad de un proceso

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### Token de reseteo

Debe ser impredecible, corto y de un solo uso

**Aparece en 1 clase(s):** [Clase 101 — Fallos de autenticación y bypass](../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md).

### Tool boundary

Frontera donde texto puede provocar una operación.

**Aparece en 1 clase(s):** [Clase 297 — Seguridad de aplicaciones con LLM: RAG y agentes](../classes/parte-15-seguridad-de-ia-y-machine-learning/297-seguridad-de-aplicaciones-con-llm-rag-y-agentes/README.md).

### top chunk

Bloque grande contiguo del que se recorta

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### TPLC

Gestión del producto durante diseño, mercado, soporte y retiro.

**Aparece en 1 clase(s):** [Clase 275 — Seguridad de dispositivos médicos](../classes/parte-13-seguridad-movil-iot-e-inalambrica/275-seguridad-de-dispositivos-medicos/README.md).

### Tráfico este-oeste

Comunicación entre hosts internos; objeto de la microsegmentación

**Aparece en 3 clase(s):** [Clase 37 — Proxies, NAT y pivoting de red](../classes/parte-1-redes-y-seguridad-de-redes/037-proxies-nat-y-pivoting-de-red/README.md), [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md), [Clase 79 — Pivoting y reenvío de puertos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/079-pivoting-y-reenvio-de-puertos/README.md).

### Trama

PDU de la capa de enlace (lleva MAC y FCS)

**Aparece en 1 clase(s):** [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md).

### Trama (frame)

Unidad de datos en el cable, con todas las cabeceras encapsuladas

**Aparece en 1 clase(s):** [Clase 26 — Wireshark: captura y análisis de paquetes](../classes/parte-1-redes-y-seguridad-de-redes/026-wireshark-captura-y-analisis-de-paquetes/README.md).

### Tramas de gestión

Asociación, autenticación y *beacons*; superficie de ataque clave

**Aparece en 1 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md).

### Transfer-Encoding (TE)

Cuerpo por chunks; termina con un chunk vacío

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Transform/módulo

Operación que consulta o deriva relaciones.

**Aparece en 1 clase(s):** [Clase 255 — Automatización de OSINT: SpiderFoot y Maltego](../classes/parte-12-osint-e-ingenieria-social/255-automatizacion-de-osint-spiderfoot-y-maltego/README.md).

### Transposición

Reordenar los símbolos sin cambiarlos

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### trap

Ejecuta código ante señales o al salir del script

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### Trayectoria,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 356 — Detección de aimbot y automatización por comportamiento](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/356-deteccion-aimbot-automatizacion-comportamiento/README.md).

### Trazabilidad

Cada afirmación respaldada por evidencia registrada

**Aparece en 1 clase(s):** [Clase 85 — Reporte profesional de pentest](../classes/parte-3-hacking-etico-y-pentesting-metodologia/085-reporte-profesional-de-pentest/README.md).

### Triage

Clasificación inicial que determina alcance, urgencia y respuesta.

**Claves de búsqueda normalizadas:** `triaje`.

**Aparece en 3 clase(s):** [Clase 114 — Bug bounty: metodología y plataformas](../classes/parte-4-seguridad-de-aplicaciones-web/114-bug-bounty-metodologia-y-plataformas/README.md), [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md), [Clase 259 — Defensa contra la ingeniería social](../classes/parte-12-osint-e-ingenieria-social/259-defensa-contra-la-ingenieria-social/README.md).

### Triage / dedup

Agrupar crashes por su causa raíz

**Aparece en 1 clase(s):** [Clase 136 — Fuzzing con AFL++ y libFuzzer](../classes/parte-5-explotacion-de-sistemas-y-binarios/136-fuzzing-con-afl-y-libfuzzer/README.md).

### Triage del reto

file, checksec, strings, abrir en Ghidra

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### Troubleshooting

Depurar fallos, casi siempre de configuración

**Aparece en 1 clase(s):** [Clase 73 — Metasploit: explotación y payloads](../classes/parte-3-hacking-etico-y-pentesting-metodologia/073-metasploit-explotacion-y-payloads/README.md).

### Troyano

Se disfraza de software legítimo

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### Truncamiento

Asignar a un tipo más pequeño descarta bits altos

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Trust

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 341 — Introducción a Game Security y modelo de amenazas](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/341-introduccion-game-security-modelo-amenazas/README.md).

### Trusted agent

Contacto autorizado que confirma o desmiente actividad del ejercicio

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### Trusted Types

Política del navegador que elimina el DOM XSS por diseño

**Aparece en 1 clase(s):** [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### TryHackMe (THM)

Plataforma de aprendizaje guiado mediante rutas, salas explicativas y salas de desafío.

**Claves de búsqueda normalizadas:** `thm`, `tryhackme`.

**Sitio oficial:** [TryHackMe (THM)](https://tryhackme.com/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### tshark

Wireshark en línea de comandos; mismo lenguaje de filtros

**Aparece en 1 clase(s):** [Clase 27 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas](../classes/parte-1-redes-y-seguridad-de-redes/027-analisis-de-trafico-filtros-seguimiento-de-flujos-y-estadisticas/README.md).

### TTD

Tiempo a detección: cuánto tarda la defensa en ver la actividad

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### TTL

Contador de saltos que evita bucles y sirve para fingerprinting.

**Aparece en 3 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md), [Clase 41 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling](../classes/parte-1-redes-y-seguridad-de-redes/041-seguridad-de-dns-envenenamiento-dnssec-y-tunneling/README.md), [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### TTL (DNS)

Tiempo que una respuesta puede permanecer en caché.

**Aparece en 1 clase(s):** [Clase 12 — DNS, DHCP y ARP: funcionamiento y riesgos](../classes/parte-0-fundamentos-y-prerrequisitos/012-dns-dhcp-y-arp-funcionamiento-y-riesgos/README.md).

### TTP / ATT&CK

Comportamiento mapeado a la taxonomía

**Aparece en 1 clase(s):** [Clase 160 — Reporte de análisis de malware](../classes/parte-6-analisis-de-malware/160-reporte-de-analisis-de-malware/README.md).

### TTP — Tácticas, técnicas y procedimientos

Tácticas, técnicas y procedimientos; la firma comportamental de un actor

**Claves de búsqueda normalizadas:** `ttp`, `ttps`.

**Aparece en 4 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md), [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md), [Clase 157 — Threat intelligence a partir de malware](../classes/parte-6-analisis-de-malware/157-threat-intelligence-a-partir-de-malware/README.md), [Clase 163 — Emulación de adversarios](../classes/parte-7-red-team-y-operaciones-ofensivas/163-emulacion-de-adversarios/README.md).

### TTR

Tiempo a respuesta: cuánto tarda en contener la actividad

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### Túnel

Encapsulación de un paquete dentro de otro para atravesar una red

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### Túnel ICMP

Datos ocultos en el payload de los ping

**Aparece en 1 clase(s):** [Clase 83 — Exfiltración de datos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/083-exfiltracion-de-datos/README.md).

### tuple

Secuencia ordenada e inmutable.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### Turbo Intruder

Herramienta para lanzar peticiones simultáneas

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### Turing-completitud

Con suficientes gadgets se computa cualquier cosa

**Aparece en 1 clase(s):** [Clase 124 — Return-Oriented Programming (ROP)](../classes/parte-5-explotacion-de-sistemas-y-binarios/124-return-oriented-programming-rop/README.md).

## U

### UAC

Control de cuentas de usuario (elevación de privilegios)

**Aparece en 2 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md), [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### UAC bypass

Técnicas para elevar sin el aviso

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### UART

Enlace serie asíncrono con RX/TX y referencia común.

**Aparece en 1 clase(s):** [Clase 268 — Análisis de hardware: UART, JTAG y SPI](../classes/parte-13-seguridad-movil-iot-e-inalambrica/268-analisis-de-hardware-uart-jtag-y-spi/README.md).

### UBSan

Sanitizer que detecta overflows de enteros en pruebas

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### UDP

Transporte sin conexión, rápido y sin garantías de entrega ni orden.

**Aparece en 1 clase(s):** [Clase 11 — Protocolos de red: IP, TCP, UDP e ICMP en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/011-protocolos-de-red-ip-tcp-udp-e-icmp-en-profundidad/README.md).

### UDP scan (-sU)

Escaneo UDP; lento y ambiguo, pero cubre DNS, SNMP y NTP

**Aparece en 1 clase(s):** [Clase 30 — Nmap: escaneo de puertos y tipos de escaneo](../classes/parte-1-redes-y-seguridad-de-redes/030-nmap-escaneo-de-puertos-y-tipos-de-escaneo/README.md).

### UEFI bootkit

Se instala en el firmware; sobrevive al formateo

**Aparece en 1 clase(s):** [Clase 151 — Rootkits y bootkits](../classes/parte-6-analisis-de-malware/151-rootkits-y-bootkits/README.md).

### UID

Identificador de tag; su estabilidad y seguridad dependen de tecnología.

**Aparece en 2 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md), [Clase 270 — Ataques a RFID y NFC](../classes/parte-13-seguridad-movil-iot-e-inalambrica/270-ataques-a-rfid-y-nfc/README.md).

### UID de aplicación

Identidad Linux usada para aislar procesos y archivos.

**Aparece en 1 clase(s):** [Clase 261 — Seguridad de Android: arquitectura](../classes/parte-13-seguridad-movil-iot-e-inalambrica/261-seguridad-de-android-arquitectura/README.md).

### UID / GID

Identificadores numéricos de usuario y grupo

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

### umask

Máscara que resta permisos a los archivos nuevos

**Aparece en 1 clase(s):** [Clase 5 — Linux esencial para seguridad: filesystem, permisos y usuarios](../classes/parte-0-fundamentos-y-prerrequisitos/005-linux-esencial-para-seguridad-filesystem-permisos-y-usuarios/README.md).

### Unicode

Catálogo universal de code points

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

### Unicode / UTF-16

Codificación de cadenas en Windows

**Aparece en 1 clase(s):** [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md).

### Unicorn Engine

Emula solo la CPU; ideal para fragmentos

**Aparece en 1 clase(s):** [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### UNION-based

`UNION SELECT` para leer datos de otras tablas

**Aparece en 1 clase(s):** [Clase 91 — Inyección SQL: fundamentos](../classes/parte-4-seguridad-de-aplicaciones-web/091-inyeccion-sql-fundamentos/README.md).

### Universal link

Enlace web asociado criptográficamente con una aplicación y dominio.

**Aparece en 1 clase(s):** [Clase 264 — Pentest de aplicaciones iOS](../classes/parte-13-seguridad-movil-iot-e-inalambrica/264-pentest-de-aplicaciones-ios/README.md).

### Unkeyed input

Entrada que afecta a la respuesta pero no a la clave

**Aparece en 1 clase(s):** [Clase 112 — Web cache poisoning y HTTP request smuggling](../classes/parte-4-seguridad-de-aplicaciones-web/112-web-cache-poisoning-y-http-request-smuggling/README.md).

### Unpacking

Recuperar el código real del malware empaquetado

**Aparece en 1 clase(s):** [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Unpacking automático

Emular el stub y volcar el código desempaquetado

**Aparece en 1 clase(s):** [Clase 158 — Emulación y unpacking automatizado](../classes/parte-6-analisis-de-malware/158-emulacion-y-unpacking-automatizado/README.md).

### Unquoted path

Ruta de servicio con espacios y sin comillas (escalada)

**Aparece en 1 clase(s):** [Clase 8 — Windows esencial para seguridad: arquitectura, registro y servicios](../classes/parte-0-fundamentos-y-prerrequisitos/008-windows-esencial-para-seguridad-arquitectura-registro-y-servicios/README.md).

### Unquoted service path

Ruta de servicio con espacios sin comillas; explotable

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### unserialize()

Función de PHP vulnerable con datos del usuario

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

### unsorted/small/large bins

Otras listas de chunks libres

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### UPX

Packer común que se deshace con un comando

**Aparece en 2 clase(s):** [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md), [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Use-after-free (UAF)

Usar un puntero a memoria ya liberada

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### User-mode

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 353 — Arquitecturas Anti-Cheat](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/353-arquitecturas-anticheat/README.md).

### Uso responsable

Solo dentro del alcance autorizado; intrusiva por diseño

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### Usos legítimos

Análisis de malware, RE de vulnerabilidades, forense

**Aparece en 1 clase(s):** [Clase 130 — Ingeniería inversa: introducción](../classes/parte-5-explotacion-de-sistemas-y-binarios/130-ingenieria-inversa-introduccion/README.md).

### UTF-8

Codificación de Unicode en 1-4 bytes

**Aparece en 1 clase(s):** [Clase 20 — Sistemas de numeración y encoding: binario, hex, base64 y URL](../classes/parte-0-fundamentos-y-prerrequisitos/020-sistemas-de-numeracion-y-encoding-binario-hex-base64-y-url/README.md).

## V

### Vacunación

Crear el mutex para engañar al malware

**Aparece en 1 clase(s):** [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### Validación activa

Interacción directa con el servicio, sujeta a autorización.

**Aparece en 1 clase(s):** [Clase 254 — OSINT técnico: Shodan y Censys](../classes/parte-12-osint-e-ingenieria-social/254-osint-tecnico-shodan-y-censys/README.md).

### Validación de entrada

Rechazar lo que no encaja, con allowlists

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### Validación de Referer

Defensa débil; el Referer puede faltar

**Aparece en 1 clase(s):** [Clase 98 — Cross-Site Request Forgery (CSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/098-cross-site-request-forgery-csrf/README.md).

### Validación de tipos

Rechazar objetos donde se espera texto; la defensa clave

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### Validación por extensión

Comprobar el sufijo; evadible con blocklist

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### Validado ≠ usado

El número comprobado difiere del realmente usado

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Validar IP resuelta

Comprobar la IP real antes de conectar

**Aparece en 1 clase(s):** [Clase 99 — Server-Side Request Forgery (SSRF)](../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md).

### Valor autoritativo en servidor

Precios y saldos calculados en el servidor

**Aparece en 1 clase(s):** [Clase 109 — Vulnerabilidades de lógica de negocio](../classes/parte-4-seguridad-de-aplicaciones-web/109-vulnerabilidades-de-logica-de-negocio/README.md).

### Variable de entorno

Mejor que el código, pero visible en procesos y volcados

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### Vaudenay (2002)

Descripción original del ataque de padding oracle

**Aparece en 1 clase(s):** [Clase 60 — Ataques criptográficos: padding oracle y timing](../classes/parte-2-criptografia-aplicada/060-ataques-criptograficos-padding-oracle-y-timing/README.md).

### Vault

Gestor de secretos con autenticación, políticas y auditoría

**Aparece en 1 clase(s):** [Clase 63 — Gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).

### vcan

Interfaz CAN virtual de Linux sin bus físico.

**Aparece en 1 clase(s):** [Clase 274 — Seguridad automotriz y bus CAN](../classes/parte-13-seguridad-movil-iot-e-inalambrica/274-seguridad-automotriz-y-bus-can/README.md).

### Vector2/Vector3

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 348 — Matemática de un aimbot](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/348-matematica-aimbot/README.md).

### Velocidad,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 349 — Aimbot avanzado, predicción, smoothing y recoil](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/349-aimbot-avanzado-prediccion-smoothing-recoil/README.md).

### Velocidad/aceleración

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 356 — Detección de aimbot y automatización por comportamiento](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/356-deteccion-aimbot-automatizacion-comportamiento/README.md).

### Ventana de pruebas

Franja horaria autorizada para operar

**Aparece en 1 clase(s):** [Clase 67 — Reglas de engagement, alcance y contratos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/067-reglas-de-engagement-alcance-y-contratos/README.md).

### venv

Entorno virtual que aísla dependencias por proyecto.

**Aparece en 1 clase(s):** [Clase 15 — Python para seguridad: fundamentos del lenguaje](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md).

### Verificación en tiempo constante

Comparación que no filtra información por timing

**Aparece en 1 clase(s):** [Clase 57 — Almacenamiento seguro de contraseñas: bcrypt, scrypt y Argon2](../classes/parte-2-criptografia-aplicada/057-almacenamiento-seguro-de-contrasenas-bcrypt-scrypt-y-argon2/README.md).

### Verificación manual

Confirmar un hallazgo cruzando CVE, CPE y exploits

**Aparece en 1 clase(s):** [Clase 71 — Análisis de vulnerabilidades con Nessus y OpenVAS](../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md).

### Verificación por objeto

Comprobar el permiso sobre el recurso concreto

**Aparece en 1 clase(s):** [Clase 105 — Control de acceso roto: IDOR y path traversal](../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md).

### Verificación pública

Cualquiera con la clave pública puede comprobar la firma

**Aparece en 1 clase(s):** [Clase 54 — Firmas digitales](../classes/parte-2-criptografia-aplicada/054-firmas-digitales/README.md).

### Verificar antes de descifrar

Orden que elimina el padding oracle

**Aparece en 1 clase(s):** [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### Verified Boot

Cadena de verificación de integridad de componentes de arranque.

**Aparece en 1 clase(s):** [Clase 261 — Seguridad de Android: arquitectura](../classes/parte-13-seguridad-movil-iot-e-inalambrica/261-seguridad-de-android-arquitectura/README.md).

### verify=False

Desactivar la validación de certificados; anula TLS

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### Versionado del cifrado

Guardar algoritmo y parámetros junto al dato

**Aparece en 1 clase(s):** [Clase 65 — Implementaciones seguras y errores criptográficos comunes](../classes/parte-2-criptografia-aplicada/065-implementaciones-seguras-y-errores-criptograficos-comunes/README.md).

### Versiones antiguas

`/api/v1` puede seguir vivo sin protección

**Aparece en 1 clase(s):** [Clase 110 — Seguridad de APIs REST](../classes/parte-4-seguridad-de-aplicaciones-web/110-seguridad-de-apis-rest/README.md).

### VEX

Declaración del estado de afectación de un producto respecto de vulnerabilidades.

**Aparece en 2 clase(s):** [Clase 240 — SCA: dependencias y riesgo de terceros](../classes/parte-11-devsecops-y-seguridad-del-sdlc/240-sca-dependencias-y-riesgo-de-terceros/README.md), [Clase 246 — Supply chain security: SBOM y SLSA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md).

### Vía JSON

La API acepta JSON y el atacante controla la estructura

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### Vía query string

`user[$ne]=x` se parsea a objeto automáticamente

**Aparece en 1 clase(s):** [Clase 94 — Inyección NoSQL](../classes/parte-4-seguridad-de-aplicaciones-web/094-inyeccion-nosql/README.md).

### Vigenère

Cifrado polialfabético con clave repetida

**Aparece en 1 clase(s):** [Clase 46 — Historia y fundamentos de la criptografía](../classes/parte-2-criptografia-aplicada/046-historia-y-fundamentos-de-la-criptografia/README.md).

### ViperMonkey

Emulador de VBA para desofuscar

**Aparece en 1 clase(s):** [Clase 152 — Análisis de documentos maliciosos: macros y PDF](../classes/parte-6-analisis-de-malware/152-analisis-de-documentos-maliciosos-macros-y-pdf/README.md).

### Virtual host

Sitio que responde según la cabecera `Host`; oculta contenido

**Aparece en 1 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md).

### Virtualización

Traducir a bytecode propio con intérprete

**Aparece en 1 clase(s):** [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### Virtualización de código

Bytecode propio con intérprete embebido

**Aparece en 1 clase(s):** [Clase 135 — Ofuscación y técnicas anti-reversing](../classes/parte-5-explotacion-de-sistemas-y-binarios/135-ofuscacion-y-tecnicas-anti-reversing/README.md).

### Virus

Se inserta en otro programa y se propaga al ejecutarlo

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### VirusTotal

Servicio que agrega detecciones de múltiples motores

**Aparece en 1 clase(s):** [Clase 143 — Análisis estático básico](../classes/parte-6-analisis-de-malware/143-analisis-estatico-basico/README.md).

### visheapchunks

Comando de pwndbg que visualiza el heap

**Aparece en 1 clase(s):** [Clase 126 — Explotación de heap: fundamentos](../classes/parte-5-explotacion-de-sistemas-y-binarios/126-explotacion-de-heap-fundamentos/README.md).

### Vishing

Ingeniería social mediante voz o telefonía.

**Aparece en 1 clase(s):** [Clase 257 — Pretexting y vishing](../classes/parte-12-osint-e-ingenieria-social/257-pretexting-y-vishing/README.md).

### Vista de grafo

Código como bloques básicos conectados por saltos

**Aparece en 1 clase(s):** [Clase 132 — IDA Pro y radare2](../classes/parte-5-explotacion-de-sistemas-y-binarios/132-ida-pro-y-radare2/README.md).

### VLAN hopping

Saltar de una VLAN a otra rompiendo la segmentación

**Aparece en 1 clase(s):** [Clase 39 — Ataques de capa 2: ARP spoofing y VLAN hopping](../classes/parte-1-redes-y-seguridad-de-redes/039-ataques-de-capa-2-arp-spoofing-y-vlan-hopping/README.md).

### VLAN / subred

Separación de la red en grandes bloques lógicos

**Aparece en 1 clase(s):** [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md).

### VLSM

Subredes de longitud variable ajustadas a cada segmento.

**Aparece en 1 clase(s):** [Clase 14 — Direccionamiento IP y subnetting](../classes/parte-0-fundamentos-y-prerrequisitos/014-direccionamiento-ip-y-subnetting/README.md).

### VM

Máquina virtual: entorno de cómputo aislado

**Aparece en 1 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md).

### VM de análisis

Máquina donde se ejecuta y estudia la muestra

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### VM de servicios

Máquina que simula los servicios de red

**Aparece en 1 clase(s):** [Clase 142 — Laboratorio seguro de análisis de malware](../classes/parte-6-analisis-de-malware/142-laboratorio-seguro-de-analisis-de-malware/README.md).

### vmmap

Mapa de memoria del proceso con permisos

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### Volatility

Framework de forense de memoria

**Aparece en 1 clase(s):** [Clase 148 — Análisis de comportamiento](../classes/parte-6-analisis-de-malware/148-analisis-de-comportamiento/README.md).

### Volcado de memoria

Captura de RAM con datos ausentes del disco

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### Volcado de pila

`%p %p %p...` imprime el contenido de la pila

**Aparece en 1 clase(s):** [Clase 125 — Vulnerabilidades de format string](../classes/parte-5-explotacion-de-sistemas-y-binarios/125-vulnerabilidades-de-format-string/README.md).

### Volcado mínimo

Extraer solo lo necesario para probar el impacto

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### Volumen

Almacenamiento persistente fuera del contenedor

**Aparece en 1 clase(s):** [Clase 22 — Docker y contenedores para laboratorios de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md).

### VPN

Red privada extendida sobre una infraestructura pública mediante cifrado

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### VPS

Servidor virtual donde se despliega la infraestructura

**Aparece en 1 clase(s):** [Clase 164 — Diseño de infraestructura de comando y control (C2)](../classes/parte-7-red-team-y-operaciones-ofensivas/164-diseno-de-infraestructura-de-comando-y-control-c2/README.md).

### VRFY / EXPN

Órdenes SMTP que permiten validar o expandir usuarios

**Aparece en 2 clase(s):** [Clase 33 — Enumeración de servicios de red](../classes/parte-1-redes-y-seguridad-de-redes/033-enumeracion-de-servicios-de-red/README.md), [Clase 70 — Enumeración: SMB, SNMP, SMTP y LDAP](../classes/parte-3-hacking-etico-y-pentesting-metodologia/070-enumeracion-smb-snmp-smtp-y-ldap/README.md).

### VSS

Instantáneas de volumen de Windows

**Aparece en 1 clase(s):** [Clase 84 — Anti-forense y borrado de huellas (concepto y límites)](../classes/parte-3-hacking-etico-y-pentesting-metodologia/084-anti-forense-y-borrado-de-huellas-concepto-y-limites/README.md).

### vssadmin delete

Comando de destrucción de respaldos; alerta temprana

**Aparece en 1 clase(s):** [Clase 150 — Ransomware: anatomía y análisis](../classes/parte-6-analisis-de-malware/150-ransomware-anatomia-y-analisis/README.md).

### VT-x / AMD-V

Virtualización asistida por hardware de Intel / AMD

**Aparece en 1 clase(s):** [Clase 4 — Montaje del laboratorio: virtualización, Kali, snapshots y aislamiento de red](../classes/parte-0-fundamentos-y-prerrequisitos/004-montaje-del-laboratorio-virtualizacion-kali-snapshots-y-aislamiento-de-red/README.md).

### vtable

Tabla de punteros a métodos virtuales de un objeto

**Aparece en 1 clase(s):** [Clase 127 — Heap: use-after-free y double free](../classes/parte-5-explotacion-de-sistemas-y-binarios/127-heap-use-after-free-y-double-free/README.md).

### Vulnerabilidad candidata

Source que alcanza un sink sin validación

**Aparece en 1 clase(s):** [Clase 137 — Descubrimiento de vulnerabilidades en código](../classes/parte-5-explotacion-de-sistemas-y-binarios/137-descubrimiento-de-vulnerabilidades-en-codigo/README.md).

### Vulnerability Assessment (VA)

Inventario de debilidades conocidas, sin explotación profunda

**Aparece en 1 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md).

### VulnHub

Catálogo de máquinas virtuales vulnerables descargables para practicar en una red local aislada.

**Sitio oficial:** [VulnHub](https://www.vulnhub.com/).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### vulnserver

Servidor vulnerable para practicar en Windows

**Aparece en 1 clase(s):** [Clase 129 — Explotación en Windows: manejo de SEH](../classes/parte-5-explotacion-de-sistemas-y-binarios/129-explotacion-en-windows-manejo-de-seh/README.md).

## W

### WAF

Firewall de aplicación que filtra peticiones maliciosas

**Aparece en 3 clase(s):** [Clase 1 — Qué es la ciberseguridad: tríada CIA, AAA, superficie de ataque y defensa en profundidad](../classes/parte-0-fundamentos-y-prerrequisitos/001-que-es-la-ciberseguridad-triada-cia-aaa-superficie-de-ataque-y-defensa-en-profundidad/README.md), [Clase 10 — Redes TCP/IP: modelo OSI, encapsulación y capas](../classes/parte-0-fundamentos-y-prerrequisitos/010-redes-tcp-ip-modelo-osi-encapsulacion-y-capas/README.md), [Clase 86 — Arquitectura web moderna y superficie de ataque](../classes/parte-4-seguridad-de-aplicaciones-web/086-arquitectura-web-moderna-y-superficie-de-ataque/README.md).

### Watchpoint

Pausa cuando una posición de memoria cambia

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### Watermarking

Marca de agua robusta para trazar procedencia

**Aparece en 1 clase(s):** [Clase 64 — Esteganografía y ocultación de datos](../classes/parte-2-criptografia-aplicada/064-esteganografia-y-ocultacion-de-datos/README.md).

### Weaponization

Fase de preparación del artefacto malicioso

**Aparece en 1 clase(s):** [Clase 2 — El panorama de amenazas moderno: actores, motivaciones y Cyber Kill Chain](../classes/parte-0-fundamentos-y-prerrequisitos/002-el-panorama-de-amenazas-moderno-actores-motivaciones-y-cyber-kill-chain/README.md).

### Web Security Academy

Plataforma gratuita de PortSwigger con material y laboratorios interactivos de seguridad web.

**Claves de búsqueda normalizadas:** `portswigger web security academy`, `wsa`.

**Sitio oficial:** [Web Security Academy](https://portswigger.net/web-security).

**Entrada transversal:** sin glosario local todavía; consulta el recurso oficial enlazado.

### Web shell

Fichero ejecutable subido que da RCE al visitarlo

**Aparece en 1 clase(s):** [Clase 108 — Vulnerabilidades en carga de archivos](../classes/parte-4-seguridad-de-aplicaciones-web/108-vulnerabilidades-en-carga-de-archivos/README.md).

### WEP

Cifrado WiFi roto en parte por reutilización de nonce

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### Where-Object

Filtra objetos del pipeline por una condición

**Aparece en 1 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md).

### White box

Acceso total a código y arquitectura

**Aparece en 1 clase(s):** [Clase 66 — Metodología de pentesting: PTES y OSSTMM](../classes/parte-3-hacking-etico-y-pentesting-metodologia/066-metodologia-de-pentesting-ptes-y-osstmm/README.md).

### White cell

Personas informadas que supervisan el ejercicio y protegen a los objetivos

**Aparece en 2 clase(s):** [Clase 161 — Red Team vs pentest: filosofía y objetivos](../classes/parte-7-red-team-y-operaciones-ofensivas/161-red-team-vs-pentest-filosofia-y-objetivos/README.md), [Clase 166 — Phishing y entrega de payloads](../classes/parte-7-red-team-y-operaciones-ofensivas/166-phishing-y-entrega-de-payloads/README.md).

### White hat

Hacker ético con autorización

**Aparece en 1 clase(s):** [Clase 25 — Ética, legalidad, alcance y divulgación responsable](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).

### WHOIS / RDAP

Propietario, contactos y rangos de un dominio o IP

**Aparece en 1 clase(s):** [Clase 68 — Reconocimiento pasivo e inteligencia de fuentes abiertas](../classes/parte-3-hacking-etico-y-pentesting-metodologia/068-reconocimiento-pasivo-e-inteligencia-de-fuentes-abiertas/README.md).

### wide

Busca la versión Unicode/UTF-16 de la cadena

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### WinPEAS / PowerUp

Herramientas de enumeración de escalada en Windows

**Aparece en 1 clase(s):** [Clase 77 — Escalada de privilegios en Windows](../classes/parte-3-hacking-etico-y-pentesting-metodologia/077-escalada-de-privilegios-en-windows/README.md).

### Wiper

Destruye datos sin recuperación posible

**Aparece en 1 clase(s):** [Clase 141 — Introducción al malware: tipos y taxonomía](../classes/parte-6-analisis-de-malware/141-introduccion-al-malware-tipos-y-taxonomia/README.md).

### WireGuard

VPN moderna en kernel, con criptografía fija y configuración mínima

**Aparece en 1 clase(s):** [Clase 36 — VPN y túneles: IPsec, WireGuard y OpenVPN](../classes/parte-1-redes-y-seguridad-de-redes/036-vpn-y-tuneles-ipsec-wireguard-y-openvpn/README.md).

### Wireshark + INetSim

Captura de red con Internet simulado

**Aparece en 1 clase(s):** [Clase 144 — Análisis dinámico básico y sandboxing](../classes/parte-6-analisis-de-malware/144-analisis-dinamico-basico-y-sandboxing/README.md).

### WMI

Interfaz de gestión de Windows accesible desde PowerShell

**Aparece en 1 clase(s):** [Clase 9 — PowerShell para seguridad ofensiva y defensiva](../classes/parte-0-fundamentos-y-prerrequisitos/009-powershell-para-seguridad-ofensiva-y-defensiva/README.md).

### WMI event subscription

Persistencia fileless disparada por eventos

**Aparece en 1 clase(s):** [Clase 82 — Persistencia en sistemas comprometidos](../classes/parte-3-hacking-etico-y-pentesting-metodologia/082-persistencia-en-sistemas-comprometidos/README.md).

### WMI / WinRM

Ejecución remota más sigilosa, sobre gestión legítima

**Aparece en 1 clase(s):** [Clase 78 — Movimiento lateral en la red](../classes/parte-3-hacking-etico-y-pentesting-metodologia/078-movimiento-lateral-en-la-red/README.md).

### Word splitting

Partición de un valor no entrecomillado por espacios

**Aparece en 1 clase(s):** [Clase 7 — Bash scripting para tareas de seguridad](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md).

### Worker / manager

Procesos que reparten el tráfico y consolidan los logs

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### Workspace

Aislamiento de los datos por cliente o fase

**Aparece en 1 clase(s):** [Clase 72 — Metasploit Framework: arquitectura y uso](../classes/parte-3-hacking-etico-y-pentesting-metodologia/072-metasploit-framework-arquitectura-y-uso/README.md).

### WORLD→VIEW→PROJECTION→SCREEN

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 346 — Información expuesta, radar, ESP y world-to-screen](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/346-informacion-expuesta-radar-esp-world-to-screen/README.md).

### WPA2-PSK

Cifrado con clave precompartida; vulnerable a crackeo offline

**Aparece en 1 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md).

### WPA3-SAE (Dragonfly)

Handshake que no expone material para crackeo offline

**Aparece en 1 clase(s):** [Clase 38 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque](../classes/parte-1-redes-y-seguridad-de-redes/038-seguridad-wifi-wpa2-wpa3-y-superficie-de-ataque/README.md).

### Wrap-around

El valor da la vuelta al superar el máximo del tipo

**Aparece en 1 clase(s):** [Clase 128 — Integer overflows y errores aritméticos](../classes/parte-5-explotacion-de-sistemas-y-binarios/128-integer-overflows-y-errores-aritmeticos/README.md).

### Writeup

Documentación de la solución de un reto

**Claves de búsqueda normalizadas:** `informe de resolucion`, `write up`.

**Relacionados:** CTF — Capture The Flag, RCA — Análisis de causa raíz, Mitigación, IOC — Indicador de compromiso.

**Aparece en 1 clase(s):** [Clase 140 — CTFs de pwn e ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/140-ctfs-de-pwn-e-ingenieria-inversa/README.md).

### WSH

Windows Script Host; ejecuta JScript y VBScript

**Aparece en 1 clase(s):** [Clase 153 — Análisis de malware en scripts: PowerShell y JavaScript](../classes/parte-6-analisis-de-malware/153-analisis-de-malware-en-scripts-powershell-y-javascript/README.md).

## X

### x/ (examine)

Leer memoria en cualquier formato (`x/8gx $rsp`)

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### X-Frame-Options

Cabecera contra clickjacking

**Aparece en 1 clase(s):** [Clase 115 — Secure coding y defensa de aplicaciones web](../classes/parte-4-seguridad-de-aplicaciones-web/115-secure-coding-y-defensa-de-aplicaciones-web/README.md).

### x/NFU

Número, formato y unidad del comando examine

**Aparece en 1 clase(s):** [Clase 118 — Debugging con GDB y pwndbg](../classes/parte-5-explotacion-de-sistemas-y-binarios/118-debugging-con-gdb-y-pwndbg/README.md).

### X25519

DH sobre Curve25519; rápido y sin parámetros débiles

**Aparece en 2 clase(s):** [Clase 50 — Criptografía de curva elíptica (ECC)](../classes/parte-2-criptografia-aplicada/050-criptografia-de-curva-eliptica-ecc/README.md), [Clase 53 — Intercambio de claves: Diffie-Hellman](../classes/parte-2-criptografia-aplicada/053-intercambio-de-claves-diffie-hellman/README.md).

### x64dbg

Depurador usado para el unpacking manual

**Aparece en 1 clase(s):** [Clase 147 — Ofuscación, packing y unpacking](../classes/parte-6-analisis-de-malware/147-ofuscacion-packing-y-unpacking/README.md).

### XChaCha20

Variante con nonce de 192 bits; seguro elegirlo al azar

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### XChaCha20-Poly1305

Variante con nonce de 192 bits; seguro al azar

**Aparece en 1 clase(s):** [Clase 59 — Cifrado autenticado (AEAD)](../classes/parte-2-criptografia-aplicada/059-cifrado-autenticado-aead/README.md).

### XOR

Operación reversible: `(M ⊕ K) ⊕ K = M`

**Aparece en 1 clase(s):** [Clase 48 — Cifrado de flujo: ChaCha20 y por qué evitar RC4](../classes/parte-2-criptografia-aplicada/048-cifrado-de-flujo-chacha20-y-por-que-evitar-rc4/README.md).

### xor rax, rax

Poner a cero sin generar bytes nulos

**Aparece en 1 clase(s):** [Clase 121 — Escritura de shellcode](../classes/parte-5-explotacion-de-sistemas-y-binarios/121-escritura-de-shellcode/README.md).

### xpcmdshell / INTO OUTFILE

Vías de RCE desde la base de datos

**Aparece en 1 clase(s):** [Clase 93 — SQLMap](../classes/parte-4-seguridad-de-aplicaciones-web/093-sqlmap/README.md).

### Xref

Referencia cruzada: quién llama o usa algo

**Aparece en 2 clase(s):** [Clase 131 — Ghidra para ingeniería inversa](../classes/parte-5-explotacion-de-sistemas-y-binarios/131-ghidra-para-ingenieria-inversa/README.md), [Clase 146 — Análisis con IDA y Ghidra aplicado a malware](../classes/parte-6-analisis-de-malware/146-analisis-con-ida-y-ghidra-aplicado-a-malware/README.md).

### XSS

Inyección de JavaScript en el navegador de otra víctima

**Aparece en 1 clase(s):** [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md).

### XSS almacenado (stored)

El payload se guarda y se ejecuta para cada visitante

**Aparece en 1 clase(s):** [Clase 97 — XSS almacenado y basado en DOM](../classes/parte-4-seguridad-de-aplicaciones-web/097-xss-almacenado-y-basado-en-dom/README.md).

### XSS reflejado

El payload viaja en la petición y se refleja en la respuesta

**Aparece en 1 clase(s):** [Clase 96 — Cross-Site Scripting (XSS) reflejado](../classes/parte-4-seguridad-de-aplicaciones-web/096-cross-site-scripting-xss-reflejado/README.md).

### XXE

Abuso de las entidades externas de XML

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### XXE ciega

Sin reflejo; se exfiltra por OOB con DTD externa

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

### XXE → SSRF

La entidad apunta a una URL interna o al metadata

**Aparece en 1 clase(s):** [Clase 100 — XML External Entities (XXE)](../classes/parte-4-seguridad-de-aplicaciones-web/100-xml-external-entities-xxe/README.md).

## Y

### YARA

Lenguaje para describir patrones que identifican malware

**Aparece en 1 clase(s):** [Clase 156 — Reglas YARA para detección](../classes/parte-6-analisis-de-malware/156-reglas-yara-para-deteccion/README.md).

### Yaw,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 348 — Matemática de un aimbot](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/348-matematica-aimbot/README.md).

### ysoserial

Herramienta que genera gadget chains para Java

**Aparece en 1 clase(s):** [Clase 106 — Deserialización insegura](../classes/parte-4-seguridad-de-aplicaciones-web/106-deserializacion-insegura/README.md).

## Z

### Z-score,

Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza.

**Aparece en 1 clase(s):** [Clase 357 — Estadística, anomalías y falsos positivos](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/357-estadistica-anomalias-falsos-positivos/README.md).

### Zeek

Motor de análisis de red que genera logs de transacción, no firmas

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### zeek-cut

Extrae columnas de los logs por nombre, para análisis por CLI

**Aparece en 1 clase(s):** [Clase 44 — Zeek para análisis de red a gran escala](../classes/parte-1-redes-y-seguridad-de-redes/044-zeek-para-analisis-de-red-a-gran-escala/README.md).

### Zero Trust

Modelo que elimina la confianza implícita por ubicación de red

**Aparece en 1 clase(s):** [Clase 42 — Segmentación de red y arquitectura Zero Trust](../classes/parte-1-redes-y-seguridad-de-redes/042-segmentacion-de-red-y-arquitectura-zero-trust/README.md).

### Zona/conducto

Agrupación y comunicación controlada según riesgo y función.

**Aparece en 1 clase(s):** [Clase 273 — Seguridad de sistemas de control industrial (ICS/SCADA)](../classes/parte-13-seguridad-movil-iot-e-inalambrica/273-seguridad-de-sistemas-de-control-industrial-ics-scada/README.md).
