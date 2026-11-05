---
type: register
title: Résurgence 2026-08-26 — AEO
aliases: [resurgence-2026-08-26]
tags: [resurgence, aeo, geo, revue-hebdo]
created: 2026-08-26
updated: 2026-08-26
sources: 4
confidence: high
status: stable
---

# Résurgence — [[concepts/aeo]] — 2026-08-26

## Pourquoi celui-là

`updated: 2026-04-13`, soit 135 jours sans révision déclarée. 70 fichiers du vault pointent vers `[[concepts/aeo]]` (94 dans le comptage de [[revue-hebdo/resurgence-2026-08-12]], qui incluait les liens `[[aeo|…]]`) : c'est le hub le plus référencé parmi les concepts stables non encore ressortis (devant [[concepts/e-e-a-t]] à 36 et [[concepts/passage-ranking]] à 33). Jamais passé en résurgence (les six précédentes : data-proprietaire, grounding-score, surprise-gap, information-gain, persistent-wiki-vs-rag, programmatique-pseo). Le concept porte la définition du pilier 4 de la doctrine et le split 70/30 SEO/GEO : le laisser dériver coûte cher.

## État vs aujourd'hui

**Drift silencieux sur les métadonnées.** La section « Pages liées » cite des sources datées du 15, 17, 22 et 24 avril 2026, alors que `updated:` est resté au 13 avril et `sources: 9`. La page a donc été enrichie sans bump de frontmatter. Le tri par ancienneté du skill ne la voyait pas comme touchée, à tort ou à raison, mais surtout la valeur `updated:` ment.

**Quinze sources postérieures pointent vers le concept sans y être reflétées.** Entre autres : [[sources/2026-04-25-organikk-reddit-pour-geo]], [[sources/2026-06-09-algorithme-ia-detruire-business-seo]], [[sources/2026-06-19-playbook-reddit-seo-geo]], [[sources/2026-06-19-playbook-x-seo-geo]], [[sources/2026-06-24-organikk-mots-cles-qui-ramenent-du-clic]]. Trois apports manquent au corps du concept :

1. La preuve quantitative repose sur une seule étude (Semrush, « 4x », confidence medium, lien indisponible). [[sources/2026-06-09-algorithme-ia-detruire-business-seo]] rassemble depuis d'autres benchmarks (Seer Interactive 15,9 % vs 1,76 %, B2B Tech 14,2 % vs 2,8 %, Microsoft Clarity 3x) et signale que ces périmètres sont hétérogènes et que le 4x Semrush date de juillet 2025. Le concept présente encore le 4x comme la preuve, sans cette réserve ni le faisceau.
2. Les canaux tiers comme levier AEO (Reddit, X, YouTube avec corrélation 0,737 sur 75 000 marques selon Ahrefs, cité dans la même source) sont absents. Le concept reste centré sur la page propre, alors que la KB a bougé vers « la citation passe aussi par les plateformes où l'IA lit ».
3. Le lien avec [[concepts/mots-cles-actionnels]] et [[concepts/test-substitution-llm]] (2026-06-24 : « je ne travaille pas pour ChatGPT ») n'est pas fait. C'est une nuance doctrinale réelle : l'AEO n'est pas une fin, on cible les requêtes que l'IA ne peut pas absorber.

**Hypothèses.** Aucune ligne de [[hypotheses]] ne s'adosse explicitement à `concepts/aeo`. H-002, H-004, H-011 portent sur la citation LLM mais via surprise-gap, wiki persistant et directories. Rien n'a bougé qui invalide le concept ; rien ne le valide non plus.

**Wording.** Ligne 27 : « focus : visibilité dans l'ère IA ». Viole [[concepts/tabou-visibilite]] (règle §11 point 10 d'AGENTS.md, apparue après la rédaction du concept). À remplacer par « citations IA ».

**Toujours juste sur le fond.** Définition, distinction AEO/GEO, rattachement à surprise-gap et grounding-score : rien dans les sources récentes ne contredit. Le concept n'est pas faux, il est incomplet et mal daté.

## Verdict proposé pour la revue hebdo

- [ ] Toujours juste, rien à faire
- [x] À mettre à jour : bump `updated:` et `sources:` (9 → ~24 backlinks sources) ; remplacer la section « Preuve quantitative » monosource par un faisceau de benchmarks avec la réserve d'hétérogénéité ([[sources/2026-06-09-algorithme-ia-detruire-business-seo]]) ; ajouter une section « Canaux tiers » (Reddit, X, YouTube) ; lier [[concepts/mots-cles-actionnels]] et [[concepts/test-substitution-llm]] ; corriger « visibilité » → « citations IA » (ligne 27). Exécution : mini-ingest de mise à jour, pas de nouvelle source à créer.
- [ ] À challenger : —
- [ ] Wording à corriger : — (inclus dans la mise à jour ci-dessus)

Point de vigilance : ici le `updated:` n'a pas été bumpé alors que la page a bien été éditée (sources d'avril ajoutées en « Pages liées »). Ce n'est pas le cas programmatique-pseo du 12 août, où la page était réellement intacte. Première occurrence observée du thème `frontmatter-updated-non-bumpe` ; à tracer `isolée` dans [[corrections-recurrentes]] seulement si Tim le confirme vendredi.
