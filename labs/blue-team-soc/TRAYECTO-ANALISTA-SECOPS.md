# Trayecto Analista SecOps — de la alerta al cierre con evidencia

Extensión del laboratorio [`blue-team-soc`](README.md) para la ruta
[Analista SecOps](../../rutas/secops-analista.md). **No sustituye al recorrido guiado del
laboratorio: lo continúa.** Donde el recorrido base termina —*ya cazaste la fuerza bruta y
escribiste la regla*—, el trabajo del analista SecOps apenas empieza.

> ⚠️ **Solo laboratorio local.** El stack escucha en `127.0.0.1` y no lleva autenticación a
> propósito. Los datos, las IP y los activos de este trayecto son **ficticios**. No apliques estos
> comandos contra sistemas que no sean tuyos o para los que no tengas autorización escrita
> ([Clase 025](../../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)).

## 🎯 Qué practicas aquí

El ciclo completo del puesto, en ocho pasos, con **tiempos registrados y evidencia en cada uno**:

```text
1. Recibir la alerta        →  ¿qué me están diciendo?
2. Validarla                →  ¿es real, es ruido, o es real pero irrelevante?
3. Relacionar               →  ¿qué activo es, qué vale, qué vulnerabilidad lo permitió?
4. Contener                 →  parar el daño sin destruir la evidencia
5. Ejecutar el runbook      →  hacerlo igual que lo haría cualquier otra persona del equipo
6. Coordinar el parcheo     →  con dueño, ventana, reversión y verificación
7. Cerrar con evidencia     →  SLA, tiempos y prueba de que se arregló
8. Proponer la mejora       →  para que esto no vuelva a pasar tres veces
```

| Paso | Clases del programa |
|---|---|
| Validación y triaje | [182](../../classes/parte-8-blue-team-deteccion-y-soc/182-logging-y-fuentes-de-telemetria/README.md), [183](../../classes/parte-8-blue-team-deteccion-y-soc/183-siem-arquitectura-y-componentes/README.md), [188](../../classes/parte-8-blue-team-deteccion-y-soc/188-threat-hunting-metodologia/README.md) |
| Activos y vulnerabilidades | [071](../../classes/parte-3-hacking-etico-y-pentesting-metodologia/071-analisis-de-vulnerabilidades-con-nessus-y-openvas/README.md), [318](../../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md) |
| Contención y runbook | [202](../../classes/parte-9-forense-digital-y-respuesta-a-incidentes/202-el-ciclo-de-respuesta-a-incidentes-nist-y-sans/README.md), [215](../../classes/parte-9-forense-digital-y-respuesta-a-incidentes/215-playbooks-de-respuesta-a-incidentes/README.md), [216](../../classes/parte-9-forense-digital-y-respuesta-a-incidentes/216-contencion-erradicacion-y-recuperacion/README.md) |
| Parcheo y hardening | [324](../../classes/parte-17-profundizacion-para-certificaciones/324-operaciones-de-seguridad-hardening-y-gestion-de-configuracion/README.md) |
| Identidades y accesos | [313](../../classes/parte-17-profundizacion-para-certificaciones/313-gestion-del-ciclo-de-vida-de-identidades-iam-empresarial/README.md), [315](../../classes/parte-17-profundizacion-para-certificaciones/315-mfa-y-gestion-de-accesos-privilegiados-pam/README.md) |
| SLA, métricas y reporte | [197](../../classes/parte-8-blue-team-deteccion-y-soc/197-metricas-y-madurez-del-soc/README.md), [287](../../classes/parte-14-grc-riesgo-y-cumplimiento/287-metricas-de-seguridad-kpis-y-kris/README.md), [321](../../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md) |
| Mejora preventiva | [217](../../classes/parte-9-forense-digital-y-respuesta-a-incidentes/217-analisis-de-causa-raiz/README.md) |

## 🧰 Qué necesitas

- El laboratorio [`blue-team-soc`](README.md) levantado y con los datos cargados.
- Opcionalmente, [`rootcause-windows`](../rootcause-windows/README.md) para el triaje del endpoint,
  y [`devsecops-pipeline`](../devsecops-pipeline/README.md) para reutilizar
  [`priorizar.py`](../devsecops-pipeline/priorizar.py) en el paso 3.
- Un cuaderno —un archivo de texto sirve— donde anotar **la hora real de cada acción**. Los tiempos
  son parte del entregable, no un adorno.

## 📇 El contexto: inventario de activos (ficticio)

El escenario del laboratorio no trae inventario, y sin inventario no hay priorización posible. Usa
este, o construye el tuyo con la misma estructura:

| Activo | Función | Criticidad | Expuesto a internet | Dueño | Ventana de mantenimiento |
|---|---|---|---|---|---|
| `srv-web01` | Portal público | Alta | Sí | Equipo Web | Diaria 02:00–04:00 |
| `srv-db01` | Base de datos de clientes | **Crítica** | No (solo red interna) | Equipo Datos | Sábados 01:00–05:00 |
| `srv-app01` | Aplicación interna de facturación | Alta | No | Equipo Apps | Diaria 02:00–04:00 |
| `wks-ana` | Estación de trabajo | Media | No | TI | Cualquiera |

Y este es el **SLA de remediación acordado con TI** que vas a aplicar y a medir:

| Severidad | Contención | Remediación | Verificación |
|---|---:|---:|---:|
| Crítica | 4 h | 7 días | 3 días tras el cierre |
| Alta | 24 h | 30 días | 7 días |
| Media | 72 h | 90 días | 30 días |
| Baja | — | Siguiente ciclo | — |

## 1️⃣ Recibir la alerta

Parte del resultado del recorrido guiado del laboratorio. La alerta que llega a tu cola dice, en
crudo:

```text
[SIEM] Regla: multiples-fallos-autenticacion
Severidad: Media
Origen: 203.0.113.66 (CL fuera de rango habitual)
Destino: srv-db01
Detalle: >=10 login_failed en 5 minutos
```

Anota la hora en la que la recibes: es el **T0** de todas tus métricas.

**Lo primero que hace un analista SecOps no es investigar: es preguntarse qué activo es.** Un
`srv-db01` marcado como *crítico* en el inventario convierte una alerta "Media" en un caso
prioritario antes de mirar un solo log.

## 2️⃣ Validarla

Tres preguntas, en este orden, contra el SIEM del laboratorio:

```json
GET eventos-auth/_search
{
  "size": 0,
  "query": { "bool": { "filter": [
    { "term": { "source.ip.keyword": "203.0.113.66" } }
  ] } },
  "aggs": {
    "por_accion": { "terms": { "field": "event.action.keyword" } },
    "por_host":   { "terms": { "field": "host.name.keyword" } },
    "linea":      { "date_histogram": { "field": "@timestamp", "fixed_interval": "5m" } }
  }
}
```

1. **¿Hubo éxito?** Si solo hay `login_failed`, es un intento; si aparece un `login_success`, es un
   compromiso y el caso cambia de categoría en el acto.
2. **¿Hasta dónde llegó?** Busca actividad posterior desde la red interna hacia otros hosts: es el
   movimiento lateral que el recorrido base te enseñó a encontrar.
3. **¿Es ruido conocido?** Contrasta contra la actividad normal de las IP internas. Si la misma
   regla dispara todos los días por un escáner de la propia empresa, el hallazgo no es el ataque:
   **es la regla**.

Registra la hora de la validación. La diferencia con T0 es tu **tiempo de triaje**.

> 📝 **Documenta también lo que descartas.** "Descartado por ser el escáner de inventario, ticket
> INV-114" vale tanto como una confirmación, y evita que el próximo turno lo investigue de cero.

## 3️⃣ Relacionar: activo, vulnerabilidad y exposición

Aquí es donde el trabajo deja de parecerse al del SOC. La pregunta no es *qué pasó*, sino **por qué
fue posible y qué otros activos comparten esa causa**.

Para este escenario, la causa raíz técnica es una combinación clásica:

- SSH con **autenticación por contraseña habilitada** y sin bloqueo por intentos fallidos.
- La cuenta **`root` puede iniciar sesión directamente** por SSH.
- No hay **MFA** ni bastión para el acceso administrativo.

Construye la tabla de causas y su alcance real:

| Causa | Activos afectados | Severidad | Justificación |
|---|---|---|---|
| `PermitRootLogin yes` | `srv-db01`, `srv-app01` | Crítica | Acceso administrativo directo sobre el activo crítico |
| Sin límite de intentos (fail2ban/`MaxAuthTries`) | los tres servidores | Alta | Hace viable la fuerza bruta |
| Sin MFA para acceso administrativo | todos | Alta | Una credencial basta para entrar |
| Sin restricción de origen para SSH | `srv-web01` | Alta | Superficie innecesaria desde internet |

**Ejercicio de priorización con criterio explícito.** Si además tienes el laboratorio
[`devsecops-pipeline`](../devsecops-pipeline/README.md), aprovecha su
[`priorizar.py`](../devsecops-pipeline/priorizar.py) para practicar el mismo razonamiento sobre CVE
reales: consulta **CISA KEV** y **EPSS** y ordena por riesgo, no por severidad nominal.

```bash
cd ../devsecops-pipeline
python priorizar.py --hallazgos hallazgos-ejemplo.json
python priorizar.py --hallazgos hallazgos-ejemplo.json --sin-red   # sin acceso a KEV/EPSS
```

Fíjate en el campo `exposicion` de cada hallazgo: el script aplica un factor (`publica` 1.0,
`interna` 0.6, `no-alcanzable` 0.2) y, cuando no se declara, usa `desconocida` = 0.8 — **no asume el
mejor caso**. Ese detalle es exactamente el criterio que tienes que defender con tu inventario.

El criterio que debes poder defender por escrito, en este orden:

1. ¿Hay **explotación activa conocida** (KEV)?
2. ¿Cuál es la **probabilidad estimada de explotación** (EPSS)?
3. ¿Está el activo **expuesto** o segmentado?
4. ¿Qué **criticidad de negocio** tiene según tu inventario?
5. Solo entonces, ¿qué dice el **CVSS**?

## 4️⃣ Contener

Contener es **parar el daño sin destruir la evidencia**. En este escenario, el orden razonable:

1. **Bloquear el origen** `203.0.113.66` en el perímetro. Rápido, reversible y no toca el servidor.
2. **Revocar las sesiones activas** de la cuenta comprometida y **forzar el cambio de credencial**.
3. **Aislar `srv-db01`** de la red solo si hay indicios de actividad posterior al acceso — y
   coordinándolo con el dueño del activo, porque es un sistema crítico.
4. **Preservar antes de limpiar.** Si vas a apagar, reinstalar o reiniciar, primero recolecta: la
   evidencia perdida no se recupera. Si el equipo afectado es Windows, este es el momento de
   [`rootcause-windows`](../rootcause-windows/README.md).

Anota la hora de la primera acción de contención: T1 − T0 es tu **tiempo hasta contención**, y es
la métrica que más te van a mirar.

> ⚠️ **No confundas contener con erradicar.** Bloquear la IP no elimina la causa: si la
> configuración sigue igual, mañana entra otra IP. La erradicación es el paso 6.

## 5️⃣ Ejecutar el runbook

Un runbook es lo que permite que **cualquier persona del equipo haga esto igual que tú a las tres de
la madrugada**. Escríbelo tú, con esta estructura mínima:

```markdown
# Runbook: acceso no autorizado por fuerza bruta SSH

## Cuándo se aplica
Alerta de >= 10 login_failed de una misma IP en 5 minutos, con o sin login_success posterior.

## Datos que hay que recolectar antes de tocar nada
- IP de origen, cuentas objetivo, host destino, ventana temporal.
- ¿Hubo login_success? ¿Desde esa IP o desde otra? ¿Hacia otros hosts?

## Decisión
- Sin éxito  -> severidad Media. Bloquear origen, registrar, cerrar.
- Con éxito  -> severidad Crítica. Continuar con contención completa y escalar.

## Pasos de contención (en orden)
1. Bloquear IP de origen en el perímetro. Registrar hora.
2. Revocar sesiones y rotar credencial de la cuenta afectada. Registrar hora.
3. Recolectar evidencia del host antes de cualquier reinicio.
4. Evaluar aislamiento con el dueño del activo.

## Criterio de escalamiento
Escalar a DFIR si: hay persistencia, movimiento lateral confirmado, exfiltración sospechada
o el activo es crítico y hubo acceso con privilegios.

## Cierre
No se cierra sin: causa raíz identificada, remediación con ticket y fecha, y verificación.
```

Guárdalo en tu repositorio. **Es uno de los entregables de portafolio de este rol.**

## 6️⃣ Coordinar la remediación y el parcheo

Aquí se juega el oficio. Convierte cada causa del paso 3 en un ticket que un equipo de TI pueda
ejecutar sin volver a preguntarte nada:

```markdown
Ticket SEC-2026-0312
Activo:        srv-db01 (crítico, dueño: Equipo Datos)
Hallazgo:      SSH permite login directo de root y no limita intentos fallidos
Evidencia:     compromiso confirmado el 2026-03-04, caso INC-0312
Acción:        PermitRootLogin no | MaxAuthTries 3 | fail2ban activo
               acceso administrativo solo vía bastión con MFA
Riesgo si no:  acceso administrativo directo a la base de datos de clientes
Ventana:       sábado 01:00-05:00 (según inventario)
Reversión:     copia de /etc/ssh/sshd_config previa; validar sesión abierta antes de cerrar
Verificación:  nuevo escaneo autenticado + intento controlado de login root (debe fallar)
SLA:           remediación 7 días (severidad crítica)
```

Tres cosas que separan un ticket que se ejecuta de uno que se ignora:

- **Un plan de reversión.** Sin él, nadie toca un servidor crítico un sábado.
- **Un criterio de verificación concreto**, escrito antes de aplicar el cambio.
- **La ventana real del inventario**, no la que a ti te viene bien.

**Cuando la remediación no es posible a tiempo**, no se deja en el aire: se documenta una excepción.

```markdown
Excepción EXC-2026-014
Riesgo aceptado:  srv-app01 no puede desactivar login por contraseña hasta migrar
                  la automatización heredada que la usa
Solicita:         Equipo Apps        Aprueba: Jefatura de Infraestructura
Compensación:     restricción de origen por firewall + alerta con umbral 3 intentos
                  + revisión semanal del log de accesos
Vence:            2026-05-31   (sin renovación explícita, se revierte a bloqueo)
```

Sin **fecha de vencimiento y control compensatorio**, eso no es una excepción: es un olvido con
membrete.

## 7️⃣ Cerrar con evidencia y registrar los tiempos

Un caso se cierra cuando puedes demostrar las tres cosas: **qué pasó, qué se cambió y que el cambio
funciona**.

| Marca | Momento | Hora | Métrica derivada |
|---|---|---|---|
| T0 | Recepción de la alerta | | — |
| T1 | Validación concluida | | Tiempo de triaje |
| T2 | Primera acción de contención | | **Tiempo hasta contención** |
| T3 | Ticket de remediación creado con dueño | | Tiempo hasta asignación |
| T4 | Remediación aplicada | | **MTTR** |
| T5 | Verificación superada | | Tiempo hasta cierre verificado |

La evidencia de cierre de este escenario:

- La consulta al SIEM que **ya no** devuelve accesos exitosos desde la IP bloqueada.
- La salida de `sshd -T | grep -i permitrootlogin` mostrando `permitrootlogin no`.
- Un intento controlado de login como `root` que **falla**, con su registro correspondiente.
- El ticket cerrado con el enlace a la evidencia y la fecha de verificación.

> 🚫 **Cerrar sin verificar es el error más común y más caro del rol.** Sube el MTTR aparente,
> baja la confianza real y garantiza que el hallazgo reaparezca en el siguiente escaneo.

## 8️⃣ Proponer la mejora preventiva

El paso que convierte un incidente en una mejora del programa. Distingue tres niveles:

- **Correctivo** (ya lo hiciste): arreglar este activo.
- **Preventivo**: aplicar la línea base a *todos* los activos con la misma causa —revisar los tres
  servidores del inventario, no solo `srv-db01`— y dejarla como configuración por defecto.
- **De detección**: mejorar la regla que disparó. Si detectó tarde, baja el umbral; si genera ruido,
  añade contexto (origen geográfico, cuenta privilegiada, activo crítico) en lugar de silenciarla.

Escríbelo como propuesta de una página con: causa raíz, alcance, esfuerzo estimado, dueño propuesto
y **qué métrica debería moverse** si se implementa. Esa última línea es la que consigue presupuesto.

## 🏆 Retos verificables

1. **Caso completo.** Entrega el informe del incidente con las seis marcas de tiempo rellenas.
   *Aceptación:* cada marca tiene su evidencia asociada y el tiempo hasta contención es coherente
   con el SLA de severidad crítica.
2. **Priorización defendible.** Entrega la tabla de causas priorizada con el criterio KEV → EPSS →
   exposición → criticidad → CVSS aplicado explícitamente. *Aceptación:* otra persona reordena la
   lista igual que tú usando solo tu criterio escrito.
3. **Runbook reutilizable.** *Aceptación:* alguien que no vivió el incidente ejecuta tu runbook
   sobre el laboratorio y llega a las mismas conclusiones y decisiones.
4. **Excepción bien construida.** *Aceptación:* incluye solicitante, aprobador, control
   compensatorio verificable y fecha de vencimiento; y explicas qué pasa el día del vencimiento.
5. **Verificación honesta.** *Aceptación:* aportas la prueba de que el cambio funciona **y** la
   prueba negativa (el intento que ahora falla). Un "ya está" no es evidencia.
6. **Mejora preventiva con métrica.** *Aceptación:* la propuesta nombra la métrica que debería
   moverse y en cuánto tiempo.
7. **Informe mensual.** Redacta una página con las métricas del periodo dirigida a una jefatura sin
   formación técnica. *Aceptación:* quien lo lee sabe **qué tiene que decidir** al terminar.

## 🔗 Cómo se conecta

- 📖 Ruta completa: [Analista SecOps](../../rutas/secops-analista.md)
- 🗺️ [Matriz de roles SecOps y DevSecOps](../../docs/matriz-roles-secops-devsecops.md) — dónde
  termina tu trabajo y empieza el del SOC, el de DFIR y el de DevSecOps
- 🎓 [Examen final por rol](../../docs/examen-final-por-rol.md) — el examen de Analista SecOps usa
  este trayecto
- 🧪 Laboratorios vecinos: [`rootcause-windows`](../rootcause-windows/README.md) ·
  [`devsecops-pipeline`](../devsecops-pipeline/README.md) ·
  [`cloud-security`](../cloud-security/README.md)
- ⬅️ [Volver al laboratorio](README.md) · 🧪 [Índice de laboratorios](../README.md)
