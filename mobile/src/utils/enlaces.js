// ============================================================
// UTILIDADES DE ENLACES
// Cada clase del programa es un README.md. La app enlaza a dos sitios:
//   - la página del sitio (GitHub Pages), para leerla con formato;
//   - la fuente en GitHub, para verla en crudo o contribuir.
// Las URLs vienen ya calculadas en el currículo generado (siteUrl / githubUrl);
// este módulo centraliza la configuración por si el repo cambia de nombre.
// ============================================================

export const GITHUB_CONFIG = {
  user: 'vladimiracunadev-create',
  repo: 'modern-cybersecurity-program',
  // `main` es la rama del remoto — con 'master' las páginas darían 404.
  branch: 'main',
};

export const SITE_BASE = `https://${GITHUB_CONFIG.user}.github.io/${GITHUB_CONFIG.repo}`;

/** URL de la página del sitio (Pages) para una carpeta de clase. */
export const getSiteUrl = (classPath) => `${SITE_BASE}/${classPath}/README.html`;

/** URL de la fuente en GitHub para una carpeta de clase. */
export const getGithubUrl = (classPath) => {
  const { user, repo, branch } = GITHUB_CONFIG;
  return `https://github.com/${user}/${repo}/blob/${branch}/${classPath}/README.md`;
};
