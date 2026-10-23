import json
import os

# Le fichier de sauvegarde est rangé à côté du script, quel que soit le dossier d'où on le lance
FICHIER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "taches.json")

MENU = """
=== Gestionnaire de tâches ===
1. Ajouter une tâche
2. Lister les tâches
3. Marquer une tâche comme faite
4. Quitter"""


def charger(fichier=FICHIER):
    """Lit les tâches dans le fichier. Retourne une liste vide s'il n'existe pas ou s'il est abîmé."""
    if not os.path.exists(fichier):
        return []
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            taches = json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Attention : le fichier de tâches est illisible, on repart d'une liste vide.")
        return []
    # On ne garde que les éléments au bon format
    return [t for t in taches if isinstance(t, dict) and "titre" in t and "fait" in t]


def sauvegarder(taches, fichier=FICHIER):
    """Écrit la liste dans le fichier (appelé après chaque modification)."""
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(taches, f, ensure_ascii=False, indent=2)


def ajouter(taches):
    titre = input("Titre de la tâche : ").strip()
    if not titre:
        print("Erreur : le titre ne peut pas être vide.")
        return
    taches.append({"titre": titre, "fait": False})
    sauvegarder(taches)
    print(f"Tâche ajoutée : « {titre} ».")


def lister(taches):
    if not taches:
        print("Aucune tâche pour le moment.")
        return
    for numero, tache in enumerate(taches, start=1):
        statut = "[x] fait" if tache["fait"] else "[ ] à faire"
        print(f"{numero}. {statut} - {tache['titre']}")


def marquer_faite(taches):
    if not taches:
        print("Aucune tâche à marquer : la liste est vide.")
        return
    lister(taches)
    saisie = input("Numéro de la tâche terminée : ").strip()
    try:
        numero = int(saisie)
    except ValueError:
        print("Erreur : entre le numéro de la tâche (un nombre entier).")
        return
    if numero < 1 or numero > len(taches):
        print(f"Erreur : il n'y a pas de tâche numéro {numero} (choisis entre 1 et {len(taches)}).")
        return
    tache = taches[numero - 1]
    if tache["fait"]:
        print(f"La tâche « {tache['titre']} » est déjà faite.")
        return
    tache["fait"] = True
    sauvegarder(taches)
    print(f"Bravo ! « {tache['titre']} » est terminée.")


def main():
    taches = charger()
    while True:
        print(MENU)
        choix = input("Ton choix (1-4) : ").strip()
        if choix == "1":
            ajouter(taches)
        elif choix == "2":
            lister(taches)
        elif choix == "3":
            marquer_faite(taches)
        elif choix == "4":
            print("À bientôt !")
            break
        else:
            print("Option invalide : entre 1, 2, 3 ou 4.")


if __name__ == "__main__":
    main()