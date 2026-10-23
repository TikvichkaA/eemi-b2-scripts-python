"""Exercice 2 · Lire une ligne « clé=valeur »               Notions : chaînes, partition, strip, tuple
Mode IA : SEUL D'ABORD, puis l'IA explique vos erreurs.

Le fichier /etc/os-release contient des lignes comme :
    PRETTY_NAME="Ubuntu 24.04.1 LTS"
    ID=ubuntu

Écrivez lire_valeur(ligne) qui renvoie le couple (clé, valeur), sans les guillemets
autour de la valeur.

    lire_valeur('PRETTY_NAME="Ubuntu 24.04.1 LTS"')  →  ("PRETTY_NAME", "Ubuntu 24.04.1 LTS")
    lire_valeur('ID=ubuntu')                          →  ("ID", "ubuntu")

Attention : la valeur elle-même peut contenir un « = » (dernier test).
Pour renvoyer un couple : return cle, valeur
"""


def lire_valeur(ligne: str) -> tuple:
    # À vous
    return ("", "")


# ---------------------------------------------------------------------------
# Vérification : lancez  python3 ex02_cle_valeur.py
# Ne modifiez pas ce qui suit.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from _verif import verifier, terminer
    terminer(verifier(lire_valeur, [
        (('ID=ubuntu',), ("ID", "ubuntu")),
        (('PRETTY_NAME="Ubuntu 24.04.1 LTS"',), ("PRETTY_NAME", "Ubuntu 24.04.1 LTS")),
        (('VERSION_ID="24.04"\n',), ("VERSION_ID", "24.04")),
        (('HOME_URL="https://www.ubuntu.com/?a=1"',), ("HOME_URL", "https://www.ubuntu.com/?a=1")),
    ]))
