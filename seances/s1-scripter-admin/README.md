# Séance 1 · Scripter l'administration (ven. 16/10)

Slides : [`slides/s1-scripter-admin.html`](../../slides/s1-scripter-admin.html)

## Au programme

| Durée | Activité |
|---|---|
| 15 min | Présentation du module et de l'évaluation |
| 15 min | [Quiz de positionnement](quiz-positionnement.md), non noté |
| 60 min | Cours : Bash ou Python, anatomie d'un script d'administration, l'IA comme copilote |
| 10 min | Pause |
| 100 min | **TP1 · Inventaire système** |
| 10 min | Débrief et suite |

## Avant de commencer

```bash
bash verifier_env.sh           # tout doit être [OK], sauf éventuellement shellcheck
cp ../../modeles/JOURNAL-IA.md ../../JOURNAL-IA.md
```

---

# TP1 · Inventaire système

**Contexte.** Vous arrivez dans une équipe d'exploitation qui gère une vingtaine de serveurs Linux. Avant chaque intervention, un collègue se connecte et tape une dizaine de commandes pour faire « l'état des lieux ». Vous allez automatiser cet état des lieux : d'abord en Bash, puis en Python, pour **comparer** les deux approches.

**Livrables** (dans ce dossier, poussés sur votre dépôt) :

- `inventaire.sh` (partie A) ;
- `inventaire.py` (partie B) ;
- au moins 2 entrées dans votre `JOURNAL-IA.md` (partie C) ;
- vos réponses aux questions de synthèse, dans `reponses.md`.

**Vérifier votre travail** à tout moment :

```bash
bash verifier_tp1.sh
```

## Partie A · En Bash (≈ 40 min)

Complétez les `TODO A1` à `A7` du fichier `inventaire.sh`. Le script doit afficher :

```
Inventaire du 2026-10-16 14:32:10

== Hôte ==
Nom      : srv-web-01
Système  : Ubuntu 24.04.1 LTS
Noyau    : 6.8.0-45-generic
Uptime   : 12j 3h 41min

== CPU et mémoire ==
CPU      : 4 cœur(s)
Charge   : 0.42 0.37 0.30
Mémoire  : 2811 Mio disponibles sur 7937 Mio

== Disques (seuil 80 %) ==
/                          47 %
/var                       86 %  ALERTE
/boot                      31 %

== Comptes interactifs (UID >= 1000) ==
alice           uid=1000   /bin/bash
bob             uid=1001   /bin/zsh

== Ports TCP en écoute ==
0.0.0.0:22
127.0.0.1:5432
[::]:80
```

| Option | Rôle |
|---|---|
| `-s SEUIL` | seuil d'alerte disque en % (défaut : 80) |
| `-o FICHIER` | écrire l'inventaire dans un fichier |
| `-h` | aide |

| Code retour | Signification |
|---|---|
| 0 | tout va bien |
| 1 | au moins un disque atteint ou dépasse le seuil |
| 2 | erreur d'usage : option inconnue, seuil invalide |

> **Contrainte de robustesse.** Si la commande `ss` n'existe pas (c'est le cas dans beaucoup de conteneurs), le script affiche « non disponible » dans la section Ports **et continue**.

## Partie B · En Python (≈ 45 min)

Complétez les `TODO B1` à `B10` de `inventaire.py`. On veut **la même chose**, avec en plus :

- `--format json` : une sortie JSON exploitable par d'autres outils, avec **exactement** cette structure :

```json
{
  "date": "2026-10-16T14:32:10",
  "hote":    {"nom": "srv-web-01", "systeme": "Ubuntu 24.04.1 LTS", "noyau": "6.8.0-45-generic", "uptime_s": 1049000},
  "cpu":     {"coeurs": 4, "charge": [0.42, 0.37, 0.3]},
  "memoire": {"total_mio": 7937, "disponible_mio": 2811},
  "disques": [{"point_montage": "/", "type": "ext4", "total_gio": 48.1, "utilise_pct": 47, "alerte": false}],
  "comptes": [{"nom": "alice", "uid": 1000, "shell": "/bin/bash"}],
  "ports_tcp": ["0.0.0.0:22", "127.0.0.1:5432"],
  "alerte": false
}
```

- les messages de diagnostic passent par `logging`, sur **stderr**, jamais sur stdout. Pourquoi ? Pensez à `inventaire.py --format json | jq .`.
- toute erreur (fichier de sortie impossible à écrire…) donne un message clair et le code retour 2, **pas une trace Python**.

Règle : **bibliothèque standard uniquement** (`pathlib`, `shutil`, `subprocess`, `json`, `argparse`, `logging`…).

## Partie C · Avec l'IA (tout au long du TP)

1. Choisissez **une** fonction de la partie B, par exemple `infos_disques` ou `ports_tcp_ecoute`, et faites-la écrire par l'IA de votre choix, avec un prompt qui suit la [charte](../../CHARTE-IA.md).
2. Passez le code obtenu au crible des **5 questions** de la grille de revue.
3. Notez dans `JOURNAL-IA.md` : le prompt, ce qui n'allait pas, ce que vous avez corrigé et comment vous l'avez vérifié.
4. Deuxième entrée au choix : explication d'une commande, d'une erreur, d'une regex…

## Questions de synthèse (`reponses.md`)

1. Citez deux choses **plus simples** en Bash et deux choses **plus simples** en Python, d'après votre expérience du TP.
2. Pourquoi est-il important que le script renvoie **1** quand un disque dépasse le seuil ? Qui va lire ce code retour ?
3. Votre % d'occupation disque en Python est-il le même que celui de `df` ? S'il diffère, pourquoi ? *(Indice : blocs réservés à root.)*
4. Votre script Bash contient-il un `cmd | while read` ? Quel problème cela pose-t-il pour la variable `ALERTE` ?
5. Qu'est-ce que l'IA a fait de travers dans votre partie C ? Comment l'auriez-vous détecté sans exécuter le code ?

## Pour aller plus loin (bonus)

- `shellcheck inventaire.sh` : corrigez tout ce qui est signalé.
- Ajoutez une option `--sections disques,ports` pour n'afficher que certaines sections.
- Planifiez l'inventaire JSON toutes les 15 minutes avec cron, écrit dans `/var/tmp/inventaire.json`. Que se passe-t-il si `ss` n'est pas dans le `PATH` de cron ? (On y reviendra en séance 4.)
