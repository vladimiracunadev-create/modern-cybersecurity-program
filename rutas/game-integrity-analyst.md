# 🔎 Game Integrity / Anti-Cheat Analyst

> Investiga abuso competitivo con evidencia reproducible, mide falsos positivos y convierte señales
> técnicas en recomendaciones revisables. **Nivel de entrada:** intermedio–avanzado · **Foco:**
> telemetría, consultas, estadística, investigación, sanciones y apelaciones.

## 🧭 Qué es y por qué importa

Este perfil opera la capacidad de Game Security. Revisa alertas y reportes, reconstruye sesiones,
contrasta una hipótesis con comportamiento legítimo, documenta la suficiencia de la evidencia y
propone una acción conforme a política. No diseña por sí solo toda la arquitectura anti-cheat ni
debe convertir el score de una regla o modelo en una sanción automática.

Se diferencia del [Game Security Engineer](game-security-engineer.md): el ingeniero construye
autoridad, instrumentación y controles; el analista investiga sus resultados, encuentra sesgos y
devuelve casos reproducibles para mejorar el sistema. Puede colaborar con Trust & Safety, soporte,
data/ML, privacidad, SOC y DFIR.

## 🧠 Qué necesitas saber

- Arquitectura cliente-servidor, ticks, latencia, predicción y estado autoritativo.
- SQL o consultas equivalentes, Python, schemas versionados y calidad de telemetría.
- Baselines, percentiles, precision/recall, matrices de confusión, segmentación y drift.
- Construcción de timeline, hipótesis alternativas, cadena de evidencia y reporte.
- Política de enforcement, proporcionalidad, revisión humana, apelación y privacidad.
- Comunicación con ingeniería: convertir un patrón repetido en invariante, regla o regresión.

## 📚 Tu ruta en el programa

1. [Parte 0](../classes/parte-0-fundamentos-y-prerrequisitos/README.md): redes, procesos, Python y ética,
   con foco en 011, 023–025.
2. [Parte 1](../classes/parte-1-redes-y-seguridad-de-redes/README.md): tráfico y metadatos (026–027, 045).
3. [Partes 8 y 9](../classes/parte-8-blue-team-deteccion-y-soc/README.md): logging, hunting, detección,
   métricas, investigación y RCA (182, 188, 197–199, 201–202, 208–209, 215–220).
4. [Parte 14](../classes/parte-14-grc-riesgo-y-cumplimiento/README.md): políticas, métricas y privacidad
   (282, 287, 289).
5. [Parte 15](../classes/parte-15-seguridad-de-ia-y-machine-learning/README.md): evaluación y gobernanza
   de modelos (298–300).
6. [Parte 19](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/README.md): fundamentos
   341–343, autoridad 351–354 y núcleo operativo 355–360.

### Laboratorio, portafolio y capstone

- Ejecuta [Game Security Range](../labs/game-security/README.md) y conserva seed, versión y consultas.
- Portafolio mínimo: schema comentado, baseline, consulta de triaje, caso falso positivo, matriz de
  confusión, recomendación proporcionada y RCA que cambie un control.
- Usa el [modelo operativo](../docs/modelo-operativo-game-security.md) para declarar quién investiga,
  quién sanciona y quién atiende la apelación.
- Presenta el [capstone 360](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/360-capstone-incidente-completo-game-security/README.md)
  desde la perspectiva de investigación y decisión.

## 🎓 Certificaciones

No hay una certificación universal que reemplace la evidencia práctica. Una base Blue Team/CySA+,
analítica de datos, privacidad y conocimiento del dominio del juego ayuda, pero el portafolio debe
demostrar que distingues anomalía, abuso e incidente.

## 📈 Progresión de carrera y salario

La progresión habitual puede avanzar desde
soporte técnico, fraude, SOC o análisis de datos hacia Game Integrity Analyst, Senior Analyst y
liderazgo de operaciones o detección. No se publica una cifra salarial sin mercado, moneda y fecha;
varía por país, estudio, plataforma, guardias y responsabilidad sobre decisiones.

## 🎤 Preguntas de entrevista

1. ¿Qué evidencia adicional pedirías antes de actuar sobre una precisión aparente del 99 %?
2. ¿Cómo distingues un snap aim de latencia, espectador, accesibilidad o un jugador experto?
3. ¿Qué debe registrar un caso para que otro analista reproduzca la conclusión?
4. ¿Cuándo escalas a Game Security, Data/ML, privacidad o DFIR?
5. ¿Cómo mides daño de falsos positivos por segmento y no sólo en promedio?
6. ¿Qué cambia en el control después de cerrar un caso confirmado?

## ⚠️ Mitos y errores comunes

- **«Una alerta es un veredicto».** Sólo inicia una investigación.
- **«Más datos siempre ayudan».** También aumentan exposición, coste y riesgo de privacidad.
- **«El modelo explica intención».** Estima patrones bajo supuestos y datos concretos.
- **«La apelación pertenece sólo a soporte».** Su resultado revela fallos de señal, política o proceso.
- **«Cerrar el caso basta».** Sin RCA y regresión, el mismo abuso o falso positivo reaparece.

## 🔗 Volver

- [Índice de rutas](README.md) · [Examen por rol](../docs/examen-final-por-rol.md) ·
  [Modelo operativo](../docs/modelo-operativo-game-security.md)
