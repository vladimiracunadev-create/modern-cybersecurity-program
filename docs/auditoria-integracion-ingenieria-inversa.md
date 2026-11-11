# Auditoría de la integración: ingeniería inversa como disciplina transversal

> Fecha de la revisión: 11 de noviembre de 2026. Estado verificado: 21 partes y 370 clases (`scripts/validar_estructura.py`). No se crean clases ni partes, no se renumera nada y REA no se convierte en eje de ninguna unidad.

## 1. Qué enseñaba ya el programa

Las clases 130–135 cubrían bien formatos ELF/PE, herramientas (Ghidra, IDA, radare2), desensamblado lineal y recursivo, CFG, call graph, análisis dinámico con strace/ltrace/GDB/Frida, emulación, packing y ofuscación; 136–137 fuzzing y descubrimiento de vulnerabilidades; 146 análisis de malware con IDA y Ghidra; 261–267 ingeniería inversa móvil y de firmware; y la Parte 18 agentes y MCP. No se interpretó la ausencia de una palabra como ausencia de conocimiento: se leyeron las clases.

## 2. Matriz de brechas y decisiones

| Clase | Estado | Brecha encontrada | Decisión | Dónde queda |
|---|---|---|---|---|
| 130 | Parcial | No explicaba qué información descarta el compilador y cuál sobrevive; análisis, modificación y explotación aparecían mezclados; no separaba observación, inferencia e hipótesis | Profundizada (alta) | Nuevas secciones en 130 y ejercicio 7 |
| 131, 132 | Completo | Herramientas bien tratadas; sin brecha que justifique cambios | Sin cambios | — |
| 133 | Parcial | No trataba el efecto de las optimizaciones ni los límites del pseudocódigo del decompilador | Profundizada (alta) | Sección nueva y ejercicio 7 |
| 134 | Parcial | No trataba el efecto de la instrumentación sobre lo observado ni el ciclo hipótesis-predicción-observación | Profundizada (alta) | Sección nueva |
| 135 | Completo | Sin brecha; la entropía se enlaza al laboratorio | Nota breve | Nota de práctica |
| 136 | Completo | Sin brecha | Sin cambios | — |
| 137 | Parcial | No existía la comparación de versiones ni la validación de parches desde binarios | Profundizada (media) | Sección nueva y ejercicio 7 |
| 146 | Completo | Sin brecha; se enlaza el triaje previo y la regla de artefacto-como-dato | Nota breve | Nota de práctica |
| 246 | Parcial | Supply chain sin la comprobación de qué cambió realmente en un binario | Nota breve | Nota de validación |
| 332 | Insuficiente en este tema | Sin caso aplicado de ingeniería inversa asistida por agentes ni de artefactos hostiles | Ampliada (alta) | Sección y caso razonado |
| 138–140, 261–267 | Completo | Sin brecha propia en este alcance | Sin cambios | — |

Se decidió no tocar la Parte 9 (no existe una brecha propia que no cubra ya el triaje estático enlazado desde la ruta DFIR) ni las Partes 13 y 19 (ya enseñan APK, Frida, firmware y hardware con su propio laboratorio).

## 3. Laboratorio: reutilizar o crear

`labs/pwn-binarios` practica explotación de un desbordamiento y `labs/rootcause-windows`, `labs/dfir-memoria` y `labs/appsec-code` cubren otros fines. Ninguno practica triaje estructural, comparación de versiones, artefactos como dato ni disciplina de evidencia, y el entorno de este trabajo no dispone de compilador. Se creó **`labs/ingenieria-inversa-triage/`**, solo con biblioteca estándar, que construye ELF64 sintéticos, los analiza (cabecera, secciones, símbolos, entropía, cadenas), compara dos versiones, marca texto dirigido a analistas o agentes y obliga a citar evidencia al cerrar hipótesis. 23 pruebas unitarias.

## 4. Herramientas y REA

La parte de herramientas del encargo (Ghidra, IDA, radare2, GDB, Frida, JADX, Apktool, Binwalk…) ya está desarrollada en las clases 131, 132, 134, 136, 265 y 267, por lo que no se repitió. Se añadió un caso en la clase 332 sobre REA, con estas afirmaciones leídas en el repositorio original `morluto/rea` el 2026-11-11:

- Es un servidor MCP y una CLI para ingeniería inversa; usa motores externos (Hopper, Ghidra, IDA, Kuna, objdump, Rizin, JADX, Apktool, TShark, Binwalk, Unblob y otros) que tienen sus propias licencias.
- Código propio bajo MIT; no concede licencias de herramientas comerciales; requiere Node.js en versiones concretas; el soporte varía por sistema operativo y objetivo.
- La inspección estática lee ficheros; la captura en ejecución actúa con los permisos del usuario; la documentación no describe ninguna *sandbox*.
- Advierte que un nombre parecido o un README copiado no demuestra que una descarga sea oficial.

La bifurcación `vladimiracunadev-create/rea` se consultó: su README es el del proyecto original y no documenta cambios propios, por lo que **no se cita como fuente de capacidades**. No se ejecutó REA en este trabajo: sus capacidades se describen según su documentación, no según pruebas propias.

## 5. Rutas

Se amplían tres rutas existentes (`investigador-seguridad`, `dfir`, `devsecops-engineer`) con clases reutilizadas, práctica y una evidencia de aprendizaje. No se crea ninguna ruta nueva: la brecha para un perfil de especialista en ingeniería inversa se cubre con `investigador-seguridad`; evaluar una ruta específica queda como mejora pendiente.

## 6. Validaciones ejecutadas

Estructura y enlaces, navegación, rutas, codificación, trazabilidad de fuentes, glosario global y catálogo móvil, markdownlint de todo el repositorio y las 23 pruebas del laboratorio. La verificación de que CI queda en verde tras el push se registra en el commit.

## 7. Pendiente y límites

- No se compiló ni ejecutó ningún binario real: el laboratorio usa datos sintéticos y lo dice. El ejercicio con `gcc` se deja como opcional.
- No se desarrolló el análisis de PE ni de Mach-O en código; la teoría de PE ya está en la clase 130.
- No se incorporaron ejercicios de ofuscación avanzada ni de virtualización de código más allá de lo ya enseñado.
- No se evaluó una ruta profesional específica de ingeniería inversa.
- No se verificó el comportamiento real de REA; solo su documentación pública.
- El detector de texto dirigido a agentes es heurístico y puede eludirse reformulando el mensaje.
