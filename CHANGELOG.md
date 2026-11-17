# Versions

## 2.3.2 — 2026-11-17

`slop.mjs` (skill `redaction-anti-ia`) détecte deux gabarits de plus : une grappe de trois familles de tells dans un même paragraphe, et des phrases de longueur trop uniforme sur l'ensemble du texte. Un tell isolé reste toléré, c'est la densité qui alerte. Correction : « évidemment », « bien sûr » et « naturellement » n'étaient jamais détectés (la limite de mot `\b` ignore les lettres accentuées). Les deux nouveautés sont des alertes (WARN), jamais bloquantes sans `--strict`.

## 2.3.1 — 2026-11-13

Les mises à jour s'annoncent d'elles-mêmes : à l'ouverture de Claude Code, une fois par jour, le coffre vérifie le dépôt SEOKB2 et, si une version plus récente existe, affiche « SEOKB2 X disponible » dans le terminal et Claude la propose dans sa première réponse avec les nouveautés, sans la lancer sans accord. L'installateur déclare cette vérification dans `.claude/settings.json` en conservant les autres réglages ; un fichier de réglages illisible n'est pas touché. Rien ne s'affiche quand le coffre est à jour. Un dépôt inaccessible donne une ligne d'avertissement, sans bloquer la session. Les coffres installés en 2.0.0 à 2.3.0 sans l'ancien pack doivent lancer une fois « mets à jour SEOKB2 » pour recevoir la vérification.

## 2.3.0 — 2026-11-13

Trois briques de pilotage. Skill `brief-matin` : un brief de moins de 400 mots qui met en tête les décisions à prendre, puis les faits sourcés, les inférences marquées, le travail fait et les questions ; le dashboard affiche le dernier brief sur sa page d'accueil. Skill `reponse-fil` : prépare la réponse à un fil d'emails (demande, engagements déjà pris avec leur source, manques, choix à trancher hors du brouillon, brouillon dans ta voix) et n'envoie jamais. Skill `sauvegarde-coffre` et script `sauvegarde.py` : archive ZIP du coffre vers un dossier synchronisé ou un disque externe, contrôlée par relecture, 7 archives gardées, restauration dans un dossier vide ; `.env*`, `_backups/` et la bibliothèque réinstallable sont exclus. Aucune tâche planifiée n'est installée.

## 2.2.0 — 2026-11-12

Agent prospect livré aux élèves : l'application (découverte, qualification, mesure de présence IA, emails relus, suivi) est dans `.seokb/base/agent-prospect/`, avec le skill `agent-prospect`. Le dossier `agent-prospect/` de la racine, copie du 2 octobre que l'installateur ne distribuait pas, est remplacé. L'identité de l'expéditeur (nom, entreprise, URL, bandeau) vient de `.env.local` au lieu d'être écrite dans le code ; le User-Agent du crawler est `ProspectAgent`. Retirés : la roadmap personnelle, la bannière, les adresses de tiers des tests, un fichier de résultats de tests qui portait des chemins locaux. `go-to-market` était déjà distribué depuis la 2.1.0 : inchangé.

## 2.1.0 — 2026-11-12

Team stratégie SEO/GEO : coordinateur local, un spécialiste par phase lancé avec Claude Code ou Codex, accord explicite entre les phases, dashboard local. Nouveaux skills `team-strategie`, `go-to-market`, `roadmap-seo`, `strategie-contenu` et `reecriture-francais`. `strategie-geo` passe au pilote en dix étapes et treize parties ; `strategie-mot-cle` s'exécute dans un portefeuille de mots-clés. Le workflow article passe à cinq phases validées (brief, structure Hn, data, FAQ, rédaction) dans `seo-workflow-article`, `article-engine-pipeline` et les deux skills de rédaction. `maillage-systeme` compte les pages sources distinctes ; `maillage-interne-gsc` sépare ce que prouvent le crawl et la Search Console. Notes de base `team-strategie`, `team-strategie-mode-emploi` et `go-to-market`.

## 2.0.0 — 2026-11-06

Première distribution installable SEOKB2. Migration depuis Organikk avec sauvegarde, contrôle des conflits, instructions d'agent, base commune séparée, skills portables issus du pack élèves, dashboard local et mise à jour vers le dépôt SEOKB2. Archivage des automatismes personnels, catalogue des notes présentes et documentation des dépendances externes.
