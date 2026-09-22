# Datasets sintéticos del Game Security Range

`game_security.datasets` genera once perfiles: `normal`, `expert-synthetic`, `snap-aim`,
`smooth-aim`, `tracking`, `trigger`, `speed-anomaly`, `fire-rate-anomaly`, `high-latency`,
`jitter` y `packet-loss`. No contienen datos personales ni capturas de jugadores reales.

Cada fila declara `event_id`, perfil/etiqueta, tiempo de reacción, cambio angular, velocidad,
intervalo entre disparos, latencia y pérdida. La semilla predeterminada es `190341`; cambiarla
permite otra muestra reproducible. Los perfiles son modelos didácticos, no una representación
válida de toda la población ni evidencia suficiente para sancionar.

```powershell
@'
from pathlib import Path
from game_security.datasets import write_csv
write_csv(Path("datasets/out/snap-aim.csv"), "snap-aim", rows=200, seed=190341)
'@ | python -
```

Uso esperado: comparar reglas, estadística y modelos sobre las mismas señales. Limitaciones:
distribuciones simplificadas, independencia artificial entre algunas variables y ausencia de
biomecánica real. Para una evaluación seria hay que validar con datos consentidos, minimizados y
estratificados por dispositivo, latencia, FPS y opciones de accesibilidad.
