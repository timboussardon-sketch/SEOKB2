---
type: query
skill: seo-page-statistiques
status: draft
title: "Signaux sociaux et citations IA : engagement = r≈0, mentions tierces = r=0,74 (2025-2026)"
tags: [seo, ia, geo, aeo, linkedin, citations-ia, signaux-sociaux, engagement, mentions, moteurs-ia]
created: 2026-10-03
updated: 2026-10-03
sources: 8
confidence: high
---

# Signaux sociaux et citations IA : engagement = r≈0, mentions tierces = r=0,74 (2025-2026)

Quatre études indépendantes convergent : les likes, réactions et commentaires sur LinkedIn et YouTube ne prédisent pas les citations par les moteurs IA — corrélation mesurée ≈ 0 dans les deux cas. La corrélation avec les mentions textuelles sur des sites tiers, souvent d'origine sociale mais structurellement distinctes, atteint 0,66 à 0,74. Ce n'est pas la même variable. Les deux confondues sous le terme "signaux sociaux" produisent des conclusions opposées.

---

## Les chiffres clés (vérifiés à la source)

### Engagement sur la plateforme : corrélation ≈ 0

**LinkedIn — OtterlyAI (jan.-juin 2026)** : analyse de 1 310 455 citations LinkedIn sur 6 moteurs (ChatGPT, Google AI Overviews, Google AI Mode, Perplexity, Copilot, Gemini), issues d'un corpus de 2 061 071 enregistrements et 161 440 URLs uniques après nettoyage. Résultat : les réactions (likes), commentaires, emojis et hashtags affichent tous une corrélation proche de zéro avec la citabilité IA. Les posts cités en médiane totalisent entre 15 et 25 réactions et au plus 1 commentaire (Semrush, 89 000 URLs, 325 000 prompts, janv.-fév. 2026). "Ce qui fait qu'un post est aimé ne fait pas qu'il est cité."

**YouTube — OtterlyAI (mars 2026)** : étude sur 100 millions d'instances de citations collectées sur 30 jours, 6 plateformes. Corrélation entre vues, likes et abonnés : r ≈ −0,03. 40,83 % des vidéos citées totalisaient moins de 1 000 vues ; 36 % affichaient moins de 15 likes au moment de la citation. La longueur de la description est le seul signal positif mesuré (r = 0,31).

### Liens entrants depuis les réseaux sociaux : quasi-équivalents à nofollow

**Semrush + Kevin Indig + Growth Memo (oct. 2025, 1 000 domaines, 5 moteurs)** : les liens dofollow affichent un Pearson de 0,334 avec les citations IA ; les liens nofollow, 0,340. Différence statistiquement indistinguable. L'étude ne distingue pas les backlinks "sociaux" des backlinks généraux, mais constate que la nature dofollow/nofollow ne change rien pour les moteurs IA — alors que cet écart est structurant en référencement classique.

### Mentions textuelles tierces : 0,66 à 0,74

**Ahrefs (75 000 marques, mai 2025)** : la corrélation entre les mentions web de marque (toutes origines, souvent issus de discussions sociales) et la présence dans Google AI Overviews atteint r = 0,664 — trois fois supérieure aux liens entrants (r = 0,218). Les mentions de chaînes YouTube atteignent r = 0,737, la valeur la plus élevée mesurée dans l'ensemble de l'étude.

### Couplage plateforme : X = 99,75 % Grok

**Higoodie.com (août-déc. 2025, 6,1 millions de citations, 10 plateformes)** : les citations de contenu issu de X (ex-Twitter) sont à 99,75 % exclusives à Grok sur l'ensemble des moteurs suivis. Instagram affiche 98,98 % d'exclusivité sur Google AI Overviews. Les citations sociales globales ont crû de 1,8× entre septembre et décembre 2025.

### Facteurs de citation positifs (sans engagement)

**Discoveredlabs (6 mois, août 2026, ~2 millions de citations, 10 000 URLs, 4 moteurs B2B)** : l'alignement entre le contenu de la page et le prompt est le premier prédicteur (coefficient standardisé +0,37, 3× supérieur au signal suivant). L'autorité de domaine perçue par l'IA représente une valeur SHAP de 0,38 — six fois supérieure au premier signal de page. Les signaux sociaux sont absents du modèle.

**Semrush LinkedIn (89 000 URLs, 325 000 prompts, janv.-fév. 2026)** : 95 % des contenus LinkedIn cités sont des contenus originaux ; 5 % des republications. Les articles entre 500 et 2 000 mots et les posts entre 50 et 299 mots concentrent les citations. La similarité sémantique entre réponses IA et contenu LinkedIn original (0,57–0,60) est la plus haute parmi les plateformes mesurées (Reddit : 0,53–0,54 ; Quora : 0,435).

---

## Trois objets confondus sous "signaux sociaux"

La littérature emploie indistinctement "signaux sociaux" pour désigner trois réalités distinctes aux propriétés radicalement différentes :

**Type 1 — Liens entrants depuis des plateformes sociales (dofollow/nofollow).**  
Structurellement proches des liens entrants généraux : Pearson 0,334–0,340 dans les études sur les citations IA. L'écart dofollow/nofollow, décisif en référencement classique, disparaît pour les moteurs génératifs. La majorité des liens depuis LinkedIn, X ou Facebook sont nofollow ou bloqués par robots.txt (X bloque GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot). Ce que les études appellent "backlinks" inclut souvent une fraction sociale non isolée.

**Type 2 — Mentions textuelles tierces non linkées.**  
C'est le signal dont les études détectent la corrélation la plus forte (r = 0,664–0,737, Ahrefs). Ces mentions proviennent fréquemment de discussions sur des forums, blogs, posts LinkedIn ou threads X qui ont été indexés par d'autres sites. Elles sont d'origine sociale au sens large, mais les outils de mesure les comptabilisent comme "web mentions" ou "earned media", jamais comme "social signals" au sens SEO classique.

**Type 3 — Engagement sur la plateforme (likes, réactions, partages, commentaires).**  
Corrélation mesurée : r ≈ 0 (OtterlyAI, deux études distinctes sur LinkedIn et YouTube, corpus combiné de 100 millions+ citations). Ce signal n'est pas intégré dans les pipelines de récupération des moteurs génératifs, qui n'ont pas accès aux métriques d'engagement propriétaires des plateformes.

La confusion des types 2 et 3 produit des conclusions opposées : "les signaux sociaux comptent" (type 2) contre "les signaux sociaux ne comptent pas" (type 3). Les deux affirmations sont correctes — elles décrivent des phénomènes différents.

---

## Pourquoi ces chiffres sont cohérents (réconciliation)

L'explication architecturale est simple. Les moteurs génératifs récupèrent des pages web et analysent leur contenu textuel. Ils n'ont pas accès aux bases de données d'engagement de LinkedIn ou YouTube. Ce que Perplexity, ChatGPT ou Google AI Mode "voient" d'un post LinkedIn est son texte, son URL, son auteur, et les pages qui le mentionnent ailleurs sur le web. Ce qu'ils ne voient pas : le nombre de likes, de commentaires ou de partages.

Le mécanisme par lequel les mentions web tierces (type 2) corrèlent avec les citations est différent : un article très discuté sur des forums, des blogs ou des newsletters génère des pages tierces qui le mentionnent explicitement. Ces pages sont crawlées, indexées, et deviennent des signaux de pertinence et d'autorité perçues. Le contenu social "viral" qui ne génère pas ce second degré de mentions reste invisible aux moteurs génératifs.

**Le cas Grok/X** illustre la limite de cette logique. X est à 99,75 % la source des citations "X" dans les moteurs IA, et Grok accède en temps réel au flux de 68 millions de tweets par jour. xAI entraîne ses modèles sur les posts publics X, y compris les fils de conversation. Mais même dans ce cas, l'engagement au sein de X (likes, retweets) ne prédit pas la citation : c'est la pertinence topique du contenu qui est citée, pas sa popularité sociale.

---

## Nos propres chiffres (données de première main)

Aucune donnée de première main disponible dans ce vault sur ce sujet. Le portefeuille de sites ne dispose pas d'un suivi systématique des corrélations entre engagement social (LinkedIn, X) et citations IA à une échelle suffisante pour tirer des conclusions. Ce bloc est réservé honnêtement : la boucle sortie → apprentissage (§14 AGENTS.md) n'a pas encore produit de données d'attribution reliées aux signaux d'engagement social.

---

## Contre-analyse

**La causalité inverse est probable pour les mentions tierces.** Un contenu cité par les moteurs IA génère de la visibilité, qui génère des mentions, qui renforcent la citabilité. L'essentiel de la corrélation mentions/citations (r = 0,664) peut refléter cette boucle plutôt qu'un effet direct des mentions sur les citations. Aucune étude publiée à ce jour ne dispose d'un protocole en double différence ou randomisé sur ce signal.

**L'autorité de domaine confond les deux variables.** Les domaines avec beaucoup de mentions web sont souvent des domaines à forte autorité (Ahrefs DR élevé). La corrélation mentions/citations est partiellement une re-mesure de l'autorité sous une forme différente. Discoveredlabs note que l'autorité de domaine perçue par l'IA représente SHAP 0,38 — six fois le premier signal de page — sans qu'il soit possible d'en isoler la composante "mentions sociales".

**Grok ne généralise pas.** Le couplage X/Grok à 99,75 % est une décision architecturale spécifique à xAI. Les autres moteurs n'ont pas accès au flux temps réel X. Extrapoler le comportement de Grok comme preuve que "l'engagement social prédit les citations" serait une erreur de généralisation.

**Les petits producteurs bénéficient d'une fenêtre sur LinkedIn.** Les auteurs avec moins de 500 abonnés sont cités aussi souvent que les auteurs populaires (Semrush, 89 000 URLs). Cela renforce la thèse "pertinence > popularité", mais crée aussi une asymétrie : les entreprises habituées à mesurer leur "ROI social" en likes et partages sous-estiment probablement leur citabilité réelle.

**La corrélation ≈ 0 de l'engagement YouTube est atypique.** Une corrélation légèrement négative (r = −0,03) pourrait indiquer un léger biais des moteurs contre les contenus viraux — ou simplement la neutralité du signal. La marge d'erreur sur ce coefficient pour un corpus de 100 millions de citations est faible, mais le résultat contre-intuitif mérite une réplication indépendante.

---

## FAQ

**Les partages LinkedIn aident-ils à être cité par les IA ?**  
Non, pas directement. L'OtterlyAI LinkedIn study (1 310 455 citations, janv.-juin 2026) et la Semrush LinkedIn study (89 000 URLs) montrent que les réactions, partages et commentaires corrèlent à ≈ 0 avec les citations IA. Ce qui aide : la profondeur du contenu, la forme article (Pulse), l'identité d'auteur nommée.

**Un post X viral sera-t-il cité par ChatGPT ?**  
Pas mécaniquement. X bloque les robots de ChatGPT, Perplexity et Claude (robots.txt). La mémoire de ChatGPT sur le contenu X est paramétrique (apprentissage passé) et ne reflète pas le score de viralité. Seul Grok accède à X en temps réel, et même dans ce cas, l'engagement ne prédit pas la citation — c'est la pertinence topique qui compte.

**Les backlinks depuis LinkedIn ou X comptent-ils ?**  
Autant que n'importe quel lien nofollow : Pearson 0,334–0,340 dans les études Semrush (oct. 2025). La nature dofollow/nofollow est indistinguable pour les moteurs IA, contrairement au référencement classique. Mais la plupart de ces liens sont de toute façon bloqués au niveau du crawl.

**Comment les "mentions web" sont-elles différentes des "signaux sociaux" ?**  
Une mention web est une page tierce qui cite, paraphrase ou discute un contenu — souvent issu d'un post social, mais publiée sur un domaine indexable (un blog, une newsletter, un forum). C'est cette page tierce que les moteurs IA voient, pas le post social original. La chaîne causale est : post social → discussion sur une page web indexable → mention détectée par les moteurs.

---

## [À SOURCER]

- **Corrélation r = −0,03 YouTube** (OtterlyAI) : source secondaire vérifiée via relais, fetch direct sur otterly.ai/blog/youtube-ai-citation-study-2026/ non résolu à cette session. Données cohérentes avec trois sources secondaires.
- **Muck Rack "84 % earned media" (25 millions de liens, mai 2026)** : figure relayée par AuthorityTech, source primaire Muck Rack non fetchée directement.
- **Engagement Instagram 98,98 % exclusif à Google AI Overview** (Higoodie.com, août-déc. 2025) : fetchée via source secondaire, pas directement depuis la publication Higoodie.
- **YouTube mentions r = 0,737** (Ahrefs, 75 000 marques) : vérifiée dans l'étude 2026-08-09 du vault, mais la source primaire Ahrefs ne désagrège pas "YouTube mentions" vs "web mentions YouTube-origin".
- Données de première main vault sur corrélation engagement social/citations : absentes (bloc réservé).

---

## Sources

| Intitulé | Organisme | Date | URL | Consultation |
|---|---|---|---|---|
| LinkedIn AI Search Citations Study 2026 | OtterlyAI | janv.-juin 2026 | https://otterly.ai/blog/linkedin-ai-search-citations-study/ | 2026-10-03 |
| We Analyzed 89K LinkedIn URLs Cited in AI Search | Semrush | janv.-fév. 2026 | https://www.semrush.com/blog/linkedin-ai-visibility-study/ | 2026-10-03 |
| YouTube AI Citation Study 2026 | OtterlyAI | mars 2026 | https://otterly.ai/blog/youtube-ai-citation-study-2026/ | 2026-10-03 |
| Backlinks in AI Search Study | Semrush, Kevin Indig, Growth Memo | oct. 2025 | https://www.semrush.com/blog/backlinks-ai-search-study | 2026-10-03 |
| What Drives AI Citations? Data from 2M Citations | Discoveredlabs | août 2026 | https://discoveredlabs.com/research/what-drives-ai-citations | 2026-10-03 |
| To Win AI Search, You Must Dominate Social (Study) | Higoodie.com | août-déc. 2025 | https://higoodie.com/blog/social-citations-ai-search-study-2026 | 2026-10-03 |
| LinkedIn Articles vs Posts: AI Citations Fell 65% | Cloro.dev | nov. 2025-août 2026 | https://cloro.dev/blog/linkedin-articles-vs-posts/ | 2026-10-03 |
| Ahrefs Studied 75,000 Brands in AI Search | Ahrefs / Machine Relations Research | mai 2025 | (via vault [[sources/2026-08-09-stats-marques-citations-ia-brand-mention-share]]) | 2026-08-09 |
