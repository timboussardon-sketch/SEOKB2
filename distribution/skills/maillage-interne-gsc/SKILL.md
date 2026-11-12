---
name: maillage-interne-gsc
description: "Plan de maillage interne depuis la Search Console, pages mère/fille. « maillage », « liens internes », « pages orphelines »."
---

# Skill — Maillage Interne GSC

## Quand utiliser ce skill

Analyse et optimisation du maillage interne depuis les données GSC. Hiérarchie page mère/fille/petite-fille selon la méthode Boussardon. Pipeline en 5 étapes : récupérer GSC → diagnostiquer la structure (mères potentielles, sous-maillées, orphelines) → construire le plan de maillage avec règles Know→Do → prioriser par score urgence → générer recommandations (page source, destination, ancre, contexte). Sortie obligatoire en plus du tableau : un rapport de pré-décision (diagnostic, preuves typées, état Critique / À améliorer / Sain, actions P1-P3 avec confiance, effort et risque, jamais de score affiché) ; sans lui le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "maillage interne", "liens internes", "cocon SEO", "pages orphelines", "GSC + structure de site", quand un fichier GSC est uploadé.

## Quand déclencher

Analyse et optimisation du maillage interne depuis les données GSC. Hiérarchie page mère/fille/petite-fille.

## Philosophie

> "Le maillage interne, c'est la puissance. Et ça part de tes mots-clés."

- Page mère = citée depuis des pages filles/petites-filles distinctes, liens du corps (repère interne : 5 ; les anciennes règles disaient 10, les deux sont des repères de travail, pas des seuils de santé)
- Le maillage part de la stratégie de mots-clés → le cocon est la conséquence
- Priorité : transactionnel > décisionnel > informationnel
- Maillage par intention (Know → Do) en plus du maillage sémantique

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Export GSC Pages — URL, Clics, Impressions, CTR, Position | Oui |
| Export GSC Requêtes par page | Recommandé |
| Période 3-6 mois | Recommandé |

## Pipeline (5 étapes)

1. **Récupérer les données GSC** — export Pages + Requêtes par URL
2. **Diagnostiquer la structure** :
   - Pages mères potentielles (impressions élevées, pos 4-15, requête transactionnelle)
   - Pages sous-maillées : déficit de liens entrants confirmé par un crawl ; le CTR seul ne le démontre pas
   - Pages orphelines : aucun lien entrant détecté dans le périmètre du crawl, à expliciter ; la GSC seule ne le démontre pas
3. **Construire le plan de maillage** — hiérarchie mère/fille/petite-fille + règles Know→Do
4. **Prioriser** — plus de score numérique (l'ancienne formule `(Impressions × 0.4) + (Potentiel position × 0.4) + (Business value × 0.2)` additionnait des grandeurs non normalisées, les impressions écrasaient le reste). Priorité justifiée, dans cet ordre : (a) page business prioritaire à fort déficit de maillage (forte en impressions, peu de liens entrants éditoriaux depuis des pages distinctes) ; (b) page en position 4-15 sur une requête transactionnelle que des liens entrants peuvent aider ; (c) page en forte baisse sur 90 jours contre 90 (tendance `declining`) ; (d) le reste. Chaque recommandation écrit la raison de son rang.
5. **Générer les recommandations** — page source + page destination + ancre + contexte + priorité

## Structure hiérarchique

```
Page Mère (mot-clé principal business)
├── Page Fille 1 (requête secondaire transactionnelle)
│   ├── Page Petite-Fille A (longue traîne / micro-intention)
│   └── Page Petite-Fille B
└── Page Fille 2
```

Règle Know → Do : chaque page Know doit pointer vers au moins 1 page Do thématiquement reliée.

## Sortie de pré-décision (obligatoire)

Ce skill n'a pas terminé tant que le rapport de pré-décision n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau, et il suit `audit-complet-v2/rapport-audit-seo-format.md` (`audit-complet-v2/rapport-audit-seo-format.md`). Fichier : `wiki/maillage/YYYY-MM-DD-slug-gsc-decision.md`.

Ce qu'il contient, dans cet ordre :

1. Diagnostic principal : une phrase, la cause structurante, pas une liste d'erreurs
2. Les chiffres à retenir : 3 à 5, ceux qui illustrent le diagnostic
3. État : Critique, À améliorer ou Sain, calculé sur l'impact SEO réel et le type de page, jamais sur le nombre d'erreurs ; jamais de score sur 10
4. Problèmes (3 maximum) et opportunités (5 maximum), séparés : chacun avec Preuve (2 à 4 données), Pourquoi c'est important, Action, Confiance (forte / moyenne / faible) ; chaque problème s'écrit en trois temps : observation prouvée → conséquence ou risque justifié → bénéfice attendu de la correction (l'observation seule n'est pas un frein SEO démontré)
5. Actions P1 / P2 / P3, 3 P1 maximum : pourquoi, preuve, signal attendu (jamais un résultat chiffré promis), dépendance préalable, test de validation (ce qui distingue « correction appliquée » de « résultat SEO observé »), effort faible / moyen / élevé (jamais en heures), confiance, risque low / medium / high ; toute action high (suppression, 301, fusion, changement d'URL) porte « À valider avant déploiement » et sa checklist
6. Ce que les données ne permettent pas de conclure, et « données insuffisantes » ou « ne rien faire » quand c'est le cas

Sur le périmètre de ce skill, le rapport tranche les pages fortes en impressions et sous-liées, tendance 28 jours contre 28 et 90 contre 90 par page stratégique (growing / stable / declining / new / insufficient_data), les fortes baisses en premier.

Règles : chaque information est typée FACT, HYPOTHESIS ou ACTION, jamais une hypothèse écrite comme un fait ; un problème existe une seule fois (ID), les observations qui parlent du même problème fusionnent ; une anomalie n'est pas une priorité par défaut ; les pages business et les tendances GSC passent avant les anomalies techniques secondaires ; jamais de recommandation automatique de fusion, 301, suppression, réécriture ou création de page ; Google n'est jamais anthropomorphisé. Phrases courtes, une donnée par diagnostic, aucune des phrases « Il est important de », « Il convient de », « Cela peut potentiellement », « Il est intéressant de noter », « Dans le cadre de ».

Restitution (corrections V2 du 23 septembre) : aucun ID technique ni mot anglais (low / medium / high) dans le rapport ; Faible / Moyen / Élevé partout ; la certitude affichée ne dépasse jamais la couverture des données (« aucun problème majeur détecté sur les URL inspectées », pas « Sain ») ; formulations précises (« URL en 404 avec encore des impressions ») ; aucune action proposée sur une page dont les requêtes ne sont pas connues (« à vérifier ») ; le nombre de mots seul n'est jamais un problème ; limites de longueur : diagnostic 70 mots, 4 chiffres, 3 problèmes de 40 mots, 6 actions, 3 opportunités de 35 mots, le reste dans les détails repliés.

Onglet Analyse technique, structure validée le 23 septembre 2026 (référence : [[audit/2026-09-22-organikk-co]]) : chaque priorité = une phrase de cadrage, « Ce qu'on observe » (faits chiffrés en liste, pages en code), « Pourquoi c'est prioritaire » (deux phrases), « Action » (liste numérotée courte), « Impact attendu » et « Risque » en gras ; puis le plan des 30 jours en trois paliers (Priorité immédiate, Deuxième étape, Priorité secondaire), une action par paragraphe en gras suivie d'une phrase ; puis « à surveiller avant d'agir » pour la page dont la cause n'est pas isolée ; puis « Autres pages à surveiller » : chiffres séparés par « · », une phrase, verdict en gras (« Aucune action recommandée », « À vérifier avant toute modification »).

## Output obligatoire

Pour chaque action :
- Page source (intention Know/Do/Know+Do)
- Page destination + intention
- Nature du lien (sémantique ou intentionnel Know→Do)
- Ancre recommandée (jamais "cliquez ici")
- Contexte d'insertion
- Priorité (Haute/Moyenne/Faible)

## Règles absolues

- Ne pas automatiser à 100% — le maillage part de la stratégie, pas des outils
- Ne pas mailler sans tenir compte de l'intention (sémantique ≠ intentionnel)
- Ne pas répéter la même ancre sur toutes les pages filles
- Une page mère se juge à ses citations depuis des pages distinctes, dans le corps (repère : 5) ; jamais un total brut qui mélange navigation et contexte

## Sauvegarde

Output dans `wiki/maillage/YYYY-MM-DD-slug.md` dans le dossier de travail du projet.

## Concepts liés

`cocon-semantique` · `pagerank-interne` · `intention-recherche` · `cannibalisation` · `gsc-export`
