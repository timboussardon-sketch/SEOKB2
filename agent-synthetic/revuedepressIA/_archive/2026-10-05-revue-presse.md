---
type: revue-presse
title: Algorithme — édition du 2026-10-05
date: 2026-10-05
auteur: SyntheticBrain
pilier_info_du_jour: Recherche agentique
piliers_breves: [GEO / search IA, Actualité SEO]
---

# Cloudflare publie une grille tarifaire pour son index RAG destiné aux agents IA, facturation au 1er novembre

**Résumé en 5 points :**

- Cloudflare bascule AI Search en version stable le 1er octobre 2026, avec démarrage de la facturation au 1er novembre et un prix public de 0,75 USD par million de tokens indexés ([Cloudflare blog](https://blog.cloudflare.com/ai-search-ga/), [docs Cloudflare](https://developers.cloudflare.com/autorag/platform/limits-pricing/)).
- Grille complète publiée : 0,75 USD/million tokens à l'ingestion, 0,50 USD/million supplémentaires pour le traitement image, 2 USD par Go stocké et par mois, 0,75 USD pour 1 000 requêtes sémantiques, 0,10 USD pour 1 000 requêtes plein texte ([docs Cloudflare](https://developers.cloudflare.com/autorag/platform/limits-pricing/), [PPC Land](https://ppc.land/cloudflare-ai-search-starts-billing-november-1-at-0-75-per-million-tokens/)).
- Enveloppe gratuite mensuelle incluse sur tous les plans Workers : 5 millions de tokens d'ingestion, 10 Go de stockage, 1 000 requêtes sémantiques, 1 000 requêtes plein texte ([Cloudflare blog](https://blog.cloudflare.com/ai-search-ga/)).
- Nouveautés techniques du passage GA : plongements d'images natifs via Qwen3-VL-Embedding, OCR sur PDF scannés, limite de fichier portée de 4 à 10 MiB ([Cloudflare blog](https://blog.cloudflare.com/ai-search-ga/)).
- L'étude Ahrefs 2026 sur les marketeurs IA (300 répondants, publiée le 30 septembre) montre que 7 % publient du contenu IA sans relecture (contre 4 % en 2025) et que 89 % relisent manuellement (contre 80 %) ([PPC Land](https://ppc.land/ahrefs-finds-7-of-ai-using-marketers-publish-mostly-unedited-ai-content/), [Ahrefs](https://ahrefs.com/blog/marketers-ai-content-creation/)).

---

## Info du jour — Recherche agentique

Pilier : **Recherche agentique**. Un service RAG managé grand public arrive sur le marché avec une grille tarifaire publique au token, à la requête et au Go stocké. Pour un consultant SEO ou un éditeur qui construit un corpus propriétaire destiné à être lu par un agent IA, c'est le premier benchmark externe chiffrable.

### Les faits

Cloudflare a annoncé le 1er octobre 2026 que son service AI Search entrait en version stable (General Availability) ([Cloudflare blog, « AI Search is now generally available », Massadas, Duarte, Vinodkumar](https://blog.cloudflare.com/ai-search-ga/)). La page de référence tarifaire de la plateforme a été mise à jour le même jour ([docs Cloudflare, « AI Search — Limits & pricing »](https://developers.cloudflare.com/autorag/platform/limits-pricing/)). PPC Land a publié la synthèse de la grille le 5 octobre, signée Luis Rijo ([PPC Land, « Cloudflare AI Search starts billing November 1 at $0.75 per million tokens »](https://ppc.land/cloudflare-ai-search-starts-billing-november-1-at-0-75-per-million-tokens/)).

Le service existait en bêta ouverte depuis plusieurs mois (anciennement AutoRAG dans la nomenclature interne, pricing en open beta gratuit). La bascule en version stable introduit trois éléments :

- Une grille tarifaire publique, détaillée ligne par ligne.
- Une date d'entrée en vigueur de la facturation : **1er novembre 2026**.
- Un ensemble de capacités techniques nouvelles : embeddings multimodaux Qwen3-VL-Embedding, OCR sur PDF scannés, limite de fichier à 10 MiB au lieu de 4 MiB.

### La grille, telle que publiée

Par unité de facturation, au-delà des enveloppes gratuites :

| Composant | Prix public | Enveloppe gratuite mensuelle |
|---|---|---|
| Ingestion de contenu | 0,75 USD / million de tokens | 5 millions de tokens |
| Traitement image (OCR + embeddings visuels) | +0,50 USD / million de tokens | compris dans les 5 millions ingestion |
| Stockage | 2 USD / Go-mois | 10 Go |
| Requêtes sémantiques (vector / hybride) | 0,75 USD / 1 000 requêtes | 1 000 requêtes |
| Requêtes plein texte | 0,10 USD / 1 000 requêtes | 1 000 requêtes |

Sources de la grille : [documentation Cloudflare publiée le 1er octobre](https://developers.cloudflare.com/autorag/platform/limits-pricing/) et [reprise PPC Land du 5 octobre](https://ppc.land/cloudflare-ai-search-starts-billing-november-1-at-0-75-per-million-tokens/).

La documentation précise que la facturation des tokens d'ingestion se fait **sur les chunks finaux indexés après parsing et découpage**, pas sur le volume brut du fichier source. Les tokens OCR partagent la même enveloppe que l'ingestion texte. Pas d'heure d'instance, pas d'unité de capacité réservée, pas de minimum mensuel.

### Ce que le passage GA change techniquement

Trois ajouts documentés au moment de la GA :

- **Plongements d'images natifs** via le modèle Qwen3-VL-Embedding. Le service encode directement les pixels pour la recherche visuelle, tout en conservant les légendes pour la couche textuelle. Cloudflare documente l'utilisation de Matryoshka Representation Learning pour maintenir des embeddings compacts sans perte d'information ([Cloudflare blog](https://blog.cloudflare.com/ai-search-ga/)).
- **OCR sur PDF scannés** intégré au pipeline d'ingestion.
- **Limite de fichier portée à 10 MiB** (contre 4 MiB en bêta).

### Pourquoi c'est un repère pour un consultant SEO

Jusqu'ici, un éditeur ou un marchand qui voulait exposer un corpus propriétaire (catalogue, documentation, archives) à des agents IA avait quatre options principales : OpenAI Vector Stores (facturation au Go stocké et à l'appel), Google Vertex AI Search / Gemini File Search, Azure AI Search, ou l'auto-hébergement d'un index vectoriel. Les prix affichés variaient fortement d'un fournisseur à l'autre et n'étaient pas tous publics ni comparables au token près.

Avec la grille Cloudflare, il devient possible de **chiffrer explicitement** le coût d'exposer un corpus défini à un agent IA pour une volumétrie donnée. Deux implications opérationnelles immédiates :

1. **Benchmark de coût**. Un corpus marchand de 50 000 fiches produits à 500 tokens moyens post-chunking = 25 millions de tokens, soit 15 USD d'ingestion au prix catalogue (après déduction des 5 millions gratuits). Un corpus éditorial de 100 000 articles à 2 000 tokens moyens = 200 millions de tokens, soit 146,25 USD d'ingestion. Ces chiffres sont désormais vérifiables en externe, pas « négociables commercialement » comme ils l'étaient en bêta.
2. **Signal de maturité du marché RAG managé**. Un acteur d'infrastructure réseau arrive sur le même terrain que les grands fournisseurs de LLM, avec une grille publique. La différenciation ne porte plus sur la disponibilité du service mais sur la latence, la couverture géographique, les modèles d'embedding supportés et la facturation à l'usage.

### Lien doctrine

Ce passage GA actualise directement [[concepts/persistent-wiki-vs-rag]] : le clivage « wiki persistant **ou** index RAG » devient de plus en plus caduc à mesure que les services RAG managés affichent des prix publics. Pour une marque, exposer un corpus structuré via un service tiers facturé au token est maintenant une décision économique chiffrable, pas une option expérimentale. L'implication pour [[concepts/agentic-search]] est que la question « comment me rendre lisible par un agent » se dédouble : être découvrable (indexation côté moteur public) et être consultable (indexation côté corpus privé exposé à l'agent via un index RAG tiers).

Le même raisonnement vaut pour [[concepts/base-publique]] : la base publique reste le canal de confiance pour les requêtes publiques des moteurs IA, mais un index RAG managé devient le canal de confiance pour les requêtes qui portent sur un corpus propriétaire que l'agent est autorisé à consulter.

### Réserves documentées

- La grille publiée est celle du 1er octobre 2026. Rien n'engage Cloudflare à la maintenir après la facturation effective au 1er novembre. Vérifier la page [limits & pricing](https://developers.cloudflare.com/autorag/platform/limits-pricing/) avant toute décision d'achat.
- Les enveloppes gratuites sont incluses sur tous les plans Workers, mais la documentation ne précise pas si elles cumulent entre comptes d'une même organisation.
- Les tokens d'ingestion sont comptés **après parsing et chunking**. Le ratio tokens source / tokens indexés dépend du type de contenu (HTML riche, markdown, PDF natif, PDF scanné). Les estimations ci-dessus sont des ordres de grandeur, pas des engagements de coût.
- Aucune mesure publique indépendante de la latence ou de la qualité du retrieval sur ce service n'est encore disponible. La comparaison avec OpenAI Vector Stores ou Gemini File Search reste à faire côté qualité, pas seulement côté prix.
- Le modèle d'embedding Qwen3-VL-Embedding est documenté par Alibaba, mais aucune mesure publique indépendante n'évalue encore sa performance sur un benchmark de retrieval multimodal face aux concurrents.

### Prédictions datées

- **P-2026-10-05-1** (confiance 0,55, échéance 2026-12-31) : au moins un concurrent direct (OpenAI, Google, Azure, Pinecone, Weaviate Cloud) publiera une grille tarifaire au token ingéré d'ici fin 2026, en réponse à la position publique de Cloudflare.
- **P-2026-10-05-2** (confiance 0,45, échéance 2027-03-31) : au moins un éditeur ou un marchand tier 1 publiera un chiffre de coût mensuel réel d'exposition de son corpus via un service RAG managé public (Cloudflare AI Search, OpenAI Vector Stores ou équivalent), avec volumétrie documentée.
- **P-2026-10-05-3** (confiance 0,40, échéance 2027-06-30) : au moins un cabinet SEO/GEO indépendant publiera une étude comparative latence/qualité/prix entre deux services RAG managés sur un corpus de référence >= 50 000 documents.

---

## Brèves

### 1. Ahrefs chiffre l'édition manuelle du contenu IA : 89 % de relecture, 7 % de publication sans correction (pilier GEO / search IA)

Ahrefs a publié le 30 septembre son enquête 2026 sur l'usage de l'IA dans le marketing de contenu ([Ahrefs blog, Ryan Law](https://ahrefs.com/blog/marketers-ai-content-creation/)), reprise le 1er octobre en communiqué puis le 5 octobre par PPC Land ([PPC Land, Luis Rijo](https://ppc.land/ahrefs-finds-7-of-ai-using-marketers-publish-mostly-unedited-ai-content/)) et par eMarketer ([eMarketer](https://www.emarketer.com/content/ai-content-marketing-2026--confidence-rises--scrutiny)).

L'enquête porte sur environ 300 professionnels du marketing et du SEO, dont 68 cadres dirigeants, interrogés en août 2026. 93 % utilisent une IA pour produire ou assister de la production de contenu, contre 87 % en 2025. Chiffres principaux :

- **7 % publient le contenu IA sans relecture**, contre 4 % en 2025.
- **89 % relisent manuellement** la sortie IA, contre 80 % en 2025.
- **24 % jugent la sortie IA supérieure à l'écriture humaine**, contre 14 % en 2025.
- **85 % rapportent une production plus rapide**.
- **78 % ne signalent pas l'usage de l'IA** à leurs lecteurs.
- **84 % des utilisateurs IA citent Claude** comme outil principal.

Ryan Law, directeur du marketing de contenu chez Ahrefs, résume : « Marketers are clearly becoming more confident in what AI can produce, but that doesn't mean they're handing over the keys. »

L'intérêt pour un consultant SEO est double. D'abord, la part de contenu IA non édité progresse (4 % → 7 %) mais reste minoritaire : la crainte d'une noyade éditoriale sous production IA brute ne se confirme pas à cette taille d'échantillon. Ensuite, le gap entre « 93 % utilisent une IA » et « 78 % ne le signalent pas » est à surveiller : la mise à jour de documentation Google du 1er octobre sur « Using generative AI content » insistait justement sur la relecture critique et le fact-check manuel ([revue de presse Algorithme du 2026-10-03](revuedepressIA/2026-10-03-revue-presse.md), [[concepts/anti-ai-writing]]).

Réserves : échantillon déclaratif de 300 répondants, biais d'auto-sélection probable (lecteurs du blog Ahrefs). Aucune mesure externe de la production IA réelle vs déclarée. Les 84 % Claude peuvent refléter le public de l'enquête plus que le marché global.

### 2. John Mueller lie la lecture des sitemaps à la perception de qualité du site (pilier Actualité SEO)

Dans l'épisode 114 du podcast Search Off The Record publié le 1er octobre 2026, John Mueller et Martin Splitt sont revenus sur l'erreur « Couldn't Fetch » affichée dans Search Console quand Google n'arrive pas à récupérer un sitemap valide ([PPC Land, Luis Rijo, 5 octobre](https://ppc.land/google-may-skip-sitemaps-on-sites-it-deems-low-quality/), [Google Search Central podcast](https://developers.google.com/search/podcasts/2026/10/sitemaps)).

Verbatim Mueller, cité par PPC Land :

> « We actually see this a lot in the forums. And there are primarily two reasons for that. »

> « crawl demand is very often based on the perceived quality of a website. »

Mueller nomme explicitement deux causes à l'erreur sur un sitemap valide : la charge serveur et la demande de crawl, cette dernière étant liée à la perception de qualité du site. Autres précisions de l'épisode, confirmées par la source primaire :

- La balise `priority` dans un sitemap XML est traitée comme maximale pour chaque URL — autrement dit elle n'a plus d'effet opérationnel.
- La balise `changefreq` n'est pas un signal de spam, elle est simplement ignorée.
- `lastmod` est évalué au cas par cas, pas pris pour argent comptant.
- `llms.txt` ne remplace pas un sitemap XML. Mueller : « I would not rely on it. I would not treat that as a priority. »
- Les limites restent 50 000 URLs et 50 Mo décompressés par fichier sitemap.
- Un flux RSS peut servir de sitemap.

Pour un consultant SEO, le fait nouveau exploitable est la **confirmation verbatim** que la perception de qualité du site conditionne la demande de crawl, et donc indirectement la fréquence à laquelle Google va chercher le sitemap. Un site perçu comme faible qualité peut voir son sitemap non récupéré sans que ce soit une erreur technique à corriger : c'est le signal qualité qu'il faut travailler, pas la configuration du serveur. Le rejet explicite de `llms.txt` comme substitut au sitemap XML tranche également un débat ouvert depuis mi-2025.

Réserves : il s'agit d'un podcast de la Search Relations team, pas d'une documentation officielle. Les verbatim sont retranscrits par PPC Land à partir de l'épisode YouTube publié le 1er octobre, et le lien direct vers la fiche officielle de l'épisode est à vérifier sur la page des podcasts Google Search Central. Pas de donnée chiffrée sur le seuil de qualité à partir duquel la demande de crawl chute.

---

*Édition rédigée par SyntheticBrain le 2026-10-05. Rien n'a été envoyé.*
