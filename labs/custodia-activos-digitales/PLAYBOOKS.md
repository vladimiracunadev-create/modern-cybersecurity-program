# Playbooks de respuesta para custodia digital

## Reglas comunes

Todo playbook abre un caso con hora UTC, líder, alcance y canal fuera de banda;
preserva ledger, logs, IAM/PAM, configuración, nodos, wallets y proveedor antes de
cambiar lo que sea viable preservar. Contención requiere autoridad y reversión.
Legal/compliance decide notificación según jurisdicción y obligaciones; el equipo
técnico no promete recuperación ni atribuye culpabilidad. El cierre exige
conciliación, riesgo residual aceptado, monitoreo reforzado y postmortem.

## 1. Pérdida inexplicable de fondos

- **Trigger/severidad:** diferencia sobre tolerancia; crítica si crece, afecta cold
  storage o compromete solvencia.
- **Roles:** líder IR, tesorería, wallet, SOC, DFIR, IAM, legal/compliance, auditor.
- **Contención:** pausar por activo/ruta con aprobación; proteger evidencias y
  bloquear destinos sólo con fundamento.
- **Evidencia:** snapshots, ledger, TXIDs, nodos, exchange, approvals, sesiones y reloj.
- **Comunicación:** canal restringido; cifras con corte, cobertura e incertidumbre.
- **Recuperación/postmortem:** reconciliar, reabrir por etapas, probar límites y
  corregir causas de autorización, registro y detección.

## 2. Compromiso de wallet

- **Trigger/severidad:** firma/destino no reconocido, seed expuesta o política de
  firma alterada; crítica ante capacidad de mover fondos.
- **Roles:** líder, custodios de clave, wallet engineering, DFIR, tesorería y legal.
- **Contención:** detener firmas afectadas; migrar según ceremonia aprobada sin
  destruir artefactos; revocar componentes/credenciales comprometidos.
- **Evidencia:** firmware, configuración, attestation, sesiones, requests, firmas y TXIDs.
- **Comunicación:** custodios por canal fuera de banda; no publicar direcciones o
  hipótesis que perjudiquen recuperación.
- **Recuperación/postmortem:** nueva política/quórum, rotación, verificación de
  backups y ceremonia registrada; probar que la ruta antigua ya no firma.

## 3. Riesgo insider

- **Trigger/severidad:** combinación de privilegio, bypass, acceso anómalo y efecto;
  ninguna señal aislada determina intención.
- **Roles:** IR, IAM/PAM, DFIR, RR. HH., legal, seguridad física y dirección autorizada.
- **Contención:** preservar discretamente, reducir acceso por riesgo y función,
  aplicar doble control; no confrontar ni vigilar fuera de autoridad.
- **Evidencia:** grants, JIT, sesiones, tickets, comunicaciones corporativas
  autorizadas, endpoint y decisiones de negocio.
- **Comunicación:** need-to-know, privacidad y debido proceso.
- **Recuperación/postmortem:** corregir acumulación de privilegios, recertificar,
  rotar secretos y separar error, cuenta comprometida, colusión e intención.

## 4. Compromiso de cuenta de exchange

- **Trigger/severidad:** login, API key, whitelist, trade o retiro no reconocido.
- **Roles:** IR, tesorería, proveedor, IAM, DFIR y legal/compliance.
- **Contención:** congelar API/retiros por canal verificado; revocar sesiones y keys;
  preservar antes/después y evitar reset prematuro de artefactos.
- **Evidencia:** exports firmados, IDs de orden, login, subcuentas, IP, soporte y TXIDs.
- **Comunicación:** contacto contractual verificado, no datos del ticket recibido por
  el mismo canal posiblemente comprometido.
- **Recuperación/postmortem:** nuevas claves de mínimo alcance, allowlist/cooling,
  subcuentas y conciliación completa de trades, fees y retiros.

## 5. API key filtrada

- **Trigger/severidad:** detector de secretos, repositorio/chat o uso desde origen
  nuevo; crítica si permite retiro o administración.
- **Roles:** servicio propietario, IAM, DevSecOps, SOC e IR.
- **Contención:** deshabilitar/rotar coordinadamente, buscar uso histórico y evitar
  exponer el secreto en tickets/logs.
- **Evidencia:** metadatos del hallazgo, historial autorizado, audit de API y scopes.
- **Comunicación:** redactar valor; avisar a propietarios y dependencias.
- **Recuperación/postmortem:** credencial corta de workload, secret manager,
  rotación y prueba negativa con la clave anterior.

## 6. Discrepancia detectada

- **Trigger/severidad:** regla de conciliación; severidad por importe, antigüedad,
  repetición y cobertura, no sólo por porcentaje.
- **Roles:** conciliador independiente, tesorería, datos, wallet, SOC y auditor.
- **Contención:** marcar excepción y evitar cierre automático; pausar únicamente la
  ruta afectada si el riesgo lo justifica.
- **Evidencia:** inputs/versiones del job, snapshots, fees, reorg/confirmaciones,
  decimales, registros tardíos y cambios de parser.
- **Comunicación:** saldo, corte, tolerancia, cobertura y explicación pendiente.
- **Recuperación/postmortem:** corrección controlada, replay idempotente y test con
  anomalías conocidas; nunca «ajustar para que cuadre» sin evidencia.

## 7. Retiro no autorizado

- **Trigger/severidad:** ejecución sin aprobación válida, destino/payload cambiado o
  política bypass; crítica si confirmado o repetible.
- **Roles:** IR, wallet, tesorería, IAM/PAM, DFIR, legal y dirección.
- **Contención:** detener ruta/credencial, proteger fondos restantes según runbook,
  preservar sesión y contactar proveedores por canal autenticado.
- **Evidencia:** request canónico, decisión de política, aprobación, firma, TXID,
  sesión, dispositivo, código/configuración y despliegues.
- **Comunicación:** hechos confirmados y rango; autoridades/contrapartes por decisión legal.
- **Recuperación/postmortem:** reparar enforcement, recertificar y probar mutación,
  autoaprobación, fail-open y destino nuevo.

## 8. Manipulación del ledger interno

- **Trigger/severidad:** asiento fuera de workflow, secuencia/hash inconsistente,
  actor imposible o diferencia con operación/cadena.
- **Roles:** DFIR, data/DBA separado del investigado, auditor, tesorería e IR.
- **Contención:** snapshot/backup consistente, bloquear escrituras de riesgo sin
  perder journal/WAL y habilitar modo degradado aprobado.
- **Evidencia:** WAL/audit DB, queries, identidades, jobs, backups, schema y cambios.
- **Comunicación:** no llamar «manipulación intencional» a corrupción o error hasta
  demostrar mecanismo y contexto.
- **Recuperación/postmortem:** restauración verificada, replay idempotente,
  append-only/separación y conciliación total antes de reabrir.

## Criterios de mantenimiento

Cada ficha debe convertirse en runbook local con propietario, versión, contactos,
comandos, approvals y dependencias. Se prueba mediante tabletop semestral y después
de cambios de proveedor, wallet, esquema o identidad. Automatizar enriquecimiento
no autoriza congelar fondos, revocar a escala ni destruir evidencia.

[← Laboratorio](README.md)
