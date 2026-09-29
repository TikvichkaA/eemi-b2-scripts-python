# Projet individuel : script d'automatisation d'une tâche d'administration

**Lancement** : séance 4 (13/11) · **Rendu et soutenance** : séance 6 (20/11) · **Poids** : 60 % de la note du module

## Attendus

Un dépôt Git personnel contenant :

1. **Le script**, en Python (ou en Bash si c'est justifié), qui automatise une tâche d'administration réaliste. Il doit :
   - accepter des arguments (`--help` complet) ;
   - produire des codes retour significatifs (0, 1, 2) ;
   - séparer le résultat (stdout) des messages (stderr ou `logging`) ;
   - échouer proprement sur une entrée absente ou malformée ;
   - pouvoir être **planifié** (cron ou timer systemd) : l'unité ou la ligne cron fait partie du rendu.
2. **Des tests** : au moins 5 tests `pytest`, dont 2 cas limites ; ou, pour un script Bash, un script de tests documenté.
3. **La documentation** : un `README.md` qui explique le but, l'installation, l'usage (avec exemples), la planification, les codes retour et les **limites connues**.
4. **Le journal d'usage de l'IA** : `JOURNAL-IA.md`, voir la [charte](../CHARTE-IA.md).
5. **Un historique Git lisible** : au moins 5 commits étalés dans le temps, avec des messages explicites.

## Sujets au choix

Vous pouvez proposer votre propre sujet ; il doit être validé en séance 4.

| # | Sujet | Ce qui le rend intéressant |
|---|---|---|
| A | **Sauvegarde avec rotation** d'un répertoire : archive horodatée, conservation de N versions, vérification d'intégrité | idempotence, espace disque, codes retour |
| B | **Audit des comptes locaux** : comptes sans mot de passe, UID 0 en double, shells inattendus, comptes inactifs | lecture de `/etc/passwd`, `/etc/shadow` et `lastlog`, rapport |
| C | **Provisioning d'utilisateurs** depuis un CSV : création, groupes, mot de passe temporaire, mode `--dry-run` | validation des entrées, effets de bord maîtrisés |
| D | **Veille d'expiration des certificats TLS** pour une liste d'hôtes, avec une alerte à J-30 et J-7 | réseau, gestion des timeouts, planification |
| E | **Analyse de journaux et rapport quotidien** (SSH, sudo, web) avec export CSV et alerte au-delà d'un seuil | parsing, agrégation, rapport |
| F | **Contrôle de conformité** d'un serveur : quelques règles CIS simples (ssh root, permissions, services) | lecture de configuration, rapport OK/KO |

## Soutenance (5 min + 5 min de questions)

- Démonstration du script : un cas nominal et un cas d'erreur.
- Choix techniques, en une diapositive au plus ou à l'oral.
- **Limites** et ce que vous amélioreriez.
- Questions : sur n'importe quelle ligne du code, sur l'usage de l'IA.

## Grille de notation (/20)

| Critère | Points |
|---|---|
| **Fonctionnement** : le script fait ce qu'il annonce, sur le cas nominal | 4 |
| **Robustesse** : entrées invalides, fichiers absents, droits, codes retour | 4 |
| **Qualité du code** : structure, lisibilité, pas de secret en dur, analyse statique propre | 3 |
| **Tests** : pertinence et cas limites | 2 |
| **Documentation** : README, `--help`, limites connues | 2 |
| **Planification** : cron ou timer fourni et expliqué | 1 |
| **Journal d'usage de l'IA** : sincère, montre un regard critique | 1 |
| **Soutenance** : clarté, maîtrise du code, réponses aux questions | 3 |

## Rattrapage

Un script fourni, qui fonctionne mal et n'est pas documenté, est à **fiabiliser, tester et documenter** en 3 h, en individuel, avec la même grille (hors soutenance, ramenée sur 20).
