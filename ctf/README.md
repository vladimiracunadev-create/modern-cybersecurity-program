# 🚩 Retos tipo CTF

Colección de retos estilo *Capture The Flag* para practicar lo aprendido en el programa.
Cada reto es autocontenido (los datos van en el propio enunciado) y trae su **solución
comentada**. El objetivo siempre es encontrar una **flag** con el formato:

```text
FLAG{...}
```

> 🎓 Intenta resolverlo por tu cuenta con `reto.md`; solo después abre `solucion.md`.
> Todo es material didáctico: resuélvelo con tus herramientas en tu propia máquina.

Una flag prueba que alcanzaste el objetivo, pero no que comprendiste el mecanismo.
Después de resolver, documenta evidencia, causa raíz, mitigación y detección con la
[plantilla de writeup](../templates/writeup-ctf.md). Si quieres continuar en un
entorno externo, elige uno desde la [guía de plataformas autorizadas](../docs/PLATAFORMAS-DE-PRACTICA.md)
y revisa primero sus reglas de publicación.

## Categorías

| Categoría | Reto | Dificultad | Parte relacionada |
|---|---|---|---|
| 🔐 Cripto | [Cebolla de encodings](cripto/reto-01-multicapa/reto.md) | ⭐ | [2](../classes/parte-2-criptografia-aplicada/README.md) |
| 🕸️ Web | [El JWT indiscreto](web/reto-01-jwt/reto.md) | ⭐ | [4](../classes/parte-4-seguridad-de-aplicaciones-web/README.md) |
| 🌐 Redes | [Autenticación a la vista](redes/reto-01-basic-auth/reto.md) | ⭐ | [1](../classes/parte-1-redes-y-seguridad-de-redes/README.md) |
| 🔬 Forense | [Lo que esconde el binario](forense/reto-01-strings/reto.md) | ⭐ | [9](../classes/parte-9-forense-digital-y-respuesta-a-incidentes/README.md) |
| 🔎 OSINT | [Postal sin remitente](osint/reto-01-geo/reto.md) | ⭐⭐ | [12](../classes/parte-12-osint-e-ingenieria-social/README.md) |
| 💥 Pwn / Rev | [Reversa el check](pwn/reto-01-xor/reto.md) | ⭐⭐ | [5](../classes/parte-5-explotacion-de-sistemas-y-binarios/README.md) |
| 🎮 Game Security | [El cliente que mandaba demasiado](game-security/reto-01-autoridad/reto.md) · [¿Snap o experto?](game-security/reto-02-falso-positivo/reto.md) | ⭐–⭐⭐ | [19](../classes/parte-19-seguridad-de-videojuegos-cheats-y-anticheat/README.md) |

## Cómo se puntúa

No hay servidor de puntuación: te autoverificas con `solucion.md`. Si quieres montar un
CTF real para un grupo, puedes cargar estos retos en [CTFd](https://ctfd.io/) usando la flag
de cada `solucion.md` como respuesta.

Para evaluar aprendizaje profesional, añade cuatro criterios a la flag: reproducción
del camino, explicación causal, control preventivo y señal de detección. El
[glosario global](../docs/GLOSARIO-GLOBAL.md) ayuda a mantener el vocabulario consistente.

## Reglas

- Resuelve con **tus** herramientas y en **tu** máquina.
- No hace falta fuerza bruta contra ningún servicio externo: todo se resuelve con los datos del enunciado.
- Comparte el *cómo*, no la flag, si ayudas a alguien.

## Aportar retos

¿Tienes un buen reto? Sigue la estructura `ctf/<categoria>/reto-NN-<slug>/` con `reto.md`
(enunciado + datos) y `solucion.md` (writeup + flag). Usa la
[plantilla común](../templates/writeup-ctf.md), declara categoría y dificultad, y
comprueba que ningún paso necesite atacar servicios externos. Ver
[CONTRIBUTING](../CONTRIBUTING.md).
