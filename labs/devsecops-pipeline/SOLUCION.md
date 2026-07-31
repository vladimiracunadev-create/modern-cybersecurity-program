# Solución — Auditoría del pipeline de despliegue

> Léelo **después** de haber intentado el [recorrido guiado](README.md). Aquí está el detalle de
> cada hallazgo plantado, qué capa lo ve, por qué, y cómo se corrige.

## Capa 1 — Composición (dependencias)

**Deliberadamente no se listan aquí CVE concretas.** Las diez dependencias fijadas de
`requirements.txt` son versiones antiguas con vulnerabilidades conocidas, pero el conjunto exacto
que reporte tu escáner **depende del día**: las bases de datos incorporan entradas nuevas cada
semana y reclasifican severidades. Un solucionario con CVE fijas estaría obsoleto en meses y te
enseñaría lo contrario de lo que importa.

Lo que **sí** debe aparecer siempre en tu análisis, y es lo evaluable:

| Comprobación | Resultado esperado |
|---|---|
| `boto3` y `lxml` aparecen en el informe | **No.** No tienen versión fijada: el escáner no puede resolverlas |
| Tu informe las menciona igualmente | **Sí**, en la sección de cobertura, como "fuera de alcance" |
| Distingues dependencias directas de transitivas | Sí: `requirements.txt` solo declara directas |
| Alguna vulnerabilidad sin versión corregida | Probable. Opciones: mitigar, aislar, sustituir o aceptar con justificación |

La corrección de fondo no es "subir versiones", sino **adoptar un lockfile** con versiones y hashes
(`pip-compile`, `poetry.lock`, `uv.lock`). Sin él, lo que instalas en producción no es
necesariamente lo que escaneaste — y esa brecha es indefendible ante un auditor.

## Capa 2 — SAST (código propio)

Los once patrones de `app.py`, con su corrección:

| # | Patrón inseguro | Corrección |
|---|---|---|
| SAST-1 | SQL por concatenación de cadenas | Consultas parametrizadas: `cursor.execute("... WHERE nombre = ?", (nombre,))` |
| SAST-2 | `subprocess` con `shell=True` sobre entrada del usuario | Lista de argumentos y `shell=False`; validar el destino contra una allowlist |
| SAST-3 | `eval()` sobre entrada del usuario | Eliminar. Si hace falta evaluar expresiones, usar un parser acotado (`ast.literal_eval` o una gramática propia) |
| SAST-4 | `pickle.loads()` sobre datos remotos | Nunca deserializar formatos que ejecutan código. Usar JSON con esquema validado |
| SAST-5 | `yaml.load()` sin Loader seguro | `yaml.safe_load()` |
| SAST-6 | MD5 para contraseñas | Argon2id, scrypt o bcrypt, con sal por usuario |
| SAST-7 | `random` para un token de sesión | `secrets.token_urlsafe()` (CSPRNG) |
| SAST-8 | `verify=False` en TLS | Verificación activada; si es una CA interna, montar su bundle |
| SAST-9 | Path traversal en `open()` | Normalizar con `os.path.realpath` y comprobar que el resultado sigue dentro del directorio permitido |
| SAST-10 | Secretos leídos del código fuente | Variables de entorno o gestor de secretos (Vault, KMS, el del proveedor) |
| SAST-11 | `debug=True` y `host="0.0.0.0"` | `debug=False` y servidor WSGI real (gunicorn/uWSGI) detrás de un proxy |

**Cobertura esperada.** Bandit y Semgrep no coinciden. Bandit es específico de Python y reconoce
bien las llamadas peligrosas de la librería estándar (SAST-2 a SAST-8, SAST-11). Semgrep aporta
reglas de la comunidad y suele ser más fuerte en patrones de framework y flujo de datos. **La
intersección no es el total: la unión tampoco.** Documentar esa diferencia es el reto 1.

**Falsos negativos que debes encontrar (reto 3).** El más claro es SAST-9: muchos analizadores no
siguen el flujo desde `request.args` hasta `open()` a través de `os.path.join`, porque exige
análisis de propagación (*taint analysis*) y no un simple patrón sintáctico. También suele escaparse
la ausencia total de autenticación y autorización en los endpoints: **no hay ningún patrón inseguro
que detectar — el fallo es lo que no está**, y ninguna herramienta estática reporta ausencias de
diseño. Eso es terreno de modelado de amenazas
([clase 237](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/237-modelado-de-amenazas-stride-y-dread/README.md)).

## Capa 3 — Secretos

`config.py` contiene varias credenciales, y no todas se detectan igual de bien:

| Valor | Cómo se detecta | Fiabilidad |
|---|---|---|
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | Patrón de proveedor (`AKIA…`) | Alta: lo pilla cualquier herramienta |
| `DB_PASSWORD` | Entropía + nombre de variable sospechoso | Media |
| `INTERNAL_API_TOKEN` | Solo entropía: no tiene prefijo conocido | **Baja** |
| `SECRET_KEY = "dev"` | Ninguna: es corto y de baja entropía | **Casi nula** |
| `SLACK_WEBHOOK` / `STRIPE_API_KEY` | Neutralizados (ver más abajo) | — |

Ese es el límite estructural de la capa: **detecta lo que tiene forma de secreto conocido**. Un
token propio de tu empresa, sin prefijo ni formato distintivo, puede pasar desapercibido — y
`SECRET_KEY = "dev"` no lo marca nadie, pese a ser un fallo grave en producción (firma de sesiones
predecible). Encontrar ese último es trabajo de **revisión humana**, no de escáner.

Corrección, en orden:

1. **Rotar** todas las credenciales expuestas en el servicio emisor. Es el paso obligatorio.
2. Sacarlas del código: variables de entorno o gestor de secretos.
3. `pre-commit` con detección de secretos, para que no vuelva a ocurrir.
4. Opcionalmente, reescribir el historial — útil, pero **nunca sustituye a rotar**.

### La capa que no controlas: protección del lado del servidor

Hay una defensa más, y este laboratorio se topó con ella al publicarse. La primera versión de
`config.py` llevaba un webhook de Slack y una clave de Stripe con el formato exacto del proveedor.
**GitHub rechazó el push**: su *push protection* analiza cada envío y bloquea los patrones de
secreto de alta confianza.

Lo interesante es lo que ocurrió pese a que:

- los valores eran **inventados** y no autenticaban contra nada;
- el repositorio tiene una **allowlist local** (`.gitleaks.toml`) que excluye `labs/`
  precisamente porque contiene material didáctico con secretos de ejemplo.

Nada de eso importó, y **está bien que no importe**: una protección que se puede desactivar desde
el repositorio que protege no es una protección. De ahí tres conclusiones aplicables a tu trabajo:

1. **Las capas se acumulan, no se sustituyen.** `pre-commit` (tu máquina) → escáner en CI (tu
   pipeline) → *push protection* (la plataforma). Cada una atrapa lo que la anterior dejó pasar, y
   cada una está bajo un control distinto.
2. **Tu configuración local no es la última palabra.** Si dependes de una allowlist para que tu
   pipeline pase, tienes un problema de diseño, no de configuración.
3. **Los detectores de alta confianza van por formato de proveedor.** Por eso Slack y Stripe se
   bloquearon y, en cambio, `DB_PASSWORD`, `SECRET_KEY = "dev"` e `INTERNAL_API_TOKEN` no: no
   encajan en ningún patrón conocido. **El secreto propio de tu empresa es el que más fácil se
   escapa**, y es tan peligroso como el de un proveedor famoso.

Los dos valores quedaron neutralizados en el archivo, con la explicación dentro. La versión
"realista" de ese fallo la puedes reproducir en un repositorio local tuyo, sin publicar.

## Capa 4 — Dockerfile

| # | Antipatrón | Categoría | Corrección |
|---|---|---|---|
| DKR-1 | `FROM python:latest` | Reproducibilidad | Etiqueta fija: `python:3.12.8-slim` |
| DKR-2 | `apt-get upgrade` en la imagen | Reproducibilidad | Eliminar; actualizar cambiando la imagen base |
| DKR-3 | Sin `--no-install-recommends` ni limpieza | Tamaño / superficie | Añadir la opción y `rm -rf /var/lib/apt/lists/*` en el mismo `RUN` |
| DKR-4 | Instala `curl`, `netcat`, `vim`, `sudo` | **Seguridad** | Quitar todo lo que no se use en ejecución: son herramientas listas para el atacante |
| DKR-5 | `COPY . /app` | **Seguridad** | `.dockerignore` con `.git`, credenciales y artefactos locales |
| DKR-6 | `pip install` sin fijar ni verificar | Cadena de suministro | Lockfile con hashes y `--require-hashes` |
| DKR-7 | Secreto en `ENV` | **Seguridad (grave)** | Nunca. Queda en la capa y lo lee `docker history`. Inyectar en tiempo de ejecución |
| DKR-8 | Sin `USER`: corre como root | **Seguridad** | `RUN useradd ...` + `USER app` |
| DKR-9 | Puerto de depuración expuesto | **Seguridad** | Eliminar `EXPOSE 5678` |
| DKR-10 | `CMD` en forma shell | Operación | Forma exec: `CMD ["python", "app.py"]`, para que el proceso reciba las señales |

La clasificación en tres cajas —seguridad, reproducibilidad, estilo— **es el ejercicio**. Un informe
que presenta DKR-10 con la misma urgencia que DKR-7 pierde credibilidad ante quien tiene que
arreglarlo.

## Capa 5 — Contenedor

Trivy reporta las CVE de los paquetes del sistema operativo base. Con `python:latest` la lista suele
ser larga, y la conclusión útil casi nunca es "parchear cada una":

- La mayoría **no se arregla desde tu repositorio**: vienen en la imagen base.
- La acción correcta es **cambiar de imagen base** — a una versión fija y reciente, a una variante
  `-slim`, o a una imagen mínima (*distroless*) que ni siquiera incluya shell.
- Reducir la imagen elimina vulnerabilidades **por eliminación de superficie**, no por parcheo. Es
  la remediación más eficiente y la menos aplicada.

Comprueba también cuántos de esos paquetes usa realmente tu aplicación. Casi siempre: ninguno.

## Capa 6 — CI/CD

| # | Fallo | Corrección |
|---|---|---|
| CI-1 | `pull_request_target` | Usar `pull_request`. Si se necesita el token, separar en dos workflows y no ejecutar código del PR |
| CI-2 | `permissions: write-all` | `permissions: contents: read` a nivel de workflow; ampliar solo en el job que lo requiera |
| CI-3 | `actions/checkout@v4` (etiqueta mutable) | Fijar por SHA completo de commit |
| CI-4 | Checkout del `head.sha` del PR bajo `pull_request_target` | Eliminar. Es la combinación explícitamente desaconsejada |
| CI-5 | Interpolación de `${{ }}` dentro de `run` | Pasar por `env:` y usar `"$VARIABLE"` citada en el script |
| CI-6 | Secreto escrito a log y a artefacto | No volcar secretos; `curl` sin `-k`; no subir logs con credenciales |
| CI-7 | `curl \| bash` | Descargar a archivo, verificar checksum o firma, y ejecutar |
| CI-8 | Artefacto con el log que contiene el token | Eliminar, o filtrar el contenido antes de subirlo |

El fallo con más impacto real es **CI-5** combinado con **CI-2**: la inyección permite ejecutar
comandos y los permisos totales determinan hasta dónde llega esa ejecución. Por separado son graves;
juntos son un compromiso completo del repositorio.

Ejemplo de la corrección de CI-5:

```yaml
      - name: Registrar el cambio
        env:
          PR_TITLE: ${{ github.event.pull_request.title }}
        run: |
          echo "Desplegando: $PR_TITLE"
```

La diferencia es sutil y decisiva: en la versión insegura, el título se **sustituye en el texto del
script** antes de ejecutarlo, así que su contenido se interpreta como comandos. En la versión
corregida, llega como **valor de una variable** y el shell lo trata como dato.

## Mapa completo hallazgo → capa

Este es el entregable del reto 1. Las casillas que importan son las que tienen **una sola marca**:
prueban por qué hacen falta las seis capas.

| Hallazgo | Deps | SAST | Secretos | Dockerfile | Contenedor | CI/CD |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| Dependencia vulnerable | ✅ | | | | parcial | |
| `eval()` en el código | | ✅ | | | | |
| Clave de AWS en `config.py` | | parcial | ✅ | | | |
| Imagen base sin versión | | | | ✅ | | |
| CVE del sistema operativo base | | | | | ✅ | |
| Secreto en `ENV` del Dockerfile | | | parcial | ✅ | ✅ | |
| Inyección en el workflow | | | | | | ✅ |
| Acción sin fijar por SHA | | | | | | ✅ |
| Falta de autenticación en los endpoints | | | | | | |

La última fila no la marca **ninguna** capa. Es el recordatorio final del laboratorio: la
automatización cubre los fallos que tienen forma reconocible; **los fallos de diseño siguen siendo
tuyos**.
