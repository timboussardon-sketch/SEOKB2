# Installation et migration vers SEOKB2

## Prérequis

Python 3.10+, Git et accès au dépôt GitHub SEOKB2. Sous Windows, utiliser `py -3` si la commande `python3` n'existe pas. L'accès au dépôt privé peut demander d'accepter son invitation, puis `gh auth login` et `gh auth setup-git`.

## Migration d'un coffre Organikk 1.5.5 ou 1.5.6

Fermer les autres sessions d'agent qui écrivent dans le coffre. Depuis un dossier distinct du coffre :

```bash
git clone https://github.com/timboussardon-sketch/SEOKB2.git seokb2-distribution
python3 seokb2-distribution/scripts/install.py --target "/chemin/vers/mon-coffre" --dry-run
python3 seokb2-distribution/scripts/install.py --target "/chemin/vers/mon-coffre"
```

Remplacer le chemin par le dossier qui contient le `raw/` et le `wiki/` de l'élève. Ne pas viser le dossier de distribution. Une installation neuve utilise les mêmes commandes avec un dossier vide ou inexistant.

L'installateur préserve les sources, les notes, les paramètres et les skills personnels. Il remplace les skills identifiés comme identiques à l'ancien pack installé, puis raccorde les hooks historiques connus. L'ancien pack reste présent pour historique, mais la commande de mise à jour utilise SEOKB2. Les blocs d'instructions SEOKB2 sont ajoutés aux instructions existantes.

En cas de conflit, rien n'est installé. Lire les chemins indiqués et comparer les modifications personnelles. `--replace-modified` permet, après choix explicite, de sauvegarder puis remplacer ces fichiers. Ne pas ajouter ce drapeau par défaut.

## Vérification

Depuis le coffre ciblé :

```bash
python3 .seokb/runtime/doctor.py
python3 .seokb/runtime/dashboard.py --port 0
```

Le diagnostic doit indiquer `2.0.0`, le dépôt `timboussardon-sketch/SEOKB2` et une liste vide `modified_or_missing`. Le dashboard affiche les notes du coffre et sa base commune. Relancer l'agent pour charger les skills.

## Texte à donner à l'agent de l'élève

> Installe SEOKB2 depuis https://github.com/timboussardon-sketch/SEOKB2 dans mon coffre actuel. Lis INSTALLATION.md. Clone le dépôt dans un dossier distinct, identifie la racine de mon coffre et lance scripts/install.py avec --target, d'abord en --dry-run puis réellement si aucun conflit n'apparaît. Préserve mes notes et réglages. N'utilise pas l'ancien script de mise à jour Organikk pour cette migration. Vérifie la version et le dépôt avec doctor.py, lance le dashboard et donne-moi son lien local vérifié. Si un conflit apparaît, présente les fichiers concernés avant tout remplacement forcé.

## Retour arrière

Chaque installation affiche un dossier `_backups/seokb2/<date>/`, contenant les versions remplacées et `rollback.json`. Avant de restaurer, sauvegarder les modifications faites après cette installation : le retour arrière rétablit les fichiers de cette sauvegarde.

```bash
python3 seokb2-distribution/scripts/install.py --target "/chemin/vers/mon-coffre" --rollback "/chemin/vers/mon-coffre/_backups/seokb2/DATE"
```

Restaurer les sauvegardes dans l'ordre inverse des installations. L'installateur de distribution doit rester disponible pour cette commande.
