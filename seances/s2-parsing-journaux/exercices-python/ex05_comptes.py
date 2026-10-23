"""Exercice 5 · Comptes humains de /etc/passwd             Notions : split, int, conditions, continue
Mode IA : L'IA PROPOSE DES CAS DE TEST.

Chaque ligne de /etc/passwd a 7 champs séparés par « : » :
    nom:x:UID:GID:commentaire:dossier:shell
    alice:x:1000:1000:Alice:/home/alice:/bin/bash

Écrivez comptes_humains(lignes) qui renvoie la liste des NOMS des comptes :
  - dont l'UID est supérieur ou égal à 1000, sauf 65534 (nobody) ;
  - dont le shell ne se termine ni par "nologin" ni par "false".
Les lignes vides ou qui n'ont pas 7 champs sont ignorées, sans planter.

Consigne IA : une fois vos tests au vert, demandez à l'IA 3 cas limites supplémentaires,
et ajoutez-les à la liste des tests en bas du fichier.
"""


def comptes_humains(lignes: list) -> list:
    # À vous
    return []


# ---------------------------------------------------------------------------
# Vérification : lancez  python3 ex05_comptes.py
# Ne modifiez pas ce qui suit.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from _verif import verifier, terminer
    PASSWD = [
        "root:x:0:0:root:/root:/bin/bash",
        "daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin",
        "alice:x:1000:1000:Alice:/home/alice:/bin/bash",
        "bob:x:1001:1001:Bob:/home/bob:/bin/zsh",
        "svc-backup:x:1002:1002::/srv/backup:/bin/false",
        "nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin",
        "",
        "ligne cassée",
    ]
    terminer(verifier(comptes_humains, [
        (([],), []),
        ((PASSWD,), ["alice", "bob"]),
        ((["carol:x:1003:1003::/home/carol:/bin/sh\n"],), ["carol"]),
        # Ajoutez ici vos cas limites proposés par l'IA :
    ]))
