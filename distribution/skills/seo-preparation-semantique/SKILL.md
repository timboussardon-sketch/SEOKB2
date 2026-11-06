---
name: seo-preparation-semantique
description: "Carte sémantique d'une requête en 10 couches, ou audit d'un contenu existant. « préparation sémantique »."
---

# Skill — Préparation sémantique sans SERP (v10)

## Quand utiliser ce skill

Engine de préparation sémantique sans scraping SERP. Deux modes : CRÉATION (requête → carte vierge en 10 couches) et AUDIT (contenu existant → diff vs carte attendue + plan de correction P0/P1/P2).

TOUJOURS utiliser ce skill quand l'utilisateur dit :
- Mode Création : "prépare la sémantique", "carte sémantique", "préparation sémantique", "engine sémantique", "tout ce que ma page doit contenir", "fais-moi l'analyse sémantique de [requête]", "lance l'engine sur [requête]", "sémantique sans SERP", "analyse sémantique [mot-clé]", "prépa sémantique [requête]", "entités pondérées [requête]", "surprise score sémantique de [requête]".
- Mode Audit : "audite la sémantique de", "audit sémantique de cette page", "ma page couvre-t-elle [requête]", "compare ce contenu à la carte sémantique attendue", "qu'est-ce qui manque à mon article sur [requête]", "diff sémantique", "audit de couverture sémantique", "ma page ne ranke pas — qu'est-ce qui lui manque", "plan de correction sémantique".

## Détecter le mode

Si l'utilisateur fournit **uniquement une requête + un profil** → Mode **CRÉATION**.

Si l'utilisateur fournit **en plus un contenu** (texte collé, chemin de fichier `*.md` / `*.html`, ou URL publique) → Mode **AUDIT**.

Si ambigu, demander : « Tu veux créer la carte sémantique d'une page à écrire, ou auditer un contenu existant ? »

Le doc source complet est `.seokb/base/wiki/methodes/engine-densite-semantique-sans-serp.md`. Lire ce doc avant la première exécution pour récupérer le détail des phases et les format des tableaux.

**Écart avec le doc source (décision Tim, 2026-09-15)** : la Phase 7 du doc (cartographie des acteurs, 5-10 acteurs avec angle dominant et faiblesse) est retirée du skill. On ne produit jamais ce tableau. Les phases 8 à 13 du doc deviennent les phases 7 à 12 ici, et la Gap analysis se fait contre le consensus du contenu dominant sur la requête (projection corpus), sans nommer d'acteurs.

## Input requis — Mode Création

| Variable | Valeur attendue | Obligatoire |
|---|---|---|
| Requête cible | mot pour mot | Oui |
| Pays / langue | FR/FR par défaut | Oui |
| B2B/B2C + rôle | « B2B — CMO SaaS 50p » | Oui |
| Objectif | Lead Gen / Conversion / Expertise FM | Oui |
| Secteur | nommé | Oui |
| Audience (expertise) | junior / expert / mixte | Oui |
| Localisation | ville ou « N/A » | Oui |
| Expertise unique | une phrase | Recommandé |
| Mode forcé | bronze / silver / gold | Optionnel |

## Input requis — Mode Audit (en plus des inputs Création)

| Variable | Valeur attendue | Obligatoire |
|---|---|---|
| Contenu à auditer | texte markdown collé, chemin local, URL publique (robots.txt OK) | Oui |
| Version cible | refonte / update freshness / élargissement d'intention / migration | Recommandé |

Si une variable obligatoire manque, Claude pose **une seule question groupée** avant de produire.

## Pipeline (12 phases)

```
Phase 0 — Filtre stratégique (informatif, jamais bloquant)
   │  alerte WARN éventuelle + annexe sous-niches
   ▼ GO toujours
Phase 1 — Décodage micro-intentionnel + Action Engine flag
Phase 2 — Entités sémantiques pondérées (poids + densité + cosinus simulé + justif + statut)
Phase 3 — Lexique signature (n-grams + co-occurrences)
Phase 4 — Pain points & verbatims Haute Surprise
Phase 5 — Preuves quantitatives (Confidence Score + Freshness Guard)
Phase 6 — Vecteurs multimodaux
Phase 7 — Gap analysis 3 vues :
   7a. Gap Map (matrice consensus × entité P1 : l'entité est-elle couverte par le contenu dominant ? gap exploitable si non)
   7b. Content Gap Score (% standard vs % surprise)
   7c. Surprise Score Sémantique 0-100
Phase 8 — Divergence calibrée Information Gain (Quotation +41%, Stats +34%, Sources +29%)
Phase 9 — FAQ stratégique FM (5-7 vecteurs latents)
Phase 10 — Structural Information GEO (title/meta/H/schema)
Phase 11 — Matrice couverture × Mapping Triade SERP
Phase 12 — Feedback loop KB (patches à archiver)
```

## Format Phase 2 — Entités sémantiques pondérées (7 colonnes)

Format obligatoire :

```
| # | Entité | Type | Poids (0-1) | Densité cible (%) | Cosinus estimé requête (0-1) | Justification | Statut |
|---|---|---|---|---|---|---|---|
| 1 | `passage ranking` | Concept | 0.94 | 0.8% | 0.91 | Brique du grounding, citée dans 3 papers MIRAS | P1 critique |
| ... | ... | ... | ... | ... | ... | ... | ... |
```

Type : Person / Concept / Tool / Method / Doctrine / Event / Location / Algo.
Poids > 0.8 = pivot. Densité pivots 0.5-1%, supportives 0.2-0.5%, périphériques < 0.2%.
**Cosinus marqué « simulé »** dans pied de tableau obligatoire.
**Justification obligatoire** par entité.
30-50 entités par run (50+ en Gold).

## Format Phase 7c — Surprise Score Sémantique

Formule :
```
Surprise Score Sémantique = pondération de 4 composantes :
  30% — Ratio entités propriétaires / entités totales (KB Gold)
  20% — Ratio verbatims Haute Surprise / verbatims totaux
  25% — Distance lexicale moyenne propriétaire ↔ consensus (1 - cosinus simulé)
  25% — Présence Quotation Addition + Statistics Addition (% preuves verbatim/chiffrées avec source)
```

Échelle :
- 0-30 = Médiocrité statistique (oubli mémoriel)
- 30-60 = Acceptable mais réplicable
- 60-85 = Information Gain validé (zone organikk.co)
- 85-100 = Inversion experte maximale (zone bootcamp 4)

**Avertissement obligatoire** : « *Score calibré sur projection corpus Claude. Pour calibration exacte : audit GEO Sentinel (skill seo-geo-audit, 7 scores algorithmiques).* »

## Règles absolues

- **Aucun scraping SERP**, jamais. Pas Google, pas Bing, pas autre moteur.
- **Robots.txt strict** pour tout WebFetch. Si bloqué : training Claude + demande à l'utilisateur, jamais bypass.
- **Cosinus simulé toujours marqué** : chaque sortie Phase 2 + Phase 7c doit inclure l'avertissement « *simulé par projection corpus Claude, non calibré mathématiquement* ».
- **Confidence Score obligatoire** sur chaque preuve chiffrée. Si basse ou inconnue → placeholder `[À SOURCER]`. Aucun chiffre inventé pour gonfler le Grounding Score.
- **Freshness Guard** : preuves > 36 mois omises sauf paper fondateur.
- **Phase 0 jamais bloquante** : alerte WARN éventuelle + propose sous-niches en annexe, mais produit toujours la carte complète.
- **Ne pas rédiger** : pas de H1 final, pas de hook, pas d'architecture Hn finale, pas de CTA, pas de prose narrative.
- **Une page = une intention** (pureté vectorielle). Si pluralité d'intentions détectée Phase 0.3, signaler en WARN + proposer N sous-cartes en annexe.
- **Anti-cliché obligatoire** dans la couche pain points : pas de « je veux du ROI », pas de « je veux des résultats ».
- **Phase 2 — Justification obligatoire** : chaque entité doit avoir une justification courte (paper, doctrine, co-occurrence). Pas d'entité arbitraire.
- **Jamais de cartographie d'acteurs** (retirée le 2026-09-15) : aucun tableau d'acteurs nommés avec leurs angles et leurs faiblesses. La Gap analysis raisonne contre le consensus du contenu dominant, projeté depuis le corpus.

## Output obligatoire

12 tableaux livrables + matrice de couverture mappée sur la Triade SERP + Surprise Score Sémantique 0-100 + verdict global + liste patches KB.

Format markdown structuré, prêt à alimenter `seo-brief-contenu` (structure Hn) ou `article-engine-pipeline` (rédaction complète).

```
PRÉPARATION SÉMANTIQUE — Requête : "[...]"
Profil : [B2B/B2C, rôle, secteur, objectif, audience, géo]
Mode détecté : [Bronze / Silver / Gold]

== PHASE 0 — Filtre stratégique (informatif) ==
- Test LLM : [PASS / WARN]
- Angle différenciant : [PASS / WARN — sous-niches proposées en annexe]
- Pureté vectorielle : [PASS / WARN — N intentions]
Verdict : [GO franche / GO avec avertissement]
Annexe sous-niches (si WARN) : [...]

== Livrables 1-12 ==
1. Micro-intentions (3 niveaux + profil + Action Engine flag)
2. Entités sémantiques pondérées (7 colonnes : entité/type/poids/densité/cosinus/justif/statut)
3. Lexique signature (n-grams + co-occurrences + statut)
4. Pain points + 3 objections priorisées
5. Preuves quantitatives (Confidence Score + Freshness Guard)
6. Multimodal
7. Gap analysis :
   7a. Gap Map (matrice consensus × entité P1)
   7b. Content Gap Score (% standard vs % surprise)
   7c. Surprise Score Sémantique : XX/100 — [verdict]
8. Divergences (Information Gain calibré)
9. FAQ stratégique FM (5-7 vecteurs)
10. Structural Information GEO (title/meta/H/schema)
11. Matrice couverture × Triade SERP
12. Patches KB à archiver
```

## Enchaînement workflow

**En amont** : aucun (c'est la première brique).

**En aval, selon objectif** :
- `seo-brief-contenu` → structure Hn complète à partir de la carte
- `article-engine-pipeline` → rédaction complète à partir de la carte (passe par seo-workflow-article)
- `seo-product-led-seo` → si Action Engine flag déclenché (intention Do)
- `seo-donnees-structurees` → implémentation JSON-LD à partir de la Phase 10
- `seo-geo-audit` → en aval d'une rédaction, audit qualité 7 scores (complémentaire à Mode Audit qui mesure la couverture)

## Sauvegarde

Output dans `wiki/queries/prepa-semantique-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md (vault seo-kb).

## Concepts liés

[[purete-vectorielle]] · [[triade-serp]] · [[information-gain]] · [[surprise-gap]] · [[surprise-metric]] · [[grounding-score]] · [[confidence-score]] · [[mots-cles-actionnels]] · [[angle-differenciant-mot-cle]] · [[data-proprietaire]] · [[fully-meets]] · [[passage-ranking]] · [[structural-information-geo]] · [[answer-first-pattern]] · [[freshness-guard]] · [[rrf]] · [[aeo]] · [[know-simple-know-do]] · [[product-led-seo]] · [[anti-ai-writing]]
