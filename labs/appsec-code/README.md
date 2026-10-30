# Lab: Code review y SAST

Laboratorio de **revisión de código segura** y **análisis estático (SAST)** para las clases
**238** (SAST), **323** (pruebas de seguridad del software) y **330** (análisis de código y
automatización), y laboratorio de práctica de la **Parte 20** (clases **361–370**: CWE, CVE, CVSS y
su gestión), donde cada debilidad se clasifica con su CWE, se corrige y se **demuestra** con una prueba
que falla antes y pasa después. Prepara el dominio *Tools and Code Analysis* de **PenTest+** y
*Software Development Security* de **CISSP**.

> ⚠️ La app de `vulnerable_app/` es **insegura a propósito**. No la despliegues; es para
> analizarla estáticamente y corregirla.

## 🎯 Qué vas a practicar

- Encontrar vulnerabilidades con **SAST** (Semgrep, Bandit).
- Hacer **revisión manual** de código y distinguir hallazgos reales de falsos positivos.
- **Corregir** cada fallo con el patrón seguro correspondiente.

## 🚀 Ejecutar el análisis

Sin instalar nada (usa el contenedor de Semgrep) o con herramientas locales:

```bash
cd labs/appsec-code
./escanear.sh
# o directamente:
docker run --rm -v "$(pwd)":/src semgrep/semgrep semgrep --config auto /src/vulnerable_app
```

## 🧭 Recorrido guiado

1. **Corre el SAST** y lee cada hallazgo: regla, línea, severidad.
2. **Revisa el código a mano** (`vulnerable_app/app.py`): hay **8 vulnerabilidades** plantadas. ¿El SAST las encontró todas? ¿Marcó algo que no es explotable (falso positivo)?
3. **Clasifica** cada hallazgo por riesgo (impacto × explotabilidad) como en un informe real.
4. **Corrige** una por una y vuelve a escanear hasta dejar el reporte limpio.
5. **Integra en CI (opcional):** añade Semgrep como paso de un workflow para que falle ante nuevos hallazgos — es justo lo que hace este repo en su propio pipeline.

## 🏆 Retos verificables

1. **Cobertura del SAST:** documenta cuántas de las 8 detecta Semgrep y cuántas Bandit. *Aceptación:* tabla vuln → ¿detectada por qué herramienta?
2. **Falsos negativos:** identifica las que ninguna herramienta detectó y explica por qué (límite del análisis estático).
3. **Remediación:** entrega el `app.py` corregido; un nuevo escaneo no reporta las 8 y las pruebas de `tests/` confirman cada corrección. *Aceptación:* consultas parametrizadas, `subprocess` sin `shell=True`, un algoritmo de coste ajustable para contraseñas (scrypt, Argon2 o bcrypt), sin `eval`/`pickle` sobre entrada, validación de rutas, sin secretos en código, `debug=False`. Hay una versión de referencia en `vulnerable_app/app_corregida.py`.
4. **Gestión de secretos:** mueve `DB_PASSWORD`/`AWS_KEY` a variables de entorno o un gestor de secretos.

## 🧬 Cada debilidad, con su CWE y su prueba

Las 8 vulnerabilidades no son solo «categorías»: cada una es una entrada del catálogo CWE (versión
5.0, importada en `knowledge/cwe/`), y [`cwe-map.json`](cwe-map.json) registra para cada una
qué CWE es y por qué, qué regla de Bandit la detecta (o no), qué etiqueta CWE le pone la herramienta
y qué prueba demuestra la corrección.

| # | Defecto | CWE | Bandit 1.9.4 | Etiqueta de Bandit | Prueba |
|---|---|---|---|---|---|
| 1 | Secretos embebidos | `CWE-798` | B105 (solo la contraseña) | `CWE-259` (menos específica) | `test_secretos_no_estan_en_el_codigo` |
| 2 | Inyección SQL | `CWE-89` | B608 | `CWE-89` (coincide) | `test_inyeccion_sql` |
| 3 | Inyección de comandos | `CWE-78` | B602 | `CWE-78` (coincide) | `test_inyeccion_de_comandos` |
| 4 | Hash débil de contraseña | `CWE-916` | B324 | `CWE-327` (menos específica) | `test_hash_de_contrasena` |
| 5 | Deserialización | `CWE-502` | B301 | `CWE-502` (coincide) | `test_deserializacion` |
| 6 | Path traversal | `CWE-22` | **no detectado** | — | `test_path_traversal` |
| 7 | `eval` | `CWE-95` | B307 | `CWE-78` (**difiere**) | `test_evaluacion_de_codigo` |
| 8 | Depuración y enlace | `CWE-489` | B201 y B104 | `CWE-94` y `CWE-605` | `test_depuracion_y_enlace` |

La tabla resume una medición, no una expectativa: la salida de Bandit está versionada en
`tests/datos/bandit-1.9.4-app.json`. Lo que se afirma de Semgrep en `SOLUCION.md` es una expectativa, porque
no se pudo ejecutar en la verificación. Para contrastar la etiqueta de la herramienta con el CWE correcto
(y ver cuáles coinciden, cuáles son menos específicas y cuáles difieren):

```bash
python scripts/cwe_kb.py sast labs/appsec-code/tests/datos/bandit-1.9.4-app.json --mapa labs/appsec-code/cwe-map.json
```

## ✅ Pruebas: el ataque funciona antes y falla después

```bash
python -m unittest discover -s labs/appsec-code/tests -v
```

Cada prueba ejecuta **el mismo ataque** contra `vulnerable_app/app.py` (debe funcionar: confirma la
debilidad) y contra `vulnerable_app/app_corregida.py` (debe fallar: confirma la defensa), y comprueba que lo
legítimo sigue funcionando. No hace falta Flask: las pruebas usan un sustituto mínimo, y nada se ejecuta
contra la red ni contra el sistema.

## 🧪 Prácticas de las clases 363–366

La carpeta [`practicas/`](practicas/) contiene pares **vulnerable / correcto** ejecutables, cada uno con sus pruebas:

| Archivo | CWE que practica | Clase |
|---|---|---|
| `autorizacion.py` | `CWE-862`, `CWE-863`, `CWE-639` (matriz de acceso usuario × recurso) | 364 |
| `memoria_y_carreras.py` | `CWE-190` → `CWE-787` (cadena `CWE-680`), `CWE-193`, `CWE-362`/`CWE-367` | 365 |
| `limites.py` | `CWE-770` (límites de tamaño y tasa), `CWE-307` (intentos de autenticación) | 365–366 |
| `ssrf.py` | `CWE-918`: lista de destinos, direcciones públicas, dirección fijada y redirecciones, con resolutor inyectado (sin red) | 363 |
| `subida.py` | `CWE-434`: extensión, contenido, tamaño y nombre generado por el servidor | 363 |

## 🔗 Cobertura en el programa

[`docs/matriz-cobertura-cwe.md`](../../docs/matriz-cobertura-cwe.md) indica, para cada CWE, si se menciona, se
explica, se practica, tiene laboratorio y tiene corrección con prueba; este laboratorio es la fuente del
nivel más alto («con corrección y prueba»).

## 🗺️ Las 8 vulnerabilidades (categorías)

Inyección SQL · Inyección de comandos · Hash débil · Deserialización insegura · Path traversal ·
Ejecución de código (`eval`) · Secretos embebidos · Debug en producción.

La explicación y la corrección de cada una están en [`SOLUCION.md`](SOLUCION.md) — míralo
**después** de intentarlo.

## 🔗 Referencias

- [Semgrep](https://semgrep.dev/) · [Bandit](https://bandit.readthedocs.io/)
- [OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/) · [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- Parte 11 y Parte 17 del programa — [índice de clases](../../classes/README.md)
