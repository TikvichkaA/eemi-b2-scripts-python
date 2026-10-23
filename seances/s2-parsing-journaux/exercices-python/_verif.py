"""Petit outil de vérification des exercices. Vous n'avez pas besoin de le modifier."""
from __future__ import annotations

import sys


def verifier(fonction, cas: list) -> bool:
    """Appelle `fonction` sur chaque cas et affiche le résultat.

    Chaque cas est un couple (arguments, attendu). `attendu` peut être une
    classe d'exception (ex. ValueError) si la fonction doit lever cette erreur.
    """
    ok = 0
    print(f"\n{fonction.__name__} :")
    for args, attendu in cas:
        appel = f"{fonction.__name__}({', '.join(repr(a) for a in args)})"
        try:
            obtenu = fonction(*args)
        except Exception as e:  # noqa: BLE001 - on veut tout afficher à l'étudiant
            if isinstance(attendu, type) and issubclass(attendu, Exception) and isinstance(e, attendu):
                print(f"  ✓ {appel} lève bien {type(e).__name__}")
                ok += 1
            else:
                print(f"  ✗ {appel}\n      erreur : {type(e).__name__}: {e}")
            continue
        if isinstance(attendu, type) and issubclass(attendu, Exception):
            print(f"  ✗ {appel}\n      attendu : une erreur {attendu.__name__}\n      obtenu  : {obtenu!r}")
        elif obtenu == attendu and type(obtenu) is type(attendu):
            print(f"  ✓ {appel} → {obtenu!r}")
            ok += 1
        else:
            print(f"  ✗ {appel}\n      attendu : {attendu!r}\n      obtenu  : {obtenu!r}")
    total = len(cas)
    print(f"\n{'Bravo, tout passe !' if ok == total else 'À reprendre'} ({ok}/{total})")
    return ok == total


def terminer(reussi: bool) -> None:
    sys.exit(0 if reussi else 1)
