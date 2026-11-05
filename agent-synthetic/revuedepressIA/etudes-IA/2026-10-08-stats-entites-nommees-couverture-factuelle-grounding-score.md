---
type: query
skill: seo-page-statistiques
title: "Densité d'entités nommées et couverture factuelle dans les pages citées : vers un Grounding Score mesurable ? (2025-2026)"
aliases: [entites-nommees-grounding-score, factual-density-citations-ia, grounding-score-mesurable]
tags: [seo-ia, geo, grounding-score, entites, couverture-factuelle, citations-ia, airops, surfer-seo, aggarwal]
created: 2026-10-08
updated: 2026-10-08
sources: 7
confidence: medium
status: draft
---

# Densité d'entités nommées et couverture factuelle dans les pages citées : vers un Grounding Score mesurable ? (2025-2026)

Les pages citées par les moteurs génératifs couvrent en médiane **62 % plus de faits** que les pages non citées sur le même sujet — et un alignement sémantique titre-requête supérieur à 50 % double le taux de citation, de 9,3 % à 20,1 %. Mais une expérience contrôlée menée en 2026 sur Perplexity obtient 0 % de citation malgré une densité d'entités variant de 1 à 2,3×, quand l'autorité du domaine passe sous un seuil critique. Quatre objets de mesure distincts sont systématiquement confondus sous l'étiquette "optimisation factuelle". Les démêler redéfinit ce que "Grounding Score mesurable" peut vouloir dire en pratique.

---

## Les chiffres clés (vérifiés à la source)

### Couverture factuelle et taux de citation

| Groupe de pages | Couverture factuelle moyenne | Source |
|---|---|---|
| Sources primaires (citées à chaque fois) | 42 % | Surfer SEO, 1 591 mots-clés |
| Pages occasionnellement citées | 34 % | Surfer SEO |
| Jamais citées | 23 % | Surfer SEO |

Surfer SEO a analysé 57 253 URL et 1,85 million d'apparitions de faits vérifiables sur 1 591 mots-clés, comparant les pages présentes dans les résultats AI Overviews de Google à celles absentes. La couverture factuelle correspond au pourcentage des faits-clés identifiés sur un sujet qu'une page donnée contient effectivement.

- Moyenne des pages citées : 31 % vs 24 % pour les non-citées (+29 % en relatif).
- Médiane : les pages citées couvrent **62 % plus de faits** que les non-citées.
- L'écart entre médiane et moyenne signale une distribution asymétrique : les "sources primaires" tirent la médiane vers le haut.

### Alignement lexical titre-requête et taux de citation

AirOps a analysé 548 534 pages récupérées par ChatGPT sur 16 851 requêtes uniques. Le taux de citation selon le chevauchement titre-requête :

| Chevauchement titre-requête | Taux de citation |
|---|---|
| < 10 % | 9,3 % |
| ≥ 50 % | 20,1 % |

Soit un rapport de 2,2× entre les deux extrêmes — sur un corpus où 85 % des pages récupérées ne sont finalement pas citées.

### Alignement sémantique des titres et taux de citation

AirOps mesure aussi la similarité cosinus entre le vecteur de la requête et le meilleur titre H1-H4 de la page (via embeddings BAAI/bge-base-en-v1.5) :

| Similarité cosinus | Taux de citation |
|---|---|
| < 0,60 | 30,2 % |
| 0,60–0,79 | 28,6 %–31,0 % |
| ≥ 0,90 | 41,0 % |

Parmi les pages positionnées en rang 1 avec une similarité ≥ 0,9, le taux atteint 79,6 %. Parmi les pages rang 11+ avec la même similarité, il chute à 21,5 % : le rang de récupération prime sur le signal sémantique.

### Stratégies factuelles et gain de visibilité (GEO paper, KDD 2024)

Aggarwal et al. ont testé neuf stratégies d'optimisation sur 10 000 requêtes et 25 sources (benchmark GEO-bench), mesurant la visibilité dans les réponses génératives via un score pondéré par position :

| Stratégie | Gain de visibilité |
|---|---|
| Ajout de citations verbatim | +42,6 % |
| Ajout de statistiques | +32,8 % |
| Sources explicitement citées | +27,7 % |
| Optimisation de la fluidité | +28,7 % |
| Ton autoritaire | +11,8 % |
| Remplissage de mots-clés | −8,7 % |

La meilleure stratégie (citations verbatim) dépasse le gain annoncé dans l'abstract (+41 %) du fait d'un arrondi de calcul. Ces résultats sont obtenus sur un corpus synthétique (GEO-bench) avec un pipeline RAG à deux étapes.

### Contenu structurel vs corps de texte seul (SAGEO Arena, KDD 2026)

SAGEO Arena a évalué 171 003 documents sur 2 700 requêtes dans un environnement simulant le pipeline complet (récupération → réordonnancement → génération) :

- Information structurelle (titres, sections, schémas) : **+22 % de Hit Rate** à l'étape de récupération.
- Optimisation du corps de texte seul : **−9 % de présence dans le top 20** en récupération en moyenne.

Le corps de texte — là où s'ajoutent les faits, statistiques et entités nommées — dégrade la récupération quand il est modifié sans toucher à la structure. Cette dissociation est le fait le moins souvent cité dans les guides pratiques.

### Densité d'entités et taux de citation : l'expérience contrôlée

The GEO Lab a conduit en avril 2026 la seule expérience publiée qui isole la densité d'entités comme variable causale. Protocole :

- 10 pages du même domaine, densité filtrée de 12,9 à 29,5 entités uniques pour 1 000 mots (rapport 2,3×).
- Comptage via spaCy `en_core_web_lg`, entités CARDINAL et ORDINAL filtrées pour éviter le biais des nombres nus.
- 52 requêtes sur Perplexity sonar-pro : 30 requêtes propriétaires, 22 requêtes concurrentielles préenregistrées.

Résultats :
- Requêtes propriétaires : taux de citation 20 % (6/30), toutes en position 1. Baseline du domaine : 7,5 % en mars 2026.
- Requêtes concurrentielles : **0 % de citation** (0/22) quelle que soit la densité d'entités.
- Domaines cités à la place : Search Engine Land (5), Semrush (3), Ahrefs (2), ainsi que des institutions (MIT, Harvard, UC Berkeley).
- Corrélation Pearson/Spearman entre densité et citation : **non définie** (variance de la variable dépendante = 0 sur les 22 requêtes concurrentielles).

Conclusion des auteurs : l'autorité du domaine agit comme une porte binaire. En dessous du seuil (estimé à environ 30 % de taux de citation sur les requêtes générales concurrentielles), les signaux page-level ne parviennent pas à la décision de citation.

---

## Pourquoi ces chiffres ne mesurent pas la même chose

Quatre objets distincts sont confondus dans la quasi-totalité des guides qui parlent d'"optimisation factuelle" ou d'"entités" :

**Objet 1 — Chevauchement lexical titre-requête** (AirOps, 20,1 % vs 9,3 %)
Signal de surface, calculable sans embeddings. Mesure si les mots du titre recouvrent les mots de la requête. S'améliore par retitrage.

**Objet 2 — Proximité sémantique titre-requête** (AirOps, cosinus ≥ 0,9 → 41 %)
Signal vectoriel, requiert un modèle d'embeddings. Mesure la similarité cosinus entre vecteurs. S'améliore par enrichissement sémantique des titres, pas par recopie des mots-clés. Les deux objets 1 et 2 sont indépendants : un titre peut chevaucher lexicalement et diverger sémantiquement, ou l'inverse.

**Objet 3 — Couverture factuelle** (Surfer SEO, 62 % de faits en plus, 31 % vs 24 %)
Signal thématique, requiert un référentiel de faits-clés par sujet. Mesure le pourcentage des faits attendus que la page contient. Corrélé à la citation, mais confondant avec l'autorité du domaine (les sources primaires ont à la fois plus de faits et plus d'autorité).

**Objet 4 — Densité d'entités nommées** (GEO Lab, 12,9 à 29,5 entités/1 000 mots → 0 % sur les requêtes concurrentielles)
Signal de richesse informationnelle brute. Mesure le nombre d'entités reconnues par un modèle de reconnaissance d'entités nommées. Résultat nul quand l'autorité du domaine est insuffisante.

Ces quatre objets s'inscrivent aussi à des étapes différentes du pipeline génératif :

| Objet | Étape où il opère | Effet démontré |
|---|---|---|
| Chevauchement lexical (1) | Récupération initiale | +2,2× de citation (corrélationnel) |
| Proximité sémantique (2) | Récupération + réordonnancement | +41 % citation (rang 1 + similarité ≥ 0,9 : 79,6 %) |
| Couverture factuelle (3) | Génération | +29 à +42,6 % de visibilité (GEO paper) |
| Densité d'entités (4) | Génération | Nul sous seuil d'autorité (GEO Lab) |

Le paradoxe documenté par SAGEO Arena : enrichir le corps de texte (objets 3 et 4) nuit à la récupération (−9 % de Hit Rate), même si cela aide la génération. Autrement dit, ajouter des faits à une page peut réduire les chances qu'elle entre dans le pool de récupération, tout en augmentant les chances qu'elle soit citée si elle y entre. Ce ciseau n'apparaît dans aucun guide pratique.

---

## Données de première main (données du vault)

Le vault intègre depuis avril 2026 une formalisation propriétaire du Grounding Score — concept qui tente précisément de réunir ces quatre objets en une mesure unique. Données anonymisées par défaut (aucun site client nommé).

La doctrine du cabinet mesure le Grounding Score comme la similarité cosinus entre le vecteur d'intention d'une requête et le vecteur d'une page, via Gemini Embedding. Elle distingue deux composantes :

1. **Proximité** : le vecteur de la page doit être proche du vecteur de l'intention.
2. **Divergence informationnelle** : la page doit apporter de l'information que le modèle ne connaît pas encore (concept de "surprise informationnelle", lié à l'architecture Titans de Google DeepMind).

L'hypothèse centrale (H-003 dans le registre du vault, statut : ouvert) est qu'un Grounding Score supérieur à 0,75 en moyenne sur un cluster et supérieur à 0,85 pour les pages piliers constitue le seuil de citabilité. Ces seuils sont des objectifs de doctrine, pas des benchmarks validés — aucune fiche preuve ne les a encore confrontés à des données réelles de citation.

Le framework distingue quatre catégories d'entités dans une page :
- Entités techniques (termes de domaine, algorithmes, outils, protocoles)
- Entités de preuve (chiffres, dates, études citées, résultats mesurés)
- Entités multimodales (données visuelles, transcripts, captures)
- Entités de divergence (contre-arguments, paradoxes, données contraires)

Cette taxonomie formalise ce que les études externes mesurent partiellement : les études de couverture factuelle (Surfer, AirOps) ne comptent que les entités de preuve. La densité d'entités nommées (GEO Lab) capture un mélange non contrôlé des quatre catégories.

Un test terrain reste à conduire : publier une page structurée selon cette taxonomy (entités de preuve + divergence explicites) et mesurer son comportement dans les moteurs génératifs face à une page équivalente en autorité mais pauvre en entités de divergence.

---

## Contre-analyse

**1. La corrélation Surfer SEO ne prouve pas de causalité.** Les pages avec une forte couverture factuelle sont aussi les pages des sites les plus autoritaires sur leurs sujets. Le facteur confondant "autorité du domaine × couverture factuelle" n'est pas contrôlé dans l'étude. Surfer commercialise Coverage Booster, un outil qui automatise l'ajout de faits — intérêt commercial évident. La corrélation est réelle ; la direction causale est spéculative.

**2. Le GEO-bench d'Aggarwal mesure une visibilité synthétique, pas des citations réelles.** Le benchmark utilise un pipeline RAG à deux étapes (récupération Google + génération LLM) et mesure la part de mots attribuables à chaque source dans la réponse finale. Ce n'est pas la même chose que d'être cité explicitement par ChatGPT, Perplexity ou Google AI Overviews. Les gains (+42 %, +32 %) sont réels sur ce benchmark ; leur transfert aux plateformes du marché est une hypothèse, pas une mesure.

**3. L'expérience GEO Lab est trop petite pour généraliser.** 10 pages, 1 domaine, 1 plateforme (Perplexity sonar-pro), résultat nul sur les requêtes concurrentielles. ChatGPT via l'endpoint DataForSEO a retourné 0 citation et a été abandonné. Le résultat "l'autorité est une porte binaire" est plausible, mais une expérience à 10 pages ne peut pas fixer le seuil. Le seuil estimé (30 % de taux de citation général) est une heuristique de travail, pas un résultat statistique.

**4. Le Grounding Score doctrine n'est pas validé empiriquement.** Les seuils 0,75 et 0,85 sont des objectifs de méthode. L'hypothèse H-003 est toujours ouverte dans le vault. Une page peut atteindre ces seuils en similarité cosinus et rester non citée si son autorité est insuffisante, ou si le pipeline de récupération ne l'atteint pas.

**5. Le paradoxe SAGEO Arena mérite une interprétation prudente.** L'expérience mesure un pipeline simulé, pas un moteur réel. Les moteurs du marché (ChatGPT, Perplexity, Google AI Mode) ont chacun une architecture de récupération propriétaire. L'effet "−9 % de récupération quand on optimise le corps de texte" peut ne pas s'observer de la même façon sur tous les moteurs.

---

## FAQ

**Le Grounding Score est-il une métrique officielle de Google ?**
Non. C'est un terme de doctrine SEO. Google n'a jamais publié de définition ni de calcul sous ce nom. La définition la plus opérationnelle connue est la similarité cosinus entre le vecteur d'intention d'une requête et le vecteur d'une page.

**Combien de faits par page pour être cité ?**
Les données Surfer SEO indiquent que les sources primaires (citées systématiquement) couvrent 42 % des faits-clés d'un sujet contre 23 % pour les pages jamais citées. Ce pourcentage dépend du référentiel de faits défini par Surfer pour chaque sujet — il n'est pas transposable tel quel à une mesure maison en "nombre de faits pour 1 000 mots".

**Entités nommées ou couverture factuelle : qu'est-ce qui compte davantage ?**
Ce sont deux proxies différents d'une même propriété. La couverture factuelle (Surfer) mesure la complétude thématique ; la densité d'entités nommées (GEO Lab) mesure la richesse informationnelle brute. Les deux sont corrélés à la citation, mais les études les testent dans des conditions différentes. L'expérience contrôlée disponible (GEO Lab) ne trouve pas d'effet de la densité d'entités seule en dessous du seuil d'autorité du domaine.

**Doit-on optimiser la structure ou le corps de texte ?**
SAGEO Arena suggère que les deux produisent des effets opposés à l'étape de récupération : la structure aide (+22 % de Hit Rate), le corps de texte seul nuit (−9 %). À l'étape de génération, la situation s'inverse — les faits et citations dans le corps de texte augmentent la visibilité (GEO paper). La conclusion pratique : enrichir la structure en premier, puis enrichir le corps sans réduire la pertinence des titres.

**L'ajout de citations verbatim (+42,6 %) est-il mesurable sur les plateformes actuelles ?**
Ce chiffre vient du GEO-bench 2024, un environnement synthétique. À ce jour, aucune étude de grande échelle sur ChatGPT, Perplexity ou Google AI Mode n'a isolé l'effet des citations verbatim seules avec un protocole contrôlé comparable.

---

## [À SOURCER]

Les chiffres suivants n'ont pas été vérifiés par fetch de la source primaire et ne sont pas repris comme acquis dans cette page :

- **Wellows (2025 Comprehensive Study)** : "Pages avec 15+ entités reconnues = 4,8× de probabilité de sélection dans les AI Overviews." Chiffre calculable depuis le tableau de l'article (29,8 % vs 6,2 %), mais la source primaire n'est pas identifiable. Aucun protocole ni taille d'échantillon divulgués.
- **Citate.ai / Kevin Indig** : "Les contenus cités par ChatGPT ont une densité d'entités d'environ 20,6 % contre 5-8 % dans le texte anglais standard." Repris en seconde main depuis l'analyse de 1,2 million de citations ChatGPT. La définition de "densité d'entités" et la méthode de comptage ne sont pas divulguées.
- **Données France** : aucune étude publiée n'isole les effets de la densité d'entités ou de la couverture factuelle dans les moteurs IA sur des requêtes en français.
- **Expérience contrôlée à grande échelle** : aucune étude publiée ne teste causalement la densité d'entités nommées contre le taux de citation en contrôlant simultanément l'autorité du domaine, le rang de récupération et la plateforme.

---

## Sources

1. **The Fan-Out Effect** — AirOps × Kevin Indig. Étude de 16 851 requêtes et 353 799 pages sur ChatGPT. Sections : chevauchement titre-requête (20,1 % vs 9,3 %) et similarité cosinus (41,0 % pour ≥ 0,9). Consulté le 2026-10-08. https://www.airops.com/blog/query-fanout-pipeline et https://www.airops.com/report/the-fan-out-effect-what-happens-between-a-query-and-a-citation

2. **Do Pages With More Key Facts Get Cited in AI Overviews?** — Surfer SEO, Kris Tavja. 57 253 URL, 1 591 mots-clés, 1,85 million d'apparitions de faits. Mise à jour : 17 septembre 2026. Consulté le 2026-10-08. https://surferseo.com/blog/do-pages-with-more-key-facts-get-cited-in-ai-overviews

3. **GEO: Generative Engine Optimization** — Aggarwal et al. KDD 2024, arXiv:2311.09735. GEO-bench : 10 000 requêtes, 25 sources, 9 stratégies testées. Consulté le 2026-10-08. https://arxiv.org/abs/2311.09735

4. **SAGEO Arena: A Realistic Environment for Evaluating Search-Augmented Generative Engine Optimization** — Kim et al. KDD 2026, arXiv:2602.12187. 171 003 documents, 2 700 requêtes, pipeline complet simulé. Consulté le 2026-10-08. https://arxiv.org/abs/2602.12187

5. **Entity Density vs Citation Rate: A Controlled Experiment** — The GEO Lab, avril 2026. 10 pages, 52 requêtes, Perplexity sonar-pro. Résultat nul sur requêtes concurrentielles. Consulté le 2026-10-08. https://thegeolab.net/entity-density-citation-rate-experiment/

6. **Grounding Score — wiki interne** — Doctrine propriétaire, vault seo-kb. Données de première main anonymisées. Framework 4 catégories d'entités, seuils GS > 0,75 / > 0,85, hypothèse H-003 (statut : ouvert). Créé : 2026-04-11, mis à jour : 2026-07-13. [wiki/concepts/grounding-score]

7. **Le pattern wiki persistant optimise-t-il structurellement le Grounding Score ?** — Query interne, vault seo-kb. Analyse des mécanismes structurels liant wiki persistant et Grounding Score. Créé : 2026-04-12. [wiki/queries/2026-04-12-wiki-pattern-vs-grounding-score]
