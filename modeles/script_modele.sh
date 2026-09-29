#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# nom_du_script.sh : une phrase qui dit ce que fait le script.
#
# Usage   : nom_du_script.sh [-o FICHIER] [-v] ARGUMENT
# Retour  : 0 = OK · 1 = anomalie détectée · 2 = erreur d'usage ou d'exécution
# Auteur  : Prénom Nom · Version : 0.1.0
# ---------------------------------------------------------------------------
set -euo pipefail          # arrêt sur erreur, variable non définie, échec dans un pipe
IFS=$'\n\t'                # découpage des mots plus sûr

SCRIPT_NAME="$(basename "$0")"
readonly SCRIPT_NAME
VERBOSE=0
OUTPUT=""

usage() {
    cat <<EOF
Usage : ${SCRIPT_NAME} [-o FICHIER] [-v] ARGUMENT

Ce que fait le script, en deux lignes au plus.

Options :
  -o FICHIER   écrire le résultat dans FICHIER (par défaut : sortie standard)
  -v           mode verbeux (messages de diagnostic sur stderr)
  -h           afficher cette aide
EOF
}

log()  { [[ "$VERBOSE" -eq 1 ]] && echo "[INFO] $*" >&2 || true; }
err()  { echo "[ERREUR] $*" >&2; }
die()  { err "$*"; exit 2; }

# Nettoyage garanti, même en cas d'erreur ou de Ctrl-C
TMPDIR_WORK="$(mktemp -d)"
cleanup() { rm -rf -- "$TMPDIR_WORK"; }
trap cleanup EXIT

# Vérifier qu'une commande existe avant de s'en servir
require() { command -v "$1" >/dev/null 2>&1 || die "commande requise introuvable : $1"; }

main() {
    while getopts ":o:vh" opt; do
        case "$opt" in
            o) OUTPUT="$OPTARG" ;;
            v) VERBOSE=1 ;;
            h) usage; exit 0 ;;
            :) die "l'option -$OPTARG attend une valeur" ;;
            *) usage >&2; exit 2 ;;
        esac
    done
    shift $((OPTIND - 1))
    [[ $# -eq 1 ]] || { usage >&2; exit 2; }
    local argument="$1"

    log "démarrage avec argument=${argument}"

    # --- Le travail du script commence ici -------------------------------
    local resultat="traitement de ${argument}"
    # ---------------------------------------------------------------------

    if [[ -n "$OUTPUT" ]]; then
        printf '%s\n' "$resultat" > "$OUTPUT"
    else
        printf '%s\n' "$resultat"
    fi
}

main "$@"
