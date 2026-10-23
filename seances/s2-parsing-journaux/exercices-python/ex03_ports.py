"""Exercice 3 · Ports en écoute                           Notions : listes, set, sorted, int
Mode IA : DEMANDER UNE EXPLICATION, PAS LE CODE.

La commande `ss -Htln` donne des adresses d'écoute comme "0.0.0.0:22" ou "[::]:22" (IPv6).
Écrivez ports_uniques(adresses) qui renvoie la liste TRIÉE des numéros de port,
en ENTIERS, SANS DOUBLON.

    ports_uniques(["0.0.0.0:22", "[::]:22", "127.0.0.1:5432", "0.0.0.0:80"])  →  [22, 80, 5432]

Piège : une adresse IPv6 contient elle-même des « : ». Le port est après le DERNIER « : ».
Indice : cherchez la différence entre split et rsplit.
"""


def ports_uniques(adresses: list) -> list:
    # À vous
    return []


# ---------------------------------------------------------------------------
# Vérification : lancez  python3 ex03_ports.py
# Ne modifiez pas ce qui suit.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from _verif import verifier, terminer
    terminer(verifier(ports_uniques, [
        (([],), []),
        ((["0.0.0.0:22"],), [22]),
        ((["0.0.0.0:22", "[::]:22", "127.0.0.1:5432", "0.0.0.0:80"],), [22, 80, 5432]),
        ((["[fe80::1%eth0]:8080", "0.0.0.0:443", "0.0.0.0:443"],), [443, 8080]),
    ]))
