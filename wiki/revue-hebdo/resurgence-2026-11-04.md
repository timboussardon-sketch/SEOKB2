---
type: register
title: Résurgence 2026-11-04, agentic-search
tags: [resurgence, revue-hebdo, agentic-search, hypotheses]
created: 2026-11-04
updated: 2026-11-04
status: stable
---

# Résurgence : [[concepts/agentic-search]] (2026-11-04)

## Pourquoi celui-là

`updated: 2026-04-13`, 205 jours sans modification, `confidence: high`, 63 backrefs dans `concepts.json` (57 à la résurgence du 10-21). Jamais passé en résurgence. Hors fenêtre de 8 semaines : persistent-wiki-vs-rag (08-05), programmatique-pseo (08-12), aeo (08-26), ingenierie-semantique-inversee (09-09), product-led-seo (09-23), e-e-a-t (10-07), tabou-visibilite (10-14), fully-meets (10-21).

[[concepts/know-simple-know-do]] a plus de backrefs (68) mais fonde son rejet du TOFU/MOFU/BOFU sur ce concept (« obsolètes à l'ère de l'Agentic Search », ligne 15). Le re-confronter couvre les deux.

Pas de résurgence le 2026-10-28 : [[ops/sante-automatisations]] la classe « en retard » (13 j au relevé du 11-03). Cause non investiguée ici.

## État vs aujourd'hui

**La définition repose sur des exemples sans source primaire.** La fiche ouvre sur « MLE-STAR, Claude Computer Use ». MLE-STAR n'existe dans le vault que dans la note de Tim ([[sources/2026-04-11-seo-ia-tim]] et `raw/notes/`). « Claude Computer Use » n'apparaît dans aucune fiche `wiki/sources/` ni dans `raw/papers/`. Le mécanisme (« pénétrer la Neural Memory ou la Persistent Memory ») est le transfert Titans de Tim, donc [[hypotheses]] H-001, statut `heuristique` : « pari architectural, non observable de l'extérieur ». La fiche le range sous « Ce que cette KB sait déjà » sans renvoyer à H-001.

**Les trois papiers ne portent pas sur des agents, et la fiche le dit elle-même** (section Limites). Mais la ligne 33 écrit que searchllm « confirme que les agents de recherche évaluent d'abord la fiabilité ». Le papier décrit un LLM de recherche générative déployé chez RedNote, avec un reward à deux couches ; sa fiche limite le résultat au contexte Xiaohongshu ([[sources/2026-04-13-searchllm-2026]]). core-ranking-jin : 80,3 % de Top-1 PSR sur ProductBench, « testé sur top-10 Amazon uniquement » ([[sources/2026-04-13-core-ranking-jin-2025]]). « Confirme » dépasse ce que les deux fiches autorisent, et `confidence: high` contredit la section Limites.

**Rien n'a été versé depuis le 13 avril.**
- [[sources/2026-08-25-algorithme-strategie-ete-agents-ia]], ligne 43 : le risque est l'exclusion de la sélection de l'agent, pas le déclassement, « à verser à [[concepts/agentic-search]] ». Jamais fait. La même fiche précise que la thèse est posée « sans étude ni part de marché ».
- [[syntheses/algorithme-week-2026-W39]], signaux faibles, chacun cité une fois : Sponsored Agents d'OpenAI (un milliard de dollars annualisé en moins de 200 jours, Shopify et HubSpot partenaires de lancement), catalogue « Agentic Resource Discovery » dans Lighthouse (Google, Microsoft, Hugging Face, Chrome 156), paiement natif Gemini activé par défaut sur les boutiques Shopify US le 22/09. Sources primaires non relues ici. W38, W42 et [[syntheses/memoire-s1-breves-mediaseo]] contiennent au moins un de ces termes, non relues en détail.
- [[sources/2026-09-25-scan-arxiv-25-septembre]] : Agent2UCB (9 stratégies GEO par contenu, sélection par bandit UCB). Côté optimisation, dans le prolongement d'AgenticGEO et MAGEO déjà cités.
- `raw/auteurs/greg-isenberg/2026-05-13-notes-on-agent-economy.md`, non ingéré en `wiki/sources/` : Greg Isenberg écrit que l'acheteur nouveau sur internet est un agent qui n'achète que via MCP. Opinion sans donnée. Il n'existe pas de page MCP dans `wiki/concepts/` ni `wiki/entities/`. Toute reprise suit l'attribution du §13.

Certains backrefs ne portent aucune matière agent : [[sources/2026-07-14-algorithme-ia-moins-utile-google]] liste le concept en « Concepts » alors que la fiche traite d'un sondage de confiance et d'AI Mode.

**Aucune hypothèse n'est adossée.** [[hypotheses]] ne contient aucune ligne sur l'agentic. L'affirmation centrale (« le SEO devient être sélectionné par l'agent ») n'a ni formulation falsifiable ni fiche preuve. Elle sert pourtant de justification dans [[concepts/know-simple-know-do]] (lignes 15, 28-29) et dans [[concepts/methode-organikk-4-piliers]] (ligne 42 : sans AEO, le reste est « invisible en Agentic Search »).

**Wording.** Pas de mot banni §11. Deux défauts de forme : « cent. M utilisateurs » (ligne 33) alors que la source dit « centaines de millions » ; `sources: 7` alors que la fiche cite 9 sources distinctes.

## Verdict proposé pour la revue hebdo

- [ ] Toujours juste, rien à faire
- [x] À mettre à jour : (1) `confidence: high` → `medium`, et `sources: 9` ; (2) verser le point de [[sources/2026-08-25-algorithme-strategie-ete-agents-ia]] (exclusion de la sélection, thèse sans étude) en le datant et en marquant qu'il est d'opinion ; (3) ajouter une section « Signaux commerce agentique » avec les trois éléments de W39, chacun marqué « cité une fois, source primaire non relue » ; (4) réécrire « Confirme » (ligne 33) en « suggère, sur un LLM de recherche, hors agent » ; (5) remplacer « cent. M » par « centaines de millions » ; (6) rattacher la définition à H-001 au lieu de la présenter comme acquise ; (7) proposer à `hypotheses-validation` une ligne `ouvert` pour la thèse « un agent sélectionne à la place de l'utilisateur », avec son contre-argument à chercher avant tout passage de statut.
- [ ] À challenger
- [ ] Wording à corriger

`raw/` reste intact. Le point (7) est une proposition : `hypotheses.md` ne bouge pas sans validation de Tim.
