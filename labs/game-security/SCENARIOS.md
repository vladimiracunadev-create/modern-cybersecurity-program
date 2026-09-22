# Catálogo de escenarios

| ID | Modo | Causa deliberada | Reproducción | Evidencia y resultado | Mitigación / regresión |
|---|---|---|---|---|---|
| GS-01 | VULNERABLE | Salud confiada al cliente | Enviar `claimed_health=999` | evento aceptado, salud 999 | ignorar el claim; `test_secure_server_rejects_impossible_state` |
| GS-02 | VULNERABLE | Munición local | Enviar `claimed_ammo=999` | munición 999 | inventario autoritativo; prueba GS-01 |
| GS-03 | SECURE | Posición sin plausibilidad | Mover 500 unidades/tick | rechazo `impossible_speed` | invariante de velocidad; prueba de autoridad |
| GS-04 | SECURE | Cadencia imposible | Repetir disparo en 50 ms | rechazo `fire_rate_violation` | cooldown del servidor; prueba de replay/cadencia |
| GS-05 | DETECTION | Snap y reacción correlacionados | perfil `snap-aim` | alerta media explicable | revisión agregada, nunca ban por una muestra |
| GS-06 | DETECTION | Falso positivo plausible | perfil `expert-synthetic` | solapamiento con automatización | segmentar dispositivo/FPS y exigir evidencia múltiple |
| GS-07 | VULNERABLE | Información excesiva | entregar targets no visibles | radar/ESP del propio simulador | relevancia/interest management y minimización |
| GS-08 | SECURE | Replay de comando | reutilizar `sequence` | rechazo `sequence_replay` | secuencia monótona; prueba de replay/cadencia |

Cada escenario sigue `abuso → señal → decisión → causa raíz → corrección → prueba`. `VULNERABLE`
existe para comparar, no para desplegar; `NORMAL` produce tráfico benigno; `SECURE` previene
violaciones de invariantes; `DETECTION` conserva señales y explicaciones para análisis.
