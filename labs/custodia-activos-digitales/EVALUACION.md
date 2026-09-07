# Evaluación del caso Nebula Custody

## Entregables

1. manifiesto SHA-256 y cadena de custodia;
2. conciliación por activo con fórmula, cobertura, tolerancia y resultado;
3. timeline UTC con referencias a eventos;
4. matriz de evidencias: afirmación, fuente, soporte, contradicción y límite;
5. análisis IAM/PAM/SoD y modelo de amenazas ampliado;
6. causa raíz sin culpa, con causas próximas, contribuyentes y sistémicas;
7. plan preventivo, detectivo y correctivo con responsables y pruebas;
8. informe ejecutivo/técnico usando la plantilla.

## Rúbrica (100 puntos)

| Dimensión | Puntos | Evidencia de dominio |
|---|---:|---|
| Preservación y reproducibilidad | 15 | hashes, originales/copia, procedimiento y límites documentados |
| Conciliación | 20 | tres verdades, Decimal, fees/tiempo/cobertura y diferencia exacta |
| Correlación y timeline | 15 | vínculos trazables; no confunde proximidad temporal con causalidad |
| Razonamiento probatorio | 15 | separa observado, inferido, hipótesis y no determinado |
| Threat model e IAM/PAM/SoD | 15 | abuso/insider, controles independientes y pruebas negativas |
| DFIR, IR y causa raíz | 10 | acciones preservan evidencia y corrigen sistema, no culpan por defecto |
| Arquitectura y controles | 10 | controles preventivos/detectivos/correctivos con dueño y verificación |

**Umbral:** 75/100 y, además, ningún cero en preservación, conciliación o
razonamiento probatorio. Atribuir intención o responsabilidad sin soporte obliga a
corregir el informe antes de aprobar, aunque el cálculo sea correcto.

## Preguntas de defensa oral

1. ¿Qué demuestra un TXID y qué no demuestra?
2. ¿Por qué una autenticación válida no legitima el retiro?
3. ¿Qué explicaciones benignas podrían producir la misma diferencia?
4. ¿Qué campo o fuente ausente limita más tu conclusión?
5. ¿Cómo probarías que el maker no puede aprobar por API aunque la UI lo oculte?
6. ¿Qué cambia si el saldo está en un exchange y no en una wallet propia?
7. ¿Qué control detectaría el caso si PAM, SIEM o reconciliación fallaran por separado?
8. ¿Qué observación sería necesaria para distinguir insider de account takeover?

[← Laboratorio](README.md)
