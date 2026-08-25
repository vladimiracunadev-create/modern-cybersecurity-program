# Cómo contribuir

Gracias por tu interés en mejorar el **Programa de Ciberseguridad Moderna**.

## Formato de las clases

Cada clase vive en `classes/parte-N-.../NNN-slug/README.md` y sigue una plantilla fija:

1. Encabezado con número, parte, fuentes (libros) y duración estimada.
2. `🎯 Objetivo`
3. `📚 Resultados de aprendizaje` (verificables, con verbos de acción)
4. `🗺️ Temas` (tabla tema → por qué importa)
5. `📖 Definiciones y características`
6. `🧰 Herramientas y preparación`
7. `🧪 Laboratorio guiado` (pasos numerados, reproducibles)
8. `✍️ Ejercicios`
9. `📝 Reto verificable` (con criterio de aceptación)
10. `⚠️ Errores comunes` (tabla síntoma → causa/solución)
11. `❓ Preguntas frecuentes`
12. `🔗 Referencias`
13. `➡️ Siguiente clase`

## Reglas de contenido

- **Español claro**, técnico pero accesible.
- **Ético por diseño**: todo laboratorio ofensivo debe realizarse en entornos propios o autorizados. Incluye siempre la advertencia cuando aplique.
- **No reproducir** texto con copyright de los libros de referencia: cítalos, no los copies.
- **Herramientas reales** y comandos reproducibles; nada de pseudocódigo cuando exista la herramienta.
- Enlaza la clase anterior/siguiente y mantén el índice (`classes/README.md`) coherente.

## Flujo

1. Haz un fork y crea una rama descriptiva.
2. Aplica tus cambios respetando la plantilla.
3. Verifica que los enlaces internos funcionan.
4. Abre un Pull Request explicando qué mejora y por qué.

## Si tocas una clase, regenera lo que se deriva de ella

El `README.md` de la clase es la única fuente de verdad; el sitio, el manual, el material
descargable y el temario de la app móvil **se generan** a partir de él. Tras editar una clase:

```bash
python scripts/mermaid_svg.py                        # diagramas nuevos o modificados
python scripts/generar_curriculum_movil.py           # catálogo de la app (--check en CI)
python scripts/generar_material.py <n_de_parte>      # guía PDF + PPTX de esa parte
python scripts/generar_manual.py                     # manual completo
```

El sitio lo reconstruye el CI en cada `push` a `main`, así que no hace falta commitear `site/`.

### Diagramas

Los diagramas van en bloques ` ```mermaid `. Antes de dar una clase por terminada, comprueba que
el diagrama **compila**: uno con la sintaxis rota no deja un hueco, sino un cartel de *"Syntax
error"* con una bomba, y ese cartel viaja igual al sitio y al PDF. `scripts/mermaid_svg.py` los
rechaza y los cuenta, así que basta con ejecutarlo y mirar el resumen.

Los diagramas dibujados viven en `diagramas/` y **se commitean**: el CI construye el sitio y no
tiene navegador con el que dibujarlos. Si editas un diagrama, ejecuta `scripts/mermaid_svg.py` e
incluye el `.svg` y el `.png` nuevos en el commit.

Tres formas de romperlo que ya han aparecido en este repositorio: usar `;` dentro de un
`Note over` (mermaid lo lee como fin de sentencia), abrir una etiqueta con `[/` (es la sintaxis de
la forma de paralelogramo, no texto — entrecomilla la etiqueta), y dejar espacios dentro de
`{ ... }` en un nodo rombo.
