---
type: query
skill: seo-page-statistiques
status: draft
created: 2026-10-28
updated: 2026-10-28
title: "Forums sectoriels, Discourse et phpBB dans les citations IA : l'espace structurellement ouvert mais absent des mesures (2025-2026)"
tags: [seo, ia, geo, citations-ia, forums, discourse, phpbb, reddit, community]
confidence: medium
sources: 7
---

# Forums sectoriels, Discourse et phpBB dans les citations IA : l'espace structurellement ouvert mais absent des mesures (2025-2026)

Forum/Q&A hors Reddit = 7,8 % des citations IA mesurées (Attrifast, 51 723 citations, avril-mai 2026). Discourse.org ne bloque aucun crawler IA. Pourtant aucune étude publiée à ce jour n'a détecté d'instances Discourse ou phpBB dans les sources régulièrement citées. La chute de Reddit sur ChatGPT (-86,4 % en août 2026) n'a pas bénéficié aux forums sectoriels : ce sont LinkedIn, Medium et Instagram qui ont capté l'espace libéré. Ce paradoxe est documenté, pas résolu.

---

## Les chiffres clés (vérifiés à la source)

### Part globale Forum/Q&A (hors Reddit) dans les citations IA

| Métrique | Valeur | Source | Méthode |
|---|---|---|---|
| Part Forum/Q&A toutes intentions | **7,8 %** des citations | Attrifast, 51 723 citations, 12 secteurs | 1 200 prompts, 4 moteurs, avril-mai 2026 |
| Part Forum/Q&A année précédente | **7,1 %** | Attrifast, pilote 300 prompts, mai 2025 | Même protocole |
| Variation annuelle | **+0,7 point** | Attrifast | — |
| Part forums (Reddit inclus), toutes requêtes | **1,0 %** | Archipel, 406 626 réponses, 6 moteurs | Requêtes d'achat, juillet-octobre 2026 |

Le chiffre Attrifast (7,8 %) et le chiffre Archipel (1,0 %) mesurent deux objets distincts : Attrifast exclut Reddit de sa catégorie Forum/Q&A et couvre quatre moteurs ; Archipel agrège Reddit et les forums sur requêtes d'achat francophones. Ces deux mesures sont incomparables.

### Variation par moteur : la chute ChatGPT (Archipel, vérifié à la source)

| Moteur | Part forums (juillet 2026) | Part forums (oct. 2026) | Variation |
|---|---|---|---|
| ChatGPT | **6,1 %** | **0,1 %** | −6,0 points |
| Google AI Overviews | — | **1,3 %** | — |
| Claude | — | **0,6 %** | — |
| Perplexity | — | **0,3 %** | — |
| Gemini | — | **0,3 %** | — |
| Microsoft Copilot | — | **0 %** | — |

Source : Archipel Marketing, 406 626 réponses IA sur 1 700+ questions d'achat (français, anglais, néerlandais), juillet 12 – octobre 11, 2026. Les données ChatGPT, Google AIO, Perplexity et Copilot proviennent de Profound ; Claude et Gemini de Peec AI. Consulté le 2026-10-28.

### Forum/Q&A par secteur (Attrifast, 51 723 citations, vérifié à la source)

| Secteur | Part Forum/Q&A |
|---|---|
| SaaS | **11,7 %** |
| Électronique grand public | **9,8 %** |
| Services B2B | **5,8 %** |
| Agroalimentaire | **4,6 %** |
| Éducation | **4,3 %** |
| Fintech | **4,2 %** |
| Immobilier | **4,1 %** |
| Assurance | **3,9 %** |
| Voyage | **3,7 %** |
| Mode DTC | **3,6 %** |
| Santé | **2,4 %** |
| Juridique | **2,1 %** |

Reddit classé séparément dans cette étude (11,4 % de part, Attrifast). Les domaines exemples cités pour Forum/Q&A : stackoverflow.com, quora.com, indiehackers.com. Discourse et phpBB absents.

### Le recul de Reddit et ses bénéficiaires

| Événement | Chiffre | Source |
|---|---|---|
| Part Reddit sur ChatGPT avant la chute | **3,83 %** | Promptwatch, juillet 18 – août 7, 2026 |
| Part Reddit sur ChatGPT après la chute | **0,52 %** | Promptwatch, août 14-17, 2026 |
| Variation | **−86,4 %** | Promptwatch |
| Part Reddit sur Google AIO (variation sur la même période) | −11,3 % | Promptwatch |
| Part Reddit globale, oct. 2025 | **2,02 %** | Conductor, 238 212 prompts |
| Part Reddit globale, jan. 2026 | **1,01 %** | Conductor |

Sources bénéficiaires après la chute Reddit (Brandlight, 425 000 prompts, 10 industries, 9-16 août 2026) :
- **LinkedIn** : +33,7 %
- **Medium** : +30,0 %
- **Lemon8** : +18,1 %
- **Instagram** : +12,4 %
- **Facebook** : +1,9 %
- **Quora** : −17,3 %
- Forums sectoriels (Discourse, phpBB, communautés verticales) : **aucune donnée**

### Accessibilité aux crawlers IA : robots.txt vérifiés à la source

| Plateforme | URL vérifiée | Règles pour les crawlers IA | Statut |
|---|---|---|---|
| discourse.org | https://discourse.org/robots.txt | Aucune règle Disallow — tous les crawlers autorisés | **Ouvert** ✅ |
| meta.discourse.org | https://meta.discourse.org/robots.txt | Bloque les bots SEO (semrushbot, ahrefsbot, etc.) mais aucune règle pour GPTBot, ClaudeBot, PerplexityBot | **Ouvert aux crawlers IA** ✅ |
| phpbb.com | https://www.phpbb.com/robots.txt | 403 Forbidden — non accessible | **[À SOURCER]** |

Fetch réalisé le 2026-10-28. Meta.discourse.org bloque spécifiquement mauibot, semrushbot, ahrefsbot, AAABot, BLEXBot et MJ12bot, mais ne liste aucune règle pour les agents IA.

---

## Pourquoi ces chiffres révèlent un paradoxe structurel

Trois niveaux d'analyse distincts convergent vers le même résultat inattendu.

**Niveau 1 : l'accès technique est ouvert.** discourse.org publie un robots.txt qui ne contient aucune règle Disallow. Meta.discourse.org — la communauté officielle de la plateforme avec des centaines de milliers de discussions sur l'administration de forums — est accessible à tous les crawlers IA. Techniquement, rien n'empêche GPTBot ou OAI-SearchBot d'indexer le contenu d'une instance Discourse dont l'administrateur n'a pas ajouté de règles de blocage manuelles.

**Niveau 2 : la part Forum/Q&A résiste au recul de Reddit.** Le chiffre Attrifast — 7,8 % de citations pour Forum/Q&A hors Reddit, stable par rapport à 7,1 % un an plus tôt — montre que les moteurs ne se sont pas détournés de ce format. La catégorie tient globalement. Pourtant l'espace libéré par la chute brutale de Reddit (-86,4 % sur ChatGPT, -50 % global) n'a pas bénéficié à d'autres forums : LinkedIn, Medium et Instagram ont capté ces volumes, selon les données Brandlight.

**Niveau 3 : aucune étude publiée ne mesure Discourse ou phpBB.** Sur les sept études à large échelle consultées pour ce travail (Attrifast 51 723 citations, Archipel 406 626 réponses, Promptwatch 26 milliards de données, Conductor 238 212 prompts, Brandlight 425 000 prompts, Otterly 1M+ citations, 5WPR 30M citations), aucune ne cite discourse.org, un sous-domaine Discourse, phpbb.com ou un forum phpBB comme source identifiée dans les réponses IA. Deux explications non exclusives :

1. **Fragmentation de l'autorité de domaine.** Chaque instance Discourse fonctionne sur son propre domaine (forum.exemple.com, discuss.laravel.com, community.grafana.com, etc.). Aucune n'accumule suffisamment d'autorité pour apparaître dans les tops N des grandes études. C'est l'inverse de Reddit, qui concentre des millions de pages sous un seul domaine avec une autorité cumulée.
2. **Contenu insuffisamment structuré pour le retrieval.** Les études Semrush (248 000 URLs Reddit, octobre 2025) et Limy.ai (503 152 citations) montrent que les posts Reddit cités ont une médiane de 80 mots et 11 upvotes. Les forums sectoriels Discourse ou phpBB ne génèrent pas les signaux de confiance agrégés (upvotes, ancienneté, backlinks) qui permettent à un domaine de s'imposer dans les résultats de retrieval.

La structure technique est favorable ; la structure de popularité ne l'est pas.

---

## Nos propres chiffres (données de première main)

Le vault seo-kb ne dispose pas d'expérience directe mesurant des citations IA de forums sectoriels. Les journaux d'ingestion (raw/journal/) mentionnent les forums comme catégorie de source potentielle mais sans données de performance. Ce bloc reste honnêtement réservé : [MATIÈRE MANQUANTE — aucune expérimentation disponible sur des forums Discourse ou phpBB sectoriels dans le vault].

---

## Contre-analyse

**L'absence de mesure ne prouve pas l'absence de citations.** Les grandes études mesurent des corpus de requêtes commerciales et informationnelles génériques. Un forum sectoriel très spécialisé (sécurité informatique, développement Python, médecine du travail) peut apparaître dans des réponses IA sur des requêtes très précises que ces études ne couvrent pas. Hacker News, absent de tous les tops 50 dans les études à large échelle, est cité dans des analyses qualitatives sur les requêtes de développeurs. La mesure à grande échelle crée un biais vers les requêtes à volume élevé.

**La fragmentation de domaine est un problème résolvable.** Un réseau de forums Discourse hébergé sur un domaine fort (par exemple community.exemple.com avec un bon profil de liens) peut potentiellement cumuler les avantages de l'autorité de domaine. Les études Attrifast montrent que SaaS (11,7 %) et électronique (9,8 %) ont les plus fortes parts Forum/Q&A : ces secteurs correspondent précisément aux communautés Discourse les plus actives (Laravel Discourse, Grafana Community, etc.).

**Le modèle Perplexity est plus favorable aux forums.** Avec 16,9 % de citations community-level selon Peec AI/Wix (chiffre non directement vérifié à la source primaire cette session — [À SOURCER]), Perplexity alloue structurellement plus de place aux discussions communautaires. Un forum bien indexé peut y avoir une présence disproportionnée par rapport à ChatGPT.

**La chute Reddit est-elle durable ?** Promptwatch note lui-même que son chiffre de -86,4 % sur ChatGPT est « provisoire ». Les changements de comportement de ChatGPT concernant les sources peuvent être réversibles. L'espace que l'on pense disponible pour les forums sectoriels peut se refermer si Reddit revient en faveur.

---

## FAQ

**Discourse bloque-t-il les crawlers IA par défaut ?**
Non. Le robots.txt de discourse.org ne contient aucune règle Disallow — tous les crawlers sont autorisés. Les administrateurs d'instances Discourse individuelles peuvent ajouter leurs propres règles, mais il n'y a pas de blocage par défaut au niveau de la plateforme. Vérifié le 2026-10-28 sur https://discourse.org/robots.txt.

**Quel moteur cite le plus les forums (hors Reddit) ?**
Perplexity est structurellement le plus favorable aux sources communautaires selon les études disponibles. La part forums sur ChatGPT a chuté de 6,1 % à 0,1 % entre juillet et octobre 2026 (Archipel). Aucune donnée par moteur n'est disponible pour Discourse ou phpBB spécifiquement.

**La chute de Reddit a-t-elle profité aux forums sectoriels ?**
Non, selon les données Brandlight (425 000 prompts, août 2026). LinkedIn (+33,7 %), Medium (+30 %) et Instagram (+12,4 %) ont capté l'essentiel de l'espace libéré. Aucune mention de forums sectoriels parmi les gagnants.

**Quelle part du marché représentent les forums non-Reddit ?**
7,8 % des citations IA sur des requêtes commerciales (Attrifast, 51 723 citations, avril-mai 2026), dont les exemples identifiés sont Stack Overflow, Quora et IndieHackers. Discourse et phpBB n'apparaissent pas dans les données.

**Y a-t-il un avantage sectoriel pour les forums ?**
SaaS (11,7 %) et électronique grand public (9,8 %) présentent les plus fortes parts Forum/Q&A (Attrifast). Ces secteurs correspondent aux communautés Discourse les plus actives. L'hypothèse d'un avantage pour les forums dans ces verticales est plausible mais non vérifiée causalement.

---

## [À SOURCER]

- **phpbb.com robots.txt** : retourne une erreur 403. Impossible de vérifier si le site officiel phpBB bloque les crawlers IA. Les instances phpBB individuelles peuvent avoir des configurations différentes.
- **Perplexity 16,9 % community forums** (Peec AI/Wix) : chiffre non re-fetché directement dans cette session. Source secondaire.
- **Otterly AI 5,9 % community forums** (1M+ citations) : page primaire non accessible lors du fetch (page vide retournée).
- **Discourse instances individuelles dans les citations IA** : aucune donnée publiée à ce jour — vide structurel documenté.
- **Données France/francophone** sur les forums sectoriels (hors étude Archipel qui couvre partiellement le marché français).
- **Stack Exchange part exacte** : aucun chiffre isolé pour stackexchange.com dans les études consultées.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté |
|---|---|---|---|---|
| AI Citation Rates by Industry 2026: A 1,200-Prompt Study | Attrifast | Avril-mai 2026 | https://attrifast.com/blog/ai-search-citations-by-vertical-2026 | 2026-10-28 |
| Archipel AI Observatory — Forums | Archipel Marketing | Juillet-oct. 2026 | https://www.archipelmarketing.com/en/observatory/sources/forums | 2026-10-28 |
| Reddit Citations Are Dropping in ChatGPT | Promptwatch | Août 2026 | https://promptwatch.com/data/reddit-citations-are-dropping-in-chatgpt | 2026-10-28 |
| The August Citation Shift 2026 | Brandlight Research | 19 août 2026 | https://research.brandlight.ai/reddit-citation-drop.html | 2026-10-28 |
| Reddit AI Citation Decline | Conductor | Jan. 2026 | https://www.conductor.com/academy/reddit-ai-citation-decline/ | 2026-10-28 |
| discourse.org robots.txt | Discourse.org | — | https://discourse.org/robots.txt | 2026-10-28 |
| meta.discourse.org robots.txt | Discourse | — | https://meta.discourse.org/robots.txt | 2026-10-28 |
