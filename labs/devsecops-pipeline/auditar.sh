#!/usr/bin/env bash
# Orquestador de las capas de auditoría del pipeline de despliegue.
#
# Uso:
#   ./auditar.sh                 # todas las capas disponibles
#   ./auditar.sh sast secrets    # solo las capas indicadas
#
# Capas: deps · sast · secrets · dockerfile · container · workflows ·
#        typosquat · priorizar
#
# Principio de diseño (el mismo que debe tener tu informe): una capa que no se
# pudo ejecutar NO es una capa limpia. El resumen final distingue siempre tres
# estados —ejecutada, sin hallazgos, no disponible— y nunca los mezcla.

set -uo pipefail

REPO="${REPO:-/audit/repo}"
SALIDA="${SALIDA:-/audit/salida}"
AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CAPAS_DISPONIBLES=(deps sast secrets dockerfile container workflows typosquat priorizar)

mkdir -p "$SALIDA"

if [ "$#" -gt 0 ]; then
    CAPAS=("$@")
else
    CAPAS=("${CAPAS_DISPONIBLES[@]}")
fi

declare -A ESTADO

titulo() {
    echo ""
    echo "=============================================================="
    echo "  $1"
    echo "=============================================================="
}

# Marca el estado de una capa según el binario disponible y el código de salida.
# Convención de los escáneres: 0 = sin hallazgos, !=0 = hallazgos (o error).
registrar() {
    local capa="$1" rc="$2"
    if [ "$rc" -eq 0 ]; then
        ESTADO[$capa]="sin hallazgos"
    else
        ESTADO[$capa]="HALLAZGOS"
    fi
}

no_disponible() {
    local capa="$1" herramienta="$2"
    ESTADO[$capa]="NO EJECUTADA (falta $herramienta)"
    echo "  [!] $herramienta no está disponible en la imagen."
    echo "      Esta capa queda FUERA de la cobertura del informe."
}

capa_deps() {
    titulo "CAPA 1/8 — Composición: dependencias de terceros"
    if command -v osv-scanner >/dev/null 2>&1; then
        osv-scanner --lockfile="requirements.txt:$REPO/requirements.txt" \
            | tee "$SALIDA/01-deps-osv.txt"
        registrar deps "${PIPESTATUS[0]}"
    elif command -v pip-audit >/dev/null 2>&1; then
        pip-audit -r "$REPO/requirements.txt" --desc \
            | tee "$SALIDA/01-deps-pip-audit.txt"
        registrar deps "${PIPESTATUS[0]}"
    else
        no_disponible deps "osv-scanner / pip-audit"
    fi
}

capa_sast() {
    titulo "CAPA 2/8 — SAST: tu propio código"
    if command -v bandit >/dev/null 2>&1; then
        bandit -r "$REPO" -f txt | tee "$SALIDA/02-sast-bandit.txt"
        registrar sast "${PIPESTATUS[0]}"
    else
        no_disponible sast "bandit"
    fi
    if command -v semgrep >/dev/null 2>&1; then
        echo "--- semgrep (segunda opinión, reglas de la comunidad) ---"
        semgrep --config auto --error "$REPO" 2>/dev/null \
            | tee "$SALIDA/02-sast-semgrep.txt"
    fi
}

capa_secrets() {
    titulo "CAPA 3/8 — Secretos en el código"
    if command -v gitleaks >/dev/null 2>&1; then
        gitleaks detect --no-git --redact -v --source "$REPO" \
            --report-path "$SALIDA/03-secretos.json" | tee "$SALIDA/03-secretos.txt"
        registrar secrets "${PIPESTATUS[0]}"
    else
        no_disponible secrets "gitleaks"
    fi
}

capa_dockerfile() {
    titulo "CAPA 4/8 — Dockerfile: antipatrones de construcción"
    if command -v hadolint >/dev/null 2>&1; then
        hadolint "$REPO/Dockerfile" | tee "$SALIDA/04-dockerfile.txt"
        registrar dockerfile "${PIPESTATUS[0]}"
    else
        no_disponible dockerfile "hadolint"
    fi
}

capa_container() {
    titulo "CAPA 5/8 — Contenedor: sistema operativo base"
    if command -v trivy >/dev/null 2>&1; then
        trivy fs --scanners vuln,secret,misconfig "$REPO" \
            | tee "$SALIDA/05-contenedor.txt"
        registrar container "${PIPESTATUS[0]}"
    else
        no_disponible container "trivy"
    fi
}

capa_workflows() {
    titulo "CAPA 6/8 — Workflows de CI/CD"
    local wf="$REPO/.github/workflows"
    if command -v zizmor >/dev/null 2>&1; then
        zizmor "$wf" | tee "$SALIDA/06-workflows-zizmor.txt"
        registrar workflows "${PIPESTATUS[0]}"
    elif command -v actionlint >/dev/null 2>&1; then
        echo "  [i] zizmor no está instalado; se usa actionlint."
        echo "      actionlint valida sintaxis y detecta inyección de expresiones,"
        echo "      pero NO cubre permisos excesivos ni acciones sin fijar por SHA."
        actionlint "$wf"/*.yml | tee "$SALIDA/06-workflows-actionlint.txt"
        registrar workflows "${PIPESTATUS[0]}"
        ESTADO[workflows]="${ESTADO[workflows]} (cobertura parcial: sin zizmor)"
    else
        no_disponible workflows "zizmor / actionlint"
    fi
}

capa_typosquat() {
    titulo "CAPA 7/8 — Cadena de suministro: nombres suplantados"
    if command -v python3 >/dev/null 2>&1 && [ -f "$AQUI/typosquat.py" ]; then
        python3 "$AQUI/typosquat.py" "$REPO/requirements.txt" \
            | tee "$SALIDA/07-typosquat.txt"
        registrar typosquat "${PIPESTATUS[0]}"
        # Esta capa nunca "aprueba" nada: solo propone candidatos a revisión.
        ESTADO[typosquat]="revisado (heurística: requiere criterio humano)"
    else
        no_disponible typosquat "python3 / typosquat.py"
    fi
}

capa_priorizar() {
    titulo "CAPA 8/8 — Inteligencia y priorización (KEV · EPSS · CVSS)"
    if command -v python3 >/dev/null 2>&1 && [ -f "$AQUI/priorizar.py" ]; then
        echo "  [i] Se usan los hallazgos de ejemplo. Para priorizar los tuyos,"
        echo "      conviértelos al formato de hallazgos-ejemplo.json y pásalos"
        echo "      con --hallazgos."
        if python3 "$AQUI/priorizar.py" --salida "$SALIDA/08-plan-priorizado.md"; then
            cat "$SALIDA/08-plan-priorizado.md"
            # Esta capa no BUSCA hallazgos: los ordena. Decir "sin hallazgos"
            # aqui seria enganoso, asi que se reporta lo que realmente hizo.
            ESTADO[priorizar]="plan generado (revisa la cobertura de las señales)"
        else
            ESTADO[priorizar]="FALLO al generar el plan"
        fi
    else
        no_disponible priorizar "python3 / priorizar.py"
    fi
}

for capa in "${CAPAS[@]}"; do
    case "$capa" in
        deps)       capa_deps ;;
        sast)       capa_sast ;;
        secrets)    capa_secrets ;;
        dockerfile) capa_dockerfile ;;
        container)  capa_container ;;
        workflows)  capa_workflows ;;
        typosquat)  capa_typosquat ;;
        priorizar)  capa_priorizar ;;
        *) echo "Capa desconocida: $capa (válidas: ${CAPAS_DISPONIBLES[*]})" ;;
    esac
done

titulo "RESUMEN DE COBERTURA"
echo ""
printf "  %-12s %s\n" "CAPA" "ESTADO"
printf "  %-12s %s\n" "----" "------"
for capa in "${CAPAS[@]}"; do
    printf "  %-12s %s\n" "$capa" "${ESTADO[$capa]:-no ejecutada}"
done
echo ""
echo "  Informes en: $SALIDA"
echo ""
echo "  RECUERDA: 'sin hallazgos' y 'NO EJECUTADA' no son lo mismo. Al redactar"
echo "  el informe, las capas no ejecutadas se declaran como fuera de alcance."
echo ""
