# Reto 01 — El cliente que mandaba demasiado

El servidor recibe `{"sequence": 7, "claimed_health": 999, "claimed_ammo": 999}` y responde
`{"server_decision":"accept","health":999,"ammo":999}`. No hay corrupción de memoria del
servidor ni bypass criptográfico.

1. Identifica la confianza incorrecta y la causa raíz.
2. Rediseña el mensaje como intención, no resultado.
3. Nombra la prueba de regresión mínima.
4. La flag es `FLAG{<componente>-<principio>}` en minúsculas.

Solo después compara con [la solución](solucion.md).
