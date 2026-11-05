# Reddit tient 18,5 % des citations Google AI Overviews et tombe à 0,52 % dans ChatGPT

## En bref

- Ahrefs a rafraîchi le 2 septembre 2026 son index des cinquante domaines les plus cités par Google AI Overviews sur plus de 3 millions de requêtes US : Reddit reste deuxième à 18,5 % de mention share, YouTube premier à 22,9 %, cf. [Ahrefs — The 50 Most-Cited Websites in Google AI Overviews](https://ahrefs.com/blog/most-cited-domains-ai-overviews/).
- Dans le même intervalle mesuré, la part Reddit dans les citations de ChatGPT Search est passée de 3,83 % (18 juillet-7 août) à 0,52 % (14-17 août), soit une baisse relative de 86,4 %, cf. [Promptwatch — Why Did ChatGPT Stop Citing Reddit](https://promptwatch.com/blog/chatgpt-stop-citing-reddit) et [Axios — Reddit fades from ChatGPT citations](https://www.axios.com/2026/08/20/chatgpt-reddit-citations-geo-strategy).
- Conséquence opérationnelle : un audit de visibilité IA mono-moteur donne une image trompeuse ; la même source peut peser vingt fois plus dans un moteur que dans un autre sur la même fenêtre.
- Le top 10 Ahrefs Sept. 2026 concentre 82,2 % de la mention share sur des plateformes ouvertes (UGC vidéo, forums, réseaux sociaux, Wikipédia, marketplaces) ; les sites de marque sortent pratiquement du décor à ce niveau d'agrégation.
- Deux vendors (Ahrefs, Semrush) formalisent en parallèle un modèle d'indice mensuel d'AI visibility rafraîchi automatiquement, cf. brève B1.

---

## Info du jour — pilier GEO

### Le fait

Ahrefs a mis à jour le 2 septembre 2026 son article « The 50 Most-Cited Websites in Google AI Overviews », rafraîchi automatiquement chaque mois par Agent A, l'agent interne de la société. La méthodologie s'appuie sur plus de 3 millions de requêtes US couvrant tous les sujets et sur les données de Brand Radar. La métrique publiée est la mention share : la part d'un domaine dans le total des citations des cinquante premières sources.

Le top 10 de septembre 2026 se lit comme suit ([Ahrefs](https://ahrefs.com/blog/most-cited-domains-ai-overviews/)) :

| Rang | Domaine | Mention share |
|---|---|---|
| 1 | youtube.com | 22,9 % |
| 2 | reddit.com | 18,5 % |
| 3 | facebook.com | 10,1 % |
| 4 | google.com | 8,8 % |
| 5 | instagram.com | 5,6 % |
| 6 | quora.com | 4,7 % |
| 7 | en.wikipedia.org | 4,0 % |
| 8 | tiktok.com | 3,3 % |
| 9 | amazon.com | 3,3 % |
| 10 | walmart.com | 1,0 % |

Le cumul des dix premiers domaines atteint 82,2 % de la mention share du top 50. Les six plateformes UGC sociales et forums (YouTube, Reddit, Facebook, Instagram, Quora, TikTok) totalisent à elles seules 65,1 %.

### Le contraste cross-moteur

Sur la même fenêtre calendaire, Promptwatch et Axios ont documenté une chute abrupte de Reddit côté ChatGPT Search ([Promptwatch — 20 août 2026](https://promptwatch.com/blog/chatgpt-stop-citing-reddit), [Axios — Reddit fades from ChatGPT citations, 20 août 2026](https://www.axios.com/2026/08/20/chatgpt-reddit-citations-geo-strategy)) : la part Reddit dans les citations ChatGPT est passée de 3,83 % en moyenne du 18 juillet au 7 août à 0,52 % du 14 au 17 août, soit une baisse relative de 86,4 %. Promptwatch a également relevé sur la même fenêtre une baisse de 11 % dans Google AI Overviews et de 31 % dans Google AI Mode, deux ordres de grandeur en dessous de ce qui a été observé côté ChatGPT.

Le point non trivial : Reddit reste deuxième citation source dans Google AI Overviews (18,5 % au 2 septembre), tandis que le domaine sort presque du référentiel dans ChatGPT. Sur la même période, sur la même source, on lit deux réalités opposées selon l'agent qui rend la réponse.

### Ce que la mesure suggère et ce qu'elle ne dit pas

Ce que la mesure établit :

1. La distribution des citations d'un domaine n'est pas transférable d'un moteur à l'autre. Un même contenu peut être surreprésenté chez l'un et absent chez l'autre.
2. Les plateformes UGC sociales dominent le référentiel Google AI Overviews sur un échantillon US large. Les six sociales et forums (YouTube, Reddit, Facebook, Instagram, Quora, TikTok) captent près des deux tiers de la mention share concentrée dans le top 50.
3. La mesure GEO qui se limite à un seul agent est structurellement incomplète. La direction (croissance ou déclin) d'une part de citation dans un moteur n'implique rien sur les autres moteurs.

Ce qu'elle ne dit pas :

- La cause exacte du décrochage Reddit dans ChatGPT n'est pas documentée publiquement par OpenAI. Promptwatch pointe une variation méthodologique de la sélection des sources ; ce reste une hypothèse externe.
- La mention share Ahrefs mesure la concentration relative dans le top 50 : une hausse pour un domaine implique mécaniquement une baisse pour d'autres. Il faut donc distinguer part de voix relative et volume absolu de citations.
- Aucune des deux sources ne mesure le clic sortant vers la source citée. La citation n'est pas la visite. La distinction reste posée par [[concepts/tabou-visibilite]].
- L'échantillon Ahrefs est US only. La distribution peut différer sur d'autres marchés.

### Lien doctrine

- [[concepts/metriques-visibilite-geo]] : la mesure GEO doit être segmentée par moteur, faute de quoi on additionne des indicateurs non commensurables. Le référentiel Reddit à 18,5 % dans AIO et 0,52 % dans ChatGPT en donne le cas d'école.
- [[concepts/tabou-visibilite]] : la citation dans un moteur générative n'est pas la visibilité, ni la conversion. La discipline de nommer la métrique et son moteur reste centrale.
- [[concepts/agentic-search]] : chaque agent (Google AI Overviews, Google AI Mode, ChatGPT Search, Perplexity, Copilot) possède son propre référentiel de sources. La stratégie GEO devient une matrice moteur × niche, pas une note unique.
- [[concepts/entites-vectorielles]] : la concentration des citations sur YouTube, Reddit, Facebook, Instagram, Quora, TikTok indique que la présence de la marque dans les corpus des grandes plateformes sociales est un signal d'entrée dans le référentiel de citation Google AI, indépendamment du positionnement sur les pages de marque.

### Trois lectures opérationnelles pour un consultant SEO/GEO

1. Reconstruire tout audit d'AI visibility en matrice moteur × niche, jamais en agrégat. Un audit qui donne « part de citation moyenne cross-moteur » masque le fait que la moyenne peut être portée par un seul moteur.
2. Réévaluer la place de Reddit dans le mix GEO client : Reddit reste un pari solide côté Google AI Overviews (18,5 %, deuxième domaine cité) mais perd sa portance côté ChatGPT. Une marque exposée à un mix client majoritairement ChatGPT ne doit pas surinvestir Reddit sur les prochains mois sans nouvelle mesure indépendante.
3. Mesurer côté Google AI Overviews la présence de la marque et de ses porte-parole sur les six grandes plateformes sociales du top 10 (YouTube, Reddit, Facebook, Instagram, Quora, TikTok). C'est le sous-ensemble qui capte 65,1 % de la mention share concentrée dans le top 50.

### Trois prédictions datées

- P-2026-09-06-1 : la mention share Reddit dans le refresh Ahrefs de décembre 2026 reste au-dessus de 15 % côté Google AI Overviews (échéance 31 décembre 2026, confidence 0,55).
- P-2026-09-06-2 : la part Reddit dans les citations ChatGPT Search mesurée par un outil tiers (Promptwatch, OtterlyAI, Peec AI, Profound) reste sous 2 % pour au moins trois mois consécutifs avant le 31 mars 2027 (confidence 0,60).
- P-2026-09-06-3 : au moins un outil GEO tiers publie avant le 31 décembre 2026 un rapport documentant l'écart cross-moteur d'un domaine tiers non Reddit (par exemple Wikipedia, Quora, Amazon) supérieur à 5x entre son AIO mention share et sa ChatGPT citation share (confidence 0,45).

---

## Brève 1 — pilier Actualité SEO

### Deux vendors formalisent en parallèle un modèle d'indice mensuel d'AI visibility

Le refresh Ahrefs du 2 septembre 2026 s'accompagne d'un fait méthodologique noté explicitement dans le blog : l'article est « generated and automatically kept up to date every month by Agent A », l'agent SEO interne d'Ahrefs qui pousse les données Brand Radar puis recalcule les métriques ([Ahrefs](https://ahrefs.com/blog/most-cited-domains-ai-overviews/)). En parallèle, Semrush annonce le 4 septembre 2026 sur Search Engine Land la conférence Spotlight (Londres, 13 octobre 2026) et affiche un chiffre inédit issu de son propre index AI visibility : sur 1 094 catégories analysées, seulement 15,2 % ont un leader clair, 85 % restant sans propriétaire de la conversation, cf. [Search Engine Land — 4 septembre 2026, Semrush is bringing AI visibility under the Spotlight](https://searchengineland.com/semrush-is-bringing-ai-visibility-under-the-spotlight-487137).

Le fait éditorial : deux vendors majeurs (Ahrefs, Semrush) formalisent la mesure d'AI visibility comme un indice de référence rafraîchi automatiquement, sur le même modèle historique que les indices Sistrix Visibility, Semrush Sensor ou Mozcast pour Google Search. Ce n'est pas une étude ponctuelle, c'est une infrastructure éditoriale mensuelle qui s'installe.

Trois précisions méthodologiques pour un consultant qui utilise ces indices :

- La mention share Ahrefs mesure la concentration relative dans le top 50 (dénominateur = citations du top 50 seulement). Elle n'est pas la « part de citation absolue » toute source confondue.
- Semrush publie son chiffre 15,2 % de leaders clairs sur un dénominateur de 1 094 catégories marketing, sans détail public de la définition « leader clair » ni de la méthodologie d'agrégation. Le chiffre est utilisable comme signal directionnel de fragmentation, pas comme benchmark reproductible.
- Ni Ahrefs ni Semrush ne publient encore la variance mois-sur-mois de leurs indices. Sans historique de variance, la comparabilité inter-mois d'un mouvement de 1 à 2 points n'est pas établie.

Le point pour l'analyste : ces indices deviennent des références citables (rapports client, décks commerciaux) mais restent des mesures vendor. La discipline d'audit consiste à recouper au moins deux vendors et à ne jamais publier un mouvement sub-décile de mois en mois comme un signal.

---

## Brève 2 — pilier Actualité SEO

### Google Ads teste des match types restrictifs dans AI Mode, suite du signal du 4 septembre

Anthony Higman a signalé le 4 septembre 2026 sur LinkedIn et X que des mots-clés en correspondance exacte et en expression exacte devenaient éligibles à servir des annonces texte dans Google AI Mode, cf. [Search Engine Roundtable — Google Ads Testing Serving Restrictive Match Types In AI Mode](https://www.seroundtable.com/google-ads-serving-restrictive-match-types-ai-mode-42024.html). Ginny Marvin, Google Ads Liaison, a confirmé publiquement qu'il s'agissait d'une expérimentation limitée, éligible aux requêtes portant une intention utilisateur explicite et directe.

Cette évolution modifie un point structurel du dispositif d'annonce dans AI Mode : jusqu'ici, seuls les modèles AI Max, Performance Max ou correspondance large avec enchères intelligentes étaient éligibles à servir dans les surfaces génératives. L'extension aux match types restrictifs, même dans un périmètre restreint, ouvre pour la première fois un canal de contrôle serré du ciblage à l'intérieur d'AI Mode.

Trois éléments méthodologiques restent ouverts et à surveiller :

- Le périmètre exact de « intention utilisateur explicite et directe » n'est pas encore documenté publiquement par Google Ads. La reproductibilité de l'expérimentation par un second annonceur ou une agence PPC tierce dans les 7 à 14 prochains jours conditionne la portée du signal.
- La documentation Google Ads Help n'a pas été mise à jour au 6 septembre 2026 pour refléter cette éligibilité. En l'absence de help page confirmée, le fait reste un test annoncé par un liaison Google, pas une règle produit stabilisée.
- L'impact sur la volatilité des CPC ou du CTR dans le périmètre AI Mode n'est pas mesuré publiquement à ce stade. Un outil PPC tiers (Optmyzr, Adalysis, WordStream) qui publierait dans les 30 prochains jours une note technique documentant l'écart avant/après serait un signal fort pour actualiser la pratique.

Le point pour l'analyste : ce test PPC porte un signal indirect côté SEO/GEO. Il indique que Google ouvre la surface générative AI Mode à des dispositifs de ciblage plus stricts côté payant, ce qui présuppose que la surface est suffisamment mature pour supporter une friction commerciale plus ferme. C'est un indicateur produit de stabilisation d'AI Mode, distinct des mesures de volatilité ou de citation habituelles.

---

## Sources principales de l'édition

- [Ahrefs — The 50 Most-Cited Websites in Google AI Overviews (September 2026)](https://ahrefs.com/blog/most-cited-domains-ai-overviews/) — publication et refresh 2 septembre 2026, méthodologie Brand Radar, 3M+ requêtes US, refresh Agent A.
- [Promptwatch — Why Did ChatGPT Stop Citing Reddit ? Inside the August 2026 Citation Collapse](https://promptwatch.com/blog/chatgpt-stop-citing-reddit) — mesure de la part Reddit dans les citations ChatGPT Search, fenêtre 18 juillet-17 août 2026.
- [Axios — Reddit fades from ChatGPT citations, 20 août 2026](https://www.axios.com/2026/08/20/chatgpt-reddit-citations-geo-strategy) — corroboration primaire indépendante de la mesure Promptwatch.
- [Search Engine Land — Semrush is bringing AI visibility under the Spotlight, Semrush, 4 septembre 2026](https://searchengineland.com/semrush-is-bringing-ai-visibility-under-the-spotlight-487137) — annonce Spotlight London 13 octobre 2026, chiffre 15,2 % de catégories avec leader clair sur 1 094 catégories.
- [Search Engine Roundtable — Google Ads Testing Serving Restrictive Match Types In AI Mode, Anthony Higman + Ginny Marvin, 4 septembre 2026](https://www.seroundtable.com/google-ads-serving-restrictive-match-types-ai-mode-42024.html) — signal éligibilité exact/phrase match dans AI Mode, expérimentation Google Ads limitée.

---

*Édition produite par SyntheticBrain, agent auto-améliorant. Rien n'a été envoyé. Voir la mémoire dans `agent-synthetic/` pour la boucle d'apprentissage.*
