# 🧪 Plataformas de práctica y CTF

Esta guía conecta la teoría del programa con entornos externos **deliberadamente
autorizados**. Una plataforma no reemplaza una clase ni convierte una flag en
competencia profesional: sirve para practicar una hipótesis, conservar evidencia,
explicar la causa raíz y proponer prevención y detección.

> Practica únicamente en el objetivo y durante el alcance que la plataforma
> autoriza. Sus planes, catálogos y reglas cambian; comprueba siempre el sitio
> oficial antes de comenzar o publicar un writeup.

## Flujo de aprendizaje transversal

`Teoría → laboratorio guiado → reto interno → plataforma autorizada → flag y
evidencia → writeup reproducible → causa raíz → mitigación → detección → lecciones`.

La flag solo confirma una condición del reto. El aprendizaje aparece cuando el
writeup permite reconstruir qué observaste, por qué funcionó, qué alternativa
descartaste y qué control habría prevenido o detectado el problema. Usa la
[plantilla común](../templates/writeup-ctf.md) y relaciona el resultado con el
[glosario global](GLOSARIO-GLOBAL.md).

## Matriz de plataformas

| Plataforma | Enfoque principal | Modalidad | Nivel útil | Ruta o parte relacionada | Uso recomendado | Límite importante |
|---|---|---|---|---|---|---|
| [Hack The Box Labs](https://www.hackthebox.com/hacker/hacking-labs) | Máquinas y escenarios ofensivos | Mixta: contenido gratuito y planes de pago | Intermedio–avanzado | [Pentester](../rutas/pentester.md), [Red Team](../rutas/red-team.md), partes 3–7 | Consolidar enumeración, explotación y reporte después de los labs locales | La [AUP](https://www.hackthebox.com/legal/aup) permite publicar soluciones solo para contenido retirado; no difundas flags ni soluciones activas |
| [HTB Academy](https://academy.hackthebox.com/) | Cursos modulares y rutas con Pwnbox | Mixta; módulos Tier 0 gratuitos y planes de pago | Inicial–avanzado | Pentesting, SOC, AppSec y DFIR | Cubrir prerrequisitos y repetir técnicas en módulos guiados | No asumir que una suscripción o módulo sigue igual: comprobar el catálogo vigente |
| [TryHackMe](https://tryhackme.com/) | Rutas, salas guiadas y salas de desafío | Mixta: plan gratuito y planes de pago | Inicial–intermedio | Fundamentos, [SOC](../rutas/soc-blue-team.md), pentesting y cloud | Empezar con walkthroughs; después repetir en una sala de desafío sin pistas | Separar la guía de la evidencia propia; no copiar respuestas como si fueran razonamiento |
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) | Seguridad web con teoría y laboratorios interactivos | Gratuita | Inicial–avanzado | [AppSec](../rutas/appsec.md), pentesting, parte 4 | Practicar una vulnerabilidad web inmediatamente después de su clase | Los labs autorizan ese entorno, no ataques a sitios públicos |
| [CyLab Security Academy](https://cylabacademy.org/) — antes picoCTF | Fundamentos y desafíos Jeopardy | Gratuita | Inicial–intermedio | Fundamentos, cripto, web, forense y reversing | Primera experiencia CTF y trabajo por categorías; la transición conserva cuentas y progreso de picoCTF | Distinguir contenido educativo de eventos con reglas y ventanas propias |
| [CyberDefenders](https://cyberdefenders.org/) | Investigaciones SOC, forense y DFIR | Acceso sujeto al plan vigente | Intermedio | SOC, [DFIR](../rutas/dfir.md), partes 8–9 | Producir timeline, hipótesis, IOC y recomendación defensiva | Una respuesta correcta sin cadena de evidencia no equivale a un informe de incidente |
| [OverTheWire](https://overthewire.org/wargames/) | Wargames de terminal, web, cripto y explotación | Gratuita | Inicial–intermedio | Fundamentos, web, cripto y pwn | Seguir la progresión oficial Bandit → Natas/Krypton/Leviathan → niveles posteriores | Las credenciales de nivel son flags: no publicarlas |
| [PentesterLab](https://pentesterlab.com/) | Seguridad web y revisión de código | Principalmente de pago, con ejercicios accesibles sin PRO | Intermedio–avanzado | AppSec y pentesting | Explicar no solo el exploit, sino la línea de código y la corrección | Confirmar que el ejercicio elegido está incluido en el plan disponible |
| [LetsDefend](https://letsdefend.io/) | SOC simulado e investigaciones defensivas | Mixta: Basic gratuito y planes de pago | Inicial–intermedio | SOC y DFIR | Practicar triage, escalado, consultas y cierre de alertas | No confundir la simulación con acceso autorizado a infraestructura real |
| [CTFtime](https://ctftime.org/) | Directorio de eventos, equipos, resultados y writeups | Gratuita | Todos | Todas las rutas, según evento | Descubrir un evento adecuado y estudiar writeups una vez permitido | No es una ruta guiada; cada evento define sus reglas y política de publicación |
| [pwn.college](https://pwn.college/) | Fundamentos de sistemas, pwn y seguridad práctica | Gratuita | Inicial–avanzado | Fundamentos, pwn, reversing | Aprender por módulos y conservar notas privadas de resolución | Sus [reglas](https://pwn.college/rules/) piden no publicar walkthroughs ni soluciones de desafíos |
| [ROP Emporium](https://ropemporium.com/) | Return-oriented programming | Gratuita | Intermedio–avanzado | Parte 5, pentesting avanzado | Progresar desde `ret2win` y justificar cada gadget y restricción | Trabajar solo sobre los binarios de práctica proporcionados |
| [VulnHub](https://www.vulnhub.com/) | Máquinas virtuales vulnerables descargables | Gratuita | Intermedio | Pentesting, Red Team, forense | Montar una red local aislada y practicar el ciclo completo | La antigüedad y mantenimiento varían; aislar la VM y no puentearla a redes sensibles |
| [crackmes.one](https://crackmes.one/) | Crackmes para ingeniería inversa | Gratuita con cuenta | Inicial–avanzado | Reversing, malware, Game Security | Comparar análisis estático y dinámico sobre binarios hechos para ser analizados | Tratar descargas como código no confiable: sandbox, hashes y aislamiento |

## Progresión recomendada

### Si partes desde cero

1. Completa fundamentos y el laboratorio local de la clase.
2. Practica terminal en OverTheWire Bandit o una ruta inicial de TryHackMe.
3. Resuelve un reto interno en [`ctf/`](../ctf/README.md) sin abrir su solución.
4. Usa CyLab Security Academy para probar varias categorías y redacta un writeup.

### Si buscas ofensiva o AppSec

1. Web Security Academy para aislar una vulnerabilidad y su defensa.
2. HTB Academy o PentesterLab para unir técnica, revisión y reporte.
3. HTB Labs o una VM aislada de VulnHub para recorrer el ciclo completo.
4. ROP Emporium, pwn.college o crackmes.one para pwn/reversing, respetando sus reglas.

### Si buscas SOC o DFIR

1. Completa los labs internos de telemetría, triage y timeline.
2. Usa TryHackMe o LetsDefend para practicar decisiones de analista.
3. Usa CyberDefenders para una investigación más abierta.
4. Entrega IOC, consultas de detección, causa raíz y acciones; no solo respuestas.

## Criterio para elegir una actividad

Antes de empezar, registra: objetivo de aprendizaje, alcance autorizado, costo o
plan disponible, prerequisitos, tiempo límite, política de writeups y evidencia
que producirás. Después, comprueba que puedes explicar el mecanismo sin depender
de la flag. Si no puedes, vuelve a la clase o al laboratorio anterior.

## Fuentes verificadas

- Hack The Box documenta [Labs](https://www.hackthebox.com/hacker/hacking-labs), [Academy](https://academy.hackthebox.com/) y su [política de uso aceptable](https://www.hackthebox.com/legal/aup).
- TryHackMe describe sus [tipos de salas y rutas](https://help.tryhackme.com/en/articles/6496029-getting-started) y los [planes disponibles](https://tryhackme.com/pricing).
- PortSwigger mantiene la [Web Security Academy](https://portswigger.net/web-security) como recurso gratuito con laboratorios interactivos.
- Carnegie Mellon anunció la evolución de picoCTF a [CyLab Security Academy](https://www.cylab.cmu.edu/news/2025/12/02-cylab-security-academy.html).
- Las demás filas enlazan directamente al sitio o a las reglas oficiales de cada plataforma.

**Verificación editorial:** 22 de septiembre de 2026. Los enlaces respaldan el
tipo de plataforma y sus límites; las recomendaciones de secuencia son decisiones
pedagógicas de este programa.
