# 📱 App móvil Android — guía técnica

La app vive en [`mobile/`](../mobile/README.md) y es una app **Expo / React Native**
que embebe las **340 clases en 19 partes** para leerlas **sin conexión** desde el
teléfono. Cada clase abre su versión completa en el sitio del curso (GitHub Pages) o
en GitHub.

## 🧩 Fuente de verdad y generación del catálogo

El temario embebido **no se escribe a mano**: se genera desde los `README.md` de las
clases, que son la única fuente de verdad.

```bash
python scripts/generar_curriculum_movil.py          # regenera mobile/src/data/classes.js
python scripts/generar_curriculum_movil.py --check   # falla si quedó desincronizado
```

El generador ancla el parseo en el **emoji** de cada sección (🎯 Objetivo, 📚
Resultados, 🗺️ Temas, 📖 Definiciones, 🧰 Herramientas, 🧪 Laboratorio, ✍️ Ejercicios),
que es estable en las 340 clases aunque el texto del encabezado varíe. Por cada clase
emite: número, título, nivel, duración, objetivo, resultados, temas, definiciones,
herramientas, laboratorio, ejercicios y dos enlaces (`siteUrl` a Pages, `githubUrl` a
la fuente). Las partes llevan su foco y el nivel dominante de sus clases.

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
│   ├── components/               PartCard · ClassCard
│   ├── navigation/AppNavigator.js  stack Home → Part → Class
│   ├── utils/enlaces.js          URLs de sitio y GitHub
│   ├── utils/progress.js         progreso local (AsyncStorage)
│   └── theme.js                  design system
└── assets/                       icono · splash · adaptive-icon · favicon
```

No hay Colab ni notebooks (a diferencia del curso de data-science): aquí cada clase es
un `README.md`, así que la app muestra un resumen navegable offline y **enlaza** a la
clase completa.

## 📦 Pipeline de release del APK

El APK **se compila y firma en GitHub Actions**, nunca en local ni se commitea ningún
binario. El workflow [`release-android.yml`](../.github/workflows/release-android.yml)
se dispara al empujar una etiqueta `v*`:

1. Regenera y **verifica** el catálogo (`generar_curriculum_movil.py --check`): un APK
   no puede salir con el temario desincronizado.
2. `npm ci` + `npx expo export` (sanidad del bundle).
3. `npx expo prebuild -p android` → proyecto Android nativo.
4. `./gradlew assembleRelease` con JDK 17 y firma (keystore de los *secrets*, o uno
   efímero como *fallback* que avisa que no permite actualizaciones in-place).
5. `zipalign` + `apksigner` → APK alineado y firmado.
6. Publica el APK + `SHA256SUMS` como assets de la GitHub Release.

### Verificación obligatoria del artefacto

Un build en verde **no** prueba que el APK lleve el contenido. Tras el release hay que
**abrir el APK y contar**: el bundle JS embebido debe contener las 340 clases. Se
verifica descargando el asset y ejecutando el verificador de releases de curso sobre
el APK (comprueba que el `index.android.bundle` no está vacío y que el catálogo viajó
dentro). Solo entonces se da el release por bueno.

> Por qué este paso: un release previo de otra app salió con el catálogo vacío
> (`CLASSES = []`) con todo en verde — checksum válido, versión correcta, 139 MB — y
> se instalaba sin contenido. Las señales de build no dicen nada del payload.

## 🔒 Privacidad

- El temario viaja embebido: se lee **sin conexión**.
- Abrir la clase completa (sitio/GitHub) requiere internet.
- El progreso se guarda **solo en el dispositivo** (AsyncStorage). Sin cuentas, sin
  analítica, sin backend.
