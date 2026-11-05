---
type: revue-presse
title: Algorithme — édition du 20 octobre 2026
date: 2026-10-20
pilier: Niche SEO
status: draft
---

# Algorithme — 20 octobre 2026

## À retenir en 15 secondes

- Pilier Niche SEO : un cas publié hier sur Search Engine Land décrit la suppression de 198 pages sur 600 (33% du site, 3,1% des clics). Quatre mois après : clics +37%, impressions +49%, sessions organiques +55%, mais mots-clés top 10 quasi stables (264 → 271).
- Pilier GEO / search IA : depuis GPT-6, les liens sortants de ChatGPT ont perdu le paramètre `utm_source=chatgpt.com` et le referrer. Les visites arrivent en direct dans les outils de mesure.
- Pilier Actualité SEO : Google teste un bouton Source preferences dans la barre latérale de citations d'AI Mode, qui ouvre directement la liste des sources préférées du compte.
- Pilier Business SEO : Google a confirmé le 16 octobre qu'il affichera des annonces publicitaires dans les réponses AI Mode des comptes qui ont activé Personal Intelligence, ce qui revient sur la promesse de mars 2026 d'une surface sans annonces.
- Résultats du cas Anna Crowe : montée de volume sans montée des positions. L'hypothèse la plus parcimonieuse est une redistribution des impressions vers les pages conservées, pas une revalorisation de la qualité globale perçue par Google.

## Info du jour — Niche SEO : pruner un tiers des pages, perdre 3% des clics, gagner 55% de sessions sans bouger le top 10

Anna Crowe a publié hier sur Search Engine Land une étude de cas détaillée sur un chantier de content pruning qu'elle a mené en décembre 2024 sur un site B2B SaaS ([Content pruning case study: Cutting 33% of pages that drove just 3% of clicks](https://searchengineland.com/content-pruning-case-study-497056), Search Engine Land, 19 octobre 2026, 11h00). Le périmètre et les chiffres sont inhabituellement explicites pour un cas pruning, ce qui permet d'en tirer une lecture propre.

Le point de départ est un crawl de 600 URLs. 198 pages sont marquées pour suppression, soit 33% du périmètre crawlé. Ces 198 pages avaient totalisé 144 clics dans Search Console, soit 3,1% des clics du site sur la période de mesure. Point souvent omis dans les cas pruning publiés : 140 des 198 pages supprimées n'avaient jamais reçu un clic en organique. Les pages concernées étaient en majorité des promotions d'évènements expirés, des posts datés, des logos clients légers et des stubs de podcasts. Le traitement a mélangé redirections 301, désindexation `noindex` et dépublication. Un mois après, un deuxième lot a sorti 60 URLs orphelines supplémentaires, essentiellement des archives de taxonomie.

Les mesures à quatre mois sont les suivantes. Clics Search Console : +37%. Impressions Search Console : +49%. Sessions organiques GA4 : +55%. Mots-clés en top 10 : 264 → 271. C'est ce dernier chiffre qui mérite l'attention. La croissance des clics, des impressions et des sessions dépasse largement la variation des mots-clés en top 10. Le sous-titre de l'article le signale explicitement : « the data told a more complicated story ».

Lecture analytique. Trois hypothèses sont compatibles avec ces chiffres, et aucune n'est tranchée dans l'article publié. **Première hypothèse** : les impressions et clics qui allaient autrefois aux 198 pages supprimées sont réabsorbés par les pages conservées, qui se repositionnent mieux sur les mêmes requêtes une fois la concurrence interne retirée. C'est la lecture [[concepts/cannibalisation]] classique. **Deuxième hypothèse** : la suppression a amélioré la fraîcheur moyenne du site (ratio pages actives sur total), ce qui a facilité le re-crawl des pages conservées, qui ont ensuite capturé des requêtes qu'elles ne couvraient pas avant. **Troisième hypothèse** : effet de signalement de qualité globale, dans la lignée des Quality Raters Guidelines ([[concepts/e-e-a-t]]), où un site plus propre reçoit une évaluation de confiance plus élevée. Cette troisième hypothèse est la plus difficile à prouver sans data externe, et c'est aussi la plus souvent invoquée par les agences qui vendent du pruning.

L'absence de progression nette sur les mots-clés top 10 (+7 positions en quatre mois) rend la troisième hypothèse peu probable comme explication principale. Si la qualité globale avait été revalorisée, le gain top 10 serait plus marqué. La redistribution des impressions ([[concepts/cannibalisation]]) et le gain de fraîcheur restent les hypothèses les plus parcimonieuses.

Points de vigilance pour reproduire la méthode sur un site publié par un lecteur :
1. Un crawl de 600 URLs est petit. Sur un site de 50 000 URLs, 33% de suppression demande un découpage par cluster thématique, pas une opération globale en un seul passage.
2. Supprimer des pages qui n'ont jamais eu de clic est une opération à faible risque, mais Search Console sous-déclare les impressions sur longue traîne. Il faut croiser avec les logs serveur et l'export GSC Discover avant de supprimer.
3. Le gain mesuré est une variation sur quatre mois sur un site qui n'a probablement pas subi de core update entre temps. Le mai 2026 core update, qui a terminé son déploiement vers le 4 juin, change le baseline de nombreux sites. Reproduire aujourd'hui, après le spam update de septembre (clos le 8 octobre), n'offrira pas les mêmes conditions.

**Ancrage doctrine**. Ce cas renforce [[concepts/cannibalisation]] (la lecture par redistribution d'impressions) sans valider [[concepts/e-e-a-t]] comme mécanisme opérant à cette échelle. Il nourrit aussi la [[concepts/boucle-sortie-mesure]] : Anna Crowe publie à J+120 avec les trois sources de mesure (Search Console clics, Search Console impressions, GA4 sessions) et le compteur de positions. C'est la méthode à retenir : trois canaux de mesure, pas un seul, et une période de référence stable.

**Pattern reproductible par d'autres sources**. Le gain post-pruning est documenté par Seer Interactive (+23% de trafic organique YoY sur un cas pruning historique, [case study Seer](https://www.seerinteractive.com/work/case-studies/content-pruning-efforts-help-reverse-traffic-loss)) et par GoInflow (hausse de revenus reportée après suppression d'environ 200 pages, [Content Pruning Case Study GoInflow](https://www.goinflow.com/blog/content-pruning-case-study/)). Le pattern tient. Ce qui change dans le cas Anna Crowe, c'est l'écart explicite entre volume (+55% sessions) et positions (+7 top 10), qui invite à ne plus décrire le pruning comme une opération qui améliore les positions, mais comme une opération qui redistribue le volume vers les pages conservées.

## Brèves

### GEO / search IA — ChatGPT retire `utm_source=chatgpt.com` et le referrer avec GPT-6

Depuis la mise en production de GPT-6 en octobre 2026, les liens sortants cliqués dans ChatGPT ne transportent plus le paramètre `utm_source=chatgpt.com` qu'OpenAI avait introduit, selon [ChatGPT appears to drop UTM tracking, making AI referral traffic harder to measure](https://searchengineland.com/chatgpt-appears-to-drop-utm-tracking-making-ai-referral-traffic-harder-to-measure-496552) (Search Engine Land, article relayé par Barry Schwartz le 14 octobre 2026 sur Search Engine Roundtable) et confirmé par [ChatGPT drops UTM tags? Clicks now show as Direct](https://www.relevantaudience.com/analytics/chatgpt-gpt-6-utm-referrer-dropped-direct-traffic/) (Relevant Audience, octobre 2026).

L'ingénieur Adobe Cedric Huesler, cité dans les deux articles, précise que GPT-6 ouvre les liens avec `rel="noopener noreferrer"` et sans le paramètre UTM. Les visites arrivent donc dans Google Analytics 4 et dans les autres outils de mesure sans source ni referrer, et sont classées en « direct ». Deux tiers des pages qui recevaient historiquement du trafic ChatGPT ont vu leur trafic direct augmenter sur la même période, selon la mesure citée dans Relevant Audience. OpenAI n'a pas confirmé si ce changement est intentionnel.

Conséquence opérationnelle pour les sites qui mesuraient l'apport ChatGPT : la méthode d'attribution basée sur `utm_source=chatgpt.com` ne fonctionne plus pour les sessions ouvertes depuis GPT-6. Les deux voies de contournement praticables sont : classer en IA toute session « direct » dont la page d'atterrissage est une URL profonde (pas la racine) ouverte en dehors des heures ouvrées habituelles, et croiser avec les logs serveur pour isoler l'user-agent `GPTBot` et les requêtes browse ChatGPT, qui gardent un user-agent détectable même sans referrer. Les deux voies sont approximatives.

Ce changement affaiblit la [[concepts/boucle-sortie-mesure]] pour l'apport ChatGPT : le canal d'attribution direct est cassé tant qu'OpenAI ne revient pas en arrière ou ne publie pas une alternative.

### Actualité SEO — Google teste un bouton Source preferences dans la barre latérale de citations d'AI Mode

Google teste depuis mi-octobre 2026 un bouton `Source preferences` directement intégré à la barre latérale de citations d'AI Mode, selon [Google AI Mode Citations With Source Preferences For Preferred Sources](https://www.seroundtable.com/google-ai-mode-citations-preferred-sources-42323.html) (Search Engine Roundtable, article publié vers le 17 octobre 2026). Le bouton ouvre la liste des sources préférées du compte connecté, où l'utilisateur peut ajouter ou retirer des éditeurs.

Le test a été repéré par Damien Andell, qui a posté une vidéo du bouton sur X. Barry Schwartz dit ne pas avoir vu le bouton lui-même et s'appuie sur la vidéo et une capture d'écran. Le test est donc non confirmé officiellement par Google, et pourrait rester expérimental.

Rappel de contexte. La fonction Preferred Sources a été étendue à AI Overviews et AI Mode le 27 mai 2026 ([Google extends Preferred Sources into AI Mode as new sites lose ground](https://ppc.land/google-extends-preferred-sources-into-ai-mode-as-new-sites-lose-ground/), PPC Land, mai 2026). Depuis cette date, les utilisateurs peuvent marquer un éditeur comme préféré via `google.com/preferences/source` et une étiquette `Preferred` apparaît à côté du lien quand l'éditeur est cité, visible uniquement pour l'utilisateur qui a défini la préférence. Google a aussi indiqué que les préférences personnelles influencent la sélection des publishers qui apparaissent dans les réponses AI Mode quand la requête est pertinente.

Ce que ce test change si Google le déploie : la friction d'ajout d'une source préférée tombe à un clic depuis la citation elle-même, au lieu de passer par la page de paramètres. Pour un éditeur spécialisé, cela signifie qu'un lecteur qui apprécie une citation peut le marquer en préféré sans sortir de la réponse. La boucle de personnalisation se referme beaucoup plus vite. Pour les éditeurs cités dans AI Mode, cela augmente mécaniquement la probabilité qu'un lecteur enregistre l'éditeur en préféré après lecture d'une citation jugée utile, à condition qu'il réutilise ensuite AI Mode sur des requêtes proches.

### Business SEO — Google confirme afficher des annonces en AI Mode pour les comptes Personal Intelligence

Google a confirmé à Search Engine Land le 16 octobre 2026 qu'il teste l'affichage d'annonces publicitaires dans les réponses AI Mode des utilisateurs qui ont activé Personal Intelligence, selon [Google begins testing ads in AI Mode for users with Personal Intelligence enabled](https://searchengineland.com/google-begins-testing-ads-in-ai-mode-for-users-with-personal-intelligence-enabled-496990) (Search Engine Land, 16 octobre 2026) et [Google Ads Coming To AI Mode With Personal Intelligence](https://www.seroundtable.com/google-ads-ai-mode-personal-intelligence-42320.html) (Search Engine Roundtable, 19 octobre 2026).

Cette confirmation revient explicitement sur une déclaration de Google de mars 2026, qui disait qu'AI Mode avec Personal Intelligence activé resterait sans annonces ([Google says AI Mode stays ad-free for Personal Intelligence users](https://searchengineland.com/google-ai-mode-ad-free-personal-intelligence-471861), Search Engine Land, mars 2026). La page d'aide Google indique que les résumés et inférences tirés des applications connectées (Gmail, Calendar, Photos) peuvent informer la sélection des annonces, sans que les annonceurs n'aient accès aux applications elles-mêmes, et que les catégories sensibles (santé, religion) sont exclues de la personnalisation.

Points non précisés par Google : marchés du test, formats d'annonces, contrôles annonceurs, reporting. Il n'y a pas eu de calendrier de déploiement large publié. Il n'est pas précisé non plus si les signaux issus des applications connectées influencent les annonces uniquement en AI Mode ou aussi dans les autres surfaces Search.

Lecture business. Le revirement sur six mois de la promesse « ad-free » signale que la surface AI Mode est désormais traitée comme une surface de monétisation complète, pas comme une interface « premium » détachée du modèle publicitaire. Pour les annonceurs, cela ouvre un nouvel inventaire enchérissable, encore sans format standardisé public. Pour les éditeurs organiques, le mélange annonces + citations dans la même réponse pose à nouveau la question de la frontière organique/payant dans les surfaces génératives, dossier déjà ouvert sur Gemini (formats Sponsored, 20 mai 2026) et désormais applicable à AI Mode avec Personal Intelligence.

## Prédictions ouvertes

1. P-2026-10-20-1 : OpenAI publie une alternative publique de tracking (header `X-OpenAI-Referral`, nouveau paramètre ou documentation GPTBot) permettant d'attribuer les visites ChatGPT dans GA4 avant le 31 mars 2027. Confiance 0,45.
2. P-2026-10-20-2 : le bouton `Source preferences` dans la barre latérale de citations d'AI Mode est confirmé par Google et déployé en version stable (non A/B test) avant le 31 janvier 2027. Confiance 0,40.
3. P-2026-10-20-3 : Google publie publiquement les formats d'annonces disponibles en AI Mode Personal Intelligence (nom du format, règles d'étiquetage, zones de rendu) avant le 30 juin 2027. Confiance 0,55.

---

*Rédigé par SyntheticBrain. Rien n'a été envoyé. Draft pour relecture et apprentissage.*
