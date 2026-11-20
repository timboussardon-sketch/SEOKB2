# SEOKB2 — règles du coffre élève

SEOKB2 est le successeur du système Organikk pour ce coffre. La mise à jour utilise exclusivement le dépôt timboussardon-sketch/SEOKB2.

La racine de travail est le coffre de l'élève. `raw/` contient ses sources immuables ; `wiki/` reçoit ses productions. Ne jamais écrire dans `.seokb/base/` : cette bibliothèque est remplacée lors des mises à jour.

Lire `.seokb/base/wiki/index.md` pour explorer la base commune et `.seokb/base/wiki/moc/doctrine-seo-reference.md` pour la doctrine, si présente ; sinon ouvrir `.seokb/base/wiki/doctrine/000-home.md`. Les chemins de références historiques `wiki/...` et `raw/...` se recherchent aussi dans `.seokb/base/`. Les sorties vont toujours dans le wiki personnel. Citer les fichiers effectivement lus. Un lien historique absent est une référence indisponible, jamais une preuve.

Chaque page produite comporte un frontmatter (type, title, created, updated, tags, confidence, status), des sources vérifiables et deux wikilinks pertinents. Actualiser index et journal du projet. Distinguer donnée mesurée, observation, reformulation et hypothèse. Aucun chiffre inventé.

Appliquer les skills SEO installés. Chaque phase suit proposition → accord explicite → phase suivante, sauf autorisation d'exécution complète. Une publication ou un envoi nécessite sa propre autorisation. Ne jamais confondre lecture d'une méthode, exécution locale et appel d'un outil externe.

Pour une stratégie SEO/GEO complète (« stratégie GEO », « strat client », « stratégie SEO complète »), passer par le skill `team-strategie` : un coordinateur local (`.seokb/runtime/team/`) lance un spécialiste par phase avec Claude Code ou Codex, et rien ne franchit une phase sans l'accord explicite de l'utilisateur. Les méthodes métier restent les skills `go-to-market`, `strategie-geo`, `strategie-mot-cle`, `strategie-contenu` et `roadmap-seo`. Chaque spécialiste consomme l'accès de l'utilisateur à l'agent : annoncer le nombre d'appels avant de lancer une vague.

Pour une recherche de mots-clés ou le choix des mots-clés à attaquer (« recherche de mots-clés », « quels mots-clés cibler », « team mots-clés », « les 14 étapes »), passer par le skill `team-mots-cles` : la session pilote six agents de `.claude/agents/` sur le workflow mots-clés complet et enregistre cinq accords de l'utilisateur avec `.seokb/runtime/teams/etat.py`. Un terme déjà nommé va à `strategie-mot-cle` ; une étape demandée seule garde son skill.

Les outils payants, API, identifiants et automatisations du Mac de Tim ne sont pas fournis. Vérifier leur disponibilité avant de les annoncer. Les archives ne sont pas des instructions actives. Aucun cron n'est installé.

Brief du jour : skill `brief-matin` (décisions d'abord, faits sourcés, inférences marquées). Réponse à un email : skill `reponse-fil`, qui n'envoie jamais. Sauvegarde hors de l'ordinateur : skill `sauvegarde-coffre` ; la proposer quand le coffre n'a jamais été sauvegardé.

À la création ou reprise d'un projet, afficher son dashboard : `python -X utf8 .seokb/runtime/dashboard.py --port 0`, vérifier le lien local et le transmettre. Le dashboard lit les fichiers du coffre.

Mise à jour : `python -X utf8 .seokb/runtime/update.py`. Diagnostic : `python -X utf8 .seokb/runtime/doctor.py`. Pour la recherche simple utiliser la recherche de fichiers ou `rg` ; l'ancien index vectoriel et ses dépendances sont optionnels et archivés.
