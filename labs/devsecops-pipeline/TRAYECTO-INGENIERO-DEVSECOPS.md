# Trayecto Ingeniero DevSecOps — construir la tubería, no solo auditarla

Extensión del laboratorio [`devsecops-pipeline`](README.md) para la ruta
[Ingeniero DevSecOps](../../rutas/devsecops-engineer.md). El recorrido base **audita** un pipeline
roto; este trayecto te pide **construir uno que no lo esté** y demostrar que funciona — incluida la
parte que casi nadie ensaya: revertirlo cuando tu propio control rompe los despliegues de toda la
empresa.

> ⚠️ Trabaja siempre sobre **un repositorio tuyo** (uno nuevo vale) o sobre una copia local de
> `repo-vulnerable/`. Nunca uses credenciales reales: todo el material del laboratorio usa
> credenciales **falsas con formato válido**, a propósito
> ([Clase 025](../../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)).

## 🎯 Qué construyes aquí

```text
1. Controles integrados en CI/CD        →  que corran solos, en el sitio correcto
2. Bloqueo proporcional                 →  qué para el merge, qué para el deploy, qué solo avisa
3. Secretos y permisos del pipeline     →  identidad efímera, mínimo privilegio, nada de larga vida
4. Cobertura de análisis                →  código, dependencias, IaC, imagen y app en ejecución
5. SBOM                                 →  el inventario que salva el fin de semana
6. Firma y verificación                 →  que lo desplegado sea lo que construiste
7. Policy as code                       →  reglas versionadas, revisadas y probadas
8. Excepciones auditables y temporales  →  la válvula que evita que te desactiven el gate
9. Reversión demostrada                 →  el control defectuoso también es un incidente
```

| Paso | Clases del programa |
|---|---|
| Pipelines y CI/CD | [242](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/242-seguridad-en-pipelines-ci-cd/README.md), [236](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/236-secure-sdlc-y-filosofia-shift-left/README.md) |
| Análisis automatizado | [238](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/238-sast-analisis-estatico-de-codigo/README.md), [239](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/239-dast-analisis-dinamico-de-aplicaciones/README.md), [240](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/240-sca-dependencias-y-riesgo-de-terceros/README.md) |
| Secretos e identidad | [241](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/241-secretos-en-el-codigo-y-pre-commit-hooks/README.md), [233](../../classes/parte-10-seguridad-en-la-nube-y-contenedores/233-gestion-de-secretos-en-la-nube/README.md), [063](../../classes/parte-2-criptografia-aplicada/063-gestion-de-secretos-vault-y-kms/README.md) |
| Contenedores e IaC | [243](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/243-imagenes-y-contenedores-seguros-en-el-pipeline/README.md), [227](../../classes/parte-10-seguridad-en-la-nube-y-contenedores/227-seguridad-de-contenedores-docker/README.md), [230](../../classes/parte-10-seguridad-en-la-nube-y-contenedores/230-seguridad-de-infrastructure-as-code-terraform/README.md), [229](../../classes/parte-10-seguridad-en-la-nube-y-contenedores/229-kubernetes-hardening-y-ataques/README.md) |
| Cadena de suministro | [246](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/246-supply-chain-security-sbom-y-slsa/README.md) |
| Policy as code | [244](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/244-politicas-como-codigo-con-opa/README.md) |
| Cultura y adopción | [248](../../classes/parte-11-devsecops-y-seguridad-del-sdlc/248-cultura-devsecops-y-security-champions/README.md), [330](../../classes/parte-17-profundizacion-para-certificaciones/330-analisis-de-codigo-y-automatizacion-de-seguridad/README.md) |

## 🧰 Herramientas y honestidad sobre la cobertura

El toolbox del laboratorio trae las herramientas de **auditoría**. Las de **construcción** de este
trayecto (SBOM, firma, policy as code) se instalan aparte y son opcionales por tramos:

| Capacidad | Herramienta de referencia | ¿Viene en el toolbox? |
|---|---|---|
| SAST | Bandit, Semgrep | Sí |
| SCA y escaneo de imagen | Trivy | Sí |
| Secretos | gitleaks | Sí |
| Dockerfile | hadolint | Sí |
| Workflows CI/CD | actionlint (zizmor si lo instalas) | Parcial |
| DAST | ZAP (imagen oficial) | No — se lanza por Docker |
| SBOM | Syft o Trivy (`--format cyclonedx`) | Trivy sí, Syft no |
| Firma y verificación | Cosign | No |
| Policy as code | OPA / Conftest | No |

Aplica aquí el mismo principio que el resto del laboratorio: **una capacidad que no pudiste ejecutar
no es una capacidad limpia**. Si no instalas Cosign, tu entrega dice "firma: no implementada", no
"firma: correcta".

## 1️⃣ Integrar los controles en el CI/CD

Coloca cada análisis donde su coste y su señal se compensan. Este es el criterio, y hay que poder
defenderlo:

| Control | Dónde | Por qué ahí |
|---|---|---|
| Escaneo de secretos | *pre-commit* + CI en cada *push* | Cuesta milisegundos y el daño es inmediato |
| SAST incremental | Cada *pull request*, solo sobre el diff | Rápido y con contexto de revisión |
| SAST completo | Nocturno sobre la rama principal | Caro; no debe frenar a nadie |
| SCA | Cada *push* y en cada cambio de *lockfile* | Es donde aparece la mayoría del riesgo real |
| IaC y Dockerfile | Cada *pull request* que los toque | Barato y de alto rendimiento |
| Escaneo de imagen | En el *build*, antes de publicar | Publicar una imagen vulnerable es propagarla |
| DAST | Contra el entorno de pruebas desplegado | Necesita la aplicación en marcha |

Un esqueleto de workflow con lo esencial (adáptalo a tu plataforma de CI):

```yaml
name: seguridad
on:
  pull_request:
  push:
    branches: ["main"]

# Mínimo privilegio explícito: por defecto, solo lectura.
permissions:
  contents: read

jobs:
  analisis:
    runs-on: ubuntu-latest
    steps:
      # Fija las acciones por SHA, no por etiqueta: una etiqueta se puede mover.
      - uses: actions/checkout@<sha-completo>

      - name: Secretos
        run: |
          docker run --rm -v "$PWD":/src zricethezav/gitleaks:v8.18.4 \
            detect --no-git --source /src -v

      - name: Dependencias e imagen base
        run: |
          docker run --rm -v "$PWD":/src aquasec/trivy:0.53.0 fs --exit-code 1 \
            --severity HIGH,CRITICAL /src

      - name: SAST
        run: |
          docker run --rm -v "$PWD":/src semgrep/semgrep:1.86.0 \
            semgrep --config auto --error /src
```

Tres decisiones que ya están tomadas en ese esqueleto y que debes saber justificar: **versiones
fijadas** (una herramienta que se autoactualiza pone tu CI en rojo sin que nadie toque el
repositorio), **`permissions` explícito y mínimo**, y **acciones fijadas por SHA**.

## 2️⃣ Definir el bloqueo proporcional

Un gate que bloquea todo se desactiva en un mes, y entonces la seguridad es cero. Define **tres
niveles** y escribe el porqué de cada umbral:

| Nivel | Qué lo activa | Efecto |
|---|---|---|
| **Bloquea el *merge*** | Secreto detectado · vulnerabilidad crítica **nueva** en dependencia directa · política de IaC violada | El *pull request* no se puede integrar |
| **Bloquea el despliegue a producción** | Imagen sin firmar · CVE crítica en KEV en el artefacto · SBOM ausente | Se construye pero no se publica |
| **Solo avisa** | Hallazgos medios y bajos · deuda preexistente · hallazgos de la rama nocturna | Comentario en el PR y entrada en el backlog |

La regla que hace viable todo lo anterior: **línea base**. El gate falla ante hallazgos **nuevos**,
no ante los preexistentes ya triados por el [Analista DevSecOps](TRAYECTO-ANALISTA-DEVSECOPS.md).
Sin línea base, el primer día bloqueas a toda la empresa y te ganas una excepción permanente.

## 3️⃣ Proteger los secretos y los permisos del pipeline

El pipeline es el sistema con más privilegio y menos vigilancia de la mayoría de las organizaciones.
Cuatro medidas, en orden de rentabilidad:

1. **Mínimo privilegio por *job*.** `permissions: contents: read` por defecto; sube solo lo que un
   *job* concreto necesite y solo en ese *job*.
2. **Identidad efímera en lugar de credenciales de larga vida.** Federación OIDC hacia la nube: el
   *job* obtiene un token de minutos en vez de guardar una clave permanente.

   ```yaml
   permissions:
     contents: read
     id-token: write     # habilita OIDC; nada más
   ```

3. **Aislamiento del disparador peligroso.** Un evento que ejecuta código de un *fork* con acceso a
   tus secretos es la vulnerabilidad clásica del CI. Si necesitas ese flujo, sepáralo en dos
   *workflows*: uno sin secretos que construye, otro con secretos que solo consume artefactos.
4. **Rotación probada.** Escribe y **ejecuta una vez** el procedimiento de rotación de un secreto.
   El día que se filtre uno de verdad no es el día de escribirlo.

Comprobación de la capa 6 del recorrido base sobre tu propio workflow:

```bash
docker compose exec auditor ./auditar.sh workflows
```

## 4️⃣ Cubrir las cinco superficies

Código propio, dependencias, IaC, imagen y aplicación en ejecución. Cada una ciega a lo que ven las
otras:

```bash
# Código propio y dependencias (dentro del toolbox)
docker compose exec auditor ./auditar.sh sast deps secrets dockerfile container

# IaC, si tu proyecto tiene Terraform o manifiestos de Kubernetes
docker run --rm -v "$PWD":/src aquasec/trivy config /src

# DAST contra la aplicación desplegada en tu entorno de pruebas
docker run --rm --network host ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py -t http://127.0.0.1:8080 -r zap.html
```

> 🔒 El objetivo del DAST debe ser **tu** aplicación de pruebas, en tu máquina. Apuntar un escáner
> dinámico a un sistema ajeno sin autorización escrita es un delito, no una práctica.

Entrega la **matriz de cobertura**: qué superficie cubre cada herramienta y —más importante— qué
queda sin cubrir. La lógica de negocio, por ejemplo, no la ve ninguna de las cinco.

## 5️⃣ Generar el SBOM

El SBOM no es un trámite de cumplimiento: es lo que te permite responder *"¿nos afecta?"* en minutos
cuando aparece una vulnerabilidad grave un domingo por la noche.

```bash
# Con Trivy (ya está en el toolbox)
docker compose exec auditor \
  trivy fs --format cyclonedx --output /audit/salida/sbom.cdx.json /audit/repo

# Con Syft, si lo instalas
syft dir:. -o cyclonedx-json=sbom.cdx.json
syft dir:. -o spdx-json=sbom.spdx.json
```

Tres requisitos para que sirva de algo:

- **Uno por artefacto y por versión**, no uno por proyecto.
- **Conservado** donde se pueda consultar meses después; un SBOM que se genera y se descarta en el
  mismo *job* es trabajo perdido.
- **Consultable**: prueba que puedes responder "¿en qué artefactos aparece este paquete?" a partir
  de tus SBOM, con `jq` o con lo que uses. Si no puedes, todavía no tienes un inventario.

## 6️⃣ Firmar y verificar

Firmar responde a una pregunta que ningún escáner responde: **¿lo que corre en producción es lo que
construiste?**

```bash
# Firmar (modo sin claves: la identidad viene del proveedor OIDC)
cosign sign-blob --yes artefacto.tar.gz --bundle artefacto.bundle

# Verificar en el punto de despliegue
cosign verify-blob artefacto.tar.gz \
  --bundle artefacto.bundle \
  --certificate-identity-regexp '^https://github\.com/TU-ORG/.+$' \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

La parte que convierte esto en un control y no en un adorno: **el despliegue debe fallar si la
verificación falla**. Demuéstralo — modifica un byte del artefacto y enseña el rechazo.

Sobre **SLSA**: no intentes saltar al nivel máximo. Sube un escalón y demuéstralo: build
reproducible desde el código fuente, procedencia generada automáticamente por el propio sistema de
CI (no por una persona) y verificación en el consumo. Documenta en qué nivel estás y qué falta para
el siguiente.

## 7️⃣ Policy as code

Una política escrita en un documento se ignora; escrita como código se revisa, se versiona y se
prueba como cualquier otra cosa.

`policy/kubernetes.rego`:

```rego
package kubernetes.security

import rego.v1

deny contains msg if {
    input.kind == "Deployment"
    c := input.spec.template.spec.containers[_]
    not c.securityContext.runAsNonRoot
    msg := sprintf("El contenedor '%s' no declara runAsNonRoot", [c.name])
}

deny contains msg if {
    input.kind == "Deployment"
    c := input.spec.template.spec.containers[_]
    endswith(c.image, ":latest")
    msg := sprintf("El contenedor '%s' usa la etiqueta ':latest'", [c.name])
}
```

`policy/kubernetes_test.rego`:

```rego
package kubernetes.security_test

import rego.v1
import data.kubernetes.security

test_rechaza_root if {
    count(security.deny) == 1 with input as {
        "kind": "Deployment",
        "spec": {"template": {"spec": {"containers": [
            {"name": "api", "image": "api:1.4.2"}
        ]}}}
    }
}
```

Ejecución:

```bash
opa test policy/ -v                       # las políticas también se prueban
conftest test k8s/deployment.yaml -p policy/
```

Regla de oficio: **una política sin pruebas es una política que algún día bloqueará lo que no
debía**. Y las pruebas son, además, la documentación que entiende quien desarrolla.

## 8️⃣ Excepciones auditables y temporales

Si tu gate no tiene válvula, la válvula la construirá otro: desactivándolo. Diséñala tú.

`.security-exceptions.yml` en el repositorio, revisado como código:

```yaml
- id: EXC-2026-011
  regla: trivy/CVE-2023-88888
  ambito: servicios/facturacion
  motivo: sin versión corregida publicada; sustitución estimada en 3 semanas
  solicita: equipo-pagos
  aprueba: jefatura-ingenieria
  compensacion: endpoint restringido a red interna + validación estricta de entrada
  vence: 2026-11-30
```

Cuatro propiedades que la hacen aceptable:

- **Vive en el repositorio** y se cambia por *pull request*: hay historial y hay revisor.
- **Tiene ámbito**, no es global. Una excepción global es desactivar el control.
- **Caduca sola.** El pipeline debe **fallar** cuando una excepción vence, no ignorarla en silencio.
- **Es visible**: se lista en el informe periódico junto con las que están por vencer.

Implementa la comprobación de vencimiento y demuéstrala: pon una fecha pasada y enseña el fallo.

## 9️⃣ Demostrar la reversión de un control defectuoso

El paso que separa a quien construye plataformas de quien añade pasos a un YAML. Tu control **va a
fallar** algún día; lo que se evalúa es cómo se comporta la plataforma ese día.

Ejercicio completo:

1. **Introduce el fallo a propósito.** Por ejemplo, una regla de SAST demasiado amplia que marca
   como crítico un patrón legítimo y frecuente, o un umbral de severidad que bloquea todo.
2. **Detéctalo.** ¿Cuánto tardas en enterarte? ¿Te lo dice tu monitorización del pipeline o te lo
   dice alguien enfadado en un chat? Registra el tiempo real.
3. **Decide.** Tres opciones, y hay que elegir con criterio: revertir la regla, degradarla a modo
   aviso, o emitir una excepción de ámbito amplio y temporal. Escribe por qué eliges la tuya.
4. **Revierte.** Con el control de versiones, no editando en caliente. El *commit* de reversión debe
   explicar qué pasó.
5. **Comunica.** Un mensaje corto: qué se rompió, a quién afectó, qué se hizo, qué falta.
6. **Postmortem sin culpables.** Causa raíz y **una** mejora concreta: pruebas de la regla contra un
   corpus antes de activarla, despliegue por fases, o modo aviso obligatorio durante una semana.

Métricas del ejercicio: **tiempo hasta la detección**, **tiempo hasta la reversión** y **número de
equipos afectados**. Anótalas. Son exactamente las que te van a preguntar en una entrevista.

## 🏆 Retos verificables

1. **Pipeline completo funcionando.** *Aceptación:* otra persona clona tu repositorio, lo ejecuta y
   obtiene el mismo resultado, con los tiempos de cada etapa medidos y publicados.
2. **Bloqueo proporcional documentado.** *Aceptación:* tres niveles con umbral y justificación, y
   una línea base que no bloquea la deuda preexistente.
3. **Cero credenciales de larga vida.** *Aceptación:* enumeras cada secreto del pipeline, su tiempo
   de vida y su vía de rotación; o demuestras la federación OIDC funcionando.
4. **Cinco superficies cubiertas.** *Aceptación:* matriz de cobertura que incluye **qué queda
   fuera**.
5. **SBOM consultable.** *Aceptación:* respondes "¿en qué artefactos está este paquete?" a partir de
   tus SBOM, con el comando incluido en la entrega.
6. **Firma que realmente bloquea.** *Aceptación:* enseñas el despliegue rechazando un artefacto
   manipulado.
7. **Política con pruebas.** *Aceptación:* `opa test` pasa y la política rechaza un manifiesto real
   del laboratorio.
8. **Excepción que caduca.** *Aceptación:* con una fecha pasada, el pipeline falla; con una futura,
   pasa; y la excepción aparece en el informe.
9. **Reversión ensayada.** *Aceptación:* entregas los tres tiempos, el *commit* de reversión, el
   mensaje de comunicación y el postmortem de una página.
10. **Adopción medida.** *Aceptación:* das el porcentaje de proyectos que usan tu plantilla y el
    tiempo que añade al pipeline. Una capacidad que nadie usa no existe.

## 🔗 Cómo se conecta

- 📖 Ruta completa: [Ingeniero DevSecOps](../../rutas/devsecops-engineer.md)
- 🧮 La otra mitad del oficio:
  [Trayecto Analista DevSecOps](TRAYECTO-ANALISTA-DEVSECOPS.md) — quien convierte en decisiones lo
  que tu tubería produce
- 🗺️ [Matriz de roles SecOps y DevSecOps](../../docs/matriz-roles-secops-devsecops.md)
- 🎓 [Examen final por rol](../../docs/examen-final-por-rol.md) — el examen de Ingeniero DevSecOps
  usa este trayecto
- 🧪 Laboratorios vecinos: [`cloud-security`](../cloud-security/README.md) ·
  [`appsec-code`](../appsec-code/README.md) · [`appsec-web`](../appsec-web/README.md)
- 📚 Referencias: SLSA — <https://slsa.dev/> · OpenSSF — <https://openssf.org/> ·
  CycloneDX — <https://cyclonedx.org/> · SPDX — <https://spdx.dev/> ·
  OWASP Top 10 CI/CD — <https://owasp.org/www-project-top-10-ci-cd-security-risks/>
- ⬅️ [Volver al laboratorio](README.md) · 🧪 [Índice de laboratorios](../README.md)
