# SEOKB2 — règles du coffre élève

SEOKB2 est le successeur du système Organikk pour ce coffre. La mise à jour utilise exclusivement le dépôt timboussardon-sketch/SEOKB2.

La racine de travail est le coffre de l'élève. `raw/` contient ses sources immuables ; `wiki/` reçoit ses productions. Ne jamais écrire dans `.seokb/base/` : cette bibliothèque est remplacée lors des mises à jour.

Lire `.seokb/base/wiki/index.md` pour explorer la base commune et `.seokb/base/wiki/moc/doctrine-seo-reference.md` pour la doctrine, si présente. Les chemins de références historiques `wiki/...` et `raw/...` se recherchent aussi dans `.seokb/base/`. Les sorties vont toujours dans le wiki personnel. Citer les fichiers effectivement lus. Un lien historique absent est une référence indisponible, jamais une preuve.

Chaque page produite comporte un frontmatter (type, title, created, updated, tags, confidence, status), des sources vérifiables et deux wikilinks pertinents. Actualiser index et journal du projet. Distinguer donnée mesurée, observation, reformulation et hypothèse. Aucun chiffre inventé.

Appliquer les skills SEO installés. Chaque phase suit proposition → accord explicite → phase suivante, sauf autorisation d'exécution complète. Une publication ou un envoi nécessite sa propre autorisation. Ne jamais confondre lecture d'une méthode, exécution locale et appel d'un outil externe.

Les outils payants, API, identifiants et automatisations du Mac de Tim ne sont pas fournis. Vérifier leur disponibilité avant de les annoncer. Les archives ne sont pas des instructions actives. Aucun cron n'est installé.

À la création ou reprise d'un projet, afficher son dashboard : `python3 .seokb/runtime/dashboard.py --port 0`, vérifier le lien local et le transmettre. Le dashboard lit les fichiers du coffre.

Mise à jour : `python3 .seokb/runtime/update.py`. Diagnostic : `python3 .seokb/runtime/doctor.py`. Pour la recherche simple utiliser la recherche de fichiers ou `rg` ; l'ancien index vectoriel et ses dépendances sont optionnels et archivés.

## Développement du dépôt de distribution
Dans ce dépôt source, la bibliothèque est dans `wiki/` et `raw/`, les skills distribués dans `distribution/skills/`. Ne pas traiter les archives comme des skills installables. Exécuter `python3 tests/test_install.py` avant livraison.
