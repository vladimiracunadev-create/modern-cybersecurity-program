# 📱 App móvil Android — guía técnica

La app vive en [`mobile/`](../mobile/README.md) y es una app **Expo / React Native**
que embebe las **340 clases en 19 partes** para leerlas **sin conexión** desde el
teléfono. Desde la versión **1.1.0** cada clase viaja **entera** —explicación en
profundidad, glosario, laboratorio, ejercicios, reto, errores comunes, preguntas
frecuentes y referencias—, no un resumen: lo que se lee en el móvil es la misma clase
que se lee en el sitio. Los enlaces al sitio y a GitHub siguen ahí para ver los
diagramas dibujados y la fuente en Markdown.

## 🧩 Fuente de verdad y generación del catálogo

El temario embebido **no se escribe a mano**: se genera desde los `README.md` de las
clases, que son la única fuente de verdad.

```bash
python scripts/generar_curriculum_movil.py          # regenera mobile/src/data/classes.js
python scripts/generar_curriculum_movil.py --check   # falla si quedó desincronizado
```

El generador ancla el parseo en el **emoji** de cada sección, que es estable en las
340 clases aunque el texto del encabezado varíe ("🧪 Laboratorio guiado (defensivo)"
sigue siendo el laboratorio). Por cada clase emite dos cosas:

- **Los campos de tarjeta** —número, título, nivel, duración, objetivo, resultados,
  temas, definiciones, herramientas, laboratorio, ejercicios— que alimentan el Home,
  el listado de la parte y el buscador, más `siteUrl` y `githubUrl`.
- **`content`: la clase completa**, convertida en una secuencia de bloques
  (`h2`/`h3` encabezados, `p` párrafos, `li` viñetas con su nivel, `table` tablas con
  cabecera, `code` bloques de código literales, `q` citas y `dg` marcas de diagrama),
  repartida en dos listas según el emoji de la sección:

  | Pestaña | Secciones |
  |---|---|
  | `theory` | 🎯 Objetivo · 📚 Resultados · 🗺️ Temas · 🧠 Explicación en profundidad · 📖 Definiciones · 📔 Glosario |
  | `practice` | 🧰 Herramientas y preparación · 🧪 Laboratorio guiado · ✍️ Ejercicios · 📝 Reto verificable · ⚠️ Errores comunes · ❓ Preguntas frecuentes · 🔗 Referencias |

  Se descartan 📥 Material descargable, ⬅️ Clase anterior y ➡️ Siguiente clase: son
  navegación del repositorio, no contenido de la clase.

Los bloques ` ```mermaid ` no se emiten como código —sería el texto del diagrama
colado como prosa— sino como un bloque `dg` que remite a la versión web. La app pinta
`<Text>`, no dibuja SVG.

Las partes llevan su foco y el nivel dominante de sus clases.

El fichero generado pasó de ~1,4 MB a ~5,7 MB al embeber el cuerpo de las clases, y el
bundle web de ~2,0 MB a ~6,2 MB. Es el precio de que la clase se lea sin conexión; se
emite **una clase por línea** para que el diff siga siendo legible.

> El `--check` está pensado para correr en CI o antes de un release: si alguien edita
> una clase y no regenera, el check lo detecta.

## 🏗️ Arquitectura de la app

```text
mobile/
├── App.js                       Entrada + NavigationContainer (tema oscuro)
├── src/
│   ├── data/classes.js          GENERADO: 340 clases + 19 partes
│   ├── screens/
│   │   ├── HomeScreen.js         19 partes + progreso global
│   │   ├── PartScreen.js         clases de una parte + buscador
│   │   └── ClassScreen.js        detalle: Teoría / Práctica + enlaces
│   ├── components/
│   │   ├── PartCard.js · ClassCard.js   tarjetas de parte y de clase
│   │   └── ClassContent.js       pinta los bloques de la clase completa
│   ├── navigation/AppNavigator.js  stack Home → Part → Class
│   ├── utils/enlaces.js          URLs de sitio y GitHub
│   ├── utils/progress.js         progreso local (AsyncStorage)
│   └── theme.js                  design system
└── assets/                       icono · splash · adaptive-icon · favicon
```

No hay Colab ni notebooks (a diferencia del curso de data-science): aquí cada clase es
un `README.md`, y la app lo pinta entero con `ClassContent`. Un bloque de tipo
desconocido se ignora en vez de romper la pantalla, así que una app antigua sigue
abriendo una clase generada por una versión más nueva del generador; y si el catálogo
embebido no trae `content` (versiones ≤ 1.0.0), `ClassScreen` cae al resumen de
siempre en lugar de quedarse en blanco.

## 📦 Pipeline de release del APK

El APK **se compila y firma en GitHub Actions**, nunca en local ni se commitea ningún
binario. El workflow [`release-android.yml`](../.github/workflows/release-android.yml)
se dispara al empujar una etiqueta `v*`:

1. Regenera y **verifica** el catálogo (`generar_curriculum_movil.py --check`): un APK
   no puede salir con el temario desincronizado.
2. `npm ci` + `npx expo export` (sanidad del bundle) y `verificar_bundle.py` sobre el
   bundle web: si el contenido no viajó, se descubre antes de compilar el APK.
3. `npx expo prebuild -p android` → proyecto Android nativo.
4. `./gradlew assembleRelease` con JDK 17 y firma (keystore de los *secrets*, o uno
   efímero como *fallback* que avisa que no permite actualizaciones in-place).
5. `zipalign` + `apksigner` → APK alineado y firmado.
6. Se abre el APK y se verifica el contenido dentro del bytecode (ver abajo).
7. Publica el APK + `SHA256SUMS` como assets de la GitHub Release.

### Verificación obligatoria del artefacto

Un build en verde **no** prueba que el APK lleve el contenido. El workflow descomprime
el APK, extrae `assets/index.android.bundle` y ejecuta
[`scripts/verificar_bundle.py`](../scripts/verificar_bundle.py) sobre el bytecode:

```bash
python scripts/verificar_bundle.py ruta/al/index.android.bundle
```

El verificador **no** se conforma con que el fichero pese: busca dentro de sus bytes

1. el slug de las 19 partes;
2. el título de una muestra determinista de clases (una de cada 40);
3. **párrafos completos** de la teoría y de la práctica de esas mismas clases —la
   comprobación que distingue "viaja el índice" de "viaja la clase";
4. los encabezados de glosario, errores comunes, preguntas frecuentes y referencias;
5. que el bundle pese al menos lo que ocupa el texto embebido.

Los marcadores se derivan de `mobile/src/data/classes.js` en cada ejecución, así que
no hay que mantener una lista de frases a mano. Cada marcador se busca en las formas
en que puede estar guardado —UTF-8, UTF-16LE (Hermes usa UTF-16 para las cadenas con
tildes) y escapado `\xNN`/`\uXXXX` (bundle web)—; buscar solo una daría un falso
negativo en cuanto el texto llevara un acento.

Comprobado contra el bundle de la 1.0.0: el verificador **falla** con el catálogo
resumido, que es justo lo que tiene que hacer.

> Por qué este paso: un release previo de otra app salió con el catálogo vacío
> (`CLASSES = []`) con todo en verde — checksum válido, versión correcta, 139 MB — y
> se instalaba sin contenido. Las señales de build no dicen nada del payload.

## 🔒 Privacidad

- El contenido viaja embebido: las 340 clases se leen **enteras y sin conexión**.
- Solo requieren internet los diagramas y los enlaces al sitio y a GitHub.
- El progreso se guarda **solo en el dispositivo** (AsyncStorage). Sin cuentas, sin
  analítica, sin backend.
