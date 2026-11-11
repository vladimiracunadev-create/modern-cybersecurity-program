# Matriz curricular — octubre de 2026

> Fuente de datos: `knowledge/cve/2026-10/mapa-curricular.json`. Una fila por CVE: debilidad (CWE del registro) → clase que lo desarrolla → laboratorio → evaluación. La asignación a clases es una **decisión pedagógica**; la prueba `test_mapa_curricular` comprueba que cada clase y archivo citado existe.

| CVE | Producto | Familia | CWE (registro) | Clase canónica | Otras clases | Laboratorio | Evaluación |
|---|---|---|---|---|---|---|---|
| `CVE-2015-3306` | ProFTPD ProFTPD | control-de-acceso | 284 | 105 | 367 | — | preguntas.json |
| `CVE-2015-5477` | ISC BIND | memoria | 617 | 365 | 367 | — | preguntas.json |
| `CVE-2016-3081` | Apache Struts | inyeccion-de-comandos | 77 | 95 | 367 | destinos_y_rutas.py::argv_seguro | preguntas.json |
| `CVE-2021-3199` | ONLYOFFICE Docs | path-traversal | 22 | 105 | 367 | destinos_y_rutas.py::ruta_segura | preguntas.json |
| `CVE-2023-22894` | Strapi Strapi | exposicion-de-informacion | 312 | 364 | 367 | — | — |
| `CVE-2025-61624` | Fortinet Multiple Products | path-traversal | 22 | 105 | — | destinos_y_rutas.py::ruta_segura | preguntas.json |
| `CVE-2026-0322` | Palo Alto Networks PAN-OS | inyeccion-de-codigo | 94 | 95 | 222 | — | preguntas.json |
| `CVE-2026-102489` | Zammad GmbH Zammad | autenticacion | 384 | 101 | — | — | preguntas.json |
| `CVE-2026-102490` | Zammad GmbH Zammad | escalada-local | 269 | 101 | 366 | — | preguntas.json |
| `CVE-2026-102764` | BeyondTrust Remote Support | autenticacion | 290 | 101 | 105 | — | preguntas.json |
| `CVE-2026-104286` | Fortinet FortiMail | path-traversal | 22 | 105 | — | destinos_y_rutas.py::ruta_segura | preguntas.json |
| `CVE-2026-104935` | Ivanti Connect Secure | autenticacion | 290 | 101 | 222, 245 | respaldo_y_triaje.py::triaje_del_mes | preguntas.json |
| `CVE-2026-105133` | Ahsay AhsayCBS | autenticacion | 287 | 101 | 105 | — | preguntas.json |
| `CVE-2026-105134` | Ahsay AhsayCBS | inyeccion-de-comandos | 77, 78 | 95 | 199, 245 | destinos_y_rutas.py::argv_seguro | preguntas.json |
| `CVE-2026-106931` | EG Secure Solutions SiteGuard Server Edition | inyeccion-de-comandos | 78 | 95 | — | destinos_y_rutas.py::argv_seguro | preguntas.json |
| `CVE-2026-109618` | PHP Group PHP | memoria | 1325, 1419, 416, 755, 824 | 365 | — | — | preguntas.json |
| `CVE-2026-109619` | PHP Group PHP | memoria | 1325, 1419, 416, 755, 824 | 365 | — | — | preguntas.json |
| `CVE-2026-110447` | Collabora Collabora Online – Built-in CODE Server | inyeccion-de-comandos | 78 | 95 | 245 | destinos_y_rutas.py::argv_seguro | preguntas.json |
| `CVE-2026-110936` | Siemens Software Center | ruta-de-busqueda | 427 | 366 | — | — | — |
| `CVE-2026-111357` | Ivanti Connect Secure | autenticacion | 829 | 101 | 364 | respaldo_y_triaje.py::triaje_del_mes | preguntas.json |
| `CVE-2026-111497` | Google Brotli | memoria | 252, 787 | 365 | 363 | — | preguntas.json |
| `CVE-2026-114625` | Arista VeloCloud Orchestrator | autorizacion | 89 | 101 | 363, 364 | — | preguntas.json |
| `CVE-2026-118527` | Ivanti Connect Secure | fechas-de-un-cve | 340 | 367 | 105 | respaldo_y_triaje.py::triaje_del_mes | preguntas.json |
| `CVE-2026-21589` | Atlassian Multiple Products | exposicion-de-archivos | 552 | 105 | 366 | destinos_y_rutas.py::ruta_segura | preguntas.json |
| `CVE-2026-41709` | Broadcom VMware ESX | registro-insuficiente | 778 | 369 | 199, 364 | respaldo_y_triaje.py::triaje_del_mes | preguntas.json |
| `CVE-2026-46300` | Linux Kernel | memoria | 123, 456 | 365 | 366 | — | preguntas.json |
| `CVE-2026-48356` | Adobe Commerce and Magento | carga-de-archivos | 434 | 105 | 95 | destinos_y_rutas.py::ruta_segura | preguntas.json |
| `CVE-2026-76418` | Cisco Secure Firewall ASA Software and Cisco Secure FTD Software | manejo-de-condiciones | 690 | 365 | — | — | preguntas.json |
| `CVE-2026-76519` | Cisco Secure Email Gateway | path-traversal | 23 | 105 | — | destinos_y_rutas.py::ruta_segura | preguntas.json |
| `CVE-2026-88779` | Citrix NetScaler | memoria | 119 | 365 | — | — | preguntas.json |
| `CVE-2026-96652` | Plex Media Server | ssrf | 918 | 99 | 222 | destinos_y_rutas.py::validar_destino | preguntas.json |
| `CVE-2026-96654` | Plex Media Server | neutralizacion-de-esquema-url | 84 | 99 | 95 | destinos_y_rutas.py::validar_destino | preguntas.json |
| `CVE-2026-96655` | Plex Media Server | ssrf | 918 | 99 | 222 | destinos_y_rutas.py::validar_destino | preguntas.json |
| `CVE-2026-96656` | Plex Media Server | escritura-de-archivos | 73 | 105 | 366 | destinos_y_rutas.py::ruta_segura | preguntas.json |
| `CVE-2026-96951` | Microsoft Windows | inyeccion-de-comandos | 77 | 95 | — | destinos_y_rutas.py::argv_seguro | preguntas.json |
| `CVE-2026-97229` | GitLab Community Edition and Enterprise Edition | enteros | 190 | 365 | 363, 245 | — | preguntas.json |

Por clase: 95 (inyección), 99 (SSRF), 101 (autenticación), 105 (rutas y archivos), 365 (memoria y enteros), 367 (fechas), 199 (detección), 222 (identidades de aplicación), 216 (recuperación), 241 (secretos), 245 (borde y gestión de vulnerabilidades) y 369 (priorización). Las clases con «—» en evaluación reciben el CVE como apoyo de otra clase canónica.
