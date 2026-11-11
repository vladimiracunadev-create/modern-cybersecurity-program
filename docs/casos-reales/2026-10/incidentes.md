# Incidentes de octubre de 2026 sin CVE propio

> Verificado el 2026-11-11. Datos estructurados en `knowledge/cve/2026-10/incidentes.json`. Los identificadores `INC-…` son **internos del programa** (no existe un CVE ni un identificador oficial equivalente). En cada caso se separan los **hechos documentados**, lo **no confirmado** y lo que el programa **infiere con fines didácticos**. No se atribuye ninguna causa técnica que la organización afectada no haya divulgado.

Selección: se eligieron los incidentes del mes con fuente primaria o de un tercero técnico identificable y con valor pedagógico (nube de proveedor, identidad de aplicación, secretos, ransomware contra el borde). **No es un inventario exhaustivo** de los incidentes de octubre de 2026: los resúmenes mensuales consultados (Comparitech, SOCRadar, CM-Alliance y otros) citan decenas más —filtraciones de datos de consumo, reclamaciones de grupos de ransomware sin confirmar— que no se incorporan porque sus fuentes primarias no se pudieron verificar o no aportan una lección de ingeniería comprobable. No se encontró en las búsquedas realizadas un incidente de octubre de 2026 atribuido por organismos chilenos (ANCI/CSIRT) que justificara un caso específico; eso no demuestra que no ocurriera ninguno.

## INC-2026-10-IDCF — Ransomware contra una nube de proveedor (Japón)

| Aspecto | Contenido |
|---|---|
| Organización | IDC Frontier (IDCF Cloud), región East Japan Region 1 |
| Cronología | 2026-10-07 hacia las 03:40 (hora de Japón): inicio, apagado de redes y sistemas; 2026-10-14: aviso con cifras de recuperación por snapshot; 2026-10-18: reanuda el servicio de respaldo; 2026-10-27: séptimo informe, investigación concluida (según coberturas secundarias) |
| Vector de entrada | **No divulgado** en las fuentes consultadas |
| Actor | No atribuido por la compañía; circuló una nota de reclamación en redes cuya autenticidad no se verificó |
| Sistemas | Cuatro zonas de IDCF Cloud; quedaron fuera IDCF Cloud TypeS y IDCF Private Cloud (según la compañía, vía coberturas) |
| Información | Una firma externa no halló evidencia de acceso a datos de clientes en las zonas afectadas |
| Impacto | 495 empresas y gobiernos locales afectados; recuperación por snapshot parcial (194 el 14 de oct., 206 el 27 de oct., según fuentes) |
| No confirmado | Las cifras del atacante (554 153 snapshots, 239 hipervisores, 225 bases de datos) y cualquier relación con otras interrupciones de terceros |
| Lección | Las copias del mismo dominio de gestión que producción no protegen frente a quien lo compromete |
| Clases y práctica | 216 (recuperación), 222, 214; `respaldo_y_triaje.py::evaluar_respaldos` |
| Incertidumbre | **Alta**: el aviso original del proveedor no se consultó (solo BleepingComputer y agregadores) |

## INC-2026-10-CONNECTWISE-CLOUD-BACKUP — Credencial de aplicación de proveedor abusada

| Aspecto | Contenido |
|---|---|
| Organización | ConnectWise (Cloud Backup, antes SkyKick) y clientes con Microsoft 365 |
| Cronología (UTC, Huntress) | 13–14 oct.: pulverización de contraseñas contra cuatro inquilinos de despachos jurídicos; 15 oct. desde las 01:58: principales de servicio asignan roles de directorio en unos 50 inquilinos; 15 oct. 06:13–08:34: tokens de Graph desde una IP de alojamiento; 15 oct. 09:25–14:20: segunda oleada dirigida a 16 inquilinos (fallida); 17 oct.: ConnectWise informa de la deshabilitación de aplicaciones |
| Vector | Credencial de la aplicación del proveedor usada desde fuera de su infraestructura habitual; **cómo se obtuvo no figura** en la fuente consultada |
| Actor | Huntress cita una atribución de Microsoft a *Storm-0940* que no verificó de forma independiente; el programa no la adopta |
| Sistemas | Inquilinos de Microsoft 365 con la aplicación autorizada |
| Información | Desconocida: las lecturas de Graph no dejan rastro de auditoría; en dos inquilinos revisados no se vieron cambios de buzones, archivos, usuarios ni políticas |
| Impacto | 162 inquilinos con acceso no autorizado confirmado al 16 de oct.; cerca de 1 000 inquilinos vieron actividad desde la IP, con más de 300 exitosos al 17 de oct. (cotas inferiores) |
| Técnicas (inferencia didáctica) | Roles adicionales en la nube (T1098.003), credenciales adicionales (T1098.001), pulverización (T1110.003); verificadas en ATT&CK v20.1 |
| Contención | Deshabilitar, sin eliminar, las aplicaciones; revisar credenciales y roles añadidos desde el 13 de oct.; revisar exclusiones de acceso condicional |
| Clases y práctica | 222 (identidad de aplicación), 199 (detección), 216; `deteccion_identidad_app.py` |
| Incertidumbre | **Media**: la fuente es un tercero técnico (Huntress); la declaración de ConnectWise se conoce por referencia |

## INC-2026-10-RAILWAY — Variables de entorno descifradas en una plataforma de despliegue

| Aspecto | Contenido |
|---|---|
| Organización | Railway |
| Cronología (UTC, informe preliminar) | 20 oct. 13:58: inicio estimado; 20 oct. 17:03: incidente declarado en la página de estado; 21 oct. 04:24–05:23: extracción de secretos cifrados; 05:27–07:25: credenciales de CI y artefactos con más acceso; 07:25–09:18: consulta y descifrado de un subconjunto de variables; 22 oct. 03:32: sin acceso interno del atacante; 22 oct. 17:00–22:49: API restaurada |
| Vector | **No divulgado**; el informe menciona un intento de escalada de privilegios en la infraestructura de compilación |
| Actor | No atribuido |
| Información | Variables de entorno de hasta ~1,85 % de los espacios de trabajo (~100 000); el atacante buscó nombres de claves de proveedores de IA |
| No confirmado | Acceso al código fuente de los usuarios; qué claves concretas se descifraron; informe forense final |
| Respuesta | Revocación de accesos, reconstrucción con credenciales nuevas, invalidación de sesiones, aviso a proveedores para revocar claves y rotación de GitHub Apps |
| Clases y práctica | 241 (secretos), 216, 295 (LLMjacking como consecuencia económica) |
| Incertidumbre | **Media**: informe preliminar del propio afectado; hay una discrepancia de 10 minutos entre dos horas internas del informe (09:25 y 09:35 UTC) |

## INC-2026-10-SAFEPAY-AA26-293A — Campaña de ransomware y dispositivos de borde

| Aspecto | Contenido |
|---|---|
| Organización | Unas 600 víctimas de infraestructura crítica de cuatro continentes (aviso conjunto de CISA, FBI y socios, 2026-10-20) |
| Vector | Credenciales robadas o adivinadas, VPN (el aviso asocia direcciones de un proveedor de VPN comercial), phishing y explotación de dispositivos expuestos |
| CVE listados | `CVE-2020-3259`, `CVE-2023-20269`, `CVE-2023-27532`, `CVE-2024-40711`, `CVE-2024-40766`: los cinco en KEV con uso conocido en ransomware; ninguno entró en octubre de 2026 |
| Técnicas | ATT&CK por táctica en el aviso: T1110, T1133, T1190, T1059, T1098, T1021, T1486, T1490, entre otras |
| No confirmado | El aviso no asigna un CVE a cada víctima |
| Recomendaciones | MFA en VPN y correo, mínimo privilegio, segmentación, respaldos aislados e inmutables probados, aislamiento de hosts y reporte |
| Clases y práctica | 245, 369, 216 |
| Incertidumbre | **Baja** para el contenido del aviso |

## Qué no se incorporó, y por qué

- Reclamaciones de grupos de ransomware sin confirmación de la organización afectada (por ejemplo, las que citan algunos agregadores contra empresas de consumo): son **afirmaciones del atacante**.
- Cifras de registros expuestos de agregadores sin aviso del afectado: no se pudo verificar el origen.
- Informes sobre intrusiones asistidas por IA en proveedores de datos de seguridad: cada fuente se apoya en otra y no hay un aviso primario consultado.
