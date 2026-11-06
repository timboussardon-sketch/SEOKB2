---
name: seo-cannibalisation
description: "Audit de cannibalisation depuis la GSC : type de conflit, puis 301, fusion ou différenciation. « cannibalisation »."
---

# Skill — Cannibalisation SEO

## Quand utiliser ce skill

Audit de cannibalisation SEO depuis les données GSC. Identifie les pages en compétition interne sur les mêmes mots-clés ou intentions, classifie le type de conflit (mot-clé exact, même intention, proximité sémantique, Triade SERP), analyse les métriques, recommande l'action (301, fusion, différenciation, maillage croisé, ou aucune action si Triade SERP). Sortie obligatoire en plus du tableau : un rapport de pré-décision (diagnostic, preuves typées, état Critique / À améliorer / Sain, actions P1-P3 avec confiance, effort et risque, jamais de score affiché) ; sans lui le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "cannibalisation", "deux pages sur le même mot-clé", "je rankais mieux avant", "pages en compétition interne", "keyword cannibalism", "audit cannibalisation".

## Quand déclencher

Deux pages se concurrencent sur les mêmes mots-clés ou intentions. Chutes de positions inexpliquées, CTR qui stagne malgré le volume.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Export GSC Requêtes — filtré par URL, 90j | Oui |
| Liste des URLs (scraping ou sitemap) | Recommandé |
| Contexte stratégique (pilier vs satellite) | Recommandé |

## Pipeline (5 étapes)

1. **Identifier les coexistences** — requêtes qui déclenchent 2+ URLs dans la GSC. Ce sont des candidats, pas des conflits. La taille du site n'exclut rien : deux pages suffisent à se concurrencer.
1bis. **Lire dans le temps et par segment avant de qualifier** — sur la période, les deux URL coexistent-elles ou se succèdent-elles (une remplace l'autre) ? Servent-elles des pays ou des appareils différents ? Répondent-elles à des facettes complémentaires de la même requête ? GSC attribue une grande partie des performances aux URL canoniques : vérifier la canonical de chaque URL avant de lire ses chiffres. Une succession, deux marchés ou deux réponses complémentaires ne sont pas des conflits.
2. **Classifier le type** :
   - **(A) Mot-clé exact** — deux pages sur la même requête précise
   - **(B) Même intention** — deux pages répondent à la même intention
   - **(C) Proximité sémantique** — sujets proches sans conflit direct
   - **(Triade SERP)** — opportunité, pas conflit
3. **Analyser les métriques** — position, impressions, clics, CTR par page
4. **Évaluer l'architecture** — pilier vs satellite, objectif business
5. **Proposer l'action, avec sa justification** — le tableau ci-dessous donne l'action type par situation ; une fusion ou une 301 demande une justification plus forte qu'un simple chevauchement (métriques des deux pages, lecture temporelle et segmentée faite, contenu lu, destination claire) et porte toujours « À valider avant déploiement » :

| Situation | Action |
|-----------|--------|
| Type A + perdante faible | Redirection 301 |
| Type A + deux fortes | Fusion + 301 |
| Type B + micro-intentions distinctes | Différenciation + maillage croisé |
| Type C | Renforcement maillage vers pilier |
| Triade SERP | Aucune action — optimiser chaque angle |

## Sortie de pré-décision (obligatoire)

Ce skill n'a pas terminé tant que le rapport de pré-décision n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau, et il suit `audit-complet-v2/rapport-audit-seo-format.md` (`audit-complet-v2/rapport-audit-seo-format.md`). Fichier : `wiki/cannibalisation/YYYY-MM-DD-slug-decision.md`.

Ce qu'il contient, dans cet ordre :

1. Diagnostic principal : une phrase, la cause structurante, pas une liste d'erreurs
2. Les chiffres à retenir : 3 à 5, ceux qui illustrent le diagnostic
3. État : Critique, À améliorer ou Sain, calculé sur l'impact SEO réel et le type de page, jamais sur le nombre d'erreurs ; jamais de score sur 10
4. Problèmes (3 maximum) et opportunités (5 maximum), séparés : chacun avec Preuve (2 à 4 données), Pourquoi c'est important, Action, Confiance (forte / moyenne / faible) ; chaque problème s'écrit en trois temps : observation prouvée → conséquence ou risque justifié → bénéfice attendu de la correction (l'observation seule n'est pas un frein SEO démontré)
5. Actions P1 / P2 / P3, 3 P1 maximum : pourquoi, preuve, signal attendu (jamais un résultat chiffré promis), dépendance préalable, test de validation (ce qui distingue « correction appliquée » de « résultat SEO observé »), effort faible / moyen / élevé (jamais en heures), confiance, risque low / medium / high ; toute action high (suppression, 301, fusion, changement d'URL) porte « À valider avant déploiement » et sa checklist
6. Ce que les données ne permettent pas de conclure, et « données insuffisantes » ou « ne rien faire » quand c'est le cas

Sur le périmètre de ce skill, le rapport tranche les conflits, trois états : cannibalisation confirmée (même requête GSC + intention concordante), chevauchement potentiel, pages proches mais différenciables ; fusion seulement pour confirmée + destination claire, sinon vérifier, repositionner, différencier ; toute fusion ou 301 = « À valider avant déploiement » + checklist.

Règles : chaque information est typée FACT, HYPOTHESIS ou ACTION, jamais une hypothèse écrite comme un fait ; un problème existe une seule fois (ID), les observations qui parlent du même problème fusionnent ; une anomalie n'est pas une priorité par défaut ; les pages business et les tendances GSC passent avant les anomalies techniques secondaires ; jamais de recommandation automatique de fusion, 301, suppression, réécriture ou création de page ; Google n'est jamais anthropomorphisé. Phrases courtes, une donnée par diagnostic, aucune des phrases « Il est important de », « Il convient de », « Cela peut potentiellement », « Il est intéressant de noter », « Dans le cadre de ».

Restitution (corrections V2 du 23 septembre) : aucun ID technique ni mot anglais (low / medium / high) dans le rapport ; Faible / Moyen / Élevé partout ; la certitude affichée ne dépasse jamais la couverture des données (« aucun problème majeur détecté sur les URL inspectées », pas « Sain ») ; formulations précises (« URL en 404 avec encore des impressions ») ; aucune action proposée sur une page dont les requêtes ne sont pas connues (« à vérifier ») ; le nombre de mots seul n'est jamais un problème ; limites de longueur : diagnostic 70 mots, 4 chiffres, 3 problèmes de 40 mots, 6 actions, 3 opportunités de 35 mots, le reste dans les détails repliés.

Onglet Analyse technique, structure validée le 23 septembre 2026 (référence : [[audit/2026-09-22-organikk-co]]) : chaque priorité = une phrase de cadrage, « Ce qu'on observe » (faits chiffrés en liste, pages en code), « Pourquoi c'est prioritaire » (deux phrases), « Action » (liste numérotée courte), « Impact attendu » et « Risque » en gras ; puis le plan des 30 jours en trois paliers (Priorité immédiate, Deuxième étape, Priorité secondaire), une action par paragraphe en gras suivie d'une phrase ; puis « à surveiller avant d'agir » pour la page dont la cause n'est pas isolée ; puis « Autres pages à surveiller » : chiffres séparés par « · », une phrase, verdict en gras (« Aucune action recommandée », « À vérifier avant toute modification »).

## Output obligatoire

Trois états, dans cet ordre, et on ne saute pas d'étape : **coexistence observée → conflit probable → action proposée avec justification**. Une coexistence sans lecture temporelle et segmentée reste une coexistence.

```
COEXISTENCE OBSERVÉE
Requête : '[requête]' — Type candidat : (A/B/C/Triade)
| URL | Canonical | Position | Impressions | Clics | CTR | Période de présence | Pays / appareil |

→ Lecture temporelle et segmentée : [succession / coexistence stable / marchés distincts / réponses complémentaires]
→ État : [coexistence observée, rien à faire / conflit probable / conflit confirmé]
→ Action proposée : [aucune action / différenciation / maillage / fusion / 301] — Justification : [métriques + contenu lu + destination]
   (fusion et 301 : « À valider avant déploiement » + checklist)
```

## Règles absolues

- Ne pas recommander une 301 sans analyser les métriques des deux pages
- Ne pas traiter toutes les cannibalisations de la même façon
- Ne pas confondre duplication de contenu et cannibalisation
- Ne pas fusionner des pages avec micro-intentions distinctes
- Identifier les Triades SERP comme opportunités, pas comme problèmes
- La taille du site n'exclut jamais un conflit : aucun seuil minimal d'URL
- Aucune fusion ni 301 sans lecture temporelle et segmentée préalable et sans avoir lu les deux contenus ; « aucune action » est une sortie normale
- « Conflit probable » exige des requêtes communes mesurées ou une évolution qui attribue une perte à la concurrence des deux pages. Un recouvrement de contenu seul, avec des requêtes indisponibles, s'écrit : « les deux pages décrivent une offre proche, leur rôle doit être clarifié ; les données présentées ne démontrent pas qu'elles se pénalisent dans Google ». La différenciation éditoriale peut être proposée, jamais vendue comme la correction d'une cannibalisation diagnostiquée.

## Sauvegarde

Output dans `wiki/cannibalisation/YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`triade-serp` · `rrf` · `maillage-interne` · `intention-recherche` · `gsc-export`

## Vérification finale (obligatoire)

Avant de présenter le livrable comme terminé : lancer `verificateur-livrable` avec les 6 sections de le skill `verification-livrable` (demande de tous les skills utilisés, livrables, sources, contraintes). Corriger les ❌, relancer le vérificateur sur la nouvelle version, recopier le dernier tableau dans la réponse. Un hook refuse la fin de la réponse tant que ce n'est pas fait.
