# 🕸️ Threat Intelligence Analyst / Analista CTI

> Convierte observables dispersos en inteligencia con procedencia, confianza, vigencia y una
> decisión destinataria. **Nivel de entrada:** intermedio–avanzado · **Foco:** colecciones,
> relaciones, TTP, hipótesis, estimación y comunicación.

## 🧭 Qué es y por qué importa

El analista CTI explica qué amenaza importa para una organización, qué se sabe, qué se infiere,
qué falta y qué decisión puede tomarse. Mantiene separados actor, capacidad, infraestructura,
servicio, cliente, campaña, objetivo e indicador. En CaaS esa separación evita atribuir una campaña
al proveedor de infraestructura, tratar una IP compartida como identidad o confundir una marca
criminal con una capacidad que puede reaparecer bajo otro nombre.

No es un SOC con más feeds. El SOC actúa sobre eventos propios; CTI construye contexto y requisitos
de inteligencia para detección, hunting, respuesta, gestión de terceros y dirección. Tampoco es una
autoridad investigadora: conserva hechos públicos y telemetría autorizada, y expresa incertidumbre.

## 🧠 Qué necesitas saber

- Redes, DNS, hosting, malware, campañas, respuesta a incidentes y ecosistemas criminales.
- Requisitos de inteligencia, plan de colección, evaluación de fuentes y análisis de hipótesis.
- STIX/TAXII, MISP u OpenCTI, MITRE ATT&CK y Diamond Model como modelos, no como prueba automática.
- Procedencia, ventana temporal, confianza, vigencia, sesgos y lenguaje estimativo.
- TLP, privacidad, riesgo legal y límites de investigar infraestructura o foros de terceros.
- Comunicación táctica, operacional, estratégica y ejecutiva con acciones concretas.

## 📚 Tu ruta en el programa

1. [Parte 0](../classes/parte-0-fundamentos-y-prerrequisitos/README.md): redes, sistemas, Python y
   ética, con foco en 011, 023–025.
2. [Partes 1 y 6](../classes/parte-1-redes-y-seguridad-de-redes/README.md): tráfico, NetFlow,
   comportamiento de malware e inteligencia derivada (026–027, 045, 149, 154, 157).
3. [Partes 7–9](../classes/parte-8-blue-team-deteccion-y-soc/README.md): adversary emulation,
   hunting, CTI operacional, detección, IR y línea temporal (161–180, 187–195, 201–220).
4. [Parte 12](../classes/parte-12-osint-e-ingenieria-social/README.md): OSINT y OPSEC (249–255, 260).
5. [Partes 14 y 17](../classes/parte-17-profundizacion-para-certificaciones/README.md): riesgo de
   terceros, comunicación y CTI avanzada (284, 321–322).
6. Recurso transversal [Cybercrime-as-a-Service](../docs/cybercrime-as-a-service.md): modelo de
   mercado, DDoS-for-hire, niveles de evidencia y coordinación por rol.

### Laboratorio, portafolio y capstone

- Usa telemetría sintética del [escenario DDoS](../labs/blue-team-soc/PLAYBOOK-DDOS.md) y fuentes
  públicas primarias; no interactúes con servicios criminales ni infraestructura sospechosa.
- Portafolio mínimo: PIR, plan de colección, tabla de procedencia, grafo de relaciones, dos
  hipótesis alternativas, estimación con nivel de confianza, paquete SOC y briefing ejecutivo.
- Entrega indicadores con contexto, ventana, propósito, confianza y condición de retiro.
- Cierra con una evaluación posterior: qué decisión cambió, qué indicador caducó y qué brecha de
  colección permanece.

## 🎓 Certificaciones

Security+, CySA+ o formación de análisis de inteligencia pueden aportar base, pero ninguna etiqueta
sustituye una estimación trazable.

## 📈 Progresión de carrera y salario

La progresión suele venir de SOC, DFIR, malware, fraude u OSINT y avanza hacia CTI
operacional/estratégica, liderazgo de inteligencia o detección. No se publica una cifra salarial sin
mercado, moneda y fecha; depende del país, sector, guardias y nivel de especialización.

## 🎤 Preguntas de entrevista

1. ¿Qué diferencia hay entre observable, indicador, inferencia y atribución?
2. ¿Cómo evitas que una IP compartida se convierta en una acusación?
3. ¿Qué PIR justifica recolectar un dato y cuándo dejas de hacerlo?
4. ¿Cómo expresas confianza y qué haría cambiar tu estimación?
5. ¿Qué entregas distinto a SOC, DFIR, infraestructura y CISO?
6. ¿Cómo mides si un informe produjo una decisión mejor?

## ⚠️ Mitos y errores comunes

- **«Más feeds equivalen a más inteligencia».** Sin requisito, procedencia y decisión sólo hay datos.
- **«ATT&CK atribuye actores».** Describe comportamientos y relaciones documentadas.
- **«Una marca criminal es una organización estable».** Proveedores, operadores y nombres cambian.
- **«OSINT significa permiso ilimitado».** Acceso público no elimina límites legales, contractuales o éticos.
- **«El informe termina al publicarse».** Debe medirse uso, caducidad y cambio de decisión.

## 🔗 Volver

- [Índice de rutas](README.md) · [Examen por rol](../docs/examen-final-por-rol.md) ·
  [Cybercrime-as-a-Service](../docs/cybercrime-as-a-service.md)
