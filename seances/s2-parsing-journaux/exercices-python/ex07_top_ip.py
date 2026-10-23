"""Exercice 7 · Top des IP qui attaquent                   Notions : fichier, import, sorted
Mode IA : PILOTER AVEC UN PROMPT STRUCTURÉ (charte), puis grille des 5 questions.

C'est un mini-TP2 : on assemble les exercices 4 et 6.
Écrivez top_ip(chemin, n) qui lit un fichier de log et renvoie les n IP qui ont le
plus d'échecs SSH, sous forme de liste de couples (ip, nombre), du plus grand au plus petit.
En cas d'égalité, les IP sont rangées dans l'ordre alphabétique.
Si le fichier n'existe pas, la fonction renvoie une liste vide (pas de plantage).

    top_ip("donnees/auth.log.extrait", 2)  →  [("203.0.113.45", ...), (..., ...)]

Vous POUVEZ (et devriez) réutiliser vos fonctions : les deux imports ci-dessous
fonctionnent dès que les exercices 4 et 6 sont réussis.

Indice pour trier : sorted(liste, key=lambda couple: (-couple[1], couple[0]))
"""

from pathlib import Path

from ex04_compter import compter
from ex06_ip_echec import ip_echec


def top_ip(chemin: str, n: int = 3) -> list:
    # À vous
    return []


# ---------------------------------------------------------------------------
# Vérification : lancez  python3 ex07_top_ip.py
# Ne modifiez pas ce qui suit.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from _verif import verifier, terminer
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    terminer(verifier(top_ip, [
        (("donnees/fichier_absent.log", 3), []),
        (("donnees/auth.log.extrait", 1), [('203.0.113.45', 22)]),
        (("donnees/auth.log.extrait", 3), [('203.0.113.45', 22), ('203.0.113.77', 5), ('198.51.100.23', 3)]),
    ]))
