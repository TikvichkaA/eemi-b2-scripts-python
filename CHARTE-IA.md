# Charte d'usage de l'IA

Dans ce module, l'IA générative (ChatGPT, Claude, Copilot, Mistral…) est **autorisée et encouragée**. En contrepartie, vous êtes **entièrement responsables** de chaque ligne que vous rendez, comme un admin l'est de chaque commande qu'il lance en production.

## Les 5 règles

1. **Aucune donnée sensible dans un prompt.** Pas de mot de passe, de clé d'API, de nom d'hôte ou d'adresse IP réels, ni de log d'une vraie entreprise. Anonymisez (`10.0.0.x`, `srv-web-01`, `user01`) ou utilisez les jeux de données fournis.
2. **Vous comprenez tout ce que vous rendez.** Si vous ne savez pas expliquer une ligne à l'oral, elle n'a rien à faire dans votre script.
3. **Vous testez avant de faire confiance.** Tout code généré s'exécute d'abord dans un environnement jetable (VM, conteneur, WSL). Jamais de `rm`, `chmod`, `iptables`, `userdel`… générés et lancés sans relecture.
4. **Vous vérifiez à la source.** Options de commande, noms de fonctions, versions : l'IA invente parfois. `man`, `--help` et la documentation officielle font foi.
5. **Vous tracez votre usage** dans `JOURNAL-IA.md`, à la racine de votre dépôt : modèle dans [`modeles/JOURNAL-IA.md`](modeles/JOURNAL-IA.md).

## Pourquoi un journal d'usage de l'IA ?

Il ne sert **pas** à sanctionner l'usage de l'IA. Il sert à montrer que vous l'avez **pilotée**. Il fait partie de l'évaluation du projet, et un journal honnête qui montre les erreurs de l'IA que vous avez corrigées vaut mieux qu'un journal vide.

## Un prompt efficace pour du scripting d'administration

```
Contexte : Ubuntu 24.04, Python 3.12, script lancé par cron en tant que root.
Tâche    : lire /var/log/auth.log et compter les échecs de connexion SSH par IP.
Contraintes : bibliothèque standard uniquement ; ne pas planter si le fichier
             est absent (message sur stderr, code retour 2).
Format   : un seul fichier, fonction main(), argparse.
Demande  : explique chaque regex, puis propose 3 cas de test, dont 1 cas limite.
```

À comparer avec : *« fais-moi un script python qui analyse les logs ssh »*.

## Grille de revue d'un code généré (5 questions)

1. Est-ce que **je comprends** chaque ligne ?
2. Que se passe-t-il si l'entrée est **absente, vide ou malformée** ?
3. Le script a-t-il des **effets de bord** : écriture, suppression, réseau, droits ?
4. Les commandes et options utilisées **existent-elles vraiment** sur ma version ?
5. Comment je **teste** que ça marche, et que ça échoue proprement ?
