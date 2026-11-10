# Auditoría de la integración: manipulación física de hardware y caso Ledger/CryptoBilis

> Fecha de la revisión: 10 de noviembre de 2026. Estado verificado: 21 partes y 370 clases (`scripts/validar_estructura.py`). La solicitud original hablaba de 360 clases y 20 partes; esas cifras estaban desfasadas y se usaron las reales. No se crean clases ni partes y no se renumera nada.

## 1. Estado del conocimiento sobre el incidente

| Afirmación | Estado | Fuente |
|---|---|---|
| Ledger confirmó (10 de octubre de 2026) un implante de hardware no autorizado en un dispositivo vendido por un revendedor autorizado, que suspendió ventas | confirmada por cobertura que cita el comunicado | CryptoSlate (secundaria) |
| Genuine Check verifica el secure element por attestation y no detecta modificaciones físicas ni verifica el historial de la cadena de suministro; los sellos no son fiables | **fuente primaria leída** | Ledger Donjon |
| El implante intercepta lo que va a la pantalla, reconstruye la frase de 24 palabras y la envía con módem celular y eSIM; tres generaciones | descrita por Tibane Labs, **solo vía prensa**; el informe primario no pudo abrirse | CryptoSlate, otros medios |
| Los especímenes de Tibane se compraron en mercados japoneses, no al revendedor del incidente; el informe no establece que su diseño sea el usado en los robos | según la cobertura | CryptoSlate |
| Pérdidas: ~91 M USD (Galaxy Digital), ~93,2 M (Bitquery), otras cifras cercanas a 102 M en titulares | **estimaciones de terceros con métodos distintos; no hay total confiable** | varias |
| Número de dispositivos afectados, quién lo hizo, en qué punto de la distribución | **desconocido** | — |

## 2. Matriz de cobertura anterior y posterior

| Tema | Antes | Después | Dónde |
|---|---|---|---|
| UART, JTAG/SWD, SPI | alta (268) | alta, más lectura de PCB y buses como sistema de confianza | 268 |
| Secure element y raíz de confianza | marginal (267) | desarrollada: attestation, qué prueba y qué no | 267 |
| Autenticidad vs integridad física vs custodia | ausente | tabla de cuatro preguntas independientes y laboratorio | 267, laboratorio |
| Evil maid e interdicción | ausente | desarrollada | 177 |
| Anti-tamper / tamper-evident | marginal (STRIDE) | tres niveles con límites | 267, 268 |
| Cadena de suministro de hardware | ausente (246 es de software) | distinguida y desarrollada | 267, 177, nota en 246 |
| Devoluciones y distribución | ausente | política y controles con límites | 177 |
| Inspección visual, rayos X, microscopía, medidas | ausente | tres familias de comprobación | 268, laboratorio |
| Cadena de custodia de un objeto físico | solo digital (201, 312) | aplicada a un dispositivo, con hashes encadenados | 268, nota en 312, laboratorio |
| STRIDE físico | genérico (237) | tabla para un dispositivo de custodia | 267, nota en 237 |
| Respuesta y notificación a usuarios | alta (215–220) | caso con rotación de secretos y comunicación | 267, nota en 215 |
| Terceros y contratos | media (284) | controles de distribución y auditoría | 267, nota en 284 |
| Privacidad y regulación | — | límites y advertencia: no se asigna obligación legal | 267 |

## 3. Reutilización y decisiones

- **Sin clases nuevas.** El material cabe en 267 (confianza y caso), 268 (placa, buses, inspección, evidencia) y 177 (distribución), que ya concentran hardware y seguridad física. Las clases 213, 215, 237, 246, 284 y 312 solo reciben una nota breve que remite a ellas.
- **Sin ruta nueva.** Los roles pedidos se cubren ampliando ocho rutas existentes (`dfir`, `soc-blue-team`, `pentester`, `investigador-seguridad`, `seguridad-infraestructura`, `ciso`, `field-ciso`, `grc`), con clases reutilizadas y una evidencia de aprendizaje por rol. Ingeniero de hardware security y especialista en ingeniería inversa se asignan a `investigador-seguridad`; arquitecto de seguridad a `seguridad-infraestructura`; auditor de cadena de suministro y riesgo tecnológico a `grc`.
- **Laboratorio nuevo `labs/hardware-tamper-defense/`**, solo con biblioteca estándar y datos ficticios, que cubre los ejercicios A–H pedidos. Las imágenes sintéticas se sustituyen por descripciones de componentes (BOM) para no depender de binarios.
- **Límites de seguridad respetados:** el código no contiene firmware de implante, esquemas de montaje, protocolos o tipografías reales de pantalla, listas de palabras de recuperación ni captura o transmisión de secretos. El "texto" del bus es una cadena inventada con una tabla de glifos inventada. Hay pruebas que impiden importar módulos de red o mencionar listas de palabras de recuperación.
- **Fuentes:** siete entradas nuevas (Ledger Donjon, CryptoSlate, MITRE T1195.003, NIST SP 800-193, SP 800-161 Rev. 1, IR 8276; Tibane Labs queda **pendiente** porque la página no pudo leerse).

## 4. Pendiente y límites

- El informe primario de **Tibane Labs** y el comunicado de Ledger en su cuenta de soporte no se pudieron verificar directamente; se citan vía prensa. Cuando estén accesibles hay que revisar las clases 267 y el registro de fuentes.
- No se incorporaron imágenes reales de PCB: la radiografía y la microscopía se explican pero no se simulan.
- La asignación a técnicas de MITRE ATT&CK (T1195.003 y T1200) es interpretativa.
- Los aspectos regulatorios se tratan como advertencias generales; no se verificó normativa de ninguna jurisdicción.
- El incidente sigue en investigación y sus detalles pueden cambiar.
