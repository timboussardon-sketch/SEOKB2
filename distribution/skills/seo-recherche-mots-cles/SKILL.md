---
name: seo-recherche-mots-cles
description: "Recherche de mots-clés depuis une thématique, avec intention et difficulté. « recherche de mots-clés », « keyword research »."
---

# Skill — Recherche de Mots-Clés

## Quand utiliser ce skill

Recherche de mots-clés from scratch : partir d'une thématique ou de quelques seed keywords et produire une liste exhaustive, qualifiée et priorisée — chaque mot-clé avec son intention et sa difficulté. Pipeline en 5 étapes : cadrer la thématique → expansion sémantique → qualification (intention/difficulté) → filtrage du bruit → tableau priorisé. Règle : volume optionnel (affiché seulement s'il vient d'une donnée réelle, jamais estimé), difficulté jamais inventée.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "recherche de mots-clés", "trouve-moi des mots-clés", "keyword research", "liste de mots-clés sur [thème]", "quels mots-clés cibler", "explore les requêtes sur", "j'ai une thématique, sors les mots-clés", "expansion de mots-clés".

## Quand déclencher

Partir d'une thématique ou de seed keywords et produire une liste de mots-clés exhaustive, qualifiée et priorisée. C'est l'amont de tout : tant que la liste n'existe pas, ni le clustering ni le brief n'ont de matière.

## Doctrine

- **Colonne Volume optionnelle** (décision Tim, 2026-09-16, qui remplace l'interdiction précédente) : le volume peut figurer dans le livrable si les chiffres viennent d'une donnée réelle (GSC, Keyword Planner, Ahrefs, Semrush). Sans donnée réelle, pas de colonne plutôt qu'un chiffre estimé. La difficulté reste un proxy déclaratif, jamais un chiffre inventé.
- On ne part pas des concurrents. On part de l'intention de l'audience et de l'offre.
- Un mot-clé sans intention claire n'est pas un mot-clé, c'est du bruit.
- Exhaustivité d'abord, tri ensuite : générer large, filtrer après.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Thématique ou 3-5 seed keywords | Oui |
| Secteur + audience / persona | Oui |
| Offre (ce qu'on vend, point de conversion) | Oui — sinon le funnel est inqualifiable |
| Marché géo + langue | Oui |
| Export GSC / Ahrefs / Semrush si dispo | Recommandé — rend les volumes réels |

## Pipeline (5 étapes)

1. **Cadrer** — thématique, périmètre, ce qui est dans le scope et ce qui en sort.
2. **Expansion sémantique** — pour chaque seed, générer :
   - modificateurs (comment, pourquoi, prix, avis, meilleur, vs, sans…)
   - questions (patterns People Also Ask)
   - longue traîne (3 mots et plus)
   - co-occurrences et entités liées
   - synonymes et variantes lexicales
   Objectif : **50 à 150 mots-clés bruts** minimum avant tri.
3. **Qualifier chaque mot-clé** — intention (Know-Simple / Know / Do, cf. `seo-cluster-aeo`), difficulté estimée (proxy : nb de mots, présence de marques, type de SERP), étage de funnel. (Volume : optionnel, uniquement depuis une donnée réelle.)
4. **Filtrer le bruit** — retirer hors-sujet, hors-intention vs l'offre, doublons stricts, requêtes branded concurrent non pertinentes.
5. **Livrable** — tableau priorisé.

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
RECHERCHE MOTS-CLÉS — '[Thématique]'

| Mot-clé | Intention | Difficulté | Funnel | Demande observée | Note |
|---|---|---|---|---|---|
| ... | Know | Moyenne | Know | moyenne (Suggest 12 · GSC 0 · calls 4 · acteurs 2) | ... |
| ... | Do | Élevée | Pré-décision | forte (Suggest 40 · GSC 56 · calls 9 · acteurs 5) | ... |

Synthèse : [nb total] mots-clés · [nb] Do · [nb] Know · [nb] Know-Simple
Top 5 à prioriser : [liste]

RAPPORT DE DÉCISION (obligatoire, voir « Sortie de pré-décision ») : diagnostic, chiffres, état, P1/P2/P3 avec preuve, confiance, effort, risque. Aucun score affiché.
```

## Règles absolues

- Deux scores affichés par mot-clé ou cluster (`.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : score business sur 5 avec ses composantes (intention 0-2, proximité offre 0-2, conversion directe 0-1) et score matière = nombre de documents du vault qui traitent le sujet (≥ 3 occurrences du champ lexical), par type de source (transcripts, clients, notes, wiki). Le comptage dit où chercher ; le verdict de matière vient de la lecture par type. Zéro document = pas de page.
- Gouvernance des pré-décisions (24 septembre, `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : une pré-décision finale par cluster avec statut VALIDÉ / À VÉRIFIER / BLOQUÉ / REJETÉ ; les sorties de ce skill sont des HYPOTHÈSES tant que le rapport n'a pas tranché, et deviennent OBSOLÈTES si elles le contredisent ; aucune page créée sans validation SERP + matière suffisante ; aucun brief avant une pré-décision URL VALIDÉ ; un candidat à la création reste « validation SERP requise » ; les scores /10 restent en backend, le rapport lit adéquation offre, intention, preuve, SERP, décision.
- Sortie finale du workflow (règles du 24 septembre, `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`) : une pré-décision URL par cluster (utiliser / renforcer l'existant / créer / conserver / analyser avant restauration / à confirmer après validation SERP) ou la raison explicite pour laquelle on ne peut pas encore décider (« Décision stratégique requise » pour le positionnement, « Pré-décision impossible avant analyse SERP de N requêtes ») ; jamais « à trancher ». Signaux de demande affichés séparément, jamais agrégés en verdict. Matière qualifiée par type (objection, cas concret, méthode, preuve, résultat, verbatim), jamais comptée en occurrences. « Cannibalisation » interdit sans SERP ni conflit GSC : « chevauchement potentiel à vérifier ». Une requête secondaire sert à repérer une sous-intention, jamais à placer un title, un H2 ou une FAQ par défaut.
- Signaux de demande obligatoires sur chaque mot-clé, affichés séparément et jamais agrégés en niveau : signaux possédés (variantes Google Suggest, impressions Search Console, fréquence dans les calls, acteurs spécialisés ; People Also Ask, YouTube, Trends quand disponibles), signaux bruts affichés à côté du niveau. Jamais un volume estimé ; un volume réel (Keyword Planner) s'affiche en plus, avec sa source. Méthode : `audit-complet-v2/demande-observee.md`.
- Le rapport de pré-décision fait partie de la sortie. Sans lui, le skill n'a pas terminé. Il se rédige à partir du tableau, aucune phrase sans mot-clé ou chiffre derrière, aucun score affiché.
- **Volume optionnel** (décision Tim, 2026-09-16) : affiché seulement s'il vient d'une donnée réelle, jamais estimé. Difficulté = proxy déclaratif, jamais un chiffre inventé.
- Si un export d'outil est fourni, utiliser **ses** chiffres, ne jamais les arrondir ni les estimer au hasard.
- Générer large (50+ avant filtrage), livrer trié.
- Chaque mot-clé a une intention identifiée, ou il dégage de la liste.

## Enchaînement workflow

`seo-recherche-mots-cles` (cette liste) → `seo-clustering-mots-cles` (regroupe en pages) → `seo-mots-cles-decisionnels` (isole les convertisseurs) → `seo-brief-contenu` / `seo-cluster-aeo` / `seo-programmatique-pseo`.

## Sauvegarde

Output dans `wiki/keywords/recherche-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`know-simple-know-do` · `funnel` · `rrf` · `clustering-mots-cles` · `mots-cles-decisionnels` · `brief-contenu`
