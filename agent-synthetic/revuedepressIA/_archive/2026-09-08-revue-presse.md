# Algorithme — édition du 8 septembre 2026

## Résumé en 4 points

- Web Bot Auth, la spécification qui permet à un agent IA de signer chaque requête HTTP avec une clé Ed25519 et à un site de vérifier la signature, est déjà vérifié en production par Cloudflare, AWS WAF, Akamai, HUMAN et Vercel, et signé côté agent par OpenAI ChatGPT, Anthropic Claude, Perplexity, Common Crawl et plusieurs bots Google, alors que l'IETF n'a formellement adopté aucun document du groupe de travail au 12 août 2026.
- La révision 02 du draft `draft-meunier-webbotauth-httpsig-protocol`, publiée le 18 août 2026, a modifié le format sur le fil du champ `Signature-Agent` (chaîne brute vers dictionnaire structuré) et fait passer le document sur la voie Standards Track ; les intégrations en production peuvent donc encore casser sur un changement de format futur.
- Bilan spam update d'août 2026 (SE Ranking, 100 000 mots-clés US, 20 verticales) : 16,71 % des URL top 10 sont sorties du top 100 sur le même mot-clé pendant les cinq jours de l'update, contre 9,2 % sur cinq jours de juillet sans update confirmée, soit une hausse relative de 82 % du taux de sortie du top 100.
- John Mueller, sur Bluesky le 6 septembre 2026 (rapporté 7 septembre par Search Engine Roundtable) : la SEO programmatique de basse valeur peut faire perdre à Google la confiance dans l'ensemble d'un site ; supprimer les pages en question ne suffit pas à récupérer la confiance perdue au niveau du domaine, la récupération demande du temps et un effort de démonstration de valeur, à un niveau comparable aux sorties de spam ou d'update core.

---

## Info du jour — Web Bot Auth : la vérification cryptographique des agents IA a franchi le seuil d'adoption production sans passer par l'IETF

Pilier : Recherche agentique.

Web Bot Auth est une spécification qui permet à un agent IA d'attacher une signature cryptographique à chaque requête HTTP qu'il émet, et à un site ou un CDN de vérifier cette signature avant de servir la ressource. Le mécanisme repose sur trois briques : une paire de clés Ed25519 générée par le fournisseur d'agent, la clé publique servie à un emplacement `well-known` sur son domaine, et une signature HTTP au format RFC 9421 (HTTP Message Signatures) portée par le header `Signature-Agent` sur chaque requête sortante ([Cloudflare docs, Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/), [IETF draft-meunier-webbotauth-httpsig-protocol-02, 18 août 2026](https://datatracker.ietf.org/doc/draft-meunier-webbotauth-httpsig-protocol/)).

L'objet couvert est différent de celui de `robots.txt` : `robots.txt` déclare une intention de l'éditeur (« ce bot n'est pas autorisé ici »), Web Bot Auth prouve l'identité de l'émetteur (« cette requête provient bien de ChatGPT ou de Perplexity, pas d'un scraper qui se déguise en ChatGPT »). L'un et l'autre se cumulent dans une politique de filtrage.

Cinq faits factuels ressortent au 8 septembre 2026.

Un, cinq fournisseurs d'infrastructure vérifient les signatures Web Bot Auth en production : Cloudflare, AWS WAF, Akamai, HUMAN et Vercel. Côté fournisseurs d'agents IA, cinq acteurs signent leurs requêtes avec la spécification : OpenAI (ChatGPT), Anthropic (Claude), Perplexity, Common Crawl, et plusieurs bots Google. Cloudflare a intégré Web Bot Auth à son programme Verified Bots, vérification active sur les plans Free et Pro, en cours d'extension sur Business et Enterprise ([nerdleveltech.com, 2026](https://nerdleveltech.com/web-bot-auth-ietf-standard-agent-verification), [contextbolt.com, Web Bot Auth explication](https://contextbolt.com/blog/web-bot-auth/)).

Deux, l'IETF n'a formellement adopté aucun document du groupe de travail Web Bot Auth au 12 août 2026 : le groupe n'a que des drafts individuels, dont le protocole (`draft-meunier-webbotauth-httpsig-protocol-02`, 18 août 2026), l'architecture (`draft-meunier-web-bot-auth-architecture-05`) et un registre (`draft-meunier-webbotauth-registry-01`). Les vérifications en production précèdent donc la stabilisation du standard ([IETF datatracker, protocole](https://datatracker.ietf.org/doc/draft-meunier-webbotauth-httpsig-protocol/), [IETF, architecture-05](https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture)).

Trois, la révision publiée le 18 août 2026 (v02) a modifié le format sur le fil du header `Signature-Agent`, passé d'une chaîne brute à un dictionnaire structuré, et l'ensemble a été placé sur la voie Standards Track. Le corollaire opérationnel est nommé explicitement dans une analyse externe : les intégrations qui vérifient les signatures aujourd'hui peuvent avoir à mettre à jour leur parseur si le format bouge encore avant la publication en RFC. Le risque de rupture est réel mais localisé au parseur, pas à la couche cryptographique ([nerdleveltech.com, 2026](https://nerdleveltech.com/web-bot-auth-ietf-standard-agent-verification)).

Quatre, le mécanisme a été conçu pour être compatible avec une politique de tarification à l'accès. AWS a livré le 15 juin 2026 une capacité de monétisation du trafic IA au niveau du edge : le propriétaire de contenu fixe un prix par catégorie de bot et par niveau de vérification, la facturation utilise les signatures Web Bot Auth pour authentifier le bot avant de compter la requête. Cloudflare fait le même choix côté publisher avec son offre Pay Per Crawl. La couche identité (Web Bot Auth) devient la brique qui rend techniquement possible la couche prix ([contextbolt.com](https://contextbolt.com/blog/web-bot-auth/), [Cloudflare, principes AI bot](https://blog.cloudflare.com/building-a-better-internet-with-responsible-ai-bot-principles/)).

Cinq, la spécification traite un point que ni `robots.txt` ni le blocage par User-Agent ne traitent : l'usurpation. Un scraper qui envoie un header `User-Agent: ChatGPT/1.0` est indistinguable, à cette couche, d'un vrai ChatGPT. Web Bot Auth impose que l'agent prouve la possession de la clé privée correspondant à la clé publique publiée sur le domaine officiel du fournisseur. Sans possession de la clé privée, la signature ne se calcule pas. Le contrôle passe donc d'un déclaratif (User-Agent) à une preuve cryptographique.

Trois lectures doctrinales pour un consultant SEO/GEO qui accompagne un éditeur, une agence ou une plateforme.

Un, la doctrine [[concepts/agentic-search]] gagne un point d'ancrage empirique : la couche identité des agents est en train de se standardiser dans les faits, chez les cinq principaux CDN et WAF, avant d'être stabilisée dans un RFC. Un site qui met en place une politique différenciée par type de bot (crawler d'entraînement, agent d'utilisateur en session, indexeur de moteur classique) dispose d'une preuve d'identité vérifiable pour chaque catégorie. La règle de filtrage cesse d'être fondée sur un User-Agent que n'importe qui peut usurper.

Deux, la doctrine [[concepts/arbitrage-plateforme-publication]] est directement modifiée : un éditeur qui héberge derrière Cloudflare peut activer Web Bot Auth pour distinguer les bots signés des bots non signés, puis appliquer une politique différente aux deux. Pratique : un vrai ChatGPT signé peut être autorisé à lire une page (pour citation), alors qu'un scraper qui se fait passer pour ChatGPT sera bloqué sur la même page. La signification opérationnelle d'un bloc `User-agent: ChatGPT` dans `robots.txt` change : elle ne s'applique plus à un fantôme, mais à un émetteur identifié.

Trois, la doctrine [[concepts/data-proprietaire]] tient sur un mécanisme de plus : si la couche paie-par-usage se met en place (AWS, Cloudflare Pay Per Crawl), les sites dont les données propres nourrissent régulièrement les citations IA peuvent capturer une facturation directe des agents qui viennent lire ces données. Cela suppose que le site publie une politique de tarification lisible par le bot et vérifie les signatures. La brique identité (Web Bot Auth) précède la brique monétisation.

Cinq lectures opérationnelles.

Un, auditer côté publisher si le CDN utilisé (Cloudflare, AWS CloudFront + WAF, Akamai, Vercel) supporte déjà Web Bot Auth et l'active par défaut. Chez Cloudflare, la vérification est incluse dans le programme Verified Bots, activation dans le tableau de bord Security.

Deux, pour un site qui bloque déjà les crawlers IA par User-Agent, remplacer la règle par une politique à deux niveaux : autoriser les requêtes signées Web Bot Auth avec la clé publique reconnue (ChatGPT, Claude, Perplexity, Common Crawl), bloquer les requêtes non signées portant le même User-Agent. La règle est plus fine et supprime le risque de bloquer des requêtes légitimes.

Trois, pour un fournisseur d'agent IA en cours de déploiement (agent SaaS vertical, plugin agent B2B), publier une clé publique à un `well-known` sur le domaine officiel de la solution et signer les requêtes sortantes selon `draft-meunier-webbotauth-httpsig-protocol-02`. C'est un pré-requis pour être reconnu comme trafic légitime par les cinq CDN cités et éviter d'être classé en trafic « unknown » qui déclenche les défenses.

Quatre, surveiller l'évolution du format `Signature-Agent` (chaîne vers dictionnaire structuré à la v02). Un site qui vérifie les signatures aujourd'hui a intérêt à isoler le parseur du header dans un module dédié pour absorber une éventuelle rupture avant la RFC.

Cinq, articuler cette couche avec la politique commerciale : si le site veut monétiser l'accès des bots (via Cloudflare Pay Per Crawl, AWS AI monetization, ou une politique directe), la signature Web Bot Auth est la brique qui rend la facturation attribuable à un émetteur nommé, pas à un flux anonyme.

Trois hypothèses vérifiables dans les 3 à 6 prochains mois.

Un, l'IETF adopte formellement au moins un document du groupe de travail Web Bot Auth (protocole, architecture ou registre) avant le 31 mars 2027, avec statut Working Group Document publiquement enregistré (confidence 0,55).

Deux, le format `Signature-Agent` reste sur le dictionnaire structuré à la publication de la RFC finale, sans rupture supplémentaire par rapport à la révision 02 (confidence 0,50).

Trois, au moins un fournisseur d'agent IA supplémentaire hors des cinq déjà listés (OpenAI, Anthropic, Perplexity, Google, Common Crawl) publie une clé Web Bot Auth et signe ses requêtes en production avant le 31 décembre 2026 (confidence 0,60).

---

## Brève B1 — Bilan spam update août 2026 : hausse relative de 82 % du taux de sortie du top 100

Pilier : Actualité SEO.

L'update spam d'août 2026 s'est déployée du 18 au 21 août, sur 2 jours et 16 heures. SE Ranking a publié le 4 septembre 2026 une analyse portant sur 100 000 mots-clés US répartis sur 20 verticales, mesurée sur la fenêtre de déploiement et comparée à une fenêtre de cinq jours de juillet 2026 sans update confirmée ([Search Engine Land, Danny Goodwin, 4 septembre 2026](https://searchengineland.com/google-august-2026-spam-update-ranking-impact-485980), [SE Ranking data via DEV.to](https://dev.to/alifar/googles-august-2026-spam-update-brought-unusually-sharp-ranking-volatility-5bkn)).

Trois chiffres saillants.

Un, 16,71 % des URL classées top 10 sur un mot-clé sont sorties du top 100 sur le même mot-clé pendant les cinq jours de l'update, contre 9,2 % sur une fenêtre de cinq jours de juillet 2026 sans update confirmée. La hausse relative est de 82 % (SE Ranking, panel 100 000 mots-clés US, 20 verticales).

Deux, la volatilité est distribuée sur les 20 verticales du panel, sans qu'aucune tactique de spam ni aucune catégorie de site ne soit disproportionnellement impactée selon la mesure. SE Ranking documente que le motif spam-cible-ciblée-vertical ne ressort pas.

Trois, dans le même mesure, 12 % des URL classées top 3 après l'update ne figuraient pas au top 20 avant. Un mouvement d'entrée dans le top 3 documenté, pas seulement des sorties.

Glenn Gabe a publié le 4 septembre 2026 une série d'études de cas sur son blog GSQI (scaled content abuse, contenu IA, SEO programmatique, thin affiliates) qui documente le profil des sites impactés au niveau du contenu et de la structure. La correspondance entre les motifs Gabe et les 20 verticales SE Ranking n'est pas quantifiée à ce jour ([Glenn Gabe, GSQI blog, 4 septembre 2026](https://www.gsqi.com/marketing-blog/august-2026-google-spam-update-case-studies/)).

Deux réserves méthodologiques. La mesure SE Ranking porte sur des mots-clés US uniquement, pas transposable aveuglément aux SERP EU. La comparaison entre une fenêtre d'update et une fenêtre sans update ne contrôle pas les saisonnalités de recherche entre juillet et août, qui peuvent expliquer une part résiduelle de la volatilité mesurée.

La doctrine [[concepts/metriques-visibilite-geo]] impose d'ajouter deux mesures à un audit post-update pour un client : la part de mots-clés du panel client où le rang a été perdu au-delà du top 100, et la part de mots-clés où un nouveau site est entré dans le top 3. Un audit qui ne mesure que le rang moyen manque le mouvement structurel documenté par SE Ranking.

---

## Brève B2 — Google Ads teste les match types restrictifs en AI Mode, la frontière organique-payant dans la réponse générative bouge

Pilier : Business SEO.

Ginny Marvin, Google Ads Liaison, a confirmé le 4 septembre 2026 sur les réseaux sociaux le lancement d'une petite expérimentation : les campagnes Search classiques bâties sur les match types exact et phrase peuvent servir des annonces texte à l'intérieur d'AI Mode. Avant cette expérimentation, la seule voie d'accès aux emplacements publicitaires d'AI Mode passait par AI Max, Performance Max pour Search, ou broad match avec Smart Bidding ([Search Engine Land, Ginny Marvin, 4 septembre 2026](https://searchengineland.com/google-tests-traditional-search-campaigns-in-ai-mode-487199), [PPC Land, exact et phrase en AI Mode](https://ppc.land/exact-and-phrase-match-keywords-gain-ai-mode-ads-in-google-test/), [Search Engine Roundtable, 4 septembre 2026](https://www.seroundtable.com/google-ads-serving-restrictive-match-types-ai-mode-42024.html)).

Trois faits documentés.

Un, l'expérimentation a été présentée comme récente et de petite ampleur, sans engagement Google sur une bascule permanente ni sur le pourcentage de trafic couvert. Marvin a précisé que le périmètre est cantonné aux requêtes portant une intention utilisateur explicite et directe, sans définition publique du critère.

Deux, le changement de paradigme opérationnel est net pour un acheteur de publicité Google : jusqu'à présent, l'exact et le phrase match ont servi de mécanisme volontaire pour garder le budget hors des surfaces IA que l'annonceur ne voulait pas viser. Si l'expérimentation devient une bascule stable, l'apparition dans AI Mode cesse d'être un paramètre de campagne pour devenir une propriété de la requête et de l'intention détectée.

Trois, l'expérimentation coïncide avec deux autres tests documentés par PPC Land : deux emplacements shopping en AI Mode et une migration des Dynamic Search Ads vers AI Max au 1er septembre 2026 ([PPC Land, deux emplacements shopping AI Mode](https://ppc.land/google-tests-two-shopping-ad-placements-inside-ai-mode-results/)). Le mouvement documenté est convergent : Google pousse davantage de formats publicitaires vers AI Mode, en levant les garde-fous que les annonceurs utilisent aujourd'hui pour rester dehors.

La lecture doctrine [[concepts/arbitrage-plateforme-publication]] est directe : la frontière organique-payant dans la réponse générative est en cours de reconfiguration, non par une bascule publique mais par des expérimentations discrètes que l'annonceur constate a posteriori. La conséquence pratique pour un consultant qui accompagne un client sur son budget paid Google : ajouter dans le reporting mensuel un filtre par surface (résultat classique, AI Mode, AI Overviews) et surveiller l'apparition d'impressions payantes en AI Mode sur les campagnes exact et phrase qui n'auraient pas dû y apparaître avant ce test.

Une réserve : l'ampleur de l'expérimentation n'est pas publiée, et un test discret peut rester à ce stade sans généralisation. Le fait à retenir est la levée du filtre de type de match, pas la promesse d'une bascule.

---

*Édition produite par SyntheticBrain le 8 septembre 2026. Format 1 info du jour + 2 brèves, 31e édition consécutive. Draft interne, non publié.*
