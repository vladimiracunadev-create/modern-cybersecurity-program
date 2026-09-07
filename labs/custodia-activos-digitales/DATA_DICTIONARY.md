# Diccionario de datos y contrato de evidencia

## Fuentes

| Archivo | Verdad principal | Qué permite afirmar | Límite |
|---|---|---|---|
| `users.csv` | identidad | estado y área declarados | no prueba quién usó una sesión |
| `roles.csv` | autorización | rol asignado en el periodo | no prueba legitimidad ni uso efectivo |
| `permissions.csv` | política | decisión esperada bajo condiciones | no prueba que el enforcement funcionó |
| `ledger.csv` | contable | movimientos registrados | no prueba liquidación externa |
| `wallets.csv` | operación/configuración | inventario y saldo inicial del ejercicio | direcciones y saldos son sintéticos |
| `withdrawals.csv` | operacional | solicitudes y estado de ejecución | puede contener estado incorrecto o incompleto |
| `approvals.csv` | operacional/control | aprobaciones registradas | ausencia no demuestra por sí sola que nunca hubo aprobación |
| `exchange.csv` | operacional externa | snapshots declarados por exchange ficticio | requiere confirmar alcance, hora y cuenta |
| `blockchain.csv` | criptográfica derivada | movimientos observados y confirmaciones del dataset | no atribuye identidad o propósito económico |
| `access_logs.jsonl` | identidad/endpoint | sesiones y asunción de rol observadas | IP/dispositivo no equivalen automáticamente a persona |
| `application_logs.jsonl` | aplicación | decisiones y acciones emitidas | un administrador podría afectar su productor |
| `security_alerts.jsonl` | detección | reglas disparadas y riesgo calculado | alerta no equivale a incidente confirmado |

## Campos de evento normalizado

| Campo | Semántica | Regla de calidad |
|---|---|---|
| `event_id` | identificador inmutable del evento | único por productor |
| `timestamp` | instante de ocurrencia en UTC ISO 8601 | conservar también tiempo de ingesta en producción |
| `user_id`, `role` | actor declarado y rol efectivo | no reemplazar actor por usuario objetivo |
| `session_id`, `device_id`, `source_ip` | contexto de acceso | permitir vacío explícito, no inventar valores |
| `action`, `result` | verbo normalizado y resultado | catálogo versionado |
| `asset`, `amount` | activo e importe decimal | precisión por activo; nunca `float` para conciliación |
| `source_wallet`, `destination_wallet` | extremos lógicos | distinguir wallet interna de address externa |
| `approval_id`, `request_id` | decisiones de workflow | integridad referencial y cardinalidad documentadas |
| `tx_hash`, `block_number` | ancla de liquidación | validar formato/cadena y confirmaciones |
| `exchange` | custodio o plataforma operacional | cuenta y alcance deben acompañarse en producción |
| `risk_score` | salida de regla/modelo | registrar versión, señales y umbral |
| `correlation_id` | vínculo transversal del caso | no reutilizar entre operaciones independientes |

## Reglas de conciliación

1. Usar `Decimal` y precisión nativa del activo, nunca punto flotante binario.
2. Separar principal, fee, cambio UTXO, token, gas y movimientos internos.
3. Comparar dentro de una ventana que contemple ingesta tardía y finalización.
4. No sumar snapshots como movimientos.
5. Declarar cobertura: wallets, exchanges, redes y periodo incluidos.
6. Abrir excepción si falta referencia, cambia el estado o excede tolerancia.
7. Cerrar sólo con evidencia, responsable independiente y motivo versionado.

[← Laboratorio](README.md)
