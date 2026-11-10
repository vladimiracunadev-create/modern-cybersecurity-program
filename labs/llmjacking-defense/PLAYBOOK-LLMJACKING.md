# Playbook — credencial o endpoint de IA presuntamente comprometido

> Guía de laboratorio, no procedimiento certificado. Adáptala a tus proveedores, a tu contrato y a tu asesoría legal.
> Los comandos concretos dependen de cada proveedor: consulta su documentación vigente antes de ejecutarlos.

## 0. Principio

Contener **sin destruir evidencia** y **sin tumbar el servicio legítimo** más de lo necesario. Una alerta es una anomalía, no
una atribución: la certeza sale de correlar identidad, origen, API llamada y facturación.

## 1. Triaje (0–15 min)

| Pregunta | Dónde se responde | Hecho / inferencia |
|---|---|---|
| ¿Qué identidad y qué clave? | registro de auditoría del proveedor | hecho |
| ¿Primer uso anómalo? | línea de tiempo del registro de invocaciones | hecho |
| ¿Qué modelos y regiones? | eventos de invocación | hecho |
| ¿Hubo cambios de permisos, nuevas claves o servicios habilitados? | auditoría de IAM | hecho |
| ¿Hay consultas de configuración de logging? | auditoría | hecho (la intención es hipótesis) |
| ¿Coincide con una clave expuesta? | secret scanning, historial de Git | hecho / inferencia |

## 2. Contención (15–60 min)

| Control | Tipo | Nota |
|---|---|---|
| Desactivar la clave comprometida (no borrarla aún) | correctivo | conserva su rastro; el borrado puede dificultar la investigación |
| Revocar sesiones/tokens de la identidad | correctivo | las credenciales de corta duración ya emitidas pueden seguir vivas hasta expirar |
| Quitar permisos añadidos y servicios de IA habilitados | correctivo | compara con la configuración aprobada |
| Cerrar el endpoint de inferencia o vincularlo a loopback | correctivo | en Ollama, tras proxy con autenticación |
| Aplicar un tope/cuota temporal | compensatorio | acepta el costo colateral sobre tráfico legítimo |
| Bloquear orígenes concretos | compensatorio | frágil: rotan fácilmente |

## 3. Preservación de evidencia

1. Exporta registros de auditoría e invocación **antes** de que expire su retención.
2. Calcula y guarda hash de cada exportación; registra quién, cuándo y desde dónde la hizo.
3. Captura la configuración de IAM, cuotas y presupuestos *antes* de modificarla.
4. Si hay un servidor propio, haz imagen/volcado según la política DFIR (Parte 9) antes de reiniciar.

## 4. Erradicación y recuperación

- Emite credenciales nuevas con el mínimo privilegio y, si el proveedor lo permite, de corta duración.
- Busca otras copias de la clave (repositorios, CI, contenedores, wikis, historial).
- Verifica que la recuperación usa orígenes y modelos esperados (escenario S7 del laboratorio).
- Vuelve a ejecutar el detector sobre la nueva actividad.

## 5. Comunicación y cierre

- Informe técnico: línea de tiempo, evidencia, controles que fallaron, hipótesis descartadas.
- Informe ejecutivo: exposición económica, causa raíz, decisiones pendientes.
- Reclamación al proveedor: solicita revisión de cargos fraudulentos conforme a sus términos; no asumas que se reembolsa.
- Revisión posterior sin culpables: ¿qué control habría cortado el gasto antes, y a qué costo?

## 6. Preguntas para la revisión

1. ¿Qué control detectivo disparó primero y cuánto tardó?
2. ¿Existía un control preventivo que limitara el gasto? ¿Por qué no se activó?
3. ¿Qué evidencia se perdió o estuvo a punto de perderse?
