---
type: revue-presse
title: "Algorithme — édition du 2026-10-08"
date: 2026-10-08
pilier_info_du_jour: GEO / search IA
piliers_breves: [Niche SEO, Actualité SEO, Business SEO]
sources_consultees: 10
sources_nouvelles: 2
tags: [algorithme, geo, cross-engine, measurement, local-seo, google-business-profile, crawl-rate, retry-after, reputation-management]
status: draft
---

# Algorithme — édition du 2026-10-08

## Résumé

- Un papier arXiv publié le 19 septembre 2026 par Benjamin Tannenbaum (arXiv 2609.22655) mesure la divergence entre les URL citées par ChatGPT, Microsoft Copilot, Google et Perplexity sur 15 prompts commerciaux (589 citations) et conclut qu'un score GEO moteur-indépendant ne peut estimer que la pertinence page-requête, pas la visibilité finale ([arXiv 2609.22655](https://arxiv.org/abs/2609.22655)).
- Un bouton WhatsApp apparaît dans le panneau local Google aux côtés de Call, Directions, Website et Share, repéré par Sachin Patel et reproduit par Barry Schwartz le 7 octobre 2026, sans annonce officielle Google ni périmètre pays publié ([Search Engine Roundtable](https://www.seroundtable.com/google-local-panel-whatsapp-button-42230.html)).
- Google restructure sa page « Reduce the Google crawl rate » le 6 octobre 2026 et déplace l'exemple de l'en-tête HTTP Retry-After depuis une autre page vers la section d'urgence, pour les codes 503 et 429 ([Google developers via changelog](https://developers.google.com/crawling/docs/crawlers-fetchers/reduce-crawl-rate), [Search Engine Roundtable](https://www.seroundtable.com/google-crawl-rate-documentation-update-42247.html)).
- Erase publie dans Search Engine Journal le 6 octobre 2026 un contenu sponsorisé analysant 22 620 liens soumis pour retrait entre janvier et septembre 2026 : délai médian de retrait réussi 18 jours tous types confondus, 9 jours pour les court records et people-search listings, 28 jours pour les articles de presse ([Search Engine Journal, sponsored](https://www.searchenginejournal.com/negative-search-result-removal-erase-spa/590856/)).

---

## Info du jour — GEO / search IA : un papier formalise la mesure de la visibilité IA en quatre étapes et quantifie la divergence inter-moteurs

**Événement.** Benjamin Tannenbaum publie sur arXiv le 19 septembre 2026 le papier « Scoring With the Engine: Retrieval Exposure, Cross-Engine Divergence, and the Limits of Engine-Agnostic GEO Scores » ([arXiv 2609.22655](https://arxiv.org/abs/2609.22655)). Le papier est un audit observationnel sur 15 prompts commerciaux fixes exécutés le 6 juin 2026 sur quatre moteurs IA : ChatGPT, Microsoft Copilot, Google (AI Mode / AI Overviews selon les prompts), Perplexity. 589 observations de citation, 528 URL uniques, 356 domaines distincts.

**Le cadre proposé.** Le papier distingue quatre quantités, à mesurer séparément plutôt que mélangées dans un score composite :

1. Page fit (adéquation page-requête) : la qualité intrinsèque d'une page relativement à une intention de recherche, mesurable sans interroger un moteur en direct.
2. Exposure (exposition par le moteur) : la probabilité qu'un moteur donné sélectionne la page dans son retrieval, dépendante de l'index, du reranker et des règles du moteur.
3. Selection (sélection comme citation) : la probabilité qu'une page exposée soit effectivement citée dans la réponse générée, conditionnelle à l'exposition.
4. Visibility (visibilité finale) : le produit observable d'exposure et selection.

**Les chiffres de divergence inter-moteurs.** Sur les paires d'engines appariées (10 prompts observés sur les quatre moteurs) :
- Jaccard pairwise moyen sur URL exactes : 0,0079.
- Médiane Jaccard pairwise : 0,0000.
- 84,9 % des paires d'engines ne partagent aucune URL citée pour la même requête ; sur l'overlap top-5, 0 % de recouvrement dans les 60 comparaisons pairwise.
- Un modèle hypergéométrique attendrait 0,1272 de Jaccard moyen : le réel observé est environ 5,7 % de l'attendu.
- Un moteur unique capture entre 11,4 % et 42,6 % de l'union des URL des quatre moteurs. 96,4 % des URL observées n'apparaissent que sur un seul moteur.
- Turnover intra-engine (5 au 6 juin 2026) : 67,0 % en moyenne. Même moteur, même requête, 24 h d'écart : les deux-tiers des URL sortent et rentrent.

**Lecture doctrine (pilier GEO ancré sur [[concepts/metriques-visibilite-geo]]).** La fiche doctrine distingue déjà apparition d'une marque dans la réponse, densité de citation, position relative. Le cadre Tannenbaum ajoute une étape amont (exposure, qui précède la sélection) et une étape aval (visibility, qui compose les deux). Deux conséquences méthodologiques émergent :

(a) Un score GEO calculé sans interroger un moteur ne peut, par construction, informer que la page fit. Les scores vendor cités en breves d'éditions précédentes (Rankability, TRM, Konabayev, Semrush AI Visibility, Ahrefs Brand Radar, Profound, AirOps) qui agrègent des métriques observationnelles multi-moteurs mélangent les quatre quantités.

(b) La turnover intra-engine 67 % en 24 h impose de dater toute mesure de citation IA au jour près et de ne pas comparer deux mesures prises à plus de 24 h d'intervalle sans réserve explicite. [[concepts/metriques-visibilite-geo]] mentionne déjà l'instabilité ; le papier fournit la première borne quantitative publiée.

**Corroborations historiques.** Le finding « cross-engine divergence sévère » n'est pas isolé : surfacedby (juin 2026, 127 198 citations, 11 647 domaines, 5 moteurs, recouvrement 2,7 % sur les 5 moteurs, 69,6 % des domaines ne sont cités que par un seul moteur) et Digital Authority Partners (juin 2026, 17 % overlap max Perplexity-AIO, 78-85 % domaines uniques par plateforme) donnent le même sens de l'écart avec des méthodologies et des périmètres différents. Le papier Tannenbaum est le premier à poser une baseline statistique (hypergéométrique) explicite et à décomposer en quatre étapes nommées.

**Lectures opérationnelles.**
1. Pour un consultant GEO, l'audit d'une marque sur plusieurs moteurs IA se décompose en quatre mesures séparées plutôt qu'en un seul score composite. L'écart « citations ChatGPT vs Perplexity » n'est pas une anomalie à corriger ; c'est la variance attendue d'un système à quatre moteurs à sélection divergente.
2. Pour un éditeur, la question « ma page apparaît-elle en citation ? » dépend d'abord de l'exposition par le moteur. Une page avec une page fit forte mais non exposée reste invisible. Les outils d'audit qui mesurent sans distinguer exposure et selection diluent la responsabilité éditoriale.
3. Pour un benchmark GEO reproductible, la fenêtre de mesure doit être resserrée à moins de 24 h sur la même requête ; au-delà, 67 % de turnover intra-engine impose une réserve statistique explicite.
4. Pour un rapport client, la différence « 15 % de citations sur Perplexity vs 3 % sur ChatGPT » ne devrait pas être présentée comme un déséquilibre à corriger mais comme une structure du marché à quatre moteurs à sélection faiblement corrélée.
5. Pour un consultant qui vend un score GEO composite, l'auditabilité du score impose aujourd'hui de nommer explicitement les quatre quantités mesurées et de dire laquelle (page fit, exposure, selection, visibility) le score prétend informer.

**Réserves documentées.**
1. Le papier repose sur un seul jour d'observation (6 juin 2026) et une seconde journée pour la mesure de turnover (5-6 juin). Pas de reproduction publique indépendante à ce jour. Préprint arXiv, pas de peer-review.
2. 15 prompts commerciaux : échantillon étroit, pas de ventilation par vertical ni par type de requête (Know vs Do). Le papier ne publie pas la liste des prompts, ce qui limite la reproduction exacte.
3. Les quatre moteurs testés incluent Google (sans distinguer AI Mode des AI Overviews dans l'ensemble pairwise) ; la publication ne détaille pas la part de prompts qui ont déclenché chaque surface Google.
4. Aucune ventilation par type de citation (lien éditeur, Wikipedia, Reddit, YouTube) n'est publiée. La divergence pourrait être portée à l'excès par les sources communautaires (Reddit, forums) qui varient par moteur, et moins marquée sur les sources institutionnelles (Wikipedia, sites officiels).
5. Le cadre à quatre étapes est posé mais pas opérationnalisé : le papier ne propose pas une méthode de mesure directe de l'exposure sans accès à l'index moteur, et reconnaît que les scores engine-agnostic restent une approximation de page fit.

**Prédictions.**
- **P-2026-10-08-1** (confiance 0,55) : un second papier académique indépendant, non lié à Tannenbaum ni à Vishwakarma (SIGIR 2605.25517), publie d'ici le 2027-06-30 une mesure de cross-engine divergence sur ≥ 4 moteurs avec ≥ 500 prompts et confirme un Jaccard pairwise moyen inférieur à 0,05. Résolution : arXiv ou proceedings peer-reviewed dans la fenêtre.
- **P-2026-10-08-2** (confiance 0,50) : un cabinet SEO/GEO (hors Semrush, Ahrefs, Profound déjà cités) publie d'ici le 2027-03-31 un rapport reprenant les quatre étapes nommées (page fit, exposure, selection, visibility) et distinguant les mesures correspondantes. Résolution : rapport public du cabinet repéré dans la fenêtre.
- **P-2026-10-08-3** (confiance 0,40) : Google ou OpenAI publie d'ici le 2027-06-30 une documentation partielle de l'exposure (fraction des pages retrievées) distincte de la selection (fraction des pages citées). Résolution : page developers.google.com ou openai.com officielle dans la fenêtre.

---

## Brèves

### Brève 1 — Niche SEO : un bouton WhatsApp dans le panneau local Google

Le 7 octobre 2026, Barry Schwartz publie sur Search Engine Roundtable l'observation d'un bouton WhatsApp dans le panneau local Google, à partir d'un signalement de Sachin Patel sur X et sur Search Engine Watch, et confirme la reproduction sur ses propres requêtes ([Search Engine Roundtable, 7 oct 2026](https://www.seroundtable.com/google-local-panel-whatsapp-button-42230.html)). Le bouton s'affiche soit en substitution du bouton chat existant, soit en ajout aux boutons Call, Directions, Website et Share. Son action : démarrer un chat WhatsApp directement depuis la SERP sans ouvrir une page intermédiaire.

Google n'a pas publié d'annonce officielle à la date de cette édition : pas de billet Google Search Central, pas de post Danny Sullivan ni John Mueller, pas de documentation support.google.com datée du 6 ou 7 octobre. Les pays, verticaux et types d'entreprises concernés ne sont pas documentés. Schwartz rappelle que Google avait, plusieurs trimestres avant cette observation, demandé aux fiches Google Business Profile de renseigner le champ WhatsApp, et avait rempli lui-même ce champ pour certaines fiches sans intervention du propriétaire.

Pour un marchand local, la décision opérationnelle est la capacité à traiter un flux de messages WhatsApp sans dégrader l'expérience, pas l'activation technique. Un restaurant qui reçoit 20 chats WhatsApp par jour n'est pas comparable à une chaîne nationale avec un seul numéro de contact. Pour une agence locale qui gère plusieurs fiches, la variable à surveiller est la part des clics issus du panneau local qui bascule vers WhatsApp au détriment des Direction ou Call, mesure que les tableaux de bord Google Business Profile ne distinguent pas aujourd'hui.

Réserves : (1) périmètre géographique non documenté ; (2) règle d'affichage substitution vs ajout non documentée ; (3) absence d'annonce officielle Google ; (4) pas de mesure publique d'impact sur taux d'appel ou de direction ; (5) incertitude sur le statut du test ou du déploiement complet.

### Brève 2 — Actualité SEO : Google déplace l'exemple Retry-After dans la page de réduction du crawl

Le 6 octobre 2026 à 14h59 ET, Barry Schwartz rapporte sur Search Engine Roundtable la mise à jour de la page Google « Reduce the Google crawl rate » ([Search Engine Roundtable, 6 oct 2026](https://www.seroundtable.com/google-crawl-rate-documentation-update-42247.html)). Le changelog Google indique en verbatim : « Restructured the emergency crawl rate reduction section and added information and examples about the Retry-After HTTP header. » La page source est [developers.google.com, Reduce the Google crawl rate](https://developers.google.com/crawling/docs/crawlers-fetchers/reduce-crawl-rate).

Le fond technique est inchangé : les crawlers Google traitaient déjà les codes HTTP 503 et 429 comme signal de réduction du crawl. L'en-tête Retry-After, défini par la RFC 9110, indique au crawler quand revenir, soit comme délai en secondes, soit comme date UTC absolue. L'édition déplace l'exemple de code depuis la page « Temporarily pause or disable a website » vers la section d'urgence de la page de réduction du crawl, et le présente comme signal explicite accompagnant 503 et 429.

Pour un SEO technique en crise de capacité serveur (DDoS, migration, pic de trafic non prévu), l'intégration explicite de Retry-After dans la page d'urgence rend la bonne pratique plus visible : renvoyer un 503 nu laisse le crawler relancer avec son propre backoff ; renvoyer 503 + Retry-After permet de communiquer un délai précis. Le mécanisme de throttling côté Google n'est pas modifié ; l'impact SEO reste nul sur les sites qui ne subissent pas d'incident capacité.

Réserves : (1) la mise à jour est documentaire, pas comportementale ; (2) aucun seuil Retry-After maximum n'est documenté publiquement ; (3) la mise à jour s'applique à Googlebot (search), ne précise rien sur Google-Extended ou GoogleOther pour l'IA ; (4) aucun chiffre public d'adoption de l'en-tête par les sites.

### Brève 3 — Business SEO : Erase publie un dataset sponsorisé de 22 620 liens soumis pour retrait, 18 jours de médiane

Le 6 octobre 2026, Nicholas Lonski (Director of Demand Generation, Erase.com) publie dans Search Engine Journal un contenu sponsorisé analysant 22 620 liens soumis pour retrait entre le 1er janvier et le 21 septembre 2026, sur environ 1 650 sites ([Search Engine Journal, sponsored, 6 oct 2026](https://www.searchenginejournal.com/negative-search-result-removal-erase-spa/590856/)). SEJ marque explicitement le contenu comme sponsorisé.

Les chiffres clés, tels que publiés par Erase :
- Délai médian de retrait pour les cas réussis : 18 jours tous types confondus. 71 % des retraits réussis confirmés sous 30 jours, 91 % sous 90 jours.
- Par catégorie : court records 9 j (89 % sous 30 j), people-search listings 9 j (84 %), mugshots 11 j (93 %), social media posts 14 j (79 %), Google reviews 19 j (67 %), news articles 28 j (51 %).
- Full removal 14 j médian, de-indexing 21 j médian.
- Les Google reviews représentent 52 % des liens soumis ; environ 1 Google review supprimée sur 10 a nécessité plus de 90 jours.
- Les sites gouvernementaux « ont rarement accepté le retrait ». TikTok et YouTube sont les plateformes les plus difficiles hors cas copyright ou contenu nuisible.

Le fait brut pour un consultant SEO qui vend du reputation management est que la vitesse de retrait varie d'un facteur 3 entre les court records (9 j médian) et les news articles (28 j médian). Pour un client en situation de crise de notoriété, la hiérarchisation des actions a un impact direct sur le délai avant stabilisation : commencer par les sources où le retrait est documenté comme rapide, puis traiter les plus lentes en parallèle.

Réserves fortes : (1) le dataset est auto-déclaré par un vendeur du service ; aucun audit tiers n'est fourni ; (2) sponsored content, pas article de presse ; les chiffres ne sont pas vérifiables indépendamment ; (3) le périmètre est US, aucune mention de législation RGPD (droit à l'oubli) qui a sa propre mécanique ; (4) les clients ayant pausé ou annulé sont exclus des comparaisons ; (5) le dataset couvre les retraits réussis, pas la probabilité globale de succès ; (6) 3 500 liens images inclus dans le total mais exclus des catégories.

---

*Édition rédigée par SyntheticBrain, 2026-10-08. Sources primaires consultées : arxiv.org, developers.google.com. Sources secondaires : Search Engine Roundtable (Barry Schwartz), Search Engine Journal (Erase sponsored). Aucune publication, draft seul.*
