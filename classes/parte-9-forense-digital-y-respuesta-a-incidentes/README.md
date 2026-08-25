# Parte 9 — Forense digital y respuesta a incidentes

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏭️ Parte siguiente](../parte-10-seguridad-en-la-nube-y-contenedores/README.md)

**20 clases** · rango 201–220 · DFIR, adquisición, memoria, timelines y playbooks

**Fuentes de referencia de esta parte:**

- Michael Hale Ligh, Andrew Case, Jamie Levy, AAron Walters — *The Art of Memory Forensics* (Wiley, 2014).
- Brian Carrier — *File System Forensic Analysis* (Addison-Wesley, 2005).
- Scott J. Roberts, Rebekah Brown — *Intelligence-Driven Incident Response* (O'Reilly, 2017).
- NIST SP 800-61 Rev. 3 — *Incident Response Recommendations and Considerations for Cybersecurity Risk Management*.
- NIST SP 800-86 — *Guide to Integrating Forensic Techniques into Incident Response*.
- RFC 3227 — *Guidelines for Evidence Collection and Archiving*.

---

## 🎯 ¿De qué trata esta parte?

La forense digital y la respuesta a incidentes (DFIR, por *Digital Forensics and Incident Response*) reúne dos capacidades relacionadas, pero no idénticas. La respuesta limita impacto, coordina decisiones y recupera servicios; la forense preserva e interpreta rastros para explicar hechos con un método reproducible. Ambas pueden activarse ante una intrusión, fraude, pérdida de datos, abuso interno o fallo operativo. No se parte de que la prevención «falló por completo» ni de que toda alerta represente un atacante: se parte de una pregunta, una autoridad y evidencia cuya calidad todavía debe evaluarse.

DFIR es donde convergen la técnica pura (entender NTFS a nivel de MFT, leer estructuras de kernel en un volcado de RAM) y el rigor de proceso (cadena de custodia, integridad por hash, documentación defendible). Un hallazgo brillante no sirve de nada si la evidencia se contamina o si el informe no se sostiene. Por eso trabajamos con herramientas reales y reproducibles —Autopsy, The Sleuth Kit, Volatility 3, FTK Imager, plaso/log2timeline, Wireshark— y con marcos reconocidos como el ciclo de NIST SP 800-61 y el PICERL de SANS.

Esta parte sirve a analistas de SOC que quieren pasar de la alerta al análisis profundo, a respondedores de incidentes, a peritos forenses y a cualquier ingeniero de seguridad que deba justificar qué hacer durante las primeras horas de un incidente. Construimos sobre lo aprendido en detección y SOC (Parte 8) y preparamos el terreno para la nube (Parte 10), donde parte de la evidencia depende de APIs, retención configurada y cooperación del proveedor.

## 🧩 Problemas que resuelve

- Cómo capturar un disco o la memoria de un equipo comprometido sin alterar la evidencia ni romper la cadena de custodia.
- Cómo reconstruir la actividad de un usuario o un atacante a partir de artefactos del sistema de archivos y del sistema operativo.
- Cómo investigar procesos, credenciales y contenido que pueden existir en memoria aunque el disco no conserve un artefacto equivalente.
- Cómo ordenar cientos de miles de eventos dispersos en una única línea de tiempo coherente.
- Cómo contener y erradicar una amenaza sin destruir los datos que necesitas para el análisis.
- Cómo escribir un informe forense y una cadena de custodia que resistan escrutinio legal.
- Cómo ensayar la respuesta antes de que ocurra el incidente real mediante ejercicios de mesa.

## 🎓 Resultados de aprendizaje

Al terminar la parte, el alumno podrá:

1. Explicar y aplicar el principio de intercambio de Locard y el orden de volatilidad en una adquisición real.
2. Adquirir imágenes forenses de disco y memoria verificando integridad con hashes y bloqueo de escritura.
3. Analizar sistemas de archivos NTFS y ext4 a nivel de metadatos (MFT, journal, inodos).
4. Extraer y correlacionar artefactos de Windows y Linux para reconstruir actividad.
5. Analizar volcados de memoria con Volatility 3 para hallar procesos, conexiones e inyecciones.
6. Construir super-timelines con plaso/log2timeline y analizarlas con criterio.
7. Redactar playbooks de respuesta y ejecutar el ciclo completo PICERL/NIST.
8. Producir un informe forense defendible y coordinar un ejercicio tabletop.

## 🧱 Prerrequisitos

- **Parte 8 — Blue Team, detección y SOC**: comprender alertas, SIEM, logs y telemetría de endpoint es la base para saber qué evidencia buscar.
- **Parte 2 — Sistemas operativos y redes**: manejo de Windows, Linux, sistemas de archivos y TCP/IP.
- **Parte 1 — Fundamentos**: criptografía básica (hashes) y línea de comandos.
- Un entorno de laboratorio aislado (máquinas virtuales) para practicar adquisición y análisis sin riesgo.

## 🗺️ Estructura temática

| Bloque | Clases | Enfoque |
|--------|--------|---------|
| Fundamentos y proceso | 201–202 | Cadena de custodia, ciclo NIST/SANS |
| Adquisición | 203 | Imágenes de disco y memoria |
| Análisis de sistemas de archivos | 204 | NTFS y ext4 |
| Artefactos del SO | 205–206 | Windows y Linux |
| Memoria y red | 207–208 | Volatility y forense de red |
| Timelines | 209 | Super-timelines con plaso |
| Fuentes específicas | 210–212 | Navegadores/correo, móvil, nube |
| Técnicas avanzadas | 213–214 | Anti-forense, carving |
| Ciclo de respuesta | 215–217 | Playbooks, contención, RCA |
| Cierre profesional | 218–220 | Informe/legal, tabletop, caso end-to-end |

## 📚 Recorrido explicado, clase por clase

La progresión sigue una pregunta profesional: **¿cómo se pasa de una señal incierta a una decisión justificada y a una explicación defendible preservando la evidencia pertinente?** Las clases no son técnicas aisladas. Cada una añade una fuente, una decisión o un control que la siguiente necesita.

**[Clase 201 — Fundamentos de DFIR y cadena de custodia](201-fundamentos-de-dfir-y-cadena-de-custodia/README.md).** Distingue responder de investigar y explica por qué hash, cadena de custodia, autorización y notas contemporáneas resuelven problemas diferentes. RFC 3227 aporta el orden de volatilidad como guía adaptable, no como una receta que ignore seguridad o continuidad. La evidencia es un formulario de custodia, una copia verificada y una explicación de qué demuestra —y qué no demuestra— su hash.

**[Clase 202 — Ciclo de respuesta NIST y SANS](202-el-ciclo-de-respuesta-a-incidentes-nist-y-sans/README.md).** Ubica la respuesta dentro de las seis funciones de CSF 2.0 siguiendo NIST SP 800-61 Rev. 3. PICERL se conserva como mnemotecnia pedagógica, pero el alumno aprende que análisis, contención y recuperación pueden retroalimentarse. La evidencia es una matriz de severidad, roles, autoridad, criterios de transición y bitácora de decisiones.

**[Clase 203 — Adquisición forense](203-adquisicion-forense-discos-e-imagenes/README.md).** Convierte la pregunta investigativa en una estrategia de adquisición física, lógica o en vivo. Explica formatos, bloqueo de escritura, errores de lectura, cifrado, SSD/TRIM y el efecto inevitable de adquirir un sistema activo. La evidencia es una imagen o colección reproducible con hashes, logs, parámetros, excepciones y copia de trabajo separada.

**[Clase 204 — NTFS y ext4](204-forense-de-sistemas-de-archivos-ntfs-y-ext4/README.md).** Enseña a leer un sistema de archivos como relaciones entre nombres, registros, inodos, bloques y transacciones. Compara MFT, atributos NTFS, USN, extents y journal ext4 sin tratar ningún journal como auditoría completa. La evidencia es una timeline de metadatos donde cada tiempo conserva su semántica y procedencia.

**[Clase 205 — Artefactos de Windows](205-analisis-de-artefactos-de-windows/README.md).** Desarrolla Registry, Prefetch, Amcache, Shimcache, LNK, Jump Lists, ShellBags y EVTX como subproductos con condiciones de generación y retención. El alumno deja de usar «aparece aquí, por tanto ocurrió» y aprende a corroborar presencia, ejecución e interacción. La evidencia es una hipótesis sostenida por artefactos independientes y alternativas explícitas.

**[Clase 206 — Artefactos de Linux](206-analisis-de-artefactos-de-linux/README.md).** Reconstruye sesiones, privilegios, persistencia y cambios usando journal, syslog, audit, wtmp/btmp, shell, SSH, cron, systemd y metadatos. Explica cómo distribución, rotación, almacenamiento volátil y opciones de montaje cambian lo observable. La evidencia es una timeline normalizada por boot, host, usuario y reloj.

**[Clase 207 — Memoria RAM con Volatility 3](207-forense-de-memoria-ram-con-volatility/README.md).** Enseña primero qué conserva una instantánea de RAM y cómo la adquisición modifica el estado; después introduce capas, símbolos y plugins. Procesos, sockets, regiones y módulos son observaciones que deben relacionarse, no etiquetas automáticas de malware. La evidencia es un cuaderno reproducible con hash, símbolos, comandos, salidas y artefactos extraídos.

**[Clase 208 — Forense de red](208-forense-de-red/README.md).** Compara PCAP, flujo y logs de protocolo según detalle, alcance y posición del sensor. Explica reensamblado, pérdida, NAT, TLS, objetos transferidos, beaconing y exfiltración sin confundir comunicación con ejecución o atribución. La evidencia es una conversación reconstruida y correlacionada con endpoint e identidad.

**[Clase 209 — Líneas de tiempo](209-analisis-de-linea-de-tiempo-timeline/README.md).** Une filesystem, logs, navegador y aplicaciones mediante Plaso, pero conserva tiempo original, zona, precisión, parser y fuente. Enseña a comenzar por hitos confiables, ampliar ventanas y buscar contradicciones. La evidencia es una timeline filtrada que separa evento, registro, ingesta y adquisición.

**[Clase 210 — Navegadores y correo](210-forense-de-navegadores-y-correo/README.md).** Interpreta perfiles, SQLite, caché, sesiones, formatos de correo y encabezados. SPF, DKIM y DMARC se explican como verificaciones distintas; un resultado no sustituye la ruta completa ni prueba intención del usuario. La evidencia relaciona mensaje original, URL o adjunto, descarga, archivo y actividad posterior.

**[Clase 211 — Forense móvil](211-forense-movil/README.md).** Parte de autoridad, estado de bloqueo, cifrado, red y energía antes de elegir extracción lógica, filesystem o física. Android, iOS, backups, bases de apps y datos cloud se interpretan según versión y método. La evidencia documenta exactamente qué pudo adquirir la herramienta y qué quedó fuera.

**[Clase 212 — Forense en la nube](212-forense-en-la-nube/README.md).** Traslada preservación y adquisición a control planes, identidad, logs de datos, snapshots, objetos y solicitudes al proveedor. Compara AWS, Azure y Google Cloud sin asumir equivalencia de retención o cobertura. La evidencia conserva respuesta original, cuenta, región, request ID, hora, consulta y garantía de integridad disponible.

**[Clase 213 — Anti-forense](213-anti-forense-y-sus-contramedidas/README.md).** Estudia borrado, timestomping, limpieza, cifrado, ocultamiento y living-off-the-land como mecanismos que reducen o vuelven ambigua la evidencia. También desarrolla explicaciones legítimas y fuentes redundantes. La evidencia es una hipótesis ponderada, no una acusación basada únicamente en un hueco.

**[Clase 214 — Recuperación y file carving](214-recuperacion-de-datos-y-file-carving/README.md).** Distingue recuperación por metadatos de carving por firmas y estructura. Explica offsets, fragmentación, falsos positivos, deduplicación y límites de SSD/TRIM o cifrado. La evidencia es un objeto candidato validado estructuralmente y relacionado con otros rastros, no solo una extensión recuperada.

**[Clase 215 — Playbooks de respuesta](215-playbooks-de-respuesta-a-incidentes/README.md).** Convierte escenarios de phishing, ransomware e identidad en ramas con entradas, decisiones, responsables, aprobaciones y salidas. Separa playbook, runbook y automatización; ATT&CK aporta vocabulario, no autoridad operativa. La evidencia es un playbook versionado probado con casos normales, excepciones y fallos.

**[Clase 216 — Contención, erradicación y recuperación](216-contencion-erradicacion-y-recuperacion/README.md).** Enseña a elegir entre observar, aislar y reconstruir según riesgo, evidencia y criticidad. La erradicación incluye persistencia, credenciales, sesiones y configuraciones cloud; la recuperación exige estado confiable y vigilancia reforzada. La evidencia es una matriz de decisiones con verificación, rollback y criterio de cierre.

**[Clase 217 — Análisis de causa raíz](217-analisis-de-causa-raiz/README.md).** Pasa de la causa próxima a un modelo con barreras fallidas y condiciones técnicas u organizativas. Los cinco porqués e Ishikawa ayudan a preguntar; no reemplazan evidencia ni obligan a encontrar una causa única. La evidencia es un grafo causal con acciones medibles, dueños y pruebas de eficacia.

**[Clase 218 — Informe forense y aspectos legales](218-reporte-forense-y-aspectos-legales/README.md).** Convierte artefactos y métodos en afirmaciones auditables para audiencias técnicas, ejecutivas y legales. Separa hechos, inferencias, opinión y limitaciones, y evita presentar NIST como asesoría jurídica. La evidencia es un informe revisable con citas a artefactos, hashes, herramientas, tiempos y cadena de custodia.

**[Clase 219 — Ejercicios tabletop](219-ejercicios-de-mesa-tabletop/README.md).** Diseña objetivos observables, participantes, injects, decisiones y consecuencias simuladas. Explica qué puede medir una conversación facilitada y qué requiere una prueba técnica distinta. La evidencia es un after-action report con brechas, responsables, plazos y una reprueba planificada.

**[Clase 220 — Caso completo end-to-end](220-caso-completo-de-respuesta-a-incidentes-end-to-end/README.md).** Integra alerta, adquisición, disco, memoria, red, timeline, contención, recuperación, RCA e informe sin imponer una historia de antemano. El alumno debe justificar decisiones con la información disponible en cada momento y registrar desconocidos. La evidencia final es un expediente reproducible y un conjunto de mejoras revalidadas.

## 🧭 Método de investigación de la parte

En todas las clases se repite un ciclo razonado: formular la pregunta, identificar autoridad y alcance, preservar la fuente, adquirir con el menor cambio viable, verificar integridad, analizar una copia, corroborar fuentes y comunicar límites. Un hallazgo se etiqueta como **observación**, **inferencia** o **hipótesis**. La ausencia de un artefacto se interpreta según generación, retención, rotación y cobertura antes de atribuirla a anti-forense.

Los diagramas representan decisiones y procedencia. Deben poder leerse en voz alta: qué entra, qué transformación ocurre, dónde puede perderse significado y qué evidencia sale. El laboratorio no acredita dominio por ejecutar una herramienta; exige conservar hashes, comandos, versiones, tiempos, errores y criterios con los que se aceptó o rechazó una hipótesis.

## 🔗 Referencias de la parte y criterio de uso

NIST y los RFC se usan como fuentes primarias para procesos, adquisición y preservación. La documentación oficial de cada sistema o herramienta respalda únicamente sus estructuras y capacidades. Los libros aportan desarrollo profesional complementario; ninguna fuente técnica sustituye asesoría legal aplicable a la jurisdicción y al mandato del caso.

- Ligh, Case, Levy, Walters — *The Art of Memory Forensics*, Wiley 2014.
- Carrier — *File System Forensic Analysis*, Addison-Wesley 2005.
- Roberts, Brown — *Intelligence-Driven Incident Response*, O'Reilly 2017.
- NIST SP 800-61 Rev. 3: integra respuesta a incidentes con CSF 2.0; sustituyó Rev. 2 en abril de 2025 — <https://doi.org/10.6028/NIST.SP.800-61r3>
- NIST SP 800-86: guía forense desde la perspectiva de TI; declara que no es asesoría legal ni manual exhaustivo — <https://doi.org/10.6028/NIST.SP.800-86>
- RFC 3227 / BCP 55: principios de colección, orden de volatilidad, documentación y cadena de custodia — <https://www.rfc-editor.org/info/rfc3227/>
- NIST SP 800-101 Rev. 1: preservación, adquisición, examen, análisis y reporte en dispositivos móviles; sus detalles tecnológicos deben contrastarse con la versión actual del dispositivo — <https://doi.org/10.6028/NIST.SP.800-101r1>
- NISTIR 8006: desafíos de forense cloud relacionados con arquitectura, datos, tiempo, localización, multitenencia y cooperación — <https://doi.org/10.6028/NIST.IR.8006>
- The Sleuth Kit: documentación primaria de sus herramientas de análisis de volúmenes y sistemas de archivos — <https://www.sleuthkit.org/sleuthkit/docs.php>
- Volatility 3: documentación primaria de capas, símbolos y plugins del framework — <https://volatility3.readthedocs.io/en/latest/>

## ▶️ Empezar

[Clase 201 — Fundamentos de DFIR y cadena de custodia](201-fundamentos-de-dfir-y-cadena-de-custodia/README.md)
