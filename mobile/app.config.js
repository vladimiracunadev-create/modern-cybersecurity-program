// Expo necesita conocer el subdirectorio público antes de construir los enlaces
// del HTML y de los assets. Pages usa /modern-cybersecurity-program/app; el ZIP
// de la release se exporta para la raíz. En desarrollo local, /app reproduce la
// disposición final dentro de site/.
module.exports = ({ config }) => ({
  ...config,
  experiments: {
    ...config.experiments,
    baseUrl: Object.prototype.hasOwnProperty.call(process.env, 'EXPO_BASE_URL')
      ? process.env.EXPO_BASE_URL
      : '/app',
  },
});
