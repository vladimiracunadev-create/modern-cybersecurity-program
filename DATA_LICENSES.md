# Licencias y procedencia de datos

Inventario revisado el **2026-10-30**.

| Dataset | Naturaleza | Licencia |
|---|---|---|
| `labs/blue-team-soc/datos/auth-events.ndjson` | Telemetría ficticia para ejercicios de autenticación y detección. Usa direcciones privadas y el bloque de documentación `203.0.113.0/24`; no representa personas ni sistemas reales. | `CC BY-NC-SA 4.0` |
| `labs/custodia-activos-digitales/data/*` | Doce fuentes sintéticas del caso ficticio Nebula Custody. Identidades, saldos, wallets, alertas y transacciones son didácticos. | Estructura de la base y contenidos originales bajo `CC BY-NC-SA 4.0`, incluidos los derechos sui generis que el licenciante pueda otorgar |
| `autoevaluaciones/preguntas.json` | Banco original de preguntas y explicaciones del programa | `CC BY-NC-SA 4.0` |
| `certificaciones/_mapeo.json` | Mapeo editorial entre clases y objetivos de certificación | `CC BY-NC-SA 4.0`; nombres y objetivos oficiales citados pertenecen a sus titulares |
| `sources/bibliography.json` | Registro factual y editorial de fuentes, localizadores y verificaciones | Selección y estructura originales bajo `CC BY-NC-SA 4.0`; los hechos, identificadores y obras enlazadas conservan su condición jurídica propia |
| `labs/devsecops-pipeline/hallazgos-ejemplo.json` | Hallazgos deliberadamente ficticios del laboratorio | `CC BY-NC-SA 4.0` |
| `knowledge/cwe/normalizado/*`, `knowledge/cwe/indices/*` | Catálogo CWE 5.0 de MITRE (nombres, descripciones, mitigaciones, consecuencias) reorganizado a JSON sin reescribir el texto, con sus índices derivados | Términos de uso de MITRE CWE: uso libre con reproducción de su copyright y licencia, que figuran en `knowledge/cwe/LICENCIA-MITRE.md` y deben acompañar a cualquier redistribución |
| `knowledge/cwe/pedagogico/mapa-curricular.json`, `knowledge/cwe/PROCEDENCIA.json` | Decisiones didácticas del programa (alias en español, clases, laboratorios) y registro de origen y huellas | `CC BY-NC-SA 4.0` |
| `labs/devsecops-pipeline/datos/casos-cwe-cve.json` | Instantánea fechada (2026-10-30) de campos factuales de 14 CVE reales: identificadores, puntuaciones CVSS y CWE de CNA, CISA-ADP y NVD, EPSS y pertenencia a KEV. No contiene catálogos completos | Los hechos y los datos de cada proveedor conservan sus términos (CVE Program, NIST NVD, FIRST EPSS, CISA); la selección y estructura son del programa, `CC BY-NC-SA 4.0` |
| `labs/devsecops-pipeline/datos/nvd-estados-2026-09-01_10.json` | Recuento agregado de estados de enriquecimiento de NVD para una ventana de CVE; sin registros individuales | `CC BY-NC-SA 4.0` para el recuento; los datos de origen mantienen los términos de NIST NVD |
| `labs/devsecops-pipeline/datos/cvss4/*` | Tablas del algoritmo de CVSS v4.0 portadas de la calculadora oficial de FIRST | BSD-2-Clause (© 2023 FIRST.ORG, Inc., Red Hat y colaboradores); el aviso figura en `LICENSE-FIRST-CVSS-v4-BSD-2.txt` |
| `labs/appsec-code/cwe-map.json`, `labs/devsecops-pipeline/cwe-map.json`, `labs/*/tests/datos/*` | Mapas de correspondencia CWE de los defectos plantados y la salida versionada de Bandit sobre la aplicación didáctica | `CC BY-NC-SA 4.0` |

Los catálogos descargados al ejecutar laboratorios, como CISA KEV, OSV, EPSS o datos de una testnet, no se versionan y mantienen los términos de su proveedor; la única excepción son los campos factuales mínimos de la instantánea de 14 CVE de la tabla anterior. El ZIP original de MITRE se descarga con `python scripts/cwe_kb.py importar --descargar` y se excluye de Git. Las salidas bajo `labs/*/salida/` están excluidas de Git para evitar publicar datos obtenidos durante una práctica.

No se detectaron datos personales reales en los datasets versionados. Si una contribución incorpora datos, debe documentar fuente, permiso, licencia, finalidad, minimización y método de anonimización antes de ser aceptada. No deben enviarse credenciales, telemetría de terceros ni evidencia de incidentes reales.
