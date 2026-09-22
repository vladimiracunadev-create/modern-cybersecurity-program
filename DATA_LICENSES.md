# Licencias y procedencia de datos

Inventario revisado el **2026-09-22**.

| Dataset | Naturaleza | Licencia |
|---|---|---|
| `labs/blue-team-soc/datos/auth-events.ndjson` | Telemetría ficticia para ejercicios de autenticación y detección. Usa direcciones privadas y el bloque de documentación `203.0.113.0/24`; no representa personas ni sistemas reales. | `CC BY-NC-SA 4.0` |
| `labs/custodia-activos-digitales/data/*` | Doce fuentes sintéticas del caso ficticio Nebula Custody. Identidades, saldos, wallets, alertas y transacciones son didácticos. | Estructura de la base y contenidos originales bajo `CC BY-NC-SA 4.0`, incluidos los derechos sui generis que el licenciante pueda otorgar |
| `autoevaluaciones/preguntas.json` | Banco original de preguntas y explicaciones del programa | `CC BY-NC-SA 4.0` |
| `certificaciones/_mapeo.json` | Mapeo editorial entre clases y objetivos de certificación | `CC BY-NC-SA 4.0`; nombres y objetivos oficiales citados pertenecen a sus titulares |
| `sources/bibliography.json` | Registro factual y editorial de fuentes, localizadores y verificaciones | Selección y estructura originales bajo `CC BY-NC-SA 4.0`; los hechos, identificadores y obras enlazadas conservan su condición jurídica propia |
| `labs/devsecops-pipeline/hallazgos-ejemplo.json` | Hallazgos deliberadamente ficticios del laboratorio | `CC BY-NC-SA 4.0` |

Los catálogos descargados al ejecutar laboratorios, como CISA KEV, OSV, EPSS o datos de una testnet, no se versionan y mantienen los términos de su proveedor. Las salidas bajo `labs/*/salida/` están excluidas de Git para evitar publicar datos obtenidos durante una práctica.

No se detectaron datos personales reales en los datasets versionados. Si una contribución incorpora datos, debe documentar fuente, permiso, licencia, finalidad, minimización y método de anonimización antes de ser aceptada. No deben enviarse credenciales, telemetría de terceros ni evidencia de incidentes reales.
