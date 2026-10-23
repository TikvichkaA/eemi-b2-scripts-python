import random
import string

LETTRES = string.ascii_letters          # a-z et A-Z
CHIFFRES = string.digits                # 0-9
SPECIAUX = "!@#$%^&*()-_=+[]{};:,.?"


def generer_mot_de_passe(longueur, avec_chiffres=True, avec_speciaux=True):
    """Génère un mot de passe aléatoire.

    longueur       : nombre de caractères souhaité (entier > 0)
    avec_chiffres  : inclure des chiffres ?
    avec_speciaux  : inclure des caractères spéciaux ?
    """
    if longueur <= 0:
        raise ValueError("La longueur doit être supérieure à 0.")

    # Les groupes de caractères autorisés (les lettres sont toujours incluses)
    groupes = [LETTRES]
    if avec_chiffres:
        groupes.append(CHIFFRES)
    if avec_speciaux:
        groupes.append(SPECIAUX)

    # On garantit au moins un caractère de chaque groupe choisi, si la longueur le permet
    caracteres = []
    if longueur >= len(groupes):
        for groupe in groupes:
            caracteres.append(random.choice(groupe))

    # On complète avec des caractères pris dans tous les groupes autorisés
    tout = "".join(groupes)
    while len(caracteres) < longueur:
        caracteres.append(random.choice(tout))

    random.shuffle(caracteres)  # pour ne pas toujours avoir les chiffres/spéciaux au début
    return "".join(caracteres)


def demander_entier_positif(message):
    """Redemande tant que la saisie n'est pas un entier strictement positif."""
    while True:
        saisie = input(message).strip()
        try:
            valeur = int(saisie)
        except ValueError:
            print("Erreur : entre un nombre entier (exemple : 12).")
            continue
        if valeur <= 0:
            print("Erreur : la longueur doit être supérieure à 0.")
            continue
        return valeur


def demander_oui_non(message):
    """Retourne True pour oui, False pour non."""
    while True:
        reponse = input(message + " (o/n) : ").strip().lower()
        if reponse in ("o", "oui"):
            return True
        if reponse in ("n", "non"):
            return False
        print("Erreur : réponds par o ou n.")


def main():
    longueur = demander_entier_positif("Longueur du mot de passe : ")
    chiffres = demander_oui_non("Inclure des chiffres ?")
    speciaux = demander_oui_non("Inclure des caractères spéciaux ?")
    nombre = demander_entier_positif("Combien de mots de passe générer ? ")

    for i in range(1, nombre + 1):
        print(f"{i}. {generer_mot_de_passe(longueur, chiffres, speciaux)}")


if __name__ == "__main__":
    main()