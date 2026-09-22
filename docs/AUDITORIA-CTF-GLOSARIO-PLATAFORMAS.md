# Auditoría de CTF, glosario y plataformas de práctica

**Fecha:** 22 de septiembre de 2026

**Alcance:** 360 clases, 20 partes, retos internos, rutas, web, aplicación móvil y CI.

## Estado inicial

- 345 clases contenían una sección de glosario local, pero no existía una vista global ni una comprobación de deriva.
- El repositorio incluía ocho retos internos en siete categorías, con `reto.md` y `solucion.md`, pero sin una plantilla común que exigiera causa raíz, mitigación y detección.
- Varias clases enlazaban plataformas aisladas; no había una guía comparativa de nivel, modalidad, ruta, costo cualitativo y límites de publicación.
- Web y móvil exponían el currículo y un recurso legal transversal, pero no un punto de acceso al vocabulario ni a la práctica externa.

## Matriz de cobertura

| Eje | Existía | Brecha | Cambio aplicado | Fuente de verdad / prueba |
|---|---|---|---|---|
| Teoría → práctica | Clases, labs y retos | El salto a plataformas era implícito | Flujo transversal y progresiones por perfil | [`PLATAFORMAS-DE-PRACTICA.md`](PLATAFORMAS-DE-PRACTICA.md) |
| CTF interno | 8 retos y soluciones | Writeups heterogéneos | Criterios comunes y plantilla reutilizable | [`ctf/README.md`](../ctf/README.md), [`writeup-ctf.md`](../templates/writeup-ctf.md) |
| Glosarios | 345 glosarios locales | Sin deduplicación, aliases ni índice | Generador determinista con trazabilidad a clases | `python scripts/generar_glosario_global.py --check` |
| Plataformas | Enlaces dispersos | Sin comparación ni límites | Matriz oficial de 14 plataformas y reglas | [`PLATAFORMAS-DE-PRACTICA.md`](PLATAFORMAS-DE-PRACTICA.md) |
| Web | Clases, rutas y recursos seleccionados | No publicaba los dos recursos nuevos ni writeups | Generador y navegación ampliados | `python scripts/generar_sitio.py` |
| Móvil | Currículo y recurso legal offline | Sin glosario/plataformas ni búsqueda de recursos | Tres recursos offline y filtro por aliases | `python scripts/generar_curriculum_movil.py --check` |
| CI | Estructura, enlaces, encoding, sitio y app | No protegía la salida generada | Tests unitarios + `--check` del glosario | workflow `CI` |

## Decisiones de consolidación

- No se añadieron clases: la clase 140 y las partes ofensivas, defensivas, forenses y de Game Security ya cubren los fundamentos necesarios.
- No se reemplazaron glosarios locales: siguen aportando significado en contexto; el documento global funciona como índice y trazabilidad.
- No se convirtió cada solución histórica en una narración artificialmente uniforme. Los nuevos aportes deben usar la plantilla, y los retos existentes quedan identificados como material autocontenido con solución comentada.
- No se presentan precios exactos ni tamaños de catálogo volátiles. La guía distingue gratuito, mixto o principalmente de pago y remite al sitio oficial.
- No se publican flags ni walkthroughs de terceros. La guía conserva expresamente las restricciones de HTB y pwn.college.

## Archivos y verificaciones

- Generador: [`scripts/generar_glosario_global.py`](../scripts/generar_glosario_global.py).
- Tests: [`scripts/tests/test_generar_glosario_global.py`](../scripts/tests/test_generar_glosario_global.py).
- Salida generada: [`GLOSARIO-GLOBAL.md`](GLOSARIO-GLOBAL.md).
- Guía externa: [`PLATAFORMAS-DE-PRACTICA.md`](PLATAFORMAS-DE-PRACTICA.md).
- Plantilla: [`templates/writeup-ctf.md`](../templates/writeup-ctf.md).
- Validaciones integradas: estructura/enlaces, UTF-8, Markdown, glosario determinista, sitio, catálogo móvil y bundle final.

## Pendientes deliberados

- Revisar modalidades y políticas de plataforma en cada release; no son datos controlados por este repositorio.
- Migrar una solución histórica a la plantilla solo cuando se amplíe sustancialmente ese reto, para evitar cambios cosméticos masivos.
- Añadir una plataforma únicamente si aporta una modalidad o ruta no cubierta y dispone de fuente oficial verificable.
