---
type: query
skill: seo-page-statistiques
status: draft
title: "Migrations de domaine, 301 et citabilité IA : l'autorité paramétrique ne se transfère pas (2025-2026)"
tags: [geo, aeo, migration, domaine, 301, parametrique, chatgpt, perplexity, gemini, claude, rebranding, ai-overviews]
created: 2026-09-20
updated: 2026-09-20
sources: 7
confidence: medium
---

# Migrations de domaine et citabilité IA : 41 jours pour que les moteurs adoptent le nouveau domaine, des mois pour effacer l'ancien (2026-09-20)

La médiane de récupération de citation IA après une migration complète de domaine est de **41 jours** — mais ce chiffre ne concerne que la couche de récupération en temps réel. La mémoire paramétrique des modèles (ce qu'ils ont appris à l'entraînement) continue de produire des réponses mentionnant l'ancien domaine ou l'ancien nom de marque sur un horizon de **plusieurs mois**, sans qu'un redirect 301 puisse l'effacer. Deux horloges, deux mécanismes, un seul KPI de migration : c'est la confusion centrale que cette page documente avec les données disponibles en 2026.

---

## Les chiffres clés (vérifiés à la source)

### Récupération de citation par moteur IA après migration (MaxAEO, 38 migrations B2B SaaS, fin 2025–mi-2026)

| Moteur | Jours avant de citer le nouveau domaine | Jours avant que l'ancien s'efface |
|---|---|---|
| Perplexity | 6 | 14 |
| Google AI Overviews | 9 | 21 |
| Copilot | 11 | 24 |
| ChatGPT | 12 | 34 |
| Grok | 14 | 30 |
| Gemini | 16 | 38 |
| Claude | 18 | 45 |
| **Médiane globale** | **~12** | **~41** |

Source : MaxAEO, 38 migrations de domaine et chemins, B2B SaaS et tech, suivi quotidien par moteur, fin 2025–mi-2026.

**Deux facteurs aggravent ces délais :**
- Migrations de domaine complet (nouveau TLD ou nouveau nom de domaine) : délai **~40 % plus long** que les changements de chemin seuls.
- Chaînes de redirects ou WAF mal configurés : récupération **~2× plus lente** qu'un 301 direct sans intermédiaire.
- Certaines migrations de domaine complet ont dépassé **90 jours** sans retour à la baseline.

### Hops de redirect tolérés par type de crawler IA

| Type de crawler | Exemples | Hops maximum tolérés |
|---|---|---|
| Crawlers d'entraînement | GPTBot, ClaudeBot, PerplexityBot | 5 hops |
| Crawlers de réponse temps réel | OAI-SearchBot, Claude-SearchBot, Perplexity-User | 3 hops |

Source : confirmé par plusieurs analyses techniques 2025-2026 (CaptainDNS, Anagram, Digital Applied).

**Conséquence directe :** une chaîne de redirects que GPTBot digère sans problème peut silencieusement exclure une page des réponses de ChatGPT Search ou Claude Search — les deux crawlers répondent à des tolérances différentes.

### Migration SEO classique : référence de base

- Durée médiane de récupération du trafic organique après migration : **523 jours** (17 mois).
- 17 % des sites restent en dessous de leur baseline après 1 000 jours.
- Récupérations les plus rapides documentées : 19 à 23 jours.

Source : analyse tierce de 892 migrations de domaine, données collectées octobre 2024, relayée par Digital Applied et Search Engine Journal.

### Présence de X.com dans les moteurs IA (RankSpot, 20 935 réponses IA, 1–19 septembre 2026)

| Moteur | Taux de citation X.com |
|---|---|
| Google AI Overviews | 0,1 % (9 sur 6 434 réponses) |
| ChatGPT | <0,1 % (1 sur 7 005 réponses) |
| Google AI Mode | <0,1 % (1 sur 7 437 réponses) |
| Rang global | 166e sur 261 domaines mesurés |

Source : RankSpot, 20 935 réponses IA analysées sur requêtes commerciales réelles, période du 1er au 19 septembre 2026.

Pour contexte : YouTube s'affiche à 13,9 %, Reddit à 9,5 %, Facebook à 3,0 %. Twitter a rebaptisé son domaine en x.com en juin 2023 — plus de trois ans plus tard, le domaine reste quasi invisible dans les réponses IA.

### KPI de référence pour une migration

BrightEdge a formalisé en 2025 le premier KPI explicite de préservation des citations IA dans les migrations :
- **≥ 95 % des citations IA conservées** dans les 60 jours post-migration.
- **≥ 90 % du trafic organique conservé** dans les 60 jours post-migration.

C'est la première fois que la préservation des citations dans les moteurs génératifs apparaît comme critère de succès formalisé, à côté du trafic organique.

Source : BrightEdge, guide de migration 2025, publié courant 2025.

---

## Trois types de migration, trois mécanismes distincts

Les études et les guides de migration confondent régulièrement trois situations qui n'obéissent pas aux mêmes règles :

### 1. Changement de chemin ou de structure d'URL (domaine identique)

Le redirect 301 est suivi par les crawlers de réponse en temps réel en **quelques jours**. La mémoire paramétrique n'est pas en jeu : les URLs ne sont pas mémorisées comme des entités nommées dans les poids du modèle. C'est le scénario le plus favorable — les délais MaxAEO du tableau ci-dessus s'appliquent dans leur partie basse.

### 2. Migration de domaine complet (nouveau TLD ou nouveau nom de domaine)

Le crawl de réponse suit le 301 en jours à semaines. Mais le **domaine d'origine** reste cité dans les réponses paramétriques — les réponses que le modèle génère sans déclencher de recherche web — pendant plusieurs mois, jusqu'au prochain cycle de ré-entraînement. MaxAEO documente des délais dépassant 90 jours pour la disparition de l'ancien domaine dans les réponses. Les migrations complètes prennent ~40 % plus de temps que les migrations de chemin.

### 3. Rebranding avec changement de nom de marque (ex. Twitter → X, Facebook → Meta)

C'est le cas le plus complexe, et le moins documenté empiriquement. Deux horloges s'ajoutent :
- L'horloge de récupération URL (crawl, semaines).
- L'horloge de récupération paramétrique sur le nom de marque lui-même (pas seulement le domaine), sur un horizon de mois à années.

Le cas X.com est illustratif : trois ans après le rebranding de Twitter en X (juin 2023), le domaine x.com reste à <0,1 % des citations IA (RankSpot, sept. 2026). Le phénomène ne se réduit pas à la citabilité du domaine — les réponses paramétriques de ChatGPT, Claude ou Gemini continueront de mentionner "Twitter" pour décrire la plateforme, indépendamment de ce que pointe le crawl, jusqu'à ce que les données d'entraînement soient majoritairement mises à jour.

---

## Pourquoi ces chiffres révèlent un angle borgne dans les études de migration

La quasi-totalité des études de migration SEO (les 892 migrations Digital Applied/SEJ, les KPIs BrightEdge) mesurent deux métriques : trafic organique et classements. Les études GEO les plus récentes ajoutent les citations IA — mais toujours comme une seule métrique, sans distinguer le mécanisme de retrieval du mécanisme paramétrique.

Or, un site peut :
- **Récupérer ses citations de retrieval** (ChatGPT Search, Perplexity, AI Overviews) en 2 à 6 semaines avec un 301 propre.
- **Continuer à être cité sous son ancien domaine ou son ancien nom** dans les réponses paramétriques de ChatGPT sans web search, Claude sans web search, ou Gemini — pendant plusieurs mois — sans aucune action possible à court terme.

La divergence crée une situation paradoxale : les outils de mesure GEO (Profound, Peec AI, Semrush) qui monitorent les citations en production peuvent afficher une récupération partielle, pendant que les réponses paramétriques pures (celles que la majorité des utilisateurs de ChatGPT obtiennent sans déclencher de recherche web) continuent de mentionner l'ancienne entité.

**Données de configuration des crawlers** : la limite à 3 hops pour les crawlers de réponse (OAI-SearchBot, Perplexity-User) contre 5 hops pour les crawlers d'entraînement crée un autre paradoxe — les pages peuvent être correctement apprises à l'entraînement mais exclues des citations en temps réel si la chaîne de redirects est trop longue.

---

## Nos propres chiffres (données de première main)

Aucune migration de domaine client dans le portefeuille actuel ne peut être mobilisée comme données de première main pour ce sujet. Ce bloc est réservé honnêtement. L'enrichissement avec des données propriétaires est possible si une migration est suivie avec export GSC avant/après dans `raw/data/exports-gsc/`.

---

## Contre-analyse

**La mémoire paramétrique n'affecte qu'une partie des réponses.** Les moteurs IA en mode recherche active (ChatGPT Search, Perplexity, AI Overviews, AI Mode) suivent les redirects et s'appuient sur le crawl récent. L'impact paramétrique est concentré sur les réponses générées sans déclenchement de recherche web — or ce mode (conversation directe sans web search) représente encore la majorité des interactions chez ChatGPT selon les données de déclenchement Semrush/Nectiv (31 à 34,5 % de déclenchement web search global).

**Les 301 restent le bon outil.** Pour les migrations de chemin intra-domaine, les données MaxAEO montrent une récupération complète des citations de retrieval en quelques semaines avec un 301 propre. La chaîne de redirects est le premier facteur de risque, pas le redirect lui-même.

**Le cas Twitter/X est atypique.** Le domaine twitter.com était massivement bloqué par robots.txt pour les crawlers IA (GPTBot, ClaudeBot, PerplexityBot : tous Disallow: / selon les analyses robots.txt 2025-2026). Le faible taux de citation de X.com en 2026 reflète autant la politique de blocage que l'effet du rebranding sur la mémoire paramétrique. Les deux effets ne sont pas séparables dans les données disponibles.

**523 jours de récupération SEO classique ≠ 41 jours de citations IA.** Les mécanismes sont distincts. Une migration bien exécutée peut récupérer ses citations IA bien avant de récupérer ses classements organiques — parce que les moteurs génératifs ont des critères de citation qui ne se réduisent pas aux classements.

**Absence de données France.** Toutes les études disponibles portent sur des marchés anglophones (US, UK) avec des requêtes en anglais. L'impact des migrations sur la citabilité IA en français reste sans mesure publiée.

---

## FAQ

**Combien de temps faut-il pour qu'un moteur IA cite le nouveau domaine après migration ?**
Entre 6 jours (Perplexity) et 18 jours (Claude) selon MaxAEO (38 migrations B2B SaaS, fin 2025–mi-2026). La médiane globale est d'environ 12 jours, avec un 301 propre et sans chaîne de redirects.

**Un redirect 301 efface-t-il les mentions paramétriques de l'ancien domaine ?**
Non. Le redirect 301 est suivi par les crawlers de réponse en temps réel (jours à semaines) mais ne modifie pas la mémoire paramétrique des modèles. Celle-ci ne se met à jour que lors des cycles de ré-entraînement, sur un horizon de plusieurs mois, indépendamment de la présence ou non d'un redirect.

**Quelle est la différence entre migration de chemin et migration de domaine pour les citabilités IA ?**
MaxAEO mesure un délai de récupération ~40 % plus long pour les migrations de domaine complet par rapport aux migrations de chemin (même domaine). Certaines migrations complètes dépassent 90 jours sans retour à la baseline.

**Combien de hops de redirects les crawlers IA tolèrent-ils ?**
Les crawlers d'entraînement (GPTBot, ClaudeBot, PerplexityBot) tolèrent jusqu'à 5 hops. Les crawlers de réponse en temps réel (OAI-SearchBot, Claude-SearchBot, Perplexity-User) abandonnent au 3e hop — une chaîne que Google digère peut silencieusement exclure une page des citations de ChatGPT Search.

**Que mesure un outil GEO comme Profound ou Peec AI après une migration ?**
Ces outils mesurent les citations de retrieval (réponses déclenchant une recherche web). Ils ne mesurent pas les réponses paramétriques pures — c'est un angle mort non documenté. Une récupération "complète" selon ces outils n'implique pas que les réponses paramétriques aient cessé de mentionner l'ancienne entité.

**Le schéma structuré est-il critique lors d'une migration ?**
Oui. La perte de balisage Schema lors d'une migration peut stopper les citations dans Google AI Overviews, Perplexity et ChatGPT Search sans impact visible sur les classements organiques — un risque de première importance identifié en 2025 (BrightEdge, Digital Applied).

---

## [À SOURCER]

- **Taux de citation twitter.com dans les moteurs IA post-rebranding** (avant la bascule x.com) : aucune étude comparative twitter.com vs x.com avant/après ne figure dans les données publiques disponibles.
- **Délai paramétrique pour les changements de nom de marque** (vs changements d'URL) : LLMMetrix et MaxAEO décrivent le mécanisme mais n'ont publié aucune mesure empirique du délai de reparamétrisation sur une cohorte de marques rebranded.
- **Données France/francophone** : aucune étude de migration avec suivi des citations IA en français n'est disponible dans les sources identifiées.
- **Impact de la migration de domaine sur Claude et Perplexity désagrégés** au-delà du tableau MaxAEO (accès limité à la méthodologie complète).
- **Récupération des citations paramétriques** : MaxAEO documente la disparition de l'ancien domaine dans le retrieval, pas dans la mémoire paramétrique directement — aucune étude ne quantifie ce second délai de façon contrôlée.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté le |
|---|---|---|---|---|
| Site Migration AI Search Visibility: Redirects, URL Changes, and Citation Recovery | MaxAEO | 2025-2026 | https://maxaeo.ai/blog/site-migration-ai-visibility/ | 2026-09-20 |
| X.com Citation Frequency in AI Engines | RankSpot | 2026-09-19 | https://www.rankspot.ai/most-cited-sources/sources/x.com | 2026-09-20 |
| 2025 Guide to a Successful Site Migration: How to Protect Your SEO in the AI Search Era | BrightEdge | 2025 | https://www.brightedge.com/blog/2025-guide-successful-site-migration-how-protect-your-seo-and-grow-era-ai-search | 2026-09-20 |
| SEO Site Migration in 2026: Zero-Traffic-Loss Playbook | Digital Applied | 2026 | https://www.digitalapplied.com/blog/seo-site-migration-2026-zero-traffic-loss-playbook | 2026-09-20 |
| AI Crawlers & Redirects: GPTBot, ClaudeBot, Perplexity 2026 | CaptainDNS | 2026 | https://www.captaindns.com/en/blog/ai-crawlers-redirects-handling-gptbot-claudebot-perplexitybot | 2026-09-20 |
| The Rebrand Problem: Why AI Still Calls You by Your Old Name | LLM Metrix | 2026 | https://llmmetrix.com/blog/the-rebrand-problem-in-ai-search | 2026-09-20 |
| Your Next Platform Migration Could Erase You from AI Search | Codal | 2026 | https://codal.com/insights/your-next-platform-migration-could-erase-you-from-ai-search-heres-how-to-prevent-it/ | 2026-09-20 |
