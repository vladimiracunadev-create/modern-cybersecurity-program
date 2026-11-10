# Laboratorio — LLMjacking: detectar, contener y demostrar que los controles funcionan

**Modalidad:** simulación local y determinista, sin red, sin proveedores de IA, sin claves reales y sin costo.
**Clases:** [295](../../classes/parte-15-seguridad-de-ia-y-machine-learning/295-owasp-top-10-para-aplicaciones-con-llm/README.md),
[297](../../classes/parte-15-seguridad-de-ia-y-machine-learning/297-seguridad-de-aplicaciones-con-llm-rag-y-agentes/README.md) y
[300](../../classes/parte-15-seguridad-de-ia-y-machine-learning/300-gobernanza-y-etica-de-la-ia-segura/README.md) (Parte 15), con
conexiones a las Partes 8, 9, 10, 11 y 14.

> ⚠️ **Ética.** Todo lo que hay aquí es ficticio: identidades, IP (rangos de documentación y privados), modelos, precios y
> claves. No hay código que valide credenciales, escanee infraestructura ni llame a un modelo. No lo adaptes para probar
> claves o servidores ajenos: eso es acceso no autorizado.

## Qué problema resuelve

El abuso de cómputo de IA se parece a un uso legítimo hasta que se mira su **contexto**: quién llama, desde dónde, con qué
modelo, a qué hora, con qué permisos recientes y con qué ritmo. Este laboratorio te hace construir y *medir* esa idea:

1. generas 16 días de actividad (14 de línea base + 2 de evaluación) con ocho escenarios;
2. un detector puntúa cada ventana de 10 minutos con señales explicables;
3. mides precisión, recall, falsos positivos y latencia;
4. comparas cuánto cuesta cada incidente con **alerta de presupuesto**, **detección + revocación** y **tope duro**.

## Ejecutar

```bash
python labs/llmjacking-defense/llmjacking_lab.py run --seed 7 --out labs/llmjacking-defense/salida
python labs/llmjacking-defense/llmjacking_lab.py robustez --seeds 5
python -m unittest discover -s labs/llmjacking-defense/tests -v
python labs/llmjacking-defense/secret_scan.py <archivo-o-carpeta>
```

Solo biblioteca estándar de Python 3.12 (no hace falta `uv`, Docker ni dependencias). `salida/` se ignora en Git.
Genera `informe.md` (resumen ejecutivo + detalle técnico), `metricas.json` y `eventos-ecs.ndjson`.

## Los ocho escenarios

| # | Escenario | Qué simula | Etiqueta real |
|---|---|---|---|
| S1 | Consumo normal | 6 identidades con horario laboral, modelos y orígenes estables | benigno |
| S2 | Exposición de clave | un escáner reporta la clave de `svc-chatbot` publicada (evento de contexto, no de uso) | contexto |
| S3 | Consumo anómalo | 20 solicitudes/min al modelo más caro desde un origen nuevo, 4 h | malicioso |
| S4 | Validación mínima | 120 solicitudes con `max_tokens=1` sobre 3 modelos y 2 consultas de configuración de logging | malicioso |
| S5 | Ollama expuesto | identidad `anonymous` contra un endpoint simulado sin autenticación | malicioso |
| S6 | Privilegios excesivos | `svc-batch-marketing` recibe una política nueva y usa un modelo caro de madrugada | malicioso |
| S7 | Contención y recuperación | `DisableKey`, reintentos con 403 y clave nueva usada desde el origen conocido | mixto |
| S8 | Ráfaga legítima | `svc-summarizer` multiplica por ocho su volumen con un cambio aprobado (`CHG-1042`) | benigno |

S2→S4→S3→S7 forman **un mismo incidente** (INC-A); S5 es INC-B y S6 es INC-C.
Los hechos reales que inspiran los patrones (validación con solicitudes mínimas, consulta de logging, reventa, Ollama
expuesto) están en la clase 295 con su fuente; aquí solo se reproducen **como patrones sintéticos**.

## Cómo puntúa el detector

Cada ventana de 10 minutos de una identidad se evalúa con nueve señales. Ninguna es concluyente por sí sola: la alerta exige
**≥ 4 puntos y ≥ 2 señales distintas**.

| Señal | Peso | Definición (unidades) |
|---|---|---|
| `costo_z` | 2 | z robusto del costo de la ventana (USD/ventana) frente a las ventanas activas de la línea base |
| `tasa_z` | 1 | z robusto del número de solicitudes por ventana |
| `identidad_nueva` | 2 | identidad sin historial |
| `modelo_no_autorizado` | 2 | modelo que la identidad nunca usó en la línea base |
| `fuera_de_horario` | 1 | hora UTC con < 1 % de la actividad histórica de esa identidad |
| `cambio_de_permisos` | 2 | `AttachPolicy`, `PutPolicy` o `EnableModel` en las 24 h previas |
| `barrido_minimo` | 3 | ≥ 20 solicitudes con `max_tokens ≤ 1` en la ventana |
| `origen_nuevo` | 1 | red /24 de origen nunca vista para la identidad (con ≥ 5 solicitudes) |
| `clave_expuesta` | 1 | clave reportada como expuesta **y** uso desde un origen nuevo |

**Z robusto:** `z = (x − mediana) / max(σ, 0,1·mediana)`, con `σ = 1,4826 · MAD`. Usa mediana y MAD porque la media y la
desviación estándar se distorsionan con un solo valor extremo (justo lo que se quiere detectar). El piso `0,1·mediana`
evita dividir por casi cero cuando la línea base es muy regular; sin él, cualquier desviación pequeña daría z enormes.
Con z > 6 se marca la señal. Los z de miles que ves en el informe indican que el piso, no la dispersión real, domina:
interprétalos como «mucho más allá del umbral», no como probabilidades.

**Sin geolocalización.** El origen solo aporta 1 punto y nunca basta: una VPN, un cambio de ISP o un servicio cloud nuevo
producirían falsos positivos, y un atacante puede usar infraestructura en el mismo país.

**Contexto de cambio aprobado.** Si la ventana está cubierta por un registro (`identidad + modelos + horario`) se descartan
las señales de volumen y de modelo. Las demás señales siguen activas: un cambio aprobado no excusa un origen desconocido.

**Detección ≠ atribución.** El campo `hipotesis` es una etiqueta para el analista, no un veredicto.

## Controles simulados y sus supuestos

| Estrategia | Tipo | Cómo se modela |
|---|---|---|
| Alerta de presupuesto | detectivo | llega `retraso_presupuesto_h` = 8 h después y un humano tarda 15 min en actuar |
| Detección + revocación | detectivo + correctivo | primera alerta + 15 min de respuesta humana |
| Tope duro diario | preventivo | 2 × el mayor costo diario de la línea base; identidad desconocida = tope 0 |
| Tope + cambio aprobado | preventivo con contexto | el tope del día se multiplica por 10 para la identidad con cambio aprobado |

El retraso de 8 h es un **supuesto de simulación** inspirado en que la documentación de AWS Budgets indica que sus datos se
actualizan hasta tres veces al día; no es una medición de ningún proveedor ni de otros servicios de presupuesto. Cámbialo
(`exposicion(..., retraso_presupuesto_h=...)`) y observa cuándo deja de importar.

### Lo que enseñan los números (semilla 7)

- La **alerta de presupuesto** no redujo el gasto: INC-A y INC-C terminan antes de que la alerta llegue.
- **INC-A** se detecta en el barrido de validación, 10 min después del primer evento, **antes** de que empiece la fase cara.
- El **tope duro** limita el daño a ~2 USD, pero deniega 149 solicitudes legítimas de `svc-chatbot`: el atacante agota la
  cuota y el servicio legítimo se queda sin ella (efecto descrito por Sysdig en 2024). Un control preventivo tiene costo.
- Con el **cambio aprobado** el tope deja de castigar a `svc-summarizer` (130 → 0 solicitudes denegadas).
- Hay un **falso positivo residual** (semillas 4 y 7): tráfico normal de `svc-batch-marketing` en la tarde posterior al
  incidente, con un cambio de permisos aún dentro de las 24 h. La señal es razonable (la credencial *sigue* comprometida
  si nadie la revocó); la lección es que el remedio no es afinar el umbral sino **revocar y quitar el permiso**.

## Evaluación y límites

- Las métricas validan la **lógica**; los umbrales se afinaron con este mismo generador, así que no prometen rendimiento real.
  `robustez` repite con cinco semillas para ver variación, no para certificar nada.
- No hay *concurrencia simultánea inusual* ni *solicitudes repetitivas de muy bajo consumo* distintas del barrido: queda como
  ejercicio ampliar el detector.
- `eventos-ecs.ndjson` usa nombres de campo al estilo ECS; **no se probó la carga en Elastic**. Es un formato de intercambio.
  El laboratorio [`blue-team-soc`](../blue-team-soc/README.md) sigue funcionando por separado.
- La detección de secretos de CI sigue siendo [gitleaks](../../.gitleaks.toml). `secret_scan.py` es didáctico y **nunca
  valida** una clave contra un proveedor.

## Rúbrica (criterios de aceptación)

| Criterio | Evidencia |
|---|---|
| Reproducibilidad | misma semilla → mismo `informe.md` byte a byte |
| Explicabilidad | cada alerta lista sus señales con valores |
| Medición honesta | precisión, recall, FP y latencia reportados con sus límites |
| Controles | tabla de exposición por estrategia con supuestos explícitos |
| Costo colateral | el alumno identifica qué tráfico legítimo bloquea el tope |
| Contención | entrega el playbook aplicado a INC-A con evidencia preservada |

## Retos

1. Añade la señal «concurrencia inusual» (identidades distintas con la misma clave en la misma ventana) y mide si mejora algo.
2. Baja `UMBRAL_Z` a 3: ¿qué falsos positivos aparecen y qué señal los absorbe?
3. Cambia `retraso_presupuesto_h` a 1 y a 0,25: ¿desde qué retraso la alerta de presupuesto empieza a pagar?
4. Escribe una regla de `secret_scan.py` para otro formato de credencial **solo con fixtures construidos en ejecución**.
5. Redacta el informe ejecutivo de INC-C en una página, separando hechos, inferencias e hipótesis.

Playbook de respuesta: [`PLAYBOOK-LLMJACKING.md`](PLAYBOOK-LLMJACKING.md).
