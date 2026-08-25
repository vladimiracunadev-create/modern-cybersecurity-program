# 📱 App móvil — Ciberseguridad Moderna

App **Android** (Expo / React Native) que embebe las **340 clases en 19 partes** del
programa **completas** para leerlas **sin conexión** desde el móvil: la explicación en
profundidad, **los diagramas**, el glosario, el laboratorio, los ejercicios, los errores
comunes y las referencias, no un resumen. Lo único que necesita red son los botones de
"Abrir la clase" y "GitHub".

> El catálogo (`src/data/classes.js`) **se genera** desde `classes/**/README.md` con
> `python scripts/generar_curriculum_movil.py` — **no se edita a mano**. Un check de
> integridad (`--check`) falla si el archivo quedó desincronizado con las clases.

## 🧭 Qué hace

- **Home** — las 19 partes con su foco, nivel y progreso global (X/340).
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
├── src/
│   ├── data/classes.js          GENERADO: las 340 clases enteras (no editar a mano)
│   ├── data/diagramas.js        GENERADO: mapa hash → PNG de cada diagrama
│   ├── screens/                 HomeScreen · PartScreen · ClassScreen
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

Regenerar el catálogo tras editar clases:

```bash
python scripts/generar_curriculum_movil.py          # regenera src/data/classes.js
python scripts/generar_curriculum_movil.py --check  # verifica que está al día
```

## 📦 Release (APK)

El APK **se compila y firma en GitHub Actions** (workflow `release-android.yml`) al
empujar una etiqueta `v*`, y se publica como asset de la GitHub Release junto a su
`SHA256SUMS`. No se compila localmente ni se commitea ningún binario. Ver
[docs/APP_MOVIL.md](../docs/APP_MOVIL.md) para el detalle del pipeline y la verificación.

## 🔒 Privacidad

- Todo el contenido viaja embebido, diagramas incluidos: las 340 clases se leen
  enteras **sin conexión**.
- Solo requieren internet los enlaces al sitio y a GitHub.
- El progreso se guarda **solo en el dispositivo** (AsyncStorage). La app no tiene
  cuentas, ni analítica, ni backend.
