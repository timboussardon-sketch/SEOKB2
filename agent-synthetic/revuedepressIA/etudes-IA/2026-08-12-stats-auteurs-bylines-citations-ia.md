---
type: query
skill: seo-page-statistiques
title: "Auteurs et bylines dans les citations IA (2025-2026)"
aliases: [stats-auteurs-bylines-ia, auteur-byline-citation-ia-2026]
tags: [citations-ia, auteur, byline, person-schema, e-e-a-t, geo, aeo]
created: 2026-08-12
updated: 2026-08-12
sources: 6
confidence: medium
status: draft
---

# Auteurs et bylines dans les citations IA (2025-2026)

Un contenu avec un auteur identifiable reçoit 8,5 citations en moyenne contre 5,5 pour un contenu de marque sans attribution nominative — soit un écart de 55 %. Pourtant, ajouter un byline n'a produit aucun effet mesurable sur Google AI Overviews dans la seule expérience contrôlée publiée à ce jour. L'auteur compte, mais pas uniformément selon les moteurs.

---

## Les chiffres clés (vérifiés à la source)

**Attribution nominative vs contenu de marque**

Parmi 1 310 455 citations LinkedIn analysées entre janvier et juin 2026 sur six moteurs (ChatGPT, Google AI Overviews, Google AI Mode, Perplexity, Copilot, Gemini) :

- Contenus attribués à un individu nommé : **87,8 % des URLs citées**, **91,7 % du total des citations** (soit 8,5 citations par URL)
- Contenus de marque ou sans attribution nominative : **12,2 % des URLs**, **8,3 % des citations** (5,5 par URL)

Source : OtterlyAI, *LinkedIn AI Search Citations Study*, 161 440 URLs analysées, janvier-juin 2026.

---

**Person schema : sur-représentation ×9,4 sur les pages citées**

Sur 1 465 pages citées par au moins un moteur IA (28 033 apparitions relevées sur ChatGPT, Perplexity, Gemini) :

- Person schema présent sur **18,9 % des pages citées** vs **2,0 % du web moyen** (référence : Web Almanac 2024)
- Multiplicateur : **×9,4**
- Schema markup toutes formes confondues : **68 % des pages citées** vs **38,5 % du web moyen** (×1,77)

Mais : entre le top 10 % des pages les plus souvent citées et les 50 % les moins citées, l'écart de Person schema est de **−1,6 %** — quasi nul. La sur-représentation reflète le profil du contenu que les moteurs citent (institutionnel, éditorial, professionnel), pas un effet causal du balisage seul.

Source : Trakkr Research, *The Anatomy of an AI Citation* (étude 008), mise à jour avril 2026.

---

**Expérience contrôlée Seer Interactive : Bing double, Google AI Overviews ne bouge pas**

Sur 123 pages traitées avec un byline (groupe test) versus pages non traitées (groupe contrôle), sur le site Seer Insights :

- Bing Webmaster Tools citations : **+109 %** (groupe test) vs **+34 %** (contrôle)
- Taux de crawl Googlebot : **+11,7 points de pourcentage** dans les deux semaines suivant l'ajout
- Google AI Overviews : **aucune différence statistiquement significative** (effet réel mesuré : **−1,3 %**, non distinguable du bruit)
- Pages avec activité de citation existante ayant progressé : **44 % (traité) vs 27 % (contrôle)**

Résultat contre-intuitif sur la notoriété : les pages attribuées à des auteurs peu connus ont progressé de **+113 %** sur Bing, contre seulement **+21 %** pour les pages du fondateur (auteur le plus reconnu du site). L'effet byline est plus fort là où la réputation de l'auteur ne préexiste pas.

Source : Seer Interactive, *Do Author Bylines Influence AI Visibility? Testing EEAT Elements in GEO*, 2026.

---

**Biais de genre : 76,4 % des citations vers des auteurs masculins**

Parmi les citations LinkedIn attribuées à un individu identifiable :

- Auteurs masculins : **76,4 %** des citations
- Autrices : **23,5 %** des citations
- Écart stable sur les six plateformes mesurées (fourchette : 23-24 % pour les femmes quel que soit le moteur)

Méthode de détection : estimation par prénom, pronom et signaux de profil — données directionnelles, non autodéclarées.

Source : OtterlyAI, *LinkedIn AI Search Citations Study*, janvier-juin 2026.

---

**Poids des signaux auteur dans la synthèse des 54 études (Zyppy, mai 2026)**

Cyrus Shepard a synthétisé 54 expériences et études pour établir 23 facteurs de citation IA, notés sur la répétabilité, la force de preuve et le soutien documentaire officiel. Dans ce classement :

- « Brand/Entity Trust » (qui englobe la notoriété de l'auteur et son inscription dans les graphes de connaissance) : **rang 16, score 6,8/10**
- « Structured Data » (dont le balisage Person) : **rang 20, score 5,6/10**
- « Known Source » (présence dans les données d'entraînement) : **rang 21, score 5,4/10**
- Aucun facteur intitulé « byline » ou « auteur » n'apparaît dans les 23 en tant qu'item isolé

Les trois premiers facteurs sont l'accessibilité URL (9,5), le rang de recherche organique (9,4) et le rang par requêtes dérivées (9,3).

Source : Zyppy Signal / Cyrus Shepard, *AI Citation Ranking Factors*, mai 2026, synthèse de 54 études couvrant ChatGPT, Gemini, Perplexity.

---

## Pourquoi ces chiffres divergent — transformation originale

Trois études mesurent trois objets distincts. Les réconcilier évite une conclusion erronée.

**Objet 1 — Présence observationnelle (Trakkr)**
Les pages citées contiennent Person schema 9,4 fois plus souvent que le web. Ce chiffre dit : « les types de contenus que les moteurs citent portent souvent un auteur balisé. » Il ne dit pas : « ajouter Person schema fera citer votre page. » Les pages institutionnelles et éditoriales, naturellement plus citées, ont aussi structurellement plus d'auteurs identifiés.

**Objet 2 — Effet causal marginal (Seer Interactive)**
L'expérience contrôlée teste l'ajout d'un byline sur des pages existantes. Elle mesure le delta attribuable. Résultat : effet sur Bing (+109 %), effet nul sur Google AI Overviews. C'est l'objet le plus proche d'une preuve causale — et il est moteur-dépendant.

**Objet 3 — Attribution des citations dans un contexte spécifique (OtterlyAI)**
La plateforme LinkedIn est un espace intrinsèquement nominatif : le format impose un auteur. La sur-représentation des contenus nominatifs (87,8 % des URLs) reflète l'architecture de la plateforme autant que l'effet de l'attribution. Ce chiffre n'est pas transposable mécaniquement à un blog ou à un site institutionnel.

**L'inversion contre-intuitive**
Dans l'expérience Seer, l'auteur le moins connu (membre de l'équipe) gagne +113 % sur Bing. L'auteur le plus connu (le fondateur) ne gagne que +21 %. Hypothèse : les moteurs qui utilisent un signal de type « entité nouvelle + byline précis » accordent plus de poids à la vérifiabilité de l'individu qu'à sa notoriété préexistante. La citabilité n'est pas une extension de la célébrité de l'auteur.

---

## Nos propres chiffres (données de première main)

Aucune propriété du portefeuille n'a fait l'objet d'une mesure isolant le signal « ajout de byline ou de page auteur » avant/après sur les citations IA. Les fiches preuves en cours ([[preuves/2026-07-10-organikk-batch-juillet-data-proprietaire]], [[preuves/2026-07-17-organikk-directories-guide-google]]) testent d'autres variables (data propriétaire, directories structurés). Ce bloc est réservé honnêtement.

---

## Contre-analyse

**1. La corrélation Trakkr confond type de contenu et signal auteur**
Les pages institutionnelles (Mayo Clinic, Reuters, PubMed) portent naturellement un auteur identifié — et sont massivement citées pour leur autorité de domaine. Isoler l'effet Person schema de l'effet autorité de domaine ou de la longueur du contenu n'est pas possible avec cette méthodologie.

**2. L'expérience Seer est limitée à un seul site dans un secteur spécifique**
123 pages d'un blog de consultants SEO ne permettent pas de généraliser. Seer note elle-même que le sujet de la page, sa fraîcheur et la sélection des prompts sont des variables confondantes. L'effet Bing pourrait être une anomalie de panel.

**3. Zyppy classe le byline comme sous-composante, pas comme facteur**
Sur les 23 facteurs de citation IA évalués dans la plus large synthèse disponible, « auteur » n'apparaît pas comme un levier autonome. Il est absorbé dans « Brand/Entity Trust » (score 6,8) — le seizième facteur, loin derrière l'accessibilité technique et le rang organique.

**4. Le biais de genre n'est pas corrigé pour la notoriété**
Les 76,4 % / 23,5 % reflètent peut-être un écart de notoriété préexistant (les hommes publient et sont cités davantage sur LinkedIn) plutôt qu'un biais de traitement des moteurs. Une étude contrôlant pour le domaine d'autorité et le volume de publication n'existe pas encore.

**5. Google AI Overviews résiste au byline**
L'absence d'effet sur Google AI Overviews dans l'expérience contrôlée de Seer — le seul moteur pour lequel une étude causale est disponible à ce jour — est le signal le plus robuste de cet inventaire. Il tempère toutes les corrélations observationnelles.

---

## FAQ

**Un byline aide-t-il à être cité par Google AI Overviews ?**
Aucune preuve causale à ce jour. L'unique expérience contrôlée publiée (Seer Interactive, 123 pages) mesure un effet de −1,3 %, statistiquement nul.

**Person schema Person vaut-il la peine d'être implémenté ?**
Person schema est 9,4× plus fréquent sur les pages citées (Trakkr), mais ce chiffre est observationnel. Bing semble plus réceptif au signal que Google AI Overviews. Comme il ne nuit pas et qu'il améliore la vérifiabilité de l'entité auteur, l'implémenter reste cohérent — sans en attendre un effet automatique sur les citations.

**Une page auteur dédiée change-t-elle quelque chose ?**
Elle consolide le graphe d'entité de l'auteur (profile URL, domaines de compétence, liens vers d'autres publications). L'effet est indirect : elle renforce le signal « Known Source » et « Brand/Entity Trust » du contenu qu'elle signe. Aucune mesure d'impact isolée n'est publiée pour les pages auteur seules.

**Les autrices sont-elles moins citées ?**
Oui, sur LinkedIn : 23,5 % des citations vers des auteurs identifiés vont à des femmes (OtterlyAI, jan.-juin 2026). L'écart est stable sur les six moteurs. La cause — biais de notoriété préexistant, biais de traitement IA, ou les deux — n'est pas élucidée.

---

## [À SOURCER]

- Poids exact « author credentials » 8 % (2024) → 16 % (2025) selon BrightEdge : non retrouvé dans le rapport BrightEdge vérifié par fetch. La source intermédiaire est rank-and-convert.ghost.io, pas BrightEdge directement. Chiffre non publié ici.
- Effet du byline sur ChatGPT Search et Perplexity en dehors du contexte LinkedIn : aucune étude contrôlée disponible.
- Données France : aucune mesure d'impact des bylines sur les sources françaises dans les moteurs IA.
- Impact de l'auteur sur Claude : aucune mesure spécifique disponible à la date de rédaction.
- La divergence Bing/Google dans l'expérience Seer demande réplication sur d'autres domaines avant généralisation.

---

## Sources

| Organisme | Étude | Date | URL | Consulté le |
|---|---|---|---|---|
| Trakkr Research | *The Anatomy of an AI Citation* (Study 008) — 1 465 pages citées, 950 domaines, 28 033 apparitions ChatGPT/Perplexity/Gemini | Avril 2026 | https://trakkr.ai/trakkr-research/anatomy-of-an-ai-citation | 2026-08-12 |
| Seer Interactive | *Do Author Bylines Influence AI Visibility?* — 123 pages traitées vs contrôle, Bing/Google AIO/ChatGPT | 2026 | https://www.seerinteractive.com/work/case-studies/author-bylines | 2026-08-12 |
| OtterlyAI | *LinkedIn AI Search Citations Study* — 1 310 455 citations, 161 440 URLs, 6 moteurs, jan.-juin 2026 | Juin 2026 | https://otterly.ai/blog/linkedin-ai-search-citations-study/ | 2026-08-12 |
| Zyppy / Cyrus Shepard | *AI Citation Ranking Factors* — 23 facteurs, synthèse de 54 études, ChatGPT/Gemini/Perplexity | Mai 2026 | https://signal.zyppy.com/ | 2026-08-12 |
| ZipTie.dev | Expérience credentials auteur — 15 articles, 4 semaines (n très limité) | 2025 | https://ziptie.dev/blog/how-original-research-wins-ai-citations/ | 2026-08-12 |
| Semrush (via sources secondaires) | 304 805 URLs — E-E-A-T signals +31 %, second prédicteur derrière answer-first +33 % | Janvier 2026 | https://www.semrush.com/blog/semrush-ai-overviews-study/ | 2026-08-12 |
