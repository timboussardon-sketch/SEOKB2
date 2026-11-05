---
title: "Skills additionnels Semaine 3 — Workflow mots-clés (recherche, clustering, décisionnels)"
bootcamp: 4
semaine: 3
type: skill-distribuable
usage: "Bundle Drive S3 — 3 skills neufs hors pack des 9, optionnels. Outillent la démo J5 « mots-clés anti-ChatGPT » et l'horizon « Mois 2-3 » du plan d'audit. À mettre sur le Drive + message WhatsApp en bonus, pas en prérequis bloquant."
related:
  - "[[sequencage-semaine-3]]"
  - "[[workflow-audit-bootcamp4]]"
  - "[[session-1-mots-cles-nouveautes]]"
---

# Skills additionnels S3 — Workflow mots-clés

Trois skills qui s'enchaînent pour transformer une thématique en pages qui rankent **et** qui convertissent. Ils ne servent pas l'audit lui-même (J1-J4). Ils servent ce qui vient **après** : la démo du call J5 (« mots-clés anti-ChatGPT ») et l'horizon « Mois 2-3 : nouvelles pages sur les gaps » du plan d'action.

> ℹ️ Ces 3 skills sont **neufs** (créés mai 2026) et **hors pack des 9** de la S1. Optionnels pour boucler l'audit. Mais ce sont eux qui transforment l'horizon « Mois 2-3 » du rapport en backlog concret, et qui te font suivre la démo du call en live. Installe-les avant le J5 si tu veux dérouler la démo en même temps que moi.

## Le workflow en un coup d'œil

```
seo-recherche-mots-cles    → thématique → 50-150 mots-clés qualifiés (intention + volume + difficulté)
        ↓
seo-clustering-mots-cles   → la liste → clusters exploitables (1 cluster = 1 page)
        ↓
seo-mots-cles-decisionnels → les clusters → les requêtes qui convertissent vraiment
        ↓
article-engine-pipeline (S2) / seo-brief-contenu / seo-cluster-aeo
```

Une brique nourrit la suivante. La recherche sort la matière, le clustering la découpe en pages, le décisionnel isole ce qui rapporte. Chaque brique sort aussi un doc final d'une page avec un score. La sortie repart dans le moteur de rédaction de la S2.

## Doc final résumé + score

Chaque skill sort, en plus de son tableau, un doc final d'une page avec un score (section « Output obligatoire » de chaque skill ci-dessous). Le dernier de la chaîne, `seo-mots-cles-decisionnels`, sort le doc qui entre dans `article-engine-pipeline`. Sans ce doc, le workflow n'est pas terminé.

## Pourquoi « additionnels » et pas dans le workflow audit

L'audit (J1-J4) répond à « qu'est-ce qui ne va pas sur ce site ». Le workflow mots-clés répond à « qu'est-ce qu'on crée maintenant ». Deux moteurs différents. Le rapport d'audit se termine sur un horizon « Mois 2-3 : nouvelles pages sur les gaps » — c'est là que ces 3 skills prennent le relais. Le call J5 fait le pont : la démo « mots-clés anti-ChatGPT » est exactement le geste de `seo-mots-cles-decisionnels` (passer du mot-clé large mangé par GPT au mot-clé décisionnel ultra-niché).

## Procédure d'install (la même qu'en S1)

1. Va dans `~/.claude/skills/` (Mac/Linux) ou `%USERPROFILE%\.claude\skills\` (Windows).
2. Crée **trois** sous-dossiers : `seo-recherche-mots-cles/`, `seo-clustering-mots-cles/`, `seo-mots-cles-decisionnels/`.
3. Dans chacun, crée un fichier `SKILL.md` et colle le bloc correspondant ci-dessous (tout ce qui est entre les deux lignes `=====`).
4. Relance Claude Code. Vérifie avec `/skills` que les 3 apparaissent.

---

## 1/3 — `seo-recherche-mots-cles`

Dossier : `~/.claude/skills/seo-recherche-mots-cles/SKILL.md`

=====

---
name: seo-recherche-mots-cles
description: |
  Recherche de mots-clés from scratch : partir d'une thématique ou de quelques seed keywords et produire une liste exhaustive, qualifiée et priorisée — chaque mot-clé avec son intention et sa difficulté. Pipeline en 5 étapes : cadrer la thématique → expansion sémantique → qualification (intention/difficulté) → filtrage du bruit → tableau priorisé. Règle : volume optionnel (affiché seulement s'il vient d'une donnée réelle, jamais estimé), difficulté jamais inventée. Sortie obligatoire en plus du tableau : un doc final d'une page, résumé + score + 5 actions prioritaires ; sans lui le skill n'a pas terminé.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "recherche de mots-clés", "trouve-moi des mots-clés", "keyword research", "liste de mots-clés sur [thème]", "quels mots-clés cibler", "explore les requêtes sur", "j'ai une thématique, sors les mots-clés", "expansion de mots-clés".

  Première brique du workflow mots-clés : sa sortie alimente seo-clustering-mots-cles puis seo-mots-cles-decisionnels.
---

# Skill — Recherche de Mots-Clés

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

## Doc final en sortie (obligatoire)

Ce skill n'a pas terminé tant que le doc final n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau. Une page, `wiki/keywords/recherche-YYYY-MM-DD-slug-resume.md`, dans cet ordre :

1. Périmètre : site ou thématique, date, période de données, nombre d'éléments analysés
2. Score : score = part des mots-clés Do ou Décision, répartition par intention, top 10, ce qui manque
3. Actions prioritaires : 5 au maximum, numérotées dans l'ordre d'exécution, une ligne chacune avec la page, l'effort et qui la fait

Aucune phrase sans chiffre ou constat derrière. Pas d'introduction, pas de conclusion. Dans le workflow complet, ce doc nourrit la Phase 7 de l'audit ou le doc final du workflow mots-clés.

## Output obligatoire

```
RECHERCHE MOTS-CLÉS — '[Thématique]'

| Mot-clé | Intention | Difficulté | Funnel | Note |
|---|---|---|---|---|
| ... | Know | Moyenne | Know | ... |
| ... | Do | Élevée | Décision | ... |

Synthèse : [nb total] mots-clés · [nb] Do · [nb] Know · [nb] Know-Simple
Top 5 à prioriser : [liste]

DOC FINAL RÉSUMÉ + SCORE (obligatoire, une page) : `wiki/keywords/recherche-YYYY-MM-DD-slug-resume.md`

Thématique · offre · marché · date · [nb] seeds en entrée → [nb] mots-clés en sortie
Score de la liste : part des mots-clés Do ou Décision = [x] %
| Intention | Nombre | Part |
|---|---|---|
| Do / Décision | ... | ... % |
| Know | ... | ... % |
| Know-Simple | ... | ... % |
Top 10 à prioriser : mot-clé, intention, pourquoi (un fait par ligne)
Ce qui manque pour aller plus loin : [export GSC absent, volume non sourcé, ...]
ACTIONS PRIORITAIRES (5 max, numérotées, dans l'ordre) : ex. lancer le clustering sur les [nb] Do, demander l'export GSC au client, écarter les [nb] Know-Simple hors offre. Une ligne par action : action, ce qu'elle débloque, qui la fait.
```

## Règles absolues

- Le doc final résumé + score fait partie de la sortie. Sans lui, le skill n'a pas terminé. Il se rédige à partir du tableau, aucune phrase sans mot-clé ou chiffre derrière.
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

=====

---

## 2/3 — `seo-clustering-mots-cles`

Dossier : `~/.claude/skills/seo-clustering-mots-cles/SKILL.md`

=====

---
name: seo-clustering-mots-cles
description: |
  Regroupe une liste brute de mots-clés en clusters exploitables — 1 cluster = 1 page. Critère de regroupement : le partage de SERP (deux mots-clés qui affichent le même top 10 = la même intention = une seule page). Pipeline en 5 étapes : importer la liste → normaliser (dédoublonner, nettoyer) → regrouper par intention de SERP → nommer chaque cluster et désigner le mot-clé pivot → affecter 1 cluster = 1 page avec détection de cannibalisation. Sortie obligatoire en plus du tableau : un doc final d'une page, résumé + score + 5 actions prioritaires ; sans lui le skill n'a pas terminé.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "cluster mes mots-clés", "groupe cette liste de mots-clés", "keyword clustering", "regroupe mes requêtes", "j'ai 200 mots-clés à organiser", "quels mots-clés vont sur la même page", "transforme ma liste en pages".

  Diffère de seo-cluster-aeo, qui part d'UN mot-clé pilier pour bâtir une architecture. Ici on part d'une LISTE BRUTE de N mots-clés et on la découpe en pages. Brique d'architecture du workflow mots-clés : après seo-recherche-mots-cles, avant seo-brief-contenu.
---

# Skill — Clustering de Mots-Clés

## Quand déclencher

Transformer une liste brute de N mots-clés en clusters exploitables, où chaque cluster devient une page.

## Doctrine

- Le vrai critère de clustering SEO = le **partage de SERP**. Si Google affiche le même top 10 pour deux requêtes, il les traite comme la même intention → une seule page.
- La proximité sémantique seule ne suffit pas. "Assurance auto pas chère" et "tarif assurance auto" se ressemblent mais peuvent avoir des SERP distinctes.
- 1 cluster = 1 page = 1 mot-clé pivot. Deux pages sur le même cluster = cannibalisation programmée.
- Sans accès aux SERP réelles, l'IA cluster par intention + sémantique **en proxy** : la sortie est une hypothèse à valider, jamais une vérité.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| La liste brute de mots-clés (collage, CSV, sortie de `seo-recherche-mots-cles`) | Oui |
| Intention + volume par mot-clé | Recommandé |
| Données de SERP overlap d'un outil (Keyword Insights, Ahrefs "Parent topic") | Recommandé — rend le clustering fiable |
| Le site / l'offre (pour orienter le nommage et détecter la cannibalisation) | Recommandé |

## Pipeline (5 étapes)

1. **Importer la liste** — accepter un collage brut, un CSV ou la sortie de `seo-recherche-mots-cles`.
2. **Normaliser** — dédoublonner, retirer le bruit (mots-clés sans intention, branded concurrent hors scope), fusionner les variantes orthographiques strictes (singulier/pluriel, accents).
3. **Regrouper** — critère #1 : SERP overlap si la donnée est fournie. Sinon proxy : intention identique + même tête sémantique. Chaque groupe = un cluster.
4. **Nommer + pivot** — pour chaque cluster : nom (head term), intention dominante (Know-Simple / Know / Do), mot-clé pivot (le plus représentatif, plus fort volume) + mots-clés secondaires.
5. **Affecter** — 1 cluster = 1 page. Détecter les clusters qui recoupent une page existante → risque de cannibalisation, renvoyer vers `seo-cannibalisation`.

## Doc final en sortie (obligatoire)

Ce skill n'a pas terminé tant que le doc final n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau. Une page, `wiki/keywords/clusters-YYYY-MM-DD-slug-resume.md`, dans cet ordre :

1. Périmètre : site ou thématique, date, période de données, nombre d'éléments analysés
2. Score : score par cluster sur 6 (décision, proximité offre, matière disponible), score global = part des clusters à 4 ou plus, les 10 pages à produire en premier, clusters qui attendent de la matière
3. Actions prioritaires : 5 au maximum, numérotées dans l'ordre d'exécution, une ligne chacune avec la page, l'effort et qui la fait

Aucune phrase sans chiffre ou constat derrière. Pas d'introduction, pas de conclusion. Dans le workflow complet, ce doc nourrit la Phase 7 de l'audit ou le doc final du workflow mots-clés.

## Output obligatoire

```
CLUSTERS — '[Liste / thématique]'

| Cluster | Mot-clé pivot | Secondaires | Intention | Page (nouvelle / existante) | Risque cannibalisation |
|---|---|---|---|---|---|
| ... | ... | ... | Know | Nouvelle | — |

Non clusterisés : [mots-clés orphelins laissés seuls]
À valider : confirmer chaque cluster par un SERP overlap réel (outil ou vérification manuelle).

DOC FINAL RÉSUMÉ + SCORE (obligatoire, une page) : `wiki/keywords/clusters-YYYY-MM-DD-slug-resume.md`

Liste source · date · [nb] mots-clés en entrée → [nb] clusters = [nb] pages
Score par cluster, sur 6, trois critères notés 0 / 1 / 2 :
- Décision : 0 aucun mot-clé décisionnel · 1 au moins un · 2 le pivot est décisionnel
- Proximité offre : 0 aucun point de conversion atteignable · 1 conversion à un clic · 2 la page porte l'offre + CTA
- Matière disponible : 0 rien dans l'Obsidian du client · 1 verbatims ou tickets · 2 un document du corpus couvre le sujet
Score global = part des clusters à 4/6 ou plus = [x] %
| Cluster | Pivot | Décision | Proximité | Matière | /6 |
|---|---|---|---|---|---|
Les 10 pages à produire en premier, score décroissant, avec la matière source
Clusters qui attendent de la matière, et ce qu'il faut demander au client
ACTIONS PRIORITAIRES (5 max, numérotées, dans l'ordre) : les clusters à 5-6/6 partent en brief (`seo-brief-contenu`), les clusters à 4/6 sans matière partent en demande au client, les cannibalisations détectées se règlent avant toute page neuve. Une ligne par action : action, cluster concerné, qui la fait.
```

## Règles absolues

- Le doc final résumé + score fait partie de la sortie. Sans lui, le skill n'a pas terminé. Il se rédige à partir du tableau, aucune phrase sans mot-clé ou chiffre derrière.
- 1 cluster = 1 page = 1 pivot. Jamais deux clusters sur la même intention (principe MECE).
- Un mot-clé n'appartient qu'à un seul cluster.
- Sans donnée SERP, marquer explicitement la sortie « hypothèse — à valider par overlap réel ».
- Ne pas forcer un mot-clé orphelin dans un cluster : le laisser en « non clusterisé ».
- Si un cluster recoupe une page live → flag cannibalisation, ne pas créer de doublon.

## Enchaînement workflow

Après `seo-recherche-mots-cles` → chaque cluster devient un input : `seo-brief-contenu` (1 cluster = 1 brief), ou `seo-cluster-aeo` si le cluster est assez gros pour devenir un pilier. Les clusters d'intention Do → `seo-mots-cles-decisionnels`.

## Sauvegarde

Output dans `wiki/keywords/clusters-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`serp-overlap` · `mece` · `cannibalisation` · `cluster-aeo` · `passage-ranking` · `maillage-interne`

=====

---

## 3/3 — `seo-mots-cles-decisionnels`

Dossier : `~/.claude/skills/seo-mots-cles-decisionnels/SKILL.md`

=====

---
name: seo-mots-cles-decisionnels
description: |
  Isole les mots-clés décisionnels — les requêtes transactionnelles et bas de funnel qui convertissent, par opposition aux requêtes informationnelles qui ne font que du trafic. Pipeline en 5 étapes : définir l'offre et le point de conversion → repérer les signaux décisionnels → classer par étage de décision → scorer le potentiel de conversion → shortlist priorisée avec page et format recommandés. Part d'une liste existante ou d'une thématique. Sortie obligatoire en plus du tableau : un doc final d'une page, résumé + score + 5 actions prioritaires ; sans lui le skill n'a pas terminé.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "mots-clés décisionnels", "mots-clés transactionnels", "mots-clés qui convertissent", "requêtes bas de funnel", "requêtes Do", "mots-clés bottom funnel", "quels mots-clés rapportent", "trie ma liste par potentiel de conversion", "mots-clés commerciaux".

  Brique de conversion du workflow mots-clés : se branche après seo-recherche-mots-cles ou seo-clustering-mots-cles.
---

# Skill — Mots-Clés Décisionnels

## Quand déclencher

Isoler, dans une liste ou une thématique, les requêtes qui amènent un client — pas seulement du trafic.

## Doctrine

- Le trafic n'est pas l'objectif, la conversion l'est. Un mot-clé à 10 000 vues/mois sans intention d'achat vaut moins qu'un mot-clé à 80 vues qui amène un client.
- Un mot-clé décisionnel = l'internaute est en train de choisir, comparer ou acheter. Il a mentalement sorti la carte bleue.
- Le décisionnel se repère à ses **modificateurs**, pas à son volume.
- Bas de funnel ≠ forcément faible volume : "meilleur [catégorie]" peut peser lourd.
- Le décisionnel se traite en priorité : c'est le ROI le plus court du SEO.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Liste de mots-clés OU thématique | Oui |
| Offre : ce qu'on vend, prix, point de conversion (formulaire, achat, démo, appel) | Oui |
| Audience / persona | Oui |
| Autres acteurs du marché (pour les requêtes branded) | Recommandé |

## Signaux décisionnels (table de modificateurs)

| Catégorie | Modificateurs |
|-----------|---------------|
| **Achat direct** | acheter, commander, prix, tarif, devis, abonnement, s'inscrire |
| **Comparaison** | meilleur, top, vs, comparatif, alternative à, lequel choisir |
| **Évaluation** | avis, test, retour d'expérience, fiable, arnaque |
| **Local / immédiat** | près de moi, [ville], en ligne, livraison, ouvert |
| **Marque** | [ta marque], [ta marque] avis/prix, [nom d'outil] alternative |

## Étages de décision

- **Do — Achat** : l'internaute veut transformer maintenant.
- **Do — Comparatif** : il choisit entre options, toi inclus.
- **Do — Local** : intention d'achat + contrainte géographique.
- **Do — Marque** : il te connaît déjà, ou connaît un autre acteur du marché.
- **Know commercial** : "comment choisir un X" — pré-décision, à capter tôt.

## Pipeline (5 étapes)

1. **Définir l'offre** — ce qu'on vend, le prix, le point de conversion réel.
2. **Repérer les signaux** — passer la liste ou la thématique au filtre des modificateurs décisionnels.
3. **Classer par étage de décision** — ranger chaque mot-clé retenu.
4. **Scorer le potentiel de conversion** — proximité à l'offre (1-5) × intention d'achat (1-5) × faisabilité de ranker (1-5), produit ramené sur une **échelle 0-10 (arrondi entier)**. Flag les requêtes branded sur un autre acteur pour vérifier la légitimité.
5. **Livrable** — shortlist priorisée ; pour chaque mot-clé : page cible (landing, comparatif, page produit, page locale), format, CTA.

## Doc final en sortie (obligatoire)

Ce skill n'a pas terminé tant que le doc final n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau. Une page, `wiki/keywords/decisionnels-YYYY-MM-DD-slug-resume.md`, dans cet ordre :

1. Périmètre : site ou thématique, date, période de données, nombre d'éléments analysés
2. Score : score global = moyenne des scores de conversion, répartition par étage, les 10 pages à produire en premier, mots-clés écartés
3. Actions prioritaires : 5 au maximum, numérotées dans l'ordre d'exécution, une ligne chacune avec la page, l'effort et qui la fait

Aucune phrase sans chiffre ou constat derrière. Pas d'introduction, pas de conclusion. Dans le workflow complet, ce doc nourrit la Phase 7 de l'audit ou le doc final du workflow mots-clés.

## Output obligatoire

```
MOTS-CLÉS DÉCISIONNELS — '[Offre]'

| Mot-clé | Étage | Score conv. /10 | Page cible | Format | CTA |
|---|---|---|---|---|---|
| ... | Do — Comparatif | 5/10 | Page comparatif | Tableau + verdict | Devis |

Top 3 à attaquer en premier : [liste + justification]

DOC FINAL RÉSUMÉ + SCORE (obligatoire, une page) : `wiki/keywords/decisionnels-YYYY-MM-DD-slug-resume.md`

Offre · point de conversion · date · [nb] mots-clés en entrée → [nb] décisionnels retenus
Score global = moyenne des scores conv. /10 des décisionnels retenus = [x]/10
| Étage | Nombre | Score conv. moyen |
|---|---|---|
| Do, comparatif | ... | ... |
| Do, prix ou devis | ... | ... |
| ... | | |
Les 10 pages à produire en premier : mot-clé, page cible, CTA, score
Mots-clés écartés et pourquoi (une ligne chacun)
ACTIONS PRIORITAIRES (5 max, numérotées, dans l'ordre) : page à créer ou à réécrire par décisionnel du top, CTA à poser sur une page existante, outil à concevoir pour une requête Do (`seo-product-led-seo`). Une ligne par action : action, mot-clé, page, qui la fait.
```

## Règles absolues

- Le doc final résumé + score fait partie de la sortie. Sans lui, le skill n'a pas terminé. Il se rédige à partir du tableau, aucune phrase sans mot-clé ou chiffre derrière.
- Ne jamais classer décisionnel un mot-clé purement informationnel pour gonfler la liste.
- Requête branded sur un autre acteur → vérifier la légitimité : page comparative honnête, aucune tromperie.
- Chaque mot-clé décisionnel pointe vers une page avec offre + CTA, sinon il ne convertit pas.
- Prioriser proximité à l'offre + faisabilité, pas le volume brut.

## Enchaînement workflow

Après `seo-recherche-mots-cles` ou `seo-clustering-mots-cles` → alimente `seo-product-led-seo` (outils pour les requêtes Do) et `seo-brief-contenu` (pages de conversion).

## Sauvegarde

Output dans `wiki/keywords/decisionnels-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`know-simple-know-do` · `funnel` · `product-led-seo` · `fully-meets` · `cannibalisation` · `e-e-a-t`

=====

## Note pour Tim (interne)

- Contenu **identique aux skills canoniques** `~/.claude/skills/seo-{recherche,clustering,mots-cles}-*/SKILL.md`, reproduit verbatim — aucune section privée à purger (pas de pointeur vault). Si tu mets à jour un skill canonique, régénère ce fichier.
- **Les 3 sont neufs (commit `a9b4eae`, mai 2026, repo `tim-claude-skills`), hors pack des 9.** Ils bouchent le trou « workflow mots-clés » repéré : avant, le seul skill keyword-first était `seo-programmatique-pseo`, le reste (cluster-aeo, brief, quick-win) empruntait du keyword à des skills pensés pour autre chose.
- **Positionnement S3 = additionnels, pas prérequis.** Le J1-J4 n'en a pas besoin. Ils servent la démo J5 « mots-clés anti-ChatGPT » (= geste exact de `seo-mots-cles-decisionnels`) et l'horizon « Mois 2-3 » du plan d'audit. Message week-end : les présenter en **bonus**, « installe si tu veux suivre la démo en live », pour ne pas alourdir un week-end déjà chargé en installs (`indexation-check`, re-bundles).
- **Ne pas confondre avec `seo-cluster-aeo`** (pack #... S1) : cluster-aeo part d'UN pilier pour bâtir une architecture, `seo-clustering-mots-cles` part d'une LISTE BRUTE de N mots-clés et la découpe en pages. À marteler si quelqu'un demande au call.
- **Limite à annoncer honnêtement** : `seo-clustering-mots-cles` cluster par SERP overlap si la donnée est là, sinon proxy intention + sémantique → sortie « hypothèse à valider ». Claude ne scrape pas les SERP. Si un participant veut du clustering fiable, outil type Keyword Insights.
- **Boucle S2 ↔ S3** : la sortie de ces 3 skills repart dans `article-engine-pipeline` de la S2. C'est le carburant de l'horizon « Mois 2-3 ». Cohérent avec la note §167 du séquençage (l'audit recharge le moteur de contenu).
