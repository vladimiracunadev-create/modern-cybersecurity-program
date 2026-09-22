# Clase 345 — Trainers e instrumentación del cliente

> Parte: **19 — Seguridad de videojuegos, cheats y anti-cheat** · Fuente principal: documentación de Epic Games y Valve
> ⏱️ Duración estimada: **120 min** · Nivel: **Avanzado**

---

## 🎯 Objetivo

Comprender y verificar **trainers e instrumentación del cliente** sobre el Game Security Range, conectando vulnerabilidad, abuso controlado, telemetría, evidencia, causa raíz, mitigación y prueba de regresión sin actuar sobre software de terceros.

## 📚 Resultados de aprendizaje

Al finalizar, el alumno podrá:

1. **Explicar** observación, modificación y freeze desde la arquitectura y no solo desde la herramienta.
2. **Relacionar** toggles y ui con una frontera de confianza concreta.
3. **Producir** evidencia reproducible sobre integridad y detección.
4. **Evaluar** límites, falsos positivos y consecuencias de comparación vulnerable/autoritativa.
5. **Verificar** una mitigación mediante un caso legítimo y uno adversarial.

## 🗺️ Temas

| # | Tema | Evidencia esperada |
|---|---|---|
| 1 | Observación, modificación y freeze | Produce una decisión o evidencia verificable |
| 2 | Toggles y UI | Produce una decisión o evidencia verificable |
| 3 | Integridad y detección | Produce una decisión o evidencia verificable |
| 4 | Comparación vulnerable/autoritativa | Produce una decisión o evidencia verificable |

## 🧠 Explicación en profundidad

Un trainer educativo tiene tres planos: observa un campo del target conocido, solicita una modificación y expone un control de UI como toggle o freeze. Freeze no es magia: vuelve a imponer un valor cada vez que el juego intenta cambiarlo. Esa carrera produce señales —transiciones imposibles, divergencia entre comando y resultado, frecuencia artificial— pero detectar el mecanismo no debe sustituir validar el estado.

La instrumentación también es legítima: depuradores, herramientas de accesibilidad y overlays de rendimiento observan procesos. Por eso 'herramienta presente' no equivale a abuso. El rango compara el mismo intento en VULNERABLE y SECURE: el primero acepta el claim; el segundo registra y rechaza. Integridad de cliente aporta evidencia con limitaciones de privilegio, compatibilidad y privacidad; autoridad reduce el número de resultados que un cliente alterado puede conseguir.

```mermaid
flowchart LR
  A[Supuesto de observaci-n-modificaci-n-y-freeze] --> B[Abuso controlado]
  B --> C[Señal observable]
  C --> D[Decisión con contexto]
  D --> E[Mitigación y regresión]
  E -. valida .-> A
```

El diagrama se lee como un bucle de ingeniería, no como una cadena de sanción. El supuesto habilita un abuso dentro del target propio; la señal solo permite formular una hipótesis; la decisión incorpora contexto; la mitigación debe volver al supuesto y demostrar con una regresión que la confianza cambió. Si el último arco no puede verificarse, solo se ocultó el síntoma.

## 📖 Definiciones y características

- **Señal:** medida observable; característica clave: no prueba por sí sola intención.
- **Evidencia:** señal contextualizada y reproducible; característica clave: trazabilidad.
- **Autoridad:** componente que decide el estado canónico; característica clave: valida intenciones.
- **Causa raíz:** condición sistémica que permitió el incidente; característica clave: su corrección evita recurrencia.

## 📔 Glosario

| Término | Definición en contexto |
|---|---|
| Observación, | Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza. |
| Toggles | Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza. |
| Integridad | Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza. |
| Comparación | Concepto de esta clase aplicado al Game Security Range y a su frontera de confianza. |

## 🧰 Herramientas y preparación

- Python 3.12 y el [Game Security Range](../../../labs/game-security/README.md).
- Escenario correspondiente de [SCENARIOS.md](../../../labs/game-security/SCENARIOS.md).
- Dataset sintético documentado; nunca datos personales ni procesos de terceros.
- Prerrequisitos: clases 023–024 (procesos/memoria), 130–134 (RE/debugging), 182/199 (telemetría/detección) y 217 (RCA).

## 🧪 Laboratorio guiado

1. Ejecuta `python -m unittest discover -s tests -v` desde `labs/game-security` y conserva la línea base.
2. Implementa un toggle solo sobre `claimed_ammo` del rango y registra diez intentos. Compara prevención, telemetría y falsos positivos en ambos modos.
3. Registra modo, comando, decisión, señal, umbral o invariante, semilla y resultado esperado.
4. Formula al menos una explicación legítima alternativa antes de atribuir abuso.
5. Aplica o diseña la mitigación y repite el caso adversarial y un caso normal.
6. Redacta la cadena `síntoma → timeline → evidencia → hipótesis → causa raíz → fix → regresión`.

## ✍️ Ejercicios

1. Explica qué cambia si el cliente controla el dato frente a si solo solicita una acción.
2. Identifica una señal débil y combínala con otra fuente independiente.
3. Diseña un caso límite de latencia, FPS, dispositivo o accesibilidad.
4. Separa prevención, detección, respuesta y gobernanza para este tema.
5. Explica qué información no necesitas recoger y por qué.

## 📝 Reto verificable

Entrega una ficha con threat boundary, reproducción en el rango, evento de telemetría, decisión explicada, alternativa legítima, causa raíz, mitigación y prueba de regresión.

**Criterio de aceptación:** otra persona puede ejecutar los comandos con la misma semilla, obtener la evidencia citada y comprobar que la mitigación bloquea el caso adversarial sin romper el caso normal.

## ⚠️ Errores comunes

| Síntoma | Causa y corrección |
|---|---|
| La anomalía se trata como culpabilidad | Falta contexto; correlaciona y revisa alternativas legítimas. |
| El control solo oculta un valor | La autoridad no cambió; valida o deriva el estado en servidor. |
| El experimento no se reproduce | Faltan semilla, versión, unidades o configuración; regístralas. |
| El detector castiga lag/FPS | El dataset no estratifica condiciones; evalúa por subpoblación. |
| Se propone instrumentar terceros | Fuera del alcance; usa exclusivamente el target educativo. |

## ❓ Preguntas frecuentes

**¿Una alerta basta para sancionar?** No. Es una hipótesis con un nivel de confianza; la consecuencia exige evidencia proporcional, política, auditabilidad y apelación.

**¿Ofuscar el cliente resuelve el problema?** Puede elevar costo, pero no reemplaza autoridad, invariantes ni minimización de información.

**¿Por qué el laboratorio es sintético?** Permite controlar verdad, semilla y falsos positivos sin invadir jugadores ni construir una herramienta reutilizable contra terceros.

## 🔗 Referencias

- Epic Games, *Networking Overview* — autoridad y replicación aplicadas a Toggles y UI. <https://dev.epicgames.com/documentation/unreal-engine/networking-overview-for-unreal-engine>
- Valve, *Latency Compensating Methods* — predicción, interpolación y límites usados para Comparación vulnerable/autoritativa. <https://developer.valvesoftware.com/wiki/Latency_Compensating_Methods_in_Client/Server_In-game_Protocol_Design_and_Optimization>
- Montero et al., *Anticheat System Based on Reinforcement Learning Agents in Unity* — ejemplo académico para contrastar prevención y detección en la clase 345. <https://doi.org/10.3390/info13040173>

## ⬅️ Clase anterior

[Clase 344 — Estado del juego, memoria y manipulación controlada](../344-estado-juego-memoria-manipulacion-controlada/README.md)

## ➡️ Siguiente clase

[Clase 346 — Información expuesta, radar, ESP y world-to-screen](../346-informacion-expuesta-radar-esp-world-to-screen/README.md)
