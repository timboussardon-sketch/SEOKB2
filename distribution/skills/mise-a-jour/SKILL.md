---
name: mise-a-jour
description: Installer les mises à jour SEOKB2 ou migrer le système Organikk existant vers SEOKB2.
---
# Mise à jour SEOKB2
Depuis la racine du coffre, exécuter `python3 .seokb/runtime/update.py`.
La source est https://github.com/timboussardon-sketch/SEOKB2.git.
Si .seokb est absent, suivre INSTALLATION.md du dépôt SEOKB2 : cloner puis lancer install.py avec le chemin explicite du coffre.
Ne pas lancer l'ancien installateur Organikk pour effectuer cette migration.
L'installateur sauvegarde ses remplacements et refuse les conflits locaux. Présenter ces conflits ; ne pas forcer sans accord.
Vérifier `python3 .seokb/runtime/doctor.py`, communiquer la version et la sauvegarde. Faire relancer la session pour charger les skills.
En cas d'accès refusé, demander de vérifier l'invitation au dépôt et l'authentification GitHub ; ne pas contourner cet accès.
