# Playbooks de kali-mcp mapeados al curso

Los `.md` de `.claude/commands/` de **[kali-mcp](https://github.com/pabpereza/kali-mcp)**
(de *pabpereza*, licencia **MIT**) son **playbooks de pentest orquestado por IA**: cada uno
le dice al agente cómo coordinar herramientas de Kali para una fase concreta.

Aquí los integramos como **puente entre la metodología del curso y la automatización con IA**:
qué automatiza cada comando, en qué fase encaja y **qué clase(s) del programa** te enseñan la
técnica *por debajo* — porque para supervisar al agente (Parte 18) primero tienes que saber
hacerlo a mano.

> 🙏 **Atribución.** Los comandos y su contenido son de **pabpereza/kali-mcp (MIT)**. Aquí
> **no se reproducen**: se catalogan y se enlazan a su archivo original. Descárgalos desde el
> repositorio oficial.
>
> ⚠️ **Uso ético.** Todos son para pentest **autorizado** (laboratorio propio o permiso escrito).
> La IA acelera; la autorización, la supervisión y la responsabilidad son **humanas** (clases 335, 339).

## 🗺️ Catálogo (21 playbooks)

| Playbook (repo) | Qué automatiza | Fase | Clases del curso |
|---|---|---|---|
| [`kali-start`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-start.md) | Inicia la sesión y define el **alcance** | Planificación | 067 (RoE/alcance), 340 |
| [`kali-recon`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-recon.md) | Reconocimiento general | Recon | 068, 069, **334** |
| [`kali-network-discovery`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-network-discovery.md) | Descubrimiento de hosts en la red | Recon | 029, **334** |
| [`kali-mass-scan`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-mass-scan.md) | Escaneo masivo de puertos | Recon | 030, 031, **334** |
| [`kali-subdomain-enum`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-subdomain-enum.md) | Enumeración de subdominios | Recon | 069, 251 |
| [`kali-vuln-scan`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-vuln-scan.md) | Escaneo de vulnerabilidades | Análisis | **071**, **318** |
| [`kali-waf-detect`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-waf-detect.md) | Detección de WAF | Web | 086, 090 |
| [`kali-web-audit`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-web-audit.md) | Auditoría web (OWASP) | Web | Parte 4 (086–115), **336** |
| [`kali-web-fuzz`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-web-fuzz.md) | Fuzzing de rutas/parámetros web | Web | 090, 108, 136 |
| [`kali-wp-audit`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-wp-audit.md) | Auditoría de WordPress | Web | Parte 4, **336** |
| [`kali-osint`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-osint.md) | OSINT de fuentes abiertas | Recon/OSINT | Parte 12 (249–260), **336** |
| [`kali-sniff`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-sniff.md) | Captura/análisis de tráfico | Redes | 026, 040 |
| [`kali-brute`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-brute.md) | Ataques de fuerza bruta a credenciales | Acceso | 081 |
| [`kali-hash-crack`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-hash-crack.md) | Cracking de hashes | Credenciales | **080** |
| [`kali-exploit`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-exploit.md) | Explotación (supervisada) | Explotación | 072–073, Parte 5, **335** |
| [`kali-ad-audit`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-ad-audit.md) | Auditoría de Active Directory | AD | Parte 7 (170–175) |
| [`kali-forensics`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-forensics.md) | Triaje/forense asistido | Defensa/DFIR | Parte 9 (201–220), **337** |
| [`kali-audit`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-audit.md) | Auditoría general de seguridad | Auditoría | 285, 318 |
| [`kali-pentest`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-pentest.md) | Orquesta el pentest (sub-agentes en paralelo) | Todo | 066 (PTES), **340** |
| [`kali-finish`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-finish.md) | Consolida hallazgos y genera el **informe** | Reporte | **085**, **338** |
| [`kali-resume`](https://github.com/pabpereza/kali-mcp/blob/main/.claude/commands/kali-resume.md) | Reanuda una sesión previa | Operación | 338 |

## 🧭 Cómo usar este catálogo

1. **Aprende la técnica a mano** en la clase indicada (columna derecha).
2. **Entiende el playbook** abriendo su `.md` en el repo oficial: verás cómo un agente encadena las herramientas.
3. **Ejecútalo supervisado** en el [lab kali-mcp-ia](README.md) contra un objetivo propio, **validando** cada resultado (recuerda: la IA alucina — clases 331, 335, 338).
4. **Cierra con `kali-finish`** y verifica el informe contra la evidencia real.

## 🔗 Referencias

- **kali-mcp (MIT)** — <https://github.com/pabpereza/kali-mcp> · carpeta `.claude/commands/`.
- [Lab kali-mcp-ia](README.md) y [Parte 18 — IA aplicada a la ciberseguridad](../../classes/parte-18-ia-aplicada-a-la-ciberseguridad/README.md).
