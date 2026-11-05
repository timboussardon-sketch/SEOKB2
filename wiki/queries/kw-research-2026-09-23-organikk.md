---
statut_decision: RAW
type: query
category: keywords
title: "Workflow recherche mots-clés complet, organikk.co, 23 septembre 2026"
slug: kw-research-2026-09-23-organikk
created: 2026-09-23
site: https://organikk.co/
skill: kw-research-workflow
status: draft
confidence: medium
---
> **Statut : RAW.** Sortie amont du workflow mots-clés. La pré-décision finale est dans [[keywords/2026-09-23-organikk-rapport-decision]] ; ce fichier ne peut pas la contredire. La colonne « demande observée » a été retirée : signaux séparés seulement. La phase 5 (modèles pSEO) est réduite par la règle « un cas ou un relevé réel par page ».


# Workflow recherche mots-clés : organikk.co

Orchestrateur `kw-research-workflow` ([[raw/notes/skill-kw-research-workflow]]), 7 phases, puis les 3 skills additionnels et le rapport de pré-décision [[keywords/2026-09-23-organikk-rapport-decision]].

## Phase 0 : Cadrage

| Question | Réponse (source vault) |
|---|---|
| Secteur | SEO et GEO pour entreprises B2B, consultant + système IA ([[entities/organikk-co]]) |
| Offre principale | accompagnement SEO + GEO 3 mois (30 pages business + agent IA), coaching 1:1 ; point de conversion « Réserver un appel » |
| Persona | CMO, fondateur B2B, Head of Growth ; cycle long ; France, ancrage Lyon |
| Keyword Planner | absent. Substitut : Google Suggest FR du 2 mai 2026, 2 587 suggestions, `count` = récurrence dans Suggest, pas un volume ([[raw/data/keyword-research-2026-05-02/keywords-classified]]) |
| GSC 90 jours | oui, API, 24 juin au 21 septembre ([[audit/2026-09-22-organikk-co-phase0-positionnement]]) |
| Verbatims | 24 transcripts de calls prospects et clients dans `raw/transcripts/` |

## Phase 1 : Keyword Planner (substitut Suggest)

Volume et CPC : N/A sur toute la liste. Suggestions retenues (hors requêtes anglophones et hors marques d'autres agences) :

| Suggestion | Récurrence Suggest | Intention |
|---|---|---|
| agence seo saas b2b | 4 | Do |
| seo ia geo | 2 | Know |
| seo ia chatgpt | 2 | Know-décisionnel |
| seo vs chatgpt optimization | 2 | Know |
| saas seo consultant | 2 | Do |
| tarif audit seo wordpress | 2 | Do |
| geo vs seo (variantes) | 3 à 4 | Know |

L'export est dominé par des requêtes anglophones AEO/GEO (934 sur 2 587) : une seule requête business française à récurrence 4, « agence seo saas b2b ».

## Phase 2 : Search Console

Quick wins (`seo-quick-win`, [[quick-wins/2026-09-22-organikk-co]]) : /methode/ position 5,5 et 78 impressions, /systeme/ 5,6 et 53, /avis/ 2,1 et 50, /tarifs/ 2,6 et 23 ; requêtes anonymisées, à lire dans l'interface avant action.

Cannibalisation (`seo-cannibalisation`, [[cannibalisation/2026-09-22-organikk-co]]) : aucune confirmée ; chevauchements potentiels sur l'accompagnement 1:1 (4 pages), l'audit (2), la prestation (2).

Content gaps (impressions > 100 sans page dédiée) : aucun. La seule requête au-dessus de 50 impressions est « timothée boussardon » (66, marque). Requêtes business visibles : « bootcamp seo » 56 impressions position 28,6, « agence seo b2b » 5 impressions position 34, « ethical seo agency » 10 impressions sur une URL redirigée. Tag `content_gap` : aucun.

## Phase 3 : DeepSearch web (4 recherches séquentielles, 23 septembre)

Search 1, consensus : le GEO est défini partout comme « être cité dans les réponses de ChatGPT, Perplexity, Gemini » ; une agence GEO vend audit de visibilité IA, optimisation des contenus existants, contenus answer-first, entités et schémas, suivi du trafic IA (webconversion.fr, seo.fr, searchbooster.fr, agenceseoia.fr, agenceonze.fr).

Search 2, terrain : 90 % des sites invisibles dans ChatGPT selon une étude citée par seo.fr ; premiers résultats annoncés en 4 à 8 semaines, citations stables en 3 à 6 mois ; trafic ChatGPT annoncé à 11,4 % de conversion contre 5,3 % en organique (seo.fr, quatrys.fr, 2magency.com). Chiffres d'agences, non vérifiés à la source.

Search 3, études récentes : paper « From Citation Selection to Citation Absorption » (Zhang, He, Yao, 2026) ; tests Mamie GEO sur 50 marques B2B françaises et 100 prompts, mars à avril 2026 ; Perplexity cite plus, Gemini favorise les sources indexées Google (mamie-geo.fr, e-strategic.fr, hi-commerce.fr, hubfi.fr).

Search 4, synthèse :

| Angle | Source consensus | Source contradiction | Pourquoi c'est un gap |
|---|---|---|---|
| « consultant GEO » | toutes les pages parlent d'« agence GEO » | la SERP « consultant geo » est occupée par des cabinets de géotechnique | aucun consultant SEO ne tient la requête, terrain vide en français |
| preuve chiffrée d'une citation obtenue | promesses de résultats en 4 à 8 semaines | aucune agence ne montre un avant / après cité | un cas client d'Organikk avec citations mesurées ([[project/chatgpt-tracker]]) serait unique |
| système transféré au client | les agences vendent une prestation continue | aucune ne vend « vous repartez avec l'agent » | angle propre à l'offre, aucune page marché |
| SEO qui ramène des leads, pas du trafic | tout le marché parle de visibilité | rien sur la mesure email entrant | vocabulaire des transcripts (« nombre de leads » dans 7 calls) |

Tag `angle_exclusif` : consultant geo, être cité par chatgpt (preuve), agent seo qui vous appartient, seo lead gen b2b.

## Phase 4 : Données propriétaires (24 transcripts)

Formulations présentes dans 3 transcripts ou plus (comptage automatique, puis lecture) :

| Formulation | Transcripts | Occurrences | Tag |
|---|---|---|---|
| créer du contenu / création de contenu | 16 et 14 | 58 | verbatim_client |
| mots-clés business | 13 | 42 | verbatim_client |
| cas clients | 14 | 51 | verbatim_client |
| trouver des mots-clés | 10 | 19 | verbatim_client |
| créer des pages | 9 | 25 | verbatim_client |
| nombre de leads / leads par mois | 7 et 4 | 20 | verbatim_client |
| trouver des clients | 7 | 8 | verbatim_client |
| agence seo | 6 | 17 | verbatim_client |
| système seo | 7 | 10 | verbatim_client |
| consultant seo | 5 | 6 | verbatim_client |
| modèle de page(s) | 4 | 21 | verbatim_client |

Pain points en langage naturel : « je n'ai pas le temps » (3 calls, dont un prospect qui a testé plusieurs outils SEO sans creuser) ; « les clients veulent des résultats concrets, ça leur parle moins » ; « le trafic a tellement baissé sur mes pages » ; « tu as 15 leads, mais est-ce que ça convertit ? ». Gmail et LinkedIn : non scannés.

Mots-clés longue traîne dérivés des verbatims : « trouver des mots-clés business », « créer des pages qui ramènent des leads », « combien de leads par mois avec le seo », « système seo pour consultant », « agence seo qui montre ses cas clients ».

## Phase 5 : Modèles pSEO (`seo-modeles-pseo`)

MODÈLES pSEO : Money Page : « accompagnement SEO + GEO » (/accompagnement-seo-geo/)
Point de conversion : appel de 30 minutes

| Catégorie | Requête cible | Intention | Score business /10 | Format de page | Ancre vers la Money Page |
|---|---|---|---|---|---|
| Secteur | agence seo saas b2b | choisir un prestataire qui connaît le secteur | 8 | page secteur (modèle /secteurs/avocat/) | « l'accompagnement SEO + GEO » |
| Secteur | agence seo avocat, agence seo hôtel | idem | 7 | pages secteurs existantes, aujourd'hui redirigées | idem |
| Pricing | agence seo prix, tarif agence seo | connaître le budget | 7 | /tarifs/ existante, FAQ « combien coûte » | « voir les tarifs » |
| Best option | agence seo ou consultant seo | trancher le format | 6 | page comparatif sans acteur nommé | « notre approche » |
| Switch | changer d'agence seo | quitter un prestataire | 8 | page dédiée, matière à collecter | « reprendre votre SEO » |
| Preuve | être cité par chatgpt (cas client) | vérifier que ça marche | 7 | étude de cas avec citations mesurées | « consultant GEO » |
| Comment | comment trouver des mots-clés business | faire soi-même | 4 | guide, alimente le bootcamp | « le système SEO » |

Top 3 spokes à créer en premier : secteur SaaS B2B (matière 7 transcripts, modèle existant), preuve « cité par ChatGPT » (angle exclusif, tracker en place), changer d'agence (quand deux verbatims au moins existent). Maillage : chaque spoke vers /accompagnement-seo-geo/, la Money Page liste les spokes.

## Phase 6 : Livrable scoré

Volume, CPC, YoY : N/A (pas de Keyword Planner). Intérêt business : décisionnelle 5, transactionnelle 4, info 2 à 3 ; +1 verbatim_client, +1 content_gap. Difficulté : position GSC (top 3 = 1, 4 à 10 = 2, 11 à 20 = 3, hors top 20 = 4, aucune page = 5). Fichier : [[keywords/annexes/kw-research-2026-09-23-organikk.csv]].

| Mot-clé | Volume | CPC | Intérêt business | Difficulté | YoY | Signaux de demande (Suggest · GSC · calls · acteurs) | Tag |
|---|---|---|---|---|---|---|---|
| agence seo geo | N/A | N/A | 5 | 5 | N/A | 98 · 4 · 4 · 5 | angle_exclusif |
| consultant geo | N/A | N/A | 5 | 4 | N/A | 0 · 4 · 0 · 0 | angle_exclusif |
| agence seo ia | N/A | N/A | 5 | 5 | N/A | 96 · 3 · 21 · 5 | kp |
| changer d'agence seo | N/A | N/A | 5 | 5 | N/A | 0 · 0 · 1 · 3 | kp |
| agence seo saas b2b | N/A | N/A | 5 | 5 | N/A | 70 · 0 · 5 · 4 | kp |
| agence seo b2b | N/A | N/A | 5 | 4 | N/A | 37 · 5 · 8 · 5 | gsc_qw |
| bootcamp seo | N/A | N/A | 4 | 4 | N/A | 0 · 72 · 17 · 3 | gsc_qw |
| agence seo prix | N/A | N/A | 4 | 2 | N/A | 4 · 0 · 24 · 4 | kp |
| être cité par chatgpt | N/A | N/A | 4 | 5 | N/A | 2 · 3 · 12 · 3 | angle_exclusif |
| mots-clés business | N/A | N/A | 4 | 5 | N/A | 0 · 0 · 13 · 0 | verbatim_client |
| seo qui ramène des leads | N/A | N/A | 4 | 2 | N/A | 13 · 0 · 10 · 2 | verbatim_client |
| agence seo ou consultant seo | N/A | N/A | 4 | 5 | N/A | 0 · 3 · 0 · 1 | kp |
| système seo pour consultant | N/A | N/A | 4 | 3 | N/A | 0 · 0 · 7 · 0 | verbatim_client |
| agence seo avocat | N/A | N/A | 4 | 5 | N/A | 2 · 2 · 5 · 2 | kp |
| agence seo hôtel | N/A | N/A | 4 | 5 | N/A | 0 · 2 · 3 · 2 | kp |
| formation seo pour dirigeant | N/A | N/A | 3 | 5 | N/A | 1 · 0 · 3 · 3 | kp |
| comment trouver des mots-clés business | N/A | N/A | 3 | 5 | N/A | 0 · 0 · 10 · 1 | verbatim_client |
| agence seo sans engagement | N/A | N/A | 3 | 5 | N/A | 0 · 0 · 2 · 1 | kp |
| comment choisir une agence seo | N/A | N/A | 2 | 5 | N/A | 0 · 0 · 6 · 5 | kp |
| agence seo éthique | N/A | N/A | 2 | 4 | N/A | 0 · 11 · 4 · 1 | gsc_qw |

Signaux de demande affichés séparément ([[methodes/demande-observee]]) : variantes Suggest, impressions GSC 90 jours, calls sur 24 qui portent le sujet, acteurs spécialisés en DeepSearch. Aucun verdict agrégé. People Also Ask, YouTube et Trends : non mesurés.

Part des mots-clés issus des phases 3 et 4 : 8 sur 20. Critère de qualité (30 %) atteint.

## Phase 7 : Synthèse

```
TOP 3 QUICK WINS         : /methode/ (5,5 · 78 imp.), /systeme/ (5,6 · 53), /tarifs/ (2,6 · 23), requêtes à lire dans l'interface
TOP 3 ANGLES EXCLUSIFS   : consultant geo, être cité par chatgpt (preuve mesurée), agent seo qui vous appartient
TOP 3 VERBATIMS CLIENT   : mots-clés business, nombre de leads par mois, créer des pages
MODÈLE pSEO PRIORITAIRE  : page secteur SaaS B2B (modèle existant, 7 transcripts, effort faible)
LIVRABLE                 : wiki/keywords/annexes/kw-research-2026-09-23-organikk.csv + rapport de pré-décision
```

## Suite du workflow

`seo-recherche-mots-cles` → `seo-clustering-mots-cles` → `seo-mots-cles-decisionnels` : sorties du 31 juillet, toujours valides, complétées par les tags ci-dessus ([[keywords/recherche-2026-07-31-agence-seo-organikk]], [[keywords/clusters-2026-07-31-agence-seo-organikk]], [[keywords/decisionnels-2026-07-31-agence-seo-organikk]]). Rapport de pré-décision : [[keywords/2026-09-23-organikk-rapport-decision]]. Ensuite `seo-brief-contenu` sur le pivot retenu.
