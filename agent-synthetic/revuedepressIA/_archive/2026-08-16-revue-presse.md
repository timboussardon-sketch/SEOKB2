---
title: "Algorithme — édition du 16 août 2026"
date: 2026-08-16
edition: 2026-08-16-revue-presse
piliers: [GEO, Business SEO]
info_du_jour_pilier: GEO
type: revue-presse
status: draft
---

# Algorithme — édition du 16 août 2026

## Résumé

- Étude Scrunch sur panel opt-in février-juin 2026 : 1,1 % seulement des visites vers éditeurs de presse dans la semaine qui suit une conversation IA sont attribuées directement à un lien cliqué depuis un assistant, mais la probabilité de visiter un éditeur augmente de 20,5 points de pourcentage la semaine qui suit une conversation IA orientée news par rapport à une conversation IA non-news.
- Concentration mesurée sur les majors : 82 % des noms d'éditeurs cités spontanément par les assistants IA sont des majors, qui reçoivent 97 % des visites de suivi vers des éditeurs nommés ; les éditeurs de taille moyenne reçoivent un uplift de 8,6 points contre 22,9 points pour les majors.
- Sondage Duane Forrester 163 répondants publié le 13 août : la donnée GEO est jugée précieuse (4,20/5 sur cinq types de données) mais l'investissement dans les plateformes qui la vendent est jugé moyen (3,19/5) ; 57 % des retours ouverts mentionnent défiance méthodologique ou absence de connexion à la valeur business, 7 % seulement citent le prix.
- Google publie le playbook « Creator Marketing: Build Edition » (juin 2026) qui met en avant une étude Supergoop (+93 % recherches Glowscreen, +55 % Supergoop) sans publier fenêtre d'attribution, période de référence, ni contrôle isolant l'effet créateur ; l'article de Greg Jarboe (SEJ, 14 août) documente le manque méthodologique.

## Info du jour — GEO : une étude Scrunch mesure 1,1 % de visites éditeurs directement attribuées à un lien IA, et 20,5 points de visites en plus la semaine après une conversation IA orientée news

Michael Iannelli, principal data scientist chez Scrunch, a publié le 13 août 2026 une étude titrée « Surviving the clickpocalypse: What millions of search events say about AI eating the news » ([billet primaire sur scrunch.com](https://scrunch.com/blog/surviving-the-clickpocalypse-ai-eating-the-news/)). Danny Goodwin, éditeur SEO chez Search Engine Land, en a fait une reprise le même jour ([SEL 484851](https://searchengineland.com/news-publisher-visits-from-ai-study-484851)), relayée par [Optimixed](https://www.optimixed.com/only-1-1-of-news-publisher-visits-come-directly-from-ai-study/) sans indépendance éditoriale marquée.

Méthodologie déclarée : panel opt-in, respectueux de la vie privée, qui suit les mêmes individus à travers leurs conversations IA, leurs recherches Google et leurs visites d'éditeurs, sur la fenêtre février-juin 2026. La mesure porte sur des visites de pages, pas sur des abonnements, du revenu ou du temps passé. La taille exacte du panel n'est pas publiée, l'étude cite « des millions de recherches, conversations IA et visites d'éditeurs ». Deux définitions structurent la mesure : une « visite post-chat » est une visite d'éditeur dans les sept jours qui suivent une conversation IA ; une « visite attribuée IA » est une visite dont la source cliquée juste avant est une plateforme IA identifiée.

Les chiffres extraits du billet primaire :

- 1,1 % des visites éditeurs post-conversation IA portent une attribution directe à un lien IA cliqué. Le reste se répartit : environ 75 % de navigation directe, environ 9 % de recherche traditionnelle, le solde d'autres référents.
- Sur les recherches Google d'actualité comportant un AI Overview, la probabilité de clic est d'environ 20 %, contre environ 30 % sans AI Overview. Sur une même requête donnée, l'écart se réduit à environ 2 points de pourcentage, ce qui indique que la sélection des requêtes qui déclenchent un AI Overview pèse dans l'écart agrégé.
- La probabilité de visiter un éditeur dans la semaine qui suit une conversation IA orientée news est supérieure de 20,5 points de pourcentage à celle qui suit une conversation IA non-news. Le uplift n'est pas également distribué : 22,9 points sur les majors, 8,6 points sur les éditeurs de taille moyenne.
- 82 % des noms d'éditeurs volontairement cités par les assistants IA sont des majors, 17 % sont de taille moyenne, moins de 1 % sont de niche. Sur les visites de suivi vers des éditeurs nommés, les majors captent 97 %.

La lecture de l'étude par son auteur : « AI takes clicks in one place and returns visits in another. » Selon Iannelli, l'IA ne détruit pas la totalité du trafic éditeur, elle le redistribue et crée des parcours multi-étapes invisibles aux outils d'attribution par référent classique. Le billet ne montre pas que l'IA crée de la demande nouvelle. Il montre que les conversations IA orientées news coïncident souvent avec la poursuite de la lecture d'actualité, avec une concentration lourde sur les majors.

L'étude s'inscrit dans le pilier GEO (Generative Engine Optimization). Elle ajoute une dimension à la fiche [[concepts/metriques-visibilite-geo]] : au-delà des métriques `Imp_wc` et `Imp_pos` définies dans [[sources/2026-04-13-geo-aggarwal-2024]] qui portent sur la proportion et la position de la citation dans la réponse générative, il faut mesurer la conversion citation-vers-visite, qui n'est pas linéaire dans le référent HTTP. Elle valide aussi côté data la [[concepts/tabou-visibilite]] dans un sens contre-intuitif : la « visibilité » dans une réponse IA ne se traduit pas par un clic direct mesurable au sens classique du référent, mais peut se traduire par une visite ultérieure dont l'attribution est perdue par les outils d'analytics standard.

Trois lectures opérationnelles pour un consultant SEO ou GEO en mandat éditeur :

1. Ne pas piloter la performance IA d'un éditeur uniquement sur la colonne « AI referral » d'un outil d'analytics. À la fenêtre semaine, un panel opt-in mesure 20,5 points d'uplift sur des visites que le référent HTTP ne rattrape pas. Il faut ajouter au tableau de bord une mesure de session non attribuée dans les sept jours suivant l'exposition à une réponse IA, en s'appuyant sur les données propriétaires de l'éditeur (login, cookies premières parties, comportement direct) plutôt que sur le référent seul.
2. La concentration 82 %/97 % sur les majors est un fait de marché à intégrer dans une revue stratégique éditeur. Un éditeur de taille moyenne obtient un uplift de 8,6 points contre 22,9 points pour un major. Cet écart de facteur 2,7 s'ajoute aux écarts déjà documentés côté citation. Pour un éditeur non-major, la boucle « je publie plus » ne compense pas mécaniquement l'écart. Il faut piloter une différenciation de niche ou une politique d'exclusivité ou de partenariat direct avec un ou plusieurs opérateurs IA.
3. La formule « AI takes clicks in one place and returns visits in another » est utile pour cadrer une conversation client, mais reste conditionnelle à la fenêtre sept jours du panel et à un contexte news. Il n'y a pas de preuve que le même schéma tient dans un contexte SaaS, marchand ou service local. Ne pas généraliser sans reproduction indépendante sur d'autres verticales.

Trois caveats explicites :

- Taille du panel non publiée. L'étude parle de « millions » d'événements, pas de « n » de panélistes. Une reproduction indépendante sur un panel de taille comparable et publiée serait utile.
- Scrunch est un vendeur d'outils GEO. Le billet primaire est produit par un fournisseur de la catégorie qu'il mesure. La reprise SEL par Danny Goodwin est un contrôle éditorial secondaire, pas une reproduction indépendante.
- La fenêtre février-juin 2026 est antérieure à plusieurs évolutions produit (Google AI Mode déploiement mondial, montée des AI Overviews, Cloudflare policy 15 septembre 2026 en cours de préparation). Une reproduction sur juillet-décembre 2026 aura des chiffres différents.

Trois prédictions vérifiables à surveiller :

- P-2026-08-16-1 : un second panel opt-in indépendant de Scrunch publie une mesure de l'uplift de visites post-conversation IA sur un éditeur non-major et rapporte un uplift compris entre 5 et 15 points de pourcentage sur les majors du même vertical. Échéance 31 mars 2027. Confidence 0.45.
- P-2026-08-16-2 : un outil d'analytics grand public (Google Analytics 4, Adobe Analytics, Matomo) publie une documentation officielle d'un mode d'attribution « fenêtre post-IA sept jours » sur les visites directes. Échéance 30 juin 2027. Confidence 0.25.
- P-2026-08-16-3 : Scrunch publie une reproduction sur juillet-décembre 2026 dans laquelle la part de visites attribuées directement à un lien IA dépasse 3 %. Échéance 31 décembre 2026. Confidence 0.35.

## Brève 1 — GEO/Business SEO : sondage Duane Forrester 163 répondants sur la valeur perçue des outils GEO, 4,20/5 pour la donnée, 3,19/5 pour l'outil, 57 % citent la défiance méthodologique ou l'attribution business

Duane Forrester, fondateur et CEO d'UnboundAnswers.com et ancien Senior Program Manager Bing, a publié le 13 août 2026 sur Search Engine Journal ([SEJ 585161](https://www.searchenginejournal.com/the-geo-trust-gap-seos-want-the-data-but-not-the-platforms-selling-it/)) l'analyse d'un sondage auto-sélectionné auprès de 163 répondants SEO. Marge d'erreur d'environ 7 points, précisée par l'auteur.

Chiffres extraits du sondage :

- Valeur perçue des données GEO en soi : 4,20/5 en moyenne sur cinq types de données mesurés.
- Valeur perçue de l'investissement dans les plateformes qui vendent ces données : 3,19/5 en moyenne. Parmi les abonnés actuels à un outil, 44 % seulement jugent l'investissement rentable.
- 123 répondants sur 163 (75 %) ont laissé un commentaire libre. Répartition thématique : 24 % défiance sur la méthodologie et le manque de transparence, 20 % manque de connexion entre données GEO et valeur business, 15 % non-déterminisme et personnalisation des réponses IA rendant la mesure instable, 11 % « synthetic prompts » vs demande réelle des utilisateurs, 9 % manque d'actionnabilité, 7 % prix.
- Systèmes que les répondants disent tracker : Google AI Overviews et AI Mode 95 %, ChatGPT 94 %, Gemini 75 %, Claude 64 %, Perplexity 34 %, Copilot 25 %.

Deux verbatim extraits du corps de l'article : « You choose the prompts, which means you decide in advance what you should be visible for, then measure yourself against your own list. » Et : « These tools... you can't reverse-engineer what's working when the answer changes every time. »

Forrester ne nomme aucun outil GEO dans son article. Il ne propose pas de solution prescriptive et note que les répondants n'ont pas proposé d'alternative au-delà de demander de la transparence méthodologique, ce que les fournisseurs ne peuvent commercialement pas offrir. L'article s'inscrit dans une série documentée par Forrester lui-même sur SEJ (Answer Engine Fingerprint le 16 juillet, ChatGPT « not provided » le 23 juillet, The web is eating itself le 9 juillet).

Deux limites explicites :

- Sondage auto-sélectionné auprès de la base LinkedIn de Forrester. Population biaisée vers les SEO qui suivent Forrester et vers ceux qui ont un avis fort sur les outils GEO. Ce n'est pas un échantillon représentatif de la profession SEO.
- 163 répondants est un effectif modeste. La marge d'erreur de 7 points suffit à faire varier plusieurs pourcentages thématiques dans une fourchette large. Les 15 % « non-déterminisme » peuvent être aussi bien 8 % que 22 %.

Le fait relie [[concepts/arbitrage-plateforme-publication]] : la surface de mesure d'un outil GEO est une plateforme, distincte de la SERP classique, avec ses propres règles opaques. La défiance mesurée est un signal de marché pour les consultants qui vendent un audit GEO à un client : la donnée est demandée, l'outil qui la vend l'est moins. Le fait relie aussi [[concepts/data-proprietaire]] : l'attribut « transparence méthodologique » est structurellement absent d'un outil de mesure IA qui exécute des « synthetic prompts » sur un système non-déterministe, ce qui laisse la place à une mesure de la performance IA à partir des données propriétaires du site plutôt que d'un panel synthétique loué.

Prédiction : P-2026-08-16-4 : un second sondage indépendant de Forrester auprès d'au moins 300 répondants SEO nord-américains reproduit un écart d'au moins 0,7 point entre valeur perçue des données GEO et valeur perçue de l'investissement outil. Échéance 30 juin 2027. Confidence 0.55.

## Brève 2 — Business SEO : le playbook « Creator Marketing: Build Edition » de Google publie une étude Supergoop +93 %/+55 % sur recherche branded sans fenêtre d'attribution ni contrôle

Greg Jarboe, VIP Contributor SEJ et co-fondateur de SEO-PR, a publié le 14 août 2026 sur Search Engine Journal ([SEJ 584876](https://www.searchenginejournal.com/youtube-measures-creator-video-on-branded-search-lift-but-the-attribution-gap-still-exists/)) une analyse du playbook Google « Creator Marketing: Build Edition » ([PDF officiel Google Services](https://services.google.com/fh/files/misc/youtube_creator_marketing_playbook_build_edition_june2026.pdf), juin 2026).

Chiffres publiés par Google dans le playbook et extraits par Jarboe :

- +93 % de recherches pour le produit-héros « Glowscreen » attribuées à une campagne creator Supergoop.
- +55 % de recherches pour le nom de marque « Supergoop » sur la même campagne.

Jarboe identifie trois éléments méthodologiques manquants dans la publication de Google :

- Aucune fenêtre d'attribution spécifiée pour la mesure des recherches branded.
- Aucune période de référence (baseline) disclosée.
- Aucun contrôle explicite isolant l'effet de la campagne creator des autres campagnes média payantes ou des effets saisonniers concurrents pendant la même fenêtre.

Verbatim de l'auteur : « A 93% increase is meaningless without knowing what it's a percentage of, over what window, against what control. »

Jarboe note que ce manque méthodologique n'est pas isolé à ce case study : plusieurs case studies publiés par Google reprennent le même format (chiffre agrégé sans dénominateur, sans fenêtre, sans contrôle). Le manque bloque la reproductibilité et l'usage opérationnel de la mesure par un annonceur qui voudrait éprouver la méthode Supergoop sur son propre catalogue.

Trois lectures opérationnelles pour un consultant SEO en accompagnement d'un annonceur qui reçoit une pitch creator marketing :

1. Demander au vendeur la fenêtre d'attribution, la baseline utilisée, et la méthode de contrôle avant d'accepter un chiffre de lift branded. Sans ces trois éléments, le chiffre n'a pas de valeur opérationnelle. C'est la même exigence que pour un chiffre GEO.
2. Mesurer soi-même l'uplift branded via Google Search Console (impressions et clics par requête branded, fenêtre 28 jours ou 90 jours avant/après campagne). Ce mode de mesure est reproductible côté annonceur, indépendant du vendeur.
3. Le playbook Google est un document commercial. La lecture SEO doit dissocier ce qui est fait vérifiable (Google publie que Supergoop a fait +93 %/+55 %) de ce qui est claim méthodologique non-instrumenté. Aucune décision d'investissement média ne peut se prendre sur ce seul document.

Le fait relie [[concepts/tabou-visibilite]] dans son axe original : un chiffre d'uplift branded présenté sans dénominateur ni fenêtre est structurellement le type de chiffre « visibilité » qui casse la conversation avec un annonceur B2C exigeant. Il relie aussi [[concepts/arbitrage-plateforme-publication]] : la SERP branded reste la surface la plus accessible pour mesurer un effet creator, alors que YouTube ne publie pas la méthodologie qui permettrait de la contester.

Prédiction : P-2026-08-16-5 : Google publie une version du playbook qui documente la fenêtre d'attribution et la baseline utilisée sur au moins un case study. Échéance 31 mars 2027. Confidence 0.25.

## Sources nouvelles ce run

- [scrunch.com](https://scrunch.com/blog/surviving-the-clickpocalypse-ai-eating-the-news/) — vendeur d'outils GEO qui publie une étude interne à partir d'un panel opt-in. Trust initial 0.65, statut explore. Une étude primaire secteur news, méthodologie partiellement publiée. Candidate au passage exploit si Scrunch publie une seconde étude sur un autre vertical avec méthodologie détaillée.
- [unboundanswers.com](https://www.searchenginejournal.com/the-geo-trust-gap-seos-want-the-data-but-not-the-platforms-selling-it/) — entité de Duane Forrester, auteur récurrent SEJ, déjà tracké dans le registre via sa signature SEJ. Le sondage 163 respondents est propre à UnboundAnswers, référencée dans l'article. Trust 0.65 pour la marque d'entité indépendamment de la présence SEJ.
- [services.google.com](https://services.google.com/fh/files/misc/youtube_creator_marketing_playbook_build_edition_june2026.pdf) — hébergement de documents commerciaux Google. Source primaire pour les chiffres du playbook, trust 0.85 sur les chiffres publiés, trust variable sur la méthodologie qui n'est pas documentée.

## Ce que cette édition ajoute

- Un chiffre neuf sur la conversion citation-vers-visite dans un panel opt-in indépendant du référent HTTP : 1,1 % de référence directe, 20,5 points d'uplift à sept jours. À ma connaissance non couvert par les éditions précédentes, cross-source primaire Scrunch + secondaire SEL.
- Une mesure de la défiance mesurée envers les outils GEO côté acheteurs SEO : 3,19/5 pour l'investissement, 57 % de retours défiants sur méthodologie ou attribution business, 7 % seulement citent le prix. Signal de marché nouveau pour un consultant qui vend un audit GEO.
- Un cas documenté du manque méthodologique dans un playbook Google grand public (creator marketing), utile pour cadrer une conversation avec un annonceur B2C sur la valeur d'un chiffre de lift branded présenté sans dénominateur.

---

Draft SyntheticBrain. Rien n'a été envoyé.
