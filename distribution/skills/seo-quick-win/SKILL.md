---
name: seo-quick-win
description: "Quick wins depuis la GSC : pages en position 3-12 à CTR faible. « quick win », « gains rapides », « CTR faible »."
---

# Skill — Quick Win SEO

## Quand utiliser ce skill

Identification des opportunités SEO rapides depuis les données GSC : pages en position 3-12 avec impressions élevées et CTR sous-performant. Priorité optimisation existant > création de contenu. Pipeline en 6 étapes : filtrer (positions 3-15, exclure branded + homepage) → trier par impressions → calculer gap CTR → croiser avec intention → prioriser → lister leviers (title, méta, H1, FAQ top de page, densification atomique). Sortie obligatoire en plus du tableau : un rapport de pré-décision (diagnostic, preuves typées, état Critique / À améliorer / Sain, actions P1-P3 avec confiance, effort et risque, jamais de score affiché) ; sans lui le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "quick win", "gains rapides", "pages proches du top 3", "CTR faible", "pages position 3-12", quand un export GSC est uploadé.

## Quand déclencher

Pages en position 3-12, impressions élevées, CTR sous-performant. Priorité : optimiser l'existant avant de créer du contenu.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Export GSC Pages — URL, Clics, Impressions, CTR, Position (90j) | Oui |
| Contexte secteur | Recommandé |

Minimum viable : export GSC 30j minimum, position 4-15, tri impressions décroissant.

## Pipeline (6 étapes)

1. **Filtrer** — positions 3.0 à 15.0, exclure branded + homepage
2. **Trier** — top 10 par impressions décroissantes
3. **Estimer l'écart de CTR** — le CTR de référence est une **estimation**, jamais une perte certaine de clics. D'abord une référence interne : le CTR des pages du même site sur des segments comparables (même position, même type de requête, même appareil) quand la donnée le permet. Sinon la grille indicative (pos 4 ≈ 7 %, 5 ≈ 5 %, 6-10 ≈ 2-3 %), présentée comme hypothèse, avec sa source. Le rapport écrit « CTR inférieur à la référence », jamais « X clics perdus ».
4. **Croiser avec l'intention** — décisionnel P1 > transactionnel P2 > informationnel P3
5. **Prioriser** — d'abord le raisonnement business (page prioritaire, intention décisionnelle), puis l'écart de CTR, puis le volume comme départage entre deux actions. Le repère de 500 impressions par mois aide à choisir entre deux pages ; il n'élimine jamais une page commercialement importante qui en a moins.
6. **Lister les leviers** — title, méta, H1, FAQ top de page, densification atomique

## Sortie de pré-décision (obligatoire)

Ce skill n'a pas terminé tant que le rapport de pré-décision n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau, et il suit `audit-complet-v2/rapport-audit-seo-format.md` (`audit-complet-v2/rapport-audit-seo-format.md`). Fichier : `wiki/quick-wins/YYYY-MM-DD-slug-decision.md`.

Ce qu'il contient, dans cet ordre :

1. Diagnostic principal : une phrase, la cause structurante, pas une liste d'erreurs
2. Les chiffres à retenir : 3 à 5, ceux qui illustrent le diagnostic
3. État : Critique, À améliorer ou Sain, calculé sur l'impact SEO réel et le type de page, jamais sur le nombre d'erreurs ; jamais de score sur 10
4. Problèmes (3 maximum) et opportunités (5 maximum), séparés : chacun avec Preuve (2 à 4 données), Pourquoi c'est important, Action, Confiance (forte / moyenne / faible) ; chaque problème s'écrit en trois temps : observation prouvée → conséquence ou risque justifié → bénéfice attendu de la correction (l'observation seule n'est pas un frein SEO démontré)
5. Actions P1 / P2 / P3, 3 P1 maximum : pourquoi, preuve, signal attendu (jamais un résultat chiffré promis), dépendance préalable, test de validation (ce qui distingue « correction appliquée » de « résultat SEO observé »), effort faible / moyen / élevé (jamais en heures), confiance, risque low / medium / high ; toute action high (suppression, 301, fusion, changement d'URL) porte « À valider avant déploiement » et sa checklist
6. Ce que les données ne permettent pas de conclure, et « données insuffisantes » ou « ne rien faire » quand c'est le cas

Sur le périmètre de ce skill, le rapport tranche les opportunités (5 maximum) : requêtes réelles, brand / non-brand, type de SERP, data_strength (< 20 impressions données insuffisantes, 20-100 faible, 100-500 exploitable, 500+ solide), « CTR inférieur au benchmark indicatif » jamais un écart en points ; « avant modification : lire les requêtes dans la GSC ».

Règles : chaque information est typée FACT, HYPOTHESIS ou ACTION, jamais une hypothèse écrite comme un fait ; un problème existe une seule fois (ID), les observations qui parlent du même problème fusionnent ; une anomalie n'est pas une priorité par défaut ; les pages business et les tendances GSC passent avant les anomalies techniques secondaires ; jamais de recommandation automatique de fusion, 301, suppression, réécriture ou création de page ; Google n'est jamais anthropomorphisé. Phrases courtes, une donnée par diagnostic, aucune des phrases « Il est important de », « Il convient de », « Cela peut potentiellement », « Il est intéressant de noter », « Dans le cadre de ».

Restitution (corrections V2 du 23 septembre) : aucun ID technique ni mot anglais (low / medium / high) dans le rapport ; Faible / Moyen / Élevé partout ; la certitude affichée ne dépasse jamais la couverture des données (« aucun problème majeur détecté sur les URL inspectées », pas « Sain ») ; formulations précises (« URL en 404 avec encore des impressions ») ; aucune action proposée sur une page dont les requêtes ne sont pas connues (« à vérifier ») ; le nombre de mots seul n'est jamais un problème ; limites de longueur : diagnostic 70 mots, 4 chiffres, 3 problèmes de 40 mots, 6 actions, 3 opportunités de 35 mots, le reste dans les détails repliés.

Onglet Analyse technique, structure validée le 23 septembre 2026 (référence : [[audit/2026-09-22-organikk-co]]) : chaque priorité = une phrase de cadrage, « Ce qu'on observe » (faits chiffrés en liste, pages en code), « Pourquoi c'est prioritaire » (deux phrases), « Action » (liste numérotée courte), « Impact attendu » et « Risque » en gras ; puis le plan des 30 jours en trois paliers (Priorité immédiate, Deuxième étape, Priorité secondaire), une action par paragraphe en gras suivie d'une phrase ; puis « à surveiller avant d'agir » pour la page dont la cause n'est pas isolée ; puis « Autres pages à surveiller » : chiffres séparés par « · », une phrase, verdict en gras (« Aucune action recommandée », « À vérifier avant toute modification »).

## Output obligatoire

Tableau 5-10 pages + fiche action par page (min 2 actions dont 1 preuve atomique).

```
QUICK WIN — Top N Opportunités GSC
| # | URL | Position | Impressions | CTR réel | CTR de référence (source : interne / grille indicative) | Écart (estimation) | Intent |

→ Page /url
Action 1 : [type] — [description concrète]
Action 2 : Densification atomique — [avant/après]
```

## Règles absolues

- Ne pas proposer de nouveau contenu avant d'épuiser les quick wins existants
- Pas de conseils génériques sans URL concernée
- Ne pas confondre volume de recherche et impressions GSC
- Toujours inclure au moins 1 exemple avant/après de densification atomique
- Le CTR de référence est une estimation : jamais « X clics perdus », toujours la source de la référence (interne ou grille indicative)
- Le volume départage, il n'élimine pas : une page business sous 500 impressions reste dans l'analyse
- Des apparitions sans clic sur une page aux requêtes indisponibles ne sont pas un gain rapide. Une position moyenne agrège toutes les apparitions de la page : position 5 ne veut pas dire cinquième sur la recherche visée. Sans requêtes ni effectifs comparables, ne pas comparer le CTR à des pages de fonction différente, et ne pas conclure que le title est en cause. Le bloc s'appelle alors « Deux pages apparaissent dans Google sans générer de clic : ciblage à vérifier », avec les chiffres, sans estimation de gain dans le résumé client.
- Si les requêtes sont anonymisées, elles ne sont pas non plus dans l'interface Search Console : l'action est d'établir pourquoi elles ne remontent pas, puis d'analyser le ciblage depuis le contenu et les résultats Google. Jamais « lire les requêtes dans l'interface » comme préalable.

## Sauvegarde

Output dans `wiki/quick-wins/YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`preuve-atomique` · `grounding-score` · `intention-recherche` · `gsc-export`
