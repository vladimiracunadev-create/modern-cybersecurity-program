# Solución — Code review, SAST y clasificación CWE

> Solución docente. Míralo **después** de intentarlo. Las 8 vulnerabilidades de
> `vulnerable_app/app.py`, su CWE, lo que cada herramienta dijo **de verdad** y cómo se
> demuestra cada corrección.

## Las 8 vulnerabilidades

| # | Dónde | Vulnerabilidad | CWE principal | Corrección |
|---|---|---|---|---|
| 1 | `DB_PASSWORD` / `AWS_KEY` | Secretos embebidos | **CWE-798** (la contraseña, en concreto, CWE-259) | Leer de variables de entorno o de un gestor de secretos; **rotar** las credenciales publicadas; escanear con gitleaks. |
| 2 | `/user` | Inyección SQL por concatenación | **CWE-89** | Consulta parametrizada: `conn.execute("SELECT * FROM users WHERE name = ?", (name,))`. |
| 3 | `/ping` | Inyección de comandos (`shell=True`) | **CWE-78** | Lista de argumentos sin shell + validación de `host` con lista permitida. |
| 4 | `/hash` | Hash de contraseña débil y sin sal (MD5) | **CWE-916** (también CWE-327 y CWE-328) | Argon2id, scrypt o bcrypt con sal única; comparar en tiempo constante. |
| 5 | `/load` | Deserialización insegura (`pickle`) | **CWE-502** | No deserializar datos no confiables con `pickle`; usar JSON (o un formato con esquema). |
| 6 | `/read` | Path traversal | **CWE-22** (variante relativa: CWE-23) | Resolver la ruta (`realpath`) y comprobar con `commonpath` que sigue dentro del directorio permitido. |
| 7 | `/calc` | Ejecución de código (`eval`) | **CWE-95** (padre: CWE-94) | No usar `eval`; evaluar el árbol sintáctico con una lista cerrada de operadores. |
| 8 | `app.run(debug=True)` | Depuración activa y enlace a `0.0.0.0` | **CWE-489** (y CWE-1327 para el enlace) | `debug=False`, escuchar en `127.0.0.1` salvo que un proxy inverso lo requiera. |

El código corregido completo, comentado, está en
[`vulnerable_app/app_corregida.py`](vulnerable_app/app_corregida.py). Compáralo con `diff`.
Todo lo de esta tabla está en forma legible por máquina en [`cwe-map.json`](cwe-map.json).

## Lo que las herramientas dijeron de verdad

El mapa [`cwe-map.json`](cwe-map.json) registra una medición, no una expectativa. Se ejecutó
**Bandit 1.9.4** el 2026-10-30 y su salida está guardada en
[`tests/datos/bandit-1.9.4-app.json`](tests/datos/bandit-1.9.4-app.json); una prueba comprueba
que el mapa y esa salida siguen coincidiendo.

| Línea | Regla | Severidad / confianza | CWE que reporta Bandit | ¿Es el CWE correcto? |
|---|---|---|---|---|
| `DB_PASSWORD = …` | B105 | LOW / MEDIUM | CWE-259 | Sí: es la variante específica de contraseña. |
| `AWS_KEY = …` | *(nada)* | — | — | **Falso negativo**: Bandit busca nombres de variable parecidos a «password» y `AWS_KEY` no lo parece. |
| `query = "SELECT … '" + name` | B608 | MEDIUM / **LOW** | CWE-89 | Sí, pero con confianza baja: la regla sospecha de todo SQL armado con cadenas. |
| `check_output(… shell=True)` | B602 | HIGH / HIGH | CWE-78 | Sí. Además B404 (`import subprocess`) repite el mismo CWE: dos hallazgos, un defecto. |
| `hashlib.md5(…)` | B324 | HIGH / HIGH | CWE-327 | Correcto pero **genérico** (es una clase). Para contraseñas el más específico es CWE-916. |
| `pickle.loads(…)` | B301 | MEDIUM / HIGH | CWE-502 | Sí. B403 (`import pickle`) es informativo. |
| `open("/var/data/" + filename)` | *(nada)* | — | — | **Falso negativo**: sin seguimiento del dato (*taint tracking*) de `request.args` hasta `open`, no lo ve. |
| `eval(expr)` | B307 | MEDIUM / HIGH | **CWE-78** | **No.** `eval` ejecuta código Python, no comandos del sistema operativo. El CWE correcto es CWE-95. |
| `app.run(…, debug=True)` | B201 | HIGH / MEDIUM | CWE-94 | Parcial: es la *consecuencia*. La debilidad es dejar la depuración activa (CWE-489). |
| `app.run(host="0.0.0.0", …)` | B104 | MEDIUM / MEDIUM | **CWE-605** | **No.** CWE-605 es «Multiple Binds to the Same Port». El defecto es CWE-1327, «Binding to an Unrestricted IP Address». |

Resumen: Bandit emitió **10 hallazgos** para **8 defectos**. Dos defectos (clave de AWS y path
traversal) no se detectaron, tres hallazgos llevan un CWE que no corresponde o no es el más
específico, y cuatro son duplicados o avisos informativos del mismo defecto. Un informe que
copie estas etiquetas sin pensar clasifica mal.

**Sobre Semgrep:** el laboratorio sugiere ejecutarlo, pero esta solución **no** incluye una
medición de Semgrep porque no estaba disponible al verificarla. Cualquier afirmación sobre qué
detecta es una expectativa, y debes contrastarla ejecutándolo (`./escanear.sh`) y guardando su
salida. Si lo haces, `python ../../scripts/cwe_kb.py sast salida/semgrep.json` la relaciona con
el catálogo igual que con Bandit.

## Cómo clasificar con CWE: el método de este laboratorio

La etiqueta de una herramienta es una **pista**, no el diagnóstico. Para cada hallazgo:

1. **Describe el defecto sin mirar el CWE**: ¿qué entrada llega a qué operación y qué falta entre
   ambas? («La entrada del usuario llega a una consulta SQL sin separar datos de estructura».)
2. **Busca el CWE más específico que describa esa causa**, no el que describa la consecuencia.
   `python ../../scripts/cwe_kb.py buscar "eval"` y `relaciones CWE-95` te muestran la jerarquía.
3. **Comprueba el uso para mapear** (`mostrar CWE-xxx`): MITRE indica si una entrada es adecuada
   para clasificar vulnerabilidades concretas (*Allowed*), requiere revisión (*Allowed-with-Review*),
   se desaconseja (*Discouraged*) o está prohibida (*Prohibited*, p. ej. las categorías).
4. **Si hay dos candidatos**, elige el que describe la causa raíz y anota el otro como
   alternativa con su motivo, como hace `cwe-map.json`.
5. **Compáralo con lo que dijo la herramienta**. Si difieren, escribe por qué: esa frase es lo que
   demuestra que entendiste el defecto.

Las decisiones de este laboratorio, con su motivo:

| Caso | Elegido | Descartado y por qué |
|---|---|---|
| MD5 de contraseñas | CWE-916 | CWE-327 es una clase genérica; CWE-328 («hash débil») es su padre. CWE-916 nombra exactamente el problema: poco esfuerzo computacional al guardar contraseñas. |
| `eval` | CWE-95 | CWE-94 es el padre; Bandit propone CWE-78, que describe otra cosa. |
| `debug=True` | CWE-489 | CWE-94 describe lo que *permite* el depurador, no el descuido que lo deja activo. |
| `0.0.0.0` | CWE-1327 | CWE-605 (propuesto por Bandit) trata de enlazar dos veces el mismo puerto. |
| Ruta con `../` | CWE-22 | CWE-23 es más específico (relativo) y válido; se usa CWE-22 por ser el de uso habitual y el del CWE Top 25. CWE-73 es la causa más general. |

## Cómo se demuestra cada corrección

`tests/test_correcciones.py` ejecuta **la misma prueba de ataque** contra la app original y la
corregida. Contra la original el ataque funciona; contra la corregida falla. Una corrección sin una
prueba que fallaba antes de aplicarla es una opinión.

```bash
python -m unittest discover -s tests -v
```

| # | Prueba | Qué demuestra |
|---|---|---|
| 1 | `test_secretos_no_estan_en_el_codigo` | La original contiene ambos secretos; la corregida ninguno (ni en comentarios) y la contraseña viene del entorno sin valor por defecto. |
| 2 | `test_inyeccion_sql` | `x' OR '1'='1` devuelve **todas** las filas en la original y ninguna en la corregida; la entrada legítima sigue funcionando. |
| 3 | `test_inyeccion_de_comandos` | La original pasa `127.0.0.1; echo …` a un shell; la corregida lo rechaza (400) sin ejecutar nada y llama a `ping` con lista de argumentos. |
| 4 | `test_hash_de_contrasena` | MD5 da siempre el mismo valor; scrypt con sal da uno distinto cada vez y se puede verificar; la verificación rechaza hashes manipulados. |
| 5 | `test_deserializacion` | La original **ejecuta** una función elegida por quien envía los bytes; la corregida rechaza el pickle y acepta JSON legítimo. |
| 6 | `test_path_traversal` | La original abre `/var/data/../../etc/passwd` sin normalizar; la corregida bloquea `../`, rutas absolutas y el directorio hermano de nombre parecido (`datos-secretos`). |
| 7 | `test_evaluacion_de_codigo` | La original importa módulos arbitrarios; la corregida solo evalúa aritmética y rechaza llamadas, nombres, potencias (`9**9**9`) y expresiones largas. |
| 8 | `test_depuracion_y_enlace` | Lee el árbol sintáctico: la original llama a `app.run(host="0.0.0.0", debug=True)`; la corregida a `host="127.0.0.1", debug=False`. |

### Defectos que la propia corrección tuvo y que las pruebas atraparon

Un buen recordatorio de por qué se prueba: al escribir `app_corregida.py`, las pruebas detectaron
dos fallos **en la corrección**:

- El comentario que explicaba el arreglo del fallo 1 **copiaba el secreto antiguo**. Un secreto citado
  en un comentario sigue publicado, y un escáner lo encuentra igual.
- La verificación de contraseñas ignoraba el prefijo del esquema: un hash con prefijo `md5$…` y los
  parámetros de scrypt se aceptaba. Ahora se exige `scrypt`.

## Lección

El SAST es excelente como primera red (y como *gate* en CI), pero **no sustituye** la revisión
humana ni las pruebas dinámicas: aquí dejó pasar dos defectos de ocho, y además etiquetó mal tres.
La combinación SAST + revisión de código + DAST/SCA es lo que pide un SDLC seguro (clases 236–248
y 323), y la **clasificación CWE** es un trabajo de criterio sobre el resultado de la herramienta,
no un campo que se copia (clases 361, 362 y 370).
