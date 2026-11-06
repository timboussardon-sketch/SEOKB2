---
type: concept
title: AEO (Answer Engine Optimization)
aliases: [aeo, answer-engine-optimization]
tags: [geo, aeo, seo-ia, ranking, moteurs-reponse]
created: 2026-04-12
updated: 2026-08-28
sources: 10
confidence: high
status: stable
---

# AEO (Answer Engine Optimization)

Optimisation pour les **moteurs de réponse** (SGE, Perplexity, ChatGPT Search) qui génèrent des réponses directes plutôt que des listes de liens.

## Ce que cette KB sait déjà

- Listé en §4.2 d'`AGENTS.md` comme concept attendu
- Le skill cluster-aeo construit des architectures optimisées pour l'AEO avec le framework Know-Simple / Know / Do (remplace TOFU/MOFU/BOFU) [[sources/2026-04-12-tim-skills-seo-proprietary]]
- Tim positionne 2026 à **70% SEO / 30% GEO** — l'AEO est la composante "être cité dans les réponses IA" [[sources/2026-03-31-tim-profil-et-regles]]
- Connexion directe avec [[concepts/surprise-gap]] (être cité = apporter l'info manquante) et [[concepts/grounding-score]] (être retrouvé = proximité vectorielle)

## Relation AEO vs GEO

AEO = optimisation pour les moteurs qui **génèrent des réponses** (focus : être la source citée).
GEO = terme plus large couvrant toute l'optimisation pour les moteurs génératifs (focus : citations IA et clics qui en découlent, cf. [[concepts/tabou-visibilite]]).
Les deux se recouvrent largement. Tim utilise les deux termes.

## Preuve quantitative — un faisceau, pas une étude

Le « 4x » Semrush ([[sources/2026-04-13-semrush-llm-conversion-study]]) a longtemps porté seul cette page. Il ne le porte plus seul, et il ne le portait pas bien : l'étude est propriétaire, son lien d'origine est indisponible, et elle date de juillet 2025.

[[sources/2026-06-09-algorithme-ia-detruire-business-seo]] agrège quatre autres relevés qui vont dans le même sens sur le rapport de conversion entre trafic IA et organique : Seer Interactive à 15,9 % contre 1,76 %, un panel B2B Tech à 14,2 % contre 2,8 %, Ahrefs à 23x, Microsoft Clarity à 3x.

Le faisceau converge, l'ordre de grandeur ne converge pas. Ces relevés ont des périmètres, des définitions de conversion et des méthodologies hétérogènes, et la source qui les rassemble le dit elle-même sans les harmoniser. Ce qui tient : le trafic issu des moteurs de réponse convertit nettement mieux que l'organique classique, sur des volumes nettement plus faibles. Ce qui ne tient pas : un multiplicateur unique, quel qu'il soit. On ne publie pas « 4x » ni « 23x » comme un fait ; on publie l'écart et sa dispersion. Confidence medium.

## Canaux tiers — l'AEO ne se joue pas que sur sa page

La page décrivait l'AEO comme un travail sur son propre contenu. La pratique de la KB a bougé depuis avril : la citation passe aussi par les plateformes où l'IA va lire. Le signal le plus fort mesuré sur ce point est la mention YouTube, à une corrélation de 0,737 avec la présence en réponse IA sur 75 000 marques (Ahrefs, via [[sources/2026-06-09-algorithme-ia-detruire-business-seo]]).

C'est ce qui a produit les deux playbooks propriétaires, [[sources/2026-06-19-playbook-reddit-seo-geo]] et [[sources/2026-06-19-playbook-x-seo-geo]], et le [[concepts/parasite-seo|parasite SEO]] comme levier assumé. Une stratégie AEO qui ne travaille que le domaine propre laisse ce canal à ses concurrents.

## Ce que l'AEO n'est pas — une fin

Être cité n'est pas l'objectif, c'est un moyen. [[concepts/test-substitution-llm]] pose la question qui tranche : si l'IA peut répondre à la place de la page, la page ne rapporte rien même bien citée. [[concepts/mots-cles-actionnels]] en tire la conséquence opérationnelle — on cible les requêtes que l'IA ne peut pas absorber, celles où l'utilisateur doit agir, pas seulement savoir. Formulé par Tim en juin : « je ne travaille pas pour ChatGPT » ([[sources/2026-06-24-organikk-mots-cles-qui-ramenent-du-clic]]).

Cette section est la limite de l'AEO comme discipline, et elle est arrivée après la rédaction initiale de la page.

## Pages liées

[[sources/2026-04-24-reflexion-organikk-4-piliers]] (pilier 4 explicite) · [[sources/2026-04-24-cluster-business-organikk-4-piliers]] (cluster opérationnel) · [[sources/2026-04-17-organikk-process-seo-b2b-2026]] (process B2B + Know-Simple/Know/Do) · [[sources/2026-04-15-opendecoder-seo-scoring-system]] (S_AEO comme 4e score) · [[sources/2026-04-13-semrush-llm-conversion-study]] · [[sources/2026-04-11-algorithme-linkedin-2e-source-ia]] (étude LinkedIn 2e source IA : "être cité vaut plus que ranker") · [[sources/2026-04-15-algorithme-listicles-chatgpt-30pct-baisse]] (Addy Osmani formalise l'AEO côté Google Cloud) · [[sources/2026-04-22-algorithme-core-update-fermes-ia]] (divergence ChatGPT/Perplexity/AI Mode = AEO différencié par moteur) · [[concepts/grounding-score]] · [[concepts/surprise-gap]] · [[concepts/data-proprietaire]] · [[concepts/agentic-search]] · [[concepts/mots-cles-actionnels]] · [[concepts/test-substitution-llm]] · [[concepts/tabou-visibilite]] · [[concepts/parasite-seo]] · [[sources/2026-06-09-algorithme-ia-detruire-business-seo]] · [[sources/2026-06-19-playbook-reddit-seo-geo]] · [[sources/2026-06-24-organikk-mots-cles-qui-ramenent-du-clic]] · [[revue-hebdo/resurgence-2026-08-26]] · [[sources/2026-04-12-tim-skills-seo-proprietary]] · [[entities/chatgpt-search]] · [[entities/perplexity]] · [[entities/google-ai-mode]] · [[entities/linkedin]]
