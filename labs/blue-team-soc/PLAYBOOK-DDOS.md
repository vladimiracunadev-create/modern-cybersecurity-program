# Playbook defensivo — degradación de disponibilidad y posible DDoS

## Cuándo se aplica

Cuando disponibilidad, latencia, PPS/BPS, solicitudes, conexiones, 429/5xx o cardinalidad de
orígenes se apartan de la línea base. La alerta abre una investigación; **mucho tráfico no equivale
automáticamente a DDoS**.

## Preparación

Mantén por servicio: propietario, criticidad, SLO/SLA, dependencias, rangos de origen, baseline por
hora, capacidad del enlace, contactos 24/7 de ISP/CDN/CSP y proveedor de *scrubbing*, canales de
comunicación, autoridad para activar mitigación y criterios de parada. Prueba el runbook con datos
sintéticos al menos una vez al año.

## Detección y confirmación

1. Registra T0, ventana, servicio, alcance y fuente de cada métrica.
2. Compara PPS, BPS, RPS, conexiones y cardinalidad con el mismo periodo de referencia.
3. Correlaciona disponibilidad, latencia, 429/5xx, salud upstream y métricas de dependencias.
4. Contrasta campaña legítima, lanzamiento, crawler, error de aplicación, retry storm, dependencia
   caída y configuración defectuosa.
5. Clasifica provisionalmente: volumétrico, protocolo/estado o aplicación. Mapea T1498 solo si la
   evidencia describe Network DoS; usa T1498.001 o T1498.002 únicamente cuando el mecanismo esté
   corroborado.

## Contención y mitigación

Escala primero donde exista capacidad: ISP/upstream, CDN o *scrubbing*. Protege el origen y aplica
controles específicos y reversibles —ACL para patrones confirmados, *rate limiting*, WAF, caché o
*circuit breakers*— cuidando el tráfico legítimo. Registra cambio, dueño, hora y rollback. Escalar
servidores no basta si el enlace de entrada está saturado.

## Recuperación y cierre

Verifica disponibilidad, latencia, backlog, dependencias y errores durante una ventana acordada;
retira controles temporales de manera gradual. Conserva consultas, métricas del proveedor, cambios y
comunicaciones. El postmortem separa desencadenante de debilidad habilitadora y asigna a cada acción
un dueño, fecha y prueba de regresión.

## Laboratorio reproducible

```bash
python labs/blue-team-soc/analizar_ddos.py
```

1. Calcula medianas de baseline e incidente y explica qué métrica cambia primero.
2. Formula al menos tres hipótesis alternativas y di qué evidencia las refutaría.
3. Construye una línea temporal T0–detección–confirmación–mitigación–recuperación.
4. Propón una defensa por capas y justifica dónde debe absorberse el volumen.
5. Entrega un postmortem con desencadenante, debilidad habilitadora y prueba de regresión.

**Criterio de aceptación:** las cifras se reproducen desde el CSV; cada conclusión cita campo y
ventana; el mapeo ATT&CK distingue técnica de atribución; la mitigación incluye dueño y rollback; la
causa raíz explica por qué hubo impacto. El ejercicio no genera tráfico.

