"""Exercice 1 · Formater une durée                       Notions : int, //, %, f-string
Mode IA : SEUL D'ABORD (voir le guide), puis l'IA explique vos erreurs.

/proc/uptime donne le temps écoulé depuis le démarrage, en secondes.
Écrivez formater_uptime(secondes) qui renvoie une chaîne « Xj Yh Zmin ».
Les secondes restantes sont ignorées.

    formater_uptime(90061)    →  "1j 1h 1min"
    formater_uptime(1049000)  →  "12j 3h 23min"

Rappels : 1 jour = 86400 s, 1 heure = 3600 s.
  17 // 5 → 3   (division entière)
  17 %  5 → 2   (reste)
"""


def formater_uptime(secondes: int) -> str:
    # À vous : calculez jours, heures et minutes, puis renvoyez la chaîne.
    return ""


# ---------------------------------------------------------------------------
# Vérification : lancez  python3 ex01_uptime.py
# Ne modifiez pas ce qui suit.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from _verif import verifier, terminer
    terminer(verifier(formater_uptime, [
        ((0,), "0j 0h 0min"),
        ((59,), "0j 0h 0min"),
        ((3600,), "0j 1h 0min"),
        ((90061,), "1j 1h 1min"),
        ((1049000,), "12j 3h 23min"),
    ]))
