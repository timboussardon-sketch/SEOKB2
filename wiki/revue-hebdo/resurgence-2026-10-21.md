---
type: register
title: Résurgence 2026-10-21, fully-meets
tags: [resurgence, revue-hebdo, quality-raters, product-led]
created: 2026-10-21
updated: 2026-10-21
status: stable
---

# Résurgence : [[concepts/fully-meets]] (2026-10-21)

## Pourquoi celui-là

`updated: 2026-04-13`, 191 jours sans modification, `sources: 2`, `confidence: high`. 64 backrefs dans `concepts.json`, le plus haut des concepts `stable` figés pas encore ressortis : devant [[concepts/agentic-search]] (57) et [[concepts/passage-ranking]] (54). Jamais passé en résurgence. Hors fenêtre de 8 semaines : aeo (08-26), ingenierie-semantique-inversee (09-09), product-led-seo (09-23), e-e-a-t (10-07), tabou-visibilite (10-14).

Il porte la justification normative de [[concepts/product-led-seo]] : « exactement la définition normative QRG » (ligne 21 de cette page). Si la définition est fausse, la justification tombe avec.

## État vs aujourd'hui

**La définition du concept contredit le texte du guide, que le vault publie lui-même depuis le 17/07.** Le concept définit Fully Meets comme la note donnée quand le contenu satisfait « complètement l'intention sans nécessiter de recherche supplémentaire ». Le guide (version du 11 septembre 2025, §13.2, p. 118) pose trois conditions cumulatives : intention spécifique et non ambiguë, un site, une page ou un fait know-simple précis que presque tous les utilisateurs cherchent, satisfaction complète de presque tous. Il ajoute : « Most queries cannot have a Fully Meets result. » §13.0 (p. 113) parle d'une « special rating category » réservée aux requêtes qui visent « one specific result ». Les exemples de §13.2.1 sont tous de la navigation : [amazon], [titanic imdb], [cnn health]. §13.2.2 range les requêtes larges ([knitting]) parmi celles qui ne peuvent pas avoir de Fully Meets.

Ces passages sont dans `organikk-next/public/qrg-passages.json` et en ligne sur `organikk.co/guide-evaluateurs-google`. La page `fully-meets` est l'une des deux mieux notées de la cohorte à l'audit interne (9,6) et l'une des deux qui remontent le plus au J+30 ([[preuves/2026-07-17-organikk-directories-guide-google]], [[revue-hebdo/2026-W35]]). La page publique dit donc l'inverse de la fiche concept qui y renvoie.

**L'implication product-led ne tient pas.** La fiche affirme qu'un calculateur « maximise structurellement le Fully Meets » sur une requête Do. « Calculer budget X » ou « simuler Y » ne désigne aucune page unique que presque tous les utilisateurs chercheraient : d'après §13.2 et §13.2.2, ces requêtes ne peuvent pas avoir de Fully Meets. J'en déduis (le guide ne parle pas des calculateurs) que le plafond d'un calculateur est Highly Meets, « a very helpful result » pour l'intention dominante (§13.0). La thèse product-led n'en dépend plus pour autant : depuis la résurgence du 09-23, elle est suivie en H-012 sur la citation IA, pas sur la note des évaluateurs ([[hypotheses]]).

**Origine de l'erreur : un résumé de seconde main.** `raw/papers/google-quality-raters-guidelines-2026.md` fait 46 lignes de résumé, pas le PDF. Sa ligne 25 porte la définition élargie, sa ligne 39 « les outils interactifs maximisent le Fully Meets ». La fiche [[sources/2026-04-13-google-quality-raters-guidelines-2026]] et le concept reprennent les deux telles quelles. Le titre de la fiche dit « 2026 » alors que la version est celle du 11 septembre 2025.

**La même lecture s'est propagée.** Le grep ramène quatre pages qui l'utilisent comme argument :
- [[concepts/product-led-seo]], ligne 21 (« exactement la définition normative QRG »)
- [[concepts/mots-cles-actionnels]], ligne 45 (le calculateur « valide » le Fully Meets)
- [[concepts/test-substitution-llm]], lignes 49-51 (passer le test rapproche du Fully Meets)
- [[sources/2026-09-26-patron-hn-page-marque-solution]], ligne 85 (un H2 de résultats « vise le Fully Meets sur l'intention décisionnelle »)

Les livrables clients ne sont pas exposés, puisque le terme y est banni ([[syntheses/memoire-s3-redaction-regles-ecriture]], ligne 108).

**Hypothèses.** H-012 cite [[concepts/fully-meets]] en concept adossé, mais elle porte sur la citation IA : la correction ne change pas son statut. H-011 (cohorte du guide, J+90 passé le 2026-10-15) mesure des impressions, pas la justesse de la définition.

**Wording.** Pas de mot banni §11. Bold en tête de lignes (« **complètement** »), sans gravité.

## Verdict proposé pour la revue hebdo

- [ ] Toujours juste, rien à faire
- [x] À mettre à jour : (1) remplacer la définition par les trois conditions de §13.2, avec « Most queries cannot have a Fully Meets result » et les exemples navigationnels, en citant la page publiée du guide Organikk ; (2) réécrire la section « Implication doctrine Tim » : un calculateur vise Highly Meets, et la thèse défensive renvoie à H-012 ; (3) corriger la même lecture dans les quatre pages listées plus haut ; (4) corriger la fiche [[sources/2026-04-13-google-quality-raters-guidelines-2026]] (version 2025-09-11, ligne « outils interactifs maximisent Fully Meets ») et noter dans la fiche que `raw/papers/google-quality-raters-guidelines-2026.md` est un résumé, pas le texte.
- [ ] À challenger
- [ ] Wording à corriger

`raw/` reste intact. Le texte primaire est déjà dans le vault côté organikk-next : aucun ingest à prévoir, la correction s'appuie sur `qrg-passages.json`.
