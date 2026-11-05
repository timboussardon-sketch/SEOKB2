---
date: 2026-11-01
pilier: product-led-seo
edition: matin
author: SyntheticBrain
---

# Marie Haynes dit aux SEO d'arrêter d'optimiser pour les LLM et de construire des apps que Google connectera à ses résultats

## L'essentiel en 15 secondes

- Marie Haynes publie le 21 octobre un bilan GA4 sur 12 mois, 100 sites et 145 millions de sessions : les sessions depuis ChatGPT représentent 0,62 % du volume Google organique ; tous LLM confondus, 0,73 %.
- Sur le sous-échantillon de 55 sites qui mesurent la conversion, ChatGPT convertit à 13,8 % contre 3,02 % pour Google organique, mais produit 36 conversions mesurées contre 964 pour Google organique.
- Dans sa newsletter du 29 octobre, elle recommande aux SEO de construire des services que Google raccorde à ses résultats via le Connected Apps Platform ouvert aux développeurs le 28 octobre, plutôt que de poursuivre l'optimisation des citations LLM.
- Google, Bing, OpenAI et Anthropic s'alignent sur un signal commun `__usage_ai-training` dans robots.txt porté par un draft IETF ; Google prévoit la prise en charge début 2027, Bing la fait démarrer le 1er février 2027.
- Bluefish, éditeur basé à New York, revendique 35 % de divergence entre Google et ChatGPT sur la marque leader à travers 5 810 sujets d'achat ; méthodologie non publiée, à traiter comme donnée vendeur non vérifiable.

## Info du jour — Marie Haynes recommande de construire des apps, pas d'optimiser des citations LLM (pilier Product-Led SEO)

Marie Haynes est consultante SEO en Ontario depuis plus de quinze ans et édite une newsletter suivie dans le milieu. Elle vient de publier coup sur coup trois textes qui tiennent la même ligne. Le 21 octobre, un billet de blog intitulé « GEO is a distraction » ([Marie Haynes, 2026-10-21](https://www.mariehaynes.com/geo-is-a-distraction/)) argumente, données GA4 à l'appui, que l'optimisation pour les citations LLM capte très peu de trafic et détourne les ressources SEO d'un terrain à plus fort rendement. Le 29 octobre, sa newsletter décrit le Google Connected Apps Platform annoncé la veille comme « l'une des choses les plus importantes sur lesquelles nous travaillerons au cours des prochaines années » et appelle les lecteurs à construire ([ppc.land, 2026-11-01](https://ppc.land/marie-haynes-tells-seos-to-build-google-search-apps-instead-of-chasing-geo/)). Le 30 octobre, dans un retour sur l'earnings call Alphabet du Q3 2026 ([Marie Haynes, 2026-10-30](https://www.mariehaynes.com/googles-q3-2026-earnings-call-search-ai-are-merging-into-one-unified-product/)), elle relie Connected Apps à l'intégration AI Overviews + AI Mode + recherche traditionnelle en un seul produit telle que décrite par les dirigeants Google.

### La donnée qui porte l'argument

Le billet du 21 octobre s'appuie sur un panel de 100 sites agrégés dans GA4 sur 12 mois, soit plus de 145 millions de sessions. Deux constats quantifiés :

- **Volume**. Les sessions provenant de ChatGPT représentent 0,62 % du volume issu de Google organique sur l'ensemble. L'addition de tous les LLM référents monte à 0,73 %. L'auteure indique que la croissance des référents ChatGPT a plafonné autour de la sortie de GPT-5 en août 2025, puis décliné.
- **Conversion**. Sur les 55 sites du panel qui mesurent effectivement un événement clé dans GA4, le taux de conversion médian atteint 13,8 % pour les visiteurs ChatGPT contre 3,02 % pour Google organique, soit un facteur supérieur à 4,5. Mais en absolu, Google organique produit 964 conversions mesurées contre 36 pour l'ensemble des LLM, et 96,5 % des conversions totales. L'auteure signale explicitement que 45 des 100 sites n'enregistrent aucun événement clé dans GA4, et que 36 conversions reste un échantillon étroit.

Interprétation portée par Marie Haynes : un chiffre de conversion élevé rapporté à un volume dérisoire ne justifie pas d'y verser une part importante du budget SEO, surtout quand la mesure elle-même repose sur un échantillon restreint. Elle qualifie l'optimisation pour les citations LLM de « distraction » par rapport à l'enjeu qu'elle juge principal : préparer les sites à l'écosystème agentique qui se construit à l'intérieur de la recherche Google.

### Ce qu'elle propose à la place

La ligne reprise dans la newsletter du 29 octobre, telle que relayée par ppc.land, se formule ainsi : « la vraie opportunité en AI Search va être que les gens utilisent votre entreprise directement depuis les résultats de Google ». Et plus loin : « commencez à réfléchir à ce que votre entreprise offre que les gens vont vouloir utiliser avec leurs agents. Puis exercez-vous à le construire ».

Le mécanisme concret est le Google Connected Apps Platform, dont Google a ouvert la preview aux développeurs le 28 octobre via la Connected Console. Les apps y sont enregistrées en MCP et déclarées sur une surface (AI Mode d'abord), les utilisateurs peuvent les ajouter depuis les paramètres de recherche, puis les appeler en langage naturel dans une requête. Google ouvre à ce stade l'inscription à cinquante partenaires nommés (Adobe, Experian, Localiza, Peloton, Calm entre autres) et au programme développeur public.

John Mueller, cité par Marie Haynes depuis un commentaire LinkedIn, qualifie le Connected Apps Platform de « search platform » et précise que c'est « encore extrêmement tôt ». Il indique ne pas travailler sur ce produit et que son commentaire est personnel.

### Les limites à poser sur cet argument

Trois caveats que l'édition retient avant d'en faire un signal fort.

- **Portée de la mesure GA4**. Les référents LLM dans GA4 sont connus pour être sous-mesurés, car tous les clics issus d'une réponse générative n'arrivent pas avec un referrer identifiable ; une partie passe en « direct ». La valeur comparative 0,62 % reste donc un plancher plutôt qu'un chiffre absolu. L'auteure ne discute pas cette limite dans son billet.
- **Spécificité du panel**. 100 sites agrégés par un cabinet SEO ne constituent pas un panel aléatoire. La composition sectorielle n'est pas publiée. Un panel orienté e-commerce, par exemple, surpondérerait des requêtes transactionnelles où ChatGPT envoie peu ; un panel orienté B2B software renverrait sans doute une part ChatGPT supérieure.
- **Scope du Connected Apps Platform**. La documentation Google limite pour l'instant la surface aux utilisateurs US, en anglais, dans AI Mode, et à cinq apps grand public au départ du consumer rollout du 16 juillet 2026 (Spotify, Google Hotels, Google Flights, YouTube, AllTrails). Le programme développeur de self-service est accessible, mais rien dans la documentation publique ne garantit la validation d'une app soumise, les critères de sélection, ni le routage entre apps concurrentes sur une même requête. Construire sous cette hypothèse engage une ressource ingénierie en pariant sur une surface Google dont les métriques opérationnelles et la carte des arbitrages ne sont pas documentées.

### Lien doctrine

Trois concepts du vault se branchent directement sur cet épisode.

- [[concepts/product-led-seo]] pose depuis l'origine que la page SEO forte est celle dont le produit lui-même tient la valeur, pas le texte qui l'entoure. L'extension logique à l'ère agentique est que le « produit SEO » devienne un service appelable par un agent, pas seulement une interface humaine. La position de Marie Haynes est précisément cette extension : construire un service que l'agent (celui de Google ou un agent tiers passant par MCP) appelle au moment d'exécuter une tâche. Le test de substitution par un LLM, défensif, se double d'un test de délégation à l'agent, offensif.
- [[concepts/agentic-search]] décrivait le passage « requête → réponse IA → (parfois) clic → site » comme un paradigme à préparer. Le Connected Apps Platform instancie cette préparation côté infrastructure : le site n'est plus seulement un contenu à référencer, mais un service déclaré sur une plateforme, avec un contrat MCP et une surface d'arbitrage. L'enjeu passe de « être trouvé » à « être sélectionné pour exécuter une tâche ».
- [[concepts/tabou-visibilite]] se trouve renforcé par les chiffres de Marie Haynes. Mesurer la conversion absolue (36 contre 964) plutôt que la citation ou la mention LLM aligne la décision budgétaire SEO sur le chiffre d'affaires, exactement comme Tim l'énonce depuis les calls prospects : la métrique de pilotage reste « leads » ou « conversion », pas « visibilité ».

### Prédiction

**P-2026-11-01-1**. D'ici fin mars 2027, au moins un cabinet SEO indépendant publiera une mesure GA4 ou GA équivalent sur un panel autre (≥ 50 sites, ≥ 6 mois) comparant volume et conversion des référents LLM contre Google organique, avec un rapport volume LLM/Google ≤ 2 % et un rapport conversion absolue LLM/Google ≤ 10 %. Confidence 0,55. Résolution 2027-03-31.

**P-2026-11-01-2**. D'ici fin juin 2027, Google rendra public au moins un critère opérationnel de sélection d'une app sur Connected Apps Platform quand plusieurs apps concurrentes couvrent la même requête (ordre d'apparition, score de pertinence, poids d'une préférence utilisateur enregistrée). Confidence 0,4. Résolution 2027-06-30.

## Brèves

### Google, Bing, OpenAI et Anthropic s'alignent sur un signal robots.txt commun pour l'opt-out IA (pilier Actualité SEO)

Le 30 octobre, Google a annoncé rejoindre un signal robots.txt partagé pour exprimer la préférence d'opt-out de l'entraînement IA, porté par l'IETF ([Search Engine Roundtable, 2026-10-30](https://www.seroundtable.com/google-ai-training-control-42430.html), [ppc.land, 2026-10-31](https://ppc.land/google-and-bing-back-one-robots-txt-rule-to-opt-out-of-ai-training/)). La directive utilise un user-agent symbolique, `__usage_ai-training`, listé sur la page Google Common Crawlers Fetchers ([developers.google.com](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)). Un site qui écrit `User-agent: __usage_ai-training` suivi de `Disallow: /` demande aux moteurs qui honorent le signal de ne pas utiliser son contenu pour entraîner leurs modèles. John Mueller précise que si un site utilise le token sans spécifier Google-Extended, Google traitera le signal comme une interdiction de Google-Extended. Les contrôles existants restent valides en parallèle.

Côté calendrier :

- Google prévoit la prise en charge « early 2027 », date reprise dans son blog Search Central ([developers.google.com/search/blog, 2026-10-30](https://developers.google.com/search/blog/2026/10/ai-training-control)).
- Bing honore ces préférences côté crawl à partir du 1er février 2027, et laisse jusqu'au 1er mars 2027 aux sites utilisant NoArchive ou NoCache pour configurer les nouveaux réglages, selon l'annonce reprise par ppc.land.
- OpenAI a publié un engagement propre à soutenir le signal.
- Search Engine Roundtable rapporte qu'Anthropic participe également, sans vérification indépendante.

Le texte de référence est le draft IETF `draft-kelley-aipref-training-preference-signal` ([IETF Datatracker](https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/)), qui n'est pas encore un standard. Les signataires s'engagent sur le fait de reconnaître le signal, pas sur une définition commune de ce que recouvre « entraînement », distinction importante côté publication : un même disallow pourra être traité différemment pour l'entraînement initial, pour le fine-tuning et pour le grounding au moment d'une réponse.

Implication SEO : à partir du 1er février 2027, un disallow sur ce user-agent devient le levier unique applicable aux quatre acteurs cités. Pour un éditeur qui souhaite distinguer l'usage pour l'entraînement (plutôt bloquer) et l'usage pour le grounding de réponse (plutôt autoriser pour rester cité), aucune granularité n'est garantie par le draft actuel. À surveiller à mesure que la rédaction IETF se stabilise.

### Bluefish annonce 35 % de divergence Google/ChatGPT sur la marque leader (pilier GEO/search IA)

Bluefish, société fondée en 2024 à New York, revendique dans une communication produit datée du 27 octobre 2026 qu'« à travers 5 810 sujets d'achat répartis en 3 catégories, Google et ChatGPT nomment une marque leader différente dans 35 % des cas » ([ppc.land, 2026-11-01](https://ppc.land/chatgpt-and-google-differ-on-top-brand-in-35-of-buying-topics-bluefish-says/)). La société vend une Agentic Marketing Platform (AMP) qui surveille la visibilité organique de marque dans les réponses IA et étend le 27 octobre son offre vers les paid media briefs générés pour Google AI Max, Performance Max et ChatGPT ad slots.

Statut à retenir : le chiffre de 35 % est présenté dans l'annonce du produit, pas dans un rapport méthodologique public. Ni la liste des trois catégories, ni la surface Google interrogée (AI Overviews, AI Mode ou Gemini), ni les dates de collecte, ni la définition de « marque leader » (première mention, recommandation explicite, fréquence majoritaire) ne sont documentées. L'édition retient donc ce chiffre comme donnée vendeur non vérifiable, utile pour signaler qu'une divergence existe entre moteurs sur l'intention commerciale, mais pas comme mesure référencable dans une doctrine SEO.

Ce résultat se place dans la série déjà notée côté SyntheticBrain : étude Averi mesurant un chevauchement de citations limité entre ChatGPT et Perplexity (680 M données, édition 2026-05-30-v5), analyses Peec de février 2026 (90 % des URL ont un taux de citation inférieur à 1,0 dans AI Mode, 64 % des URL Perplexity ne sortent jamais de la sidebar). Cette série converge sur un fait de scénario : les moteurs génératifs sélectionnent des marques différentes pour une même intention. La taille de l'écart et les conditions dans lesquelles il se produit restent, elles, en construction.

### Google étudie le retour du paramètre `&num=100` dans la recherche (pilier Actualité SEO)

Le 30 octobre, Barry Schwartz rapporte que Google pourrait être en train de ramener le paramètre `&num=100`, qui permettait d'afficher jusqu'à 100 résultats sur une seule page de résultats de recherche ([Search Engine Roundtable, 2026-10-30](https://www.seroundtable.com/google-search-100-search-results-parameter-back-42423.html)). Google a retiré ce paramètre en septembre 2025, ce qui avait fortement perturbé les trackers de rang (SISTRIX, Semrush, Ahrefs et autres) qui s'en servaient pour collecter des positions au-delà du top 10 à moindre coût.

Deux implications si le paramètre revient effectivement :

- Les séries de rang 11-100 collectées par les trackers vont redevenir cohérentes et comparables à celles d'avant septembre 2025, après plus d'un an de données partielles. Les analystes qui ont construit un modèle sur la fenêtre octobre 2025 → octobre 2026 pour corriger la perte de couverture devront vérifier que leur mesure reste calibrée.
- Si le paramètre revient sans contrepartie côté détection de bots, Google rouvre une vanne d'extraction automatisée qu'il avait choisi de fermer, ce qui soulèverait la question du moteur qui a motivé cette décision à ce stade du cycle AI Overviews.

À confirmer dans les jours qui viennent par une source Google ou par un test opérationnel sur `google.com/search?q=...&num=100`.

## Sources

- [Marie Haynes, « GEO is a distraction », 2026-10-21](https://www.mariehaynes.com/geo-is-a-distraction/)
- [Marie Haynes, « Google's Q3 2026 Earnings Call: Search & AI are merging into one unified product », 2026-10-30](https://www.mariehaynes.com/googles-q3-2026-earnings-call-search-ai-are-merging-into-one-unified-product/)
- [ppc.land, « Marie Haynes tells SEOs to build Google Search apps instead of chasing GEO », 2026-11-01](https://ppc.land/marie-haynes-tells-seos-to-build-google-search-apps-instead-of-chasing-geo/)
- [Search Engine Roundtable, « Google Adopts New AI Training Control », 2026-10-30](https://www.seroundtable.com/google-ai-training-control-42430.html)
- [ppc.land, « Google and Bing back one robots.txt rule to opt out of AI training », 2026-10-31](https://ppc.land/google-and-bing-back-one-robots-txt-rule-to-opt-out-of-ai-training/)
- [Google Search Central blog, « AI Training Control », 2026-10-30](https://developers.google.com/search/blog/2026/10/ai-training-control)
- [IETF Datatracker, draft-kelley-aipref-training-preference-signal](https://datatracker.ietf.org/doc/draft-kelley-aipref-training-preference-signal/)
- [ppc.land, « ChatGPT and Google differ on top brand in 35% of buying topics, Bluefish says », 2026-11-01](https://ppc.land/chatgpt-and-google-differ-on-top-brand-in-35-of-buying-topics-bluefish-says/)
- [Search Engine Roundtable, « Google Search May Be Bringing Back 100 Search Results Parameter », 2026-10-30](https://www.seroundtable.com/google-search-100-search-results-parameter-back-42423.html)

---

*Édition produite par SyntheticBrain. Rien n'a été envoyé. Draft à relire avant publication.*
