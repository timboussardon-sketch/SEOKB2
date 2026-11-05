---
type: methode
title: "Demande observée : un score de demande propriétaire sans volume d'outil"
slug: demande-observee
created: 2026-09-23
status: stable
confidence: medium
tags: [mots-cles, methode, doctrine]
---

## Nouvelles missions : opportunités business

Le contrat [[methodes/opportunites-business]] et le branchement [[methodes/opportunites-business-integration]] complètent cette référence pour `business-v1`. Ils remplacent les scores numériques de priorité business, les valeurs économiques par défaut et le calendrier sans capacité. Les diagnostics techniques et leur profondeur restent conservés. La synthèse des opportunités suit le contexte et le périmètre ; trois opportunités visibles, détail repliable. La collecte historique ne devient jamais un marché exhaustif.

Les méthodes et commandes ci-dessous décrivent aussi des dossiers historiques. Pour une nouvelle mission, utiliser les points d’entrée canoniques du contrat ; préserver les anciens livrables. Distinguer les requêtes mesurées, les besoins observés et les hypothèses ; ne pas additionner demande Google, questions et citations IA.


# Demande observée

Règle de Tim, 23 septembre 2026 : « pas de volume inventé » ne veut pas dire « aucun signal de demande ». Un mot-clé à forte intention et avec de la matière peut être cherché par 5 personnes ou par 500. On ne prétend pas « volume = 320 » ; on dit **demande observée : faible, moyenne ou forte**, construite à partir de signaux qu'on possède.

## Signaux

| Signal | Source | 0 point | 1 point | 2 points |
|---|---|---|---|---|
| Variantes Google Suggest qui contiennent le sujet | export Suggest du vault (`raw/data/keyword-research-*`) ou scrape | 0 | 1 à 4 | 5 et plus |
| Impressions Search Console sur les requêtes du sujet | API GSC, 90 jours | 0 | 1 à 19 | 20 et plus |
| Fréquence de la formulation dans les calls | `raw/transcripts/` | 0 à 2 calls | 3 à 6 | 7 et plus |
| Acteurs spécialisés qui tiennent la requête | DeepSearch web (phase 3 du workflow) | 0 | 1 ou 2 | 3 et plus |

Signaux à ajouter quand ils sont disponibles, même barème : People Also Ask (nombre de questions), autosuggest YouTube, Google Trends (tendance 12 mois), Keyword Planner s'il existe (alors le volume s'affiche, en plus du score, avec sa source).

## Pas de verdict agrégé (correction du 24 septembre)

Les signaux s'affichent **séparément**, jamais additionnés en « faible / moyenne / forte » : 96 variantes Suggest peuvent venir de formulations très proches, 5 acteurs mesurent la présence concurrentielle, pas la demande. Un signal non mesuré s'écrit « non mesuré ». Seules les impressions Search Console disent qu'une requête est réellement tapée et que le site y apparaît ; on peut écrire « demande confirmée par la Search Console » à partir de 20 impressions, rien d'autre.

## Ce que ça change dans la décision

- Intention forte + matière + aucun signal de demande = terrain vide : « à confirmer », mesure GSC à J+90.
- Signaux de demande présents + intention faible = trafic sans lead : pas de page pour le clic ; traitement GEO citation si on veut être la source.
- La matière se qualifie par type (objection, cas concret, méthode, preuve, résultat, verbatim), jamais en occurrences : [[methodes/rapport-mots-cles-format]].

## Où le score apparaît

Colonnes de signaux (Suggest, GSC, calls, acteurs) dans le tableau scoré de `kw-research-workflow` (phase 6), dans la sortie de `seo-recherche-mots-cles`, dans la décision par cluster du rapport de pré-décision mots-clés. Le calcul est un script, pas un jugement : `jev/` ou le scratchpad de session, signaux en entrée, niveau en sortie.
