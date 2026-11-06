---
name: seo-mots-cles-overview
description: "Matrice objectif × secteur d'un terme-pilier pour les AI Overviews. « se placer sur [terme] », « mot-clé overview »."
---

# Skill — Spécialiste Mot-Clé OVERVIEW (GEO)

## Quand utiliser ce skill

Spécialiste mot-clé OVERVIEW (GEO / Google AI Overviews). Cartographie l'univers de mots-clés d'un terme-pilier concurrentiel (« agent », « consultant », « logiciel »…) en croisant DEUX axes : l'objectif principal (tous les buts / jobs-to-be-done de la personne) × le secteur d'activité (toutes les verticales). Sort une matrice objectif × secteur, chaque croisement qualifié sur son potentiel d'être cité en AI Overview / réponse LLM. Brique AMONT du workflow mots-clés : sa matrice alimente seo-recherche-mots-cles → seo-clustering-mots-cles → seo-mots-cles-decisionnels.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "se placer sur [terme]", "spécialiste mot-clé overview", "matrice objectif secteur", "cartographie mot-clé", "tous les objectifs et tous les secteurs", "univers de mots-clés d'un terme-pilier", "comment ranker sur un mot générique/concurrentiel", "être cité en AI Overview sur [terme]", "GEO sur le mot [terme]".

## Quand déclencher

Un terme-pilier générique et concurrentiel (« agent », « consultant », « logiciel », « formation »…) est trop large pour être attaqué frontalement. On ne rank pas sur « agent » ; on rank en couvrant **tout l'univers** que le mot recouvre. Ce skill construit cet univers en croisant deux axes, puis qualifie chaque croisement pour la visibilité dans les **AI Overviews et les réponses génératives (GEO)**.

C'est la **première brique** du workflow mots-clés quand on part d'un mot-pilier large. Sa matrice devient la matière de `seo-recherche-mots-cles`.

## Doctrine

- **GEO d'abord.** OVERVIEW = Google AI Overviews / SGE, SearchGPT, Perplexity, citations LLM. Jamais SEO local. L'objectif n'est pas seulement de ranker, c'est d'**être la source citée** dans la réponse générée.
- **On ne rank pas sur le pilier, on rank sur ses croisements.** Le mot « agent » seul est ingagnable et sans intention. « Agent IA pour prospecter dans l'immobilier » est gagnable, intentionné, et citable.
- **Deux axes, jamais un seul.** Un mot-clé de valeur est toujours un objectif × un secteur. Sortir un axe sans l'autre produit une liste plate qui rate la moitié de l'univers.
- **Exhaustivité des deux axes avant tout croisement.** On génère d'abord TOUS les objectifs, puis TOUS les secteurs, ensuite on croise. Générer large, filtrer après.
- **Le vault décide.** Objectifs et secteurs s'ancrent sur la data réelle (verbatims, GSC, corpus). Le vault mince = on le signale, on n'invente pas de secteurs fantômes.
- **Volume optionnel** (décision Tim, 2026-09-16) : affiché seulement s'il vient d'une donnée réelle, jamais estimé. Difficulté et potentiel AI Overview = proxys déclaratifs, jamais des chiffres inventés.

## Le principe de la matrice — 2 axes

```
                 SECTEUR D'ACTIVITÉ  →
                 immobilier | e-commerce | avocat | SaaS | santé | …
OBJECTIF ↓
rédiger            agent IA rédaction immobilier | …
prospecter         agent IA prospection immobilier | …
support client     agent IA SAV e-commerce | …
prise de RDV       …
veille / analyse   …
…
```

Chaque cellule = un mot-clé candidat = **un terme-pilier + un objectif + un secteur**. La valeur du skill est de rendre les DEUX axes exhaustifs avant de croiser.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Terme-pilier (le mot générique visé : « agent », « consultant »…) | Oui |
| Marché géo + langue | Oui |
| Offre / point de conversion (pour qualifier le funnel plus tard) | Recommandé |
| Verbatims Reddit / avis / support (pour ancrer les objectifs réels) | Recommandé — rend l'axe Objectif crédible |
| Export GSC / Keyword Planner si dispo | Recommandé — révèle secteurs et objectifs déjà performants |

## Pipeline (6 étapes)

1. **Isoler le terme-pilier + son objectif racine.** Que veut fondamentalement la personne qui tape ce mot ? (« agent » → déléguer une tâche à une IA autonome). C'est le sens qui contraint les deux axes.

2. **Axe OBJECTIF PRINCIPAL — exhaustif.** Lister tous les buts / jobs-to-be-done que la personne poursuit avec le pilier. Sources : verbatims réels, patterns « pour + verbe », People Also Ask, cas d'usage du corpus. Viser **15 à 30 objectifs** avant tri. Ex. pour « agent » : rédiger, prospecter, répondre au support, qualifier des leads, prendre des RDV, faire de la veille, analyser des données, automatiser un workflow, traduire, modérer…

3. **Axe SECTEUR D'ACTIVITÉ — exhaustif.** Lister toutes les verticales / métiers qui achètent le pilier. Sources : secteurs présents dans le corpus, clients existants, PAA « pour [métier] ». Viser **15 à 40 secteurs** avant tri. Ex. : immobilier, e-commerce, avocat, expert-comptable, restaurant, SaaS B2B, santé, assurance, RH, artisan…

4. **Croiser en matrice.** Objectif × Secteur. Ne pas tout garder : couper les cellules absurdes (objectif incompatible avec le secteur) et les doublons sémantiques. Garder les croisements plausibles où une audience réelle cherche.

5. **Qualifier chaque croisement retenu (GEO).** Pour chaque cellule shortlistée :
   - **Intention** : Know-Simple / Know / Do (cf. `seo-cluster-aeo`).
   - **Potentiel AI Overview** : ce croisement déclenche-t-il probablement une réponse générée (Fort / Moyen / Faible) — proxy déclaratif, jamais présenté comme certitude. Les Know-Simple et comparatifs (« meilleur agent IA pour X », « comment automatiser Y ») déclenchent le plus souvent un AI Overview.
   - **Angle de citation** : ce qu'il faut fournir pour ÊTRE la source citée (définition nette, donnée originale, comparatif, procédure pas-à-pas). Cf. `seo-entites-vectorielles` / `seo-geo-audit`.

6. **Livrable + passage de relais.** Sortir la matrice + la shortlist priorisée, puis passer la main à `seo-recherche-mots-cles` (qui fera l'expansion longue traîne de chaque croisement retenu).

## Sortie de pré-décision (obligatoire)

Ce skill est une étape du workflow mots-clés complet (`.seokb/base/wiki/methodes/workflow-mots-cles-complet.md`). Sa sortie porte un `statut_decision` (RAW, HYPOTHÈSE, VALIDÉ, OBSOLÈTE, BLOQUÉ) et nourrit le rapport de pré-décision, seule sortie visible du workflow ; toute sortie de ce skill qui contredit ce rapport devient OBSOLÈTE. Format complet : `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`.

Ce que le rapport de pré-décision rend, et que ce skill doit rendre possible sur son périmètre :

1. Diagnostic en trois lignes.
2. Pré-décision par marché (5 max) : Marché / Page / Score business sur 5 (intention 0-2, proximité offre 0-2, conversion directe 0-1) / Docs du vault (documents qui traitent le sujet, par type : transcripts, clients, notes, wiki) / Matière qualifiée (objection, cas, méthode, preuve, résultat, verbatim) / SERP (compatible, à vérifier, non vérifiée) / Pré-décision (utiliser, renforcer l'existant, créer, conserver et enrichir, analyser avant restauration, candidat avec validation SERP requise, bloqué, attendre).
3. Ce qui est bloqué, et par quoi : statut, raison, actions autorisées, actions interdites ; « décision stratégique requise » quand c'est le positionnement (c'est la décision de Tim) ; « pré-décision impossible avant analyse SERP de N requêtes » sinon. Jamais « à trancher ».
4. À ne pas produire maintenant.
5. Fiabilité, une ligne ; analyse technique derrière ; logs du workflow en annexe.

Règles : signaux de demande séparés (Suggest, Search Console, calls, acteurs), jamais agrégés en verdict, aucun volume estimé ; matière comptée en documents du vault puis qualifiée par lecture, jamais en occurrences d'un mot ; « cannibalisation » interdit sans SERP ni conflit GSC, « chevauchement potentiel à vérifier » ; une requête secondaire sert à repérer une sous-intention, jamais à placer un title, un H2 ou une FAQ par défaut ; aucune page sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un cas ou un relevé réel par page programmatique ; scores /10 en backend ; Faible / Moyen / Élevé, jamais d'anglais ; la certitude affichée ne dépasse jamais la couverture des données.

## Output obligatoire

```
OVERVIEW MOT-CLÉ — terme-pilier : '[agent]'   ([marché] · [langue])
Objectif racine : [ce que la personne veut fondamentalement]

AXE OBJECTIFS ([n]) : rédiger · prospecter · support · RDV · veille · …
AXE SECTEURS ([n])  : immobilier · e-commerce · avocat · SaaS · santé · …

MATRICE PRIORISÉE
| Croisement (mot-clé) | Objectif | Secteur | Intention | AI Overview | Angle de citation |
|---|---|---|---|---|---|
| agent IA rédaction pour l'immobilier | rédiger | immobilier | Know | Fort | Procédure + exemple de fiche générée |
| meilleur agent IA prospection e-commerce | prospecter | e-commerce | Know/Do | Fort | Comparatif chiffré |
| … | | | | | |

Synthèse : [n] objectifs × [n] secteurs → [n] croisements retenus
Top croisements GEO (fort potentiel de citation) : [liste]
Prochaine étape : seo-recherche-mots-cles sur les [n] croisements retenus.
```

## Règles absolues

- **Toujours les deux axes.** Un livrable OVERVIEW sans axe Objectif OU sans axe Secteur est incomplet et se refait.
- **Exhaustivité d'abord** : générer chaque axe large (15-30 objectifs, 15-40 secteurs) avant de croiser et couper.
- **GEO, pas local.** « OVERVIEW » = AI Overviews génératifs. Ne jamais dériver vers le SEO géographique.
- **Volume optionnel** : seulement depuis une donnée réelle, jamais estimé. Difficulté et potentiel AI Overview restent des proxys déclaratifs, jamais des chiffres inventés. Si un export d'outil est fourni, utiliser SES chiffres.
- **Ancrer sur le réel.** Objectifs et secteurs viennent des verbatims / du corpus / de la GSC quand ils existent. Vault mince = le signaler, pas combler au hasard.
- Ne pas faire l'expansion longue traîne ici : c'est le rôle de `seo-recherche-mots-cles` en aval. Ce skill cadre l'univers, il ne le déroule pas.

## Enchaînement workflow

`seo-mots-cles-overview` (cette matrice, AMONT) → `seo-recherche-mots-cles` (expansion + qualification de chaque croisement) → `seo-clustering-mots-cles` (regroupe en pages) → `seo-mots-cles-decisionnels` (isole les convertisseurs) → `seo-cluster-aeo` / `seo-brief-contenu` / `seo-programmatique-pseo`.

Complémentaire : `seo-programmatique-pseo` et `seo-modeles-pseo` quand la matrice objectif × secteur est assez dense pour devenir un template pSEO (une page par cellule).

## Sauvegarde

Output dans `wiki/keywords/overview-YYYY-MM-DD-slug.md` selon le hook §7 AGENTS.md, puis update `wiki/index.md` + `wiki/log.md`.

## Concepts liés

`know-simple-know-do` · `ai-overview` · `geo` · `grounding-score` · `triade-serp` · `rag-structurer` · `clustering-mots-cles` · `mots-cles-decisionnels` · `pseo`
