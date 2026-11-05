---
type: query
skill: seo-page-statistiques
title: "Documentation collaborative publique (Confluence, Notion, GitBook) dans les citations IA B2B : accessible, lue, jamais citée — 2025-2026"
tags: [citations-ia, documentation, confluence, notion, gitbook, b2b, robots-txt, agents-ia, geo]
created: 2026-10-31
updated: 2026-10-31
sources: 8
confidence: medium
status: draft
---

# Documentation collaborative publique (Confluence, Notion, GitBook) dans les citations IA B2B : accessible, lue, jamais citée — 2025-2026

En juillet 2026, 66 % du trafic vers les documentations techniques provient d'agents IA — 213 millions de requêtes machines contre 105 millions humaines sur les sites propulsés par Mintlify. Ces mêmes plateformes de documentation collaborative — GitBook, Notion, Confluence — sont absentes de tous les classements des 50 domaines les plus cités dans chaque étude publiée sur les citations IA. Robots.txt ouverts. Agents actifs. Citations dans les réponses : inexistantes dans les données disponibles.

---

## Les chiffres clés (vérifiés à la source)

### Accessibilité aux crawlers IA — robots.txt vérifiés le 2026-10-31

| Plateforme | User-agent: * | Règles spécifiques IA | Résultat |
|---|---|---|---|
| GitBook (gitbook.com) | Allow: / | `Content-Signal: ai-input=yes, ai-train=no` | Accès total explicite |
| Notion (notion.so) | Allow: / | Aucune — bloque uniquement AhrefsBot, SemrushBot, BLEXBot, dotbot | Accès total aux crawlers IA |
| Atlassian.com | Ouvert (sauf /blog/author/*, /purchase/*) | Aucune règle IA | Accès total |
| Confluence (confluence.atlassian.com) | Ouvert sauf chemins fonctionnels | `crawl-delay: 60`, pas de blocage IA | Accès total, délai 60 s |
| Coda.io | Ouvert sauf /apis/, /embed/, /docs, /d/ | Aucune règle IA | Accès partiel |

**Constat** : aucune des cinq plateformes ne bloque les crawlers IA par nom (GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot). L'accès est techniquement ouvert pour toutes.

GitBook va plus loin : il publie une déclaration de signal explicite (`ai-input=yes`) et fournit un fichier `llms.txt` plus des versions Markdown de chaque page. Confluence.atlassian.com impose un délai de crawl de 60 secondes, mais ne restreint pas les agents IA nommément.

### Consommation par les agents IA — documentation Mintlify (juillet 2026, vérifié)

- **66 %** du trafic total vers les documentations Mintlify provient d'agents IA en juillet 2026
- **15,2 %** en janvier 2026 → **66 %** en juillet 2026 (hausse de 50,8 points en 7 mois)
- **213 millions** de requêtes agents en juillet 2026, contre **105 millions** de visites humaines
- **Projection** : ~90 % du trafic documentation en agents d'ici fin 2026, si la tendance se maintient
- **83,7 %** des requêtes agents passent par des chemins machine-lisibles explicites (`.md`, content-negotiation `text/markdown`, plain text) — le reste est des pages HTML ordinaires demandées par des agents connus
- **Réduction d'erreurs 404** : de 2,23 erreurs par retrieval en HTML à 0,11 avec Markdown + `llms.txt`, soit **−95 %** (benchmark 2 400 runs sur 20 sites, Mintlify, juillet 2026)

### Citations dans les réponses — présence dans les études (2025-2026)

- Aucune des plateformes (Notion, GitBook, Confluence, Coda) **n'apparaît dans les 50 premiers domaines cités** dans les études à grande échelle : Profound 680 M citations, Peec AI 30 M, Ahrefs Brand Radar 1,9 M requêtes, Obsurfable top-domain août 2026
- La documentation vendeur au sens large représente **1,1 %** des citations dans les réponses IA sur les requêtes B2B SaaS (BeVisibleIQ, 2 020 citations, mars 2026, cross-référencé dans [[sources/2026-09-17-stats-documentation-help-center-citations-ia]])
- Sur 1 739 citations B2B SaaS analysées en juillet 2026 : les pages vendeur représentent **24 %** des citations ChatGPT et **12 %** des citations Perplexity (Growfusely, 128 requêtes, 16 catégories, juillet 2026) — mais aucune documentation collaborative spécifiquement identifiée dans cette taxonomie
- La documentation technique (help centers, guides produit) figure bien dans les citations sur les **requêtes développeurs** : Reddit #1 (10 831 citations), Medium #2, Dev.to #3 (DevTune, 126 814 citations, 43 catégories dev tools, 5 moteurs, avril-juin 2026) — les plateformes collaboratives absentes du top 10

---

## La triple confusion dans les analyses du secteur

Trois objets distincts sont régulièrement confondus sous l'intitulé « citabilité de la documentation IA » :

**Objet 1 — L'accessibilité technique** (robots.txt) : toutes les plateformes majeures sont ouvertes aux crawlers IA. C'est la condition nécessaire, pas suffisante.

**Objet 2 — La consommation par les agents** : les agents IA lisent massivement la documentation (66 % du trafic docs en juillet 2026, Mintlify). Cette lecture est silencieuse : elle sert au raisonnement interne de l'agent, pas à produire une citation visible.

**Objet 3 — La citation dans les réponses** : le lien que l'utilisateur voit. C'est ce que mesurent les études de citabilité (Profound, Peec AI, Ahrefs Brand Radar). Les plateformes collaboratives n'y apparaissent pas.

Ces trois objets ont trois mécanismes distincts, trois mesures séparées et trois réponses pratiques différentes. Les confondre fausse le diagnostic pour les équipes B2B qui cherchent à être citées dans les réponses IA.

---

## Pourquoi la documentation collaborative est-elle absente des citations ?

### Paradoxe 1 — Le signal `ai-input=yes` de GitBook ne déclenche pas de citation

GitBook déclare explicitement `Content-Signal: ai-input=yes` dans son robots.txt et expose un fichier `llms.txt`. Cela signifie que les moteurs peuvent utiliser ce contenu comme entrée pour leur raisonnement — mais cette permission ne crée pas de citation automatique dans les réponses. La documentation est consommée en amont dans la chaîne de traitement, pas présentée comme source à l'utilisateur.

Le parallèle : llms.txt réduit les erreurs d'agents codeurs de 95 % (Mintlify, 2 400 runs) mais zéro corrélation avec les citations dans les réponses (SE Ranking, 300 000 domaines, étude [[sources/2026-10-14-stats-llms-txt-directives-agents-ia]]).

### Paradoxe 2 — La fragmentation des domaines dilue l'autorité

Confluence héberge des milliers d'espaces publics (sous `*.atlassian.net` ou des domaines personnalisés). Notion héberge des pages publiques sur `notion.site`. GitBook héberge des sites sur `*.gitbook.io` ou des domaines personnalisés. Chaque espace ou site a son propre domaine ou sous-domaine, sans capital d'autorité partagé. Le signal de domaine référent — qui est le premier facteur de citabilité dans les modèles XGBoost (SE Ranking, SHAP 0,56 AI Mode, SHAP 1,21 ChatGPT, étude [[sources/2026-08-21-stats-profondeur-topicale-vs-autorite-domaine-citations-ia]]) — est fragmenté sur des milliers d'entités distinctes.

Comparer : `docs.gitbook.com` n'a pas le même capital qu'un domaine like `reddit.com` ou `stackoverflow.com` qui concentre toute son autorité sur un seul domaine.

### Paradoxe 3 — Le contenu collaboratif sans auteur nommé souffre du déficit d'attribution

Les études disponibles sur les bylines montrent que les individus nommés représentent 87,8 % des pages IA citées (OtterlyAI, 1,31 M citations, jan.-juin 2026, étude [[sources/2026-08-12-stats-auteurs-bylines-citations-ia]]). La documentation collaborative — Confluence, Notion, GitBook — est souvent publiée sans auteur identifié, sous un nom d'entreprise ou anonymement. Ce format réduit la densité d'attribution, un signal que les moteurs IA semblent valoriser.

---

## Nos propres chiffres (données de première main)

Aucune donnée du vault ne porte spécifiquement sur des espaces Confluence publics, des sites GitBook, ou des pages Notion en tant que sources citées dans les réponses IA. Le registre [[wiki/preuves/index]] ne recense aucun test contrôlé sur ces plateformes.

Ce bloc est réservé honnêtement : le vide est documenté ici comme vide de données, pas comme absence de performance.

---

## Contre-analyse

**Absence du top 50 ≠ absence totale des citations.** Les études de citation analysent les domaines les plus fréquents. Une documentation Confluence très authoritative sur une requête technique précise peut apparaître dans une réponse sans jamais atteindre le top 50 d'un dataset cross-industrie.

**Les pages vendeur bien référencées remontent.** Sur les requêtes directes du type « comment configurer X » ou « documentation API X », les moteurs citent régulièrement des pages `docs.X.com`. La distinction pertinente n'est pas plateforme collaborative vs. blog éditorial — c'est la correspondance sémantique entre la requête et le contenu de la page. Une page Confluence bien structurée peut performer sur des requêtes précises même si elle n'apparaît jamais dans les classements agrégés.

**L'architecture multi-tenant peut évoluer.** GitBook centralise désormais ses sites sous `gitbook.com/[org]` (nouveaux sites) plutôt que sous des sous-domaines `*.gitbook.io` séparés. Cette consolidation crée progressivement un signal de domaine agrégé. Si cette tendance se poursuit, la visibilité agrégée de GitBook dans les citations pourrait croître.

**Le trafic agent 66 % est propre à Mintlify.** Les documentations hébergées sur Confluence Cloud ou Notion Sites ne sont pas mesurées par Mintlify. Le taux réel de consommation par les agents sur ces plateformes reste inconnu — potentiellement plus faible, potentiellement similaire.

**Le crawl-delay: 60 de Confluence peut créer un retard d'indexation.** Un délai de 60 secondes entre deux requêtes de crawl ralentit l'indexation des nouvelles pages, ce qui peut créer un décalage entre la publication et la disponibilité dans les moteurs IA.

---

## FAQ

**Les pages Notion publiques sont-elles indexées par les crawlers IA ?**
Oui, selon deux sources. Le robots.txt de notion.so (vérifié le 2026-10-31) autorise tous les crawlers IA sans restriction. Un rapport GitHub d'octobre 2026 confirme que les pages publiques sur `notion.site` servent du HTML rendu côté serveur aux crawlers, incluant GPTBot et ClaudeBot.

**GitBook est-il mieux positionné que Notion pour les citations IA ?**
Sur le plan technique, GitBook a une position plus explicite : il déclare `ai-input=yes`, expose un `llms.txt` et génère des versions Markdown de ses pages. Cela facilite la consommation par les agents. Mais aucune étude publiée ne compare les taux de citation Notion vs. GitBook sur les mêmes requêtes. L'absence de données comparatives directes interdit une réponse définitive.

**Pourquoi les moteurs IA consomment-ils la documentation mais ne la citent-ils pas ?**
Distinction fondamentale : les agents IA lisent la documentation pour construire leur réponse (66 % du trafic docs selon Mintlify), mais la citation — le lien visible dans la réponse — obéit à une logique différente. Les moteurs tendent à citer les sources d'autorité généraliste (Wikipedia, Reddit, Stack Overflow) qui ont accumulé des signaux de confiance sur une longue période, pas les espaces de documentation d'une entreprise spécifique.

**Un espace Confluence public peut-il apparaître dans ChatGPT ou Perplexity ?**
Techniquement oui : les pages sont crawlables, le crawl-delay de 60 secondes ne bloque pas. En pratique, l'absence de données dans les études disponibles suggère que cela arrive rarement pour les requêtes génériques. Sur des requêtes très spécifiques portant sur un produit ou une configuration précise, la probabilité de citation augmente.

**La déclaration `Content-Signal: ai-train=no` de GitBook est-elle respectée ?**
C'est une déclaration de préférence dans le robots.txt — non pas une restriction technique de crawl. Aucune étude ne confirme que les LLMs respectent ce signal de la même façon qu'une règle `Disallow`. En pratique, `ai-train=no` avec `ai-input=yes` indique une préférence d'usage (utilisation en retrieval, pas en entraînement), mais son application dépend de chaque moteur.

---

## [À SOURCER]

- **Taux de citation de Notion (notion.site), GitBook (*.gitbook.io, *.gitbook.com) et Confluence par moteur IA** : aucune étude publiée ne désagrège les citations par ces domaines/sous-domaines spécifiques. Vide structurel documenté.
- **Taux réel de consommation agents sur Confluence Cloud et Notion** : les données Mintlify couvrent uniquement les sites propulsés par Mintlify. Le taux agent sur Confluence Cloud ou Notion Sites est inconnu.
- **Effet du crawl-delay: 60 de Confluence sur la fraîcheur des citations** : aucune étude comparant la fraîcheur des pages Confluence vs. des pages sans crawl-delay.
- **ReadTheDocs.io robots.txt** : non vérifié dans cette session.
- **Comparaison contrôlée documentation collaborative vs. page éditoriale à autorité équivalente** : aucune étude publiée.
- **Fraction des pages publiques Confluence sur l'ensemble des espaces Confluence** : Atlassian ne publie pas ce chiffre.
- **Nombre exact de sites publics actifs sur Notion Sites** : non publié.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté le |
|---|---|---|---|---|
| GitBook robots.txt — robots.txt complet avec Content-Signal ai-input=yes | GitBook | Fetché 2026-10-31 | https://www.gitbook.com/robots.txt | 2026-10-31 |
| Notion robots.txt — ouvert aux crawlers IA, bloque SEO bots | Notion | Fetché 2026-10-31 | https://www.notion.so/robots.txt | 2026-10-31 |
| Atlassian.com robots.txt — aucune règle IA | Atlassian | Fetché 2026-10-31 | https://www.atlassian.com/robots.txt | 2026-10-31 |
| Confluence documentation robots.txt — crawl-delay: 60, chemins fonctionnels bloqués | Atlassian | Fetché 2026-10-31 | https://confluence.atlassian.com/robots.txt | 2026-10-31 |
| Coda.io robots.txt — bloque /apis/, /embed/, /docs, /d/ | Coda | Fetché 2026-10-31 | https://coda.io/robots.txt | 2026-10-31 |
| State of Docs Traffic — 66 % agents, 213 M requêtes agents juillet 2026, -95 % erreurs 404 avec llms.txt | Mintlify | 2026-07-29 | https://www.mintlify.com/blog/state-of-docs-traffic | 2026-10-31 |
| AI Citation Analysis B2B Software — 1 739 citations, 24 % ChatGPT vs 12 % Perplexity sur pages vendeur | Growfusely | Juillet 2026 | https://growfusely.com/blog/ai-citation-analysis-b2b-software/ | 2026-10-31 |
| Étude documentation help centers (cross-référence vault) — vendor docs 1,1 % citations B2B SaaS | BeVisibleIQ via vault | Mars 2026 | Voir [[sources/2026-09-17-stats-documentation-help-center-citations-ia]] | 2026-10-31 |
| GitBook public docs — 150 000 organisations, llms.txt, Markdown export, Content-Signal | GitBook | 2026 | https://www.gitbook.com/solutions/public-docs | 2026-10-31 |
