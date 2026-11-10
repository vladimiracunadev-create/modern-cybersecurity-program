# Laboratorio — manipulación física del hardware: auténtico no es íntegro

**Modalidad:** simulación local y determinista con datos ficticios, sin red, sin hardware y sin secretos reales.
**Clases:** [267](../../classes/parte-13-seguridad-movil-iot-e-inalambrica/267-hacking-de-firmware/README.md),
[268](../../classes/parte-13-seguridad-movil-iot-e-inalambrica/268-analisis-de-hardware-uart-jtag-y-spi/README.md) y
[177](../../classes/parte-7-red-team-y-operaciones-ofensivas/177-red-teaming-fisico/README.md), con notas en las clases 213, 215, 237, 246, 284 y 312.
**Caso que inspira el laboratorio:** el implante de hardware confirmado por Ledger en octubre de 2026 en un dispositivo vendido por un
revendedor (ver la clase 267 para el relato causal y sus límites).

> ⚠️ **Ética y alcance.** Todo es ficticio: el dispositivo "Modelo-X", sus componentes, el bus, los consumos y los envíos. El código **no
> contiene** firmware de implante, esquemas de montaje, protocolos o tipografías reales de pantalla, listas de palabras de recuperación
> ni ninguna forma de capturar o transmitir secretos. El "texto" del bus es una cadena inventada codificada con una tabla de glifos
> inventada. No lo adaptes para manipular dispositivos ajenos ni para extraer secretos de nadie.

## Qué aprendes

La idea central es que **tres preguntas distintas** se suelen confundir:

| Pregunta | Qué la responde | Qué NO demuestra |
|---|---|---|
| ¿Es auténtico el secure element? | attestation criptográfica del fabricante | que el resto de la placa sea el original |
| ¿Es íntegro físicamente el dispositivo? | inspección comparada con una referencia, radiografía, microscopía, medidas | quién lo tocó ni cuándo |
| ¿Es continua la cadena de custodia? | registro de eslabones, sellos, canales autorizados | que el contenido del paquete sea el correcto |

Un dispositivo puede pasar la primera y fallar las otras dos: el secure element sigue siendo genuino mientras se le añade electrónica
alrededor. Por eso una verificación de software **no puede** garantizar integridad física (Ledger lo declara así en su modelo de amenazas).

## Ejecutar

```bash
python labs/hardware-tamper-defense/tamper_lab.py run --seed 7 --out labs/hardware-tamper-defense/salida
python -m unittest discover -s labs/hardware-tamper-defense/tests -v
```

Solo biblioteca estándar de Python 3.12. Genera `informe.md` y `resultado.json`; `salida/` se ignora en Git.

## Las tres muestras

| Muestra | Qué es | Qué debería concluir un analista |
|---|---|---|
| **A** | Placa idéntica a la referencia, envío continuo | riesgo bajo; uso normal con controles de rutina |
| **B** | Secure element auténtico + cinco componentes añadidos sin marcado, ráfagas de consumo periódicas, carga extra en el bus y envío con intermediarios no autorizados | autenticidad verificada, integridad **fallida**, custodia **fallida**: riesgo crítico |
| **C** | Pantalla de otro lote, envío continuo | integridad **no concluyente**: parece una reparación, pero hay que comprobar la orden de servicio antes de decidir |

La muestra C existe para que no aprendas a gritar «implante» ante cualquier diferencia: un cambio no es un componente añadido.

## Los ocho ejercicios del laboratorio

| Ejercicio | Función | Qué practicas |
|---|---|---|
| A. Comparar PCB | `comparar_pcb` | diferencias entre una placa de referencia y una inspeccionada, con severidad razonada |
| B. Bus de pantalla | `generar_traza_spi`, `analizar_traza_spi` | entender que el bus lleva lo que se ve, y que un tiempo de subida mayor es un indicio de carga, no una prueba |
| C. Reconocer añadidos | `TIPOS_CRITICOS` | por qué un microcontrolador, un módem o una eSIM no previstos pesan más que un cambio de lote |
| D. Consumo | `detectar_rafagas` | z robusto + duración mínima + periodicidad para separar una radio activa de actividad legítima corta |
| E. Riesgo | `veredictos`, `evaluar_riesgo` | combinar tres veredictos independientes y declarar la acción recomendada |
| F. Custodia | `crear_cadena`, `verificar_cadena`, `auditar_trazabilidad` | cadena de hashes, huecos de custodia, sellos que cambian, devoluciones reabiertas |
| G. Informe | `informe_md` | separar hechos, inferencias y límites |
| H. Distribución | `verificar_controles` | comprobar una política de recepción y entender qué controles son débiles (sellos, masa) |

### Cómo se leen los números

- **Tiempo de subida del bus.** Una señal cuyo flanco tarda más puede indicar carga adicional en la línea, porque cada entrada conectada añade
  capacitancia. Aquí sube de ~22 ns a ~29 ns con 8 pF extra (valores del modelo didáctico). En la vida real depende de la sonda, la longitud del
  cable y la temperatura: es un **indicio**, nunca una prueba.
- **Consumo.** `z = (x − mediana) / max(σ, 0,05)` con `σ = 1,4826·MAD`, en miliamperios. Se exige `z > 6` durante ≥ 3 s y un patrón periódico
  (desviación de los intervalos ≤ 2 s) para marcar «ráfagas». El radio de corto alcance de la referencia produce una ráfaga corta cada 150 s
  que **no** se marca: sin la duración mínima habría un falso positivo.
- **Riesgo.** La suma de puntos es una ayuda de decisión explicada, no una probabilidad.

## Preservación de evidencia (ejercicio F)

1. Fotografía el dispositivo cerrado, con escala y número de sello, **antes** de abrirlo.
2. Registra cada manipulación como un eslabón; el encadenamiento por hash hace visible cualquier edición posterior (el laboratorio demuestra que
   alterar o quitar un eslabón rompe la verificación). El hash prueba que el registro no cambió, no que su contenido sea veraz.
3. No energices ni cargues el dispositivo hasta decidir cómo preservarlo: una radio activa puede enviar datos o recibir órdenes, y un reinicio
   puede cambiar el estado.
4. Aísla del exterior (bolsa o caja de aislamiento de radiofrecuencia) en lugar de apagarlo, y documenta el método.
5. Haz la apertura y las imágenes (microscopía, radiografía) con alguien cualificado y con el consentimiento del propietario; no lo hagas sobre
   dispositivos de terceros.

## Límites

- La simulación valida el razonamiento, no el rendimiento de una técnica real; los umbrales se ajustaron con este generador.
- No sustituye a un laboratorio de análisis electrónico. La radiografía y la microscopía se describen en la clase 268 pero no se simulan aquí.
- La muestra B no reproduce ningún diseño real; los incidentes reales siguen bajo investigación y sus detalles pueden cambiar.

## Retos

1. Añade una muestra D con un componente añadido **con marcado** y justifica si cambia el veredicto.
2. Cambia la duración mínima de ráfaga a 1 s y observa qué falso positivo aparece.
3. Escribe una política de recepción de 8 controles para un revendedor y señala cuáles detectan un implante, cuáles solo un reemplazo grosero y cuáles
   solo dejan trazabilidad.
4. Redacta la nota a usuarios afectados de la muestra B: qué sabes, qué no sabes y qué deben hacer.
5. Explica por qué reiniciar de fábrica el dispositivo B no resuelve nada.
