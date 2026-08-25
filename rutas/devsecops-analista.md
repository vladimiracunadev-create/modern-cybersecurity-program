# 🧮 Analista DevSecOps (triaje, priorización y riesgo del SDLC)

> El rol que convierte **miles de hallazgos automáticos en un puñado de decisiones defendibles**.
> Recibe la salida de SAST, DAST, SCA, escaneo de secretos, IaC y contenedores; separa lo real de lo
> ruidoso; prioriza con KEV, EPSS, CVSS, exposición y criticidad de negocio; abre el ticket con el
> dueño correcto; acuerda SLA; documenta las excepciones; y **verifica que la corrección funcionó**.
>
> **Nivel de entrada:** semi-senior; requiere entender código, no escribirlo a nivel de producción · **Foco:** triaje de hallazgos, falsos positivos, priorización por riesgo, backlog de seguridad, SLA y excepciones, métricas y cumplimiento (NIST SSDF, OWASP SAMM) · **Certificación faro:** CompTIA CySA+ (+ Security+ como base)

## 🧭 Qué es y por qué importa

Cuando una organización enchufa las herramientas de seguridad al pipeline, en dos semanas tiene el
problema contrario al que quería resolver: **20 000 hallazgos y cero confianza en ellos**. Los
equipos de desarrollo dejan de mirar el informe, el gate se desactiva "temporalmente" y la seguridad
del SDLC se convierte en teatro.

El **Analista DevSecOps** existe para que eso no pase. Su producto no es un escaneo: es una
**lista corta, priorizada y creíble** de lo que hay que arreglar, con dueño y plazo, más la
trazabilidad de por qué el resto puede esperar.

Su trabajo tiene cuatro ejes:

- **Triaje con criterio.** Normalizar y deduplicar la salida de herramientas distintas que reportan
  el mismo problema con nombres distintos, y separar **hallazgo real**, **falso positivo** y
  **verdadero pero irrelevante en este contexto** (la categoría que más tiempo ahorra y peor se
  documenta).
- **Priorización por riesgo, no por severidad.** ¿Está el código realmente ejecutando esa función?
  ¿Está el servicio expuesto? ¿Existe explotación activa (**CISA KEV**)? ¿Cuál es la probabilidad de
  explotación (**EPSS**)? ¿Qué vale el activo para el negocio? La severidad CVSS es **una** entrada,
  no la respuesta.
- **Gobierno del backlog.** SLA por severidad, excepciones temporales con responsable y vencimiento,
  aceptación de riesgo documentada, y seguimiento hasta el cierre **verificado**.
- **Medición y cumplimiento.** Tableros de deuda y tendencia, y mapeo de la evidencia contra
  **NIST SP 800-218 (SSDF)**, **OWASP SAMM** y los requisitos internos o del cliente.

Importa porque es **el eslabón que hace sostenible todo lo demás**. Se puede comprar el mejor
conjunto de escáneres del mercado; sin alguien que haga este trabajo, el resultado es ruido caro.

### Qué problema resuelve

El problema de la **credibilidad**. En seguridad del software, la confianza se pierde con el tercer
falso positivo que bloquea un despliegue y no se recupera en meses. Este rol protege el activo más
frágil del programa: que cuando seguridad diga *esto hay que arreglarlo ahora*, desarrollo lo crea.

## 🚫 Qué NO es este rol

- **No es "el que ejecuta los escáneres".** Ejecutarlos es trivial y además debería estar
  automatizado por el [Ingeniero DevSecOps](devsecops-engineer.md). El trabajo empieza cuando el
  informe existe.
- **No es quien construye el pipeline.** No define las etapas del CI/CD, no firma artefactos, no
  escribe políticas OPA. **Consume** esa plataforma y le pide cambios.
- **No es AppSec.** No hace modelado de amenazas ni revisión de código de diseño; puede leer código
  para validar un hallazgo, pero la profundidad de seguridad del código es del
  [AppSec Engineer](appsec.md).
- **No es un pentester.** Valida hallazgos, no los explota. Confirmar explotabilidad más allá de lo
  documental se coordina con AppSec o con una prueba autorizada.
- **No es GRC.** Produce evidencia y métricas para cumplimiento, pero no gestiona el SGSI ni el
  registro de riesgos corporativo.
- **No es un buzón de tickets.** Si el rol se degrada a reenviar la salida del escáner a desarrollo,
  desaparece el valor: eso lo hace un webhook.

### Frente a los perfiles vecinos

- Frente al [Ingeniero DevSecOps](devsecops-engineer.md): él **construye la capacidad** (pipeline,
  gates, SBOM, firma, policy as code); tú **operas el riesgo** que esa capacidad revela. Es la misma
  relación que entre un analista y un ingeniero de SOC. En una empresa pequeña, las dos mitades caen
  en la misma persona — y entonces el título suele ser *Especialista DevSecOps*.
- Frente al [AppSec Engineer](appsec.md): AppSec trabaja **hacia adentro del código y del diseño**
  (threat modeling, ASVS, revisión, acompañamiento al desarrollador); tú trabajas **hacia afuera,
  sobre el flujo de hallazgos y decisiones**. Colaboráis constantemente: cuando un hallazgo tuyo
  necesita criterio profundo de código, es AppSec quien lo resuelve.
- Frente al [Analista SecOps](secops-analista.md): idéntico oficio, distinta superficie. Él persigue
  vulnerabilidades en servidores y endpoints **en producción**; tú, en el código, las dependencias,
  las imágenes y la IaC **antes** de que lleguen ahí. Cuando una dependencia vulnerable ya está
  desplegada, el caso es de los dos.
- Frente al [Analista de Gestión de Vulnerabilidades](gestion-vulnerabilidades.md): ese rol es el
  equivalente clásico centrado en infraestructura; este es su versión para el SDLC, con
  herramientas, dueños y tiempos distintos.
- Frente al [Cloud Security Engineer](cloud-security.md): él asegura **la plataforma donde corre**
  lo que tú ayudas a construir con seguridad. Tus hallazgos de IaC son el punto exacto donde os
  cruzáis.

## 🪜 Nivel de entrada y prerrequisitos

No es un primer empleo, pero tampoco exige ser desarrollador senior.

- **Imprescindible:** leer código de al menos un lenguaje con soltura (Python, Java, JavaScript…) lo
  bastante para juzgar si un hallazgo de SAST es real; entender Git y el flujo de trabajo de un
  equipo de desarrollo; conocer CVE, CVSS y el ciclo de vida de una vulnerabilidad.
- **Muy recomendable:** haber trabajado antes en QA, desarrollo, soporte de aplicaciones, SOC o
  gestión de vulnerabilidades. Cualquier experiencia previa que te haya obligado a **negociar
  prioridades con desarrollo** vale oro aquí.
- **Deseable:** scripting para tratar informes (JSON, SARIF, CSV), nociones de contenedores y de
  infraestructura como código.
- **No hace falta:** construir pipelines, administrar Kubernetes ni escribir políticas Rego. Sí
  entender qué hacen, para pedir cambios con sentido.

En el programa: **Parte 0 completa** (con Git y Python) y al menos las clases 236–240 de la Parte 11
antes de asumir el rol.

## 🧾 Responsabilidades habituales

- **Analizar los hallazgos** de SAST, DAST, SCA, escaneo de secretos, IaC y contenedores; normalizar
  y deduplicar entre herramientas.
- **Eliminar falsos positivos de manera trazable**: cada descarte queda documentado con motivo,
  fecha y responsable; nunca es un borrado silencioso.
- **Priorizar** con CISA KEV, EPSS, CVSS, exposición real, alcanzabilidad del código y contexto de
  negocio.
- **Mantener el backlog de seguridad**: que exista, que tenga dueños, que envejezca poco y que se
  pueda explicar.
- **Gestionar SLA, excepciones temporales y aceptación de riesgo** con responsable, vencimiento y
  control compensatorio.
- **Definir métricas y tableros**: deuda por severidad, edad media, tasa de falsos positivos,
  cumplimiento de SLA, cobertura de escaneo.
- **Mapear evidencia** contra NIST SSDF, OWASP SAMM y los requisitos internos o contractuales.
- **Coordinar** a desarrollo, [AppSec](appsec.md), [Ingeniería DevSecOps](devsecops-engineer.md),
  operaciones y cumplimiento.
- **Comprobar que la corrección se verificó**: no basta con que el ticket esté cerrado ni con que el
  escáner ya no lo reporte — hay que saber por qué dejó de reportarlo.

## 🗓️ Un día en el puesto

- **Revisión de la cola nocturna.** Los pipelines corrieron de madrugada. Miras qué es nuevo, qué es
  recurrente y qué **bloqueó un despliegue**: lo bloqueado va primero, porque hay gente esperando.
- **Triaje.** Un hallazgo de SAST marca inyección SQL en un módulo que resulta ser un script de
  migración que corre una vez y con parámetros fijos: falso positivo *en contexto*. Lo documentas
  con esa razón exacta y creas la regla para que no vuelva a aparecer cada semana.
- **Dependencias.** Llegan doce CVE nuevas del escaneo SCA. Dos están en KEV; una de esas dos vive
  en una biblioteca que el código **importa pero nunca ejecuta**. Ese matiz —alcanzabilidad— es la
  diferencia entre parar un equipo y no molestarlo.
- **Conversación con desarrollo.** No un correo: una conversación. Explicas por qué esas dos cosas
  hay que hacerlas esta semana y por qué las otras diez pueden ir al siguiente ciclo. Sales con
  fechas acordadas, no impuestas.
- **Una excepción.** Un servicio no puede actualizar una biblioteca sin romper un cliente. Redactas
  la excepción: quién la pide, quién la aprueba, qué control compensatorio se aplica mientras tanto,
  y **cuándo vence**. Sin fecha de vencimiento no es una excepción, es un olvido.
- **Verificación.** Vuelves sobre los cierres de la semana pasada: ¿el escáner dejó de reportarlo
  porque se arregló, o porque alguien excluyó la carpeta del análisis? Esta pregunta es la que
  distingue a un analista serio.
- **Reporte y métricas.** Actualizas el tablero. Preparas la vista para desarrollo (qué te toca) y
  la vista para dirección (vamos mejor o peor, y en qué).

Dicho sin adornos: es un rol de **mucha negociación y mucha lectura**. Si esperabas romper cosas,
este no es el puesto; si te gusta que las decisiones estén bien fundamentadas, es de los más
satisfactorios del sector.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- **Las familias de análisis y sus límites:** SAST (falsos positivos por falta de contexto de
  ejecución), DAST (solo ve lo que alcanza), SCA (depende del manifiesto y del *lockfile*), escaneo
  de secretos (el historial no se olvida), IaC y escaneo de imágenes (heredas el sistema operativo
  base). Saber **qué no ve cada una** es más útil que saber ejecutarlas.
- **Alcanzabilidad y explotabilidad.** Una CVE en una dependencia transitiva que tu código nunca
  invoca no es el mismo riesgo que la misma CVE en la ruta caliente de tu API.
- **Priorización moderna:** **CISA KEV** (explotación confirmada en el mundo real), **FIRST EPSS**
  (probabilidad estimada de explotación a 30 días), **CVSS v3.1/v4.0** (severidad técnica, con sus
  métricas ambientales que casi nadie rellena) y el contexto de negocio.
- **Lectura de código suficiente** para validar: seguir un flujo de datos desde la entrada hasta el
  sink, distinguir una entrada controlada por el usuario de una constante.
- **Vulnerabilidades de aplicación:** OWASP Top 10 y las categorías de **OWASP ASVS**, para hablar
  el mismo idioma que AppSec y desarrollo.
- **Formatos y tuberías de datos:** SARIF, CycloneDX y SPDX (SBOM), JSON de cada herramienta, y cómo
  se normalizan para deduplicar.
- **El flujo de trabajo del desarrollo:** ramas, *pull requests*, revisión, versionado y despliegue.
  Sin esto, tus tickets caen en el momento equivocado del ciclo.
- **Marcos del SDLC seguro:** **NIST SP 800-218 (SSDF)** como catálogo de prácticas, **OWASP SAMM**
  como modelo de madurez y la **OWASP DevSecOps Guideline** como mapa de controles del pipeline.
- **Gestión del riesgo:** qué es una excepción, qué es una aceptación, quién puede firmarla y por
  qué el control compensatorio no es opcional.

### Herramientas del oficio

```text
Análisis estático:   herramientas SAST y de reglas (tipo Semgrep, Bandit, CodeQL)
Dependencias (SCA):  escáneres de manifiesto y lockfile, avisos del ecosistema, SBOM
Dinámico:            DAST sobre la app en ejecución (tipo ZAP), pruebas de API
Secretos:            escáner de repositorio e historial (tipo gitleaks, detect-secrets)
IaC y contenedores:  análisis de plantillas y de imágenes (tipo trivy, checkov, hadolint)
Inteligencia:        CISA KEV, FIRST EPSS, CVSS, avisos del proveedor y del ecosistema
Agregación:          plataforma de gestión de vulnerabilidades o, como mínimo, un backlog serio
Trabajo diario:      Git y el foro del repositorio, ticketing, hoja de cálculo, tableros
```

Las marcas se sustituyen; **el criterio no**. Este programa enseña las categorías y usa
herramientas libres como vehículo, no como objetivo de aprendizaje.

### Habilidades no técnicas

- **Diplomacia técnica.** Vas a decirle a alguien que su código tiene un problema. Cómo lo digas
  determina si lo arregla o si aprende a ignorarte.
- **Capacidad de decir "esto no importa".** Es la habilidad más escasa y la más valiosa: descartar
  con argumento y dejarlo por escrito.
- **Escritura precisa.** Un hallazgo bien redactado —qué, dónde, por qué importa aquí, cómo se
  arregla, cómo se verifica— se arregla; uno mal redactado se discute durante tres semanas.
- **Pensamiento de sistema.** Si el mismo tipo de hallazgo aparece en quince repositorios, el
  problema no son los quince repositorios: es una plantilla, una biblioteca interna o una práctica.
- **Firmeza sin dramatismo.** Si todo es crítico, nada lo es. Guardar la palabra "crítico" para
  cuando toca es una decisión de credibilidad.

## 📦 Artefactos que produces

- **Informe de triaje** con la clasificación de cada hallazgo y el motivo del descarte.
- **Backlog priorizado** de seguridad, con criterio de orden explícito y verificable.
- **Registro de excepciones** con responsable, aprobador, control compensatorio y vencimiento.
- **Definición de SLA** por severidad, acordada con desarrollo (no impuesta).
- **Tablero de métricas**: deuda, edad, tendencia, cumplimiento de SLA, tasa de falso positivo.
- **Informe de riesgo del SDLC** para dirección: qué mejoró, qué empeoró y qué decisión se pide.
- **Matriz de evidencia** contra NIST SSDF y OWASP SAMM para auditoría o para un cliente.
- **Verificación de corrección**: la prueba de que el hallazgo se cerró por la razón correcta.

## 📊 Cómo se te mide

| Métrica | Qué mide | Trampa habitual |
|---|---|---|
| **Tasa de falsos positivos** entregados a desarrollo | Calidad de tu triaje | Bajarla descartando también lo real |
| **Tiempo medio de remediación** por severidad | Si el ciclo funciona | Medirlo solo sobre lo que se cerró |
| **Deuda de seguridad y su edad** | Si el programa gana terreno | Cerrar en masa lo trivial |
| **Cumplimiento de SLA** | Si los acuerdos se sostienen | SLA sin acuerdo real de desarrollo |
| **Cobertura de escaneo** (repos, ramas, tipos de análisis) | El tamaño del punto ciego | Contar repos escaneados sin mirar si el análisis falló |
| **Excepciones vigentes y vencidas** | Riesgo aceptado visible | Excepciones perpetuas |
| **Reapertura tras cierre** | Si la verificación es real | Fiarse de que el escáner ya no lo diga |
| **Adopción por parte de desarrollo** | Si el proceso se usa o se rodea | Medir tickets creados, no tickets resueltos |

## 📚 Tu ruta en el programa

El eje es la **Parte 11**, con la Parte 4 para entender las vulnerabilidades que estás triando y la
Parte 17 para el gobierno del programa.

1. 📚 [**Parte 0 — Fundamentos**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md)
   (001–025) · [003 frameworks](../classes/parte-0-fundamentos-y-prerrequisitos/003-frameworks-de-seguridad-nist-csf-iso-27001-mitre-att-ck-y-diamond-model/README.md),
   [015 Python](../classes/parte-0-fundamentos-y-prerrequisitos/015-python-para-seguridad-fundamentos-del-lenguaje/README.md),
   [018 Git](../classes/parte-0-fundamentos-y-prerrequisitos/018-git-y-control-de-versiones-para-profesionales-de-seguridad/README.md),
   [019 regex](../classes/parte-0-fundamentos-y-prerrequisitos/019-expresiones-regulares-para-analisis-de-logs-y-datos/README.md),
   [022 Docker](../classes/parte-0-fundamentos-y-prerrequisitos/022-docker-y-contenedores-para-laboratorios-de-seguridad/README.md)
   y [025 ética](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).
2. 📚 [**Parte 11 — DevSecOps y seguridad del SDLC**](../classes/parte-11-devsecops-y-seguridad-del-sdlc/README.md)
   (236–248) · **el núcleo, entera**, con foco especial en **238** SAST · **239** DAST ·
   **240** SCA y dependencias · **241** secretos · **243** imágenes y contenedores ·
   **245** gestión de vulnerabilidades a escala · **246** SBOM y cadena de suministro ·
   **248** cultura y security champions.
3. 📚 [**Parte 4 — Seguridad web**](../classes/parte-4-seguridad-de-aplicaciones-web/README.md)
   · **087** OWASP Top 10 y las clases de las vulnerabilidades que más vas a triar; **110** APIs REST.
   No para explotarlas, para **entender el hallazgo** que tienes delante.
4. 📚 [**Parte 17 — Profundización**](../classes/parte-17-profundizacion-para-certificaciones/README.md)
   · **318** gestión del programa de vulnerabilidades · **323** pruebas de seguridad del software ·
   **321** comunicación y reporte · **330** análisis de código y automatización.
5. 📚 [**Parte 14 — GRC**](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md)
   · **277** gestión de riesgos · **282** políticas y procedimientos · **284** riesgo de terceros
   (que es exactamente lo que son tus dependencias) · **287** métricas.
6. 📚 [**Parte 10 — Nube y contenedores**](../classes/parte-10-seguridad-en-la-nube-y-contenedores/README.md)
   · **227** contenedores · **230** IaC/Terraform · **231** CSPM: la superficie que compartes con
   [Cloud Security](cloud-security.md).
7. 📚 [**Parte 15 — Seguridad de IA**](../classes/parte-15-seguridad-de-ia-y-machine-learning/README.md)
   · opcional pero cada vez menos: modelos y bibliotecas de IA ya entran por el mismo pipeline.

Clases concretas por las que empezar:

- 📈 [245 · Gestión de vulnerabilidades a escala](../classes/parte-11-devsecops-y-seguridad-del-sdlc/245-gestion-de-vulnerabilidades-a-escala/README.md) — **la clase central de este rol**.
- 🧬 [240 · SCA: dependencias y riesgo de terceros](../classes/parte-11-devsecops-y-seguridad-del-sdlc/240-sca-dependencias-y-riesgo-de-terceros/README.md) — la fuente número uno de tu backlog.
- 🔬 [238 · SAST: análisis estático de código](../classes/parte-11-devsecops-y-seguridad-del-sdlc/238-sast-analisis-estatico-de-codigo/README.md) y [239 · DAST](../classes/parte-11-devsecops-y-seguridad-del-sdlc/239-dast-analisis-dinamico-de-aplicaciones/README.md) — de dónde salen los falsos positivos y por qué.
- 📦 [246 · Supply chain security: SBOM y SLSA](../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md) — el inventario que hace posible responder "¿nos afecta?" en minutos.
- 🎯 [318 · Gestión del programa de vulnerabilidades](../classes/parte-17-profundizacion-para-certificaciones/318-gestion-del-programa-de-vulnerabilidades/README.md) — SLA, excepciones y gobierno.
- 🧪 [323 · Pruebas de seguridad del software y evaluación](../classes/parte-17-profundizacion-para-certificaciones/323-pruebas-de-seguridad-del-software-y-evaluacion/README.md) — qué prueba cada técnica y qué deja fuera.
- 🗣️ [321 · Comunicación y reporte](../classes/parte-17-profundizacion-para-certificaciones/321-comunicacion-y-reporte-para-analistas-de-seguridad/README.md) y [248 · Cultura DevSecOps y security champions](../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md) — la mitad relacional del puesto.
- ⚖️ [277 · Gestión de riesgos cuantitativa y cualitativa](../classes/parte-14-grc-riesgo-y-cumplimiento/277-gestion-de-riesgos-cuantitativa-y-cualitativa/README.md) — para que "aceptar el riesgo" signifique algo.

### Laboratorios

- 🧪 [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md) — **tu laboratorio principal**.
  Sigue el **[Trayecto Analista DevSecOps](../labs/devsecops-pipeline/TRAYECTO-ANALISTA-DEVSECOPS.md)**:
  varios escáneres → normalizar y deduplicar → separar falsos positivos → priorizar con KEV/EPSS/CVSS
  y exposición → tickets y SLA → excepción documentada → verificación → informe de riesgo y métricas.
  El script [`priorizar.py`](../labs/devsecops-pipeline/priorizar.py) consulta KEV y EPSS de verdad.
- 🧪 [`appsec-code`](../labs/appsec-code/README.md) — para aprender a **validar** un hallazgo de
  SAST leyendo el código, que es la habilidad que separa el triaje del reenvío.
- 🧪 [`appsec-web`](../labs/appsec-web/README.md) — ver una vulnerabilidad funcionando cambia para
  siempre cómo priorizas su hallazgo.
- 🧪 [`cloud-security`](../labs/cloud-security/README.md) — hallazgos de IaC y de postura, la
  frontera con [Cloud Security](cloud-security.md).

## 🧩 Proyecto integrador

**"De 20 000 a 12".** Partiendo de la salida cruda de varios escáneres sobre el repositorio
vulnerable del laboratorio, entrega:

1. Un **inventario normalizado y deduplicado** de hallazgos, explicando la regla de deduplicación.
2. La **clasificación de triaje** (real / falso positivo / real pero no aplicable) con motivo escrito
   para cada descarte y al menos tres descartes bien argumentados.
3. La **priorización final** —máximo doce elementos— con la fórmula explícita: KEV, EPSS, CVSS,
   exposición, alcanzabilidad y criticidad de negocio.
4. **Cinco tickets** listos para desarrollo, con criterio de verificación incluido, y **una
   excepción** completa (responsable, aprobador, compensación, vencimiento).
5. La **verificación de dos correcciones**, demostrando *por qué* el hallazgo desapareció.
6. Un **informe de riesgo y métricas** de dos páginas y una **matriz de evidencia** contra al menos
   cinco prácticas del NIST SSDF.

Criterio de aceptación: una persona ajena reproduce tu priorización con tus datos y tu criterio, y
llega al mismo orden.

## 🧪 Examen final del rol

Rinde el **[examen final de Analista DevSecOps](../docs/examen-final-por-rol.md)** — 100 puntos:
teoría (25), práctica reproducible (50) e informe (25). Se aprueba con ≥ 70/100 y ≥ 30/50 en la
práctica.

## 💼 Evidencias para tu portafolio

- El **informe de triaje** completo, con los falsos positivos y su justificación: es la pieza que
  más impresiona en una entrevista, porque casi nadie la trae.
- La **hoja de priorización** con la fórmula y los datos de KEV/EPSS.
- Un **registro de excepciones** de ejemplo bien redactado.
- El **tablero de métricas** con la interpretación escrita, no solo el gráfico.
- La **matriz de evidencia SSDF/SAMM**, que demuestra que sabes traducir trabajo técnico a lenguaje
  de auditoría.
- Opcional y muy diferenciador: un **repositorio propio** con el pipeline y el informe generado sobre
  tu propio código.

## 🎤 Preguntas típicas de entrevista

- El SCA reporta una CVE crítica en una dependencia transitiva. ¿Qué preguntas antes de escalarla?
- Diferencia entre CVSS, EPSS y KEV. ¿Cuál usarías para decidir si paras un despliegue?
- ¿Cómo documentas un falso positivo para que no vuelva a consumir tiempo cada semana?
- Desarrollo dice que tu hallazgo no es explotable. ¿Cómo lo resuelves sin pelear ni ceder?
- ¿Qué tiene que contener una excepción de seguridad para que sea aceptable?
- Un hallazgo desapareció del informe. ¿Cómo distingues "se arregló" de "se dejó de mirar"?
- ¿Qué métricas de DevSecOps llevarías a dirección y cuáles nunca?
- ¿Para qué sirve un SBOM cuando aparece una vulnerabilidad grave un domingo por la noche?
- ¿Qué harías si el gate de seguridad se desactivó "temporalmente" hace cuatro meses?

## 🎓 Certificaciones

Con archivo en el programa:

- 📋 [**CompTIA CySA+** (CS0-003)](../certificaciones/comptia-cysa-plus-cs0-003.md) — **la más
  cercana**: gestión de vulnerabilidades, priorización, reporte y operaciones. Es el examen que
  mejor describe el oficio.
- 🎓 [**CompTIA Security+** (SY0-701)](../certificaciones/comptia-security-plus-sy0-701.md) — base
  y filtro de RR. HH. si vienes de desarrollo sin fondo de seguridad.
- 🏛️ [**CISSP**](../certificaciones/cissp.md) — a medio plazo, si el rol te lleva hacia gobierno del
  programa y riesgo.

Fuera del programa, en este perfil se valoran las certificaciones de **seguridad del software**
(por ejemplo CSSLP) y las de producto de la plataforma de gestión de vulnerabilidades que use la
empresa. **Formación no es certificación**: este programa te da el cuerpo de conocimiento y la
práctica; el examen lo rinde y lo cobra un tercero, y ninguno de los dos garantiza empleo. Consulta
el [mapeo completo a certificaciones](../certificaciones/README.md).

## 📈 Progresión de carrera y salario

Ruta habitual: **desarrollo, QA, SOC o gestión de vulnerabilidades → Analista DevSecOps →
Analista Sr. / líder del programa de seguridad del SDLC**. Desde ahí:

- Hacia **construir**: [Ingeniero DevSecOps](devsecops-engineer.md). Es la progresión más natural si
  el trabajo te empuja a automatizar lo que hoy haces a mano.
- Hacia **la profundidad de código**: [AppSec Engineer](appsec.md).
- Hacia **la plataforma**: [Cloud Security Engineer](cloud-security.md).
- Hacia **gobierno**: gestión del programa, [GRC](grc.md) o
  [jefatura de seguridad](ciso-jefe-seguridad.md).

Sobre **salario**: este programa no publica un estudio salarial propio ni va a inventar cifras. Como
referencia orientativa, el perfil de análisis suele quedar **por debajo** del de ingeniería en el
mismo dominio; consulta ofertas reales indicando país, moneda y fecha antes de negociar. Los rangos
varían enormemente por sector, tamaño de empresa y año.

## ⚠️ Mitos y errores comunes

- **"Más escáneres, más seguridad."** Más escáneres sin capacidad de triaje es más ruido y menos
  credibilidad. La capacidad de análisis es el cuello de botella, no la de escaneo.
- **"Bloquear todo lo crítico."** Un gate que bloquea sin criterio se desactiva en un mes, y entonces
  no queda nada.
- **"El CVSS decide."** El CVSS describe la vulnerabilidad, no tu exposición. Sin contexto,
  priorizar es sortear.
- **"Si el escáner ya no lo reporta, está arreglado."** Puede que alguien excluyera la ruta, cambiara
  la rama analizada o el escáner fallara en silencio. Verificar es parte del trabajo.
- **"El falso positivo se descarta y ya."** Un descarte sin registro se vuelve a triar el mes que
  viene. El registro es el producto.
- **"Es un rol para quien no sabe programar."** Es un rol para quien **sabe leer** código y decidir.
  Muy distinto, y bastante más difícil de lo que parece.

## ⚖️ Límites éticos y legales

- **Validar no es explotar.** Confirmar un hallazgo con una prueba activa contra un sistema
  requiere autorización explícita y alcance escrito
  ([Clase 025](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)).
- **Los secretos encontrados son datos sensibles.** Un token filtrado se rota y se documenta; no se
  pega en un ticket, en un chat ni en una captura de pantalla.
- **Licencias y terceros.** El SBOM revela también obligaciones legales de licenciamiento: es
  información sensible de la empresa, no material para publicar.
- **La aceptación del riesgo es de quien tiene autoridad.** Tú documentas la opción y sus
  consecuencias; la firma es de negocio.
- **Divulgación responsable.** Si encuentras una vulnerabilidad en una dependencia de terceros,
  repórtala por el canal del proyecto, no en público.
- **Los entornos vulnerables del programa son de laboratorio**: escuchan en `127.0.0.1`, sus
  credenciales son falsas y no deben exponerse a internet ni reutilizarse.

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Ingeniero DevSecOps](devsecops-engineer.md) · [AppSec Engineer](appsec.md) · [Analista SecOps](secops-analista.md) · [Cloud Security](cloud-security.md) · [Gestión de vulnerabilidades](gestion-vulnerabilidades.md)
- 🗺️ [Matriz comparativa SecOps y DevSecOps](../docs/matriz-roles-secops-devsecops.md)
- 🏠 [Inicio del programa](../README.md)
