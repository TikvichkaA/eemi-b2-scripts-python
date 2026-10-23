"""Exercice 8 (bonus) · Valider un seuil                    Notions : try/except, raise
Mode IA : DÉBOGUER. Lisez le code fourni, lancez-le, puis demandez à l'IA d'expliquer
POURQUOI certains tests échouent, avant de corriger vous-même.

lire_seuil(texte) convertit un texte saisi par l'utilisateur en entier entre 0 et 100.
Si le texte n'est pas un entier, ou s'il est hors de 0..100, la fonction doit lever
ValueError avec un message clair.

    lire_seuil("80")    →  80
    lire_seuil(" 75 ")  →  75
    lire_seuil("abc")   →  ValueError
    lire_seuil("150")   →  ValueError

Le code ci-dessous a été écrit trop vite : il contient DEUX erreurs.
"""


def lire_seuil(texte: str) -> int:
    try:
        valeur = int(texte)
    except ValueError:
        print("seuil invalide")
        return 80
    if valeur < 0 or valeur > 100:
        raise ValueError(f"seuil hors limites : {valeur}")
    return str(valeur)


# ---------------------------------------------------------------------------
# Vérification : lancez  python3 ex08_seuil.py
# Ne modifiez pas ce qui suit.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from _verif import verifier, terminer
    terminer(verifier(lire_seuil, [
        (("80",), 80),
        ((" 75 ",), 75),
        (("0",), 0),
        (("100",), 100),
        (("abc",), ValueError),
        (("150",), ValueError),
        (("-1",), ValueError),
    ]))
