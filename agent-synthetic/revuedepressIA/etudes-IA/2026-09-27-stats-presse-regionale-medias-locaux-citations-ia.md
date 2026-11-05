---
type: query
skill: seo-page-statistiques
title: "Presse régionale et moteurs IA : 0,18 % des citations presse vont aux médias locaux (2025-2026)"
aliases: [stats-presse-regionale-citations-ia, presse-locale-ia-2026]
tags: [seo, ia, geo, citations-ia, presse, médias-locaux, presse-régionale, concentration, france]
created: 2026-09-27
updated: 2026-09-27
sources: 9
confidence: high
status: draft
---

# Presse régionale et moteurs IA : 0,18 % des citations presse vont aux médias locaux (2025-2026)

Les moteurs IA citent les médias locaux dans 0,18 % des cas au sein des citations presse. C'est la mesure la plus précise disponible sur l'effacement des titres régionaux dans les réponses génératives, tirée de l'analyse de 4 millions de citations (BuzzStream, janvier 2026). Dans le même corpus, Forbes capte 33 % de l'ensemble des citations presse à lui seul. Les dix premiers éditeurs mondiaux en concentrent 84 %.

Ce n'est pas une question de qualité éditoriale. C'est une question de structure.

---

## Les chiffres clés (vérifiés à la source)

| Indicateur | Valeur | Source |
|---|---|---|
| Part des médias locaux dans les citations presse | **0,18 %** | BuzzStream, 4M citations, janv. 2026 |
| Part des contenus syndiqués dans les citations presse | **6,2 %** | BuzzStream, 4M citations, janv. 2026 |
| Top 5 éditeurs mondiaux : part des citations presse | **66 %** | Goodie, 31M citations, oct. 2025-juil. 2026 |
| Top 10 éditeurs mondiaux : part des citations presse | **84 %** | Goodie, 31M citations, oct. 2025-juil. 2026 |
| Forbes seul : part des citations presse | **33 %** | Goodie, 31M citations, oct. 2025-juil. 2026 |
| Part de la presse dans toutes les citations IA | **1,3 à 1,9 %** | Goodie, 31M citations, 11 surfaces |
| Coefficient de Gini des citations presse (OpenAI) | **0,83** | arXiv 2507.05301, 366 087 citations |
| Sources d'information uniques citées par Perplexity | **1 430** | arXiv 2507.05301, 24 069 conversations |
| Sources d'information uniques citées par OpenAI | **707** | arXiv 2507.05301, 24 069 conversations |
| Presses françaises bloquant au moins un robot IA | **22,6 %** | lvlup.fr, 1 132 sites de presse, nov. 2025 |
| Entreprises visibles dans l'IA locale (ChatGPT) | **1,2 %** | SOCi, 350 000 établissements, août 2026 |
| Établissements visibles dans le local pack Google | **35,9 %** | SOCi, 350 000 établissements, août 2026 |

---

## La concentration : un Gini de 0,83 pour mesurer l'inégalité

L'arXiv 2507.05301 (Kai-Cheng Yang, 2025) est la première étude à appliquer un coefficient de Gini à la distribution des citations presse dans les moteurs IA. Un Gini de 0 signifierait une distribution parfaitement égale entre tous les domaines. Un Gini de 1 signifie qu'un seul domaine capte tout. OpenAI affiche 0,83.

L'étude a analysé 366 087 citations issues de 24 069 conversations, sur 12 modèles appartenant à trois fournisseurs (OpenAI, Perplexity, Google). Résultat : 9 % de l'ensemble des citations pointent vers des sources d'information, réparties sur 1 795 domaines distincts. Mais dans ces 9 %, les 20 premières sources captent 67,3 % des citations OpenAI, 31,9 % des citations Google et 28,5 % des citations Perplexity.

Perplexity se révèle le moteur le plus ouvert : 1 430 sources uniques citées, contre 881 pour Google et 707 pour OpenAI. Ce chiffre change en fonction de la façon dont on mesure la diversité, mais il confirme que les modèles d'un même fournisseur tendent à citer les mêmes sources (similarité cosinus intra-famille : 0,82 à 0,99 ; inter-famille : 0,11 à 0,58).

---

## Le paradoxe de la dépêche régionale (transformation originale)

Le chiffre BuzzStream mérite une lecture précise. L'étude distingue trois catégories dans les citations presse : les contenus éditoriaux originaux (81 % des citations presse), les contenus syndiqués (6,2 %) et les médias locaux (0,18 %). Ces catégories ne sont pas exclusives : un article d'un quotidien régional repris sur un fil AFP devient du contenu syndiqué au moment où l'IA le récupère depuis un agrégateur national.

Ce mécanisme produit une distorsion systématique. Quand un fait local est repris par une dépêche AFP, retransmise sur Le Monde, L'Obs ou BFMTV, les moteurs IA citent la version nationale, pas l'original régional. La presse régionale absorbe le coût de collecte de l'information de terrain ; les éditeurs nationaux captent la citation. Ce transfert de valeur n'est pas intentionnel de la part des moteurs IA. Il est structurel : le modèle a appris sur des sources surcitées, et la syndication amplifie ce biais au moment du retrieval.

Les 6,2 % de contenus syndiqués constituent donc en partie des informations qui provenaient d'une rédaction locale avant leur reprise. La comparaison 6,2 % vs 0,18 % ne mesure pas deux types d'information différents. Elle mesure deux états du même fait selon l'endroit où les moteurs vont le chercher.

Cette distinction n'apparaît dans aucune des grandes études de citabilité IA publiées à ce jour. Les études Goodie, BuzzStream et arXiv 2507.05301 ne définissent pas explicitement ce qu'est un "média local" et ne tracent pas la chaîne de syndication.

---

## La presse régionale française face aux robots IA

L'étude lvlup.fr (novembre 2025) a analysé le fichier robots.txt de 1 132 sites de presse français reconnus par le ministère de la Culture. 22,6 % bloquent au moins un robot IA. CCBot est la cible la plus fréquente (20,6 % des sites), suivi de GPTBot (19,4 %) et de ChatGPT-User (16,4 %).

Parmi les dix premiers médias nationaux (SEOlivier, 2026), Ouest-France est le plus restrictif avec 14 bots sur 14 bloqués, devant BFMTV (même score). L'Équipe, France Info, Le Monde, Le Figaro, Le Parisien et Les Échos ont des postures intermédiaires (7 à 12 bots bloqués). CNews est le seul à n'avoir bloqué aucun robot.

La stratégie de blocage varie selon la taille. Les grands groupes régionaux (Groupe Télégramme, Groupe La Dépêche du Midi) avaient déjà introduit des protocoles de blocage en HTML, HTTP headers ou JSON dès septembre 2024 (mind Media). Les petits titres locaux, eux, bloquent moins. Soit par manque de ressources techniques pour mettre en place ces fichiers, soit parce qu'ils espèrent maintenir une exposition IA que les grands éditeurs ont décidé de refuser.

Ce clivage crée une asymétrie : les éditeurs régionaux avec un service technique compétent bloquent activement les robots (sans recevoir de compensation), tandis que les titres plus petits restent accessibles sans bénéficier d'une citabilité mesurable.

---

## L'IA dans les rédactions locales : une adoption plus forcée que choisie

L'étude de l'université du Maryland (arXiv:2510.18774, octobre 2025) a analysé 186 000 articles dans 1 500 journaux américains. Résultat : 9,1 % contiennent du contenu généré ou partiellement généré par une IA. La distribution est inversée par rapport à ce que les déclarations publiques laisseraient attendre : les petits journaux (moins de 100 000 exemplaires) affichent 9,3 % de contenu IA contre 1,7 % pour les grands titres.

Boone News Media atteint 20,9 %, Advance Publications 13,4 %. Ces groupes opèrent dans des marchés locaux avec peu de ressources rédactionnelles. L'IA n'est pas adoptée en premier par les ressources humaines abondantes, mais par les rédactions qui n'ont pas le choix.

Le contexte macrostructurel confirme cette contrainte. Le rapport State of Local News 2025 (Northwestern/Medill) recense 148 fermetures ou fusions de journaux locaux sur l'année, soit un rythme de deux par semaine. 212 comtés américains sont désormais sans aucun journal local. 50 millions d'Américains n'ont pas accès à une information locale fiable.

---

## Nos propres chiffres (données de première main)

Les données de citation IA de ce vault portent sur les requêtes de référencement (organikk.co), pas sur les requêtes d'actualité locale. La comparaison directe de la presse régionale française dans les moteurs IA n'a pas de mesure maison disponible à ce stade. Ce bloc est réservé honnêtement.

Une mesure directe exigerait de poser à ChatGPT, Perplexity, Google AI Mode et Claude 100 à 200 requêtes d'actualité locale (type "que s'est-il passé à Nantes cette semaine", "actualité politique à Toulouse", "faits divers Normandie") et de tracer les domaines cités. Ce protocole n'a pas été exécuté dans ce vault. Il constitue un test de terrain que cette étude propose d'inscrire dans les prochains travaux.

---

## Contre-analyse

La concentration des citations presse reflète en partie la concentration de la valeur informationnelle réelle. Forbes, Reuters ou le Financial Times couvrent des sujets transnationaux qui ont une pertinence pour des millions de requêtes. Un quotidien régional couvre un périmètre limité, ce qui réduit mécaniquement sa pertinence sur la majorité des requêtes posées aux moteurs IA.

La corrélation citation IA / présence web est documentée (Ahrefs, r = 0,664 pour les mentions web vs r = 0,218 pour les liens entrants, 75 000 marques). Les médias locaux ont une présence web faible comparée aux nationaux sur la majorité des sujets couverts par les IA. La sous-citation n'est pas uniquement un artefact algorithmique : elle reflète un déséquilibre existant dans l'espace numérique.

La presse locale française en particulier souffre d'un paradoxe de la paywallisation : les titres qui ont les ressources pour proposer du contenu de qualité (Ouest-France, Le Télégramme) bloquent aussi les robots IA le plus agressivement. Ils se protègent contre une extraction sans compensation, mais ce faisant ils réduisent encore leur citabilité.

La définition de "média local" varie selon les études. BuzzStream ne précise pas si elle inclut les sites d'information hyperlocale (city.news, quartier.com), les blogs de mairie, les radios locales. Le chiffre de 0,18 % pourrait couvrir des périmètres très différents selon l'opérationnalisation retenue.

---

## FAQ

**Pourquoi les IA ne citent-elles quasiment pas la presse locale ?**

Trois mécanismes distincts s'accumulent. Les modèles ont été entraînés sur un corpus où les grands éditeurs étaient déjà surcités (effet paramétrique). Le retrieval en temps réel favorise les domaines avec une forte autorité (mesurée par les liens entrants et le trafic). La syndication transfère la "propriété" éditoriale d'un fait local vers l'éditeur national qui le reprend.

**Les médias locaux peuvent-ils améliorer leur citabilité IA ?**

Oui, mais dans des conditions restrictives. Perplexity cite 1 430 sources uniques, contre 707 pour OpenAI. Un titre local peut apparaître dans Perplexity plus facilement qu'en OpenAI pur. Les données de terrain suggèrent que les requêtes à forte composante locale (type "mairie de X + décision + date") génèrent des citations vers les sources régionales, faute de concurrence nationale sur ces sujets précis. C'est la fenêtre réelle : les sujets strictement hyperlocaux sans reprise nationale.

**Les blocages robots.txt aggravent-ils la situation ?**

Pour les médias qui bloquent, les citations IA tombent à zéro sur ChatGPT, Claude et Gemini (démontrée pour le NYT dans l'étude Goodie). Grok, AI Overviews et DeepSeek ne respectent pas ces blocages dans une large mesure. Le blocage réduit donc la citabilité sur les moteurs qui respectent le protocole, sans protéger contre ceux qui ne le font pas.

**La situation est-elle différente en France ?**

Aucune étude n'a encore mesuré les citations IA de la presse française régionale spécifiquement. Le déploiement des AI Overviews en France date du 22 juillet 2026 (étude 2026-08-16 du vault). L'impact sur la presse locale française n'a pas encore fait l'objet d'une mesure J+30 ou J+90 publiée.

---

## [À SOURCER]

- **Chiffres spécifiques de l'étude Hipertext.net** (Sarrionandia et al., Basque Country) : le fetch retourne 403. La conclusion générale (biais national systématique sur les requêtes locales, 5 LLMs) est confirmée par d'autres sources mais les pourcentages précis restent non vérifiés.
- **Données françaises de citation presse régionale** : aucune étude primaire disponible (Peec AI, Goodie, arXiv 2507.05301) n'isole la presse régionale française des données EU ou mondiales.
- **Chaîne de syndication quantifiée** : le paradoxe de la dépêche régionale est documenté par les données BuzzStream (0,18 % vs 6,2 %) mais aucune étude ne trace explicitement le chemin source régionale → fil national → citation IA.
- **Pertes de trafic GSC des régionaux post-AIO France** (juillet 2026) : aucune donnée J+30 publiée.

---

## Sources

| Intitulé | Organisme | Date | URL | Consulté le |
|---|---|---|---|---|
| The Role of News Publications in AI Citations | BuzzStream / Pebblous | Janv. 2026 | https://www.buzzstream.com/blog/news-publications-ai-citations/ | 2026-09-27 |
| AI Citations & News Publishers: 2026 Study | Goodie | Oct. 2025-Juil. 2026 | https://higoodie.com/blog/publishers-and-ai-search-study/ | 2026-09-27 |
| News Source Citing Patterns in AI Search Systems (arXiv:2507.05301) | Kai-Cheng Yang et al. | Juil. 2025 | https://arxiv.org/html/2507.05301 | 2026-09-27 |
| Étude robots.txt presse française (1 132 sites) | lvlup.fr | Nov. 2025 | https://www.lvlup.fr/blog/etude-presse-francaise-ia-bloque-bot | 2026-09-27 |
| Blocage IA : Top 10 médias en France | SEOlivier | 2026 | https://seolivier.com/blocage-ia-medias-france/ | 2026-09-27 |
| 2026 Local Visibility Index | SOCi | Août 2026 | https://mshahid.com/blog/ai-local-visibility-report-2026 | 2026-09-27 |
| State of Local News 2025 | Medill / Northwestern | 2025 | https://localnewsinitiative.northwestern.edu/projects/state-of-local-news/2025/report/ | 2026-09-27 |
| AI Use in American Newspapers is Widespread, Uneven (arXiv:2510.18774) | U. of Maryland / Microsoft / Pangram | Oct. 2025 | https://arxiv.org/pdf/2510.18774 | 2026-09-27 |
| Generative artificial intelligence and local media (Hipertext.net) | Sarrionandia et al. | 2025 | https://raco.cat/index.php/Hipertext/article/view/9800252 | 2026-09-27 (source primaire 403) |
