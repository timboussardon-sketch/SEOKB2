---
type: revue-presse
title: "Algorithme — édition du 28 octobre 2026"
date: 2026-10-28
pilier_info_du_jour: Business SEO
piliers_breves: [Niche SEO, Agentic Search]
tags: [algorithme, revue-presse, business-seo, serp-data, outils-seo, ugc, agentic-search]
created: 2026-10-28
sources: 11
confidence: medium
status: draft
---

# Google corrompt entre 5 et 20 % des SERP livrés aux outils SEO, Ahrefs et Semrush l'écrivent

## En bref

- Ahrefs publie le 22 octobre un bilan vendeur estimant que 5 à 20 % des SERP livrés aux fournisseurs de données SEO sont falsifiés par Google, et dit nettoyer les mesures historiques affectées.
- Semrush confirme à Barry Schwartz que l'anomalie dure depuis la fin de l'été 2026 et dit avoir ajouté des contrôles de filtrage.
- Cloro mesure 71,5 % de SERP corrompus sur sa fenêtre 30 septembre-12 octobre 2026, avec des journées à 83 %, chiffre non audité par un tiers.
- Pilier Business SEO : les scores de difficulté, les estimations de trafic et le suivi AI Overviews reposent sur des données que leurs propres éditeurs qualifient désormais d'instables ; impact direct sur les décisions d'achat de mots-clés, les reportings clients et les benchmarks concurrentiels.
- Brèves : LLM Pulse mesure Reddit à 5,82 % des réponses IA en septembre contre 6,31 % en juillet sur 17 plateformes UGC trackées ; Walmart confirme le déploiement grand public des Agent Profiles dans les comptes Walmart et Sam's Club avant fin novembre 2026.

## Info du jour (pilier Business SEO)

Ahrefs a publié le 22 octobre 2026 un billet signé « An update on Google's poisoning of search results » dans lequel la société évalue la part de résultats falsifiés par Google à **entre 5 % et 20 %, selon le fournisseur de données concerné**. Le billet ajoute qu'Ahrefs « nettoie les résultats historiques susceptibles d'avoir été affectés », formulation reprise par [PPC Land](https://ppc.land/ahrefs-says-google-poisons-5-to-20-of-results-served-to-seo-data-tools/) qui consolide la chronologie des publications depuis septembre.

Barry Schwartz a recueilli une déclaration de Semrush à la même période : « Nous confirmons avoir observé le problème de SERP corrompus, Google renvoyant des résultats inexacts, depuis la fin de l'été. » PPC Land précise que Semrush a « ajouté des contrôles supplémentaires » pour filtrer les résultats, et rappelle que les données SERP de Semrush alimentent les scores de difficulté par mot-clé, les estimations de trafic, l'analyse concurrentielle et le suivi des AI Overviews ([Search Engine Roundtable, 12 octobre 2026](https://seroundtable.com/third-party-google-rank-tracking-broken-42272.html) ; [Search Engine Journal](https://www.searchenginejournal.com/analysis-google-is-poisoning-search-results-for-rank-trackers/592873/)).

Deux mesures tierces encadrent la gravité. [Nozzle](https://ppc.land/google-feeds-rank-trackers-swapped-results-on-8-of-pages-nozzle-finds/), rank tracker, a étudié 27,5 millions de SERP et observé 8,0 % de pages corrompues depuis le 13 septembre 2026, contre 0,17 % avant cette date. [Cloro](https://cloro.dev/blog/google-poisoned-serps/), société d'ingénierie, rapporte entre le 30 septembre et le 12 octobre 2026 une part de 71,5 % de ses pages Google corrompues, avec des journées isolées à 83 %. Les deux échantillons ne sont pas comparables (sondage de rank tracker avec IP résidentielles vs sondage d'un pipeline d'ingestion de données SERP) : ils mesurent deux surfaces différentes du même mécanisme.

Nouveauté de la fenêtre 22-28 octobre : les deux éditeurs d'outils SEO majeurs (Ahrefs, Semrush) publient eux-mêmes leur mesure du problème et le qualifient dans leur voix de marque, après plusieurs semaines de couverture par des tiers (Nozzle, DemandSphere, Cloro). Jusqu'au 20 octobre, les prises de position des vendeurs restaient confinées à des citations courtes dans des articles tiers. Le billet Ahrefs du 22 octobre ouvre une documentation vendeur-côté, mesurée et explicite, avec engagement de retraitement rétroactif.

**Nature du mécanisme (recoupé par Nozzle, Ahrefs, Semrush, Cloro)** : Google livre, à des requêtes qu'il suspecte provenir d'un fournisseur de données SEO ou d'un moteur de réponse qui ingère ses SERP, des résultats complets mais incorrects, plutôt que de les bloquer explicitement. Le site d'une marque, qui apparaît réellement en position 3 pour un mot-clé donné, peut être remonté en position 1 ou disparaître pour l'IP qui scrape. L'utilisateur humain ordinaire, lui, voit les résultats normaux.

**Portée opérationnelle pour un consultant SEO** :

1. **Scores de difficulté par mot-clé** : la mesure repose sur l'identité et l'autorité des URL en SERP. Si 5 à 20 % des SERP sont bruitées, les scores affichés dans Ahrefs et Semrush portent une marge d'erreur asymétrique non quantifiée par leurs éditeurs. Les écarts de score inférieurs à 5 points ne sont plus discriminants.
2. **Estimations de trafic concurrent** : les volumes projetés dépendent du couple position moyenne × volume mensuel. Avec un bruit position de l'ordre de 5-20 %, les estimations individuelles d'URL concurrentes sont, à ce jour, à prendre comme ordres de grandeur. La comparaison entre deux concurrents reste utilisable si les deux URL sont scrapées depuis la même infrastructure et la même fenêtre.
3. **Suivi AI Overviews** : les rank trackers mesurent l'apparition d'un AI Overview sur une requête donnée. Si la page scrapée est falsifiée, la présence ou l'absence d'un AI Overview peut être altérée. Les reportings clients « AIO apparition » doivent, le temps que les filtres vendeurs stabilisent, indiquer explicitement la source de mesure et la méthode (rank tracker, panel navigateur, instrumentation serveur).

Doctrine : la propriété « la mesure de la visibilité organique est instable et dépend de l'instrument » décrite dans [[concepts/tabou-visibilite]] trouve ici un terrain d'application opérationnel. L'arbitrage avec [[concepts/metriques-visibilite-geo]] se durcit : les métriques dépendantes de la position Google scrapée (score difficulté, trafic estimé, SOV concurrentiel) perdent 5 à 20 % de fiabilité ; les métriques dépendantes de la mesure directe (GSC impressions, GSC clics, GA4 sessions) restent intactes. Pour la critique de la fiabilité des outils vendeurs, voir aussi [[concepts/scam-objection-data-aleatoire]].

**Réserves documentées** :
- Les chiffres de Cloro (71,5 % pic 83 %) ne sont pas vérifiés par un auditeur tiers ; échantillon mono-vendor non pondéré.
- Aucune des parties n'a publié sa méthode d'identification du caractère « falsifié » d'un résultat au niveau du mot-clé.
- Google n'a pas commenté publiquement le mécanisme à la date du 28 octobre 2026.
- La durée de persistance de la correction annoncée par Ahrefs (rétro-nettoyage) n'est pas précisée.
- Les éditeurs n'ont pas publié d'estimation de l'impact financier sur leurs clients (abonnements, re-ventes de données).

**Prédictions ouvertes datées** :
- Un éditeur SEO majeur (Ahrefs, Semrush, Sistrix, Moz) publie une documentation méthodologique publique de son filtre anti-poisoning avec un intervalle de confiance affiché avant le 31 mars 2027 (P-2026-10-28-1, confiance 0,55).
- Google ne publie pas de billet officiel sur ce mécanisme avant le 31 décembre 2026 (P-2026-10-28-2, confiance 0,70).
- Un cabinet SEO indépendant publie un recensement comparatif des taux de bruit SERP mesurés sur ≥ 3 fournisseurs avant le 30 avril 2027 (P-2026-10-28-3, confiance 0,45).

## Brève 1 — Pilier Niche SEO : LLM Pulse mesure la part de Reddit dans les réponses IA à 5,82 % en septembre, contre 6,31 % en juillet

[LLM Pulse](https://llmpulse.ai/data-studies/top-ugc-sources) suit 17 plateformes UGC et publie leur part dans les réponses IA sur une fenêtre glissante de 28 jours. La métrique est le pourcentage de réponses qui citent au moins un lien du site concerné, cumulé sur ChatGPT, Perplexity, Gemini et Google AI Overviews.

La trajectoire sur Reddit : 6,31 % (juillet 2026) → 5,82 % (septembre 2026). Baisse relative de 7,8 %. La mesure parallèle d'Ahrefs sur son [Benchmark UGC Citations](https://ahrefs.com/benchmarks/ugc-citations) suit un panel comparable.

Ces chiffres succèdent au programme UGC Fresh Data documenté par Google le 8 octobre 2026, qui met en place un canal d'ingestion dédié pour les plateformes communautaires validées (déjà traité en info du jour 2026-10-11). Le programme ne garantit ni l'indexation ni la citation. La trajectoire Reddit observée par LLM Pulse laisse ouverte la question : la stabilisation observée est-elle le signe d'un plafond atteint pour Reddit sur ces moteurs, ou l'effet d'un partage de ressources inter-plateformes au sein du quota moteur ?

Doctrine : [[concepts/metriques-visibilite-geo]], angle décomposition par plateforme UGC d'une mesure Share of Voice cross-moteur IA. Signal pour l'audit d'une marque B2B/B2C qui investit un play Reddit (community posting) : la part de citations IA venant de Reddit semble baisser trimestre après trimestre, à surveiller sur un échantillon tiers.

**Réserves** : LLM Pulse est un éditeur commercial de solution AI visibility, ses chiffres sont auto-publiés sans audit tiers. Le découpage par moteur n'est pas restitué dans la vue publique. La fenêtre 28 jours lisse les pics intra-mensuels.

## Brève 2 — Pilier Agentic Search : Walmart confirme le déploiement grand public des Agent Profiles dans les comptes Walmart et Sam's Club avant fin novembre 2026

Après l'annonce du 21 octobre 2026 du lancement de l'Agent Gateway (serveur MCP Walmart ouvert aux agents IA tiers autorisés, voir édition 2026-10-23), Walmart précise la mise à disposition grand public : les options Agent Profiles apparaîtront dans les comptes Walmart et Sam's Club **avant fin novembre 2026**. Le dispositif de plafonds de dépense annoncé (50, 100 ou 200 USD par agent, avec option d'approbation par achat) devient opérable côté client final à cette échéance ([TechCrunch, 21 octobre 2026](https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/)).

La fenêtre est courte (environ 3 semaines) et aucune liste d'agents partenaires n'est publiée à la date du 28 octobre. Walmart dit se réserver le droit de suspendre le dispositif à tout moment.

Contexte juridique parallèle : Perplexity a déposé une motion to dismiss contre la plainte amendée d'Amazon devant le District Court du Northern District of California. La date d'audience sur cette motion n'est pas confirmée publiquement à ce jour. L'injonction préliminaire accordée à Amazon en mars 2026, puis temporairement suspendue en appel, laisse Perplexity Comet opérationnel sur Amazon tant que le fond n'est pas tranché.

Doctrine : [[concepts/agentic-search]]. Walmart documente un canal où la relation marchand-agent est médiée par le marchand (Agent Profiles côté compte client, MCP server côté infrastructure), à l'inverse du dispositif Universal Cart où le panier est opéré par Google. Les deux modèles coexistent et ne se substituent pas.

**Réserves** : la date « avant fin novembre » n'est pas rendue précise par Walmart. Les plafonds de dépense sont annoncés mais, selon une source, « n'existent pas encore » techniquement. L'extension à Sam's Club est annoncée sans détail d'intégration technique.

## Sources

- [Ahrefs says Google poisons 5 to 20% of results served to SEO data tools (PPC Land, 22 octobre 2026)](https://ppc.land/ahrefs-says-google-poisons-5-to-20-of-results-served-to-seo-data-tools/)
- [Google feeds rank trackers swapped results on 8% of pages, Nozzle finds (PPC Land)](https://ppc.land/google-feeds-rank-trackers-swapped-results-on-8-of-pages-nozzle-finds/)
- [Third-party Google rank tracking broken (Search Engine Roundtable, 12 octobre 2026)](https://seroundtable.com/third-party-google-rank-tracking-broken-42272.html)
- [Analysis: Google is poisoning search results for rank trackers (Search Engine Journal)](https://www.searchenginejournal.com/analysis-google-is-poisoning-search-results-for-rank-trackers/592873/)
- [Poisoned Google SERPs: what we measured and how we fixed it (Cloro)](https://cloro.dev/blog/google-poisoned-serps/)
- [An update on Google's poisoning of search results (Ahrefs, 22 octobre 2026)](https://ahrefs.com/blog/google-search-results-poisoning-update/)
- [Top UGC Sources cited by AI (LLM Pulse)](https://llmpulse.ai/data-studies/top-ugc-sources)
- [UGC AI Visibility Trends (Ahrefs Benchmarks)](https://ahrefs.com/benchmarks/ugc-citations)
- [While Amazon blocks AI agents, Walmart rolls out the welcome mat (TechCrunch, 21 octobre 2026)](https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/)
- [Walmart sets the rules for AI shopping agents (ActuIA)](https://www.actuia.com/en/news/walmart-sets-the-rules-for-ai-shopping-agents/)
- [Perplexity AI moves to dismiss Amazon's amended US claims over AI agents (MLex)](https://www.mlex.com/mlex/artificial-intelligence/articles/2537838)

---

*SyntheticBrain, édition du 28 octobre 2026. Draft, rien n'a été envoyé.*
