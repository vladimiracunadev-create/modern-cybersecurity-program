# 🏗️ Ingeniero DevSecOps (pipeline, cadena de suministro y policy as code)

> El rol que **construye la capacidad**: pipelines CI/CD seguros, análisis automatizado en cada
> etapa, puertas de bloqueo proporcionales al riesgo, SBOM, firma y procedencia de artefactos,
> policy as code, identidades efímeras y gestión de secretos. Su producto no es un informe: es que
> **el camino seguro sea el camino fácil** para cientos de personas que desarrollan.
>
> También aparece en ofertas como **Especialista DevSecOps** o *DevSecOps Platform Engineer*: la
> sección «Especialista DevSecOps», más abajo, explica cómo saber qué perfil pide realmente cada una.
>
> **Nivel de entrada:** semi-senior/senior; exige oficio real de ingeniería · **Foco:** CI/CD, SAST/DAST/SCA automatizados, secretos, IaC, contenedores y Kubernetes, SBOM, firma y SLSA, OPA/Rego, mínimo privilegio en el pipeline · **Certificación faro:** ninguna encaja del todo; CySA+ como base y CKS si el terreno es Kubernetes

## 🧭 Qué es y por qué importa

Un pipeline de despliegue es, para la mayoría de las organizaciones, **el sistema con más privilegio
y menos vigilancia** que existe: puede escribir en producción, tiene credenciales de nube, firma lo
que se ejecuta y casi nadie lo audita. El Ingeniero DevSecOps es quien lo convierte en una
infraestructura defendible **y** en una plataforma que la gente quiere usar.

Su trabajo tiene cuatro capas:

- **Controles automatizados en el ciclo.** SAST, DAST y SCA integrados donde corresponde, escaneo de
  secretos, análisis de IaC, de Dockerfile y de imágenes, y validación de manifiestos de Kubernetes.
  Ejecutándose solos, en el momento correcto, con resultados accionables.
- **Decisión automatizada.** Puertas de seguridad **proporcionales**: qué bloquea el *merge*, qué
  bloquea el despliegue a producción, qué solo avisa. Un gate mal calibrado es peor que ninguno,
  porque se desactiva y ya no vuelve.
- **Integridad de la cadena de suministro.** SBOM (CycloneDX o SPDX), firma de artefactos y
  procedencia verificable, niveles de **SLSA**, y verificación en el punto de despliegue: que lo que
  corre en producción sea exactamente lo que se construyó desde el código que se revisó.
- **Seguridad del propio pipeline.** Identidades efímeras (OIDC en lugar de credenciales de larga
  vida), mínimo privilegio por *job*, acciones y dependencias fijadas por versión o suma de
  verificación, aislamiento de los *runners* y gestión seria de secretos.

Importa porque es la vía con **mejor relación entre esfuerzo y riesgo evitado** del sector: un
control bien puesto en el pipeline protege todo lo que pasa por él, para siempre, sin depender de
que alguien se acuerde.

### Qué problema resuelve

Dos problemas a la vez. El primero, **escala**: no hay equipo de seguridad capaz de revisar a mano
lo que producen doscientas personas desarrollando; hay que instrumentar el ciclo. El segundo,
**incentivos**: si lo seguro es lento y molesto, la gente lo rodea. Este rol resuelve ambos
convirtiendo la seguridad en **camino por defecto** — plantillas, bibliotecas internas, workflows
reutilizables y valores predeterminados sensatos.

## 🚫 Qué NO es este rol

- **No es quien triaja los hallazgos.** Construye la tubería que los produce y los enruta; quien los
  analiza, prioriza y negocia es el [Analista DevSecOps](devsecops-analista.md). Cuando una sola
  persona hace las dos cosas, la organización debería saber que está pidiendo dos puestos.
- **No es un DevOps con un escáner.** El DevOps optimiza para entrega y disponibilidad; aquí se
  añade un modelo de amenazas del propio pipeline y decisiones de riesgo. Comparten herramientas,
  no criterios.
- **No es Cloud Security.** No es el dueño de la postura de la cuenta de nube, del CSPM ni de la
  detección en la nube: eso es [Cloud Security Engineer](cloud-security.md). Sí es el dueño de lo
  que el pipeline **hace** con esa nube.
- **No es AppSec.** No hace modelado de amenazas de la aplicación ni revisión de código de diseño.
  Automatiza las comprobaciones que [AppSec](appsec.md) define.
- **No es el policía del despliegue.** Si el rol se vive como "el que bloquea", ha fracasado. Se
  mide por adopción, no por número de bloqueos.

### Frente a los perfiles vecinos

- Frente al [Analista DevSecOps](devsecops-analista.md): **construir** frente a **operar**. Tú
  entregas la capacidad y las métricas; él las convierte en decisiones y en tickets. La frontera
  práctica: si el entregable es código o configuración que queda corriendo, es tuyo; si el
  entregable es una decisión documentada, es suyo.
- Frente al [Cloud Security Engineer](cloud-security.md): **el proceso de construcción y entrega**
  frente a **la plataforma donde eso corre**. Tú aseguras que la imagen se construya, se firme y se
  verifique; él, que el clúster y la cuenta donde aterriza estén bien configurados, vigilados y
  segmentados. Colaboráis en IaC, contenedores y Kubernetes, que es territorio compartido.
- Frente al [AppSec Engineer](appsec.md): AppSec define **qué** hay que comprobar y por qué (ASVS,
  modelado de amenazas, requisitos); tú defines **cómo** se comprueba automáticamente y en qué punto
  del ciclo.
- Frente al [Ingeniero SecOps / Security Engineer](secops-engineer.md): misma mentalidad de
  ingeniería, distinto dominio. Ese rol automatiza la **operación** (EDR, flota, identidades,
  respuesta); este automatiza la **construcción y la entrega**. Muchas carreras pasan por los dos.
- Frente a **Platform Engineering**: tu trabajo suele vivir dentro de esa plataforma interna. Si en
  la empresa existe un equipo de plataforma, tu producto es un conjunto de piezas suyas — no un
  silo aparte.

## 🏷️ "Especialista DevSecOps": la denominación alternativa

**Especialista DevSecOps** no es un tercer rol: es un **título comercial** que las ofertas usan de
forma ambigua. Puede designar el perfil de análisis, el de ingeniería o —lo más frecuente en
empresas medianas— **los dos en la misma persona**.

La regla práctica: **el contenido real de la oferta manda sobre el título**. Léela buscando el verbo.

| Lo que dice la oferta | Perfil real |
|---|---|
| "analizar hallazgos", "priorizar", "gestionar el backlog", "reportar métricas", "coordinar con desarrollo" | [Analista DevSecOps](devsecops-analista.md) |
| "implementar pipelines", "integrar herramientas", "automatizar", "definir políticas como código", "firmar artefactos", "gestionar secretos" | Ingeniero DevSecOps (esta ruta) |
| Ambas listas, con una sola vacante | Perfil **mixto** — pide alcance y prioridades en la entrevista, y negocia el sueldo por las dos |
| "modelado de amenazas", "revisión de código", "ASVS", "formar a desarrolladores" | [AppSec Engineer](appsec.md) |
| "CSPM", "IAM de la nube", "hardening del clúster", "detección en la nube" | [Cloud Security Engineer](cloud-security.md) |

Si la oferta pide **las dos listas completas más la nube más AppSec**, no es un especialista: es un
equipo entero mal presupuestado. Saber detectarlo también es parte del oficio.

## 🪜 Nivel de entrada y prerrequisitos

Es un rol de **ingeniería de verdad**. No es una puerta de entrada al sector.

- **Imprescindible:** Git y flujos de trabajo de equipo con soltura; al menos un lenguaje de
  programación en el que puedas escribir y mantener herramientas (Python es la apuesta segura);
  Linux; Docker y contenedores; entender qué hace un CI/CD y por qué falla.
- **Muy recomendable:** experiencia previa como desarrollador, DevOps, SRE o
  [Ingeniero SecOps](secops-engineer.md). Es la vía de entrada dominante.
- **Deseable:** Kubernetes, Terraform, alguna nube pública y experiencia manteniendo algo que otras
  personas usan a diario.
- **No hace falta:** ser pentester ni experto en explotación. Sí entender los ataques a la cadena de
  suministro y al propio pipeline para diseñar contra ellos.

En el programa: **Parte 0 completa** (Python, Git, Docker), y las Partes 10 y 11 como columna
vertebral.

## 🧾 Responsabilidades habituales

- **Diseñar y mantener pipelines CI/CD seguros** y las plantillas o workflows reutilizables que
  usan los demás equipos.
- **Integrar SAST, DAST y SCA** en el punto correcto del ciclo, con resultados en formato consumible
  (por ejemplo SARIF) y sin duplicar trabajo entre herramientas.
- **Escaneo de secretos** en código, historial y artefactos, con bloqueo previo al *commit* y
  proceso de rotación cuando algo se filtra.
- **Análisis de IaC, Dockerfile, imágenes y manifiestos de Kubernetes** dentro del pipeline.
- **Definir las puertas de seguridad**: qué bloquea, qué avisa, con qué umbral y con qué vía de
  excepción **auditable y temporal**.
- **Generar y publicar SBOM** (CycloneDX o SPDX) por artefacto, y conservarlo donde sirva durante un
  incidente.
- **Firmar artefactos y emitir procedencia**; verificar la firma en el punto de despliegue. Elevar
  el nivel de **SLSA** de forma incremental y medible.
- **Policy as code** con OPA/Rego y validación en CI (por ejemplo con Conftest), para que las reglas
  sean revisables, versionadas y probadas como cualquier otro código.
- **Endurecer el propio pipeline**: identidades efímeras (OIDC), permisos mínimos por *job*,
  dependencias y acciones fijadas, aislamiento de *runners*, protección de ramas y entornos.
- **Gestión de secretos**: bóveda, rotación, inyección en tiempo de ejecución y erradicación de
  credenciales de larga vida.
- **Observabilidad y retroalimentación desde producción** hacia el ciclo de desarrollo.
- **Rutas seguras por defecto** para desarrollo: plantillas, bibliotecas internas, valores
  predeterminados y documentación que se pueda seguir sin preguntar.

## 🗓️ Un día en el puesto

- **Revisión de lo que se rompió de noche.** Un pipeline falla en veinte repositorios porque un
  escáner sacó versión nueva con reglas nuevas. Primera lección del oficio: **fija las versiones**.
  Segunda: ten un camino de reversión listo, porque hoy vas a usarlo.
- **Un despliegue bloqueado.** Un equipo no puede desplegar por una vulnerabilidad en una imagen
  base. Miras si el gate está bien calibrado, ofreces la imagen base actualizada que ya mantienes y,
  si no llega a tiempo, tramitas una **excepción con vencimiento** — no un "desactívalo un rato".
- **Construcción.** El bloque bueno del día: implementas la firma de artefactos con verificación en
  el despliegue, o migras un repositorio de credenciales estáticas a **OIDC con identidad efímera**,
  o escribes la política Rego que impide desplegar un contenedor como *root*.
- **Revisión de código de otros.** Revisas un *pull request* de infraestructura: un `IAM Role` con
  comodines, un bucket sin cifrar, una acción de terceros sin fijar. Tu comentario enseña; el gate
  automatiza lo que ya no hace falta enseñar.
- **Conversación con el analista.** El [Analista DevSecOps](devsecops-analista.md) te trae un patrón:
  el mismo hallazgo aparece en quince repositorios. La respuesta no es quince tickets: es una
  plantilla o una biblioteca interna corregida.
- **Trabajo de plataforma.** Documentas, publicas la plantilla nueva, avisas y —lo más importante—
  **mides la adopción**. Una capacidad que nadie usa no existe.

Dicho sin adornos: una parte del trabajo es **soporte a otros equipos**, y otra parte es política
organizacional. Si solo te gusta construir en soledad, aquí vas a sufrir.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **CI/CD por dentro:** *runners*, cachés, artefactos, entornos, matrices, secretos por ámbito,
  permisos por *job* y el modelo de amenazas propio de cada plataforma (un *pull request* de un
  *fork* que ejecuta código con tus credenciales, por ejemplo).
- **Automatización de análisis:** dónde poner SAST (bloqueante en *merge*, incremental), DAST
  (contra un entorno desplegado, no en cada *commit*), SCA (con *lockfile*) y qué formato común usar
  para no reimplementar el mismo triaje tres veces.
- **Contenedores y Kubernetes:** construcción reproducible, imágenes mínimas, multi-etapa, usuario
  no root, políticas de admisión, contextos de seguridad y por qué escanear la imagen no basta.
- **Infraestructura como código:** Terraform y sus patrones inseguros habituales, análisis estático
  de plantillas y el ciclo de vida del estado.
- **Cadena de suministro:** SBOM (**CycloneDX**, **SPDX**), firma y verificación de artefactos,
  atestaciones de procedencia, niveles de **SLSA**, ataques de confusión de dependencias y
  typosquatting, y buenas prácticas de **OpenSSF**.
- **Policy as code:** OPA y el lenguaje **Rego**, validación en CI, pruebas de las propias políticas
  y control de versiones de las reglas.
- **Identidad y secretos en CI/CD:** federación OIDC hacia la nube, credenciales de corta vida,
  bóvedas, rotación, y por qué una variable de entorno "secreta" en los logs deja de serlo.
- **Programación y mantenimiento:** Python o Go a nivel de escribir herramientas que otros usan,
  con pruebas, manejo de errores y versionado. Lo que construyes es infraestructura.
- **Marcos de referencia:** **NIST SP 800-218 (SSDF)** para las prácticas, la
  **OWASP DevSecOps Guideline** para el mapa de controles del pipeline, **OWASP SAMM** para medir
  madurez y **CIS Benchmarks** para las líneas base.

### Herramientas del oficio

```text
CI/CD:              GitHub Actions, GitLab CI, Jenkins u otro; workflows reutilizables
Análisis en CI:     SAST, DAST y SCA integrados; formato común de resultados (SARIF)
Secretos:           escáner de repositorio e historial, hooks previos al commit, bóveda
Contenedores:       construcción multi-etapa, escaneo de imagen, linters de Dockerfile
Kubernetes:         políticas de admisión, análisis de manifiestos, contextos de seguridad
IaC:                Terraform y análisis estático de plantillas
Cadena de suministro: SBOM (CycloneDX/SPDX), firma y verificación, atestaciones, SLSA
Policy as code:     OPA/Rego, Conftest y pruebas de política
Identidad en CI:    federación OIDC, permisos mínimos por job, entornos protegidos
Observabilidad:     métricas del pipeline, trazas de despliegue, señales de producción
```

Ninguna marca es el objetivo. Lo que se transfiere entre empresas es **el modelo de controles del
ciclo** y la capacidad de implantarlo con las herramientas que ya existan allí.

### Habilidades no técnicas

- **Empatía con quien desarrolla.** Cada segundo que añades al pipeline lo pagan cientos de
  ejecuciones al día. Un control lento se acaba desactivando.
- **Diseño de incentivos.** La pregunta correcta no es "¿cómo lo bloqueo?", sino "¿cómo hago que la
  opción segura sea la más cómoda?".
- **Comunicación de cambios.** Tocar el pipeline es tocar la línea de producción de la empresa.
  Avisar, versionar, dar plazo y ofrecer reversión no es burocracia: es respeto operacional.
- **Criterio de proporcionalidad.** Distinguir lo que justifica parar un despliegue de lo que
  justifica un aviso es la decisión más política del puesto.
- **Documentación.** Una plantilla sin documentación es una plantilla que nadie adopta.

## 📦 Artefactos que produces

- **Pipelines y workflows reutilizables** seguros, versionados y documentados.
- **Definición de puertas de seguridad** con umbrales, justificación y **procedimiento de excepción
  auditable** con vencimiento.
- **SBOM por artefacto**, publicado y conservado.
- **Firmas y atestaciones de procedencia**, con verificación en el despliegue.
- **Políticas OPA/Rego** con sus pruebas.
- **Guía de rutas seguras por defecto** para desarrollo (plantillas, imágenes base, bibliotecas).
- **Modelo de amenazas del propio pipeline** y su plan de mitigación.
- **Runbook de reversión** de un control defectuoso y de rotación de un secreto filtrado.
- **Métricas de plataforma**: adopción, tiempo añadido, tasa de bloqueo y de excepción.

## 📊 Cómo se te mide

| Métrica | Qué mide | Trampa habitual |
|---|---|---|
| **Adopción** (% de repos/servicios con el pipeline seguro) | Si la capacidad existe de verdad | Contar repos configurados, no repos que la ejecutan |
| **Tiempo añadido al pipeline** | El coste que impones | Ignorarlo hasta que alguien lo desactiva |
| **Tasa de bloqueo y de excepción** | Calibración de los gates | Presumir de bloqueos; muchos bloqueos = mala calibración |
| **Cobertura de SBOM y de firma** | Capacidad de responder ante un incidente de cadena de suministro | Generar SBOM que nadie conserva |
| **Secretos de larga vida restantes** en CI/CD | El riesgo más concreto del pipeline | Contar solo los secretos declarados |
| **Nivel SLSA alcanzado** por artefacto | Madurez de la procedencia | Declararlo sin verificación en el despliegue |
| **Tiempo de reversión** de un control defectuoso | Fiabilidad de la plataforma | No haberlo ensayado nunca |
| **Falsos positivos introducidos** por tus reglas | Impacto en la credibilidad ajena | Medirlo solo desde el lado de seguridad |

## 📚 Tu ruta en el programa

Columna vertebral: **Parte 11 completa + Parte 10**, con la Parte 0 (Python, Git, Docker) como base
y la Parte 17 para automatización y gobierno.

1. 📚 [**Parte 0 — Fundamentos**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md)
   (001–025) · [007 Bash](../classes/parte-0-fundamentos-y-prerrequisitos/007-bash-scripting-para-tareas-de-seguridad/README.md),
   [015–016 Python](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md),
   [018 Git](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md),
   [022 Docker](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md)
   y [025 ética](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).
2. 📚 [**Parte 11 — DevSecOps y seguridad del SDLC**](../classes/parte-11-devsecops-y-seguridad-del-sdlc/README.md)
   (236–248) · **entera y en orden**. Es tu especialidad: **236** shift-left · **237** modelado de
   amenazas · **238–240** SAST/DAST/SCA · **241** secretos · **242** pipelines CI/CD ·
   **243** imágenes y contenedores · **244** políticas como código con OPA ·
   **245** vulnerabilidades a escala · **246** SBOM y SLSA · **247** APIs · **248** cultura.
3. 📚 [**Parte 10 — Nube y contenedores**](../classes/parte-10-seguridad-en-la-nube-y-contenedores/README.md)
   (221–235) · **227** Docker · **228–229** Kubernetes · **230** Terraform/IaC ·
   **233** gestión de secretos en la nube · **222** IAM: el terreno que compartes con
   [Cloud Security](cloud-security.md).
4. 📚 [**Parte 2 — Criptografía aplicada**](../classes/parte-2-criptografia-aplicada/README.md)
   · firmas, hashing y [063 gestión de secretos: Vault y KMS](../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md).
   Firmar artefactos sin entender qué garantiza una firma es teatro.
5. 📚 [**Parte 4 — Seguridad web**](../classes/parte-4-seguridad-de-aplicaciones-web/README.md)
   · **087** OWASP Top 10 y **110** APIs REST: lo que tus controles buscan.
6. 📚 [**Parte 17 — Profundización**](../classes/parte-17-profundizacion-para-certificaciones/README.md)
   · **330** análisis de código y automatización de seguridad · **324** hardening y configuración ·
   **313**/**315** identidades y accesos privilegiados · **323** pruebas de software.
7. 📚 [**Parte 8 y Parte 9**](../classes/parte-8-blue-team-deteccion-y-soc/README.md)
   · **182** telemetría y **202** respuesta a incidentes: el pipeline también genera señales, y
   algún día será el origen de un incidente.
8. 📚 [**Parte 14 — GRC**](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md)
   · **284** riesgo de terceros y **282** políticas: la cadena de suministro con lenguaje de
   auditoría.

Clases concretas por las que empezar:

- 🔧 [242 · Seguridad en pipelines CI/CD](../classes/parte-11-devsecops-y-seguridad-del-sdlc/242-seguridad-en-pipelines-ci-cd/README.md) — **la clase central de este rol**.
- 📦 [246 · Supply chain security: SBOM y SLSA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md) — firma, procedencia e inventario.
- 📜 [244 · Políticas como código con OPA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/244-politicas-como-codigo-con-opa/README.md) — reglas versionadas y probadas.
- 🐳 [243 · Imágenes y contenedores seguros en el pipeline](../classes/parte-11-devsecops-y-seguridad-del-sdlc/243-imagenes-y-contenedores-seguros-en-el-pipeline/README.md) y [227 · Seguridad de contenedores Docker](../classes/parte-10-seguridad-en-la-nube-y-contenedores/227-seguridad-de-contenedores-docker/README.md).
- 🔐 [241 · Secretos en el código y pre-commit hooks](../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md) y [233 · Gestión de secretos en la nube](../classes/parte-10-seguridad-en-la-nube-y-contenedores/233-gestion-de-secretos-en-la-nube/README.md).
- 🧱 [230 · Seguridad de Infrastructure as Code (Terraform)](../classes/parte-10-seguridad-en-la-nube-y-contenedores/230-seguridad-de-infrastructure-as-code-terraform/README.md) y [229 · Kubernetes: hardening y ataques](../classes/parte-10-seguridad-en-la-nube-y-contenedores/229-kubernetes-hardening-y-ataques/README.md).
- 🤖 [330 · Análisis de código y automatización de seguridad](../classes/parte-17-profundizacion-para-certificaciones/330-analisis-de-codigo-y-automatizacion-de-seguridad/README.md) — la mentalidad convertida en herramienta.
- 🧭 [236 · Secure SDLC y filosofía shift-left](../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md) y [248 · Cultura DevSecOps y security champions](../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md) — sin esto, lo demás se desactiva.

### Laboratorios

- 🧪 [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md) — **tu laboratorio principal**.
  Sigue el **[Trayecto Ingeniero DevSecOps](../labs/devsecops-pipeline/TRAYECTO-INGENIERO-DEVSECOPS.md)**:
  integrar controles en CI/CD → reglas de bloqueo proporcionales → proteger secretos y permisos →
  escanear código, dependencias, IaC, imagen y aplicación en ejecución → generar SBOM → firmar y
  verificar → policy as code → excepciones auditables → demostrar la reversión de un control
  defectuoso.
- 🧪 [`cloud-security`](../labs/cloud-security/README.md) — el otro extremo de la tubería: postura,
  Kubernetes y contenedores ya desplegados.
- 🧪 [`appsec-code`](../labs/appsec-code/README.md) — para calibrar tus reglas de SAST con casos
  reales antes de imponerlas a otros equipos.
- 🧪 [`appsec-web`](../labs/appsec-web/README.md) — un objetivo desplegado contra el que enganchar el
  DAST de tu pipeline.
- 🧰 **Tu propio repositorio** como laboratorio final: aplica todo lo anterior a un proyecto tuyo.
  Es el portafolio más convincente que puedes tener para este puesto.

## 🧩 Proyecto integrador

**"El camino seguro por defecto".** Toma un proyecto propio (o el repositorio vulnerable del
laboratorio) y entrega una plataforma completa:

1. Un **pipeline reutilizable** con SAST, SCA, escaneo de secretos, análisis de IaC y de imagen, y
   DAST contra el servicio desplegado — con **versiones fijadas** y tiempos medidos.
2. **Puertas proporcionales**: al menos tres niveles (bloquea *merge*, bloquea despliegue, solo
   avisa) con la justificación escrita de cada umbral.
3. **Secretos e identidad**: cero credenciales de larga vida; federación OIDC o equivalente,
   permisos mínimos por *job* y un procedimiento de rotación probado.
4. **SBOM firmado** por artefacto y **verificación de la firma en el despliegue**, con la evidencia
   de que un artefacto no firmado **no** se despliega.
5. Una **política OPA/Rego** con pruebas, que rechace un caso real (por ejemplo, contenedor como
   *root* o recurso sin cifrado).
6. Un **mecanismo de excepción auditable**: quién la pide, quién la aprueba, dónde queda registrada
   y **cuándo caduca automáticamente**.
7. Una **demostración de reversión**: introduce a propósito un control defectuoso que rompa los
   despliegues y muestra cómo se detecta, se revierte y se comunica, con tiempos reales.

Criterio de aceptación: otra persona clona tu repositorio, sigue tu documentación y obtiene el mismo
pipeline funcionando, incluida la verificación de firma que rechaza el artefacto manipulado.

## 🧪 Examen final del rol

Rinde el **[examen final de Ingeniero DevSecOps](../docs/examen-final-por-rol.md)** — 100 puntos:
teoría (25), práctica reproducible (50) e informe (25). Se aprueba con ≥ 70/100 y ≥ 30/50 en la
práctica.

## 💼 Evidencias para tu portafolio

Este es el rol donde el portafolio pesa **más que la certificación**, porque el trabajo es código
público por naturaleza:

- Un **repositorio con el pipeline completo** funcionando y su documentación.
- El **SBOM y la firma** de una release tuya, con las instrucciones de verificación.
- Las **políticas Rego con sus pruebas**.
- El **modelo de amenazas del pipeline** en una página.
- El **runbook de reversión** y el registro de la vez que lo ejecutaste.
- Las **métricas de adopción y tiempo añadido**: demuestra que piensas en quien lo usa, no solo en
  el control.

## 🎤 Preguntas típicas de entrevista

- ¿Qué puede hacer un *pull request* malicioso desde un *fork* en tu CI y cómo lo impides?
- ¿Dónde pondrías SAST, DAST y SCA en el ciclo, y por qué no todos en el mismo sitio?
- ¿Qué bloquearías en el *merge* y qué solo en el despliegue a producción?
- ¿Cómo eliminas las credenciales de larga vida de un pipeline que despliega a la nube?
- Explica SBOM, firma y procedencia: ¿qué problema resuelve cada uno y cuál no resuelve ninguno?
- ¿Qué es SLSA y qué cambia en tu pipeline al subir de nivel?
- ¿Por qué escribir una política en Rego en lugar de un script que compruebe lo mismo?
- Tu control nuevo rompió los despliegues de toda la empresa. ¿Qué haces en los primeros 10 minutos?
- ¿Cómo consigues adopción sin obligar por decreto?
- Se filtró un token en el historial de Git. ¿Cuál es el orden exacto de tus acciones?

## 🎓 Certificaciones

Con archivo en el programa:

- 📋 [**CompTIA CySA+** (CS0-003)](../certificaciones/comptia-cysa-plus-cs0-003.md) — base sólida de
  operaciones y gestión de vulnerabilidades; no cubre pipeline ni cadena de suministro.
- 🎓 [**CompTIA Security+** (SY0-701)](../certificaciones/comptia-security-plus-sy0-701.md) — el
  vocabulario común, útil si vienes de DevOps sin fondo de seguridad.
- 🏛️ [**CISSP**](../certificaciones/cissp.md) — a medio plazo, para el lado de arquitectura y
  gobierno del programa.

**Ninguna certificación describe bien este rol todavía**, y conviene decirlo sin adornos. Fuera del
programa, lo más cercano es **CKS** (seguridad de Kubernetes) cuando el terreno es Kubernetes, las
certificaciones de la nube que uses y las formaciones de **OpenSSF** sobre cadena de suministro. En
este puesto, un **repositorio público con un pipeline bien hecho convence más que cualquier examen**.
Distingue siempre formación de certificación, y recuerda que ninguna de las dos garantiza empleo.
Consulta el [mapeo completo a certificaciones](../certificaciones/README.md).

## 📈 Progresión de carrera y salario

Ruta habitual: **desarrollo, DevOps/SRE o [Ingeniero SecOps](secops-engineer.md) → Ingeniero
DevSecOps → Ingeniero Sr. / Staff → líder de plataforma de seguridad o arquitecto**. Salidas
naturales:

- Hacia **la plataforma en ejecución**: [Cloud Security Engineer](cloud-security.md).
- Hacia **el código y el diseño**: [AppSec Engineer](appsec.md).
- Hacia **la arquitectura**: arquitectura de seguridad y zero trust (clases 316 y 329).
- Hacia **la dirección técnica**: liderazgo de un equipo de plataforma o de seguridad de producto.

Es uno de los perfiles con **mejor techo técnico** del programa, junto con
[Ingeniero SecOps](secops-engineer.md): no obliga a pasar a gestión para seguir creciendo.

Sobre **salario**: este programa no publica un estudio salarial propio y no inventa cifras. Como
referencia orientativa, este perfil suele situarse **en el rango alto** de la seguridad defensiva,
comparable al de [Ingeniero SecOps](secops-engineer.md#-progresión-de-carrera-y-salario) —cuya tabla
orientativa por región sirve de referencia— y por encima de los perfiles de análisis puro. Verifica
siempre con ofertas reales, indicando país, moneda y fecha: los rangos cambian por sector, tamaño y
año.

## ⚠️ Mitos y errores comunes

- **"Un gate más estricto es más seguridad."** Un gate mal calibrado se desactiva, y entonces la
  seguridad es cero. La calibración es el trabajo, no el bloqueo.
- **"DevSecOps es poner escáneres en el CI."** Eso es el primer 20 %. El resto es decisión, cadena
  de suministro, identidad del pipeline y adopción.
- **"El SBOM es un requisito de cumplimiento."** También, pero su valor real es responder
  *"¿nos afecta?"* en minutos cuando aparece una vulnerabilidad grave un fin de semana.
- **"Escanear la imagen es asegurar el contenedor."** El escaneo mira paquetes conocidos: no ve
  privilegios, montajes, red, ni lo que hace el proceso al arrancar.
- **"El pipeline es infraestructura de desarrollo, no un activo crítico."** Tiene llaves de
  producción. Es de los activos más críticos que existen.
- **"Si está en la nube, es problema de Cloud Security."** El pipeline es tuyo aunque corra en su
  cuenta. Poneos de acuerdo por escrito sobre la frontera.
- **"Si no hay excepciones, vamos bien."** Si no hay excepciones registradas, probablemente las haya
  sin registrar.

## ⚖️ Límites éticos y legales

- **Tu pipeline tiene privilegios de producción.** Cambiarlo sin comunicación ni ventana puede
  parar la operación de la empresa: aplica gestión de cambios como cualquier sistema crítico.
- **Nunca uses credenciales reales en un laboratorio ni en un ejemplo.** Todo el material de este
  programa usa credenciales falsas con formato válido, a propósito.
- **Secretos filtrados:** se rotan primero y se documentan después; no se comparten en tickets ni
  capturas, y no se "prueban" para ver si funcionan.
- **No expongas entornos vulnerables.** Los laboratorios escuchan en `127.0.0.1` por diseño
  ([Clase 025](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)).
- **Licencias de terceros.** Automatizar SBOM revela obligaciones de licenciamiento; trátalo como
  información interna y consulta con quien corresponda antes de publicar.
- **Divulgación responsable.** Si tu automatización descubre una vulnerabilidad en un proyecto de
  terceros, repórtala por su canal oficial.
- **Las puertas de seguridad afectan al trabajo de otras personas.** Bloquear sin aviso, sin vía de
  excepción y sin explicación no es rigor: es abuso de una posición técnica.

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Analista DevSecOps](devsecops-analista.md) · [Cloud Security](cloud-security.md) · [AppSec Engineer](appsec.md) · [Ingeniero SecOps](secops-engineer.md)
- 🗺️ [Matriz comparativa SecOps y DevSecOps](../docs/matriz-roles-secops-devsecops.md)
- 🏠 [Inicio del programa](../README.md)
