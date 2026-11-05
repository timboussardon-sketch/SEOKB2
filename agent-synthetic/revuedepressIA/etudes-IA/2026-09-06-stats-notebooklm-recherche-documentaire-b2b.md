---
type: query
skill: seo-page-statistiques
title: "NotebookLM (Gemini Notebook) : 30 millions d'utilisateurs, une logique de citation radicalement distincte des moteurs IA (2024-2026)"
tags: [notebooklm, rag, geo, citations-ia, recherche-documentaire, b2b, audio-overview, gemini]
created: 2026-09-06
updated: 2026-09-06
sources: 8
confidence: medium
status: draft
---

# NotebookLM (Gemini Notebook) : 30 millions d'utilisateurs, une logique de citation radicalement distincte des moteurs IA (2024-2026)

30 millions d'utilisateurs et 600 000 organisations en juillet 2026 — c'est le chiffre que Google a rendu public en rebaptisant NotebookLM sous le nom Gemini Notebook. C'est aussi un chiffre presque inutile pour mesurer l'influence de l'outil sur la citabilité des contenus. Car NotebookLM n'est pas un moteur de recherche : il ne choisit pas les sources à la place de l'utilisateur. L'utilisateur les choisit lui-même. Ce renversement de logique rend caducs tous les outils de mesure standard du secteur (Profound, Peec AI, Semrush AI Toolkit, Otterly.ai).

---

## Les chiffres clés (vérifiés à la source)

### Croissance utilisateurs — deux jalons officiels Google

| Date | Utilisateurs | Organisations |
|---|---|---|
| Octobre 2024 | « Des millions » | 80 000+ |
| Juillet 2026 | 30 millions | 600 000+ |

Les deux chiffres proviennent de déclarations officielles Google, relayées sans intermédiaire par 9to5Google. Le premier date du retrait du label « expérimental » (17 octobre 2024). Le second accompagne le renommage en Gemini Notebook (16 juillet 2026). Soit une multiplication par au moins 7,5 du nombre d'organisations en 21 mois — de 80 000 à 600 000.

### Audio Overview : la fonctionnalité qui a déclenché la croissance

Google a lancé la fonctionnalité Audio Overview (discussion audio entre deux animateurs IA générée à partir des documents uploadés) en septembre 2024. Elle est devenue virale en octobre 2024 — Wall Street Journal, Axios, et les réseaux sociaux ont largement diffusé des exemples de conversations IA générées à partir de mémoires universitaires, de contrats juridiques ou de livres entiers.

Spotify a intégré la technologie dans son Wrapped 2024, générant des résumés audio personnalisés à partir des habitudes d'écoute de ses utilisateurs. C'est l'un des rares cas vérifiés d'intégration grand public de NotebookLM à l'extérieur de Google.

En avril 2025, Google a étendu Audio Overview à plus de 50 langues, en mode bêta — source primaire : blog officiel Google Workspace (29 avril 2025). Le mode interactif (possibilité d'interrompre les animateurs pour poser des questions) est resté exclusivement anglophone à cette date.

### Capacités techniques par plan — limites de sources par notebook

| Plan | Sources max par notebook | Source unique max |
|---|---|---|
| Standard (gratuit) | 50 | 500 000 mots ou 200 Mo |
| Plus | 100 | idem |
| Pro | 300 | idem |
| Ultra | 500 à 600 | idem |

Types de sources acceptés : PDFs, Google Docs, Google Sheets, fichiers Word (.docx), URL web, vidéos YouTube (via transcription automatique), fichiers texte, images. Un même fichier, quelle que soit sa taille jusqu'à la limite, compte comme une seule source.

### Chronologie produit

- **Mai 2023** : introduction sous le nom « Project Tailwind » au Google I/O
- **Juin 2023** : rebaptisé NotebookLM, accès limité
- **17 octobre 2024** : retrait du label « expérimental », accès général
- **Décembre 2024** : lancement NotebookLM Plus (entreprises via Google Workspace, abonnés Gemini Advanced)
- **Novembre 2025** : ajout de Deep Research — l'outil peut désormais naviguer sur le web de manière autonome pour compléter les sources uploadées par l'utilisateur
- **16 juillet 2026** : rebaptisé Gemini Notebook, intégré à l'écosystème Gemini

---

## Pourquoi ces chiffres ne disent pas l'essentiel — la transformation originale

### Trois types de moteurs IA, trois logiques de citation

Les études du secteur (Profound, Peec AI, SE Ranking, Ahrefs, Semrush) mesurent toutes la même chose : quels domaines apparaissent dans les réponses des moteurs IA en fonction des requêtes posées. Ce modèle fonctionne pour ChatGPT Search, Perplexity, Google AI Mode et AI Overviews, où **l'algorithme choisit les sources**.

NotebookLM introduit une troisième logique, absente de toute grande étude cross-engine :

| Type | Qui choisit les sources | Mesurable par les outils secteur |
|---|---|---|
| Mémoire paramétrique (ChatGPT sans web) | Le modèle, à l'entraînement | Non (pas de runtime retrieval) |
| Retrieval algorithmique (Perplexity, AI Mode) | L'algorithme à chaque requête | Oui — c'est ce que mesurent Profound, Peec AI, etc. |
| RAG utilisateur (NotebookLM) | **L'utilisateur, avant la requête** | **Non — structurellement invisible** |

Dans NotebookLM, la page d'un éditeur n'est citée que si un utilisateur a pris la décision de l'uploader dans son notebook. L'outil de citation IA n'a accès à aucune donnée externe : il répond à partir du corpus privé de l'utilisateur, et de rien d'autre. Les outils de mesure qui envoient des prompts standardisés ne peuvent pas capter ce qui se passe dans 30 millions de notebooks privés.

### Le paradoxe de l'invisibilité mesurable

Il est impossible, depuis l'extérieur, de savoir si un contenu est cité dans NotebookLM. Aucun referral, aucune API, aucune donnée de citation. Google Search Console ne remonte pas ces signaux. Le trafic issu de NotebookLM apparaît en « accès direct » dans Google Analytics 4 — quand l'utilisateur clique sur un lien dans sa réponse, ce qui est loin d'être systématique.

La conséquence : la bataille pour être cité dans NotebookLM ne se joue pas au niveau du retrieval, mais **en amont** — au moment où l'utilisateur décide d'uploader ou non un contenu dans son notebook. C'est une bataille de confiance et de réputation qui précède entièrement la phase algorithmique.

### L'exception Deep Research (novembre 2025)

Le lancement de Deep Research a partiellement changé la donne. Quand une requête dépasse le corpus uploadé, l'outil peut désormais naviguer sur le web de manière autonome pour trouver des sources complémentaires. NotebookLM se rapproche ici du modèle Perplexity — avec un retrieval algorithmique supplémentaire qui échappe au contrôle de l'utilisateur.

Mais ce retrieval autonome s'effectue à partir d'un contexte (les documents déjà uploadés) que l'utilisateur a lui-même défini. L'algorithme comble des lacunes dans un corpus curé, il ne remplace pas la curation. La logique reste fondamentalement distincte des moteurs de recherche généralistes.

---

## Nos propres données (données de première main)

Cette base de connaissances documente NotebookLM depuis avril 2026 dans deux entrées :

- **[[entities/notebooklm]]** (créé 2026-04-11) : stub de contraste, où l'outil est cité comme exemple canonique de « RAG stateless » selon la taxonomie de Karpathy. La page pose explicitement les questions ouvertes : NotebookLM maintient-il un état persistant entre sessions (notebooks sauvegardés) ? Les sources uploadées dans NotebookLM influencent-elles indirectement les signaux de popularité que Google AI Mode utilise ?
- **[[concepts/persistent-wiki-vs-rag]]** (mis à jour 2026-08-07) : cadre conceptuel qui distingue le RAG stateless (NotebookLM, ChatGPT file uploads) du wiki persistant (ce vault), avec une note sur la superposition des deux couches — le vault utilise désormais ChromaDB + embeddings en couche de retrieval, sans remplacer la structure wiki.

Ces deux pages confirment que la logique RAG utilisateur est documentée en interne comme un **objet distinct** des moteurs génératifs standards — ce que les grandes études sectorielles n'ont pas encore formalisé.

Observation anonymisée de pratiques terrain : dans les contextes de conseil et de veille stratégique observés, les utilisateurs professionnels de NotebookLM uploadent en priorité des rapports sectoriels, des audits concurrentiels, des transcriptions de réunions et des documents réglementaires — pas des articles de blog optimisés pour le référencement. La citabilité dans ces cas dépend d'un accès ouvert aux documents sources et de leur lisibilité machine (pas de scan non OCRisé, pas de verrou PDF).

---

## Contre-analyse

### Deep Research comme brouilleur de frontière

Le lancement de Deep Research en novembre 2025 rend le modèle NotebookLM moins pur. Quand l'outil navigue sur le web de manière autonome, il applique une logique de retrieval algorithmique que l'utilisateur ne contrôle pas directement. Les contenus bien référencés sur les moteurs classiques bénéficient probablement d'un avantage indirect dans cette phase. Le modèle « utilisateur-curé » n'est plus absolument étanche.

### Biais de confirmation dans la curation utilisateur

Les utilisateurs uploadent ce qu'ils connaissent déjà et font confiance. NotebookLM ne crée pas de nouvelles découvertes de sources — il approfondit des sources que l'utilisateur a déjà identifiées. Pour les éditeurs inconnus des professionnels d'un secteur, NotebookLM n'offre pas de porte d'entrée algorithmique alternative. C'est l'inverse de la longue traîne : l'outil renforce la notoriété existante plutôt que de la redistribuer.

### L'entreprise change l'équation individuelle

NotebookLM Enterprise (décembre 2024) connecte l'outil aux drives partagés des organisations. Les notebooks ne sont plus le choix d'un seul utilisateur : les contenus uploadés reflètent des décisions de procurement IT ou de knowledge management. Pour un éditeur B2B, être « approuvé » par le système de gestion documentaire d'une grande organisation signifie potentiellement être présent dans des milliers de notebooks simultanément — sans qu'aucun individu ne l'ait activement choisi.

### L'absence de données est une limite méthodologique, pas un angle borgne

Aucune étude ne peut mesurer ce qui se passe dans des notebooks privés. Mais cette limite est aussi une information : tout chiffre sur « les citations NotebookLM » émanant d'outils tiers devra être traité avec scepticisme extrême. Les données déclaratives (sondages utilisateurs) restent la seule voie d'accès, avec tous les biais associés au déclaratif.

---

## FAQ

**NotebookLM cite-t-il des sources extérieures à ce que j'uploade ?**
En mode standard, non — il répond uniquement à partir des documents que vous avez fournis. En mode Deep Research (disponible depuis novembre 2025), oui — il peut naviguer sur le web pour compléter les lacunes de votre corpus. Chaque réponse indique clairement la source (votre document ou une source web externe).

**Peut-on mesurer ses citations dans NotebookLM depuis l'extérieur ?**
Non. Il n'existe ni API publique, ni signal de referral, ni donnée accessible. Le trafic éventuel issu d'un clic depuis NotebookLM apparaît dans Google Analytics 4 comme trafic direct. C'est structurellement différent de Perplexity ou ChatGPT Search, dont les citations génèrent des referrals mesurables.

**Quelle différence entre NotebookLM et Perplexity pour un éditeur ?**
Perplexity choisit vos sources de manière algorithmique — vous pouvez optimiser pour entrer dans ce processus de sélection (GEO, qualité des contenus, autorité de domaine). NotebookLM laisse l'utilisateur décider. L'optimisation se déplace en amont : il faut devenir une référence que les professionnels de votre secteur vont d'eux-mêmes inclure dans leurs notebooks.

**Le renommage en Gemini Notebook change-t-il quelque chose ?**
Sur la logique de citation, non — l'architecture RAG utilisateur reste la même. Sur la distribution, potentiellement oui : l'intégration à l'écosystème Gemini peut augmenter le nombre d'utilisateurs via les abonnements Google One AI Premium, sans modifier la mécanique de curation individuelle.

**Comment optimiser sa présence dans NotebookLM ?**
L'optimisation porte sur trois points : (1) accessibilité des documents — PDF non verrouillé, HTML propre, transcript disponible pour les vidéos ; (2) citabilité dans les bases de données sectorielles, les rapports institutionnels et les revues professionnelles — ce sont ces sources que les professionnels uploadent en priorité ; (3) notoriété préalable dans la communauté cible — un utilisateur uploade ce qu'il connaît. C'est moins une question de référencement naturel que de relations dans l'écosystème professionnel.

---

## [À SOURCER]

Les chiffres suivants circulent dans les sources secondaires et les agrégateurs (gitnux.org, seosandwitch.com, zipdo.co, worldmetrics.org) mais n'ont pas été vérifiés sur une source primaire par fetch :

- « 10 millions de MAU en avril 2024 » : aucune annonce officielle Google retrouvée pour cette date ; chiffre présent dans des articles de synthèse sans lien vers la source primaire.
- « 67 % des utilisateurs lancent un Audio Overview chaque jour » et « 82 % chaque semaine » : provenance : gitnux.org — site agrégateur, aucune méthodologie.
- « 2 millions d'utilisateurs utilisent Audio Overview » : chiffre relayé mais source primaire non identifiée.
- « CSAT 4,6/5 sur 500 000 avis » : origine non tracée ; aucun programme public de collecte d'avis à cette échelle n'est documenté chez Google pour NotebookLM.
- « Croissance 120 % des MAU trimestriel au T4 2024 » : chiffre de synthèse agrégateur, pas de source primaire Google.
- Usage professionnel détaillé (types de documents uploadés, répartition B2B vs éducation) : aucune étude indépendante identifiée à ce jour.

---

## Sources

1. **9to5Google — Google renames NotebookLM to Gemini Notebook**, 9to5Google / Chance Miller, 16 juillet 2026 — https://9to5google.com/2026/07/16/notebooklm-gemini-notebook/ — consulté le 2026-09-06
2. **Google drops 'experimental' status for NotebookLM**, 9to5Google, 17 octobre 2024 — https://9to5google.com/2024/10/17/google-notebooklm-experimental-label/ — consulté le 2026-09-06
3. **NotebookLM is now available to all education users**, Google Workspace Updates Blog, août 2025 — https://workspaceupdates.googleblog.com/2025/08/notebooklm-is-now-available-to-all.html — consulté le 2026-09-06
4. **Use NotebookLM to generate Audio Overviews in more than 50 languages**, Google Workspace Updates Blog, 29 avril 2025 — https://workspaceupdates.googleblog.com/2025/04/language-expansion-audio-overviews-notebooklm.html — consulté le 2026-09-06
5. **Google debuts NotebookLM for enterprise**, TechCrunch, 13 décembre 2024 — https://techcrunch.com/2024/12/13/google-debuts-notebooklm-for-enterprise/ — consulté le 2026-09-06
6. **NotebookLM adds Deep Research and support for more source types**, blog.google / Google Labs, novembre 2025 — https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-deep-research-file-types/ — consulté le 2026-09-06
7. **NotebookLM**, Wikipedia, article en anglais — https://en.wikipedia.org/wiki/NotebookLM — consulté le 2026-09-06
8. **NotebookLM Limits Explained (2026)**, Elephas / Atlasworkspace, août 2026 — https://elephas.app/blog/notebooklm-source-limits / https://www.atlasworkspace.ai/blog/notebooklm-limitations — consulté le 2026-09-06 (données techniques de produit, non déclaration de performance)

**Données de première main vault** :
- [[entities/notebooklm]] — créé 2026-04-11, stub de contraste RAG stateless vs wiki persistant
- [[concepts/persistent-wiki-vs-rag]] — mis à jour 2026-08-07, cadre conceptuel sur la distinction RAG/wiki et ses implications GEO

---

*SyntheticBrain pour le wiki SEO/IA/GEO de Timothée Boussardon — 2026-09-06*
