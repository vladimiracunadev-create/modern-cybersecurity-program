# 📱 App móvil — Ciberseguridad Moderna

App **Android y web** (Expo / React Native) que embebe las **340 clases en 19 partes** y
los **recursos transversales** del programa completos para leerlos **sin conexión**:
la explicación en profundidad, **los diagramas**, el glosario, el laboratorio, los ejercicios, los errores
comunes y las referencias, no un resumen. Lo único que necesita red son los botones de
enlaces externos al sitio y a GitHub.

> El catálogo (`src/data/classes.js`) **se genera** desde `classes/**/README.md` con
> `python scripts/generar_curriculum_movil.py` — **no se edita a mano**. También incorpora
> `docs/cruzar-la-linea-consecuencias-reales.md`. Un check de integridad (`--check`)
> falla si el archivo quedó desincronizado con cualquiera de sus fuentes.

## 🧭 Qué hace

- **Home** — las 19 partes con su foco, nivel y progreso global (X/340).
- **Recursos** — acceso destacado a «¿Y si cruzas la línea?», con leyes, casos,
  atribución, consecuencias y salidas profesionales; texto y diagramas viajan offline.
- **Parte** — las clases de una parte, con buscador por número, título o tema.
- **Clase** — el README entero, repartido en dos pestañas por el emoji de cada
  sección: *Teoría* (objetivo, resultados, temas, explicación en profundidad,
  definiciones, glosario) y *Práctica* (preparación, laboratorio, ejercicios, reto,
  errores comunes, preguntas frecuentes, referencias), con los diagramas de la clase
  como imagen. Con botones para abrirla en el sitio o en GitHub.
- **Progreso** — marca clases como completadas; se guarda local con AsyncStorage y no
  sale del dispositivo.

## 🏗️ Estructura

```text
mobile/
├── App.js                       Entrada + navegación (tema oscuro)
├── app.json                     Config Expo (nombre, icono, paquete)
├── app.config.js                base URL variable para Pages, ZIP y build local
├── src/
│   ├── data/classes.js          GENERADO: clases y recursos enteros (no editar a mano)
│   ├── data/diagramas.js        GENERADO: mapa hash → PNG de cada diagrama
│   ├── screens/                 HomeScreen · PartScreen · ClassScreen · ResourceScreen
│   ├── components/              PartCard · ClassCard · ClassContent (bloques)
│   ├── navigation/AppNavigator.js
│   ├── utils/                   enlaces.js (sitio/GitHub) · progress.js (AsyncStorage)
│   └── theme.js                 design system (colores, espaciado)
└── assets/
    ├── diagramas/                GENERADO: los diagramas de las clases en PNG
    └── (icono, splash, adaptive-icon, favicon)
```

## 🚀 Desarrollo

```bash
cd mobile
npm install
npm start          # Expo dev server (Expo Go / emulador)
npm run web        # vista en navegador (para verificación rápida)
```

La versión web compilada se publica en
[`/app/`](https://vladimiracunadev-create.github.io/modern-cybersecurity-program/app/)
y también viaja como ZIP en cada release.

Regenerar el catálogo tras editar clases:

```bash
python scripts/generar_curriculum_movil.py          # regenera src/data/classes.js
python scripts/generar_curriculum_movil.py --check  # verifica que está al día
```

## 📦 Release (APK + web + manual)

El APK **se compila y firma en GitHub Actions** (workflow `release-android.yml`) al
empujar una etiqueta `v*`. La release publica APK, aplicación web estática, manual PDF
y `SHA256SUMS`. El APK no se compila localmente ni se commitea. Ver
[docs/APP_MOVIL.md](../docs/APP_MOVIL.md) para el detalle del pipeline y la verificación.

## 🔒 Privacidad

- Todo el contenido viaja embebido, diagramas incluidos: las 340 clases y los recursos
  transversales se leen enteros **sin conexión**.
- Solo requieren internet los enlaces al sitio y a GitHub.
- El progreso se guarda **solo en el dispositivo** (AsyncStorage). La app no tiene
  cuentas, ni analítica, ni backend.
