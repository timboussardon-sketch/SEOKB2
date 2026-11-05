---
title: Algorithme — édition du 19 octobre 2026
date: 2026-10-19
pilier_info_du_jour: GEO / search IA
auteur: SyntheticBrain
voix: analyste search / IA, vouvoiement
---

# Mesurer les citations ChatGPT par l'API ou par Google rate une majorité des pages réellement citées

## Résumé

- Une préimpression arXiv postée le 11 octobre 2026 par cinq chercheurs de Singapour et Xi'an mesure l'écart entre les citations de ChatGPT Web, celles de l'OpenAI Responses API et les résultats Google : combinées, les deux sources externes ne recouvrent que 26,2 % des pages citées par GPT-5.5 Instant et 48,7 % des sites.
- Un outil de monitoring GEO qui s'appuie uniquement sur l'API retrouve 22,5 % à 22,9 % des pages selon la génération de modèle ; qui s'appuie uniquement sur Google retrouve 6,4 % à 9,4 %.
- 40,8 % (GPT-5.3) à 44,5 % (GPT-5.5) des pages uniques citées n'apparaissent que dans une seule exécution sur 20 ; la variance inter-runs rend un snapshot ponctuel non représentatif.
- Pour les prompts en chinois, ChatGPT reformule la requête en anglais dans 67,0 % à 69,6 % des cas, ce qui rend l'overlap avec Google local encore plus faible.
- Brèves : Google ajoute un pipeline d'ingest UGC distinct du crawl pour plateformes qualifiées (Niche SEO) ; Google retire le formulaire d'approbation de l'Indexing API (Actualité SEO) ; la nouvelle série Search Central YouTube « The Non-Canonical Cabinet » relance la position mot-clé dans l'URL = signal très faible, basiquement nul une fois le contenu indexé (Actualité SEO).

## Info du jour — Pilier GEO / search IA

Cinq chercheurs du National University of Singapore et de la Xi'an Jiaotong University ont publié le 11 octobre 2026 sur arXiv la préimpression [arXiv:2610.15382](https://arxiv.org/abs/2610.15382) « Understanding ChatGPT Citations: Evidence from Production Web Search Across Model Generations » (Yunxuan Jiang, Shiqi Zhang, Anqi Xing, Xiangyu Chang, Xiaokui Xiao). Le papier a été relayé le 18 octobre 2026 par [Search Engine Journal](https://www.searchenginejournal.com/openais-api-only-partly-matched-chatgpts-citations-paper-finds/593304/) sous la plume de Matt G. Southern.

Les auteurs ont rejoué 80 questions issues de Search Arena (40 en anglais, 40 en chinois, quatre types de requêtes : recommandation, lookup factuel, synthèse d'information, analyse) à travers quatre configurations de ChatGPT Web (GPT-5.2 et GPT-5.4 Thinking, GPT-5.3 et GPT-5.5 Instant), vingt exécutions par question entre le 29 mars et le 29 juillet 2026. Pour chaque question, ils ont aussi collecté jusqu'à cinq pages de résultats Google via SerpAPI (environ 43 résultats par question) et vingt réponses de l'OpenAI Responses API avec recherche web activée (modèles gpt-5.3-chat-latest et gpt-5.5). Une page compte comme citée si elle apparaît dans au moins une des vingt exécutions ChatGPT.

Les résultats, agrégés en moyennes sur les 80 questions, décrivent trois dispositifs de mesure externes qui ne reconstituent qu'une fraction des citations frontend :

- Google + Responses API combinés recouvrent 26,2 % des pages citées par GPT-5.5 Instant et 48,7 % des sites citées. Pour GPT-5.3 Instant, 28,3 % des pages et 50,3 % des sites.
- Responses API seule recouvre 22,9 % (GPT-5.3) à 22,5 % (GPT-5.5) des pages citées, Google seul 9,4 % (GPT-5.3) à 6,4 % (GPT-5.5), 26,1 % à 22,8 % des sites.
- Les pages citées par la Responses API elle-même sont citées par ChatGPT Web dans 23,3 % des exécutions pour GPT-5.5 Instant, 16,4 % pour GPT-5.3 Instant.

Variance inter-runs du même modèle : 44,5 % (GPT-5.5) et 40,8 % (GPT-5.3) des pages uniques citées n'apparaissent que dans une seule des vingt exécutions. L'overlap site-level entre runs est systématiquement supérieur à l'overlap page-level. Un modèle supervisé qui combine les deux signaux externes (API + Google) atteint un AUC supérieur à 0,74 pour GPT-5.3 et GPT-5.5 aux trois niveaux (URL, hostname, entité).

Comportement de reformulation des requêtes documenté : ChatGPT n'utilise jamais la formulation exacte de la question pour GPT-5.3 et GPT-5.5 (GPT-5.2 le fait dans 5,5 % des exécutions). Pour les prompts en chinois dont les recherches sont visibles, 67,0 % (GPT-5.3) et 69,6 % (GPT-5.5) des recherches sont exécutées en anglais seul.

Les auteurs documentent explicitement la bascule de modèle en cours de collecte : deux sessions ont changé de version active après 14 et 16 runs, ce qui invite à vérifier quelle version a produit chaque réponse. Toute la mesure prédate GPT-5.6 et GPT-6 ; les auteurs écrivent « monitoring strategies should be re-evaluated when the model behind ChatGPT changes ».

Trois lectures opérationnelles pour un consultant SEO/GEO :

- Un outil de monitoring de citations IA qui interroge la Responses API retrouve au mieux ~23 % des pages réellement citées par ChatGPT Web et ~50 % des sites, tant que la version du modèle est appariée. Vérifier la source de données de l'outil (API vs scraping frontend) devient un critère méthodologique de choix, pas un détail de documentation. Un outil qui n'affiche pas sa provenance de données vend une couverture qu'il ne fournit pas.
- Mesurer au niveau site plutôt qu'à l'URL rapporte systématiquement plus de recouvrement avec la vérité frontend. Pour un suivi de visibilité consultant, l'unité pertinente est l'hostname ou l'entité, pas la page. La page cite trop finement : elle rate l'overlap réel du site, et surestime la volatilité.
- Un run ponctuel manque près de la moitié des pages citées par un modèle. Un dispositif de mesure sérieux rejoue chaque prompt un nombre fixe de fois (ici 20) et agrège sur toute la fenêtre, en appariant explicitement la version de modèle. Toute mesure monoshot est une anecdote.

Rattachement doctrine. Fiche [[concepts/metriques-visibilite-geo]] : le papier ajoute une distinction méthodologique opératoire manquante jusqu'ici dans la fiche, celle de la source de données du dispositif de mesure (API Responses vs frontend scrapé). Un même outil peut mesurer deux objets différents sous la même étiquette « citations ChatGPT » selon qu'il interroge l'API ou qu'il scrape le frontend. La fiche gagne une 5e dimension d'audit d'outil, après apparition, densité, position, attribution clic. Fiche [[concepts/data-proprietaire]] : la donnée primaire du consultant (ce qui est réellement cité sur son client) reste intraçable par les deux sources externes à près de 75 % au niveau URL ; les tableaux de bord des éditeurs d'outils ne remplacent pas le monitoring frontend direct. Fiche [[concepts/tabou-visibilite]] : la « visibilité en IA » affichée par un dashboard est, dans la majorité des outils aujourd'hui, une mesure partielle d'une surface approximée, pas la citation réelle.

Trois réserves à poser. (1) Le dispositif de collecte est US-anglophone en majorité et chinois en minorité ; d'autres langues européennes et commerciales ne sont pas testées. (2) Les quatre types de requêtes (recommandation, fact, synthèse, analyse) ne pèsent pas le même poids dans un trafic de consultant SEO B2B ; la ventilation par type n'est pas publiée dans l'article tel que vu. (3) La mesure Google utilise SerpAPI et jusqu'à cinq pages de résultats ; une mesure Google avec AI Overviews et Discover inclus (surfaces supplémentaires de 2026) donnerait sans doute un overlap différent, à la hausse pour les sites, pas forcément pour les pages. Les auteurs ne testent pas AI Overviews comme proxy.

Trois prédictions ouvertes à surveiller.

1. Un éditeur d'outil GEO majeur (Peec AI, Profound, Writesonic, Otterly, llmpulse, Siftly, Averi) publie dans les six mois la source de données exacte (API vs frontend) de son dashboard citations ChatGPT, avec un comparatif de couverture : échéance 2027-04-30, confiance 0,45.
2. Une reproduction indépendante de l'étude Jiang et al. avec GPT-6 et GPT-5.6 et un échantillon de langues européennes (français, allemand, espagnol) sort avant 2027-06-30, confiance 0,35.
3. Un cabinet GEO publie avant 2027-03-31 une méthodologie standardisée explicitement multi-runs (≥ 20) avec appariement de version de modèle, et la revendique comme critère de différenciation : confiance 0,45.

## Brèves

### Google ajoute un pipeline d'ingest UGC distinct du crawl pour les plateformes forum et social qualifiées — Pilier Niche SEO

Google a mis en ligne le 8 octobre 2026 la documentation d'un **UGC Fresh Data Program**, relayée le 16 octobre par [Search Engine Journal](https://www.searchenginejournal.com/google-ugc-fresh-data-program-applications/593113/) sous la plume de Matt G. Southern. Le programme ouvre un canal d'ingest direct, distinct du crawl standard et de l'Indexing API, pour aider les plateformes approuvées à faire remonter leur UGC dans les surfaces Search. Google précise explicitement que la participation « does not guarantee inclusion in Search ».

Six critères d'éligibilité : contenu majoritairement UGC sur URLs stables (pas profils ni feeds), volume élevé et base utilisateurs significative, pages publiques accessibles à Googlebot sans paywall, authentification OAuth 2.0 et JSON-LD strictement validé, modération active anti-contenus illégaux, fraîcheur « ideally within minutes » et compteurs d'engagement mis à jour dans les 72 heures. Formulaire de candidature à sept champs incluant 10 URLs d'exemple UGC, MAU et date de lancement. Google qualifie la candidature de « merely an expression of interest » et annonce un délai de réponse de 6 à 8 semaines, avec documentation d'intégration livrée aux plateformes acceptées sans calendrier annoncé.

Trois distinctions utiles pour un consultant. (1) Le crawl standard reste la voie d'entrée par défaut pour tous les sites non-UGC. (2) L'Indexing API reste limitée à JobPosting et BroadcastEvent dans VideoObject, avec quota par défaut 200/jour. (3) Le UGC Fresh Data Program fonctionne sur un push plateforme-vers-Google, pas sur un pull Googlebot, mais les posts doivent rester publiquement crawlables. Pour un site non-UGC, la lecture pratique est que les forums et plateformes sociales approuvés gagnent une avance d'ingest sur la fraîcheur UGC, ce qui renforce la pression concurrentielle du UGC dans les SERPs mixtes. Les structured data forum post et profile page, supportées depuis novembre 2023, restent par ailleurs valables indépendamment du programme.

Google n'a nommé aucune plateforme participante, et la documentation ne précise ni la date de démarrage effective du pipeline, ni les surfaces Search alimentées, ni l'usage fait des compteurs d'engagement.

### Google retire le formulaire d'approbation de l'Indexing API et son texte d'instructions — Pilier Actualité SEO

Google a mis à jour le 16 octobre 2026 la documentation de son Indexing API, et [Search Engine Journal](https://www.searchenginejournal.com/google-indexing-api-docs-approval-form-removed/593292/) a documenté le changement le 17 octobre sous la plume de Matt G. Southern. Le changelog Google indique que la page quota a été mise à jour « to reflect the current quota limits and process » et « to remove an outdated form ». Il ne précise pas si l'exigence d'approbation elle-même est maintenue ou supprimée.

Ont été retirés : le formulaire d'approbation lui-même, les instructions demandant aux développeurs de solliciter un quota supérieur, la section « Request quota and approval » qui indiquait que « the quota may increase or decrease based on the document quality », l'étape « Request approval and quota » du quickstart initial, et trois notes de la page usage sur le quota par défaut qualifié « for testing ». Les quotas par défaut restent écrits : 200 requêtes publish par jour tous usages confondus, 180 requêtes metadata par minute, 380 requêtes par minute cross-endpoints, reset à minuit heure Pacifique. L'API reste limitée aux pages portant un markup JobPosting ou BroadcastEvent embarqué dans VideoObject. Le guide job posting, mis à jour pour la dernière fois le 8 septembre, recommande toujours l'Indexing API plutôt que les sitemaps pour les URLs d'offres d'emploi.

L'ambiguïté a un impact concret pour les opérateurs de job boards et de livestreams qui, selon la couverture de SEJ en septembre, rapportaient des délais d'approbation de plusieurs mois sans retour. La documentation ne dit pas ce qu'il advient des candidatures en cours ni si un projet jamais approuvé peut utiliser le quota par défaut pour une production live. Les développeurs peuvent voir leur quota actuel dans la Google API Console, mais le canal officiel de demande d'un quota supérieur a disparu de la documentation sans alternative publique.

### « The Non-Canonical Cabinet » : nouvelle série vidéo Search Central, premier épisode acte que les mots-clés dans l'URL sont un signal « incredibly small » — Pilier Actualité SEO

Google a lancé le 14 octobre 2026 le premier épisode de « The Non-Canonical Cabinet », une nouvelle série vidéo Search Central YouTube animée par Gary Illyes et Cherry Prommawin, avec un teaser mis en ligne le 6 octobre. [Search Engine Roundtable](https://www.seroundtable.com/google-search-urls-42305.html) l'a documenté le 14 octobre à 10h57 par Barry Schwartz. [Search Engine Journal](https://www.searchenginejournal.com/google-launches-a-video-series-for-odd-technical-seo-questions/592952/) a repris le 14 octobre sous la plume de Matt G. Southern.

Le premier épisode traite les caractères admissibles dans les noms de domaine et les chemins URL (emojis, caractères non latins, séparateurs), et surtout la question du poids des mots-clés d'URL dans le classement. Les trois citations verbatim d'Illyes publiées par les deux sources : les mots-clés dans une URL sont « an incredibly small signal » ; « It really only matters when we have absolutely nothing else to go on », par exemple pour un site de quelques secondes sans contenu ; une fois que Google voit du contenu, les mots-clés du domaine et de l'URL deviennent « basically irrelevant ».

Les autres points traités dans l'épisode : les emojis sont techniquement crawlables dans les chemins mais s'affichent mal pour certains utilisateurs ; les noms de domaine non latins passent par Punycode et peuvent prêter à confusion entre scripts proches ; Google traite les mots séparés par des underscores comme un seul mot et recommande explicitement les tirets. Google peut aussi détecter les URLs à motif spam.

Pour un consultant, l'épisode ne change rien pour un site existant qui suit déjà la documentation URL structure. Il clarifie pour un site nouveau en création qu'il n'y a aucun intérêt à bourrer un URL de mots-clés : le signal est marginal au départ et disparaît dès que le contenu est indexé. Illyes vocalise une position que Google tient depuis 2016 ; la nouveauté est le format vidéo thématique récurrent, et le fait que Google reprenne la parole directement sur un sujet où les blogs d'agences continuent de recommander les URLs riches en mots-clés.

---

*Édition rédigée par SyntheticBrain, 19 octobre 2026. Voix propre d'analyste search/IA, vouvoiement, zéro métaphore. Rien n'est envoyé.*
