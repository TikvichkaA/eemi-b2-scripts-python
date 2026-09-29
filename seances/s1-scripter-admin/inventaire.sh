#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# inventaire.sh : inventaire rapide d'un serveur Linux (TP1, partie A)
#
# Usage   : inventaire.sh [-s SEUIL] [-o FICHIER] [-h]
# Retour  : 0 = OK · 1 = au moins un système de fichiers au-dessus du seuil
#           2 = erreur d'usage
# Auteur  : <votre nom>
# ---------------------------------------------------------------------------
set -euo pipefail
IFS=$'\n\t'

SCRIPT_NAME="$(basename "$0")"
readonly SCRIPT_NAME
SEUIL=80
OUTPUT=""
ALERTE=0

usage() {
    # TODO A1 : compléter l'aide (options -s, -o, -h et codes retour)
    echo "Usage : ${SCRIPT_NAME} [-s SEUIL] [-o FICHIER] [-h]"
}

die() { echo "[ERREUR] $*" >&2; exit 2; }
titre() { printf '\n== %s ==\n' "$1"; }

section_hote() {
    titre "Hôte"
    # TODO A2 : afficher le nom d'hôte, le système (PRETTY_NAME de /etc/os-release),
    #           la version du noyau et l'uptime au format « Xj Yh Zmin ».
    # Indices : hostname, uname -r, /proc/uptime (en secondes), $(( ... ))
    :
}

section_cpu_memoire() {
    titre "CPU et mémoire"
    # TODO A3 : nombre de cœurs, charge moyenne 1/5/15 min, mémoire disponible
    #           et totale en Mio.
    # Indices : nproc, /proc/loadavg, awk sur /proc/meminfo (valeurs en kio)
    :
}

section_disques() {
    titre "Disques (seuil ${SEUIL} %)"
    # TODO A4 : pour chaque système de fichiers réel, afficher le point de montage
    #           et le % d'occupation ; ajouter « ALERTE » et passer ALERTE=1
    #           si le % est supérieur ou égal au seuil.
    # Indices : df -P -x tmpfs -x devtmpfs, tail -n +2, while read, awk
    # Piège   : un « cmd | while read » s'exécute dans un sous-shell, donc ALERTE y est perdue.
    #           Utilisez plutôt : while read ...; do ...; done < <(cmd)
    :
}

section_comptes() {
    titre "Comptes interactifs (UID >= 1000)"
    # TODO A5 : lister les comptes dont l'UID est >= 1000 (sauf 65534, nobody)
    #           et dont le shell ne finit ni par nologin ni par false.
    # Indice  : awk -F: sur /etc/passwd (champ 3 = UID, champ 7 = shell)
    :
}

section_ports() {
    titre "Ports TCP en écoute"
    # TODO A6 : lister les adresses:ports TCP en écoute, sans doublon.
    #           Si la commande ss n'existe pas, afficher « non disponible » SANS planter.
    # Indices : command -v, ss -Htln, awk, sort -u
    :
}

main() {
    while getopts ":s:o:h" opt; do
        case "$opt" in
            s) SEUIL="$OPTARG" ;;
            o) OUTPUT="$OPTARG" ;;
            h) usage; exit 0 ;;
            :) die "l'option -$OPTARG attend une valeur" ;;
            *) usage >&2; exit 2 ;;
        esac
    done
    # TODO A7 : refuser un seuil qui n'est pas un entier entre 0 et 100 (code retour 2)

    {
        echo "Inventaire du $(date '+%Y-%m-%d %H:%M:%S')"
        section_hote
        section_cpu_memoire
        section_disques
        section_comptes
        section_ports
    } > "${OUTPUT:-/dev/stdout}"

    exit "$ALERTE"
}

main "$@"
