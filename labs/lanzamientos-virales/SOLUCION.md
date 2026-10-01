# Solución docente — caso OrbitPup

## Reconstrucción mínima

El video `evt-001` aporta el gancho, no autenticidad. `evt-002` y `evt-006` muestran que la landing no
es el dominio de referencia y anuncia otro `asset_id` bajo el mismo símbolo. `evt-003` es suplantación
por cuenta imitadora. `evt-004`–`evt-005` sostienen una toma probable de la cuenta real porque la
publicación ocurre durante una sesión nueva y geográficamente anómala; no identifican al operador.

`evt-007` crea una sesión sin cambio de estado. El punto decisivo es `evt-008`: la etiqueta visible
promete reclamar PUP, pero la acción decodificada concede gasto ilimitado de otro activo a
`0xdddd…`. En `evt-009` ese mismo spender ejecuta el movimiento. Esa correlación sostiene la ruta del
drainer sin atribuir identidad humana. `evt-006` también solicita una frase semilla, pero el dataset no
demuestra que se enviara; queda como intento de una segunda ruta.

`evt-010` prueba que un proceso sustituyó una dirección del portapapeles. Es un incidente de endpoint
que amplía el alcance y requiere contención, aunque no explica el gasto delegado ya trazado.

`LV-002` no pertenece a la misma campaña. El activo fue verificado, pero el promotor controlaba los LP
tokens, el supuesto lock no fue corroborado y casi toda la liquidez fue retirada. Es el escenario de
rug pull del ejercicio; no un token falso ni un drainer.

## Controles que rompen la cadena

| Punto | Control | Prueba |
|---|---|---|
| video/cuenta | corroborar desde dos canales independientes y MFA resistente a phishing | cuenta tomada no puede cambiar ambos canales |
| búsqueda/dominio | navegación desde marcador o dominio publicado oficialmente | el lookalike no aparece en el recorrido aprobado |
| token | allowlist por red + contrato/mint | símbolo igual con ID distinto se rechaza |
| wallet | decodificación, simulación, límites y cartera separada | approval ilimitado a spender desconocido bloqueado |
| endpoint | EDR y confirmación de dirección fuera del portapapeles | proceso anómalo alerta y la dirección no coincide |
| respuesta | revocación/migración condicionada y preservación | permiso desaparece o wallet antigua deja de custodiar valor |

La solución no usa reputación de un influencer, candado TLS, volumen de seguidores o una auditoría de
código como garantía suficiente. Cada control responde a una frontera distinta.

[Volver al laboratorio](README.md)
