# Scripts de parsing et d'automatisation (Python)

**EEMI Paris · B2 Cybersécurité · 21 h (6 séances de 3 h 30)**
Titre RNCP 37680 *Administrateur d'infrastructures sécurisées*, bloc 1, compétence CP3.
Intervenant : Emmanuel Pinglier

## Objectifs

À l'issue du module, vous serez capables de :

1. **automatiser et planifier** une tâche d'administration par script, en Python ou en Bash ;
2. **analyser et exploiter** les événements système à partir des journaux et de la supervision ;
3. **documenter** les scripts que vous produisez, et faire évoluer cette documentation ;
4. **vérifier la fiabilité et la robustesse** d'un script avant de le mettre en exploitation.

L'IA générative fait partie du module : c'est un outil à **maîtriser**, pas à subir. Lisez [CHARTE-IA.md](CHARTE-IA.md) avant la première séance.

## Programme

| # | Date | Thème | Dossier |
|---|---|---|---|
| 1 | ven. 16/10 | Scripter l'administration : Bash ou Python, anatomie d'un script propre, l'IA comme copilote | [`seances/s1-scripter-admin`](seances/s1-scripter-admin) |
| 2 | ven. 23/10 | Parser les journaux : regex, auth.log, journald, logs web | [`seances/s2-parsing-journaux`](seances/s2-parsing-journaux) |
| 3 | ven. 06/11 | Supervision : métriques, seuils, alertes · **TP noté en binôme** | [`seances/s3-supervision`](seances/s3-supervision) |
| 4 | ven. 13/11 | Automatiser et planifier : cron, timers systemd, journalisation, configuration · **lancement du projet** | [`seances/s4-planification`](seances/s4-planification) |
| 5 | jeu. 19/11 | Fiabilité et documentation : erreurs, tests, analyse statique, README | [`seances/s5-fiabilite-doc`](seances/s5-fiabilite-doc) |
| 6 | ven. 20/11 | Finalisation et soutenances · **note individuelle** | [`seances/s6-soutenances`](seances/s6-soutenances) |

Le détail se trouve dans [PROGRAMME.md](PROGRAMME.md). Les slides sont dans [`slides/`](slides/) : ouvrez simplement le fichier `.html` dans un navigateur.

## Évaluation

| Note | Quand | Forme | Poids |
|---|---|---|---|
| Note 1 | Séance 3 | TP noté **en binôme** : mini-agent de surveillance avec alertes | 40 % |
| Note 2 | Séance 6 | **Projet individuel** : script d'automatisation d'une tâche d'administration, avec sa documentation, ses tests et son journal d'usage de l'IA, puis **oral de 5 min** sur son fonctionnement et ses limites | 60 % |

Les sujets et la grille sont dans [`evaluation/`](evaluation/). Un sujet de rattrapage est prévu.

## Mettre en place son environnement (avant la séance 1)

Il vous faut **un Linux** (Debian, Ubuntu ou équivalent) avec **Python 3.10 ou plus**, **Git** et **Bash**. Au choix :

| Votre machine | Solution recommandée |
|---|---|
| Linux | rien à faire |
| Windows | **WSL 2** avec Ubuntu : `wsl --install -d Ubuntu`, dans un PowerShell administrateur |
| macOS | une VM Ubuntu (UTM, VirtualBox) : la plupart des TP lisent des fichiers propres à Linux (`/proc`, `/etc/os-release`, `journalctl`) |
| Aucune | un conteneur : `docker run -it --rm -v "$PWD":/work -w /work ubuntu:24.04 bash`, puis `apt update && apt install -y python3 python3-venv git iproute2` |

Ensuite :

```bash
git clone https://github.com/TikvichkaA/eemi-b2-scripts-python.git
cd eemi-b2-scripts-python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 --version          # 3.10 ou plus
bash seances/s1-scripter-admin/verifier_env.sh
```

## Organisation du dépôt

```
.
├── README.md             ce fichier
├── PROGRAMME.md          déroulé détaillé des 6 séances
├── CHARTE-IA.md          règles d'usage de l'IA et journal d'usage à tenir
├── requirements.txt      dépendances Python du module
├── slides/               slides HTML de chaque séance
├── seances/              un dossier par séance : énoncés de TP, fichiers de départ, données
├── modeles/              modèles de scripts propres (Bash et Python), à copier pour démarrer
└── evaluation/           sujets du projet individuel et grille
```

## Rendre son travail

Chaque étudiant travaille dans **son propre fork** (ou sa copie) du dépôt. Pour chaque TP :

```bash
git add seances/s1-scripter-admin/
git commit -m "TP1 : inventaire système"
git push
```

Committez souvent, avec des messages clairs : l'historique Git fait partie de ce qui est évalué pour le projet.
