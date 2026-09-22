# Parte 19 — Seguridad de videojuegos, cheats y anti-cheat

Esta especialización aplica memoria, reversing, redes, detección, estadística, ML y respuesta a incidentes a una pregunta concreta: **¿qué confianza permite una ventaja ilegítima y cómo se corrige sin convertir una señal en culpabilidad?** No repite las Partes 5–9; las usa para razonar sobre un cliente controlado por el jugador, un servidor que decide estado y una operación anti-cheat que también debe ser segura, privada y auditable.

## Resultado profesional

Al terminar, el estudiante puede construir un threat model, reproducir un abuso solo en el target propio, diseñar autoridad e invariantes, crear telemetría minimizada, evaluar reglas/estadística/ML, investigar falsos positivos, ejecutar RCA y entregar una corrección con regresión e informe ejecutivo.

## Prerrequisitos y tiempo

Se recomiendan 023–024, 026–027, 116–140, 141–160, 182, 199, 201–220, 298 y Python. Son **40 horas guiadas** (20 × 120 min), más 20–30 horas de práctica y capstone.

## Bloques de progresión

1. **Fundamentos y superficie de ataque (341–343):** activos, arquitectura y taxonomía.
2. **Cliente, memoria e información (344–347):** estado, trainers, ESP y rendering.
3. **Automatización de apuntado y juego (348–350):** matemática, predicción y bots.
4. **Multiplayer y protocolo (351–352):** autoridad, ticks, replay y reconciliación.
5. **Anti-cheat y observabilidad (353–356):** capas, prevención, eventos y comportamiento.
6. **Analytics, IA y gobernanza (357–359):** estadística, ML, privacidad y sanciones.
7. **Capstone (360):** incidente completo con RCA y regresión.

```mermaid
flowchart LR
  F[341-343 Fundamentos] --> C[344-347 Cliente e información]
  C --> A[348-350 Automatización]
  A --> N[351-352 Autoridad y red]
  N --> D[353-356 Anti-cheat y datos]
  D --> G[357-359 Analytics y gobernanza]
  G --> P[360 Capstone]
```

La progresión avanza de **qué se protege** a **por qué puede romperse**, luego a **cómo se observa sin sobrerreaccionar** y finalmente a **cómo se elimina la causa**. Cada bloque entrega evidencia reutilizada por el siguiente: el threat model fija supuestos; el rango produce eventos; la detección genera hipótesis; estadística y gobernanza limitan la decisión; el capstone demuestra cierre.

## Guía clase por clase

| Clase | Propósito y conexión | Recorrido causal | Evidencia |
|---:|---|---|---|
| [341](./341-introduccion-game-security-modelo-amenazas/README.md) | Introducción a Game Security y modelo de amenazas | Activos, adversarios y fairness → Trust boundaries y threat model | Evidencia reproducible del rango |
| [342](./342-arquitectura-videojuegos-perspectiva-seguridad/README.md) | Arquitectura de videojuegos desde la perspectiva de seguridad | Game loop y entidades → Networking, persistencia y autoridad | Evidencia reproducible del rango |
| [343](./343-taxonomia-tecnica-cheats/README.md) | Taxonomía técnica de cheats | Estado, recursos y movimiento → Automatización conductual y señales | Evidencia reproducible del rango |
| [344](./344-estado-juego-memoria-manipulacion-controlada/README.md) | Estado del juego, memoria y manipulación controlada | Representación y lifetime → Estado local frente a autoritativo | Evidencia reproducible del rango |
| [345](./345-trainers-instrumentacion-cliente/README.md) | Trainers e instrumentación del cliente | Observación, modificación y freeze → Comparación vulnerable/autoritativa | Evidencia reproducible del rango |
| [346](./346-informacion-expuesta-radar-esp-world-to-screen/README.md) | Información expuesta, radar, ESP y world-to-screen | Entidades y coordenadas → Minimización de información | Evidencia reproducible del rango |
| [347](./347-rendering-visibilidad-occlusion-wallhack/README.md) | Rendering, visibilidad, occlusion y wallhack | Pipeline y depth buffer → Demostración y defensa | Evidencia reproducible del rango |
| [348](./348-matematica-aimbot/README.md) | Matemática de un aimbot | Vector2/Vector3 y normalización → Line-of-sight y experimento | Evidencia reproducible del rango |
| [349](./349-aimbot-avanzado-prediccion-smoothing-recoil/README.md) | Aimbot avanzado, predicción, smoothing y recoil | Velocidad, proyectil y tiempo de vuelo → Recoil, spread y señales | Evidencia reproducible del rango |
| [350](./350-triggerbot-macros-input-automation-bots/README.md) | Triggerbot, macros, input automation y bots | Decisión de disparo y timing → Legítimo, asistivo y abusivo | Evidencia reproducible del rango |
| [351](./351-multiplayer-autoridad-nunca-confiar-cliente/README.md) | Multiplayer y autoridad: nunca confiar en el cliente | Client-authoritative vs server-authoritative → Predicción, corrección e invariantes | Evidencia reproducible del rango |
| [352](./352-seguridad-protocolo-juego/README.md) | Seguridad del protocolo de juego | TCP, UDP, WebSocket y ticks → Replay, reorder e invalid state | Evidencia reproducible del rango |
| [353](./353-arquitecturas-anticheat/README.md) | Arquitecturas Anti-Cheat | Defensa por capas → Privacidad, privilegio y enforcement | Evidencia reproducible del rango |
| [354](./354-server-side-anticheat-diseno-autoritativo/README.md) | Server-side Anti-Cheat y diseño autoritativo | Invariants y sanity checks → Reconciliación y regression tests | Evidencia reproducible del rango |
| [355](./355-telemetria-game-security/README.md) | Telemetría para Game Security | Schema y versionado → Minimización y reproducibilidad | Evidencia reproducible del rango |
| [356](./356-deteccion-aimbot-automatizacion-comportamiento/README.md) | Detección de aimbot y automatización por comportamiento | Datasets controlados → Trayectoria, disparo y cambio de target | Evidencia reproducible del rango |
| [357](./357-estadistica-anomalias-falsos-positivos/README.md) | Estadística, anomalías y falsos positivos | Centro, dispersión y percentiles → Precision, recall y errores | Evidencia reproducible del rango |
| [358](./358-machine-learning-aplicado-anticheat/README.md) | Machine Learning aplicado a Anti-Cheat | Features y normalización → Drift, adaptación y explainability | Evidencia reproducible del rango |
| [359](./359-privacidad-gobernanza-sanciones-seguridad-anticheat/README.md) | Privacidad, gobernanza, sanciones y seguridad del propio Anti-Cheat | Minimización y transparencia → Proporcionalidad y auditabilidad | Evidencia reproducible del rango |
| [360](./360-capstone-incidente-completo-game-security/README.md) | Capstone: incidente completo de Game Security | Threat model y reproducción → RCA, mitigación, regresión e informe | Evidencia reproducible del rango |

## Cómo recorrer la parte

Lee la explicación, interpreta el diagrama y ejecuta el laboratorio antes del reto. Conserva un cuaderno con comando, versión, semilla, evento, decisión y limitación. Todos los experimentos ofensivos se restringen al [Game Security Range](../../labs/game-security/README.md); los componentes invasivos se estudian arquitectónicamente y no se implementan.

## Anatomía y evaluación

Cada clase incluye objetivo, resultados verificables, temas, explicación causal, diagrama interpretado, definiciones, glosario, preparación, laboratorio, ejercicios, reto con aceptación, errores, FAQ y fuentes. La evidencia de bloque culmina en un paquete profesional: threat model, reglas del servidor, dataset documentado, evaluación de falsos positivos, ficha de privacidad y reporte de incidente.

## Después de terminar

Continúa con la [ruta Game Security Engineer / Anti-Cheat Engineer](../../rutas/game-security-engineer.md), resuelve la [autoevaluación](../../autoevaluaciones/README.md#parte-19--seguridad-de-videojuegos-cheats-y-anti-cheat), los [retos CTF](../../ctf/game-security/README.md) y presenta el capstone según el [examen final por rol](../../docs/examen-final-por-rol.md).

## Navegación

- [Índice completo](../README.md)
- [Parte 18](../parte-18-ia-aplicada-a-la-ciberseguridad/README.md)
