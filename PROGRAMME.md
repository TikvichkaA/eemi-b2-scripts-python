# Programme détaillé

Chaque séance dure 3 h 30 et alterne apports courts (30 % du temps au plus) et pratique. Chaque séance contient un temps de travail **avec l'IA**, cadré par la [charte](CHARTE-IA.md).

| Objectif du syllabus | Séances |
|---|---|
| O1. Automatiser et planifier une tâche d'administration | 1, 4 |
| O2. Analyser et exploiter les événements système | 2, 3 |
| O3. Documenter les scripts | 1, 5, 6 |
| O4. Vérifier la fiabilité et la robustesse | 3, 5, 6 |

---

## Séance 1 · Scripter l'administration

**Contenu**
- Pourquoi automatiser : fiabilité, traçabilité, reproductibilité.
- Bash ou Python : critères de choix.
- Anatomie d'un script d'administration propre :
  - shebang, `--help`, arguments ;
  - codes retour, stdout et stderr ;
  - pas de secret en dur.
- Bash robuste (`set -euo pipefail`, guillemets, `trap`) et Python robuste (`main()`, `argparse`, `subprocess.run`, `pathlib`).
- L'IA comme copilote : ce qu'elle fait bien, ce qu'elle fait mal, les règles d'usage, le prompt efficace.

**Activités**
- Quiz de positionnement (15 min, non noté).
- Démonstration : prompt → code → revue critique.
- **TP1 · Inventaire système** : le même script d'inventaire, d'abord en Bash, puis en Python avec une sortie JSON et une alerte disque. Premières entrées du journal d'usage de l'IA.

---

## Séance 2 · Les bases de Python, avec l'IA comme tuteur

**Contenu**
- Lancer Python : interpréteur et script, indentation.
- Valeurs et conversions, chaînes (`split`, `partition`, `strip`, f-strings), listes, `set`, dictionnaires.
- Conditions, boucles, fonctions ; lire un fichier ; lire un message d'erreur.
- Apprendre avec l'IA : expliquer, donner un indice, proposer des tests, comparer, déboguer.

**Activités**
- **8 exercices Python** auto-vérifiés, chacun avec un mode d'usage de l'IA différent ; l'exercice 7 est le cœur du détecteur de brute force SSH.
- Le TP2 complet (expressions régulières, fenêtres de temps, rapport CSV/JSON) suit à la prochaine séance.

---

## Séance 3 · Supervision et alertes

**Contenu**
- Métriques système avec `psutil` : CPU, mémoire, disque, processus, services.
- Seuils, hystérésis, anti-spam d'alertes.
- Notifier par mail, webhook ou syslog.
- Ce que fait un vrai outil de supervision (Zabbix, Prometheus), et ce que fait votre script.

**Activités**
- **Note 1 · TP noté en binôme** : mini-agent de surveillance paramétrable qui produit des alertes.
- **IA** : faire expliquer une anomalie de logs ; repérer où l'IA se trompe.

---

## Séance 4 · Automatiser et planifier

**Contenu**
- cron et timers systemd : syntaxe, environnement d'exécution, sortie des tâches.
- Idempotence, fichier de verrou, reprise sur erreur.
- Journalisation avec le module `logging` : niveaux, rotation.
- Configuration (fichier INI ou YAML, variables d'environnement) et gestion des secrets.

**Activités**
- Planifier le TP2 ou le TP3 avec un timer systemd.
- **Lancement du projet individuel** : choix du sujet, cahier des charges d'une page.
- **IA** : générer les unités systemd et les expressions cron, puis les vérifier.

---

## Séance 5 · Fiabilité et documentation

**Contenu**
- Gestion d'erreurs et validation des entrées ; mode `--dry-run`.
- Tests avec `pytest` : cas nominaux, cas limites, fichiers de test.
- Analyse statique : `shellcheck`, `ruff`, `bandit`.
- Documentation : README, `--help`, docstrings, schéma de fonctionnement, CHANGELOG.

**Activités**
- Atelier projet.
- **IA** : revue de code et génération de tests, avec vérification croisée (les tests générés passent-ils vraiment ? couvrent-ils les bons cas ?).

---

## Séance 6 · Finalisation et soutenances

**Activités**
- Finalisation et rendu du projet : dépôt Git, README, tests, journal d'usage de l'IA.
- **Note 2 · Soutenances individuelles** : 5 min de présentation (fonctionnement, démo, limites), puis 5 min de questions.
- Bilan du module.
