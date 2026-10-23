"""Exercice 2 : analyseur de texte (strings, split(), boucles)."""

import string


def nettoyer_mots(texte):
    """Découpe le texte en mots, en minuscules et sans ponctuation autour."""
    mots = []
    for mot in texte.lower().split():
        mot = mot.strip(string.punctuation + "«»…“”")  # retire . , ! ? ; : " etc.
        if mot:  # ignore ce qui n'était que de la ponctuation (ex : "-")
            mots.append(mot)
    return mots


def compter_caracteres(texte):
    """Nombre de caractères sans compter les espaces (ni tabulations, ni retours)."""
    total = 0
    for caractere in texte:
        if not caractere.isspace():
            total += 1
    return total


def mot_le_plus_frequent(mots):
    """Retourne (mot, nombre d'apparitions). En cas d'égalité : le premier apparu."""
    compteur = {}
    for mot in mots:
        compteur[mot] = compteur.get(mot, 0) + 1

    meilleur_mot, meilleur_score = None, 0
    for mot, score in compteur.items():  # le dictionnaire garde l'ordre d'apparition
        if score > meilleur_score:
            meilleur_mot, meilleur_score = mot, score
    return meilleur_mot, meilleur_score


texte = input("Saisis un texte : ")
mots = nettoyer_mots(texte)

if not mots:
    print("Le texte est vide : il n'y a rien à analyser.")
else:
    mot, fois = mot_le_plus_frequent(mots)
    print(f"Nombre de mots : {len(mots)}")
    print(f"Nombre de caractères (sans les espaces) : {compter_caracteres(texte)}")
    print(f"Mot le plus fréquent : « {mot} » ({fois} fois)")
