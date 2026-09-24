# 📨 Responsable de divulgación coordinada de vulnerabilidades

> También aparece como **Vulnerability Disclosure Coordinator**, **CVD Coordinator**,
> **VDP/PSIRT Analyst** o responsable de *vulnerability intake*. No es una traducción elegante
> de «publicar fallos»: es la función que convierte un reporte sensible en una corrección coordinada.

## 🧭 Qué es y por qué importa

La persona responsable de **divulgación coordinada de vulnerabilidades (CVD)** recibe reportes,
confirma que contienen evidencia suficiente, localiza a los propietarios técnicos, protege la
información previa a la publicación y mantiene a investigador, proveedor, desplegadores y, cuando
corresponde, a un coordinador externo trabajando sobre el mismo caso. Su producto no es un
hallazgo: es una **decisión trazable** que termina en mitigación, aviso o cierre justificado.

El nombre «Responsible Disclosure» sigue usándose en ofertas y programas, pero esta ruta prefiere
**divulgación coordinada**. «Responsable» puede sugerir que una sola parte decide qué conducta es
correcta; «coordinada» deja claro que descubridor, reportante, proveedor, desplegador y coordinador
pueden ser actores distintos. CERT/CC separa precisamente esos roles y advierte que una persona u
organización puede desempeñar varios a la vez.

Este rol no autoriza investigación fuera de alcance, no promete una recompensa y no decide por sí
solo que un producto es seguro. Tampoco es gestión ordinaria de vulnerabilidades: aquella prioriza
fallos conocidos en los activos propios; CVD gestiona información potencialmente nueva entre
organizaciones antes y durante su corrección.

## 🗓️ Un caso de principio a fin

1. **Ingreso seguro:** acusa recibo sin prometer severidad, pago ni fecha; asigna identificador y
   restringe el acceso al material.
2. **Completitud y alcance:** comprueba producto, versión, configuración, pasos, resultado esperado,
   resultado observado e impacto alegado. Separa un reporte incompleto de uno no válido.
3. **Reproducción segura:** entrega la prueba al equipo capaz de validarla en un entorno controlado;
   nunca pide al reportante que aumente el impacto sobre producción.
4. **Triaje:** registra afectados, explotabilidad observada, exposición, impacto y dependencias. Una
   puntuación CVSS ayuda a describir severidad, pero no sustituye el contexto ni decide el calendario.
5. **Propiedad y coordinación:** identifica mantenedores, productos derivados y desplegadores; fija
   responsables, canales, hitos y una siguiente actualización verificable.
6. **Remediación:** sigue parche, mitigación, pruebas de regresión y distribución. «Código corregido»
   no equivale a «usuarios protegidos».
7. **Publicación coordinada:** acuerda contenido y fecha según riesgo, disponibilidad del arreglo,
   explotación conocida y capacidad de desplegar. Un plazo es una política, no una ley universal.
8. **Cierre y aprendizaje:** conserva la cronología, acredita a quien corresponda, mide tiempos sin
   incentivar cierres falsos y convierte fricciones recurrentes en cambios del VDP o del producto.

La evidencia mínima del caso es: reporte original inmutable, registro de comunicaciones, hipótesis
de impacto, resultado de reproducción, decisiones con autor y fecha, activos/versiones afectados,
mitigación o parche verificado, aviso final y asuntos que quedaron inciertos.

## 🧠 Qué necesitas saber

### Conocimiento técnico

- Redes, sistemas, web, APIs y lectura de código suficiente para hacer preguntas precisas y enviar
  el caso al propietario correcto.
- Reproducción en laboratorios aislados, manejo de PoC, versiones, configuraciones y regresiones.
- CVE/CWE/CVSS, sin confundir identificación, debilidad, severidad y prioridad operacional.
- Cadenas de suministro: una biblioteca puede exigir coordinar al mantenedor, integradores,
  distribuidores y operadores con calendarios distintos.
- Cifrado de comunicaciones, control de acceso, retención y saneamiento de artefactos sensibles.

### Criterio y comunicación

- Redactar acuses y actualizaciones que expliquen el siguiente paso sin divulgar información de más.
- Distinguir hecho reproducido, afirmación del reportante, hipótesis e impacto todavía desconocido.
- Mediar desacuerdos sobre reproducibilidad, severidad, crédito y fecha de publicación.
- Escalar a legal, privacidad, seguridad de producto, dirección o un CERT cuando el caso lo requiere,
  sin convertirlos en sustitutos del análisis técnico.
- Diseñar un VDP con alcance, canal, expectativas, *safe harbor* aplicable y rutas para emergencias.

## 📚 Tu ruta en el programa

1. 📚 [**Parte 0 — Fundamentos**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md):
   sistemas, redes, Git, criptografía base y, sobre todo,
   [025 — Ética, legalidad, alcance y divulgación](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md).
2. 📚 [**Parte 3 — Pentesting**](../classes/parte-3-hacking-etico-y-pentesting-metodologia/README.md):
   066–067 para mandato y alcance, 071 para validación y 084–085 para priorización y reporte.
3. 📚 [**Parte 4 — Seguridad web**](../classes/parte-4-seguridad-de-aplicaciones-web/README.md):
   087, 110, 114 y 115 para comprender reportes frecuentes, programas de bounty y corrección.
4. 📚 [**Partes 8 y 9**](../classes/parte-8-blue-team-deteccion-y-soc/README.md): 195 para
   inteligencia y 202, 215–217 para coordinación, contención y aprendizaje del incidente.
5. 📚 [**Parte 11 — DevSecOps**](../classes/parte-11-devsecops-y-seguridad-del-sdlc/README.md):
   236–246 para llevar el reporte hasta código, dependencias, pipeline, SBOM y procedencia.
6. 📚 [**Partes 14 y 17**](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md): 277,
   282, 284–285, 318, 320–322 y 324 para riesgo, terceros, auditoría, gobierno y hardening.

Práctica recomendada: usa [`appsec-code`](../labs/appsec-code/README.md) para reproducir y corregir
un fallo, [`devsecops-pipeline`](../labs/devsecops-pipeline/README.md) para comprobar que el arreglo
llega al artefacto y [`blue-team-soc`](../labs/blue-team-soc/README.md) para ensayar la respuesta si
ya existe explotación. Toda la evidencia debe ser sintética o pertenecer a un entorno autorizado.

## 🎯 Portafolio verificable

Construye un expediente CVD ficticio con: política de divulgación, formulario de ingreso, reporte
técnico, matriz de actores, bitácora, decisión de triaje, plan de coordinación, borrador de aviso,
prueba del arreglo y retrospectiva. Introduce deliberadamente un proveedor no responsivo y una
dependencia compartida para demostrar cuándo pedirías ayuda a un coordinador externo.

Se evalúa que un tercero pueda reconstruir **qué se sabía en cada momento**, por qué se compartió
información con cada actor y qué evidencia permitió cerrar. No se evalúa que el calendario sea corto.

## 🎓 Certificaciones

No hay una certificación universal que defina esta función. **Security+** o **CySA+** sirven como
base; formación en respuesta a incidentes, seguridad de producto, PSIRT y normas ISO/IEC 29147 y
30111 completa el perfil. Para puestos senior pesan más expedientes bien coordinados, capacidad de
negociación y comprensión de producto que una insignia aislada.

## 📈 Progresión de carrera y salario

La función suele aparecer dentro de **PSIRT**, Product Security, CSIRT/CERT, AppSec o Vulnerability
Management, no siempre como un puesto independiente. Una progresión razonable es:

1. Analista de ingreso y triaje de reportes.
2. Analista PSIRT / coordinador CVD de un producto.
3. Coordinador multiparte o responsable del VDP y sus métricas.
4. Product Security Manager, PSIRT Lead o coordinación sectorial/nacional.

El salario depende del país, sector, criticidad del producto, guardias y amplitud del mandato. No se
publica una cifra global porque mezclar analista PSIRT, responsable legal-operativo y coordinador
nacional produciría una comparación engañosa. Al evaluar una oferta, comprueba autoridad para
convocar a ingeniería, presupuesto, cobertura horaria, responsabilidad de publicación y apoyo legal.

## ⚠️ Mitos y errores comunes

- **«Responsible disclosure significa publicar a los 90 días.»** Un plazo fijo puede ser una
  política válida, pero la coordinación considera explotación, parche, cadena de suministro y riesgo.
- **«Si tiene CVE, el caso terminó.»** El identificador no parchea ni despliega nada.
- **«El coordinador decide la verdad.»** Facilita, conserva evidencia y hace explícitos los
  desacuerdos; no reemplaza a proveedor, investigador, desplegador ni autoridad legal.
- **«Un reporte incompleto es falso.»** Puede requerir datos adicionales. La credibilidad y la
  completitud se evalúan sin castigar a quien reporta de buena fe.
- **«Cifrar el correo resuelve la confidencialidad.»** Quedan permisos, copias, tickets, logs,
  retención, reuniones y destinatarios; el canal es solo una parte del control.
- **«Cerrar rápido es rendir bien.»** Incentiva rechazos prematuros. Mide acuse, tiempo hasta
  propietario, reproducción, mitigación disponible, adopción y calidad de comunicación por separado.

## 📎 Fuentes primarias

- CERT/CC, **Roles in Coordinated Vulnerability Disclosure** —
  <https://certcc.github.io/CERT-Guide-to-CVD/topics/roles/>
- CERT/CC, **Reporter Vulnerability Response Process** —
  <https://certcc.github.io/CERT-Guide-to-CVD/tutorials/response_process/reporter/>
- FIRST, **CSIRT Services Framework 2.1** —
  <https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2-1>
- ISO/IEC 29147, *Vulnerability disclosure* — <https://www.iso.org/standard/72311.html>
- ISO/IEC 30111, *Vulnerability handling processes* — <https://www.iso.org/standard/69725.html>

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Investigador de seguridad](investigador-seguridad.md) ·
  [AppSec / Bug Bounty](appsec.md) · [Gestión de vulnerabilidades](gestion-vulnerabilidades.md)
- 🏠 [Inicio del programa](../README.md)
