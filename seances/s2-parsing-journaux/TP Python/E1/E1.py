"""Exercice 1 : calculateur d'IMC (variables, conditions, input())."""


def demander_nombre(message):
    """Redemande une valeur tant que ce n'est pas un nombre strictement positif."""
    while True:
        saisie = input(message).strip().replace(",", ".")  # accepte 1,80 comme 1.80
        try:
            valeur = float(saisie)
        except ValueError:
            print("Erreur : entre un nombre (exemple : 75 ou 1.80).")
            continue
        if valeur <= 0:
            print("Erreur : la valeur doit être supérieure à 0.")
            continue
        return valeur


def categorie(imc):
    """Retourne la catégorie correspondant à l'IMC."""
    if imc < 18.5:
        return "sous-poids"
    elif imc < 25:
        return "poids normal"
    elif imc < 30:
        return "surpoids"
    else:
        return "obèse"


poids = demander_nombre("Poids en kg : ")
taille = demander_nombre("Taille en mètres : ")

imc = poids / (taille ** 2)
print(f"Ton IMC est de {imc:.1f} : {categorie(imc)}.")
