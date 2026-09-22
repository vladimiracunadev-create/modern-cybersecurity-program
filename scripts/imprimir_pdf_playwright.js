/** Fallback de impresión PDF para hosts donde Chromium no devuelve el proceso headless. */
const path = require('path');
const { pathToFileURL } = require('url');
const { chromium } = require('playwright');

(async () => {
  const [, , input, output] = process.argv;
  if (!input || !output) throw new Error('uso: node imprimir_pdf_playwright.js entrada.html salida.pdf');
  const executablePath = process.env.PLAYWRIGHT_BROWSER || 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
  const browser = await chromium.launch({ executablePath, headless: true, args: ['--disable-gpu'] });
  const page = await browser.newPage();
  await page.goto(pathToFileURL(path.resolve(input)).href, { waitUntil: 'load' });
  await page.pdf({ path: path.resolve(output), format: 'A4', printBackground: true, displayHeaderFooter: false });
  await browser.close();
})().catch(error => { console.error(error); process.exit(1); });
