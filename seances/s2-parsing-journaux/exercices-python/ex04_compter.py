"""Exercice 4 · Compter des occurrences                   Notions : dictionnaire, get, boucle
Mode IA : L'IA ÉCRIT, VOUS EXPLIQUEZ.

Écrivez compter(elements) qui renvoie un dictionnaire {élément: nombre d'apparitions}.
N'utilisez PAS collections.Counter : le but est de comprendre le mécanisme.

    compter(["a", "b", "a"])  →  {"a": 2, "b": 1}
    compter([])               →  {}

Consigne IA : faites écrire la fonction par l'IA, puis ajoutez AU-DESSUS DE CHAQUE LIGNE
un commentaire # qui explique, avec vos mots, ce qu'elle fait. Pas de commentaire = pas fait.
"""


def compter(elements: list) -> dict:
    # À vous
    return {}


# ---------------------------------------------------------------------------
# Vérification : lancez  python3 ex04_compter.py
# Ne modifiez pas ce qui suit.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from _verif import verifier, terminer
    terminer(verifier(compter, [
        (([],), {}),
        ((["a"],), {"a": 1}),
        ((["a", "b", "a"],), {"a": 2, "b": 1}),
        ((["203.0.113.45", "10.0.0.12", "203.0.113.45", "203.0.113.45"],), {"203.0.113.45": 3, "10.0.0.12": 1}),
    ]))
