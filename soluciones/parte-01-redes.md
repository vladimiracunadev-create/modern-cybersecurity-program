# Soluciones — Parte 1: Redes y seguridad de redes

> Estas son **claves de referencia** para el instructor y para autoevaluación. Intenta resolver cada reto y ejercicio por tu cuenta **antes** de mirar aquí: el valor está en el proceso, no en la respuesta. Puede haber más de una solución correcta; lo que sigue es una guía técnicamente válida.
>
> Volver al índice de la parte: [../classes/parte-1-redes-y-seguridad-de-redes/README.md](../classes/parte-1-redes-y-seguridad-de-redes/README.md)

Todo se realiza en un entorno de laboratorio aislado (VMs o contenedores propios), sobre redes y hosts propios, y sin apuntar herramientas a sistemas de terceros. Las IPs `192.168.56.0/24`, `10.10.0.0/24` y `10.20.0.0/24` son ejemplos de laboratorio.

---

## Clase 026 — Wireshark: captura y análisis de paquetes

### Solución del reto verificable

Objetivo: entregar un `.pcapng` que contenga **solo** una conversación HTTP completa, más los datos (IP cliente, IP servidor, recurso, código de respuesta).

Pasos:

1. Captura tráfico mixto (ICMP + DNS + HTTP) en tu laboratorio:

   ```bash
   sudo dumpcap -i eth0 -w mixto.pcapng
   # en otra terminal genera tráfico:
   ping -c2 192.168.56.101 ; dig @192.168.56.1 example.com ; curl http://192.168.56.101/index.html
   ```

2. Abre `mixto.pcapng` en Wireshark, clic derecho sobre un paquete HTTP → **Follow → HTTP Stream**. Wireshark autoaplica el filtro `tcp.stream eq N`.
3. Con ese filtro activo: **Archivo → Exportar paquetes especificados → Displayed** y guarda como `http-solo.pcapng`. Solo se escriben los paquetes de esa conversación.
4. Lee los datos de la disección: `ip.src` (cliente), `ip.dst` (servidor), `http.request.uri` (recurso), `http.response.code` (p. ej. `200 OK`).

Verificación equivalente en consola:

```bash
tshark -r http-solo.pcapng -Y http -T fields -e ip.src -e ip.dst -e http.request.uri -e http.response.code
tshark -r http-solo.pcapng -q -z conv,ip     # debe mostrar UNA sola conversación
```

Evidencia que cumple el criterio: la tabla **Estadísticas → Conversaciones** del archivo recortado muestra un único par cliente↔servidor y ningún otro host; los cuatro datos de la nota coinciden con la disección.

### Claves de los ejercicios

1. `ping`: filtro `icmp`. El *echo request* es `icmp.type == 8` y el *reply* `icmp.type == 0`; se emparejan por el mismo `icmp.seq` e `icmp.id`.
2. `User-Agent`: filtro `http.request`; en la disección **HTTP → User-Agent**, o `http.user_agent`. En consola: `tshark -r cap.pcapng -Y http.request -T fields -e http.user_agent`.
3. TTL: añade columna `ip.ttl`. El gateway local suele responder con TTL alto (64/128/255 menos 0 saltos); un host remoto llega con TTL decrementado por cada router. TTL de origen ≈ 64 → Linux/Unix, ≈ 128 → Windows, ≈ 255 → equipo de red/*BSD.
4. Perfil "triage": **Editar → Perfiles de configuración → +**, nómbralo `triage`, define tus columnas y reglas de color; cambia con el selector inferior derecho. Los perfiles se guardan en `~/.config/wireshark/profiles/triage/`.
5. **Estadísticas → Jerarquía de protocolos** muestra el porcentaje de bytes/paquetes por capa y protocolo (Ethernet → IP → TCP/UDP → HTTP/DNS/TLS…).
6. **Archivo → Exportar disecciones de paquetes → As Plain Text**, con "Displayed" y un filtro `tcp.stream eq N` activo, exporta solo ese flujo a texto.

---

## Clase 027 — Análisis de tráfico: filtros, seguimiento de flujos y estadísticas

### Solución del reto verificable

Objetivo: informe con la conversación de más bytes, total de retransmisiones, protocolo dominante y captura del I/O Graph, más el comando `tshark` de verificación.

Pasos:

1. Conversación con más bytes: **Estadísticas → Conversaciones → pestaña TCP**, ordena por columna *Bytes* descendente. En consola:

   ```bash
   tshark -r lab027.pcapng -q -z conv,tcp
   ```

2. Total de retransmisiones (el número exacto que verificará el revisor):

   ```bash
   tshark -r lab027.pcapng -Y 'tcp.analysis.retransmission' | wc -l
   # o sin ambigüedad de conteo:
   tshark -r lab027.pcapng -q -z io,stat,0,'COUNT(tcp.analysis.retransmission)tcp.analysis.retransmission'
   ```

3. Protocolo de aplicación dominante: **Estadísticas → Jerarquía de protocolos** (o `tshark -r lab027.pcapng -q -z io,phs`); toma el de mayor porcentaje.
4. I/O Graph: **Estadísticas → I/O Graph**, añade una serie con filtro `tcp.analysis.retransmission` y captura la imagen.

Evidencia que cumple el criterio: los tres números del informe (bytes de la conversación top, retransmisiones, protocolo dominante) reproducen exactamente lo que da el revisor con `tcp.analysis.retransmission` y la tabla de Conversaciones sobre la misma captura.

### Claves de los ejercicios

1. TLS handshake (Client Hello): `tls.handshake.type == 1`.
2. Conversaciones > 100 KB: tabla **Conversaciones**, ordena por Bytes y filtra las que superan 100000; o `tshark -q -z conv,tcp` y revisa la columna Bytes.
3. Todos los eventos de análisis: `tcp.analysis.flags` (incluye retransmisiones, dup ACK, zero window, etc.).
4. `Server:` de la respuesta: Follow → HTTP Stream y localiza la cabecera, o `tshark -r cap.pcapng -Y http.response -T fields -e http.server`.
5. RTT medio: añade columna `tcp.analysis.ack_rtt`; promedia sus valores (o usa **Estadísticas → TCP Stream Graphs → Round Trip Time**).
6. Endpoints en consola: `tshark -r lab027.pcapng -q -z endpoints,ip`.

---

## Clase 028 — tcpdump y captura de tráfico en línea de comandos

### Solución del reto verificable

Objetivo: capturar 30 s de todo el tráfico **excepto** el puerto 22, con rotación de 5 MB, y entregar el primer archivo, el comando y el conteo de paquetes.

Comando exacto:

```bash
sudo timeout 30 tcpdump -i eth0 -s 0 -C 5 -W 5 -w captura.pcap 'not port 22'
```

- `-C 5` rota cada 5 MB; `-W 5` limita a 5 archivos (`captura.pcap0`, `captura.pcap1`, …); `not port 22` excluye tu sesión SSH; `timeout 30` corta a los 30 s.

Conteo de paquetes del primer archivo:

```bash
tcpdump -r captura.pcap0 -n 'not port 22' | wc -l
```

Evidencia que cumple el criterio: el archivo abre sin errores en Wireshark; el filtro `tcp.port == 22` no devuelve nada hacia/desde tu IP; el conteo declarado coincide con el que obtiene el revisor con `tcpdump -r … | wc -l`.

### Claves de los ejercicios

1. ICMP entre dos hosts: `sudo tcpdump -i eth0 -w icmp.pcap 'icmp and host 192.168.56.10 and host 192.168.56.20'`.
2. HTTP y HTTPS: filtro BPF `port 80 or port 443` (paréntesis si combinas con más términos).
3. RST activo: `sudo tcpdump -i eth0 -n 'tcp[tcpflags] & tcp-rst != 0'`. Un RST rechaza/cierra la conexión: puerto cerrado, reset por firewall o cierre abrupto de la aplicación.
4. `-c 100` detiene tras 100 paquetes; útil para muestreo rápido, pruebas de filtro y evitar capturas enormes cuando solo quieres una muestra.
5. Rotación por tiempo: `sudo tcpdump -i eth0 -G 60 -w 'cap-%Y%m%d-%H%M%S.pcap'` (usa `strftime` en el nombre; añade `-W n` para limitar).
6. Conversión: `editcap captura.pcap captura.pcapng` (editcap detecta el formato por la extensión de salida) y ábrelo en Wireshark.

---

## Clase 029 — Nmap: descubrimiento de hosts y técnicas de ping

### Solución del reto verificable

Objetivo: `vivos.txt` con todos los hosts activos usando la técnica que más detecte, más justificación y evidencia tcpdump.

En una LAN, la técnica que más detecta es **ARP** (`-PR`), default de Nmap cuando el objetivo está en el mismo dominio de difusión: opera en capa 2 y los firewalls de host no la filtran fácilmente.

```bash
# captura las sondas en paralelo para la evidencia:
sudo tcpdump -i eth0 -n arp -w descubrimiento-arp.pcap &
sudo nmap -sn -PR 192.168.56.0/24 -oG - | awk '/Up$/{print $2}' > vivos.txt
sudo pkill tcpdump
```

Justificación (3–4 líneas): en la propia LAN, ARP alcanza incluso hosts que bloquean ICMP/TCP con su firewall, porque responder al ARP es imprescindible para tener conectividad IP; por eso detecta más que `-PE`/`-PS`. A través de un router habría que cambiar a sondas IP (`-PE -PS443,80 -PA`).

Evidencia que cumple el criterio: la captura `descubrimiento-arp.pcap` muestra los `who-has`/`is-at`; `vivos.txt` incluye todos los hosts que el revisor sabe encendidos.

### Claves de los ejercicios

1. `-sn` vs `-sn -PR`: en LAN Nmap ya usa ARP por defecto, así que el conteo suele coincidir; la diferencia aparece si fuerzas sondas IP (`--send-ip`), que detectan menos porque los hosts con firewall no responden a ICMP/TCP.
2. Con `-sn` a otra subred, tcpdump muestra que Nmap envía por defecto ICMP echo (`-PE`), TCP SYN a 443, TCP ACK a 80 e ICMP timestamp; ya **no** ARP (fuera del dominio de difusión).
3. Solo responden a SYN 22: `sudo nmap -sn -PS22 192.168.56.0/24`.
4. List scan: `nmap -sL 192.168.56.0/29`; solo resuelve DNS y lista objetivos, **no** envía paquetes a los hosts (verifícalo con tcpdump: sin tráfico hacia ellos).
5. One-liner a `vivos.txt`: `sudo nmap -sn 192.168.56.0/24 -oG - | awk '/Up$/{print $2}' > vivos.txt` (o partiendo del `.gnmap`: `grep Up hosts-vivos.gnmap | awk '{print $2}'`).
6. `sudo nmap -sn --traceroute 192.168.56.101` añade a cada host vivo la ruta de saltos hasta él.

---

## Clase 030 — Nmap: escaneo de puertos y tipos de escaneo

### Solución del reto verificable

Objetivo: inventario TCP + UDP con estado y **razón** (`--reason`), incluyendo al menos un puerto `filtered` justificado.

```bash
sudo nmap -sS -sU -p T:22,80,443,U:53,161 --reason -oN inventario.txt 192.168.56.101
```

Tabla resultante (ejemplo):

| Puerto | Protocolo | Estado | Razón |
|--------|-----------|--------|-------|
| 22 | tcp | open | syn-ack |
| 80 | tcp | open | syn-ack |
| 443 | tcp | filtered | no-response (o admin-prohibited) |
| 53 | udp | open | udp-response |
| 161 | udp | open\|filtered | no-response |

Evidencia que cumple el criterio: al reescanear, el revisor obtiene los mismos estados; cada uno queda respaldado por su razón (`syn-ack` → open, `reset` → closed, `no-response`/`admin-prohibited` → filtered).

### Claves de los ejercicios

1. `-sS` vs `-sT`: mismos estados, pero `-sS` (semiabierto, envía RST sin completar) es más rápido y no deja log de aplicación; `-sT` usa `connect()`, completa el handshake, es más lento y queda registrado en el servicio.
2. `--reason` sobre un `filtered`: la razón `no-response` (firewall descarta) o `admin-prohibited`/`host-unreachable` (ICMP de rechazo) explica por qué Nmap no puede confirmar apertura.
3. UDP 53 `open|filtered`: si el servicio no responde al datagrama y no llega un ICMP port-unreachable, Nmap no puede distinguir "abierto silencioso" de "filtrado". Con `-sV` o una sonda específica de DNS se resuelve a `open`.
4. `-sA`: si los puertos salen `unfiltered` → firewall **sin estado**; si salen `filtered` (no llega el RST esperado) → firewall **con estado** que descarta ACK no asociados a una conexión.
5. `-T3` vs `-T4 --min-rate 1000`: el segundo es mucho más rápido pero, si la red pierde paquetes, puede marcar puertos abiertos como `filtered` (falsos negativos por timeouts agresivos).
6. Por nombre de servicio: `nmap -p http,https,domain 192.168.56.101` (Nmap traduce vía `/etc/services`/`nmap-services` a 80, 443, 53).

---

## Clase 031 — Nmap: detección de servicios y fingerprinting de OS

### Solución del reto verificable

Objetivo: inventario de servicios con producto, versión y CPE, más una columna "riesgo potencial" con un CVE real de una versión detectada.

```bash
sudo nmap -sV -O -oA servicios 192.168.56.101
grep -o 'cpe:[^ )]*' servicios.nmap | sort -u
```

Tabla (ejemplo):

| Puerto | Producto | Versión | CPE | Riesgo potencial |
|--------|----------|---------|-----|------------------|
| 22 | OpenSSH | 7.2p2 | `cpe:/a:openbsd:openssh:7.2p2` | CVE-2016-6210 (enumeración de usuarios por temporización) |
| 80 | Apache httpd | 2.4.29 | `cpe:/a:apache:http_server:2.4.29` | CVE-2017-15710 (mod_authnz_ldap) |

El CVE se **cita** desde NVD, sin explotarlo.

Evidencia que cumple el criterio: producto, versión y CPE coinciden con el reescaneo del revisor; el CVE citado corresponde realmente a esa versión según <https://nvd.nist.gov/>.

### Claves de los ejercicios

1. Producto/versión/CPE: `-sV` los reporta en la columna VERSION y como línea `CPE:`.
2. `-O` vs `-O --osscan-guess`: sin `--osscan-guess` Nmap solo muestra el OS si supera el umbral de fiabilidad; con él lista las conjeturas más probables aunque ninguna sea exacta.
3. `-A` = `-sV` + `-O` + `-sC` (scripts default) + `--traceroute`; clasifica cada bloque de salida por su fuente.
4. `-O` necesita **al menos un puerto abierto y uno cerrado**: el abierto da respuestas de servicio y el cerrado provoca RST, y de la comparación de ISN/opciones/ventana/TTL infiere la pila TCP/IP.
5. CPE → CVE: copia el CPE en la búsqueda de NVD (o `searchsploit`) para listar CVEs asociados, **sin explotar**.
6. `--version-intensity 0` lanza pocas sondas (rápido, menos preciso) y `9` lanza todas (más preciso, más ruidoso); a mayor intensidad, más servicios difíciles se identifican.

---

## Clase 032 — Nmap Scripting Engine (NSE)

### Solución del reto verificable

Objetivo: escaneo NSE de un servicio web que entregue título, cabeceras de seguridad y cifradores TLS, más interpretación de dos hallazgos.

```bash
sudo nmap -p80,443 \
  --script http-title,http-headers,http-security-headers,ssl-enum-ciphers \
  -oN nse-web.txt 192.168.56.101
```

Interpretación (ejemplo de dos hallazgos de seguridad):

- Falta la cabecera **HSTS** (`Strict-Transport-Security`): el sitio es susceptible a SSL stripping (ver clase 040).
- `ssl-enum-ciphers` marca con `C`/`F` suites obsoletas (p. ej. TLS 1.0 o `3DES`/`RC4`): downgrade y cifrado débil.

Evidencia que cumple el criterio: la salida contiene los tres bloques (título, cabeceras, cifradores) y la interpretación identifica al menos una debilidad real.

### Claves de los ejercicios

1. `ls /usr/share/nmap/scripts/ | grep vuln` lista los scripts `vuln`; elige tres y lee `nmap --script-help <nombre>`.
2. `-sC` ejecuta la categoría `default`: añade título HTTP, cabeceras, certificados TLS, información SMB, etc., según los puertos abiertos.
3. `ssl-enum-ciphers` califica cada suite (`A`–`F`); la presencia de suites `C`/`F` (RC4, 3DES, export) indica soporte de cifradores débiles.
4. `hello.nse` con servicio: añade `local shortport = require "shortport"` no es necesario; en `action` usa `nmap.get_port_state`/`port.service`, p. ej. `return "Puerto " .. port.number .. " servicio " .. (port.service or "?")`.
5. `-sV --script banner` captura el banner crudo; compáralo con la versión que deduce `-sV` (a veces el banner está ofuscado y `-sV` acierta igual por otras sondas).
6. `portrule` decide por puerto (se ejecuta por cada puerto que cumpla la condición); `hostrule` decide por host (una vez por objetivo, sin depender de un puerto concreto).

---

## Clase 033 — Enumeración de servicios de red

### Solución del reto verificable

Objetivo: "hoja de enumeración" por servicio abierto (versión, información sensible, vector priorizado) con comandos reproducibles.

Metodología (una sección por servicio):

```bash
# SMB (445)
smbclient -L //192.168.56.101/ -N
nmap -p445 --script smb-enum-shares,smb-enum-users,smb-os-discovery 192.168.56.101
# HTTP (80)
whatweb http://192.168.56.101/
gobuster dir -u http://192.168.56.101/ -w /usr/share/wordlists/dirb/common.txt -t 30
# DNS (53)
dig @192.168.56.1 lab.local ANY ; dig @192.168.56.1 lab.local AXFR
# SNMP (161/udp)
snmpwalk -v2c -c public 192.168.56.101 | head
```

Hoja (ejemplo):

| Servicio | Versión | Información obtenida | Vector priorizado |
|----------|---------|----------------------|-------------------|
| SMB | Samba 4.x | Share `backups` con acceso null | Descarga de archivos sensibles |
| HTTP | Apache 2.4 | `/admin` (403), `/backup.zip` | Fuga de credenciales en el zip |
| DNS | BIND 9 | AXFR permitido → todos los registros | Mapa completo de la infraestructura |

Evidencia que cumple el criterio: la hoja cubre todos los servicios abiertos, cada hallazgo se reproduce con el comando indicado y el vector es coherente con la información.

### Claves de los ejercicios

1. `smbclient -L //IP/ -N`: los shares que listan sin credenciales admiten null session; confírmalo conectando con `smbclient //IP/share -N`.
2. gobuster: los códigos `200`/`301`/`403` sobre rutas no enlazadas (`/admin`, `/backup`) son directorios ocultos; filtra ruido con `-b 404` o `--exclude-length`.
3. AXFR con éxito = fuga completa de la zona (todos los hosts, subdominios, servicios). Debe estar restringido a los secundarios autorizados (`allow-transfer`).
4. `snmpwalk` con community válida: `sysName` (`1.3.6.1.2.1.1.5.0`) da el nombre del sistema y `hrSWRunName` la tabla de procesos.
5. SMTP `VRFY`: confirma si un usuario existe por la respuesta (250 vs 550); se desactiva porque permite enumerar cuentas válidas para fuerza bruta/phishing.
6. Stack tecnológico: `whatweb http://IP/` (CMS, lenguaje, servidor) + `curl -I http://IP/` (cabeceras `Server`, `X-Powered-By`).

---

## Clase 034 — Firewalls: tipos, iptables y nftables

### Solución del reto verificable

Objetivo: firewall stateful con política **DROP** en INPUT que permita loopback, established, SSH solo desde la subred de laboratorio y HTTP desde cualquiera; registra y descarta el resto.

```bash
sudo iptables -F
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -p tcp -s 192.168.56.0/24 --dport 22 -m conntrack --ctstate NEW -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -m conntrack --ctstate NEW -j ACCEPT
sudo iptables -A INPUT -j LOG --log-prefix "FW-DROP: " -m limit --limit 5/min
sudo iptables -P INPUT DROP
sudo iptables-save > ruleset.txt
```

Equivalente nftables:

```bash
sudo nft add table inet filtro
sudo nft add chain inet filtro entrada '{ type filter hook input priority 0; policy drop; }'
sudo nft add rule inet filtro entrada iif lo accept
sudo nft add rule inet filtro entrada ct state established,related accept
sudo nft add rule inet filtro entrada ip saddr 192.168.56.0/24 tcp dport 22 ct state new accept
sudo nft add rule inet filtro entrada tcp dport 80 ct state new accept
sudo nft add rule inet filtro entrada limit rate 5/minute log prefix "FW-DROP: " drop
```

Evidencia que cumple el criterio: desde otra VM, `nmap -Pn 192.168.56.101` muestra 80 abierto siempre y 22 abierto **solo** desde la subred autorizada; el resto sale `filtered`. Los intentos denegados aparecen con `journalctl -k | grep FW-DROP`.

### Claves de los ejercicios

1. SSH solo desde una subred: `-A INPUT -p tcp -s 192.168.56.0/24 --dport 22 -j ACCEPT` (y DROP por defecto).
2. Limitar fuerza bruta: `-A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m limit --limit 3/min --limit-burst 3 -j ACCEPT`; en nftables `tcp dport 22 ct state new limit rate 3/minute accept`.
3. Traducir iptables→nftables: mantén el orden (ACCEPT específicos antes del DROP); verifica con un escaneo que ambos dan el mismo resultado.
4. Logging solo de denegados: coloca la regla `LOG` justo antes de la política DROP; consúltalo con `journalctl -k -g FW-DROP`.
5. OUTPUT restrictivo: `-P OUTPUT DROP` + ACCEPT para established, DNS (`--dport 53`) y HTTP/HTTPS (`--dport 80,443`).
6. `sudo conntrack -E` muestra en vivo eventos `[NEW]`, `[UPDATE]`, `[DESTROY]` de cada conexión.

---

## Clase 035 — IDS/IPS con Snort y Suricata

### Solución del reto verificable

Objetivo: Suricata en modo IDS con una regla propia que detecte un patrón concreto, generar el tráfico y entregar regla + línea de `fast.log` + objeto de `eve.json`.

Regla en `/etc/suricata/rules/local.rules`:

```text
alert http any any -> $HOME_NET any (msg:"Acceso a /admin con user-agent sospechoso"; flow:to_server,established; http.uri; content:"/admin"; http.user_agent; content:"evilscanner"; nocase; sid:1000010; rev:1;)
```

Recarga y ejecuta:

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml       # valida config
sudo suricata -i eth0 -l /var/log/suricata/ &
# genera el tráfico que la dispara:
curl -A "evilscanner" http://192.168.56.101/admin
sudo tail -n1 /var/log/suricata/fast.log
jq 'select(.event_type=="alert" and .alert.signature_id==1000010)' /var/log/suricata/eve.json
```

Evidencia que cumple el criterio: `fast.log` contiene la línea con el `msg` exacto, `eve.json` tiene el objeto de alerta con `signature_id: 1000010`, y una petición legítima (`curl http://192.168.56.101/admin` sin ese user-agent) **no** dispara la regla (bajo falso positivo).

### Claves de los ejercicios

1. Puerto de administración: `alert tcp any any -> $HOME_NET 3389 (msg:"Intento de conexion RDP"; flow:to_server; sid:1000020; rev:1;)`.
2. PCRE en URL: `alert http any any -> any any (msg:"Patron en URL"; http.uri; pcre:"/\/(admin|config)\.php/i"; sid:1000021; rev:1;)`.
3. `flowbits`: una regla marca `flowbits:set,paso1; flowbits:noalert;` y otra dispara con `flowbits:isset,paso1;`, correlacionando dos eventos de la misma sesión.
4. Consultas DNS con jq: `jq 'select(.event_type=="dns") | .dns.rrname' eve.json | sort | uniq -c`.
5. `threshold` para limitar ruido: `threshold:type limit, track by_src, count 1, seconds 60;` dentro de la regla (o en `threshold.config`).
6. Rendimiento: `suricata -r cap.pcap` (multihilo) vs `snort -r cap.pcap`; compara paquetes/segundo en las estadísticas finales de cada uno.

---

## Clase 036 — VPN y túneles: IPsec, WireGuard y OpenVPN

### Solución del reto verificable

Objetivo: túnel funcional (WireGuard) entre dos VMs en subredes distintas, alcanzables por IP interna, con evidencia de cifrado y claves `600`.

```bash
# en cada peer:
wg genkey | tee privada.key | wg pubkey > publica.key
chmod 600 privada.key
```

Servidor `/etc/wireguard/wg0.conf`:

```ini
[Interface]
Address = 10.10.0.1/24
ListenPort = 51820
PrivateKey = <privada-servidor>

[Peer]
PublicKey = <publica-cliente>
AllowedIPs = 10.10.0.2/32
```

Levanta y verifica cifrado:

```bash
sudo wg-quick up wg0
sudo wg show                       # handshake reciente + bytes rx/tx
ping -c3 10.10.0.1                  # desde el cliente
sudo tcpdump -i eth0 -n udp port 51820   # solo UDP cifrado, NO el ICMP en claro
```

Evidencia que cumple el criterio: el `ping` entre IPs internas responde; en `eth0` la captura solo muestra UDP/51820 con payload opaco (no aparece el ICMP interno en claro); `ls -l privada.key` da `-rw-------` y las claves privadas nunca se incluyen en la entrega.

### Claves de los ejercicios

1. tcpdump en la interfaz física muestra el tráfico como UDP cifrado; en `wg0` (interfaz del túnel) verías el ICMP en claro → demuestra que el cifrado ocurre en el encapsulado.
2. Split tunnel: en el cliente pon `AllowedIPs = 10.10.0.0/24` (solo esa subred cruza la VPN); el resto sale por la ruta normal.
3. Revocar cert OpenVPN: `./easyrsa revoke cliente1 ; ./easyrsa gen-crl`, referencia la CRL en `server.conf` (`crl-verify crl.pem`); el cliente revocado ya no completa el TLS.
4. WireGuard: config de pocas líneas y handshake de 1-RTT (Noise); OpenVPN: config extensa, PKI/TLS y handshake de varios mensajes.
5. Fases IKE en Wireshark: filtra `isakmp`; verás IKE_SA_INIT (negociación de claves DH) e IKE_AUTH (autenticación), tras lo cual ESP cifra la carga.
6. Firewall solo VPN: `-A INPUT -p udp --dport 51820 -j ACCEPT` y DROP del resto (integración con clase 034).

---

## Clase 037 — Proxies, NAT y pivoting de red

### Solución del reto verificable

Objetivo: desde un pivote con dos interfaces, tunelizar para escanear/acceder a un servicio interno no alcanzable directamente, con explicación del recorrido del paquete.

```bash
# 1) túnel SOCKS dinámico a través del pivote:
ssh -D 1080 usuario@pivote
# 2) proxychains apuntando a 127.0.0.1:1080 (socks5 en /etc/proxychains4.conf)
# 3) escaneo de la red interna a través del túnel (TCP connect, sin raw):
proxychains4 nmap -sT -Pn -p 22,80,445 10.20.0.0/24
proxychains4 curl http://10.20.0.5/
```

Recorrido del paquete: tu herramienta → proxy SOCKS local `127.0.0.1:1080` → sesión SSH cifrada → el `sshd` del pivote abre la conexión hacia `10.20.0.5` por su segunda interfaz → respuesta por el mismo camino inverso.

Evidencia que cumple el criterio: `curl http://10.20.0.5/` responde solo a través del túnel (falla sin él), `proxychains4 nmap` lista puertos de la red interna, y la explicación del recorrido es correcta.

### Claves de los ejercicios

1. `-L`: `ssh -L 8080:10.20.0.5:80 usuario@pivote` y luego `curl http://127.0.0.1:8080/`.
2. `-D 1080` + `proxychains4 nmap -sT -Pn 10.20.0.0/24`.
3. Con SOCKS conviene `-sT` porque el proxy solo tuneliza conexiones TCP completas (`connect()`); `-sS` necesita raw sockets que no atraviesan SOCKS.
4. `-R` legítimo: exponer temporalmente un servicio de tu equipo hacia el pivote para que un admin acceda a una demo interna sin abrir puertos en el firewall perimetral.
5. Chisel con solo salida HTTP: `chisel server -p 8000 --reverse` en el pivote y `chisel client PIVOTE:8000 R:socks` en el atacante; el túnel viaja sobre HTTP/WebSocket, atravesando el egress permitido.
6. Detección azul: alerta sobre conexiones SSH salientes de larga duración con mucho tráfico bidireccional, o SOCKS local + patrones de escaneo interno (regla IDS por volumen/beaconing).

---

## Clase 038 — Seguridad WiFi: WPA2, WPA3 y superficie de ataque

### Solución del reto verificable

Objetivo: sobre **tu propia** red con passphrase débil, capturar handshake/PMKID, crackear offline y luego demostrar que WPA3 (o WPA2 fuerte + PMF) frustra el mismo ataque.

Fase vulnerable (WPA2 + passphrase débil, p. ej. `password1`):

```bash
sudo airmon-ng check kill
sudo airmon-ng start wlan0
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w captura wlan0mon &
sudo aireplay-ng --deauth 3 -a AA:BB:CC:DD:EE:FF wlan0mon   # sobre TU red
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b AA:BB:CC:DD:EE:FF captura-01.cap
# => KEY FOUND! [ password1 ]
```

Fase endurecida: reconfigura el AP con **WPA3-SAE** (o WPA2 con passphrase aleatoria de 15+ caracteres y PMF obligatorio) y repite; el diccionario ya no recupera la clave.

Evidencia que cumple el criterio: en la fase 1 `aircrack-ng`/`hashcat` devuelve la passphrase débil; en la fase 2 el ataque agota el diccionario sin resultado. Todo sobre red propia.

### Claves de los ejercicios

1. En airodump: columna BSSID (MAC del AP), CH (canal), ENC/CIPHER/AUTH (WPA2/CCMP/PSK) y, abajo, los STATION (clientes) asociados.
2. Validar handshake sin crackear: `aircrack-ng captura-01.cap` muestra "1 handshake" si la captura es válida (sin lanzar diccionario).
3. Una passphrase débil (en `rockyou.txt`) cae en segundos/minutos; una de 15+ caracteres aleatorios es inviable por diccionario y por fuerza bruta.
4. WPA3-SAE (Dragonfly) exige interactuar con el AP en cada intento (no hay handshake capturable atacable offline), eliminando el crackeo por diccionario.
5. PMF (802.11w) firma/protege las tramas de gestión, así que las tramas de deauth falsas se rechazan y no se puede forzar la desconexión.
6. Evil twin: dos BSSID distintos anunciando el mismo SSID, señal anómala o cambios de BSSID; detéctalo comparando BSSID esperado, potencia y capabilities.

---

## Clase 039 — Ataques de capa 2: ARP spoofing y VLAN hopping

### Solución del reto verificable

Objetivo: posicionarte como MitM entre dos VMs por ARP spoofing, demostrar intercepción en claro y luego neutralizarlo con una contramedida.

Fase de ataque:

```bash
sudo sysctl -w net.ipv4.ip_forward=1
sudo bettercap -iface eth0
# dentro de bettercap:
set arp.spoof.targets 192.168.56.10, 192.168.56.1
arp.spoof on
net.sniff on
```

En la víctima, `arp -a` muestra la MAC del gateway sustituida por la del atacante; capturas su tráfico HTTP en claro.

Contramedida (entrada ARP estática en la víctima, o DAI en el switch):

```bash
# en la víctima:
sudo arp -s 192.168.56.1 <MAC-real-del-gateway>
```

Evidencia que cumple el criterio: en la fase de ataque interceptas tráfico entre las VMs; tras fijar el ARP estático (o activar DAI), la tabla ARP ya no se envenena y dejas de ver su tráfico.

### Claves de los ejercicios

1. Con `ip_forward=1` y `arp.spoof on`, el tráfico HTTP de la víctima pasa por ti; `net.sniff on`/Wireshark lo muestra en claro (solo laboratorio).
2. Firma en Wireshark: respuestas ARP (`is-at`) no solicitadas y `arp.duplicate-address-detected` (una IP con dos MAC).
3. MAC flooding: al desbordar la tabla CAM, el switch entra en fail-open y difunde todas las tramas por todos los puertos, comportándose como un hub → puedes esnifar tráfico ajeno.
4. Double tagging: el atacante inserta dos etiquetas 802.1Q; el primer switch quita la externa (native VLAN) y reenvía por el trunk con la interna intacta, entregándola a la VLAN víctima. Es **unidireccional** porque no hay ruta de retorno etiquetada.
5. `switchport port-security maximum 1` + `violation shutdown`: al inyectar muchas MAC, `macof` dispara la violación y el puerto se apaga/bloquea.
6. DAI valida cada ARP contra la tabla de DHCP snooping (IP↔MAC↔puerto aprendida por DHCP); si el par no coincide, descarta el ARP falso.

---

## Clase 040 — Man-in-the-Middle: técnicas y defensa

### Solución del reto verificable

Objetivo: MitM contra dos versiones de tu sitio (HTTP sin HSTS vs HTTPS con HSTS); interceptar la primera y resistir en la segunda.

```bash
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
mitmproxy --mode transparent --listen-port 8080
```

- Versión vulnerable (HTTP/sin HSTS): mitmproxy ve y modifica las peticiones; SSL stripping mantiene la conexión en HTTP.
- Versión endurecida (HTTPS + HSTS): el navegador, con la política HSTS memorizada, **exige** HTTPS y rechaza el downgrade; el MitM sin CA de confianza no puede leer el contenido.

Configura y verifica HSTS:

```bash
curl -I https://mi-sitio.lab/    # Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

Evidencia que cumple el criterio: interceptación/modificación exitosa en la versión vulnerable y fallo del ataque en la endurecida, explicando que **HSTS impide el downgrade** y **TLS válido impide leer el contenido**.

### Claves de los ejercicios

1. Modificar respuesta HTTP: en mitmproxy usa un script/`~s` para reescribir el cuerpo (p. ej. cambiar un texto) y observa el cambio en la víctima.
2. Stripping: en el sitio sin HSTS la barra cae a `http://`; en el que tiene HSTS el navegador fuerza `https://` desde el inicio y el stripping no ocurre.
3. Pinning: la app solo confía en un certificado/clave concretos, así que aunque el atacante presente un certificado "válido" firmado por otra CA, la app lo rechaza.
4. Indicadores de MitM: cambio de la MAC del gateway, advertencias de certificado inesperadas, degradación a HTTP en sitios que deberían ser HTTPS, CAs emisoras desconocidas.
5. HSTS con preload: cabecera `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`; verifica con `curl -I`.
6. Una VPN cifra todo el tráfico entre tu equipo y el endpoint VPN, así que en el WiFi público el atacante local no puede posicionarse en medio del tráfico útil.

---

## Clase 041 — Seguridad de DNS: envenenamiento, DNSSEC y tunneling

### Solución del reto verificable

Objetivo: resolver validante que rechaza una respuesta falsificada que uno sin validación aceptaría, más un método reproducible para detectar DNS tunneling.

Parte DNSSEC:

```bash
# resolver validante (unbound con auto-trust-anchor-file):
dig +dnssec @127.0.0.1 dominio-firmado.lab
delv @127.0.0.1 dominio-firmado.lab      # "fully validated"
# respuesta manipulada => el validante la marca SERVFAIL/bogus; el no validante la sirve
```

Parte detección de tunneling:

```bash
tshark -r dns.pcapng -Y 'dns.flags.response==0' -T fields -e dns.qry.name \
  | awk '{ print length, $0 }' | sort -rn | head
```

Los nombres muy largos, con alta entropía y consultas TXT/NULL frecuentes al mismo dominio delatan el túnel (iodine/dnscat2).

Evidencia que cumple el criterio: el resolver validante devuelve bogus/SERVFAIL ante la respuesta manipulada mientras el no validante la acepta; el método señala el tráfico de túnel frente al DNS legítimo por longitud/entropía.

### Claves de los ejercicios

1. `dig +dnssec dominio-firmado` incluye registros `RRSIG` junto a cada RRset y activa el flag `ad` (authenticated data); un dominio sin firmar no trae RRSIG.
2. DNSSEC firma (integridad/autenticidad) pero no cifra; la confidencialidad la aportan **DoT** (853/tcp) o **DoH** (443/https).
3. Kaminsky: el atacante inunda con respuestas falsas adivinando el TXID (16 bits) para subdominios inexistentes antes de que llegue la real. Mitigaciones: **aleatorización del puerto de origen** (añade entropía) y **DNSSEC** (firma las respuestas).
4. Longitud media: `... -e dns.qry.name | awk '{s+=length;n++} END{print s/n}'`; un valor muy alto frente a la línea base sugiere túnel.
5. DoH en el navegador: activa "DNS seguro"; en Wireshark las consultas ya no aparecen como `dns` en claro, sino dentro de TLS hacia el resolver (443).
6. Zeek `dns.log`: campos `query`, `qtype_name`, `answers`, `rejected`; nombres largos, muchos `TXT`/`NULL` y volumen a un mismo dominio ayudan a detectar tunneling.

---

## Clase 042 — Segmentación de red y arquitectura Zero Trust

### Solución del reto verificable

Objetivo: diseñar una red segmentada (≥5 zonas) con diagrama, matriz de flujos de mínimo privilegio y mapeo Zero Trust, con al menos tres reglas traducidas a firewall.

Zonas: **DMZ** (web), **App**, **Datos**, **Administración** (bastión), **Usuarios**, **Dispositivos no confiables** (IoT/impresoras).

Matriz de flujos permitidos (mínimo privilegio):

| Origen | Destino | Puerto | ¿Permitido? |
|--------|---------|--------|-------------|
| Usuarios | Web (DMZ) | 443 | Sí |
| Web (DMZ) | App | 8080 | Sí |
| App | Datos | 5432 | Sí |
| Usuarios | Datos | 5432 | No |
| Cualquiera | Administración | 22 | Solo desde bastión con MFA |
| IoT | Cualquier interna | — | No (deny por defecto) |

Tres reglas traducidas (nftables):

```bash
sudo nft add rule inet zt forward ip saddr $USUARIOS ip daddr $WEB tcp dport 443 accept
sudo nft add rule inet zt forward ip saddr $WEB     ip daddr $APP tcp dport 8080 accept
sudo nft add rule inet zt forward ip saddr $APP     ip daddr $DATOS tcp dport 5432 accept
# política: sudo nft add chain inet zt forward '{ type filter hook forward priority 0; policy drop; }'
```

Zero Trust: el **PEP** es el firewall/gateway entre zonas; el **PDP** decide con identidad + postura del dispositivo + MFA; el acceso a Datos y Administración se re-evalúa continuamente.

Evidencia que cumple el criterio: la matriz no tiene flujos innecesarios (mínimo privilegio verificable), Datos y Administración están estrictamente controlados y el diseño aborda ≥5 de los 7 principios de NIST SP 800-207.

### Claves de los ejercicios

1. La BD nunca debe ser accesible desde Usuarios porque una estación comprometida daría acceso directo a los datos; solo la capa App (con su lógica y autenticación) debe hablar con Datos.
2. DMZ: el servidor web se ubica en una zona intermedia entre Internet y la red interna; solo expone 443 hacia fuera y solo 8080 hacia App, nunca acceso directo Internet→interna.
3. Traducir tres flujos: ver las reglas nftables de arriba (443, 8080, 5432).
4. VLAN separa dominios de difusión a nivel de red; microsegmentación aplica políticas por carga de trabajo/host (firewall de host o hipervisor), mucho más granular.
5. Señales Zero Trust: identidad autenticada (MFA), postura del dispositivo (parcheado, gestionado), ubicación/hora, sensibilidad del recurso y comportamiento.
6. Brecha típica: falta de verificación continua o de cifrado interno entre zonas; ciérrala con reautenticación por sesión, mTLS entre servicios y monitoreo (clases 043–045).

---

## Clase 043 — Network Security Monitoring (NSM): fundamentos

### Solución del reto verificable

Objetivo: "expediente" NSM de un evento (escaneo + descarga anómala) que enlace alerta → logs de sesión/transacción → full content, con conclusión fundamentada.

Pasos:

```bash
sudo so-import-pcap /ruta/incidente.pcapng
```

1. **Alerta**: en la consola de Security Onion (Alerts), identifica la firma de Suricata que disparó (p. ej. escaneo o user-agent sospechoso) y anota su `uid`/flujo.
2. **Sesión/transacción**: pivota a los logs de Zeek asociados: `conn.log` (5-tupla, bytes, duración), `http.log` (host/URI/status), `dns.log` (consultas).
3. **Full content**: desde la alerta, extrae el pcap del flujo y ábrelo en Wireshark para el análisis fino de la descarga anómala.
4. **Conclusión**: correlaciona los tres niveles; si el mismo `uid`/5-tupla aparece en alerta + conn.log + http.log y la descarga es un binario inesperado, es **incidente**; si es tráfico legítimo mal clasificado, **falso positivo**.

Evidencia que cumple el criterio: el expediente enlaza alerta → logs → full content del **mismo** flujo (mismo `uid`/5-tupla) y la conclusión se apoya en esa evidencia.

### Claves de los ejercicios

1. Clasificación NSM: pcap del flujo → full content; `conn.log` → sesión; `http.log`/`dns.log` → transacción; alerta de Suricata → alert data; contadores/bytes → estadísticos.
2. Sensor entre DMZ e interna: colócalo en el TAP/SPAN del enlace que une ambas zonas, para ver todo el tráfico que las cruza.
3. Reconstruir sesión: toma el `uid` de la alerta y búscalo en `conn.log`, `http.log`, `files.log` para el relato completo.
4. Hipótesis de hunting: (a) beaconing → `conn.log` por regularidad temporal; (b) exfiltración → `conn.log` por `orig_bytes` altos; (c) dominios raros → `dns.log` por entropía/longitud.
5. Compromiso: el full content da máxima fidelidad pero ocupa muchísimo; se retiene poco tiempo y se prioriza guardar sesión/flujo (barato) para el histórico.
6. Métricas NSM: MTTD (tiempo medio de detección), MTTR (de respuesta), % de alertas triadas, cobertura de sensores.

---

## Clase 044 — Zeek para análisis de red a gran escala

### Solución del reto verificable

Objetivo: procesar una captura con Zeek y entregar (a) top de conexiones por bytes, (b) un archivo extraído con su hash y (c) un script `.zeek` propio que emita un notice.

```bash
mkdir zeek-out && cd zeek-out
zeek -r /tmp/lab027.pcapng
# (a) top por bytes:
cat conn.log | zeek-cut id.orig_h id.resp_h resp_bytes | sort -k3 -rn | head
# (b) extracción de archivos + hash:
zeek -r /tmp/lab027.pcapng /opt/zeek/share/zeek/policy/frameworks/files/extract-all-files.zeek
sha256sum extract_files/*
```

Script `deteccion.zeek` (detección por user-agent, usando el evento de cabecera para acceder al valor con fiabilidad):

```zeek
@load base/protocols/http

event http_header(c: connection, is_orig: bool, name: string, value: string) {
    if ( is_orig && name == "USER-AGENT" && /sqlmap|nikto|[Nn]map/ in value )
        NOTICE([$note=Weird::Activity,
                $msg="User-Agent de herramienta ofensiva detectado",
                $conn=c]);
}
```

```bash
zeek -r /tmp/lab027.pcapng ./deteccion.zeek
cat notice.log | zeek-cut msg
```

Evidencia que cumple el criterio: los logs se generan, el `sha256sum` del archivo extraído coincide con el transferido, y el script produce el notice esperado sin falsos positivos sobre tráfico legítimo.

> Nota técnica: en el `http_request` los headers aún no se han parseado, por lo que conviene detectar el user-agent en el evento `http_header` (como arriba) en vez de leer `c$http$user_agent` en `http_request`.

### Claves de los ejercicios

1. Top 10 por bytes: `cat conn.log | zeek-cut id.orig_h id.resp_h orig_bytes resp_bytes | sort -k4 -rn | head`.
2. Certificados sospechosos: `cat ssl.log | zeek-cut server_name validation_status subject | grep -i 'self.signed\|unable'`.
3. Extraer y verificar: usa `extract-all-files.zeek`, luego `sha256sum extract_files/<archivo>` y compáralo con el original.
4. Notice por volumen: en `connection_state_remove` comprueba `c$conn$orig_bytes > umbral` y emite `NOTICE` (posible exfiltración).
5. Beaconing: correlaciona `conn.log`/`dns.log` agrupando por `id.resp_h`/`query` y midiendo la regularidad de los intervalos `ts` (conexiones periódicas ≈ mismo delta).
6. Zeek aporta contexto de transacción (qué host, qué URI, qué certificado); Suricata aporta la coincidencia de firma. Zeek explica el "qué pasó"; Suricata señala el "esto es malicioso".

---

## Clase 045 — NetFlow y análisis de metadatos de tráfico

### Solución del reto verificable

Objetivo: generar flujos con tráfico normal + una anomalía (escaneo o transferencia grande) y detectarla **solo** con metadatos.

```bash
# genera y recolecta flujos:
sudo softflowd -i eth0 -n 127.0.0.1:9995
nfcapd -w -D -l /tmp/flows -p 9995
# introduce la anomalía (escaneo):
sudo nmap -sS -p- 192.168.56.101
```

Detección del escaneo (una IP tocando muchos destinos/puertos con pocos paquetes):

```bash
nfdump -R /tmp/flows 'proto tcp and packets < 3' -s srcip/flows -n 10
```

Detección de exfiltración (flujos salientes con muchos bytes hacia externos):

```bash
nfdump -R /tmp/flows 'src net 192.168.56.0/24 and bytes > 10000000' -s dstip/bytes
```

Caracterización: la IP con miles de flujos de pocos paquetes = **escaneo horizontal/vertical**; la IP con un flujo saliente enorme a un destino externo = **posible exfiltración**.

Evidencia que cumple el criterio: identificas la actividad anómala a partir de los flujos (no del contenido), la caracterizas correctamente y aportas la consulta nfdump que la evidencia, coincidiendo con lo que introdujiste.

### Claves de los ejercicios

1. Cinco pares top: `nfdump -R /tmp/flows -s record/bytes -n 5` (o `-s ip/bytes`).
2. Escaneo horizontal: una IP origen con muchísimos `flows` hacia muchas IP destino y pocos paquetes/bytes por flujo → `-s srcip/flows` lo destaca.
3. DDoS volumétrico: multitud de IP origen convergiendo en una IP/puerto destino con enorme volumen agregado de flujos/bytes en poco tiempo.
4. Beaconing: flujos periódicos y de tamaño similar hacia el mismo destino; la **regularidad temporal** delata un canal automatizado (C2) aunque el contenido esté cifrado.
5. Ahorro: un registro de flujo son decenas de bytes por conexión frente a los KB/MB del pcap equivalente; el ahorro es de varios órdenes de magnitud, ideal para retención histórica.
6. Campos para SIEM: 5-tupla, bytes/paquetes, marcas de tiempo, flags TCP y duración; permiten alertas de escaneo, volumen anómalo y periodicidad (beaconing).
