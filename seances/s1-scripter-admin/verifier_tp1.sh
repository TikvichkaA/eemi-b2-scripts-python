#!/usr/bin/env bash
# verifier_tp1.sh : vérifications automatiques du TP1.
# Usage : bash verifier_tp1.sh      (depuis le dossier seances/s1-scripter-admin)
# Ce script ne note rien : il vous dit ce qui manque encore.
# shellcheck disable=SC2016,SC2034  # les tests sont volontairement évalués plus tard par eval
set -uo pipefail
cd "$(dirname "$0")" || exit 2

OK=0; KO=0
ok() { printf '  \033[32m[OK]\033[0m %s\n' "$1"; OK=$((OK+1)); }
ko() { printf '  \033[31m[KO]\033[0m %s\n' "$1"; KO=$((KO+1)); }
check() { if eval "$2" >/dev/null 2>&1; then ok "$1"; else ko "$1"; fi; }

echo "Partie A · inventaire.sh"
check "le script est exécutable (chmod +x)"               '[[ -x inventaire.sh ]]'
check "-h affiche une aide qui mentionne -s et -o"         'out=$(./inventaire.sh -h); grep -q -- "-s" <<<"$out" && grep -q -- "-o" <<<"$out"'
check "-h renvoie le code 0"                               './inventaire.sh -h'
check "une option inconnue renvoie le code 2"              './inventaire.sh -z; [[ $? -eq 2 ]]'
check "un seuil invalide (abc) renvoie le code 2"          './inventaire.sh -s abc; [[ $? -eq 2 ]]'
check "un seuil de 150 renvoie le code 2"                  './inventaire.sh -s 150; [[ $? -eq 2 ]]'
check "la section Hôte affiche le noyau"                   'out=$(./inventaire.sh -s 100); grep -qF "$(uname -r)" <<<"$out"'
check "la section Disques affiche /"                       'out=$(./inventaire.sh -s 100); grep -Eq "^/ +[0-9]+ %" <<<"$out"'
check "seuil 0 : ALERTE affichée et code retour 1"         'out=$(./inventaire.sh -s 0); r=$?; grep -q ALERTE <<<"$out" && [[ $r -eq 1 ]]'
check "-o écrit dans un fichier"                           'f=$(mktemp); ./inventaire.sh -s 100 -o "$f"; grep -q "Hôte" "$f"; r=$?; rm -f "$f"; [[ $r -eq 0 ]]'
if command -v shellcheck >/dev/null; then
    check "shellcheck ne signale rien"                     'shellcheck inventaire.sh'
else
    echo "  [--] shellcheck non installé (sudo apt install shellcheck) : vérification ignorée"
fi

echo "Partie B · inventaire.py"
PY="python3 inventaire.py"
check "--help mentionne --seuil, --format et --output"     'out=$($PY --help); grep -q -- --seuil <<<"$out" && grep -q -- --format <<<"$out" && grep -q -- --output <<<"$out"'
check "un seuil de 150 renvoie le code 2"                  '$PY --seuil 150; [[ $? -eq 2 ]]'
check "--format json produit du JSON valide"               '$PY --seuil 100 --format json | python3 -m json.tool'
check "le JSON contient toutes les clés attendues"         '$PY --seuil 100 --format json | python3 -c "import json,sys; d=json.load(sys.stdin); assert {\"date\",\"hote\",\"cpu\",\"memoire\",\"disques\",\"comptes\",\"ports_tcp\",\"alerte\"} <= d.keys()"'
check "hote.noyau correspond à uname -r"                   '$PY --seuil 100 --format json | python3 -c "import json,sys,platform; assert json.load(sys.stdin)[\"hote\"][\"noyau\"] == platform.release()"'
check "memoire.total_mio est un entier > 0"                '$PY --seuil 100 --format json | python3 -c "import json,sys; m=json.load(sys.stdin)[\"memoire\"][\"total_mio\"]; assert isinstance(m,int) and m>0"'
check "disques contient / avec utilise_pct entre 0 et 100" '$PY --seuil 100 --format json | python3 -c "import json,sys; d=[x for x in json.load(sys.stdin)[\"disques\"] if x[\"point_montage\"]==\"/\"]; assert d and 0<=d[0][\"utilise_pct\"]<=100"'
check "seuil 0 : alerte=true et code retour 1"             '$PY --seuil 0 --format json | python3 -c "import json,sys; assert json.load(sys.stdin)[\"alerte\"] is True"; $PY --seuil 0 >/dev/null; [[ $? -eq 1 ]]'
check "même % d'occupation de / que df (écart <= 1)"       'a=$($PY --seuil 100 --format json | python3 -c "import json,sys; print([x for x in json.load(sys.stdin)[\"disques\"] if x[\"point_montage\"]==\"/\"][0][\"utilise_pct\"])"); b=$(df -P / | awk "NR==2{gsub(\"%\",\"\",\$5); print \$5}"); (( a-b <= 1 && b-a <= 1 ))'
check "une sortie vers un dossier inexistant renvoie 2"    '$PY --seuil 100 -o /dossier/inexistant/x.json; [[ $? -eq 2 ]]'

echo
echo "Résultat : ${OK} OK, ${KO} KO"
[[ $KO -eq 0 ]]
