#!/usr/bin/env bash
# verifier_env.sh : vérifie que votre environnement est prêt pour le module.
set -uo pipefail

manque=0
verifier() {   # verifier COMMANDE CONSEIL [optionnel]
    if command -v "$1" >/dev/null 2>&1; then
        printf '  [OK] %-10s %s\n' "$1" "$("$1" --version 2>&1 | head -n1)"
    elif [[ "${3:-}" == "optionnel" ]]; then
        printf '  [--] %-10s absent (conseillé) : %s\n' "$1" "$2"
    else
        printf '  [KO] %-10s absent : %s\n' "$1" "$2"
        manque=1
    fi
}

echo "Système : $(uname -s) $(uname -r)"
[[ "$(uname -s)" == "Linux" ]] || { echo "  [KO] il faut un Linux (WSL 2, VM ou conteneur) : voir le README"; manque=1; }

verifier bash       "normalement toujours présent"
verifier python3    "sudo apt install python3 python3-venv"
verifier git        "sudo apt install git"
verifier ss         "sudo apt install iproute2"
verifier shellcheck "sudo apt install shellcheck" optionnel

if command -v python3 >/dev/null; then
    if python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)'; then
        echo "  [OK] Python >= 3.10"
    else
        echo "  [KO] Python 3.10 ou plus requis"; manque=1
    fi
fi

if [[ $manque -eq 0 ]]; then echo "Environnement prêt."; else echo "Complétez les éléments [KO] avant la séance."; fi
exit "$manque"
