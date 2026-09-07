# Solución docente — Nebula Custody

> No abras esta página hasta conservar hashes y producir tu propio análisis.

## Resultado reproducible

El ledger BTC suma `10 + 3 - 0,5 = 12,5 BTC`. La wallet parte en `10 BTC` y la
fuente blockchain registra `+3 - 0,5 - 0,7 = 11,8 BTC`. La diferencia es
`0,7 BTC`. ETH suma `200 + 60 - 20 = 240 ETH` en ambas fuentes y concilia.

`req-002` enlaza el retiro BTC de `0,7` con `tx-synth-btc-002`. Está ejecutado en
`withdrawals.csv` y presente en `blockchain.csv`, pero no tiene fila en
`approvals.csv` ni asiento en `ledger.csv`. El analizador también encuentra dos
alertas críticas abiertas relacionadas con el mismo `correlation_id`.

## Timeline mínima

| Hora UTC | Observado | Fuente |
|---|---|---|
| 22:12:10 | login sólo con contraseña, equipo no administrado, riesgo 92 | `acc-003` |
| 22:12:30 | rol de wallet asumido por `u007` | `acc-004` |
| 22:12:40 | alerta de privilegio abierta | `alert-001` |
| 22:13:50 | `policy_override`, sin `approval_id` | `app-log-002` |
| 22:14:02 | retiro `req-002` marcado ejecutado | `withdrawals.csv` |
| 22:14:19 | salida BTC observada | `bc-003` |
| 00:05:00 | conciliador abre diferencia de 0,7 BTC | `alert-002` |

## Qué puede concluirse

Se observa una transferencia y una ruta de control anómala: rol privilegiado,
ausencia de aprobación registrada, override, salida on-chain y asiento ausente.
Los datos son consistentes con un bypass de controles. También muestran que una
alerta anterior a la transmisión no impidió la operación.

No puede determinarse con este dataset si `u007` actuó personalmente, si su cuenta
fue comprometida, si hubo autorización de emergencia fuera de sistema, qué
persona controló el destino, ni intención o responsabilidad penal. Harían falta,
entre otros, sesión PAM completa, IdP/MFA, ticket JIT, EDR, configuración y cambios
del policy engine, comunicaciones corporativas autorizadas, nodo propio y registros
del custodio/proveedor.

## Causa raíz de referencia

- **Causa próxima:** una ruta privilegiada ejecutó un retiro sin approval registrado.
- **Factores contribuyentes:** password-only, equipo no administrado, rol de servicio
  asumible por admin, override fail-open y alerta sin enforcement.
- **Condiciones sistémicas:** SoD aplicada de forma incompleta en backend, exceso de
  privilegio permanente, acoplamiento débil entre aprobación-firma-ledger y falta de
  barrera independiente antes de transmitir.
- **Fallo detectivo:** la conciliación sí detectó el descuadre, pero después de la
  liquidación y sin bloqueo temprano por alerta crítica.

## Controles verificables

| Tipo | Control | Prueba |
|---|---|---|
| Preventivo | deny explícito: platform admin no asume wallet signer | intento negativo por API y nube |
| Preventivo | firma sobre payload canónico ligado a approval y destino allowlisted | mutar un byte invalida autorización |
| Preventivo | JIT/JEA + FIDO2 + dispositivo conforme | sesión sin ticket/MFA/dispositivo falla |
| Preventivo | quórum/MPC-HSM con policy independiente | un solo dominio no transmite |
| Detectivo | bloqueo por alerta crítica y destino nuevo en cooling period | simulación abre caso y no firma |
| Detectivo | conciliación continua por wallet/activo | anomalía de 0,7 detectada dentro del SLA |
| Correctivo | rotación/revocación y recertificación | credencial anterior falla y grants coinciden con inventario |
| Correctivo | replay controlado del ledger con evidencia | saldo concilia sin editar originales |

## Error pedagógico central

«La blockchain dice la verdad» es incompleto: confirma la salida para las reglas de
esa cadena, pero no su legitimidad corporativa ni identidad humana. «El ledger
dice 12,5» tampoco prueba disponibilidad. La conclusión defendible nace al
reconciliar fuentes independientes y declarar límites.

[← Laboratorio](README.md)
