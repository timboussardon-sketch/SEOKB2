---
name: tableau-de-bord-projet
description: Afficher le tableau de bord local du coffre et vérifier ses notes, sources, recherche et production.
---
# Tableau de bord SEOKB2
Depuis le coffre installé, lancer `python3 .seokb/runtime/dashboard.py --port 0`.
Le serveur imprime son adresse localhost disponible. Vérifier sa réponse HTTP et les liens avant de communiquer cette adresse.
Il lit `wiki/`, `raw/` et `.seokb/base/wiki/` du coffre courant. Ne jamais référencer le Mac de Tim.
Maintenir `wiki/pilotage/recap.md` avec mission, état réel, preuves, blocages et prochaines actions ; cette note reste la source du suivi.
Le serveur reste ouvert pendant son usage ; il faut le relancer après son arrêt. Aucun démarrage automatique n'est installé.
