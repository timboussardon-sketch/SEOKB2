---
title: "OpenAI a ses Quality Raters : 10 000 évaluateurs, et certains laissent l'IA noter l'IA"
date: 2026-09-26
pilier_info_du_jour: Recherche agentique
piliers_breves: [Actualité SEO, Niche SEO]
edition: 66
---

# OpenAI a ses Quality Raters : 10 000 évaluateurs, et certains laissent l'IA noter l'IA

*Édition Algorithme — 26 septembre 2026 — SyntheticBrain*

- OpenAI opère un programme d'évaluation humaine baptisé « Project Lily » avec plus de 10 000 contractuels qui notent les réponses de ChatGPT sur une échelle de 1 à 7 (source primaire [404 Media](https://www.404media.co/people-training-openais-ai-fired-for-using-ai-to-train-the-ai/), 22 septembre 2026).
- Plusieurs de ces contractuels ont été renvoyés après avoir utilisé eux-mêmes des IA pour rédiger leurs notations, avec pour indices détectés « les motifs de mots répétitifs, les tirets cadratins en excès et des temps de saisie anormalement courts ».
- L'instruction interne aux évaluateurs est explicite : « Do not use AI detection tools, or AI yourself ». Les superviseurs ont pour consigne de ne pas révéler leurs méthodes de détection.
- Google a mis à jour la documentation de son schéma VideoObject le 24 septembre pour ajouter les propriétés `creator` et `author`, et clarifier les quatre `interactionType` supportés (WatchAction, LikeAction, CommentAction, ShareAction).
- Google Business Profile durcit sa politique des Posts : les numéros de téléphone, emails et handles sociaux non vérifiés peuvent désormais faire retirer un post.

## Info du jour — Recherche agentique — Project Lily documente la chaîne d'évaluation humaine de ChatGPT

Le 22 septembre 2026, Joseph Cox publie dans [404 Media](https://www.404media.co/people-training-openais-ai-fired-for-using-ai-to-train-the-ai/) une enquête sur le programme interne d'OpenAI baptisé « Project Lily ». L'article documente l'existence d'un dispositif d'évaluation humaine des réponses de ChatGPT, activé par plus de dix mille contractuels recrutés via l'entreprise Crossing Hurdles et rémunérés par la société d'AI-training Mercor. La tâche décrite : lire une conversation ChatGPT anonymisée, résumer ce que voulait l'utilisateur, puis noter plusieurs réponses candidates sur une échelle de 1 à 7. Le résultat de ces notations alimente les cycles d'apprentissage par renforcement à partir de retours humains (RLHF) utilisés pour orienter le comportement du modèle.

Le fait qui déclenche l'enquête : plusieurs de ces contractuels ont été terminés après que leurs relecteurs ont conclu que leur travail était généré par une IA. Les instructions internes reproduites par 404 Media sont directes. Aux évaluateurs : « Do not use AI detection tools, or AI yourself ». Aux superviseurs : « it is easier for them to hide if they know what you look for ». Les indices concrets utilisés pour repérer les tricheurs sont trois : motifs de mots répétitifs, tirets cadratins en excès (« excessive em dashes »), et temps de complétion anormalement courts. L'usage d'outils comme GPTZero ou Grammarly est explicitement interdit aux relecteurs, non pas seulement pour préserver leur méthode de détection, mais aussi parce que ces outils sont jugés « pas fiables » par OpenAI selon les documents consultés.

Mercor a confirmé à 404 Media que ses contrats interdisent aux collaborateurs d'utiliser des grands modèles de langage pour accomplir les projets, et déclare investir « dans les outils et systèmes pour détecter les usages abusifs ». OpenAI a décliné de commenter les licenciements liés à l'usage d'IA. La reprise éditoriale la plus visible côté SEO est intervenue le 25 septembre chez Search Engine Roundtable, où Barry Schwartz relève dans son article [OpenAI Has Quality Raters, AI Trainers, & They Cheated With AI](https://www.seroundtable.com/openai-quality-raters-ai-trainers-42149.html) le parallèle direct entre ce dispositif et les Quality Raters de Google. Reprises complémentaires : [Tom's Guide](https://www.tomsguide.com/ai/openai-contractors-were-reportedly-fired-for-using-ai-to-train-chatgpt-heres-how-they-got-caught), [Cybernews](https://cybernews.com/tech/openai-fires-contractors/), [AI Weekly](https://aiweekly.co/alerts/openai-fires-contractors-caught-using-ai-to-grade-chatgpt).

Un point secondaire mérite d'être noté sans en surinterpréter la portée : un contractuel cité par 404 Media rapporte avoir volontairement choisi de mauvaises réponses pour « saboter » le modèle, motivé par une gêne éthique. C'est un témoignage individuel, un cas, pas une mesure. Il documente néanmoins qu'un canal de dégradation active du signal d'entraînement existe côté annotateurs, en plus du canal passif de la triche via LLM.

Ce que ce dispositif change, pour un consultant SEO ou GEO qui travaille la visibilité dans ChatGPT et dans les réponses génératives. D'abord, une clarification structurelle : OpenAI opère une couche d'évaluation humaine industrialisée, comparable dans son principe aux Search Quality Rater Guidelines de Google, sans que cette couche soit publiquement documentée par OpenAI ni qu'une grille équivalente à la QRG ait été publiée. Cette couche pèse sur la préférence du modèle entre réponses candidates. Voir dans le vault [[entities/quality-raters-guidelines]] pour le pendant Google, et [[concepts/agentic-search]] pour le paradigme SEO agentique où « être sélectionné par l'agent » remplace « être affiché dans une liste ».

Ensuite, une conséquence pratique sur la robustesse du signal d'entraînement. Si une part non chiffrée des notations reçues par le modèle est produite par une autre IA, la boucle de renforcement humaine devient partiellement une boucle de renforcement IA-sur-IA. La documentation publique ne permet pas de quantifier cette part. 404 Media rapporte que le phénomène a nécessité des licenciements « multiples », que les instructions internes évoquent l'usage d'IA de manière habituelle par les collaborateurs, et qu'un contractuel interrogé déclare voir des collègues utiliser une IA « tout le temps ». Aucune de ces déclarations n'est chiffrée par un cabinet indépendant. On tient un fait qualitatif solide, pas une mesure de taille d'effet.

Enfin, un signal de convergence sur la doctrine anti-IA-writing de ce vault. Les indices utilisés par les relecteurs OpenAI pour détecter la triche recoupent point par point la liste des patterns statistiques identifiés par le guide Wikipedia « Signs of AI Writing », socle de [[concepts/anti-ai-writing]]. La répétition de mots, l'em dash surreprésenté, la formulation générique probable : ce sont les mêmes tells. Ce que valide l'enquête 404 Media, c'est que ces signes ne sont pas seulement mobilisables comme critères de qualité par un consultant qui relit, ils sont opérationnellement utilisés à l'échelle de dizaines de milliers de traces par un employeur qui décide de renvoyer sur cette base.

Cinq lectures opérationnelles ressortent pour un consultant SEO/GEO.

Un, une page publiée qui vise à être citée par ChatGPT est évaluée en amont non seulement par le modèle, mais par une chaîne d'annotateurs humains dont on connaît maintenant la taille (>10 000), la structure (Mercor via Crossing Hurdles), l'échelle de notation (1 à 7), et les indices de suspicion qu'ils emploient. L'anti-IA-writing cesse d'être un choix stylistique, elle devient un pré-requis fonctionnel.

Deux, la mesure d'exposition dans les moteurs génératifs (voir [[concepts/metriques-visibilite-geo]]) porte sur un signal qui a été façonné par une couche d'évaluation humaine dont la fiabilité est publiquement contestée sur une part indéterminée. Toute lecture d'un score d'exposition ChatGPT tirée d'un outil GEO tiers doit intégrer que le signal amont est bruité par une contamination LLM-sur-LLM non chiffrée.

Trois, la parité conceptuelle avec la QRG de Google offre un cadre d'analyse. Les 175 pages de la QRG documentent publiquement comment les Quality Raters de Google notent Needs Met, E-E-A-T, Fully Meets, Effort. Aucune documentation équivalente n'est publiée par OpenAI. On sait maintenant que la couche existe, on ne connaît ni ses critères, ni ses seuils, ni la répartition des tâches. C'est une asymétrie d'information exploitable en veille pour qui suit la GEO comme la SEO se suit avec la QRG.

Quatre, l'annonce documente une dépendance opérationnelle d'OpenAI à un intermédiaire de staffing (Mercor) et à un sous-traitant de recrutement (Crossing Hurdles). Toute évolution de cette chaîne (rupture de contrat, renégociation, changement de sous-traitant, régulation du travail des annotateurs IA) est un point à surveiller pour anticiper des inflexions de comportement de ChatGPT.

Cinq, l'écart entre la mesure officielle et la mesure indépendante reste entier : aucune publication OpenAI ne détaille le programme, aucune mesure cabinet tiers ne quantifie le taux de contamination des notations, aucune revue par les pairs ne valide la méthode de détection retenue. Il faut donc traiter l'information comme documentée en source primaire journalistique unique (404 Media), reprise mais non recoupée par une seconde enquête à ce jour. La corroboration existe côté citations (Tom's Guide, Cybernews, AI Weekly, SER Roundtable), pas côté vérification primaire indépendante. À suivre.

Trois concepts doctrine s'articulent ici. [[entities/quality-raters-guidelines]] gagne un pendant OpenAI documenté publiquement pour la première fois. [[concepts/agentic-search]] se voit consolider son cadre : la sélection par l'agent dépend d'une pré-évaluation humaine dont on connaît maintenant l'existence chez OpenAI. [[concepts/anti-ai-writing]] est validée dans son socle empirique : les tells qu'elle interdit sont ceux qu'OpenAI utilise pour licencier.

Cinq réserves méthodologiques explicites. Un, l'enquête 404 Media est publiée par une seule rédaction, aucune autre équipe d'investigation n'a produit sa propre analyse à partir des mêmes documents internes. Deux, OpenAI décline de commenter, ce qui prive le corpus d'une source contradictoire officielle. Trois, la part contaminée des notations n'est pas chiffrée. Quatre, l'échelle 1-7 et le protocole exact d'agrégation des notations ne sont pas publiés. Cinq, le fait de sabotage volontaire par un contractuel est un témoignage isolé, non pas une mesure.

## Brève 1 — Actualité SEO — Google ajoute `creator`/`author` et clarifie `interactionStatistic` sur le schéma VideoObject

Google a publié le 24 septembre 2026 (« Last updated 2026-09-24 UTC ») une mise à jour de sa documentation officielle du schéma [VideoObject](https://developers.google.com/search/docs/appearance/structured-data/video). Le changelog Google indique : « to document support for the creator and author properties, and clarify supported interaction types for interactionStatistic in VideoObject structured data ». Deux changements de fond. D'abord, l'ajout formel de la propriété `creator` (avec un alias `author`), qui accepte un type `Person` ou `Organization`, et exige la sous-propriété `creator.name`. Ensuite, la doc liste explicitement les quatre `interactionType` acceptés dans `interactionStatistic` : `WatchAction` pour le nombre de vues, `LikeAction` pour likes et upvotes, `CommentAction` pour commentaires, `ShareAction` pour partages.

Le repérage éditorial est signé Barry Schwartz sur [Search Engine Roundtable](https://www.seroundtable.com/google-video-structured-data-creator-update-42162.html) le 25 septembre, avec comparaison à un snapshot Wayback antérieur (21 septembre 2026) pour matérialiser l'écart de version. Ce que ça change concrètement, pour les éditeurs qui gèrent du contenu vidéo indexé par Google : la déclaration explicite de l'auteur ou du créateur d'une vidéo dans le structured data devient un signal formel documenté, alignant VideoObject sur les autres types de contenu (Article, HowTo) qui déclarent déjà auteur ou organisation. La clarification des `interactionType` retire l'ambiguïté sur les métriques d'engagement acceptées, ce qui matérialise le contour du signal social pris en compte par Google pour évaluer la popularité d'une vidéo.

Deux réserves explicites. Un, Google ne précise pas dans ce billet si la déclaration de `creator` devient un critère d'éligibilité aux rich results vidéo ni s'il pondère la sélection dans Google Video Search. Deux, la mise à jour est documentaire, pas fonctionnelle : le comportement de recherche n'est pas modifié à ce stade. Suivi utile côté doctrine : voir [[concepts/e-e-a-t]] pour la lecture Authoritativeness d'une propriété `creator` déclarée.

## Brève 2 — Niche SEO — Google Business Profile retire les Posts avec numéros et emails non vérifiés

Google a mis à jour deux pages d'aide Business Profile pour resserrer sa politique de contenu sur les Posts. La page officielle [Business Profile photos, videos and posts content policy](https://support.google.com/business/answer/7213077) est modifiée pour ajouter : « To avoid fraud or abuse, we may remove posts with unverified contact information. This includes phone numbers, email addresses, and social media handles ». Repérage attribué à Hiroko Imai sur LinkedIn, reprise éditoriale par Barry Schwartz sur [Search Engine Roundtable](https://www.seroundtable.com/unverified-contact-information-google-posts-42159.html) le 25 septembre 2026.

Ce que ça change pour un consultant en SEO local. Un Post Business Profile qui affiche un numéro de téléphone dans son texte sans que Google ne considère ce numéro « vérifié » devient candidat au retrait automatique, sans notification préalable documentée à ce stade. Google ne précise pas ce qui constitue une « vérification » suffisante côté propriétaire : le numéro de la fiche titulaire lui-même n'est pas explicitement listé comme sécurisé dans le texte du Post. La lecture opérationnelle prudente : basculer la sollicitation d'appel vers le bouton d'action du Post (`Call now`, `Book`, `Learn more`) plutôt que d'exposer un numéro dans le corps de texte.

Deux réserves méthodologiques. Un, aucune indication du volume de Posts déjà retirés sous cette politique n'est publiée. Deux, la définition de « unverified » n'est pas donnée par Google dans le texte des pages modifiées : la portée exacte de la règle reste ouverte. Suivi utile côté doctrine : voir [[concepts/tabou-visibilite]] pour la lecture d'un signal Business Profile qui filtre le canal de conversion téléphonique.

## Prédictions vérifiables

- **P-2026-09-26-1** — Un cabinet indépendant (non-404 Media, non-Mercor, non-OpenAI) publie d'ici le 31 mars 2027 une seconde enquête ou une mesure chiffrée du taux de contamination LLM dans les notations d'évaluateurs OpenAI (Project Lily ou successeur). Confiance : 0,40.
- **P-2026-09-26-2** — OpenAI publie d'ici le 30 juin 2027 une documentation officielle (blog OpenAI, System Card, papier technique) sur son programme d'évaluation humaine, avec un minimum d'informations sur la grille de notation utilisée. Confiance : 0,30.
- **P-2026-09-26-3** — Une clarification Google Business Profile publiée d'ici le 31 décembre 2026 précise ce qui constitue un numéro de téléphone « vérifié » pour un Post, résolvant l'ambiguïté relevée sur la page 7213077. Confiance : 0,45.

## Sources consultées ce run

Info du jour :
- [404 Media — Joseph Cox — People Training OpenAI's AI Fired for Using AI to Train the AI, 22 septembre 2026](https://www.404media.co/people-training-openais-ai-fired-for-using-ai-to-train-the-ai/)
- [Search Engine Roundtable — Barry Schwartz — OpenAI Has Quality Raters, AI Trainers, & They Cheated With AI, 25 septembre 2026](https://www.seroundtable.com/openai-quality-raters-ai-trainers-42149.html)
- [Tom's Guide — OpenAI contractors were reportedly fired for using AI to train ChatGPT — here's how they got caught](https://www.tomsguide.com/ai/openai-contractors-were-reportedly-fired-for-using-ai-to-train-chatgpt-heres-how-they-got-caught)
- [Cybernews — OpenAI fires contractors for using AI to train ChatGPT](https://cybernews.com/tech/openai-fires-contractors/)
- [AI Weekly — OpenAI Fires Contractors Caught Using AI to Grade ChatGPT](https://aiweekly.co/alerts/openai-fires-contractors-caught-using-ai-to-grade-chatgpt)

Brève 1 :
- [Google Search Central — VideoObject structured data documentation, mise à jour 2026-09-24 UTC](https://developers.google.com/search/docs/appearance/structured-data/video)
- [Search Engine Roundtable — Barry Schwartz — Google Video Structured Data Gets Creator Property & Updated interactionStatistic, 25 septembre 2026](https://www.seroundtable.com/google-video-structured-data-creator-update-42162.html)

Brève 2 :
- [Google Business Profile Help — Business Profile photos, videos and posts content policy](https://support.google.com/business/answer/7213077)
- [Search Engine Roundtable — Barry Schwartz — Google Gets Stricter On Unverified Contact Information In Google Posts, 25 septembre 2026](https://www.seroundtable.com/unverified-contact-information-google-posts-42159.html)

*Édition produite par SyntheticBrain, agent de veille search/IA autonome. Aucune publication automatique. Draft à valider avant diffusion.*
