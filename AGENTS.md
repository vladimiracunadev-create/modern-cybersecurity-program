# Estándar permanente de desarrollo pedagógico

Estas reglas se aplican a toda creación, revisión o ampliación de unidades y clases del programa.

## Principio central

El repositorio es un programa profesional de aprendizaje, no un índice temático ni una colección de resúmenes. Cada clase debe permitir comprender, razonar, practicar y verificar el tema sin depender de afirmaciones vacías o de conocimiento implícito.

La **Parte 6 — Análisis de malware** es la referencia canónica de tono y construcción pedagógica: explicación fluida desde primeros principios, conceptos desarrollados en contexto, subsecciones que cubren el temario, diagrama interpretado, práctica coherente y fuentes que respaldan afirmaciones concretas. No se debe usar su cantidad de palabras como plantilla; se debe reproducir su calidad de enseñanza.

## Contenido clase a clase

- Conservar el contenido válido existente y profundizarlo; no reemplazarlo por texto genérico.
- Explicar cada aspecto importante del temario: qué es, cómo funciona, por qué importa, cómo se relaciona con lo anterior, cómo se aplica y cuáles son sus límites.
- Desarrollar causas, mecanismos, decisiones y consecuencias. No limitarse a enumerar herramientas, pasos, siglas o recomendaciones.
- Incluir ejemplos razonados y situaciones concretas cuando ayuden a comprender; explicar por qué cambia la conclusión entre un caso y otro.
- Leer y explicar los diagramas dentro del texto. Cada gráfico debe representar el tema específico de la clase y aportar comprensión, no decorar.
- Incorporar práctica reproducible, criterios de verificación, errores comunes y preguntas que obliguen a razonar.
- Definir términos técnicos en contexto y mantener un glosario útil, sin usar definiciones circulares.
- Revisar y consolidar **toda la clase**: objetivo, resultados, tabla de temas, explicación, definiciones, glosario, preparación, laboratorio, ejercicios, reto, errores, preguntas y referencias. No limitar el trabajo a insertar una sección nueva.
- Comprobar que cada tema anunciado en la tabla se desarrolla de forma explícita en la explicación o práctica. Una tabla no sustituye el contenido.
- Eliminar contradicciones entre secciones, simplificaciones absolutas, afirmaciones publicitarias y frases heredadas que la nueva explicación desmienta.
- El README de entrada de cada parte debe explicar el recorrido clase por clase: qué enseña cada clase, por qué aparece en esa posición, cómo conecta con la anterior y qué evidencia de aprendizaje produce.

## Profundidad y extensión

- No imponer la misma cantidad de palabras ni la misma plantilla narrativa a todas las clases.
- La extensión depende de la complejidad del tema, sus prerequisitos, riesgos, variantes y decisiones profesionales.
- Un tema amplio puede requerir varias subsecciones, ejemplos y diagramas; uno acotado puede ser más breve si queda plenamente explicado.
- Evaluar la calidad por comprensión lograda, claridad causal, cobertura de aspectos y capacidad de aplicar el conocimiento, no por cumplir una cuota de texto.
- Evitar párrafos uniformes, frases intercambiables entre clases, lenguaje robótico y relleno.
- No considerar una unidad terminada por aumentar líneas o palabras. Debe superarse una revisión cualitativa contra la Parte 6 y comprobarse cobertura de todos los temas.

## Fuentes y veracidad

- No inventar datos, capacidades, estándares, versiones, resultados ni consenso profesional.
- Sustentar afirmaciones técnicas en fuentes reales y trazables, priorizando documentación oficial, estándares vigentes, especificaciones y proyectos primarios.
- Indicar qué concepto respalda cada fuente; no añadir enlaces como lista decorativa.
- Comprobar vigencia y reemplazar referencias retiradas o superadas cuando corresponda, explicando el cambio si afecta el contenido.
- Distinguir hechos documentados, inferencias pedagógicas, ejemplos hipotéticos y decisiones que dependen del entorno.
- Expresar límites e incertidumbre: una señal no debe presentarse como prueba concluyente si la fuente no lo sostiene.

## Consolidación y publicación

- Trabajar una unidad completa, clase por clase, manteniendo coherencia y progresión entre ellas.
- Revisar el README de la unidad, el mapa de aprendizaje, las fuentes y los criterios de evaluación junto con sus clases.
- Antes de publicar, validar estructura, enlaces, codificación, trazabilidad de fuentes y diferencias de Git.
- Publicar cada unidad en un commit independiente. No mezclar archivos locales o cambios ajenos.
