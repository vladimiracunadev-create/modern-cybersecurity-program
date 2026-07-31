# Informe de auditoría del pipeline de despliegue

> Plantilla del entregable del laboratorio (reto 6). Sustituye todo lo que esté `<entre ángulos>`.
> El objetivo no es rellenar casillas: es que alguien que no estuvo en la auditoría pueda **decidir
> qué hacer primero** leyendo solo el resumen ejecutivo.

- **Repositorio auditado:** `<nombre / commit>`
- **Fecha de la auditoría:** `<AAAA-MM-DD>`
- **Auditor:** `<nombre>`
- **Herramientas y versiones:** `<osv-scanner x.y · bandit x.y · gitleaks x.y · hadolint x.y · trivy x.y · zizmor/actionlint x.y>`

## 1. Resumen ejecutivo

Tres párrafos como máximo, sin jerga. Debe responder: **¿se puede desplegar esto?**, **¿qué es lo
más urgente?** y **¿cuánto trabajo supone arreglarlo?**

| Severidad | Hallazgos | Con explotación activa (KEV) |
|---|---:|---:|
| Crítica | `<n>` | `<n>` |
| Alta | `<n>` | `<n>` |
| Media | `<n>` | `<n>` |
| Baja | `<n>` | `<n>` |

**Recomendación:** `<desplegar / desplegar con mitigaciones / no desplegar>` — `<una frase de motivo>`.

## 2. Alcance y cobertura

La sección que da credibilidad al resto del informe. Se escribe **antes** de los hallazgos, no como
apéndice.

### 2.1 Capas ejecutadas

| Capa | Herramienta | Estado | Observaciones |
|---|---|---|---|
| Composición | `<herramienta>` | `<ejecutada / no ejecutada>` | |
| SAST | | | |
| Secretos | | | |
| Dockerfile | | | |
| Contenedor | | | |
| CI/CD | | | `<cobertura parcial si se usó actionlint sin zizmor>` |

### 2.2 Fuera de alcance

Lista explícita. Cada línea es algo sobre lo que este informe **no** se pronuncia:

- Dependencias sin versión fijada: `<boto3, lxml, …>` — no resolubles por el escáner.
- Dependencias transitivas no declaradas en un lockfile.
- `<capas no ejecutadas y por qué>`
- Comportamiento en tiempo de ejecución: no se realizó análisis dinámico (DAST).
- Lógica de negocio y controles de autorización: requieren revisión manual y modelado de amenazas.

> Redacción obligatoria de la conclusión: *"no se encontraron vulnerabilidades **dentro del alcance
> descrito**"*. Nunca "no hay vulnerabilidades".

## 3. Hallazgos

Uno por bloque, **ordenados por prioridad real**, no por severidad nominal.

### H-01 · `<título corto y concreto>`

- **Capa:** `<composición / SAST / secretos / Dockerfile / contenedor / CI-CD>`
- **Ubicación:** `<archivo:línea o dependencia@versión>`
- **Severidad:** `<crítica/alta/media/baja>` · **CVSS:** `<n.n>` · **EPSS:** `<n%>` · **KEV:** `<sí/no>`
- **Exposición real:** `<¿el código afectado se ejecuta? ¿es alcanzable desde fuera? ¿hay mitigación en su sitio?>`
- **Prioridad asignada:** `<P1/P2/P3>` — `<por qué esta prioridad difiere, si difiere, de la severidad nominal>`

**Descripción.** `<qué es el fallo, en lenguaje llano>`

**Evidencia.**

```text
<salida de la herramienta o fragmento de código, recortado a lo relevante>
```

**Impacto.** `<qué consigue un atacante que lo explote — concreto, no genérico>`

**Remediación.** `<acción exacta: versión objetivo, línea a cambiar, configuración>`

**Verificación.** `<cómo se comprueba que quedó arreglado>`

## 4. Falsos positivos descartados

Documentar lo que **no** es un hallazgo demuestra criterio y evita que el siguiente auditor repita
el trabajo.

| Reportado por | Hallazgo | Motivo del descarte |
|---|---|---|
| `<herramienta>` | `<qué reportó>` | `<por qué no es explotable en este contexto>` |

## 5. Plan de remediación

Priorizado y con dueño. Sin responsable ni fecha, un plan es una lista de deseos.

| # | Acción | Hallazgos que cierra | Esfuerzo | Responsable | Fecha |
|---|---|---|---|---|---|
| 1 | `<acción>` | H-01, H-04 | `<bajo/medio/alto>` | `<área>` | `<fecha>` |

### 5.1 Remediaciones bloqueadas

Las que se intentaron y **no** se pudieron aplicar. Son hallazgos con contexto, no fracasos.

| Hallazgo | Remediación intentada | Motivo del bloqueo | Mitigación provisional |
|---|---|---|---|
| `<H-nn>` | `<subir X de 1.2 a 2.0>` | `<rompe los tests: cambio de API>` | `<qué se hace mientras tanto>` |

## 6. Recomendaciones estructurales

Más allá de los hallazgos concretos: qué cambiar para que **no vuelvan a aparecer**.

- `<adoptar lockfile con hashes>`
- `<pre-commit con detección de secretos>`
- `<fijar acciones de CI por SHA y aplicar mínimo privilegio>`
- `<cambiar la imagen base a una versión fija y mínima>`
- `<automatizar esta auditoría en el pipeline, con línea base para no bloquear por hallazgos ya aceptados>`

## 7. Anexos

- Salida completa de cada herramienta (`salida/`).
- Comandos exactos ejecutados, para que la auditoría sea **reproducible**.
