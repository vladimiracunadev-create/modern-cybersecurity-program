# Toolbox de auditoría del pipeline de despliegue (Parte 11 — DevSecOps).
#
# Todas las herramientas son de SOLO LECTURA: analizan archivos y consultan
# bases de datos públicas de vulnerabilidades. Ninguna modifica tu repositorio.
#
# Nota deliberada: este Dockerfile está escrito siguiendo las buenas prácticas
# que el laboratorio te enseña a exigir (base con versión fija, sin apt-get
# upgrade, limpieza de listas, usuario sin privilegios, CMD en forma exec).
# Compáralo con `repo-vulnerable/Dockerfile`, que hace justo lo contrario.
FROM python:3.12-slim

ARG TRIVY_VERSION=0.58.1
ARG GITLEAKS_VERSION=8.21.2
ARG HADOLINT_VERSION=2.12.0
ARG ACTIONLINT_VERSION=1.7.7
ARG OSV_SCANNER_VERSION=1.9.2

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl git ca-certificates jq \
    && rm -rf /var/lib/apt/lists/*

# Capas en Python: SAST propio (bandit, semgrep) y composición (pip-audit).
RUN pip install --no-cache-dir \
        bandit==1.9.4 \
        semgrep \
        pip-audit

# Binarios. Se instalan con "|| true" a propósito: si una descarga falla (red,
# proxy corporativo, release movida), la imagen se construye igual y el script
# `auditar.sh` te dirá qué capa NO pudo ejecutarse. Un informe de auditoría que
# no distingue "limpio" de "no escaneado" es un informe que miente.
RUN curl -sSfL "https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_Linux-64bit.tar.gz" \
      | tar -xz -C /usr/local/bin trivy || true

RUN curl -sSfL "https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}/gitleaks_${GITLEAKS_VERSION}_linux_x64.tar.gz" \
      | tar -xz -C /usr/local/bin gitleaks || true

RUN curl -sSfL -o /usr/local/bin/hadolint \
      "https://github.com/hadolint/hadolint/releases/download/v${HADOLINT_VERSION}/hadolint-Linux-x86_64" \
    && chmod +x /usr/local/bin/hadolint || true

RUN curl -sSfL "https://github.com/rhysd/actionlint/releases/download/v${ACTIONLINT_VERSION}/actionlint_${ACTIONLINT_VERSION}_linux_amd64.tar.gz" \
      | tar -xz -C /usr/local/bin actionlint || true

RUN curl -sSfL -o /usr/local/bin/osv-scanner \
      "https://github.com/google/osv-scanner/releases/download/v${OSV_SCANNER_VERSION}/osv-scanner_${OSV_SCANNER_VERSION}_linux_amd64" \
    && chmod +x /usr/local/bin/osv-scanner || true

# Usuario sin privilegios: el toolbox no necesita root para leer archivos.
RUN useradd --create-home --shell /bin/bash auditor
WORKDIR /audit
USER auditor

CMD ["sleep", "infinity"]
