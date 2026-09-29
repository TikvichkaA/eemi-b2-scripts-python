#!/usr/bin/env python3
"""nom_du_script.py : une phrase qui dit ce que fait le script.

Codes retour :
    0  OK
    1  anomalie détectée (le script a fonctionné, mais il signale un problème)
    2  erreur d'usage ou d'exécution (le script n'a pas pu faire son travail)

Auteur : Prénom Nom · Version : 0.1.0
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

__version__ = "0.1.0"

EXIT_OK = 0
EXIT_ANOMALIE = 1
EXIT_ERREUR = 2

log = logging.getLogger(Path(__file__).stem)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Définit et lit les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Ce que fait le script, en deux lignes au plus.",
    )
    parser.add_argument("entree", type=Path, help="fichier à traiter")
    parser.add_argument("-o", "--output", type=Path, help="fichier de sortie (défaut : stdout)")
    parser.add_argument("-v", "--verbose", action="store_true", help="messages de diagnostic")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser.parse_args(argv)


def traiter(chemin: Path) -> str:
    """Le cœur du métier : une fonction pure, facile à tester.

    Elle lève une exception en cas de problème : c'est main() qui décide
    du message et du code retour.
    """
    contenu = chemin.read_text(encoding="utf-8", errors="replace")
    return f"{chemin} : {len(contenu.splitlines())} lignes"


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.WARNING,
        format="%(asctime)s %(levelname)s %(name)s : %(message)s",
        stream=sys.stderr,          # les logs sur stderr, le résultat sur stdout
    )
    log.debug("arguments : %s", args)

    try:
        resultat = traiter(args.entree)
    except FileNotFoundError:
        log.error("fichier introuvable : %s", args.entree)
        return EXIT_ERREUR
    except PermissionError:
        log.error("permission refusée : %s (lancer avec sudo ?)", args.entree)
        return EXIT_ERREUR

    if args.output:
        args.output.write_text(resultat + "\n", encoding="utf-8")
    else:
        print(resultat)
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
