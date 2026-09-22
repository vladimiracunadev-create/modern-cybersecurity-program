# 🎮 Game Security Engineer / Anti-Cheat Engineer

> Diseña juegos resistentes al abuso, instrumenta la experiencia competitiva y convierte señales
> ambiguas en decisiones auditables. **Nivel de entrada:** avanzado · **Foco:** arquitectura
> cliente-servidor, C++/Python, reversing, telemetría, detección y privacidad.

## 🧭 Qué es y por qué importa

El rol protege integridad competitiva, cuentas, inventarios, economías, matchmaking y servicios de
juego. No se limita a buscar programas prohibidos: trabaja con gameplay, backend, data, soporte,
privacidad y respuesta a incidentes para retirar confianza incorrecta del cliente y medir lo que no
puede prevenirse. Su decisión característica es separar **intención del jugador** de **estado
canónico**, y señal estadística de evidencia suficiente para sancionar.

Se intersecta con Software/Backend Engineer al construir simulación autoritativa; Security y
Reverse Engineer al analizar superficie de cliente; Detection/Data/ML Engineer al diseñar eventos,
features y evaluación; Trust & Safety al gobernar revisión, bans y appeals.

## 🧠 Qué necesitas saber

- Arquitectura de motores, game loop, ECS, física, rendering, input y persistencia.
- C/C++, Python, memoria, reversing y debugging con límites éticos claros.
- Networking en tiempo real: ticks, snapshots, prediction, interpolation y reconciliation.
- Threat modeling, invariantes, state machines, rate limits y secure game development.
- Telemetría versionada, estadística, evaluación de detectores, ML y concept drift.
- Privacidad, mínimo privilegio, supply chain, respuesta, RCA y comunicación de incidentes.

El día a día alterna revisión de un diseño de feature, consultas de telemetría, reproducción de un
abuso en un target interno, tuning con casos legítimos difíciles, code review de validaciones y
postmortem. Sus entregables son threat models, especificaciones de autoridad, schemas, reglas,
datasets, dashboards, paquetes de evidencia, playbooks y regression tests.

## 📚 Tu ruta en el programa

1. [Parte 0](../classes/parte-0-fundamentos-y-prerrequisitos/README.md): procesos, memoria, redes,
   Python y ética (023–025).
2. [Parte 5](../classes/parte-5-explotacion-de-sistemas-y-binarios/README.md): arquitectura,
   debugging, reversing, protecciones y fuzzing (116–140).
3. [Parte 6](../classes/parte-6-analisis-de-malware/README.md): análisis estático/dinámico y
   comportamiento (141–160), aplicado aquí al cliente propio y no repetido.
4. [Partes 8 y 9](../classes/parte-8-blue-team-deteccion-y-soc/README.md): telemetría, detección,
   IR y RCA (182, 188, 199, 201–220).
5. [Parte 15](../classes/parte-15-seguridad-de-ia-y-machine-learning/README.md): evaluación y
   límites de ML (298–300).
6. [Parte 19](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/README.md):
   especialización completa 341–360.

### Laboratorio, portafolio y capstone

- Ejecuta [Game Security Range](../labs/game-security/README.md), conserva seeds y tests.
- Resuelve los [CTF de Game Security](../ctf/game-security/README.md) sin herramientas externas.
- Portafolio mínimo: threat model, módulo autoritativo probado, schema v1, dataset card, regla con
  matriz de confusión, análisis de privacidad y postmortem.
- Capstone: [360](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/360-capstone-incidente-completo-game-security/README.md), con reproducción, RCA y regresión.

## 🎓 Certificaciones

No existe una certificación universal que sustituya el portafolio. Security+, CySA+ o CISSP
aportan base; formación en C++, motores, backend distribuido, estadística/ML y privacidad completa
el perfil. En selección pesa más demostrar decisiones de arquitectura y experimentos reproducibles.

## 📈 Progresión de carrera y salario

La progresión habitual es Gameplay/Backend/Security Engineer → Game Security Engineer → Senior o
Lead Anti-Cheat → Principal/Architect. Otra entrada nace de Detection/Data/ML o Reverse Engineering.
Los salarios dependen fuertemente de país, estudio, plataforma y guardias; esta guía no publica una
cifra sin mercado y fecha verificables. El crecimiento se demuestra reduciendo abuso sin disparar
falsos positivos ni privilegios.

## 🎤 Preguntas de entrevista

1. ¿Cómo conviertes un cliente autoritativo en uno predictivo con servidor autoritativo?
2. ¿Qué diferencia hay entre información conocida y renderizada en un ESP?
3. ¿Cómo evalúas snap aim sin castigar a un jugador experto o a accesibilidad?
4. ¿Qué campos mínimos necesita una investigación reproducible?
5. ¿Cuándo una regla simple es mejor que ML y cómo detectas drift?
6. ¿Cómo respondes a una vulnerabilidad en el propio anti-cheat?

## ⚠️ Mitos y errores comunes

- **«Kernel equivale a seguro».** Más privilegio también aumenta impacto, superficie y deber de cuidado.
- **«Precisión alta prueba cheating».** Puede ocultar imbalance, leakage y falsos positivos costosos.
- **«Ofuscar reemplaza al servidor».** Eleva costo; no corrige autoridad.
- **«Banear rápido siempre ayuda».** Puede revelar señales y hacer irreversible una mala decisión.
- **«El equipo anti-cheat trabaja solo».** Sin gameplay, backend, data, soporte y privacidad no cierra el ciclo.

## 🔗 Volver

- [Índice de rutas](README.md) · [Examen por rol](../docs/examen-final-por-rol.md)
