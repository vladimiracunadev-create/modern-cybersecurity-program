# Lab: Auditoría del pipeline de despliegue (DevSecOps)

Laboratorio de la **Parte 11 — DevSecOps y seguridad del SDLC** (clases 236–248). Auditas un
repositorio deliberadamente vulnerable en **ocho capas complementarias** —dependencias, código
propio, secretos, Dockerfile, contenedor, workflows de CI/CD, suplantación de paquetes e
inteligencia de explotación— y produces un informe con un plan de remediación priorizado.

Dos de esas capas vienen **implementadas** en el laboratorio, no solo explicadas:
[`priorizar.py`](priorizar.py) consulta CISA KEV y EPSS de verdad y ordena los hallazgos, y
[`typosquat.py`](typosquat.py) detecta nombres de paquete suplantados.

Es el laboratorio que responde a una pregunta que ningún otro del programa cubre: **¿qué se rompe
entre que el código sale de tu editor y llega a producción?**

> ⚠️ **Todo lo que hay en `repo-vulnerable/` es inseguro a propósito.** No lo despliegues, no lo
> ejecutes y no reutilices su código. Las credenciales de `config.py` son **falsas**: tienen el
> formato correcto y contenido inventado, para que un escáner las encuentre. El workflow de
> `repo-vulnerable/.github/workflows/deploy.yml` **no se ejecuta nunca**: GitHub Actions solo corre
> los workflows del `.github/workflows/` de la raíz del repositorio, no los de un subdirectorio.
> Practica solo aquí o en repositorios **tuyos o con autorización explícita**
> ([Clase 025](../../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)).

## 🧭 Por qué existe este laboratorio

Cuando se habla de "asegurar una aplicación" casi siempre se piensa en la aplicación: sus
inyecciones, su autenticación, su lógica. Pero una aplicación en producción es el resultado de una
**cadena de montaje**, y cada eslabón de esa cadena es una superficie de ataque con dueño,
herramientas y modos de fallo distintos:

```text
   tu código  →  dependencias  →  imagen base  →  pipeline  →  producción
       │              │               │              │
     SAST            SCA          contenedor    CI/CD + secretos
```

El dato incómodo del oficio es que **la mayor parte del código que despliegas no lo escribiste tú**.
Un proyecto Python moderno con veinte dependencias directas arrastra fácilmente doscientas
transitivas. Tu código propio —el único sobre el que hiciste revisión— puede ser una fracción muy
pequeña de lo que acaba ejecutándose.

Y hay un eslabón todavía más olvidado: **el pipeline mismo**. Un workflow de CI/CD es código con
permisos de escritura sobre el repositorio y acceso a los secretos de despliegue. Comprometerlo no
da acceso a *una* aplicación: da acceso a **todo lo que ese pipeline publica**. Por eso los ataques
a la cadena de suministro apuntan cada vez más ahí y menos a la aplicación.

De ahí la idea central del laboratorio: **ninguna herramienta ve el cuadro completo**. Cada una
mira una capa y es estructuralmente ciega a las demás. Un repositorio con "cero hallazgos" en SAST
puede tener una dependencia con explotación activa documentada, un token en el historial de git y
un workflow que cualquiera con un *fork* puede secuestrar. Aprender a **componer capas** y a
**declarar honestamente lo que quedó fuera** es el objetivo real de este ejercicio.

### En qué se diferencia de [`appsec-code`](../appsec-code/README.md)

Los dos laboratorios se complementan y no se solapan:

| | [`appsec-code`](../appsec-code/README.md) | `devsecops-pipeline` (este) |
|---|---|---|
| **Pregunta** | ¿Mi código tiene fallos? | ¿Qué despliego realmente? |
| **Alcance** | Un archivo de código propio | Repositorio completo: deps, imagen, CI/CD, secretos |
| **Herramientas** | Semgrep, Bandit | Ocho capas, ocho herramientas distintas |
| **Habilidad** | Revisión de código y SAST | Composición de capas, priorización y cobertura |
| **Entregable** | Código corregido | Informe de auditoría con plan priorizado |

Haz `appsec-code` primero si nunca has usado un SAST. Aquí el SAST es **una capa de seis**.

## 🗺️ El modelo de capas

Esta tabla es el corazón del laboratorio. La columna que de verdad importa es la última: **lo que
cada capa NO ve** — porque es lo que justifica la existencia de la siguiente.

| # | Capa | Herramienta | Qué encuentra | Qué **no** puede ver |
|---|---|---|---|---|
| 1 | **Composición** | `osv-scanner` / `pip-audit` | Vulnerabilidades conocidas de tus dependencias | Fallos en tu propio código; dependencias sin versión fijada |
| 2 | **SAST** | `bandit`, `semgrep` | Patrones inseguros en el código que escribiste | Vulnerabilidades de terceros; fallos de lógica de negocio; nada en tiempo de ejecución |
| 3 | **Secretos** | `gitleaks` | Credenciales en archivos y en el historial de git | Secretos con formato no reconocible; secretos ya rotados (falso positivo) |
| 4 | **Dockerfile** | `hadolint` | Antipatrones de construcción de la imagen | Vulnerabilidades de los paquetes que la imagen instala |
| 5 | **Contenedor** | `trivy` | CVE del sistema operativo base y sus paquetes | Cómo se usa la imagen; qué hace la aplicación dentro |
| 6 | **CI/CD** | `zizmor` / `actionlint` | Inyección de expresiones, permisos excesivos, acciones sin fijar | Lo que hagan los scripts que el workflow invoca |
| 7 | **Suplantación** | [`typosquat.py`](typosquat.py) | Paquetes con nombre casi idéntico a uno popular | Paquetes maliciosos con nombre propio, que no imitan a nadie |
| 8 | **Inteligencia** | [`priorizar.py`](priorizar.py) | Qué se explota **ya** (KEV), qué se explotará (EPSS) | Tu contexto: si ese código se ejecuta y quién lo alcanza |

Léela dos veces. La primera lectura te dice qué hace cada herramienta; la segunda te dice **por qué
hacen falta las seis**.

## 🎯 Qué vas a practicar

| Objetivo | Clases |
|---|---|
| Composición de software y riesgo de terceros (SCA) | [240](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/240-sca-dependencias-y-riesgo-de-terceros/README.md) |
| Análisis estático del código propio (SAST) | [238](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/238-sast-analisis-estatico-de-codigo/README.md) |
| Secretos en el código y prevención en `pre-commit` | [241](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md) |
| Seguridad del pipeline de CI/CD | [242](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/242-seguridad-en-pipelines-ci-cd/README.md) |
| Imágenes y contenedores seguros | [243](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/243-imagenes-y-contenedores-seguros-en-el-pipeline/README.md) · [227](../../classes/parte-10-seguridad-en-la-nube-y-contenedores/227-seguridad-de-contenedores-docker/README.md) |
| Priorización y gestión a escala | [245](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md) · [318](../../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md) |
| Cadena de suministro, SBOM y SLSA | [246](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md) |
| Filosofía *shift-left* y cultura | [236](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md) · [248](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md) |
| Automatización del análisis | [330](../../classes/parte-17-profundizacion-para-certificaciones/330-analisis-de-codigo-y-automatizacion-de-seguridad/README.md) |

## 🚀 Levantar el toolbox

```bash
cd labs/devsecops-pipeline
docker compose build
docker compose up -d
docker compose exec auditor bash
```

Ya dentro del contenedor:

```bash
./auditar.sh                    # las ocho capas
./auditar.sh sast secrets       # solo las capas que indiques
./auditar.sh typosquat priorizar # las dos capas implementadas en el propio lab
```

Las capas 7 y 8 son scripts de este laboratorio y **solo necesitan Python**, así que también se
ejecutan fuera del contenedor:

```bash
python typosquat.py repo-vulnerable/requirements.txt
python priorizar.py --hallazgos hallazgos-ejemplo.json
python priorizar.py --sin-red   # sin conectividad: usa la caché y lo declara
```

Los informes quedan en `salida/` (montada desde tu máquina, así que los puedes leer fuera del
contenedor). El repositorio objetivo se monta en **solo lectura**: una auditoría nunca debe poder
modificar lo que audita.

### Sin construir la imagen

Si prefieres no construir nada, cada capa se puede lanzar con la imagen oficial de su herramienta:

```bash
cd labs/devsecops-pipeline/repo-vulnerable

docker run --rm -v "$(pwd)":/src semgrep/semgrep semgrep --config auto /src
docker run --rm -v "$(pwd)":/src aquasec/trivy fs /src
docker run --rm -v "$(pwd)":/src zricethezav/gitleaks:latest detect --no-git --source /src -v
docker run --rm -i hadolint/hadolint < Dockerfile
```

### Si una capa no está disponible

El `Dockerfile` del toolbox descarga varios binarios en tiempo de construcción. Si tu red o un
proxy bloquea alguna descarga, la imagen **se construye igual** y `auditar.sh` marcará esa capa
como `NO EJECUTADA`. Es deliberado: prefieres un informe que admite un hueco a uno que lo esconde.

`zizmor` no viene preinstalado (se distribuye con `cargo`). Sin él, la capa 6 recurre a
`actionlint`, que valida sintaxis y detecta inyección de expresiones pero **no** cubre permisos
excesivos ni acciones sin fijar por SHA. El script te avisa de esa cobertura parcial.

## 🧭 Recorrido guiado

Haz las capas en orden. Cada una está pensada para que descubras el límite de la anterior.

### Capa 1 — Composición: lo que no escribiste tú

```bash
./auditar.sh deps
```

Abre `repo-vulnerable/requirements.txt`. Diez dependencias fijadas con `==` y **dos sin versión**.

Lo primero que debes mirar no es la lista de vulnerabilidades: es **la cobertura**. Un escáner de
composición resuelve versiones exactas. `boto3` y `lxml`, sin pin, no se pueden resolver: la
herramienta no las analiza, y si tu informe no lo dice, estás afirmando que son seguras cuando en
realidad **nunca se miraron**. Este es el error de reporte más frecuente en auditoría de
dependencias, y el que más caro sale.

Después, los hallazgos. No te digo cuántos hay ni cuáles: las bases de datos de vulnerabilidades se
actualizan cada semana, así que el resultado de hoy no será idéntico al de dentro de seis meses. Esa
inestabilidad **es parte de la lección**: un escaneo es una foto con fecha, no un certificado
permanente.

Preguntas para responder mientras lees la salida:

- ¿Cuántas de las vulnerabilidades encontradas están en dependencias **directas** y cuántas en
  **transitivas** (las que arrastran tus dependencias)?
- ¿Hay alguna que no tenga versión corregida disponible? ¿Qué haces entonces? (Pista: mitigar,
  aislar o sustituir la dependencia — la clase [245](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md) desarrolla las opciones.)

### Capa 2 — SAST: tu propio código

```bash
./auditar.sh sast
```

`repo-vulnerable/app.py` tiene once patrones inseguros marcados como `[SAST-n]`. El ejercicio **no**
es encontrarlos leyendo el archivo —los comentarios te los señalan— sino contestar tres preguntas:

1. ¿Cuáles detecta **bandit** y cuáles **semgrep**? No coinciden, y la diferencia enseña más que
   cualquiera de las dos listas por separado.
2. ¿Alguna herramienta marca algo que **no es explotable** en este contexto? Eso es un falso
   positivo, y descartarlo con argumentos es exactamente lo que hace un analista senior.
3. ¿Hay algún fallo que **ninguna** detecta? Los hay. El análisis estático razona sobre patrones
   sintácticos, no sobre la lógica de tu negocio ni sobre el flujo real de los datos en ejecución.

Ese tercer punto es la razón de existir del **DAST**
([clase 239](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/239-dast-analisis-dinamico-de-aplicaciones/README.md))
y del modelado de amenazas
([clase 237](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/237-modelado-de-amenazas-stride-y-dread/README.md)):
hay clases enteras de fallos que solo se ven ejecutando o pensando, nunca leyendo.

### Capa 3 — Secretos: el historial no se olvida

```bash
./auditar.sh secrets
```

`config.py` tiene credenciales con formato realista y contenido inventado. La detección es la parte
fácil. Lo importante es lo que viene después, y conviene interiorizarlo ahora:

> **Un secreto commiteado está comprometido.** Borrarlo en un commit posterior no lo elimina: sigue
> en el historial, en cada clon, en cada *fork* y en cada copia de seguridad. La única remediación
> válida es **rotar la credencial** en el servicio que la emitió. Reescribir el historial es
> opcional y secundario; rotar, no.

Fíjate además en el modo de escaneo. Aquí se usa `--no-git` (solo el árbol de archivos actual). Sin
esa opción, la herramienta recorre **todo el historial** — que es donde vive el secreto que alguien
"ya borró" hace dos años. Pruébalo si el directorio tiene historial propio y compara.

Y el paso que de verdad cambia las cosas: mover la detección **hacia la izquierda**, a un
`pre-commit` hook, para que el secreto no llegue nunca al historial
([clase 241](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md)).
Detectar es curar; prevenir es *shift-left*.

> 💡 **Historia real de este laboratorio.** La primera versión de `config.py` llevaba un webhook de
> Slack y una clave de Stripe con el formato exacto del proveedor. **GitHub rechazó la publicación**
> con su *push protection*, pese a que los valores eran inventados y a que este repositorio tiene una
> allowlist local que excluye `labs/`. Es la lección de la capa condensada: las defensas se
> **acumulan** (`pre-commit` → CI → plataforma), y la de la plataforma no obedece a tu configuración
> — que es justo lo que la hace útil. El detalle está en [`SOLUCION.md`](SOLUCION.md).

### Capa 4 — Dockerfile: cómo se construye la imagen

```bash
./auditar.sh dockerfile
```

`repo-vulnerable/Dockerfile` tiene diez antipatrones marcados como `[DKR-n]`. Al leer la salida de
hadolint, clasifica cada aviso en una de tres cajas:

- **Riesgo de seguridad real** — correr como `root`, un secreto en un `ENV` (queda grabado en la
  capa y lo lee cualquiera con `docker history`), instalar `netcat` y `sudo` en una imagen de
  producción.
- **Reproducibilidad** — `FROM python:latest` y `apt-get upgrade`: la imagen de mañana no será la
  de hoy, y eso rompe tu capacidad de auditar qué desplegaste.
- **Estilo o tamaño** — importantes, pero no son un hallazgo de seguridad.

Meterlo todo en el mismo saco de "hallazgos críticos" es lo que hace que los equipos de desarrollo
dejen de leer los informes de seguridad. La clasificación honesta es la que se gana la credibilidad.

### Capa 5 — Contenedor: el sistema operativo que heredas

```bash
./auditar.sh container
```

Aquí aparece lo que ninguna capa anterior podía ver: **los paquetes del sistema operativo base**.
Cuando escribes `FROM python:latest` estás heredando una distribución entera —OpenSSL, glibc,
utilidades de sistema— que tu gestor de paquetes de Python no conoce ni escanea.

La pregunta a responder: de todo lo que reporta trivy, **¿cuánto es tuyo?** Buena parte
probablemente no tenga arreglo desde tu repositorio y se resuelva cambiando la imagen base (a una
versión fija y reciente, o a una imagen mínima tipo *slim* o *distroless*). Ese es el hallazgo útil:
no una lista de CVE, sino **una decisión de arquitectura**.

### Capa 6 — CI/CD: el eslabón con las llaves

```bash
./auditar.sh workflows
```

Es la capa más importante del laboratorio y la que menos gente audita.

`repo-vulnerable/.github/workflows/deploy.yml` contiene ocho fallos marcados como `[CI-n]`. Tres
merecen que te detengas:

- **`pull_request_target` + checkout del código del PR.** Esta combinación concreta hace que el
  código de un *fork* cualquiera se ejecute con el token del repositorio base. Es el patrón que
  GitHub desaconseja de forma explícita, y ha sido la causa de compromisos reales sonados.
- **Inyección de expresiones (*template injection*).** `${{ github.event.pull_request.title }}` se
  interpola **dentro del script** antes de ejecutarlo. El título de un PR lo escribe quien abre el
  PR. La corrección es pasar el valor por una variable de entorno (`env:`) y usar `"$VARIABLE"` en
  el script, para que el shell lo trate como dato y no como código.
- **`permissions: write-all`.** Mínimo privilegio: se declara `permissions` restrictivo a nivel de
  workflow y se amplía solo en el job que lo necesite.

Y uno estructural: **`actions/checkout@v4` es una etiqueta mutable**. Quien controle ese repositorio
puede cambiar lo que ejecutas sin que tú toques nada. En un pipeline con permisos de escritura, las
acciones se fijan **por SHA completo**.

> 🔎 **Ejercicio con este mismo repositorio.** Abre [`.github/workflows/`](../../.github/workflows/)
> y comprueba cómo se fija cada cosa. Verás que el CI **fija por versión exacta**
> `markdownlint-cli2@0.23.0` —con un comentario que explica el porqué— pero que sus propias acciones
> usan etiquetas mayores mutables (`actions/checkout@v7`). ¿Es un hallazgo? Depende de **qué protege
> ese pipeline**: un workflow que solo valida documentación no es lo mismo que
> [`release-android.yml`](../../.github/workflows/release-android.yml), que firma y publica un
> artefacto. Argumenta la respuesta para cada workflow por separado. Ese razonamiento —el riesgo se
> mide por lo que el pipeline puede hacer, no por la regla en abstracto— es exactamente el que se te
> va a pedir en una auditoría real, y es lo que distingue un hallazgo de una queja genérica.

### Capa 7 — Suplantación: el paquete que no tiene CVE

```bash
./auditar.sh typosquat
# o, fuera del contenedor:
python typosquat.py repo-vulnerable/requirements.txt
```

Vuelve a mirar `requirements.txt`. Al final hay dos nombres que **no existen en PyPI**:
`requets` (por `requests`) y `python-dateutils` (por `python-dateutil`).

Aquí está el punto que justifica esta capa entera: **la capa 1 no los reporta**. Un escáner de
composición busca versiones vulnerables de paquetes conocidos; un paquete suplantado no tiene CVE,
no tiene historial y no es "una versión vulnerable de nada". **Tiene carga útil.** No se busca una
vulnerabilidad: se busca una impostura, y eso exige otra herramienta y otro criterio.

El script usa distancia de Levenshtein contra una lista de paquetes muy descargados. Es una
heurística **deliberadamente simple y con falsos positivos**, y su salida lo dice: *"ninguno es un
veredicto"*. Antes de concluir nada hay que mirar el índice — fecha de publicación, descargas,
repositorio de origen, autor, y si el paquete legítimo está *también* en la lista (señal clásica:
el atacante cuenta con que no notes que tienes los dos).

Y fíjate en lo que el propio script admite cuando no encuentra nada: que eso **no significa que las
dependencias sean legítimas**. Un paquete malicioso con nombre propio, que no imite a ninguno
conocido, es invisible para esta capa.

### Capa 8 — Inteligencia: qué se está explotando de verdad

```bash
./auditar.sh priorizar
# o, fuera del contenedor:
python priorizar.py --hallazgos hallazgos-ejemplo.json
```

Esta capa no busca hallazgos nuevos: **ordena los que ya tienes**, que es un problema distinto y
más difícil. Está desarrollado en la sección siguiente.

## ⚖️ El problema difícil: priorizar

Cuando termines las capas de descubrimiento tendrás decenas de hallazgos. Aquí es donde el
laboratorio deja de ser técnico y se vuelve profesional: **no puedes arreglarlo todo, y fingir que
sí es lo que hace inútil a un informe**.

Tres señales, que responden a preguntas distintas y no son intercambiables:

| Señal | Pregunta que responde | Límite |
|---|---|---|
| **CVSS** | ¿Cuán grave sería si se explotara? | Es una nota teórica y descontextualizada. Una crítica en un componente que no usas no es crítica **para ti** |
| **EPSS** | ¿Qué probabilidad hay de que se explote pronto? | Probabilístico: describe tendencias del ecosistema, no tu entorno |
| **CISA KEV** | ¿Se está explotando **ya**, de forma documentada? | Solo cubre lo confirmado por la agencia: no estar en KEV no significa estar a salvo |

La regla práctica que usan los equipos maduros: **KEV primero** (explotación activa confirmada),
después **EPSS alto** aunque el CVSS sea medio, y por último el CVSS crudo. Y sobre todo: la
**exposición real**. Una vulnerabilidad crítica en una función que tu código nunca llama tiene menos
prioridad que una media en la ruta de autenticación de tu API pública.

Ese último ajuste —el contexto— no lo pone ninguna herramienta. Lo pones tú, y es exactamente por lo
que te pagan. La clase [245](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md)
desarrolla el modelo completo y la [318](../../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md)
lo convierte en un programa con SLAs.

### Implementado: `priorizar.py`

Esta regla no se queda en la teoría. [`priorizar.py`](priorizar.py) la ejecuta: descarga el catálogo
**CISA KEV**, consulta la **API de EPSS** de FIRST, aplica el **factor de exposición** que tú
declaras y emite el checklist ordenado.

```bash
python priorizar.py --hallazgos hallazgos-ejemplo.json
```

Los datos de ejemplo están elegidos para que veas el efecto en una sola pantalla:

| Hallazgo | CVSS | Exposición | Resultado |
|---|---|---|---|
| Heartbleed (CVE-2014-0160) | 7.5 | pública | **P1** — está en KEV: explotación confirmada |
| Log4Shell (CVE-2021-44228) | 10.0 | pública | **P1** — KEV + EPSS altísimo |
| CVE inventado, crítico | 9.8 | **no alcanzable** | **P4** — el código afectado no se ejecuta |

Léelo dos veces: una vulnerabilidad de **7.5 acaba por encima de una de 9.8**. Si ordenas por CVSS
—que es lo que hace la mayoría— trabajas primero en la que nadie está explotando y que además no
puedes alcanzar. Ese es el coste real de priorizar mal, y por eso las tres señales no son
intercambiables.

Dos decisiones del script que conviene entender, porque son criterio profesional y no detalles de
implementación:

- **Una señal no consultada no vale cero.** Si no hay red, el informe encabeza con "NO DISPONIBLE"
  y marca el orden como **provisional**. Es la misma regla que `auditar.sh` aplica a las capas: *sin
  hallazgos* y *no ejecutada* nunca se mezclan.
- **La etiqueta P1–P4 usa el CVSS ajustado**, el mismo que el orden. Una etiqueta que contradice el
  orden de la lista destruye la confianza en el informe entero.

### Minimal blast radius: subir lo mínimo, no lo último

Cuando hay varias versiones que corrigen un fallo, `priorizar.py` propone **la más baja**, no la más
reciente. Con `[2.17.1, 2.16.0, 2.15.0]` propone `2.15.0`.

Es contraintuitivo hasta que lo has sufrido: subir a la última disponible arrastra cambios de API,
dependencias nuevas y comportamiento distinto que **nadie pidió**, y convierte una corrección de
seguridad de diez minutos en una migración de dos días — o en un build roto un viernes. Se sube lo
imprescindible para cerrar la vulnerabilidad. **Modernizar es otra tarea**, con otro calendario y
otro riesgo, y se planifica aparte.

## 📐 Cobertura honesta: la sección que casi nadie escribe

Todo informe de auditoría debe declarar **qué quedó fuera**. En este laboratorio, como mínimo:

- Las dependencias **sin versión fijada** (`boto3`, `lxml`): no analizables por el escáner.
- Las dependencias **transitivas** no reflejadas en un *lockfile*.
- Cualquier capa que el script marcó como `NO EJECUTADA`.
- La capa 6 si corrió con `actionlint` en lugar de `zizmor` (cobertura parcial).
- Todo lo que solo se ve **en ejecución**: DAST, pruebas de lógica de negocio, comportamiento real.

Un informe que dice "no se encontraron vulnerabilidades" sin declarar su alcance no es un informe
optimista: es un informe **incorrecto**. La frase profesional es *"no se encontraron vulnerabilidades
dentro del alcance descrito"*, y el alcance va escrito.

## 🔧 Remediar sin romper producción

Subir una dependencia arregla una vulnerabilidad y, a veces, rompe la aplicación. El procedimiento
seguro, y el que debes automatizar:

1. **Copia de seguridad** del manifiesto.
2. **Aplica** la subida de versión.
3. **Instala** las dependencias.
4. **Ejecuta los tests**.
5. Si fallan → **revierte** y registra el hallazgo como *"remediación bloqueada"*, con el motivo.
6. Si pasan → mantén el cambio y anota *"verificado: tests OK"*.

El paso 5 es el que distingue un proceso profesional. Una subida bloqueada **no es un fracaso**: es
un hallazgo con dueño y contexto —"esta dependencia no se puede actualizar sin migrar la API; se
propone mitigación X mientras tanto"—. Ocultarla o forzar el cambio sin verificar es cómo se rompe
producción un viernes.

## 🏆 Retos verificables

1. **Matriz de cobertura.** Construye una tabla `hallazgo → capa que lo detectó`. *Aceptación:*
   incluye al menos un hallazgo que **solo** una capa haya visto, y explica por qué las demás eran
   ciegas a él.
2. **Falsos positivos con argumento.** Encuentra al menos uno y justifica en dos frases por qué no es
   explotable **en este contexto**. *Aceptación:* el argumento debe apoyarse en el código, no en una
   opinión.
3. **Falsos negativos.** Identifica un fallo real de `app.py` que ninguna herramienta detectó y
   explica el límite técnico que lo causa. *Aceptación:* nombrar la categoría de análisis que sí lo
   encontraría (DAST, revisión manual, modelado de amenazas).
4. **Corrige el workflow.** Reescribe `deploy.yml` eliminando los ocho fallos. *Aceptación:* sin
   `pull_request_target` con checkout del PR; `permissions` mínimo y explícito; acciones fijadas por
   SHA; el título del PR pasado por `env:` y citado; sin secretos en logs ni artefactos; sin
   `curl | bash`.
5. **Endurece el Dockerfile.** *Aceptación:* base con versión fija, sin `apt-get upgrade`, sin
   paquetes innecesarios, sin secretos en `ENV`, usuario sin privilegios, `CMD` en forma exec, y
   `.dockerignore` que excluya `.git`.
6. **Informe priorizado.** Redacta el informe usando [`INFORME-PLANTILLA.md`](INFORME-PLANTILLA.md),
   con los hallazgos ordenados por KEV → EPSS → CVSS ajustado por exposición, y **la sección de
   cobertura completa**. *Aceptación:* un lector no técnico entiende qué hacer primero y por qué.
7. **Prioriza tus propios hallazgos.** Convierte la salida de la capa 1 al formato de
   [`hallazgos-ejemplo.json`](hallazgos-ejemplo.json), **declara la exposición real de cada uno** y
   pásalo por `priorizar.py`. *Aceptación:* justificar en una frase la exposición asignada a cada
   hallazgo — es el único dato que ninguna herramienta puede deducir, y el que más cambia el orden.
8. **Rompe el orden a propósito.** Ejecuta `priorizar.py --sin-red` y compara con la ejecución
   normal. *Aceptación:* explicar qué cambió, y por qué un plan sin KEV ni EPSS debe entregarse
   marcado como provisional en vez de presentarse como definitivo.
9. **Caza al impostor.** Ejecuta `typosquat.py` y, para cada candidato, decide si es suplantación o
   falso positivo. *Aceptación:* indicar qué comprobaste en el índice de paquetes (fecha, descargas,
   origen) y explicar por qué la capa 1 no reportó ninguno de los dos.
10. **Shift-left (avanzado).** Convierte la auditoría en prevención: un `pre-commit` que bloquee
    secretos y un workflow de CI que falle ante hallazgos nuevos, pero **no** ante los preexistentes
    ya aceptados. *Aceptación:* explicar cómo gestionas la línea base sin volver el pipeline inútil.

Las respuestas y el detalle de cada capa están en [`SOLUCION.md`](SOLUCION.md) — míralo **después**
de intentarlo.

## ⚠️ Errores comunes

- **Confundir "sin hallazgos" con "no escaneado".** El error más caro del informe, y por eso el
  script los separa siempre.
- **Reportar la salida cruda de la herramienta.** Un volcado de 300 líneas no es un informe. El
  trabajo es filtrar, contextualizar y priorizar.
- **Tratar todo hallazgo como crítico.** Es la forma más rápida de que desarrollo deje de leerte.
- **Arreglar el secreto borrándolo del código.** Sin rotar la credencial, sigue comprometida.
- **Subir todas las versiones de golpe.** Sin verificación por paso, cuando algo se rompa no sabrás
  cuál de los quince cambios fue.
- **Auditar la aplicación y olvidar el pipeline.** El pipeline tiene las llaves de todo lo que
  publica: es el objetivo de mayor valor, no el de menor.
- **Creer que el escaneo caduca solo.** Un repositorio limpio hoy tiene vulnerabilidades nuevas en
  tres meses sin haber cambiado una línea. Por eso se automatiza y se repite.

## 🔗 Cómo se conecta con el resto del programa

- **Antes:** [`appsec-code`](../appsec-code/README.md) para el SAST puro, y
  [`appsec-web`](../appsec-web/README.md) para entender qué explota el atacante.
- **Después:** [`cloud-security`](../cloud-security/README.md) lleva el mismo enfoque de auditoría a
  la infraestructura donde acaba desplegándose todo esto.
- **Rutas que lo usan:** [AppSec](../../rutas/appsec.md) ·
  [Security Engineer / SecOps](../../rutas/secops-engineer.md) ·
  [Cloud Security](../../rutas/cloud-security.md) ·
  [Gestión de Vulnerabilidades](../../rutas/gestion-vulnerabilidades.md)
- **Certificaciones:** dominios de herramientas y análisis de **CompTIA PenTest+** y **CySA+**, y
  *Software Development Security* de **CISSP**.

## 📚 Referencias

- OSV — <https://osv.dev/> · CISA KEV — <https://www.cisa.gov/known-exploited-vulnerabilities-catalog> · EPSS — <https://www.first.org/epss/>
- Trivy — <https://trivy.dev/> · gitleaks — <https://github.com/gitleaks/gitleaks> · hadolint — <https://github.com/hadolint/hadolint>
- Bandit — <https://bandit.readthedocs.io/> · Semgrep — <https://semgrep.dev/>
- zizmor — <https://docs.zizmor.sh/> · actionlint — <https://github.com/rhysd/actionlint>
- Seguridad de GitHub Actions — <https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions>
- OWASP Top 10 CI/CD Security Risks — <https://owasp.org/www-project-top-10-ci-cd-security-risks/>
- SLSA (niveles de integridad de la cadena de suministro) — <https://slsa.dev/>
- Parte 11 del programa — [índice de clases](../../classes/README.md)
