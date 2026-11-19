# watchdog — agent de supervision système

`watchdog` est un script Python qui tourne en boucle, collecte des métriques système (CPU, RAM, disque) et écrit une alerte dans un fichier de log dès qu'un seuil est dépassé.

## Téléchargement

[Télécharger le ZIP](https://github.com/TikvichkaA/eemi-b2-scripts-python/releases/download/v1.0-watchdog/watchdog.zip)

## Installation

```bash
python -m pip install -r requirements.txt
```

## Utilisation

```bash
python main.py
python main.py --log /var/log/watchdog.log --interval 60
```

## Structure

| Fichier | Rôle |
|---|---|
| `config.py` | Seuils et paramètres globaux |
| `metrics.py` | Collecte des métriques avec `psutil` |
| `checker.py` | Comparaison aux seuils, production des alertes |
| `reporter.py` | Mise en forme et écriture dans le fichier de log |
| `main.py` | Point d'entrée, boucle principale, arguments CLI |

---

## Exercices

### 1 · Lire et comprendre

Lisez l'ensemble du code, fichier par fichier. Pour chaque fichier, rédigez **deux ou trois phrases** qui expliquent :
- ce qu'il fait,
- ce qu'il reçoit en entrée et ce qu'il produit en sortie,
- comment il s'articule avec les autres fichiers.

> Conseil : demandez à un LLM d'expliquer les parties que vous ne comprenez pas, puis reformulez avec vos propres mots.

---

### 1bis · Inventaire des paramètres

Ouvrez `config.py`. Pour chaque paramètre :
- indiquez à quoi il sert concrètement,
- précisez son unité,
- évaluez si la valeur actuelle vous semble raisonnable pour un serveur en production — justifiez votre réponse.

---

### 2 · Seuil disque

La valeur actuelle de `DISK_THRESHOLD` déclencherait une alerte sur la quasi-totalité des serveurs Linux en production dès leur mise en service.

- Quelle valeur est généralement retenue comme seuil d'alerte disque ? Cherchez une référence (documentation, bonne pratique).
- Corrigez la valeur dans `config.py`.
- Ajoutez un commentaire d'une ligne qui justifie votre choix.

---

### 3 · Intervalle de vérification

La valeur actuelle de `CHECK_INTERVAL` a deux effets indésirables.

- Identifiez-les (pensez à la charge sur le système et au volume du fichier de log).
- Quelle valeur serait plus adaptée à une supervision de serveur ? Justifiez.
- Corrigez `config.py`.

---

### 4 · Fichier de log

Lancez le watchdog, attendez qu'une alerte soit émise, arrêtez-le puis relancez-le.

- Que contient `watchdog.log` après le deuxième démarrage ?
- Identifiez la ligne dans `reporter.py` qui cause ce comportement.
- Corrigez-la. Quelle est la différence entre les modes `'w'` et `'a'` en Python ?

---

### 5 · Hostname dans les alertes

Les alertes écrites dans le log n'indiquent pas la machine d'origine. C'est acceptable sur un seul serveur, mais problématique si le même script tourne sur plusieurs machines et que les logs sont centralisés.

- Trouvez comment récupérer le nom de la machine en Python (module `socket`).
- Modifiez `reporter.py` pour que chaque ligne de log inclue le hostname.

Exemple de format attendu :

```
[2024-11-06 14:23:01] [srv-web-01] ALERTE : Disque plein : 82.3% (seuil 80%)
```

---

### 6 · Anti-spam *(bonus)*

Dans l'état actuel, si le disque reste au-dessus du seuil, une alerte est émise à **chaque cycle**.

- Modifiez `main.py` pour qu'une alerte ne soit réémise que si elle a disparu puis réapparu.
- Indication : il suffit de mémoriser l'ensemble des alertes actives au cycle précédent.
