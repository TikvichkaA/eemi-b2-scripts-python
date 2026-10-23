"""Exercice 6 · L'IP d'un échec SSH                        Notions : in, split, index, None
Mode IA : COMPARER DEUX SOLUTIONS.

Écrivez ip_echec(ligne) qui renvoie l'adresse IP d'une ligne d'échec SSH
(une ligne qui contient "Failed password"), et None pour toute autre ligne.

    ... sshd[21031]: Failed password for oracle from 203.0.113.45 port 30383 ssh2
    ... sshd[21078]: Failed password for invalid user ubuntu from 203.0.113.45 port 46613 ssh2
    → "203.0.113.45" dans les deux cas

Indice : ligne.split() découpe en mots ; liste.index("from") donne la position d'un mot.

Consigne IA : demandez à l'IA DEUX solutions, l'une avec split, l'autre avec une
expression régulière (module re). Gardez celle que vous savez expliquer, et notez
dans JOURNAL-IA.md pourquoi.
"""


def ip_echec(ligne: str):
    # À vous
    return None


# ---------------------------------------------------------------------------
# Vérification : lancez  python3 ex06_ip_echec.py
# Ne modifiez pas ce qui suit.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from _verif import verifier, terminer
    L1 = "2026-10-15T06:03:46+02:00 srv-web-01 sshd[21031]: Failed password for oracle from 203.0.113.45 port 30383 ssh2"
    L2 = "2026-10-15T06:12:07+02:00 srv-web-01 sshd[21078]: Failed password for invalid user ubuntu from 192.0.2.150 port 46613 ssh2"
    L3 = "2026-10-15T06:12:49+02:00 srv-web-01 sshd[21117]: Accepted publickey for bob from 10.0.0.12 port 59936 ssh2"
    L4 = "2026-10-15T06:09:30+02:00 srv-web-01 CRON[21058]: pam_unix(cron:session): session opened for user root(uid=0)"
    terminer(verifier(ip_echec, [
        ((L1,), "203.0.113.45"),
        ((L2,), "192.0.2.150"),
        ((L3,), None),
        ((L4,), None),
        (("",), None),
    ]))
