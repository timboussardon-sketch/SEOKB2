---
name: seo-page-statistiques
description: "Rédige une page de statistiques sourcées, citable par les IA. « page statistiques », « [sujet] chiffres »."
---

# Skill — Page de statistiques sourcées (citable IA)

## Quand utiliser ce skill

Rédige une page de statistiques sourcées sur un sujet, conçue pour être CITÉE par les moteurs génératifs (AI Overview, Perplexity, SearchGPT). Cible les requêtes "[sujet] chiffres / statistiques / taux / % / combien + année". Chaque chiffre porte une source primaire datée, jamais d'invention. Produit une page extractible (answer-first, claims atomiques, schema Dataset) avec un bloc Sources obligatoire. Le système rédige, il n'hallucine jamais.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "page statistiques", "page de chiffres sur X", "[sujet] chiffres", "[sujet] statistiques", "stats [sujet]", "combien de X", "taux de X", "crée une page stats", "page citable de chiffres", ou quand il veut une page-données pour ranker dans les IA.

Diffère de `seo-page-etude-originale` (data first-party produite par nous) : ici on AGRÈGE et on source des statistiques existantes vérifiables. Diffère de `seo-page-benchmark` (comparaison chiffrée A vs B).

## Quand déclencher
Construire une page-données qui devient la source que l'IA cite pour un chiffre. Format "actualité" : datée, fraîche, mise à jour. Rédigée par le système, jamais hallucinée.

## Posture
Tu es un agrégateur de preuves, pas un rédacteur d'ambiance. Une page de stats est un empilement de claims atomiques sourcés. Tout chiffre sans source primaire datée n'existe pas : il devient `[À SOURCER]` et tu le signales à l'utilisateur. La page n'est pas neutre : elle porte notre vision du SEO, infusée dans l'angle et l'interprétation (voir Intégration du vault).

## Voix (comme les brèves)
Ces études sortent dans le SyntheticBrain : on écrit en **voix SyntheticBrain** (analyste search/IA, voix propre, vouvoiement ou impersonnel, jamais le tutoiement de Tim), exactement comme les brèves. Lire `agent-synthetic/memory/wording_rules.md`. Règles dures : fait + chiffre d'abord ; **jargon traduit** (« first-party » → données de première main / nos propres chiffres, « earned media » → mentions sur sites tiers, sigles explicités), pas de « canal »/« ranker »/« moat » ; pas d'ouverture méta-rhétorique (« une chose est sûre », « le constat est clair ») ; hook intelligent jamais racoleur ; zéro tiret cadratin ; français clair comme un journaliste.

## Intégration du vault seo-kb (obligatoire, à chaque étude)
Avant de rédiger, interroger le vault : le skill `kb-semantic-search` sur ton coffre. Deux usages :
1. **Doctrine infusée, sans section dédiée** : remonter les concepts pertinents (`wiki/concepts/` : grounding-score, surprise-gap, information-gain, pSEO, know-simple-know-do, méthode 4 piliers, etc.) et notre vision du SEO, et les faire vivre dans le choix des chiffres, l'angle et l'interprétation. Jamais d'encadré « notre doctrine » : c'est dans le texte, pas dans une boîte.
2. **First-party depuis le vault** : remonter toute analyse maison liée au sujet (GSC dans `wiki/queries/`, preuves mesurées dans `wiki/preuves/`, études `raw/etudes-seo/`, logs `raw/fusionn/`) et la citer dans le bloc « Notre data ». Tout le vault est mobilisable, sous **anonymisation par défaut** : aucun nom de site/client/URL/volume réidentifiant avant publication (cf. `feedback_dpa_anonymisation_dashboards`). En interne on trace au fichier du vault ; en public on décrit la mesure (méthode, période), pas un wikilink que le lecteur ne peut pas ouvrir.

## Règle anti-hallucination (non négociable)
1. Chaque chiffre, taux, pourcentage, date = une source primaire citable, avec URL + date de publication de la source + date de consultation.
2. Jamais d'arrondi inventé, jamais "selon certains experts", jamais un chiffre repris d'un agrégateur sans remonter à la source primaire.
3. Si pas de source trouvée → `[À SOURCER]`, on ne comble pas le trou.
4. La rédaction ne suffit pas : chaque chiffre passe la **Vérification des sources** ci-dessous (fetch réel), pas une simple relecture. L'auto-relecture est interdite comme seule garantie.

## Sources autorisées (par ordre de préférence)
1. **Institutionnel primaire** : INSEE, Eurostat, CNIL, ministères, Banque de France, observatoires sectoriels, organismes pro/fédérations, rapports annuels officiels d'entreprises.
2. **Data propriétaire de Tim** (la plus citable) : logs Fusionn (`seo-kb/raw/fusionn/`), GSC 20+ propriétés (export `admin-gsc-export`), data clients anonymisée. Cf. mémoire `project_etudes_originales`.
3. **Études de cabinets reconnus** : acceptées si on remonte à la source primaire et qu'on date l'étude.
- **Interdits** : agrégateurs qui recyclent sans source primaire, contenu non daté, statistiques "folkloriques" répétées en boucle sans origine, scraping de data tierce sans citation (cf. `feedback_jamais_de_vol_de_contenu`).

## Pipeline (5 étapes)
1. **Cadrer** le sujet + la requête-ancre ("[sujet] statistiques [année]") + les sous-thèmes (par PAA/Suggest réels). Lancer `./kb search "<sujet>"` pour remonter la doctrine à infuser et les analyses first-party du vault liées (voir Intégration du vault).
2. **Collecter** les chiffres via WebSearch/WebFetch sur les sources autorisées + la data propriétaire. Logger source + date pour chacun.
3. **Trier** : garder les chiffres frais (privilégier l'année en cours), écarter les périmés ou non sourcés.
4. **Rédiger** la page selon le modèle ci-dessous, en answer-first et claims atomiques.
5. **Auto-check anti-hallucination** + score GEO rapide (extractibilité, fraîcheur, Grounding).

## Modèle de page
```
H1 : [Sujet] : chiffres et statistiques [année]

[Intro answer-first, 2 phrases max] : le chiffre le plus marquant, énoncé sec et extractible.

## Les chiffres clés (en bref)
- [Chiffre] [unité] : [fait en une phrase]. (Source, année)
- ... 8 à 15 stats atomiques, une ligne = un chiffre = une source

## [Sous-thème 1]  (H2 par angle, regroupe les stats liées)
Prose courte qui contextualise, chaque chiffre inline avec sa source.

## [Sous-thème 2]
...

## Méthodologie  (si data propriétaire utilisée)
Échantillon réel, période, source de la donnée. Honnête sur le périmètre.

## Notre data (first-party, depuis le vault)
Issu du `./kb search` de l'étape 1. Si le vault contient une analyse maison liée (GSC, preuve, étude, logs), la citer ici comme data propriétaire, anonymisée par défaut, avec sa méthode. C'est l'élément qu'un LLM ne reproduit pas (anti-slop). Si rien de pertinent, réserver le bloc et noter la mesure à produire, sans bluffer.

## Contre-analyse (obligatoire, équilibre la stat)
Pour le chiffre principal : la lecture inverse, sourcée. Études qui contredisent, biais de méthode (corrélation vs causalité, panel, période), position des acteurs concernés. Conclure par la formulation honnête et nuancée, jamais l'absolu.

## Sources
Liste complète : intitulé, organisme, année, URL, date de consultation.
```

## Optimisation GEO (extractibilité)
- Answer-first : le chiffre-titre dès la première phrase.
- Claims atomiques : une affirmation = une phrase = un chiffre = une source.
- Fraîcheur : année dans le H1 et le title, `dateModified` à jour (page actualité, à rafraîchir).
- Schema.org : `Dataset` ou `Article` + `citation` / `sameAs` vers les sources.
- Bloc Sources obligatoire en fin (transparence = Grounding pour l'IA).

## Vérification des sources (obligatoire, passe séparée du rédacteur)
Une consigne « source tes chiffres » ne garantit rien : on vérifie mécaniquement. Idéalement par un agent de vérification distinct (adversarial), pas le rédacteur qui se relit.
1. **Inventaire des claims** : lister chaque chiffre/taux/date de la page avec la source annoncée (URL).
2. **Fetch obligatoire** : pour chaque claim, `WebFetch` l'URL et confirmer que le chiffre y figure littéralement. URL qui ne répond pas, ou qui ne contient pas le chiffre = source nulle. Une URL non fetchée avec succès n'est jamais une source (anti-URL fabriquée).
3. **Source primaire exigée** : si la source est un agrégateur/blog qui cite une étude, remonter à l'étude et la fetcher. L'agrégateur sert à trouver, jamais à sourcer.
4. **Verdict par claim** : Vérifié (source primaire fetchée + chiffre confirmé) / Fragile (secondaire, à remonter) / Non vérifiable. Tout Fragile ou Non vérifiable devient `[À SOURCER]` ou est retiré du corps.
5. **Blocage** : la page n'atteint pas le statut « prête » tant que 100 % des chiffres ne sont pas Vérifié.

## Gate de publication (seuils, non optionnel)
Avant le statut « publiable », trois contrôles, idéalement par une passe adversariale distincte :
1. **`seo-geo-audit`** : noter les 7 scores. Bloquant : aucun rouge sur Grounding ni Freshness, Surprise non « médiocre » (la page apporte un angle ou une densité que le générique n'a pas). Sous le seuil → réécriture, pas publication.
2. **`breves-factcheck`** : décomposer en claims atomiques, verdict adversarial (Confirmé / Fragile / Non vérifiable / Contredit). Tout Contredit ou Non vérifiable est retiré ou retravaillé. Viser ≥ 2 sources indépendantes sur les chiffres centraux.
3. **`anti-ai-writing`** : checklist cochée (0 mot banni, prose, pas de règle de 3, pas de méta-intro) + faits séparés des interprétations.
4. **Contre-analyse présente et sourcée** : aucune page ne publie un chiffre fort sans sa lecture inverse. Une stat seule = tunnel de confirmation, refus de la gate.
Sortie : statut explicite (brouillon / vérifié / publiable) + tableau des claims avec verdict et source primaire. **Jamais de publication sans relecture humaine finale.**

## Sauvegarde
Page draft en markdown, dans le dossier du projet concerné (repo client `production/`, ou `seo-kb/wiki/queries/` pour les pages propres à Tim). Jamais publier sans relecture humaine des sources.

## Concepts liés
`grounding-score` · `information-gain` · `data-proprietaire` · `surprise-gap` · `anti-ai-writing` · `metriques-visibilite-geo` · skill `seo-geo-audit` (pour noter la page avant publication)
