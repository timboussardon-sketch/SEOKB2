---
name: seo-geo-audit
description: "Audit GEO d'une page ou d'un texte : 7 scores pour être cité par les IA. « audit GEO », « score GEO »."
---

# Skill — Audit GEO (GEO Sentinel)

## Quand utiliser ce skill

Audit GEO (Generative Engine Optimization) d'une page ou d'un texte : note le contenu sur 7 scores algorithmiques (Surprise, Grounding, Content Effort, Alignement RRF, RAG Structurer, Freshness Guard, Action Engine) pour détecter la "Médiocrité Statistique" et garantir la citation par les moteurs génératifs (Google SGE / AI Overview, SearchGPT, Perplexity). Pipeline en 5 étapes : cadrer le texte + l'intention → noter les 7 scores avec problèmes localisés → calculer le score global → prioriser les corrections → plan de réécriture. Règle anti-hallucination stricte : aucun chiffre ni date inventé, placeholder [À SOURCER] obligatoire.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "audit GEO", "score GEO", "optimiser pour les moteurs génératifs", "GEO Sentinel", "mon texte est-il citable par l'IA", "SGE / AI Overview", "pourquoi ChatGPT/Perplexity ne me cite pas", "analyse ce texte pour le GEO", "Surprise Score", "Grounding Score d'une page", "ce contenu survivra-t-il aux filtres IA".

## Quand déclencher

Auditer une page ou un texte déjà rédigé pour le GEO (Generative Engine Optimization) : savoir s'il sera cité par les moteurs hybrides (Google SGE / AI Overview, SearchGPT, Perplexity) ou rejeté comme contenu générique.

Diffère de `seo-entites-vectorielles` (qui prépare les entités *avant* rédaction) et de `seo-workflow-article` (qui *rédige*). Ici on **note un texte existant** et on liste les corrections.

## Posture

Tu n'es pas un coach bienveillant, tu es un **Validateur de Signaux**. Un texte n'est pas de la littérature, c'est un ensemble de vecteurs de données. Tu rejettes :

- un texte agréable mais vide de preuves → risque d'hallucination ;
- un texte juste mais qui répète le consensus → Low Surprise, oubli mémoriel ;
- un texte qui explique sans permettre d'agir → pas d'Action Engine.

Sois impitoyable mais constructif : chaque problème détecté doit être actionnable.

## Concepts clés

- **Médiocrité Statistique** — le contenu que n'importe quelle IA aurait pu générer ; cible n°1 de l'audit.
- **Surprise Metric** (architecture Titans) — le gradient d'apprentissage : seul le contenu à fort gradient est gravé en Neural Memory, le reste est oublié.
- **Grounding Score** — densité de triplets [Sujet] + [Relation] + [Entité/Valeur] ; l'ancrage factuel.
- **Weight Decay** — l'oubli architectural des contenus anciens : justifie le Freshness Guard.
- **Answer-first pattern** — réponse directe dans les 2-3 premières phrases ; nourrit le RAG Structurer.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Le texte à auditer (page, article, section) | Oui |
| La requête cible / l'intention principale visée | Oui |
| Le secteur + le type de page (éditorial, produit, locale) | Recommandé |
| Les concurrents top 10 (pour juger la divergence) | Optionnel |

## Les 7 scores GEO

Chaque score est noté **0-100**. Pour chaque score, lister les **problèmes localisés** : phrase problématique + raison précise et actionnable.

### 1. Surprise Score — algorithme de mémorisation
- Mesure le gradient d'apprentissage du texte.
- Cherche : distance sémantique au consensus, inversion de valeur, data propriétaire.
- Exigence : le texte doit contenir **une donnée que tu es le seul à posséder**.
- Problèmes typiques : répétition du consensus, similarité avec Wikipédia, absence de thèse originale.

### 2. Grounding Score — l'ancrage factuel
- Mesure la densité de triplets [Sujet] + [Relation] + [Entité Nommée/Valeur].
- Cherche : dates précises, chiffres, noms de lois, citations exactes.
- Exigence : **2 preuves atomiques par 100 mots minimum**.
- Problèmes typiques : affirmations vagues, "bientôt", "important", absence de données chiffrées.

### 3. Content Effort — preuve de travail humain
- Mesure les signaux que l'IA ne peut pas simuler (E-E-A-T).
- Cherche : "j'ai testé", méthodologie, processus documenté, anecdotes d'échec.
- Exigence : prouver **plus de 30 secondes de travail réel**.
- Problèmes typiques : synthèse générique, absence d'expérience personnelle, théorie pure.

### 4. Alignement RRF — Reciprocal Rank Fusion
- Mesure la couverture vectorielle et les micro-intentions.
- Cherche : réponse aux intentions explicites ET latentes (prix, intégration, support…).
- Exigence : **aucun trou sémantique** dans la couverture de la requête.
- Priorité : intentions explicites, questions fréquentes, micro-intentions. Les objections enrichissent le contexte mais sont optionnelles (impact limité, ~5%).
- Problèmes typiques : aspects implicites manquants, questions Know/Do/Comparatif non répondues.

### 5. RAG Structurer — lisibilité machine
- Mesure la capacité d'un Retriever à parser le contenu.
- Cherche : proximité titre-réponse (**<30 mots après un H2**), tableaux, listes structurées.
- Exigence : **pyramide inversée** à chaque section, format natif LLM (answer-first).
- Problèmes typiques : intros vagues, structure narrative, absence de tableaux comparatifs.

### 6. Freshness Guard — biais de récence
- Mesure l'obsolescence du contenu (conséquence du Weight Decay).
- Cherche : dates récentes, mentions temporelles explicites.
- Exigence : références à **2026**, mention "À jour en [Mois]".
- Problèmes typiques : données de 2023 ou antérieures, absence de timestamp.

### 7. Action Engine — utilité & conversion
- Mesure la capacité du texte à permettre l'action.
- Cherche : verbes d'action, liens vers outils / templates / calculatrices.
- Exigence : transformer le "Savoir" en "Faire".
- Problèmes typiques : explication théorique sans outil, absence de call-to-action fonctionnel.

## Pipeline (5 étapes)

1. **Cadrer** — récupérer le texte, la requête cible et le type de page. Vérifier la longueur minimale exploitable (au moins 100 caractères).
2. **Noter les 7 scores** — passer le texte au crible des 7 critères ci-dessus ; pour chacun, noter 0-100 et lister chaque problème (phrase + raison).
3. **Calculer le score global** — moyenne arithmétique des 7 scores, arrondie. Compter le nombre total de problèmes.
4. **Prioriser les corrections** — trier les scores du plus bas au plus haut ; attaquer d'abord les 2-3 scores les plus faibles (effort de correction le plus rentable).
5. **Plan de réécriture** — pour chaque problème prioritaire, une action concrète. Aucune réécriture inventée : si une donnée chiffrée ou une date manque, marquer `[À SOURCER]`.

## Barème de lecture du score global

| Score global | Verdict | Action |
|--------------|---------|--------|
| 80-100 | Citable | Corrections cosmétiques, refresh périodique |
| 60-79 | Fragile | Corriger les 2 scores les plus bas avant publication |
| 40-59 | À retravailler | Réécriture des sections faibles, injection de data |
| 0-39 | Médiocrité Statistique | Le contenu n'aurait pas dû exister tel quel — refonte |

## Output obligatoire

```
AUDIT GEO — Requête : "[Requête cible]"
Type de page : [éditorial / produit / locale]

| Score | Note /100 | Problèmes | Diagnostic court |
|---|---|---|---|
| Surprise | 38 | 4 | Répète le consensus, aucune data propriétaire |
| Grounding | 52 | 6 | 0,8 preuve / 100 mots — sous le seuil de 2 |
| Content Effort | ... | ... | ... |
| Alignement RRF | ... | ... | ... |
| RAG Structurer | ... | ... | ... |
| Freshness Guard | ... | ... | ... |
| Action Engine | ... | ... | ... |

SCORE GLOBAL : XX/100 — [Verdict] | Problèmes totaux : XX

Problèmes localisés (extraits) :
- [Surprise] « phrase exacte » → raison + correction proposée
- [Grounding] « phrase exacte » → raison + correction proposée

Plan de réécriture priorisé :
1. [Score le plus bas] — action concrète
2. [Score suivant] — action concrète
3. ...
```

## Règle anti-hallucination (absolue)

- Ne jamais inventer un chiffre, une date, une statistique ou une source pour "remplir" un score Grounding ou Freshness.
- Toute donnée manquante recommandée → placeholder `[À SOURCER]`, jamais une valeur fabriquée.
- Ne pas inventer une anecdote d'expérience pour gonfler le Content Effort : signaler que l'auteur doit en fournir une.

## Règles absolues

- Identifier **tous** les problèmes, même mineurs — un audit complaisant ne sert à rien.
- Citer la phrase exacte du texte pour chaque problème : un problème non localisé n'est pas corrigeable.
- Ne jamais noter un score sur l'impression générale : chaque note doit s'appuyer sur des problèmes listés (ou leur absence).
- Le score global est une moyenne des 7, pas une somme pondérée : aucun score ne "rachète" un autre.
- Le Surprise Score sans data propriétaire plafonne — une bonne structure ne compense pas l'absence d'info unique.

## Enchaînement workflow

En amont : `seo-entites-vectorielles` (cartographie des entités à intégrer). En aval, selon les scores faibles : `seo-workflow-article` (réécriture complète), `seo-product-led-seo` (si Action Engine faible → créer un outil), `seo-brief-contenu` (si Alignement RRF faible → re-briefer la structure Hn).

## Sauvegarde

Output dans `wiki/queries/geo-audit-YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`surprise-metric` · `grounding-score` · `surprise-gap` · `weight-decay` · `rrf` · `answer-first-pattern` · `structural-information-geo` · `metriques-visibilite-geo` · `e-e-a-t` · `fully-meets`
