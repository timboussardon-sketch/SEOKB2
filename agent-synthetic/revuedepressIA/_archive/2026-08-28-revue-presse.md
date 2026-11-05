---
type: revue-presse
title: "Algorithme. Édition du 28 août 2026"
date: 2026-08-28
pilier_info_du_jour: Recherche agentique
piliers_breves: [Actualité SEO]
tags: [seo, ia, aeo, geo, revue-presse, agentic-search]
sources_count: 8
confidence: high
status: draft
---

# Algorithme. 28 août 2026

## À retenir

- Claude embarque son propre navigateur Chromium dans son application desktop, en side panel, activé par défaut sur les plans Pro/Max/Team/Enterprise. Le navigateur n'utilise pas Chrome et n'a pas accès aux logins email et bancaires de l'utilisateur.
- Le déploiement contourne le mécanisme du choice screen imposé par le DMA aux gatekeepers désignés, puisque Anthropic ne l'est pas et qu'un browser inclus dans une app ne déclenche pas la fenêtre de choix.
- Le déplacement change la surface d'observation SEO/GEO : la session de navigation est initiée par le LLM, pas par l'utilisateur, et le référent transmis au site visité peut ne rien avoir à voir avec google/organic.
- L'étude SE Ranking sur 100 000 mots-clés US par 20 verticales chiffre enfin les conséquences du spam update Google d'août 2026 : 82 % de hausse des URLs top 10 qui chutent au-delà de la position 100 par rapport à un intervalle calme.
- La volatilité varie de 74,64 % en immobilier à 85,55 % en beauté et mode. Aucun tracker n'avait publié de bilan large échantillon par verticale depuis la clôture du 21 août.

## Info du jour. Recherche agentique. Claude embarque son navigateur dans son app desktop et sort du choice screen européen

Anthropic a annoncé le 26 août 2026 dans un billet de blog (couvert le 27 par plusieurs éditeurs indépendants) l'intégration d'un navigateur Chromium dans l'application desktop de [Claude Cowork](https://the-decoder.com/claude-cowork-now-runs-its-own-browser-inside-the-desktop-app/). Le navigateur s'ouvre en side panel quand un prompt exige une navigation web, lit les pages, clique, remplit des formulaires. Il est déployé cette semaine, activé par défaut, sur les plans Pro, Max, Team et Enterprise. Sources : [The New Stack (26 août, Frederic Lardinois)](https://thenewstack.io/claude-built-in-browser-cowork/), [The Decoder (27 août)](https://the-decoder.com/claude-cowork-now-runs-its-own-browser-inside-the-desktop-app/), [TheNextWeb (27 août)](https://thenextweb.com/news/anthropic-claude-cowork-built-in-browser-dma-choice-screen), [BigGo Finance (27 août)](https://finance.biggo.com/news/3a8d2bc8-f8d5-4636-ba4b-6c66dd481696), [Gizmodo (27 août)](https://gizmodo.com/anthropic-is-quietly-cutting-google-out-of-the-equation-2000803895).

Ce qui est nouveau, ce n'est pas la capacité de navigation d'un agent (Claude fait déjà du Computer Use, ChatGPT a eu Atlas, Perplexity a Comet). C'est que la navigation entre désormais dans le périmètre du produit desktop, sans dépendre d'une extension Chrome ni d'un navigateur tiers installé sur la machine. La citation officielle d'Anthropic reprise par TheNextWeb : « a lot of web tasks don't need your browser, just a browser, and now Claude has one ». Anthropic isole ce runtime des données utilisateur : pas d'accès aux onglets, bookmarks ou mots de passe existants, et l'import de logins est incrémental et volontaire, avec les sites bancaires et email exclus par défaut.

Le point sur le DMA. TheNextWeb formule explicitement le point réglementaire : « A browser inside an app never triggers any of it » (le choice screen imposé aux gatekeepers). Anthropic n'étant pas désigné gatekeeper, l'in-app browser embarqué dans son produit ne rentre pas dans le régime qui, chez Google ou Apple, force l'affichage d'un écran de choix de navigateur au niveau système. C'est une forme d'arbitrage réglementaire assumé.

Le repositionnement concurrentiel. OpenAI a fermé le navigateur autonome Atlas ce mois-ci et l'a replié dans un « Work mode » de ChatGPT qui intègre son propre navigateur (repris par [The Decoder](https://the-decoder.com/claude-cowork-now-runs-its-own-browser-inside-the-desktop-app/) et [Gizmodo](https://gizmodo.com/anthropic-is-quietly-cutting-google-out-of-the-equation-2000803895)). Perplexity fait la même chose depuis Comet. La direction est convergente : l'assistant conversationnel absorbe la couche navigation, plutôt que d'appeler un navigateur tiers.

Trois lectures opérationnelles pour un consultant SEO ou GEO.

Un. La session tracée côté site quand un utilisateur fait faire une recherche à Claude n'est plus initiée par Chrome. Le User-Agent envoyé au site visité est celui du browser Anthropic (voir Applebot-web comme précédent), le referrer HTTP peut être absent, direct, ou pointer vers un domaine anthropic.com selon l'implémentation. Ce trafic ne s'assied donc pas dans la colonne google / organic de GA4. Il finira dans (direct) / (none) ou dans un référent nouveau qu'il faudra apprendre à classer. C'est un déplacement de la mesure au moins aussi sérieux que le google.com/goto documenté par [Barry Schwartz sur SEL le 26 août](https://searchengineland.com/google-confirms-deploying-goto-url-redirects-to-search-results-links-485926), sur un autre canal.

Deux. Le site qui héberge des données propriétaires vérifiables reste défendable, mais la sécurité de la lecture change. Le navigateur intégré ne stocke pas les cookies de l'utilisateur au premier passage. Une page publique sera lue comme n'importe quelle page publique, une page derrière authentification ne l'est que si l'utilisateur importe manuellement ses logins. Concrètement, un éditeur qui verrouille son contenu derrière un paywall lit à travers ces browsers embarqués la même chose qu'à travers un scraper d'agent : rien de plus que le HTML public.

Trois. La couche paiement n'est pas dans le scope. Anthropic n'annonce pas de checkout intégré (à la différence d'ACP côté OpenAI ou d'UCP côté Google), donc le navigateur Claude reste un instrument de lecture et d'interaction avec des formulaires, pas un environnement de commerce agentique complet. La question de la première vente mesurée via un agent reste ouverte, non résolue par cette annonce.

Trois réserves à poser franchement. Un, aucune source publiée aujourd'hui ne mesure l'adoption réelle (nombre de sessions par jour ou par seat). Le déploiement est activé par défaut, mais l'usage est une inconnue. Deux, la spécification technique du referrer envoyé aux sites visités n'a pas été détaillée par Anthropic dans son billet ni reprise par les éditeurs, elle sera vérifiable côté serveur dans les jours qui viennent. Trois, la protection contre le prompt injection reste, selon les mêmes articles, un problème non résolu que les experts jugent difficilement solvable dans le format actuel.

Trois prédictions datées, critère binaire.

P-2026-08-28-1 : d'ici le 31 mars 2027, au moins un outil de mesure d'analytics (Adobe Analytics, GA4 audit ou tracker de visibilité) publie une segmentation nommée séparant le trafic issu de navigateurs embarqués LLM (Claude Cowork, ChatGPT Work, Perplexity Comet) sur un panel d'au moins 100 sites. Confiance 0,35.

P-2026-08-28-2 : d'ici le 31 décembre 2026, ni la Commission européenne ni la CMA UK ne publient une prise de position formelle sur la conformité DMA des navigateurs embarqués dans des applications d'assistants IA non-gatekeeper. Confiance 0,70.

P-2026-08-28-3 : d'ici le 30 juin 2027, aucun assistant IA n'aura publié un chiffre d'adoption vérifiable du type « nombre de sessions de navigation par utilisateur actif quotidien » sur son navigateur intégré, dans un rapport chiffré ou un billet officiel. Confiance 0,55.

Lien avec la doctrine. Cette annonce déplace de nouveau l'objet à optimiser vers [[concepts/agentic-search|un environnement de navigation piloté par un LLM]] hébergé chez l'éditeur du LLM. Elle rejoint la ligne du google.com/goto documentée le 26 août : plusieurs canaux d'attribution de visite se dégradent en même temps, ce qui rend la mesure côté site sur [[concepts/metriques-visibilite-geo|la couche référent GA4]] critique. La distinction [[concepts/data-proprietaire|contenu public lu librement vs contenu authentifié inaccessible]] devient un choix éditorial explicite et pas seulement une contrainte technique. La [[concepts/tabou-visibilite|mesure de la performance SEO par sessions google/organic]] va perdre en fidélité, le pont vers les leads et conversions mesurés côté site devient obligatoire. Enfin, cette annonce est un cas d'[[concepts/arbitrage-plateforme-publication|arbitrage réglementaire]] : la même fonction (fournir un navigateur qui accède au web) est traitée différemment selon que le fournisseur est désigné gatekeeper ou non.

## Brève. Actualité SEO. SE Ranking chiffre le spam update Google d'août 2026 sur 100 000 mots-clés par verticale

L'attente d'un bilan large échantillon post-spam update, ouverte depuis la clôture du 21 août, se referme partiellement. Danny Goodwin a publié le 27 août sur SEL une analyse de SE Ranking portant sur 100 000 mots-clés US organiques dans 20 industries, comparant les positions du 17 août (pré-update) et du 22 août (post-update), avec comme point de référence l'intervalle calme du 26 au 31 juillet. Source : [Search Engine Land (27 août 2026, Danny Goodwin)](https://searchengineland.com/google-august-2026-spam-update-ranking-impact-485980), méthodologie SE Ranking détaillée dans l'article.

Les chiffres clés. Pendant le spam update, 16,71 % des URLs du top 10 sont sorties au-delà de la position 100 sur leur mot-clé, contre 9,2 % sur la fenêtre de juillet, soit une hausse relative de 82 %. Multiplicateur 1,8 pour qu'une URL du top 10 disparaisse du top 100. Réciproquement, 12 % de hausse des URLs qui apparaissent en top 3 post-update sans jamais avoir figuré en top 20 auparavant.

La ventilation par verticale. La volatilité top 10 varie de 74,64 % en immobilier à 85,55 % en beauté et mode, sur les 20 industries suivies. Les catégories YMYL (immobilier et santé notamment) sont parmi les plus stables. L'analyse ne suit que les positions 1 à 100, elle ne permet pas de distinguer une URL désindexée d'une URL simplement tombée sous la 100.

Trois lectures opérationnelles.

Un. Le multiplicateur 1,8 sur la chute top 10 vers hors top 100 est un chiffre de référence à utiliser en audit client. Un site qui a perdu deux fois plus de positions top 10 vers hors top 100 sur la fenêtre 17-22 août par rapport à sa fenêtre de juillet est dans la moyenne de l'update, pas dans une anomalie spécifique. Un site nettement au-delà mérite une hypothèse spam policy (link spam, site reputation abuse, scaled content abuse) plutôt qu'un problème technique.

Deux. La faible dispersion inter-verticales (74,64 % à 85,55 %) confirme que l'update ne cible pas une verticale particulière, contrairement à des updates plus verticalisées observées historiquement. La cause de la variation est probablement le taux de spam pré-existant par verticale, pas une politique différenciée.

Trois. La fenêtre de comparaison propre est 17-22 août vs 26-31 juillet. Elle exclut le defect de logging du rapport Search Generative AI de Google Search Console (13-17 août), sujet documenté dans les éditions antérieures. Une comparaison basée sur les données Search Console du site sur la fenêtre 6-12 août vs 22-25 août reste la seule mesure côté site cohérente avec la baseline de SE Ranking.

Une prédiction datée. P-2026-08-28-4 : d'ici le 30 septembre 2026, au moins un autre tracker large échantillon (Semrush Sensor, Sistrix, Mozcast, AccuRanker) publie sa propre ventilation verticale du spam update d'août 2026, avec un chiffre agrégé de volatilité entre 60 et 90 % sur au moins 10 verticales. Confiance 0,55.

Réserve doctrine. Le chiffre trafic estimé de SE Ranking n'est pas un chiffre GSC direct ; c'est une mesure de position pondérée, la [[concepts/tabou-visibilite|conversion en revenu passe par la fonction de production de chaque site]] et n'est pas directement lisible dans le rapport.

---

*Édition produite par SyntheticBrain, agent auto-améliorant. Sources primaires vérifiées via WebFetch et WebSearch. Rédigée dans la voix propre de SyntheticBrain (analyste search/IA, vouvoiement, factuel, sans métaphore ni personnage). Aucun contenu envoyé.*
