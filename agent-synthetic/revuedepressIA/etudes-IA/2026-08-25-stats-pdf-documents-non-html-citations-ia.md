---
type: query
skill: seo-page-statistiques
status: draft
title: "PDFs et documents non-HTML dans les citations IA : présents à l'entraînement, absents au moment de répondre (2025-2026)"
tags: [pdf, non-html, citations-ia, crawl, retrieval, training-data, geo, aeo]
created: 2026-08-25
updated: 2026-08-25
sources: 7
confidence: medium
---

# PDFs et documents non-HTML dans les citations IA — 25 août 2026

Les PDFs représentent 1,016 % des pages crawlées sur le web (Common Crawl, CC-MAIN-2026-34, août 2026). Dans le corpus d'entraînement The Pile, arXiv seul pèse 8,96 % du dataset (112 GiB). La même technologie IA qui a appris sur une montagne de PDFs académiques refuse, dans ses réponses en temps réel, de citer des URLs au format .pdf. Ce que les études de citabilité mesurent comme "format de fichier" recouvre en réalité deux phénomènes sans rapport.

---

## Les chiffres clés (vérifiés à la source)

**Web crawlé et Common Crawl**

Common Crawl (CC-MAIN-2026-34, dernière archive mensuelle disponible) mesure la composition MIME du web crawlable :
- HTML (text/html) : 98,26 % selon les en-têtes HTTP
- PDF (application/pdf) : 1,016 % selon les en-têtes HTTP
- Détection Tika (contenu réel) : HTML 90,79 %, PDF 1,031 %

L'écart entre 98,26 % et 90,79 % pour l'HTML reflète des pages mal déclarées (JavaScript, XML) plutôt qu'une présence cachée de PDFs. La proportion de PDFs reste stable à environ 1 % quelle que soit la méthode de détection. Common Crawl est la base de données principale derrière la majorité des corpus d'entraînement ouverts (FineWeb, RedPajama-v2, DataComp).

**The Pile et les sources académiques**

Dans The Pile (EleutherAI, arXiv:2101.00027, 825 GiB total), les composants "PDF-first" occupent une place bien plus large que dans le web crawlé :
- arXiv : 8,96 % (112,42 GiB)
- PubMed Central : 14,40 % (180,55 GiB)
- PubMed Abstracts : 3,07 % (38,53 GiB)
- PhilPapers : 0,38 % (4,76 GiB)
- NIH ExPorter : 0,30 % (3,79 GiB)
- Total sources académiques/PDF-first : environ 27 % du dataset

**Point technique** : arXiv ne livre pas ses papiers au format PDF brut dans The Pile. Le corpus utilise les sources LaTeX (.tex) pour extraire le texte, pas les PDFs rendus. PubMed Central fournit du XML/HTML structuré. Les PDFs en tant que fichiers binaires sont donc sous-représentés dans les corpus d'entraînement réels même là où on les attendrait.

**Citabilité runtime : le seul chiffre publié**

MaxAEO a suivi 61 400 citations issues de 9 200 prompts B2B-SaaS sur sept moteurs (ChatGPT, Gemini, Perplexity, Claude, Copilot, Google AI Mode, AI Overviews) sur huit semaines en début 2026. Le constat sur les formats non-HTML est qualificatif : "PDFs et transcriptions sont parfois cités, vidéo et audio rarement sans équivalent texte." Aucun chiffre de taux de citation n'est fourni pour les PDFs. Les 61 400 citations classées par MaxAEO portent sur des types de page (listicles, guides, pages comparatives), pas sur des formats de fichiers.

**Conversion PDF → HTML : une mesure de terrain**

Graph Digital, agence britannique spécialisée en visibilité IA, a converti 73 PDFs en pages HTML pour un fabricant industriel de taille intermédiaire, puis mesuré les changements de visibilité dans ChatGPT, Perplexity et Google AI Mode. Résultat : +52 % de visibilité IA pour les gammes de produits concernées. Ni la durée du suivi ni la méthode de calcul de "visibilité IA" ne sont détaillées dans la publication.

---

## Architecture du problème : trois types de PDFs, trois réponses différentes

Les PDFs ne forment pas une catégorie homogène pour les moteurs IA.

**PDFs textuels ouverts** (URL publique se terminant en .pdf, contenu textuel extrait). Ces fichiers sont techniquement crawlables par GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot. Ils sont indexés comme n'importe quelle URL. La documentation officielle d'OpenAI et d'Anthropic ne mentionne pas de traitement différencié pour les PDFs. Inter-Dev (étude B2B, 2026) confirme que les "PDFs textuels non verrouillés" figurent dans la même catégorie "crawlable et citable" que les pages HTML publiques. En pratique, ces PDFs sont rarement cités car les moteurs IA leur préfèrent leurs équivalents HTML quand ils existent.

**PDFs scannés ou basés sur des images**. Ces fichiers contiennent des images de texte, non du texte machine-lisible. Aucun des crawlers IA déclarés ne documente de capacité OCR à la volée. Ces fichiers sont effectivement invisibles : crawlés en apparence (le bot reçoit un PDF), mais non extraits. Le problème est identique à celui d'une page protégée par JavaScript rendu côté client.

**PDFs verrouillés derrière un formulaire**. Ces fichiers ne sont jamais crawlés, quelle que soit leur qualité technique. L'obstacle est l'accès, pas le format.

---

## Pourquoi ces chiffres révèlent une confusion fondamentale

### La mémoire et le retrieval sont deux systèmes distincts

Les LLMs (grands modèles de langage) apprennent sur des corpus d'entraînement qui incluent massivement des textes académiques, dont une partie provient de sources PDF-first (arXiv, PubMed). Cette connaissance est encodée dans les poids du modèle, pas dans une base de données consultable.

Au moment de répondre, les moteurs IA qui opèrent en mode "retrieval" (recherche en temps réel) consultent un index web distinct, comparable à un moteur de recherche classique. Cet index est construit à partir du web crawlé. Le web crawlé est constitué à 98 % d'HTML et à 1 % de PDFs.

Conséquence : un modèle peut avoir une connaissance paramétrique profonde d'un article paru sur arXiv (lu en LaTeX pendant l'entraînement) tout en étant incapable de le citer depuis une URL en .pdf au moment de la requête, faute d'index retrieval sur ce format.

### Le paradoxe arXiv

arXiv.org est un domaine fréquemment cité par les moteurs IA. Perplexity cite régulièrement des papiers scientifiques dans ses réponses avec des URLs de type arxiv.org/abs/XXXXXXX. Ce sont des pages HTML (page d'abstract), pas les PDF qui se trouvent à arxiv.org/pdf/XXXXXXX. Les moteurs IA citent l'enveloppe HTML d'arXiv, non le fichier PDF qu'elle référence. La distinction ne change rien pour l'utilisateur final, mais elle est essentielle pour comprendre ce que "citer un PDF" signifie dans ce contexte : presque jamais.

### Le gain +52 % de Graph Digital : ce qu'il mesure réellement

Convertir un PDF en page HTML ne change pas seulement le format. Cela ajoute généralement des balises HTML structurées, un titre H1, des méta-données, des liens internes, une indexation dans le sitemap XML, et une URL propre. Il est impossible d'attribuer le gain de 52 % au seul changement de format. Une page HTML d'un fabricant industriel bien rédigée surpassera toujours un PDF équivalent, mais pas uniquement parce qu'elle est en HTML.

---

## Données de première main

Ce bloc est réservé honnêtement. Le portefeuille mesuré dans ce repository ne comporte pas de données GSC ou d'analytics IA isolant les URLs .pdf des URLs .html dans les citations reçues. L'intégration d'un export PDF-vs-HTML depuis Ahrefs Brand Radar ou depuis un suivi MaxAEO propre constitue le chantier à venir pour documenter ce point en données de première main.

---

## Contre-analyse

### La "mort du PDF" est prématurée

Plusieurs cas documentés montrent des PDFs cités directement dans des réponses IA, notamment sur Perplexity lors de requêtes académiques. Perplexity crawle des PDFs publics dans certains contextes, en particulier via son mode Academic Focus (requêtes de type recherche scientifique). La règle "les PDFs ne sont pas cités" est une tendance statistique, pas une loi.

### L'upload utilisateur contourne l'obstacle

Perplexity Pro permet d'uploader jusqu'à 3 PDFs par jour pour les analyser. Claude.ai et ChatGPT offrent des fonctions similaires. Ces usages n'apparaissent pas dans les études de citabilité publique (qui mesurent les citations dans des réponses générées sur des requêtes ouvertes, sans document joint). Le "PDF invisible aux moteurs IA" est vrai pour la citabilité organique, pas pour l'usage documentaire.

### Le problème de composition de corpus

The Pile date de 2021. Les corpus d'entraînement des modèles récents (GPT-4, Claude 3, Gemini) ne sont pas publics. Certains incluent des partenariats avec des éditeurs académiques (Wiley, Springer) qui fournissent du contenu PDF sous licence. La proportion réelle de PDFs dans les données d'entraînement des modèles actuels est inconnue.

### L'avantage structurel du HTML reste relatif

Le gain à attendre d'une conversion PDF → HTML dépend du secteur. Dans des verticales où les PDFs sont la norme de référence (recherche médicale, documentation technique, normes ISO), les moteurs IA ont développé une tolérance au format, ou accèdent aux données via leur mémoire paramétrique. L'impact de la conversion sera différent d'une verticale à l'autre.

---

## FAQ

**Les robots.txt différencient-ils HTML et PDF ?**
Non. Les directives robots.txt s'appliquent à des chemins d'URL, pas à des types MIME. Un site peut bloquer /docs/ et autoriser /blog/ sans distinction de format. Les crawlers IA lisent les extensions d'URL mais leur comportement face à un .pdf non bloqué n'est pas documenté officiellement par OpenAI ou Anthropic.

**arXiv.org est-il un bon contre-exemple ?**
Partiellement. arXiv est très cité par les moteurs IA, mais presque toujours via ses pages HTML d'abstract (arxiv.org/abs/), pas via ses PDFs (arxiv.org/pdf/). La présence d'arXiv dans les citations IA prouve que le domaine est autorité, pas que les PDFs sont crawlés.

**Que faire d'un catalogue produits en PDF ?**
Convertir en HTML les fiches qui ont une valeur commerciale ou comparative est la recommandation dominante dans la littérature GEO. Le gain vient de la structure HTML, du titre H1, des métadonnées et de l'indexation, pas uniquement du changement de format.

**Les LLMs "savent" ce qu'il y a dans les PDFs ?**
Souvent oui, via la mémoire paramétrique (entraînement sur arXiv, PubMed, etc.). Mais "savoir" et "citer depuis une URL .pdf au moment de la requête" sont deux choses différentes. La connaissance est là, la citation runtime peut être bloquée.

---

## [À SOURCER]

- Taux de citation des URLs .pdf vs .html par moteur (ChatGPT, Perplexity, Gemini, Claude) : aucune étude à large échelle n'a mesuré ce ratio directement.
- Proportion réelle de PDFs dans les corpus d'entraînement des modèles post-2022 (GPT-4o, Claude 3.5, Gemini 2.0) : non divulguée.
- Comportement de PerplexityBot face aux PDFs publics en dehors du mode Academic Focus : non documenté officiellement.
- Gain isolé "format seul" dans la conversion PDF → HTML (sans changement de contenu, de structure ou de méta-données) : inexistant dans la littérature actuelle.
- Données France : proportion de citations IA issues d'URLs .pdf sur des domaines français (académiques, institutionnels, gouvernementaux).

---

## Sources

1. **Statistics of Common Crawl Monthly Archives by commoncrawl** — Common Crawl Foundation, CC-MAIN-2026-34, août 2026. URL : https://commoncrawl.github.io/cc-crawl-statistics/plots/mimetypes. Consulté le 25 août 2026.

2. **The Pile: An 800GB Dataset of Diverse Text for Language Modeling** — Gao et al., EleutherAI, arXiv:2101.00027, janvier 2021 (HTML lisible : ar5iv.labs.arxiv.org/html/2101.00027). Consulté le 25 août 2026.

3. **Content Formats for AI Citations: Ranked by Real Citation Data** — MaxAEO, 2026. URL : https://maxaeo.ai/blog/content-formats-ai-citations/. Consulté le 25 août 2026.

4. **Why PDF documents make technical expertise invisible to AI** — Graph Digital, 2026. URL : https://graph.digital/guides/ai-visibility/pdf-invisibility. Consulté le 25 août 2026.

5. **From Gated to Ghosted: The High Cost of Blocking AI from Your Best Specs** — Inter-Dev, 2026. URL : https://inter-dev.co.il/from-gated-to-ghosted-the-high-cost-of-blocking-ai-from-your-best-specs/. Consulté le 25 août 2026.

6. **Overview of OpenAI Crawlers** — OpenAI, documentation officielle, 2025-2026. URL : https://developers.openai.com/api/docs/bots. Consulté le 25 août 2026.

7. **PDF Parsing Documentation** — Crawl4AI, v0.9.x, 2025. URL : https://docs.crawl4ai.com/advanced/pdf-parsing/. Consulté le 25 août 2026.
