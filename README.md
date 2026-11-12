# SEOKB2

Le système SEO et la base de connaissances commune de Tim, installables dans le coffre de chaque élève. SEOKB2 prend la suite du système `organikk-seo-system` ; la version de distribution est **2.1.0**.

**Pour installer ou migrer : lire [INSTALLATION.md](INSTALLATION.md).** Donner le lien de ce dépôt à un agent ne suffit pas : il doit exécuter l'installateur en ciblant le coffre de l'élève.

L'installateur ajoute la bibliothèque commune dans `.seokb/base/`, les skills dans `.claude/skills/` et les commandes de diagnostic, dashboard et mise à jour dans `.seokb/runtime/`. Les données personnelles `raw/` et les productions `wiki/` restent dans le coffre. Les remplacements sont sauvegardés ; un conflit local interrompt l'installation avant toute écriture.

Les skills distribués reprennent le pack élèves Organikk 1.5.6 avec des chemins adaptés, une collecte GEO indépendante des outils privés, et les entrées SEOKB2. Les méthodes et sources du coffre filtré complètent cette distribution. Les automatisations personnelles du Mac de Tim sont conservées dans `archives/` pour référence ; elles ne sont pas installées.

La team stratégie (skill `team-strategie`, code dans `.seokb/runtime/team/`) pilote une stratégie SEO/GEO complète phase par phase : cadrage commercial, stratégie, sélection de 5 à 10 mots-clés business, un agent par mot-clé, roadmap. Elle lance chaque spécialiste avec Claude Code ou Codex déjà installé sur le poste de l'élève et exige l'accord explicite de l'élève entre les phases. Mode d'emploi : `.seokb/base/wiki/agents/team-strategie-mode-emploi.md`.

Python 3.10 ou supérieur et Git sont nécessaires. Aucune bibliothèque Python supplémentaire pour l'installation, le diagnostic et le dashboard. Certains workflows métier requièrent des outils, accès API, dépendances Python/Node ou données externes : leur disponibilité doit être vérifiée au lancement de la mission. Voir [CAPACITES.md](CAPACITES.md).

Le corpus reste une copie filtrée : des liens historiques peuvent viser des notes exclues pour confidentialité. L'index `wiki/index.md` liste les notes présentes. Une référence absente n'est pas une preuve consultée.

## Après installation

Depuis le coffre de l'élève :

```bash
python3 .seokb/runtime/doctor.py
python3 .seokb/runtime/dashboard.py --port 0
```

Ouvrir l'adresse localhost imprimée par le serveur. Les sections donnent accès au catalogue, au journal, aux sources, à la recherche, à la production et à la base commune. Relancer la session de l'agent après l'installation pour charger les skills.

## Prochaines mises à jour

```bash
python3 .seokb/runtime/update.py
```

Cette commande télécharge SEOKB2 et applique le même installateur avec sauvegarde et contrôle des conflits. Les anciens hooks connus sont raccordés à SEOKB2 ; aucun cron personnel n'est créé.
