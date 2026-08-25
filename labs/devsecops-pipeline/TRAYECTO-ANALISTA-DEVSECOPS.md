# Trayecto Analista DevSecOps — de 20 000 hallazgos a 12 decisiones

Extensión del laboratorio [`devsecops-pipeline`](README.md) para la ruta
[Analista DevSecOps](../../rutas/devsecops-analista.md). **No sustituye al recorrido guiado de las
ocho capas: lo continúa.** El recorrido base termina cuando los escáneres han hablado; el trabajo
del analista empieza exactamente ahí.

> ⚠️ Todo lo que hay en `repo-vulnerable/` es **inseguro a propósito** y sus credenciales son
> **falsas**. No lo despliegues ni reutilices su código. Practica solo aquí o en repositorios
> tuyos o con autorización explícita
> ([Clase 025](../../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)).

## 🎯 Qué practicas aquí

```text
1. Recibir la salida de varios escáneres   →  formatos distintos, mismo problema
2. Normalizar y deduplicar                 →  un hallazgo es un hallazgo, no tres
3. Separar los falsos positivos            →  con argumento y por escrito
4. Priorizar                               →  KEV, EPSS, CVSS, exposición y criticidad
5. Crear tickets y acordar SLA             →  con dueño, fecha y criterio de verificación
6. Documentar una excepción                →  responsable, vencimiento y compensación
7. Verificar la corrección                 →  ¿se arregló o se dejó de mirar?
8. Reportar riesgo y métricas              →  dos vistas: desarrollo y dirección
```

| Paso | Clases del programa |
|---|---|
| Escáneres y sus límites | [238](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/238-sast-analisis-estatico-de-codigo/README.md), [239](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/239-dast-analisis-dinamico-de-aplicaciones/README.md), [240](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/240-sca-dependencias-y-riesgo-de-terceros/README.md), [241](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md) |
| Priorización y escala | [245](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md), [318](../../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md) |
| Inventario y respuesta | [246](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md) |
| Riesgo y excepciones | [277](../../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md), [282](../../classes/parte-14-grc-riesgo-y-cumplimiento/282-politicas-estandares-y-procedimientos/README.md), [284](../../classes/parte-14-grc-riesgo-y-cumplimiento/284-gestion-de-riesgo-de-terceros-y-proveedores/README.md) |
| Reporte y cultura | [321](../../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md), [248](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md) |

## 🧰 Punto de partida

Ejecuta el recorrido base completo para tener materia prima real:

```bash
cd labs/devsecops-pipeline
docker compose build && docker compose up -d
docker compose exec auditor ./auditar.sh          # las ocho capas -> salida/
```

Trabaja sobre lo que quede en `salida/`. Si alguna capa aparece como `NO EJECUTADA`, **anótalo**:
esa es la primera línea de tu informe de cobertura, y distinguirlo de "sin hallazgos" es la
diferencia entre un analista y un generador de PDF.

## 1️⃣ Recibir la salida de varios escáneres

Vas a tener, como mínimo, cinco fuentes con cinco vocabularios distintos:

| Fuente | Qué reporta | Identificador que usa | Su punto ciego |
|---|---|---|---|
| SCA (dependencias) | CVE en paquetes de terceros | CVE + paquete + versión | No sabe si tu código llama a esa función |
| SAST (código propio) | Patrones peligrosos en tu código | Regla + archivo + línea | No sabe si la entrada es controlable |
| Secretos | Credenciales en código e historial | Tipo de secreto + commit | No sabe si el secreto sigue siendo válido |
| Dockerfile / imagen | Malas prácticas y CVE del sistema base | Regla o CVE + capa | No ve lo que hace el proceso al arrancar |
| Workflows CI/CD | Permisos, acciones sin fijar, inyección | Regla + archivo | No ve la configuración del repositorio |

**Primera decisión profesional:** no mezcles todavía. Un hallazgo de SAST y una CVE de dependencia
se priorizan con criterios distintos aunque acaben en el mismo backlog.

## 2️⃣ Normalizar y deduplicar

El objetivo es un registro único por **problema real**, no por línea de salida.

Modelo mínimo de normalización —te sirve una hoja de cálculo o un JSON como el de
[`hallazgos-ejemplo.json`](hallazgos-ejemplo.json):

```json
{
  "id_interno": "DS-2026-0042",
  "fuentes": ["trivy-fs", "bandit"],
  "tipo": "dependencia | codigo | secreto | imagen | iac | ci",
  "cve": "CVE-2021-44228",
  "componente": "log4j-core 2.14.1",
  "ubicacion": "repo-vulnerable/requirements.txt",
  "cvss": 10.0,
  "exposicion": "publica",
  "criticidad_activo": "alta",
  "estado": "nuevo | triado | ticket | excepcion | cerrado | verificado",
  "decision": "",
  "motivo": ""
}
```

Reglas de deduplicación que debes escribir y poder defender:

- **Misma CVE + mismo componente + misma versión** = un hallazgo, aunque lo reporten tres
  herramientas. Guarda las tres fuentes: coincidir eleva la confianza.
- **Misma regla + mismo archivo + misma línea** = uno. Si la línea se movió por un formateo, sigue
  siendo el mismo: dedupica por contenido, no por número de línea.
- **Un secreto en el historial y el mismo secreto en el archivo actual** = un incidente, dos
  acciones (rotar y purgar). No lo cuentes dos veces en las métricas.
- **Un mismo problema en quince repositorios** = quince hallazgos operativos, pero **una sola causa
  raíz**. Anótalo: eso no se arregla con tickets, se arregla con una plantilla.

> 📉 En este laboratorio la deduplicación reduce poco, porque el repositorio es pequeño. En un
> entorno real es donde desaparece la mayor parte del "volumen aterrador" del primer informe.

## 3️⃣ Separar los falsos positivos

Tres categorías, no dos. La tercera es la que ahorra más tiempo y la que peor se documenta:

| Categoría | Definición | Qué haces |
|---|---|---|
| **Real** | Existe y es alcanzable en este contexto | Priorizar |
| **Falso positivo** | La herramienta se equivocó | Descartar **con motivo escrito** y suprimir la regla en ese punto |
| **Real pero no aplicable** | Existe, pero aquí no es explotable | Documentar por qué, con fecha de revisión |

Ejemplos del propio laboratorio para practicar el argumento:

- Una CVE en un paquete que aparece en `requirements.txt` pero cuyo módulo vulnerable **nunca se
  importa**: real, no aplicable. El argumento tiene que apoyarse en el código, no en una intuición.
- Un hallazgo de SAST sobre una consulta construida con una constante: falso positivo *en contexto*.
- Las credenciales de `repo-vulnerable/config.py`: **son falsas a propósito** en el laboratorio,
  pero el hallazgo es correcto. Si fuera un repositorio real, la acción sería rotar primero y
  purgar después.

Cada descarte necesita cuatro datos: **quién**, **cuándo**, **por qué** y **cuándo se revisa**. Un
descarte sin registro se vuelve a triar el mes que viene: el registro *es* el producto.

## 4️⃣ Priorizar

Convierte tus hallazgos normalizados al formato de [`hallazgos-ejemplo.json`](hallazgos-ejemplo.json),
declara la **exposición real** de cada uno y pásalos por el priorizador:

```bash
python priorizar.py --hallazgos salida/mis-hallazgos.json --salida salida/plan.md
python priorizar.py --hallazgos salida/mis-hallazgos.json --sin-red     # compara
```

El orden es **KEV → EPSS → CVSS**, y sobre él actúa el factor de exposición que ninguna herramienta
puede calcular por ti:

| `exposicion` | Factor | Significado |
|---|---:|---|
| `publica` | 1.0 | Alcanzable desde internet |
| `interna` | 0.6 | Solo desde la red corporativa |
| `no-alcanzable` | 0.2 | El código afectado no se ejecuta |
| `desconocida` | 0.8 | Sin analizar — **no se asume el mejor caso** |

Añade tú la quinta señal, la que el script no conoce: la **criticidad de negocio** del servicio.
Documenta la fórmula final que uses. Da igual que sea simple; lo que se evalúa es que sea
**explícita y reproducible por otra persona**.

Dos comprobaciones honestas antes de dar la lista por buena:

1. Ejecuta `--sin-red` y compara. Si cambia el orden, tu plan **sin** KEV ni EPSS es provisional y
   debe entregarse marcado como tal, no presentarse como definitivo.
2. Mira cuántos hallazgos quedaron con `exposicion: desconocida`. Si son muchos, tu prioridad
   número uno no es parchear: es **averiguar la exposición**.

## 5️⃣ Crear tickets y acordar SLA

Un ticket que desarrollo puede ejecutar sin volver a preguntarte:

```markdown
DS-2026-0042 · Actualizar log4j-core 2.14.1 -> 2.17.1
Servicio:      facturacion-api        Dueño: Equipo Pagos
Por qué ahora: explotación activa confirmada (KEV) y el servicio está expuesto a internet
Acción:        fijar 2.17.1 en requirements.txt y regenerar el lockfile
Verificación:  el SCA deja de reportar la CVE **y** el arranque del servicio no cambia
               de comportamiento en las pruebas de integración
SLA:           7 días naturales (severidad crítica)
Notas:         se elige 2.17.1 (mínima corregida), no la última: menos riesgo de romper
```

Propuesta de SLA **para acordar con desarrollo, no para imponer**:

| Severidad efectiva | Remediación | Verificación |
|---|---:|---:|
| Crítica (KEV o expuesto con EPSS alto) | 7 días | 3 días tras el cierre |
| Alta | 30 días | 7 días |
| Media | 90 días | 30 días |
| Baja | Siguiente ciclo de mantenimiento | — |

Un SLA que desarrollo no firmó no es un SLA: es una expectativa tuya que se incumplirá en silencio.

## 6️⃣ Documentar una excepción

Cuando la corrección no es posible en plazo, la respuesta profesional no es bajar la severidad: es
**registrar la decisión**.

```markdown
Excepción EXC-2026-007
Hallazgo:       DS-2026-0051 · parser-ejemplo 0.9.0, CVE-2023-88888, sin versión corregida
Riesgo:         ejecución de código al procesar entrada no confiable (CVSS 8.1, exposición interna)
Solicita:       Equipo Pagos            Aprueba: Jefatura de Ingeniería
Motivo:         no existe versión corregida publicada; sustituir la biblioteca requiere
                reescribir el módulo de importación (estimado: 3 semanas)
Compensación:   validación estricta de entrada en el borde + el endpoint queda restringido
                a la red interna + alerta específica en el SIEM
Vence:          2026-11-30
Al vencer:      se revisa obligatoriamente; sin renovación explícita, vuelve a ser bloqueante
Revisión:       mensual, responsable del seguimiento: analista DevSecOps
```

Los cuatro elementos innegociables: **responsable, aprobador con autoridad, control compensatorio
verificable y fecha de vencimiento**. Falta uno y no es una excepción: es un riesgo aceptado en la
sombra.

## 7️⃣ Verificar la corrección

La pregunta que separa el oficio del trámite: **¿el hallazgo desapareció porque se arregló, o
porque se dejó de mirar?**

Cuatro razones habituales por las que un hallazgo desaparece sin haberse arreglado:

1. Se excluyó la ruta o el archivo del análisis.
2. Cambió la rama que se escanea.
3. El escáner falló y su salida vacía se interpretó como "limpio".
4. Se actualizó la herramienta y su regla ya no cubre ese caso.

Verificación mínima aceptable para cada cierre:

```bash
# 1. Reejecuta la capa concreta y guarda la evidencia
docker compose exec auditor ./auditar.sh deps
# 2. Comprueba que la versión instalada es la corregida (no solo el manifiesto)
docker compose exec auditor pip show <paquete>
# 3. Confirma que el alcance del análisis no cambió: mismo repo, misma rama,
#    mismas exclusiones que en la ejecución anterior
```

Y la prueba que casi nadie hace: **el control negativo**. Reintroduce temporalmente el patrón
vulnerable en una rama de prueba y confirma que el escáner vuelve a detectarlo. Si no lo detecta, tu
verificación anterior no valía nada.

## 8️⃣ Reportar riesgo y métricas

Dos vistas del mismo dato. No es duplicar trabajo: es que cada audiencia decida algo distinto.

**Vista para desarrollo** — qué te toca, en orden, con fecha:

```text
facturacion-api   1 crítica (7 d) · 3 altas (30 d) · 2 excepciones vigentes
portal-web        0 críticas      · 1 alta (30 d)
```

**Vista para dirección** — una página, con tendencia y una decisión pedida:

| Métrica | Este periodo | Anterior | Tendencia |
|---|---:|---:|---|
| Hallazgos críticos abiertos | | | |
| Edad media de la deuda (días) | | | |
| Cumplimiento de SLA | | | |
| Falsos positivos entregados a desarrollo | | | |
| Cobertura de escaneo (repos / tipos de análisis) | | | |
| Excepciones vigentes / vencidas | | | |

Cierra con la **sección de cobertura**, que es la que da credibilidad a todo lo anterior: qué capas
se ejecutaron, cuáles no y por qué, y qué **no** cubre este informe. Reutiliza
[`INFORME-PLANTILLA.md`](INFORME-PLANTILLA.md), que ya la incluye.

Por último, mapea tu evidencia contra un marco público —al menos cinco prácticas de
**NIST SP 800-218 (SSDF)** o de **OWASP SAMM**—. Es lo que convierte tu trabajo técnico en algo que
un auditor o un cliente puede aceptar.

## 🏆 Retos verificables

1. **Deduplicación defendible.** Entrega el registro normalizado y la regla de deduplicación.
   *Aceptación:* aplicando tu regla, otra persona obtiene el mismo número de hallazgos únicos.
2. **Tres descartes argumentados.** Uno falso positivo, uno "real pero no aplicable" y uno que
   dudaste y decidiste tratar como real. *Aceptación:* cada argumento cita el código o la
   configuración concreta, no una impresión.
3. **Priorización reproducible.** Máximo doce elementos con la fórmula explícita.
   *Aceptación:* alguien con tus datos y tu criterio llega al mismo orden.
4. **El experimento `--sin-red`.** *Aceptación:* explicas qué cambió y por qué el plan degradado se
   entrega marcado como provisional.
5. **Cinco tickets accionables.** *Aceptación:* incluyen criterio de verificación **escrito antes**
   de aplicar el cambio.
6. **Una excepción completa.** *Aceptación:* tiene los cuatro elementos innegociables y explicas qué
   ocurre exactamente el día del vencimiento.
7. **Verificación con control negativo.** *Aceptación:* aportas la prueba de que el escáner vuelve a
   detectar el problema cuando lo reintroduces.
8. **Informe de dos vistas.** *Aceptación:* la vista de dirección cabe en una página y termina con
   una decisión concreta que pedir.
9. **Matriz SSDF/SAMM.** *Aceptación:* cinco prácticas mapeadas a evidencia real generada por ti.
10. **Patrón, no incidente.** Identifica un hallazgo que, en una organización real, se repetiría en
    muchos repositorios. *Aceptación:* propones la corrección estructural (plantilla, biblioteca
    interna o gate) en lugar de N tickets.

## 🔗 Cómo se conecta

- 📖 Ruta completa: [Analista DevSecOps](../../rutas/devsecops-analista.md)
- 🏗️ La otra mitad del oficio:
  [Trayecto Ingeniero DevSecOps](TRAYECTO-INGENIERO-DEVSECOPS.md) — quien construye la tubería que
  tú acabas de operar
- 🗺️ [Matriz de roles SecOps y DevSecOps](../../docs/matriz-roles-secops-devsecops.md)
- 🎓 [Examen final por rol](../../docs/examen-final-por-rol.md) — el examen de Analista DevSecOps
  usa este trayecto
- 🧪 Laboratorios vecinos: [`appsec-code`](../appsec-code/README.md) ·
  [`appsec-web`](../appsec-web/README.md) · [`cloud-security`](../cloud-security/README.md) ·
  [`blue-team-soc`](../blue-team-soc/README.md)
- ⬅️ [Volver al laboratorio](README.md) · 🧪 [Índice de laboratorios](../README.md)
