# Parte 10 — Seguridad en la nube y contenedores

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏭️ Parte siguiente](../parte-11-devsecops-y-seguridad-del-sdlc/README.md)

**15 clases** · rango 221–235 · AWS, Azure, GCP, IAM, Docker, Kubernetes e IaC

**Fuentes de referencia de esta parte:**

- Liz Rice — *Container Security* (O'Reilly, 2020).
- Andrew Martin & Michael Hausenblas — *Hacking Kubernetes* (O'Reilly, 2021).
- Chris Farris, Rich Mogull et al. — *AWS Well-Architected Framework: Security Pillar* (documentación oficial de AWS).
- Microsoft — *Azure Security Benchmark* y *Microsoft Cloud Security Benchmark*.
- Google — *Google Cloud Security Foundations Guide*.
- CIS — *CIS Benchmarks* para AWS, Azure, GCP, Docker y Kubernetes.
- NIST — *SP 800-190 Application Container Security Guide* y *SP 800-204 Microservices*.

---

## 🎯 ¿De qué trata esta parte?

La seguridad cloud no consiste en trasladar controles del centro de datos a una consola. Los recursos se crean mediante API, las identidades pueden operar entre cuentas y servicios, y gran parte de la infraestructura es efímera o administrada por un proveedor. El alumno debe aprender a preguntar quién controla cada capa, qué identidad autoriza una acción, qué configuración expresa la intención y qué registro permite reconstruirla.

El modelo de responsabilidad compartida no es una frontera única ni una exención contractual automática: cambia por servicio, configuración y tarea. IAM tampoco reemplaza red, cifrado, aplicaciones o operación. Esta parte conecta esos controles y enseña a razonar sobre su composición en AWS, Azure y Google Cloud, antes de pasar a contenedores, Kubernetes, IaC, postura, serverless, secretos, detección y respuesta.

Sirve a arquitectos de seguridad cloud, ingenieros DevSecOps, pentesters que auditan infraestructura
moderna y equipos SRE que deben endurecer plataformas Kubernetes en producción. Toda la práctica usa
herramientas reales y de código abierto: **Prowler**, **ScoutSuite**, **kube-bench**, **Trivy**,
**Terraform**, **tfsec/Checkov** y las CLIs oficiales de cada nube.

## 🧩 Problemas que resuelve

- Configuraciones inseguras por defecto (buckets públicos, security groups abiertos, secretos en texto plano).
- Roles y políticas IAM con permisos excesivos y rutas de **escalada de privilegios**.
- Imágenes de contenedor con vulnerabilidades y secretos incrustados.
- Clústeres Kubernetes con API server, kubelet o etcd expuestos y RBAC laxo.
- Drift entre lo definido en código (Terraform) y lo desplegado realmente.
- Falta de visibilidad: sin CloudTrail/Activity Logs no hay detección ni forense.
- Gestión de secretos manual y no rotada que termina filtrada en repositorios o logs.

## 🎓 Resultados de aprendizaje

Al terminar la parte, el alumno podrá:

- Explicar el modelo de responsabilidad compartida por tipo de servicio (IaaS/PaaS/SaaS) y aplicarlo a decisiones de arquitectura.
- Diseñar y auditar políticas IAM con privilegio mínimo, y detectar rutas de escalada.
- Ejecutar auditorías automatizadas de postura con **Prowler** y **ScoutSuite** e interpretar sus hallazgos.
- Endurecer imágenes y hosts Docker según el **CIS Docker Benchmark** y escanearlas con **Trivy**.
- Describir la arquitectura de Kubernetes y endurecer un clúster usando **kube-bench** y NetworkPolicies.
- Reproducir y mitigar ataques cloud y a Kubernetes en laboratorios controlados.
- Escanear código Terraform con **tfsec/Checkov** e integrar controles en el pipeline.
- Diseñar estrategias de gestión de secretos, logging centralizado y respuesta a incidentes en la nube.

## 🧱 Prerrequisitos

- Parte 1–2 (fundamentos, redes y protocolos).
- Parte 4 (pentest y explotación) para las clases ofensivas cloud/Kubernetes.
- Parte 9 (forense y respuesta a incidentes) como base para la clase 235.
- Manejo de línea de comandos Linux, Docker básico y nociones de HTTP/APIs REST.

## 🗺️ Estructura temática

| Bloque | Clases | Foco |
|--------|--------|------|
| Fundamentos e identidad | 221–222 | Responsabilidad compartida, IAM |
| Seguridad por proveedor | 223–225 | AWS, Azure, GCP |
| Ofensiva cloud | 226 | Pentest en entornos cloud |
| Contenedores | 227 | Docker: aislamiento, imágenes, runtime |
| Kubernetes | 228–229 | Arquitectura, hardening y ataques |
| Automatización y postura | 230–231 | IaC/Terraform, CSPM |
| Cargas modernas | 232–233 | Serverless, gestión de secretos |
| Operación y defensa | 234–235 | Logging/detección, respuesta a incidentes |

## 📚 Recorrido explicado, clase por clase

**[Clase 221 — Fundamentos y responsabilidad compartida](221-fundamentos-de-seguridad-en-la-nube-y-responsabilidad-compartida/README.md).** Construye el vocabulario de servicio, región, zona, plano de control y plano de datos. Enseña a asignar cada tarea de seguridad al proveedor, cliente o responsabilidad compartida sin usar porcentajes publicitarios. La evidencia es una matriz razonada para una arquitectura IaaS, PaaS y SaaS.

**[Clase 222 — IAM en la nube](222-iam-en-la-nube-identidades-roles-y-permisos/README.md).** Convierte identidad en una decisión evaluable: principal, credencial, política, recurso, condición, sesión y límites superiores. Aparece antes de los proveedores porque toda consola y API necesita autorización. La evidencia es una política mínima acompañada por pruebas positivas y negativas.

**[Clase 223 — Seguridad en AWS](223-seguridad-en-aws/README.md).** Aplica los fundamentos a cuentas, VPC, S3, KMS, CloudTrail, Config, GuardDuty y Security Hub. No presenta servicios como botones mágicos: explica qué fuente usan y qué cobertura depende de configuración. La evidencia es una revisión de arquitectura con controles preventivos, detectivos y trazabilidad.

**[Clase 224 — Seguridad en Azure](224-seguridad-en-azure/README.md).** Relaciona tenant, management groups, suscripciones, Entra ID, Azure RBAC, Policy, NSG, Key Vault, Defender for Cloud y Sentinel. La secuencia obliga a distinguir identidad del directorio y autorización sobre recursos. La evidencia es una asignación por ámbito y una política con efecto probado.

**[Clase 225 — Seguridad en Google Cloud](225-seguridad-en-google-cloud-platform/README.md).** Explica organización, carpetas, proyectos, IAM, cuentas de servicio, Organization Policy, VPC Service Controls y Security Command Center. La evidencia es un diseño donde herencia, perímetro de datos y excepciones quedan documentados.

**[Clase 226 — Ataques y pentest cloud](226-ataques-y-pentest-en-entornos-cloud/README.md).** Usa un laboratorio autorizado para mostrar cómo una credencial limitada, metadatos, relaciones de confianza o permisos indirectos pueden producir rutas de ataque. Enseña reglas de compromiso y política del proveedor antes que herramientas. La evidencia es una cadena reproducible con impacto controlado y mitigación.

**[Clase 227 — Seguridad de contenedores Docker](227-seguridad-de-contenedores-docker/README.md).** Pasa de los servicios administrados al aislamiento de procesos: namespaces, cgroups, capabilities, daemon, imágenes, capas, secretos y perfiles de runtime. La evidencia es una imagen reconstruida y una ejecución con privilegios medidos.

**[Clase 228 — Arquitectura de seguridad Kubernetes](228-seguridad-de-kubernetes-arquitectura/README.md).** Presenta API server, etcd, kubelet, autenticación, autorización, admisión, ServiceAccounts, namespaces y red como una cadena de decisiones. La evidencia es el seguimiento de una petición desde identidad hasta persistencia y ejecución.

**[Clase 229 — Hardening y ataques Kubernetes](229-kubernetes-hardening-y-ataques/README.md).** Aplica Pod Security Admission, `securityContext`, RBAC, NetworkPolicy y benchmarks sin confundir cumplimiento con seguridad completa. La evidencia es un workload que falla bajo una política insegura y funciona con la excepción mínima explicada.

**[Clase 230 — Seguridad de Terraform e IaC](230-seguridad-de-infrastructure-as-code-terraform/README.md).** Conecta código, plan, state, proveedores, módulos, drift, escaneo y policy-as-code. La evidencia es un cambio revisado desde HCL hasta plan y estado, con secretos y dependencias tratados explícitamente.

**[Clase 231 — CSPM](231-cloud-security-posture-management-cspm/README.md).** Enseña a convertir miles de checks en decisiones basadas en exposición, privilegio, datos, explotabilidad y dueño. Se coloca después de IaC para corregir tanto el recurso como su fuente declarativa. La evidencia es una cola priorizada y métricas de cierre y recurrencia.

**[Clase 232 — Seguridad serverless](232-seguridad-serverless/README.md).** Analiza funciones, triggers, payloads, identidades, dependencias, concurrencia, costos y observabilidad. La evidencia es un flujo de evento validado con permisos acotados y límites operativos.

**[Clase 233 — Gestión de secretos](233-gestion-de-secretos-en-la-nube/README.md).** Distingue secreto, clave, token, certificado e identidad de carga, y explica almacenamiento, entrega, rotación, revocación y auditoría. La evidencia es un secreto entregado en runtime sin quedar en código, imagen o logs, más un procedimiento de compromiso.

**[Clase 234 — Logging y detección cloud](234-logging-y-deteccion-en-la-nube/README.md).** Diseña visibilidad por planos de gestión, datos, identidad, red y carga. Explica cobertura, latencia, costo, retención e integridad antes de crear una alerta. La evidencia es una matriz de fuentes y una detección probada con evento benigno controlado.

**[Clase 235 — Respuesta a incidentes cloud](235-respuesta-a-incidentes-en-la-nube/README.md).** Integra la Parte 9 con identidades, API, snapshots, logs, recursos efímeros e IaC. La evidencia final es una bitácora de decisiones, preservación reproducible, contención reversible y recuperación validada.

## 🧭 Método de trabajo de la parte

Cada clase usa el mismo razonamiento profesional: definir activo y frontera de responsabilidad, identificar identidad y plano, expresar estado esperado, comprobar estado efectivo, observar cambios y registrar excepciones. Los laboratorios se ejecutan solo en cuentas, suscripciones, proyectos o clústeres propios y con límites de costo. Una herramienta entrega observaciones; el alumno debe explicar alcance, falsos positivos, permisos usados y qué control corrige la causa.

## 🔗 Referencias de la parte y criterio de uso

- Liz Rice, *Container Security*, O'Reilly. <https://www.oreilly.com/library/view/container-security/9781492056690/>
- Martin & Hausenblas, *Hacking Kubernetes*, O'Reilly. <https://www.oreilly.com/library/view/hacking-kubernetes/9781492081722/>
- AWS Well-Architected — Security Pillar. <https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html> — principios oficiales de diseño AWS; no sustituye la documentación específica de cada servicio.
- Microsoft Cloud Security Benchmark. <https://learn.microsoft.com/security/benchmark/azure/> — baseline oficial multi-cloud de Microsoft; cada recomendación debe ajustarse al ámbito y servicio.
- Google Cloud Security Foundations. <https://cloud.google.com/architecture/security-foundations> — guía oficial de organización y controles fundacionales.
- CIS Benchmarks. <https://www.cisecurity.org/cis-benchmarks> — baselines verificables; una coincidencia no demuestra ausencia de otras rutas de riesgo.
- NIST SP 800-190. <https://doi.org/10.6028/NIST.SP.800-190> — riesgos y recomendaciones para contenedores; se complementa con documentación actual de Docker y Kubernetes.

## ▶️ Empezar

[Clase 221 — Fundamentos de seguridad en la nube y responsabilidad compartida](221-fundamentos-de-seguridad-en-la-nube-y-responsabilidad-compartida/README.md)
