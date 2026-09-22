# Auditoría de licencias y propiedad intelectual

**Repositorio:** `vladimiracunadev-create/modern-cybersecurity-program`

**Fecha de corte:** 2026-09-22
**Alcance:** árbol Git, historial local completo, código, contenido pedagógico, laboratorios, payloads de demostración, datos, configuraciones, dependencias, herramientas, imágenes, artefactos generados y contributors.

## Resultado ejecutivo

La licencia MIT única era demasiado amplia y ambigua para un repositorio mixto: trataba igual software, 340 clases, manuales, datasets, imágenes y referencias a herramientas externas. Se implantó una matriz explícita:

| Tipo de material propio | Licencia actual |
|---|---|
| Código, scripts, aplicación, workflows y configuraciones | Apache-2.0 |
| Contenido educativo, rutas, soluciones, evaluaciones, manuales y presentaciones | CC BY-NC-SA 4.0 |
| Fragmentos de código original pensados para copiarse y ejecutarse | Apache-2.0 |
| Datos sintéticos y selección/estructura de registros editoriales | CC BY-NC-SA 4.0 |
| Diagramas, capturas y activos gráficos propios | CC BY-NC-SA 4.0 |
| Terceros | Licencia original; fuera de la concesión del proyecto |

No se modificó la funcionalidad ni se ampliaron capacidades ofensivas. Las revisiones ya publicadas con MIT conservan esa licencia. La adopción de Apache-2.0 y CC BY-NC-SA 4.0 se aplica a la revisión que incorpora esta política y a versiones futuras, con las excepciones documentadas.

## Evidencia examinada

Las cifras de esta sección y de «Validación ejecutada» son la instantánea histórica
tomada para la auditoría de licencias, inmediatamente antes de añadir la Parte 19.
El catálogo vigente tiene 20 partes y 360 clases; conservar la instantánea permite
reproducir qué árbol se examinó para adoptar la nueva política.

- 2.393 archivos versionados y 115 commits del historial local;
- 359 README bajo `classes/`, incluidos índices de parte y 340 clases;
- 341 PDF, 340 PPTX, 754 PNG y 387 SVG;
- 51 archivos de código o scripts (`.py`, `.js`, `.sh`, `.c`) y 22 configuraciones estructuradas;
- 13 archivos dentro de carpetas de datasets;
- `mobile/package.json` y `mobile/package-lock.json`;
- Dockerfiles, Compose, workflows de CI y comandos de descarga;
- referencias globales a `MIT`, `license`, `licencia`, `copyright` y `SPDX`;
- autores de commit y trailers `Co-Authored-By`.

## Hallazgos y resolución

### A-01 — licencia única sin delimitación

**Severidad:** alta. El `LICENSE` MIT no distinguía software de contenido, datos, salidas generadas o terceros.
**Resolución:** `LICENSE` contiene el texto íntegro Apache-2.0 para software propio; `LICENSE-CONTENT.md` delimita CC BY-NC-SA 4.0; se añadieron inventarios de terceros, activos y datos.

### A-02 — afirmaciones MIT actuales desincronizadas

**Severidad:** alta. El badge y la sección de licencia del README, además del generador del sitio, afirmaban que todo el proyecto era MIT.
**Resolución:** se sustituyeron por la matriz de licencias. Las menciones a `kali-mcp (MIT)` y a terceros se conservaron porque siguen siendo verdaderas. Las referencias históricas a la licencia inicial se conservaron como historia.

### A-03 — dependencias y contenedores sin aviso central

**Severidad:** media. El proyecto usa paquetes Node, herramientas Python, imágenes Docker y binarios descargados con licencias que incluyen MIT, Apache-2.0, BSD, MPL-2.0, GPL, LGPL, ELv2, NPSL, CC BY 4.0 y licencias específicas.
**Resolución:** `THIRD_PARTY_NOTICES.md` registra los componentes, excepciones y fuentes primarias. `mobile/package-lock.json` sigue siendo la fuente de verdad por versión.

### A-04 — activos sin registro de procedencia

**Severidad:** media. Había 1.141 activos PNG/SVG y artefactos de publicación sin un inventario de licencia.
**Resolución:** `ASSET_LICENSES.md` distingue diagramas generados, copias móviles, capturas, iconos, PDF y PPTX. La procedencia de capturas e iconos se apoya en el historial local y queda marcada como una limitación de evidencia, no como certeza externa.

### A-05 — datasets sin licencia explícita

**Severidad:** media. Los datos sintéticos estaban descritos como ficticios, pero no tenían términos de reutilización.
**Resolución:** `DATA_LICENSES.md` identifica cada familia, confirma su carácter didáctico y aplica CC BY-NC-SA 4.0 a la estructura y contenido original.

### A-06 — contenido de doble uso y licencia confundibles

**Severidad:** alta. El aviso ético existía, pero no separaba de forma sistemática aprendizaje, investigación, pruebas defensivas, laboratorio autorizado y acciones contra terceros.
**Resolución:** `SECURITY_AND_ETHICS.md` establece esos límites y aclara que una licencia de copyright nunca es una autorización operativa.

### A-07 — atribución y contributors

**Severidad:** media. El titular figuraba como `Vladimir Acuña`, mientras el nombre de cuenta aparecía de forma informal.
**Resolución:** se normalizó el titular como **Vladimir Acuña** y `vladimiracunadev-create` como identidad pública. Los 115 commits tienen una sola identidad de autor humano. Noventa commits declaran trailers de tres identidades automatizadas de Claude; se registran como asistencia, no como titulares humanos. No se hallaron autores de commit externos en el historial disponible.

### A-08 — material ofensivo y payloads

**Severidad:** baja respecto de propiedad intelectual; alta si se operara fuera de alcance. No se encontraron `.exe`, `.dll`, `.bin`, `.pcap`, dumps ni malware real versionados. `.gitignore` excluye esos formatos y carpetas. Sí hay código fuente deliberadamente vulnerable, retos, comandos y ejemplos de payloads en prosa.
**Resolución:** se mantuvo el contenido sin aumentar capacidades, se documentó como material educativo y se vinculó a la política de autorización.

## Historial y no retroactividad

El commit inicial `addece870bbb4282a25063367afba5dc87b199d7`, de 2026-07-12, publicó el proyecto bajo MIT. No se alteraron commits ni tags. Las personas que recibieron esas revisiones conservan sus permisos MIT. [docs/LICENSING_HISTORY.md](docs/LICENSING_HISTORY.md) explica cómo determinar la licencia de una revisión.

## Riesgos residuales

- Los tags `latest` de DVWA, Nmap, FTP y OpenSSH pueden cambiar de contenido o licencia sin cambiar el repositorio. Conviene fijarlos por digest y volver a inventariarlos antes de distribuir una imagen de laboratorio.
- `mobile/package-lock.json` aporta metadatos de licencia, pero una distribución binaria debería generar un SBOM y un archivo de avisos desde los paquetes realmente incorporados.
- No existía un registro de creación o archivos fuente separados para iconos y capturas. El historial respalda su origen en el proyecto, pero cualquier evidencia externa posterior debe prevalecer y actualizar `ASSET_LICENSES.md`.
- Esta auditoría comprueba el historial Git local disponible. No prueba acuerdos privados, cesiones, borradores externos o material que nunca entró al repositorio.
- Las licencias y marcas de herramientas cambian. El inventario debe revisarse al modificar versiones, imágenes, fuentes o dependencias.
- `npm ci` informó 42 vulnerabilidades en el árbol fijado de la app (2 bajas, 26 moderadas, 13 altas y 1 crítica). No se ejecutó `npm audit fix` porque actualizar dependencias puede cambiar funcionalidad y queda fuera de esta auditoría de gobernanza. Debe tratarse en una remediación técnica separada.

## Validación ejecutada

| Control | Resultado |
|---|---|
| `validar_estructura.py` | 19 partes, 340 clases, 475 Markdown y 4.015 enlaces; 0 rotos |
| `generar_navegacion.py --check` | navegación coherente en 340 clases |
| `validar_rutas.py` | 28 guías, 637 referencias y 88 anclas válidas |
| `validar_encoding.py` | 557 archivos; UTF-8 válido y sin mojibake |
| `verify-sources` | 1.591 citas resueltas; registro y README coherentes; 4 avisos preexistentes de localización |
| Unit tests de custodia digital | 3 pruebas superadas |
| `compileall` | scripts y laboratorios compilan |
| Bandit 1.9.4, severidad media/alta | sin hallazgos |
| markdownlint-cli2 0.23.0 | 475 archivos; 0 errores |
| Generación del sitio | 453 páginas más `index.html`; pie de licencia actualizado |
| Catálogo móvil | 340 clases, 19 partes, 1 recurso y 363 diagramas al día |
| `npm ci` y export web de Expo | instalación y exportación correctas |
| `verificar_bundle.py` | 340 clases y 1 recurso completos dentro del bundle |
| `git diff --check` | sin errores de espacios o parches |

## Controles de mantenimiento

1. Toda contribución debe identificar si es código, contenido, dato, activo o material de terceros.
2. No se aceptará contenido externo sin fuente, licencia compatible y atribución.
3. Los cambios a manifests, lockfiles, Dockerfiles o imágenes deben actualizar `THIRD_PARTY_NOTICES.md` cuando corresponda.
4. Los nuevos datasets deben documentar procedencia, autorización, privacidad y licencia.
5. Las imágenes y capturas nuevas deben añadirse a `ASSET_LICENSES.md`.
6. Cada release debe conservar `LICENSE`, `NOTICE`, `LICENSE-CONTENT.md` y los avisos aplicables.
7. La CI debe seguir validando estructura, enlaces, encoding, fuentes, aplicación y seguridad; una revisión de licencias automatizada o SBOM es la siguiente mejora recomendada.

## Documentos resultantes

- [LICENSE](LICENSE) — Apache License 2.0 para software propio.
- [LICENSE-CONTENT.md](LICENSE-CONTENT.md) — CC BY-NC-SA 4.0 para contenido.
- [NOTICE](NOTICE) — atribución y mapa de documentos.
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) — herramientas y dependencias.
- [ASSET_LICENSES.md](ASSET_LICENSES.md) — activos visuales y artefactos generados.
- [DATA_LICENSES.md](DATA_LICENSES.md) — datasets y registros editoriales.
- [TRADEMARKS.md](TRADEMARKS.md) — uso de nombres y marcas.
- [SECURITY_AND_ETHICS.md](SECURITY_AND_ETHICS.md) — usos autorizados y límites.
- [docs/LICENSING_HISTORY.md](docs/LICENSING_HISTORY.md) — cronología sin retroactividad.

Esta auditoría es una revisión técnica y documental del repositorio; para una decisión jurídica sobre explotación comercial, jurisdicción o titularidad externa se requiere asesoría profesional con acceso a los acuerdos y evidencias fuera de Git.
