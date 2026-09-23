# Seguridad, autorización y ética

Este repositorio enseña capacidades de doble uso. Una licencia de copyright permite copiar o modificar material; nunca concede permiso para acceder, analizar, interceptar, alterar o probar un sistema de terceros.

## Contextos permitidos

### Aprendizaje

Puedes estudiar el material y ejecutar ejemplos inofensivos localmente. Cuando una técnica interactúe con una red, cuenta, dispositivo o servicio, usa un objetivo creado para practicar o que controles legítimamente.

### Laboratorio autorizado

Usa los laboratorios incluidos, CTFs, cyber ranges y máquinas propias aisladas. Define límites de red, datos, tiempo y persistencia. Restablece el entorno al terminar y no conectes servicios vulnerables a Internet.

### Investigación

La investigación debe respetar la ley, los contratos, los términos del proveedor, la privacidad y las reglas del programa de divulgación. Recolecta la evidencia mínima, protege los datos obtenidos y coordina la comunicación con el responsable del sistema.

### Pruebas defensivas

El análisis, la detección, el hardening, la respuesta a incidentes y la validación de controles requieren autoridad sobre los activos y datos. Conserva aprobación escrita, reglas de enfrentamiento, contactos, ventanas, exclusiones, criterios de parada y plan de recuperación.

## Sistemas de terceros sin autorización

No uses el material para escanear, explotar, persistir, evadir controles, obtener credenciales, interceptar comunicaciones, desplegar payloads, alterar datos o degradar servicios de terceros sin autorización explícita. Que un servicio sea accesible desde Internet, tenga una vulnerabilidad conocida o aparezca en un buscador no constituye permiso.

Si descubres accidentalmente una vulnerabilidad, detén la prueba, evita ampliar el acceso, conserva solo la evidencia mínima y usa el canal de divulgación coordinada del propietario o su programa autorizado. No publiques secretos, datos personales ni instrucciones explotables antes de la corrección acordada.

## Contenido sensible del repositorio

- Los ejemplos de código vulnerable y los retos están diseñados para entornos desechables.
- El repositorio no versiona malware real, ejecutables, volcados de memoria, capturas de paquetes ni credenciales.
- Los datasets incluidos son ficticios o sintéticos y se documentan en [DATA_LICENSES.md](DATA_LICENSES.md).
- Las herramientas externas se descargan o ejecutan bajo sus propias licencias y controles; consulta [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Antes de una práctica profesional, documenta al menos: propietario que autoriza, activos incluidos, técnicas permitidas, datos autorizados, horario, contactos, restricciones, evidencia que se conservará y condición de cierre. La [Clase 025](classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md) desarrolla este proceso.

## Game Security, anti-cheat y telemetría de jugadores

Las clases 341–360 permiten instrumentar y modificar únicamente el
[Game Security Range](labs/game-security/README.md), software propio o un target interno cubierto por
autorización escrita. No conectes trainers, automatizaciones, proxies, depuradores o pruebas de
memoria del curso a juegos de terceros y no desarrolles bypasses contra sus controles.

Una alerta, anomalía, score o coincidencia técnica inicia una investigación; no demuestra por sí
sola identidad, intención ni culpabilidad. La práctica debe separar ingeniería de la señal,
investigación, decisión de sanción y apelación. Para telemetría, documenta finalidad, minimización,
acceso, retención y borrado; prueba falsos positivos en segmentos legítimos y accesibilidad.

El [modelo operativo de Game Security](docs/modelo-operativo-game-security.md) define los roles,
evidencias y límites, y la [Clase 359](classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/359-privacidad-gobernanza-sanciones-seguridad-anticheat/README.md)
desarrolla privacidad, gobernanza y seguridad del propio anti-cheat.

## CaaS, inteligencia y pruebas de disponibilidad

No contrates, registres cuentas, pruebes ni interactúes con servicios criminales, booter/stresser,
mercados, botnets o infraestructura sospechosa para completar el programa. La investigación se
limita a fuentes oficiales y públicas, expedientes, feeds autorizados y telemetría de activos bajo
tu control. No compres «muestras», accesos o datos robados.

Una prueba de carga necesita autorización escrita del propietario, rangos y endpoints exactos,
límites de tasa, ventana, observabilidad, contactos, criterio de parada y coordinación con
ISP/CDN/CSP cuando corresponda. El laboratorio DDoS incluido sólo analiza telemetría sintética y no
genera tráfico. La sección de [responsabilidades CaaS](docs/cybercrime-as-a-service.md#modelo-operativo-y-responsabilidades-por-rol)
define qué corresponde a CTI, SOC, SecOps, infraestructura, DFIR, CISO y legal.

Para reportar fallos del propio proyecto, consulta [SECURITY.md](SECURITY.md). Este documento expresa las condiciones éticas del programa; no sustituye asesoría jurídica aplicable al país, contrato o sector de quien practica.
