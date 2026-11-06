# Vérification SEOKB2 2.0.0 — 6 novembre 2026

Vérifications locales exécutées avec Python sur macOS :

- Installation neuve et installation dans un chemin contenant des espaces.
- Migration depuis les fichiers Git de la version 1.5.5.
- Migration depuis une copie complète de la version 1.5.6, avec skills déjà copiés dans .claude/skills.
- Conservation des notes, des sources et des réglages personnels.
- Réinstallation sans changement ; conflit local refusé avant écriture.
- Liens symboliques refusés ; restauration des fichiers après une erreur d'écriture simulée.
- Retour arrière d'une installation neuve.
- Diagnostic des coffres migrés : aucun fichier géré manquant ou altéré.
- Contrôle HTTP du dashboard : accueil, sources, base commune, recherche, lecture d'une note personnelle et du catalogue commun. Traversée hors coffre refusée.
- Validation des skills seokb et mise-a-jour avec quick_validate.py.

Commande reproductible : `python3 tests/test_install.py`.

Limites : le navigateur de contrôle était indisponible, donc aucune validation visuelle n'est attestée. Les tests ont été exécutés sur macOS, pas sur Windows. Les workflows SEO et les intégrations externes ne sont pas tous exécutés par ces tests. Voir CAPACITES.md.
