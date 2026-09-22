# Avisos de terceros

Auditoría realizada el **2026-09-22**. Este documento es un inventario operativo, no sustituye los textos de licencia incluidos por cada proveedor. Antes de redistribuir una imagen, binario o bundle, conserva sus avisos y vuelve a comprobar la versión exacta.

El proyecto no relicencia software de terceros. `LICENSE`, `LICENSE-CONTENT.md`, `ASSET_LICENSES.md` y `DATA_LICENSES.md` solo conceden derechos que el titular del proyecto puede otorgar.

## Aplicación móvil y web

`mobile/package-lock.json` es el inventario reproducible y la fuente de verdad por paquete y versión. La revisión de sus metadatos encontró 1.169 entradas con licencia declarada:

| Familia declarada | Entradas |
|---|---:|
| MIT | 995 |
| ISC | 92 |
| BSD-3-Clause | 30 |
| Apache-2.0 | 14 |
| BSD-2-Clause | 12 |
| MPL-2.0 | 9 |
| BlueOak-1.0.0 | 6 |
| `(MIT OR CC0-1.0)` | 4 |
| 0BSD | 2 |
| Unlicense | 2 |
| Otras expresiones individuales | 3 |

Las dependencias directas de Expo, React, React Native, React Navigation, AsyncStorage y sus módulos asociados declaran licencias MIT en el lockfile auditado. Las excepciones transitivas que requieren atención son:

- `lightningcss` y sus paquetes binarios: MPL-2.0;
- `caniuse-lite`: CC BY 4.0;
- `node-forge`: elección `BSD-3-Clause OR GPL-2.0`;
- `rc`: elección `BSD-2-Clause OR MIT OR Apache-2.0`;
- `readline`: identificador histórico `BSD`;
- `type-fest` en varias versiones: elección `MIT OR CC0-1.0`.

`node_modules` no se versiona. Un bundle o APK sí incorpora código de dependencias: quien distribuya esos artefactos debe incluir los avisos exigidos por las versiones resueltas. Consulta los repositorios enlazados desde `mobile/package-lock.json` y el [directorio de licencias SPDX](https://spdx.org/licenses/).

## Generadores y herramientas de CI

| Componente | Uso | Licencia declarada por el proyecto de origen |
|---|---|---|
| Python | runtime de scripts y laboratorios | Python-2.0 |
| Python-Markdown | generación HTML | BSD-3-Clause |
| python-pptx | presentaciones | MIT |
| pypdf | verificación de PDF | BSD-3-Clause |
| Mermaid 11, servido por jsDelivr | render de diagramas | MIT |
| markdownlint-cli2 | lint de Markdown | MIT |
| Bandit | SAST en CI | Apache-2.0 |
| gitleaks | detección de secretos | MIT |
| GitHub Actions de `actions/*` | checkout y runtimes | consulta el aviso del tag/commit usado |

Los navegadores Edge o Chrome usados para renderizar no se distribuyen con el repositorio y mantienen sus propios términos.

## Laboratorios y contenedores

Los archivos Compose y Dockerfile propios están bajo Apache-2.0. Las imágenes y herramientas que descargan conservan sus licencias:

| Componente externo | Dónde se usa | Licencia o condición comprobada |
|---|---|---|
| OWASP Juice Shop | `labs/appsec-web` | MIT |
| Damn Vulnerable Web Application (DVWA) | `labs/appsec-web` | GPL-3.0-or-later |
| Elasticsearch y Kibana 8.15.3, distribución oficial | `labs/blue-team-soc` | Elastic License 2.0; la distribución oficial no queda bajo Apache-2.0 |
| Nmap | `labs/redes-nmap` | Nmap Public Source License; contiene condiciones adicionales de redistribución comercial |
| nginx | `labs/redes-nmap` | BSD-2-Clause para el proyecto nginx; la imagen incluye además paquetes con sus propias licencias |
| OpenSSH | `labs/redes-nmap` | licencias BSD y permisivas incluidas por OpenSSH |
| `delfer/alpine-ftp-server`, `instrumentisto/nmap`, `linuxserver/openssh-server` | `labs/redes-nmap` | imágenes externas; revisar avisos de la etiqueta efectiva antes de redistribuir |
| Debian y Python slim | varios Dockerfile | agregados de paquetes libres; cada paquete conserva su licencia |
| Volatility 3 | `labs/dfir-memoria` | Volatility Software License 1.0 |
| YARA / `yara-python` | `labs/dfir-memoria` | BSD-3-Clause |
| Capstone | `labs/dfir-memoria` | BSD-3-Clause |
| pefile | `labs/dfir-memoria` | MIT |
| Impacket | `labs/red-team-ad` | Apache-2.0 con avisos propios |
| BloodHound.py | `labs/red-team-ad` | MIT |
| NetExec | `labs/red-team-ad` | BSD-2-Clause |
| GOAD | enlazado desde `labs/red-team-ad` | GPL-3.0; se clona por separado y no está incorporado |
| Prowler | `labs/cloud-security` | Apache-2.0 |
| ScoutSuite | `labs/cloud-security` | GPL-2.0 |
| Trivy | `labs/cloud-security`, `labs/devsecops-pipeline` | Apache-2.0 |
| kube-bench | descrito en el laboratorio cloud | Apache-2.0; el Dockerfile actual no lo instala |
| pwntools | `labs/pwn-binarios` | MIT, con dependencias propias |
| PyCryptodome | dependencia opcional de `labs/cripto` | combinación de dominio público, BSD y componentes con avisos propios; revisar su archivo `LICENSE.rst` |
| Semgrep CLI | `labs/appsec-code`, `labs/devsecops-pipeline` | LGPL-2.1-or-later para el motor abierto; reglas y servicios pueden tener términos distintos |
| pip-audit | `labs/devsecops-pipeline` | Apache-2.0 |
| hadolint | `labs/devsecops-pipeline` | GPL-3.0 |
| actionlint | `labs/devsecops-pipeline` | MIT |
| OSV-Scanner | `labs/devsecops-pipeline` | Apache-2.0 |
| RootCause Windows Inspector | enlazado desde `labs/rootcause-windows` | Apache-2.0; se clona por separado |
| kali-mcp, de pabpereza | documentación de Parte 18 y `labs/kali-mcp-ia` | MIT; el repositorio contiene descripciones y mapas propios, no una copia del proyecto |

Las imágenes Docker son distribuciones agregadas. Este cuadro identifica el componente principal, pero no reemplaza `/usr/share/doc`, los labels, SBOM o archivos `LICENSE` presentes dentro de cada imagen.

## Fuentes, libros, normas y certificaciones

`sources/bibliography.json` registra 714 obras externas para trazabilidad. Citarlas o enlazarlas no incorpora su texto ni las pone bajo la licencia del programa. Los nombres y objetivos de certificaciones, marcos, normas y productos permanecen sujetos a los derechos de sus titulares.

## Fuentes primarias consultadas

- Apache License 2.0: <https://www.apache.org/licenses/LICENSE-2.0>
- Creative Commons BY-NC-SA 4.0: <https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode>
- Elastic licensing FAQ y ELv2: <https://www.elastic.co/pricing/faq/licensing> · <https://www.elastic.co/licensing/elastic-license>
- Nmap Public Source License: <https://nmap.org/npsl/>
- DVWA: <https://github.com/digininja/DVWA>
- OWASP Juice Shop: <https://github.com/juice-shop/juice-shop>
- Licencias concretas de paquetes Node: `mobile/package-lock.json` y los repositorios declarados allí.

Si una versión o licencia cambia, actualiza este archivo junto con el manifest o Dockerfile correspondiente. Una referencia a una herramienta no autoriza su uso contra terceros; consulta [SECURITY_AND_ETHICS.md](SECURITY_AND_ETHICS.md).
