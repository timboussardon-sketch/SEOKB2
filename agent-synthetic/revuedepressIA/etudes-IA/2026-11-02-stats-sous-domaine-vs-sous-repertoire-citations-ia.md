---
type: query
skill: seo-page-statistiques
status: draft
title: "Sous-domaine vs sous-répertoire dans les citations IA : trois mécanismes distincts, zéro étude contrôlée (2025-2026)"
tags: [citations-ia, geo, architecture-url, sous-domaine, sous-repertoire, chatgpt, perplexity, ai-overviews, robots-txt, autorité-domaine]
created: 2026-11-02
updated: 2026-11-02
sources: 7
confidence: medium
---

# Sous-domaine vs sous-répertoire dans les citations IA (2026-11-02)

Les moteurs génératifs citent-ils différemment un blog en `blog.exemple.com` et un blog en `exemple.com/blog` ? La réponse courte : probablement oui, pour les sites de taille moyenne, mais le seul chiffre disponible vient d'un audit de 13 clients non contrôlé. Il n'existe aucune étude indépendante à grande échelle sur ce sujet précis. Ce document documente l'état des données et réconcilie trois mécanismes que tous les articles de blog confondent en un seul.

## Les chiffres clés (vérifiés à la source)

**Répartition observée sur 348 blogs des 2 000 sites les mieux classés (Tranco, septembre 2026) :**

- 62 % utilisent un sous-répertoire (`site.com/blog`)
- 23 % utilisent un sous-domaine (`blog.site.com`)
- 16 % utilisent un domaine séparé

Mais parmi les 100 premiers sites, la répartition s'inverse : 44 % sous-domaine, 24 % sous-répertoire, 32 % domaine séparé. Les très grands sites font ce que bon leur semble ; le débat ne les concerne pas.

**Documentation Anthropic (primaire, support.claude.com) :** ClaudeBot exige un fichier `robots.txt` sur chaque sous-domaine séparément. La règle sur `exemple.com` ne couvre pas `blog.exemple.com`. L'instruction explicite d'Anthropic : « Please do this for every subdomain that you wish to opt out from. »

**Documentation OpenAI (primaire, developers.openai.com) :** OAI-SearchBot (le bot de recherche de ChatGPT) peut être bloqué indépendamment de GPTBot (entraînement). Bloquer OAI-SearchBot exclut le site des réponses de recherche de ChatGPT. Aucun paragraphe spécifique sur les sous-domaines, mais la logique robots.txt s'applique par hôte selon le standard RFC 9309.

**Audit interne, 13 clients (seoengico.com, janvier-mars 2026) :** les blogs en sous-domaine atteignent 18 % à 41 % du taux de citation par page indexée des blogs en sous-répertoire, soit un rapport de 2 à 5 fois. Un seul cas publié : 11 citations pour le sous-répertoire contre 2 pour le sous-domaine sur 90 jours, pour deux guides quasi-identiques (`docs.entreprise.com` vs `entreprise.com/docs`). Un site a triplé ses citations dans les AI Overviews en huit semaines après migration vers le domaine principal. **Source non indépendante, échantillon de 13 clients, aucune méthode publiée.** Chiffres fournis sous réserve stricte.

**SE Ranking, 129 000 domaines, 2,3 millions de pages, AI Mode (dans le vault, étude 2026-08-21) :** le trafic du domaine est le premier facteur d'un modèle XGBoost avec un score SHAP de 0,63 ; le nombre de domaines référents suit à 0,56. Ces signaux opèrent à l'échelle du domaine enregistrable, pas du sous-domaine. Un sous-domaine part avec des signaux nuls ou réduits tant qu'il n'a pas accumulé ses propres données de trafic et de liens.

**Fuite Google API (mai 2024, confirmée) :** les attributs `siteFocusScore`, `siteRadius` et `site2vecEmbeddingEncoded` montrent que Google mesure la cohérence thématique à l'échelle du site. Un sous-domaine forme une entité distincte dans ce calcul. La pondération réelle n'est pas connue, et ces signaux concernent l'algorithme de classement organique, pas directement les citations dans les réponses IA.

**Migrations observées (theguidex.com, 348 blogs, septembre 2026) :** 80 sites redirigent un ancien sous-domaine `blog.` vers un dossier ; 15 font l'inverse. La direction majoritaire des migrations va du sous-domaine vers le sous-répertoire, ce qui reflète une croyance professionnelle dominante, pas une preuve causale.

## Pourquoi ces chiffres parlent de trois objets différents

La quasi-totalité des articles sur ce sujet mélangent trois mécanismes distincts :

**Mécanisme 1 : l'accès technique du crawler (par hôte)**

GPTBot, ClaudeBot, OAI-SearchBot et PerplexityBot lisent chaque hôte séparément. Un `robots.txt` sur le domaine apex ne couvre pas le sous-domaine. Résultat pratique : un blog en sous-domaine sans `robots.txt` propre peut être crawlé sans contrôle, ou à l'inverse rester invisible si la plateforme tierce hébergeant le sous-domaine applique un `robots.txt` restrictif par défaut. Ce mécanisme est documenté, vérifiable, et n'a rien à voir avec la qualité du contenu.

**Mécanisme 2 : l'accumulation d'autorité et de confiance**

Les signaux de domaine mesurés par SE Ranking (trafic, domaines référents) s'accumulent à l'échelle du domaine enregistrable. Un sous-domaine repart avec ses propres compteurs. Une page voisine sur `exemple.com/blog/sujet-2` bénéficie de la confiance déjà accumulée sur `exemple.com/blog/sujet-1`. Ce n'est pas le cas entre `blog.exemple.com/sujet-2` et `exemple.com`. Ce mécanisme est connu du SEO classique et s'applique aux moteurs IA dans la mesure où ceux-ci utilisent des signaux de popularité de domaine pour sélectionner les pages à citer.

**Mécanisme 3 : l'association d'entité dans les réponses générées**

Les moteurs IA attribuent une citation à un hôte exact. `blog.exemple.com` et `exemple.com` sont deux entités distinctes pour les modèles de langage, à moins que la cooccurrence du nom de marque dans les deux contextes n'établisse l'association. Un sous-domaine d'une marque peu connue aura du mal à établir cette association sans effort explicite (schéma `Organization` identique, `sameAs`, liens croisés, déclaration dans le `llms.txt` de l'apex). Pour une marque comme HubSpot, la cooccurrence est telle que `blog.hubspot.com` hérite naturellement de l'entité HubSpot.

**Le paradoxe des grands sites :** les 100 premiers sites Tranco utilisent le sous-domaine à 44 %, et ils figurent parmi les domaines les plus cités par tous les moteurs IA. Cela prouve que la structure URL n'est pas le facteur limitant pour les sites à forte autorité et notoriété établie. Le débat concerne les sites de taille moyenne.

## Le vide expérimental documenté

Il n'existe à ce jour aucune étude publiée comparant directement des sites avec un contenu identique en sous-domaine et en sous-répertoire, à autorité et notoriété égales, pour mesurer l'écart de citabilité IA. Les grandes études (SE Ranking 129 000 domaines, AirOps 548 534 pages, Profound 680 millions de citations) mesurent les signaux de domaine comme variable agrégée sans isoler la structure d'URL. L'audit de 13 clients est le seul chiffre disponible et il est trop limité pour être généralisé.

## Nos propres données de première main

Ce vault ne dispose pas de données comparées entre un sous-domaine et un sous-répertoire pour un même site. Les données disponibles (`organikk.co`) portent sur les types de pages (commerciales vs informationnelles) et les outils interactifs, pas sur la structure d'URL. Ce bloc reste honnêtement réservé.

## Contre-analyse

**L'absence de preuve n'est pas une preuve d'absence.** Les grandes études ne détectent pas d'effet subdomain parce qu'elles ne l'ont pas cherché, pas parce qu'il n'existe pas.

**Google l'a dit plusieurs fois : les deux structures sont équivalentes.** Matt Cutts en 2012, John Mueller en 2017, Gary Illyes en 2023. Pour le classement organique, les preuves empiriques à grande échelle sont faibles et contradictoires. La migration de Mention.com (janvier 2016) n'a montré aucune variation de trafic notable après le passage du sous-domaine au sous-répertoire.

**Le sous-domaine peut être justifié.** Une application authentifiée, une documentation technique sur infrastructure tierce, un forum UGC à isoler : dans ces cas, le sous-domaine est la bonne décision d'architecture, et la citabilité IA n'est pas l'objectif.

**Le chiffre de 2 à 5 fois vient d'un seul acteur.** L'audit de 13 clients (seoengico.com) n'a pas de groupe témoin, pas de méthode publiée, pas de test statistique. Il ne contrôle pas l'ancienneté des sous-domaines, le nombre de liens entrants, ni la qualité du contenu. Les auteurs eux-mêmes le qualifient de « small sample, far from a peer-reviewed study ».

**L'effet de l'architecture est probablement second par rapport à la notoriété de la marque.** Les données Ahrefs sur 75 000 marques montrent que les mentions tierces corrèlent à 0,664 avec la visibilité IA, contre 0,218 pour les domaines référents. Une marque citée naturellement sur des sites tiers sera citée qu'elle soit en sous-domaine ou en sous-répertoire.

## FAQ

**Faut-il migrer un blog de sous-domaine vers sous-répertoire pour être mieux cité par les IA ?**

Pas en urgence. Si le blog génère déjà des citations, une migration risque de créer un délai de récupération de 6 à 18 semaines (voir l'étude migrations de domaine du vault, 2026-09-20). Si le blog est récent et peu cité, le sous-répertoire est le choix sans regret.

**Un `llms.txt` sur le domaine apex couvre-t-il le sous-domaine ?**

Non. Chaque hôte a besoin de son propre fichier. Citevera recommande de déclarer explicitement le sous-domaine dans le `llms.txt` de l'apex comme atténuation partielle, mais aucune donnée ne confirme l'efficacité de cette pratique sur les citations.

**Les robots d'indexation IA gèrent-ils le sous-domaine différemment des robots de recherche classiques ?**

Mécaniquement, non : la RFC 9309 s'applique dans les deux cas par hôte exact. La différence réside dans le fait que les robots d'entraînement (GPTBot, ClaudeBot) et les robots de recherche (OAI-SearchBot) sont des agents distincts avec des `user-agent` distincts, ce qui signifie qu'un `robots.txt` restrictif sur le sous-domaine peut bloquer l'entraînement sans bloquer la citation en temps réel, ou l'inverse.

**HubSpot est sur un sous-domaine (`blog.hubspot.com`) et est massivement cité. Pourquoi ?**

Parce que le mécanisme 3 (association d'entité) fonctionne à plein pour une marque dont le nom apparaît des millions de fois en cooccurrence avec `hubspot.com` sur le web. Ce n'est pas transposable à un site de taille moyenne.

## [À SOURCER]

- **18 % à 41 % (seoengico.com, 13 clients)** : chiffre non vérifiable en source primaire indépendante. L'article reconnaît lui-même ses limites. À ne pas citer comme donnée établie.
- **11 citations vs 2 (seoengico.com)** : cas unique, sans groupe témoin publié.
- **Triplement des citations AI Overviews en 8 semaines** : migration non nommée, taille non précisée, méthode de mesure non publiée.
- **Common Crawl, 288,6 millions d'hôtes vs 134,2 millions de domaines** : cité dans l'article seoengico.com, non re-fetché en source primaire dans cette session.
- **Comportement de PerplexityBot et de Google-Extended sur les sous-domaines** : aucune documentation primaire retrouvée. Les mêmes règles robots.txt s'appliquent par analogie avec ClaudeBot et GPTBot, mais Perplexity et Google ne l'ont pas documenté explicitement en ces termes.
- **Données France** : aucune étude publiée sur ce sujet en contexte francophone.

## Sources

| Intitulé | Organisme | Date | URL | Consulté |
|---|---|---|---|---|
| ClaudeBot documentation — opt-out instructions | Anthropic | 2024 (mis à jour 2026) | https://support.claude.com/en/articles/8896518 | 2026-11-02 |
| GPTBot and OAI-SearchBot documentation | OpenAI | 2026 | https://developers.openai.com/api/docs/bots | 2026-11-02 |
| Subdomain vs Subdirectory for SEO in 2026: What 2,000 Top Sites Do | TheGuideX | Septembre 2026 | https://theguidex.com/insights/subdomain-vs-subdirectory | 2026-11-02 |
| Subdomain vs Subdirectory in 2026: AI Citations | seoengico.com | 2026 | https://seoengico.com/blog/subdomain-vs-subdirectory-2026-ai-citations | 2026-11-02 |
| Subdomain vs Subfolder for AEO: How AI Engines Treat Host Boundaries | Citevera | 2026 | https://citevera.com/blog/subdomain-vs-subfolder-aeo | 2026-11-02 |
| What Drives AI Citations? Data from 129,000 Domains (SE Ranking XGBoost) | SE Ranking via vault | 2026 | (étude citée dans wiki/syntheses, étude 2026-08-21) | 2026-11-02 |
| 2024 Google Search documentation leak — siteFocusScore, siteRadius | Rand Fishkin / SEL | Mai 2024 | https://searchengineland.com/unpacking-googles-massive-search-documentation-leak-442716 | 2026-11-02 |
