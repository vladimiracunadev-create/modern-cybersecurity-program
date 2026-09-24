# 🔬 Investigador/a de seguridad

> **Security Researcher** es una familia de especialidades, no el sinónimo de pentester ni una
> licencia para probar sistemas ajenos. Esta ruta se centra en investigación técnica reproducible
> de vulnerabilidades, protocolos, software, firmware, malware y controles de seguridad.

## 🧭 Qué es y por qué importa

Un investigador de seguridad formula una pregunta que todavía no tiene respuesta suficiente,
construye un entorno donde pueda ponerla a prueba, obtiene evidencia y comunica el resultado con
sus límites. Puede descubrir una vulnerabilidad, demostrar que una mitigación falla, caracterizar
una familia de malware o medir una superficie nueva. El trabajo termina cuando otra persona puede
**reproducir o refutar** la conclusión, no cuando aparece una captura espectacular.

Se diferencia del pentester por el contrato de salida: el pentester evalúa un alcance y plazo para
un cliente; el investigador profundiza una pregunta y puede producir PoC, corpus, herramienta,
artículo o reporte CVD. Se diferencia de Threat Intelligence porque estudia mecanismos técnicos,
no principalmente actores y campañas. Y se diferencia de quien coordina divulgación: puede ser el
**descubridor** y el **reportante**, mientras el coordinador mantiene alineadas a las partes.

La autorización sigue siendo el primer control. Un producto comprado, un servicio visible o una
hipótesis interesante no conceden permiso ilimitado. Se investiga en activos propios, entornos
aislados, código con licencia compatible o programas cuya política autoriza exactamente la prueba.

## 🧪 El método de investigación

1. **Pregunta y amenaza:** formula qué propiedad estudias, para quién importa y qué observación
   refutaría tu hipótesis.
2. **Mandato y límites:** documenta propiedad, licencia, alcance, técnicas permitidas, datos y
   criterio de parada antes de ejecutar pruebas.
3. **Estado del arte:** consulta especificaciones, código, avisos y trabajos previos. Distingue una
   novedad real de una variante ya conocida.
4. **Laboratorio reproducible:** fija versiones, configuración, arquitectura, entradas, reloj y
   red. Aísla la ejecución y conserva un estado limpio restaurable.
5. **Experimento mínimo:** cambia una variable, incluye control negativo y captura evidencia
   suficiente. Una caída no demuestra explotabilidad; una coincidencia no demuestra causalidad.
6. **Reducción y análisis:** elimina pasos accidentales hasta obtener el caso mínimo y explica el
   mecanismo causal, precondiciones e impacto plausible.
7. **Validación independiente:** repite desde un entorno limpio y, cuando sea seguro, pide revisión
   sin revelar datos que expongan a usuarios.
8. **Comunicación:** si hay vulnerabilidad no corregida, inicia CVD. Publica método, versiones,
   límites y mitigaciones sin convertir el resultado en una receta de daño innecesaria.

## 🧠 Qué necesitas saber

### Base transversal

- Sistemas operativos, procesos, memoria, permisos, redes, protocolos, criptografía aplicada y al
  menos Python y un lenguaje cercano al dominio investigado.
- Git, automatización, pruebas, contenedores o VMs y captura de metadatos del entorno.
- Estadística descriptiva y diseño experimental básico: muestras, sesgos, controles y repetición.
- Lectura de especificaciones y código; búsqueda bibliográfica y trazabilidad de afirmaciones.
- Ética, licencias, privacidad, manejo de datos y divulgación coordinada.

### Especializaciones posibles

- **Vulnerability research:** fuzzing, depuración, sanitizers, análisis de causa y PoC mínimo.
- **Binarios y hardware:** ensamblador, ABI, reversing, firmware, buses e instrumentación.
- **Web, nube e identidad:** protocolos, lógica, aislamiento multi-tenant y modelos de autorización.
- **Malware:** análisis estático/dinámico, desempaquetado, comportamiento y atribución prudente.
- **Defensa:** evaluación de detecciones, telemetría, evasiones en laboratorio y regresiones.
- **IA y sistemas emergentes:** modelos de amenaza, evaluaciones repetibles y límites de inferencia.

No hace falta dominar todas. Un perfil en forma de T combina fundamentos anchos con profundidad
demostrable en una o dos superficies.

## 📚 Tu ruta en el programa

1. 📚 [**Parte 0 completa**](../classes/parte-0-fundamentos-y-prerrequisitos/README.md):
   laboratorio aislado, Linux/Windows, redes, Python, Git, arquitectura y legalidad.
2. 📚 [**Partes 1 y 2**](../classes/parte-1-redes-y-seguridad-de-redes/README.md): protocolos,
   captura, criptografía y errores de implementación para formular hipótesis con fundamento.
3. Elige profundidad principal: [**Parte 4**](../classes/parte-4-seguridad-de-aplicaciones-web/README.md)
   para web/API; [**Parte 5**](../classes/parte-5-explotacion-de-sistemas-y-binarios/README.md) para binarios;
   [**Parte 6**](../classes/parte-6-analisis-de-malware/README.md) para malware; o
   [**Parte 13**](../classes/parte-13-seguridad-movil-iot-e-inalambrica/README.md) para móvil, IoT y firmware.
4. 📚 [**Parte 7**](../classes/parte-7-red-team-y-operaciones-ofensivas/README.md) y
   [**Parte 8**](../classes/parte-8-blue-team-deteccion-y-soc/README.md): relaciona mecanismo,
   telemetría, detección y límites de evasión sin convertir una técnica en una conclusión universal.
5. 📚 [**Partes 11, 15 y 18**](../classes/parte-11-devsecops-y-seguridad-del-sdlc/README.md):
   automatiza pruebas y cubre cadena de suministro, IA y asistencia responsable por agentes.
6. Vuelve siempre a [**025**](../classes/parte-0-fundamentos-y-prerrequisitos/025-etica-legalidad-alcance-y-divulgacion-responsable/README.md)
   y enlaza el hallazgo con la ruta de
   [divulgación coordinada](divulgacion-responsable.md) antes de contactar o publicar.

Los laboratorios [`appsec-code`](../labs/appsec-code/README.md),
[`dfir-memoria`](../labs/dfir-memoria/README.md), [`pwn-binarios`](../labs/pwn-binarios/README.md) y
los [CTF](../ctf/README.md) ofrecen material autorizado. Un CTF enseña técnicas; para convertirlo en
investigación debes añadir pregunta, controles, repetibilidad, análisis causal y límites.

## 🎯 Portafolio verificable

Entrega un repositorio que permita reconstruir un hallazgo sintético desde cero:

- pregunta, amenaza, alcance y criterio de parada;
- manifiesto de versiones y script de construcción del laboratorio;
- corpus o entrada mínima sin datos de terceros;
- experimento con control positivo y negativo;
- logs, hashes y resultado repetido desde estado limpio;
- análisis de causa, precondiciones, impacto y explicaciones alternativas;
- prueba de corrección o mitigación y test de regresión;
- reporte privado simulado y artículo público posterior que explique qué se omitió y por qué.

No incluyas secretos, malware operativo, datos personales ni instrucciones que amplíen el daño
sin aportar capacidad defensiva. Reproducible no significa irresponsablemente armado.

## 🎓 Certificaciones

No existe una certificación única para «Security Researcher». **Security+** puede acreditar base;
**OSCP/OSED**, formación de reversing, web, cloud o DFIR puede ordenar una especialidad. Para este
rol pesan más un artículo reproducible, contribuciones revisadas, CVE bien documentados, herramientas
con pruebas y una divulgación profesional que acumular certificaciones desconectadas.

## 📈 Progresión de carrera y salario

La entrada suele ser desde desarrollo, AppSec, pentesting, detección, malware o academia:

1. Analista o ingeniero que reproduce y reduce fallos conocidos.
2. Investigador junior responsable de experimentos acotados y documentación.
3. Investigador con una especialidad, publicaciones y coordinación de hallazgos propios.
4. Senior/principal que define agendas, revisa riesgo y forma a otros; o líder de research.

El salario varía demasiado entre universidad, fabricante, laboratorio de producto, consultora y
equipo interno como para dar una cifra global honesta. Compara mandato para publicar, propiedad
intelectual, tiempo protegido de investigación, acceso a laboratorio, bonos por hallazgo y guardias.
Un cargo llamado «researcher» que solo ejecuta escáneres no ofrece la misma progresión.

## ⚠️ Mitos y errores comunes

- **«Investigar es probar cosas hasta que algo cae.»** Sin hipótesis, controles y reducción solo hay
  una observación difícil de interpretar.
- **«Una PoC demuestra impacto máximo.»** Demuestra lo que ejecutó bajo esas precondiciones; el
  resto debe justificarse o declararse como hipótesis.
- **«Si está en Internet, se puede investigar.»** Visibilidad no es autorización.
- **«Kali convierte a alguien en investigador.»** Una distribución empaqueta herramientas; el
  trabajo está en la pregunta, el mecanismo, la evidencia y la comunicación.
- **«Más herramientas producen mejor cobertura.»** Aumentan superficie de mantenimiento y ruido.
  Instala lo necesario y registra versiones.
- **«Publicar primero prueba autoría.»** Puede exponer usuarios antes de una mitigación. Conserva
  evidencia fechada y usa CVD.
- **«No pude reproducirlo, luego es falso.»** Puede faltar una precondición. Documenta el entorno,
  pide datos concretos y distingue no reproducido de refutado.

## 📎 Fuentes primarias

- CERT/CC, **Roles in Coordinated Vulnerability Disclosure** —
  <https://certcc.github.io/CERT-Guide-to-CVD/topics/roles/>
- CERT/CC, **Reporter Vulnerability Response Process** —
  <https://certcc.github.io/CERT-Guide-to-CVD/tutorials/response_process/reporter/>
- ISO/IEC 29147, *Vulnerability disclosure* — <https://www.iso.org/standard/72311.html>
- NIST SP 800-115, *Technical Guide to Information Security Testing and Assessment* —
  <https://csrc.nist.gov/pubs/sp/800/115/final>
- OWASP Web Security Testing Guide — <https://owasp.org/www-project-web-security-testing-guide/>

---

- ⬅️ [Volver al índice de rutas](./README.md)
- 🔀 Rutas vecinas: [Divulgación coordinada](divulgacion-responsable.md) ·
  [Pentester](pentester.md) · [AppSec / Bug Bounty](appsec.md) ·
  [Threat Intelligence](threat-intelligence-analyst.md)
- 🏠 [Inicio del programa](../README.md)
