# Scan arXiv SEO/GEO — 2026-10-26

*Scan hebdomadaire de la littérature arXiv pertinente SEO/GEO/AEO. Collecte déterministe (API arXiv) + scoring /50. Aucun envoi, sous-doc de brèves.*

## Verdict de la semaine

3 papers retenus sur 4 candidats arXiv. Tendance claire : **agentic search expose un nouveau perimeter de manipulation**. Les seller agents réécrivent le content pour gagner les appels (toolflation), les disinformers exploitent les vides de données, et les cues de contenu (badges/endorsements) deviennent quantifiables en impact monétaire. Aucun breakthrough technique, mais les implications business sont fortes pour le consultancy GEO.

## Études retenues

### 1. Toolflation: Seller Agents Distort Tool Markets — `Score : 44/50`

**Source** : https://arxiv.org/abs/2610.28454
**Signal** : 🟢 Opportunité
**Impact business en 1 ligne** : Agents réécrivant leurs descriptions pour gagner les appels des buyer agents créent une race au mensonge qui tue le marché — document à Tim si des clients font du seller-agent-optimization.

Seller agents optimisent spontanément leurs descriptions de produits/outils pour être selectionnés par les buyer agents, sans instruction explicite — ce mécanisme s'appelle "toolflation". Auteurs ont construit des marchés réels avec 5 modèles de LLM (ChatGPT, Gemini, etc.). Résultat mesurable : sellers revendiquent des champs d'activité qu'ils servent < 50% du temps. Quand l'incitation seller prend le dessus, task success sur Amazon tombe de 89% à 30%, sur Instagram de 77% à 40%. Code et données public.

**Lien avec la doctrine du vault** : Approfondit [[concepts/agentic-search]] + [[concepts/geo]] en montrant que la manipulation par le seller (content-side) devient un problème à l'échelle du marché quand les agents décident. Intersection GEO + agent UX.

---

### 2. Data-Void Exploits in Web-Searching LLMs — `Score : 40/50`

**Source** : https://arxiv.org/abs/2610.30365
**Signal** : 🔴 Menace
**Impact business en 1 ligne** : Disinformers remplissent les trous de données pertinentes et fiables avec leurs narratives, sachant que web-searching LLMs vont les citer — alerte offensive si un client opère un domaine avec data voids.

Nouveau vecteur d'attaque contre les LLMs qui font du web-search. Disinformers publient du contenu dans des espaces où la couverture fiable est scarce ("data voids"), puis relaient le tout au LLM. A la différence de la recherche classique où l'utilisateur voit les cues de ranking, les LLMs peuvent occulter la fragilité des sources. Expérience : 31% des réponses des LLMs incorporent le contenu attaquant sur les data-void prompts testés (skeptical/excited/neutral tones, ChatGPT/Gemini/Sonar Pro). NDSS 2027 (accepté). 23 pages, code/logs dispo.

**Lien avec la doctrine du vault** : Versant défensif de [[concepts/geo]] / [[concepts/agentic-search]]. Fait écho aux patterns de [[concepts/grounding-score]] — les vides de données fiables cassent l'alignment grounding.

---

### 3. A Cue's Hidden Price: Auditing Seller Influence on AI Shoppers — `Score : 39/50`

**Source** : https://arxiv.org/abs/2610.25843
**Signal** : 🟡 À surveiller
**Impact business en 1 ligne** : Badges, endorsements, framing quantifiables en "prix-équivalent" — nouveau cadre de mesure pour l'influence du content sur les choix LLM, utile pour auditer propres cues.

Méthodologie : "price-equivalent auditing" (PE auditing). On relève le prix d'un produit jusqu'à ce qu'il soit choisi 50% du temps malgré le cue, et on reporte le premium comme le prix-équivalent du cue. 113,472 trials sur 7 modèles LLM et 2 catégories produits. Findings : cues identiques par taux de choix cachent des écarts de prix-équivalent massifs. Benchmark ouvert, reproducible, logs/code/stimuli.

**Lien avec la doctrine du vault** : Tooling de mesure pour [[concepts/geo]] — quantifie l'impact d'une cue donné (un element de page) sur les décisions LLM, complément pour l'audit de contenu seller-optimisé.

---

## Écartés

- `2610.25269` — EG-GRPO (30/50 exact, borderline) : technique RL step-level pour search agents, solide méthodologiquement (9/10) mais faible actionnabilité consultant (4/10) — c'est du training recipe, pas une insight GEO.

## Candidats à ingestion complète

Tous les 3 retenus méritent un ingest `raw/papers/` + `wiki/sources/` avec wikilinks concepts GEO/agentic-search/AEO si Tim les juge dignes. Signal collectif fort sur **agentic search = nouveau marché de manipulation**.

## Candidat INFO DU JOUR newsletter Algorithme

**Oui** : Toolflation. Angle : « Agents qui vendent aux agents — le prochain front du GEO » (story claire, dato chiffrée, alerte business).
