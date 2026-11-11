# Laboratorio — Octubre de 2026: casos reales de CVE e incidentes, defendidos con código

**Modalidad:** simulación local y determinista, **sin red, sin exploits y sin claves reales**. Solo biblioteca estándar de Python 3.12 (sin `uv`, Docker ni dependencias).
**Clases:** [95](../../classes/parte-4-seguridad-de-aplicaciones-web/095-inyeccion-de-comandos-del-sistema-operativo/README.md),
[99](../../classes/parte-4-seguridad-de-aplicaciones-web/099-server-side-request-forgery-ssrf/README.md),
[101](../../classes/parte-4-seguridad-de-aplicaciones-web/101-fallos-de-autenticacion-y-bypass/README.md),
[105](../../classes/parte-4-seguridad-de-aplicaciones-web/105-control-de-acceso-roto-idor-y-path-traversal/README.md),
[199](../../classes/parte-8-blue-team-deteccion-y-soc/199-ingenieria-de-deteccion-como-disciplina/README.md),
[216](../../classes/parte-9-forense-digital-y-respuesta-a-incidentes/216-contencion-erradicacion-y-recuperacion/README.md),
[222](../../classes/parte-10-seguridad-en-la-nube-y-contenedores/222-iam-en-la-nube-identidades-roles-y-permisos/README.md),
[367](../../classes/parte-20-debilidades-y-vulnerabilidades-cwe-cve-cvss/367-cve-identificar-vulnerabilidades-concretas/README.md) y
[369](../../classes/parte-20-debilidades-y-vulnerabilidades-cwe-cve-cvss/369-epss-cisa-kev-y-priorizacion-por-riesgo/README.md).
Informe del mes: [docs/casos-reales/2026-10](../../docs/casos-reales/2026-10/README.md).

> ⚠️ **Ética y límites.** Todo es ficticio o público: dominios `.test`, rangos de documentación (RFC 5737), inquilinos y aplicaciones inventados. Las funciones «vulnerables» **no ejecutan comandos, no abren conexiones ni leen archivos**: devuelven la decisión que tomaría un servidor ingenuo. **No reproducen el código de ningún producto real** (los fabricantes no lo publican y aquí no se infiere). No las adaptes para probar sistemas ajenos: eso es acceso no autorizado.

## Qué contiene

| Módulo | Qué practicas | Caso real que lo inspira (fuente) |
|---|---|---|
| `destinos_y_rutas.py` | Validar destinos de red (SSRF), rutas de archivo (path traversal) y argumentos (inyección de comandos), cada uno con su versión vulnerable y su corrección | Plex `CVE-2026-96652`/`96655`; Fortinet, Cisco, Atlassian; Ahsay, Collabora, SiteGuard (registros CVE y KEV) |
| `deteccion_identidad_app.py` | Reglas de detección sobre eventos sintéticos de identidad en la nube y su medición (verdaderos y falsos positivos) | Abuso de la credencial de ConnectWise Cloud Backup (informe de Huntress) |
| `respaldo_y_triaje.py` | (1) Qué copias sobreviven si cae el plano de gestión; (2) triaje de los 36 CVE de KEV de octubre con la tabla de BOD 26-04 | IDC Frontier (coberturas secundarias); BOD 26-04; KEV de octubre |
| `tests/test_octubre_2026.py` | 33 pruebas de las tres piezas, de la instantánea y del mapa curricular | — |

Datos que consume: `knowledge/cve/2026-10/instantanea.json` (generada con `scripts/cve_mensual.py`), `mapa-curricular.json` e `incidentes.json`.

## Ejecutar

```bash
python -m unittest discover -s labs/octubre-2026-casos-reales/tests -v
python labs/octubre-2026-casos-reales/respaldo_y_triaje.py
```

La segunda orden imprime el resumen de las tres fechas (publicado en el mes / antes / después de KEV). Para rehacer la instantánea desde las fuentes (requiere red) y compararla:

```bash
python scripts/cve_mensual.py snapshot --mes 2026-10 --salida salida-nueva.json
python scripts/cve_mensual.py comparar knowledge/cve/2026-10/instantanea.json salida-nueva.json
```

## Guía del estudiante

Trabaja en este orden; cada paso tiene una pregunta de comprensión y un criterio de aceptación.

### 1. Destinos, rutas y comandos (clases 95, 99, 105)

1. Abre `destinos_y_rutas.py` y localiza `construir_destino_vulnerable`, `ruta_vulnerable` y `linea_de_shell_vulnerable`. **Pregunta:** ¿en qué punto exacto un dato externo se convierte en instrucción o en destino?
2. Ejecuta las pruebas `SSRF`, `Rutas` y `Comandos`. **Criterio:** todas pasan.
3. Añade una entrada que creas peligrosa a `test_bloquea_destinos_internos` (por ejemplo, `http://100.64.0.1/`) y comprueba si la regla la bloquea; si no, corrige `_es_privada` y justifica. **Pregunta:** ¿por qué se comprueba la dirección **resuelta** y no el texto del host?
4. Extiende `ruta_segura` para rechazar enlaces simbólicos (pista: necesitarías `os.path.realpath` sobre un sistema de archivos real, que el modelo evita a propósito). **Criterio:** explicas por qué el modelo de cadenas no los cubre.

### 2. Detección sobre identidades de aplicación (clases 199 y 222)

1. Ejecuta `deteccion_identidad_app.py` desde un intérprete: `generar(7)`, `detectar(...)` y `medir(...)`. **Criterio:** detecta todos los eventos maliciosos y cero falsos positivos.
2. Llama a `detectar(eventos, propietarios={})`: la regla R2 alerta sobre el cambio legítimo. **Pregunta:** ¿qué dato de contexto falta y quién debe mantenerlo?
3. Cambia `umbral_spray` a 20 y vuelve a medir. **Pregunta:** ¿qué ganas y qué pierdes?

### 3. Respaldos y triaje (clases 216, 367 y 369)

1. Modela tu organización con `Copia(...)` y ejecuta `evaluar_respaldos` suponiendo comprometido tu plano de gestión principal. **Criterio:** al menos una copia inmutable, fuera de banda y con restauración probada, o concluyes «no recuperable».
2. Ejecuta `triaje_del_mes(...)` con `expuesto=True` y `expuesto=False`. **Pregunta:** ¿qué 10 CVE conservan «3 días y triaje forense» aunque el activo sea interno y por qué?

## Solución razonada

- **Destinos:** `rebind.test` devuelve una dirección pública y otra de loopback; basta una privada para rechazar, porque el cliente puede usar cualquiera. La lista cerrada de hosts es más fuerte que bloquear rangos: permite solo lo que necesitas.
- **Rutas:** `a/../b.txt` es legítima (se queda dentro); `%252e%252e/x` solo es `..` tras decodificar dos veces. La comprobación que protege es que la ruta **final** esté dentro de la base; las demás solo reducen formas.
- **Comandos:** `argv_seguro` devuelve `["ping", "-c", "1", "--", host]` solo para nombres válidos; con `;`, `$()`, comillas inversas o un guion inicial devuelve `None`. El riesgo restante (apuntar a un host interno) es SSRF, no inyección.
- **Detección:** R1 a R4 cubren las fases (pulverización, uso del principal fuera de rango, auto-asignación de rol, credencial añadida). Sin el inventario de propietarios, R2 produce falsos positivos: la calidad depende del contexto.
- **Respaldos:** una copia sirve si es inalcanzable para el atacante, inmutable y probada; falta una condición y no cuenta.
- **Triaje:** los 36 CVE caen en 20 / 15 / 1 (publicados en octubre / antes / después de KEV). Con el activo expuesto, 28 reciben «3 días y triaje forense»; con el activo interno, 26 pasan a 14 días.

## Versión vulnerable y versión corregida

| Pieza | Vulnerable (didáctica) | Corregida |
|---|---|---|
| Destino | `construir_destino_vulnerable` acepta una URL completa en `protocolo` | `validar_destino` |
| Ruta | `ruta_vulnerable` | `ruta_segura` |
| Comando | `linea_de_shell_vulnerable` + `comandos_que_ejecutaria_un_shell` | `argv_seguro` |
| Detección | `detectar(..., propietarios={})` (sin contexto) | `detectar(...)` con inventario |
| Respaldo | todo en el dominio comprometido | bóveda inmutable y fuera de banda |

## Criterios de aceptación

1. `python -m unittest discover -s labs/octubre-2026-casos-reales/tests -v` termina en `OK`.
2. Puedes explicar, sin mirar el código, por qué cada corrección funciona y qué **no** cubre.
3. Dejas por escrito qué parte de cada caso real es dato documentado y cuál es inferencia tuya.

## Entorno, limpieza y límites de seguridad

- **Entorno:** ningún servicio se inicia; no hay red, ni archivos temporales, ni contenedores. Nada que limpiar: si ejecutaste `scripts/cve_mensual.py snapshot` con `--salida`, borra el archivo generado.
- **Reproducibilidad:** los eventos usan semilla (`random.Random(semilla)`); la prueba `test_robusto_a_otras_semillas` repite con otras.
- **Límites:** las reglas se miden con datos sintéticos; **un resultado perfecto aquí no prueba el rendimiento en producción**. El modelo de shell es una simplificación de POSIX. El modelo de rutas no resuelve enlaces simbólicos. El laboratorio **no** cubre cadenas de explotación, memoria de PHP/kernel (para eso, `labs/pwn-binarios` en un entorno aislado), ni el procesamiento multimedia de Plex; esos límites están declarados en el [informe](../../docs/casos-reales/2026-10/README.md).
