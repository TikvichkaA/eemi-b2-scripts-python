# Journal d'usage de l'IA

> Copiez ce fichier à la racine de votre dépôt et complétez-le **au fil de l'eau**, pas la veille du rendu.
> Une entrée par usage significatif : génération de code, explication, débogage, revue, tests.

| # | Date | Outil | Pour quoi faire | Prompt (résumé ou lien) | Ce qui était faux ou incomplet | Ce que j'ai corrigé ou vérifié, et comment |
|---|---|---|---|---|---|---|
| 1 | 16/10 | ChatGPT | Lire `/etc/os-release` en Python | « En Python 3.12, lire /etc/os-release et récupérer PRETTY_NAME… » | Ne gérait pas les guillemets autour de la valeur | Ajouté `.strip('"')` ; testé sur Ubuntu et Debian |
|   |   |   |   |   |   |   |

## Bilan (à remplir au rendu du projet)

- Ce que l'IA m'a fait gagner :
- Où elle m'a induit en erreur :
- Ce que je ferais différemment :
