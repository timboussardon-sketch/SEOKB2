---
type: source
source_type: article
title: "30 questions que tes clients pourraient taper sur ChatGPT (+ skill)"
aliases: [30-questions-chatgpt]
tags: [algorithme, tim, geo, chatgpt, mesure, claude]
created: 2026-10-06
updated: 2026-10-20
sources: 1
confidence: medium
status: stable
---

# 30 questions que tes clients pourraient taper sur ChatGPT (+ skill)

**Auteur** : Timothée Boussardon (algorithme.substack.com)
**Type** : newsletter
**URL** : https://algorithme.substack.com/p/30-questions-que-tes-clients-pourraient
**Date publication** : 2026-10-06

## Contexte
Comment mesurer la présence d'une marque dans les réponses des assistants IA quand on n'a pas accès aux vraies questions des utilisateurs. Tim part d'un mot-clé business et de 10 à 15 vraies questions, et présente le skill `geo-citations`.

## Chiffres / faits clés
- Requêtes passant de 4 mots en moyenne sur Google à 24 mots sur les LLM.
- Abandon d'un score pondéré (100 points en 1re position, 70 en 2e…) jugé arbitraire, remplacé par trois mesures : présence P (domaine dans les sources), recommandation R (marque citée dans la réponse), évolution entre deux relevés.
- Questions extraites de [[entities/gsc]], reformulées en questions naturelles, validées à la main puis figées pour comparer les périodes.
- Prompt Claude : 30 formulations (recommandation, liste, comparaison, débutant, contexte, confiance), 6 à 25 mots, sans citer la marque cible.
- Deux protocoles : même question répétée (10 questions × 3 modèles × 30 runs = 900+ appels API, sur [[entities/chatgpt-search]], [[entities/gemini]], [[entities/perplexity]]) ou 30 formulations posées une fois.
- Règles du skill : annonce du nombre d'appels avant exécution, échantillon trop petit signalé non crédible, aucun relevé hebdomadaire automatique sans accord.
- 1 500+ téléchargements des skills en trois semaines.

## Citations marquantes
> "Tu écris des prompts que de vrais humains tapent dans un assistant IA" (attribution : Tim, 2026-10-06)
> "ne jamais citer la marque cible" (attribution : Tim, 2026-10-06)

## Angle SEO à retenir
- Mesurer P et R sur un jeu de questions figé plutôt qu'un score de position composite.
- Les questions viennent de la data propriétaire (GSC), pas d'un outil sémantique générique.

## Limites
- « 30 questions » présenté comme minimum fiable sans source chiffrée dans le post.
- Le chiffre de téléchargements n'est pas vérifiable.
- Contenu récupéré via WebFetch (résumé), pas de lecture verbatim intégrale.

## Pages liées
**Entity** : [[entities/chatgpt-search]], [[entities/perplexity]], [[entities/gemini]], [[entities/gsc]]
**Concepts** : [[concepts/metriques-visibilite-geo]], [[concepts/geo]], [[concepts/data-proprietaire]], [[concepts/query-fan-out]]
