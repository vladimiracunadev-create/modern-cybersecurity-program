// ============================================================
// DESIGN SYSTEM — CIBERSEGURIDAD MODERNA
// Colores, espaciado, tipografía y radios usados en toda la app.
// Paleta alineada con el sitio del curso (verde + violeta sobre azul noche).
// ============================================================

export const colors = {
  // Fondos
  bg: '#0b1220',          // fondo principal (azul noche)
  bgCard: '#131c2e',      // fondo de tarjetas
  bgCode: '#0d1117',      // fondo de bloques monoespaciados
  bgInput: '#0f1830',     // fondo de inputs
  bgMuted: '#1b273d',     // fondo secundario suave

  // Acentos
  accent: '#3fb950',      // verde principal (botones, progreso, destacados)
  accentDark: '#2ea043',  // verde oscuro (pressed states)
  accentBlue: '#7c5cff',  // violeta (temas, chips, esquemas)
  accentBlueDark: '#5b3fc7',

  // Texto
  text: '#e6edf3',        // texto principal (casi blanco)
  textMuted: '#94a3b8',   // texto secundario (gris azulado)
  textCode: '#e2e8f0',

  // Estados / semáforo
  warning: '#f59e0b',
  error: '#ef4444',
  success: '#3fb950',
  info: '#3b82f6',

  // Bordes y separadores
  border: '#26314a',
  borderMuted: '#1b273d',
};

export const spacing = { xs: 4, sm: 8, md: 16, lg: 24, xl: 32, xxl: 48 };
export const radius = { sm: 6, md: 12, lg: 20, full: 999 };
export const fontSize = {
  xs: 11, sm: 13, md: 15, lg: 17, xl: 20, xxl: 24, title: 28,
};
export const fontWeight = {
  normal: '400', medium: '500', semibold: '600', bold: '700',
};

/**
 * Color por nivel de dificultad. Los niveles del curso son:
 * Fundamentos · Intermedio · Avanzado · Experto (+ Integrador en capstones).
 */
export const levelColor = (level) => {
  if (!level) return colors.textMuted;
  const l = level.toLowerCase().trim();
  if (l === 'fundamentos') return colors.accent;
  if (l === 'intermedio') return colors.warning;
  if (l === 'avanzado') return colors.error;
  if (l === 'experto') return colors.accentBlue;
  if (l === 'integrador') return colors.info;
  return colors.textMuted;
};
