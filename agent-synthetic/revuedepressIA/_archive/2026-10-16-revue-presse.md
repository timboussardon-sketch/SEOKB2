---
type: revue-presse
title: "Algorithme — édition du 16 octobre 2026"
date: 2026-10-16
pilier_info_du_jour: Actualité SEO
author: SyntheticBrain
tags: [revue-presse, actualite-seo, ai-mode, ai-overviews, universal-cart, agentic-search, geo]
---

# Algorithme — 16 octobre 2026

**En résumé**

- Google ajoute pour la troisième fois en 2026 des liens dans AI Mode et AI Overviews, sans donner aux éditeurs la donnée de clics par surface.
- Universal Cart passe en production aux États-Unis dans Google Search et dans l'application Gemini, un panier qui porte des articles de plusieurs marchands.
- Google teste une barre latérale AI Mode sur la page des résultats classiques, remontée par Search Engine Roundtable le 14 octobre.
- Google Dataset Search ne retourne plus de résultats depuis le 15 octobre, panne non communiquée publiquement.
- Trois rollouts côté Google en vingt-quatre heures, et toujours aucune donnée de performance séparée par surface pour mesurer leur effet.

## Info du jour — Actualité SEO : Google ajoute encore des liens dans AI Mode et AI Overviews, sans donnée de clics pour les éditeurs

Le 15 octobre 2026, Google a publié sur son blog officiel une mise à jour de la façon dont les liens apparaissent dans AI Mode et dans AI Overviews. L'annonce est signée par Hema Budaraju, VP, Product Management pour Search ([Google blog](https://blog.google/products-and-platforms/products/search/updates-ai-mode-overviews-explore-web/)). Elle est reprise le même jour par [9to5Google](https://9to5google.com/2026/10/15/google-ai-mode-overviews-links/) sous la signature d'Abner Li à 9h00 heure du Pacifique, par [Search Engine Land](https://searchengineland.com/google-updates-ai-mode-and-ai-overview-with-more-links-context-carousels-and-information-on-creators-496242) et par [Search Engine Roundtable](https://www.seroundtable.com/) sous l'intitulé « Google Updates Links In AI Mode & AI Overviews Again, Won't Show Click Data » (15 octobre 2026, 12h).

Cinq changements sont annoncés. Deux sont déployés : des liens posés directement à côté du texte qu'ils soutiennent et plus souvent en haut de la réponse, et une refonte de la zone « Dive Deeper » en bas de certaines réponses, avec miniatures et design plus cliquable. Trois sont au stade du test : une section dédiée en tête de certaines réponses qui met en avant la source officielle d'une tâche ou d'une information, un court texte d'explication à côté de chaque lien qui dit pourquoi il est utile, et des noms de créateurs ou d'éditeurs cliquables sur les résultats vidéo d'AI Mode, qui renvoient vers des profils Search. Les carrousels d'articles et les Preferred Sources, déjà déployés plus tôt en 2026, s'étendent à plus de langues et de pays, et Google indique une multiplication par sept de l'usage de la personnalisation depuis le lancement initial.

C'est la troisième vague de changements de la zone de citation en six mois : [Google avait annoncé le 6 mai 2026](https://9to5google.com/2026/05/06/google-ai-mode-overviews-direct-links/) une première série de cinq ajustements (liens inline, prévisualisation au survol, labels d'abonnement, perspectives issues des forums, section « Explore new angles ») puis, le [9 mai sur Search Engine Journal](https://www.searchenginejournal.com/google-expands-ai-search-links-without-new-click-data/574307/), Matt G. Southern avait documenté que l'opération ajoutait des surfaces de liens mais aucune donnée de clics séparée. Le texte publié hier reconduit cette asymétrie : Google augmente la place accordée aux liens dans la réponse générative, et Search Console ne distingue toujours pas les clics venus d'AI Mode, d'AI Overviews et des résultats classiques.

Le fait est triple. Un, Google documente officiellement un travail d'attribution plus visible côté interface, avec des surfaces nouvelles pour les sites officiels, les créateurs et les carrousels d'actualité. Deux, Google renonce de nouveau à exposer les clics correspondants dans Search Console, alors que le rapport Performance des fonctions IA, ouvert en juin 2026 avec impressions, pages, pays, appareils et dates, ne contient toujours pas de dimension clics ni CTR. Trois, le rapport ne distingue pas non plus l'origine du clic quand il existe : un clic qui part d'un lien inline dans AI Overviews et un clic qui part d'un résultat organique classique arrivent dans la même colonne. L'éditeur ne peut donc pas répondre à la question qui conditionne toute décision éditoriale ou technique : la surface d'AI Overviews a-t-elle amené du trafic, lequel, et sur quel contenu.

**Lecture pour le consultant.** La décision opérationnelle se déplace vers trois questions, chacune cadrée par la doctrine [[concepts/metriques-visibilite-geo]] et [[concepts/tabou-visibilite]] :

1. **Mesurer sans la mesure officielle.** Les métriques déjà documentées (Imp_wc, Imp_pos et Subjective Impression chez Aggarwal, part de citations, part de voix cross-engine) restent utiles pour cadrer la présence côté réponse générative, pas pour attribuer un clic. Toute promesse de « visibilité IA » qui mélange présence et performance tombe sous [[concepts/tabou-visibilite]].
2. **Reconsidérer les Preferred Sources et la section pages officielles.** Google ouvre une surface explicitement adossée à la source la plus légitime pour une tâche donnée. Pour une marque, cela redevient un chantier d'identité numérique (fiche, profil, autorité documentée), proche de la logique [[concepts/structural-information-geo]], mesurable avant tout par des audits manuels des réponses.
3. **Préserver les flux non-AI.** Faute de signal d'attribution côté AI Mode, la mesure propre des contenus continue d'exister sur les requêtes où AI Overviews ne se déclenche pas et sur les requêtes locales ou transactionnelles où il reste minoritaire. Les décisions de calendrier éditorial et de maillage se prennent sur ce segment-là, en attendant qu'une donnée réelle sorte.

Trois réserves. Les testing features (section pages officielles, texte d'explication des liens, créateurs cliquables sur vidéo) peuvent ne pas aller jusqu'au déploiement, Google ne garantit rien dans son texte. Les carrousels de Preferred Sources étendent une personnalisation côté utilisateur, pas une sélection éditoriale côté résultat : le chiffre « multiplié par sept depuis le lancement » cité par Hema Budaraju n'est pas détaillé en volume absolu, en pays, ni en catégorie d'utilisateur, et aucun cabinet indépendant ne l'a répliqué à ce stade. Enfin, l'ensemble de ces changements concerne les surfaces visibles. Il ne dit rien du mécanisme de sélection sous-jacent, de la logique de fan-out, ni du poids que la refonte d'octobre 1er-2 de la documentation Google ([décrite par Lily Ray le 4 octobre 2026](https://ppc.land/google-ai-overviews-cut-self-ranking-listicle-citations-38-lily-ray-finds/)) pèse sur la liste des sources jugées éligibles.

**Trois prédictions ouvertes.**

1. P-2026-10-16-1 : aucun rapport Search Console ne distingue AI Mode, AI Overviews et classique d'ici au 31 mars 2027 (confiance 0,65).
2. P-2026-10-16-2 : un cabinet indépendant publie un recoupement de part de citations avant et après la vague d'octobre sur au moins 10 000 requêtes d'ici au 31 janvier 2027 (confiance 0,45).
3. P-2026-10-16-3 : les créateurs cliquables sur résultats vidéo d'AI Mode sortent du stade de test et deviennent le mode par défaut d'ici au 30 juin 2027 (confiance 0,35).

## Brèves

### Agentic Search — Universal Cart passe en production aux États-Unis dans Google Search et Gemini

Le 15 octobre 2026, Google a confirmé sur son [blog Shopping officiel](https://blog.google/products-and-platforms/products/shopping/universal-cart-launch/) le lancement d'Universal Cart aux États-Unis, dans Google Search (y compris AI Mode) et dans l'application Gemini. L'information est corroborée par [9to5Google](https://9to5google.com/2026/10/15/google-rolling-out-universal-cart-that-lets-you-shop-the-web-and-find-deals-with-gemini-search/), par [Search Engine Journal](https://www.searchenginejournal.com/google-universal-cart-store-handoff/593145/), par [PPC Land](https://ppc.land/googles-universal-cart-reaches-us-search-and-gemini-but-not-youtube/) et par [Relevant Audience](https://www.relevantaudience.com/ecommerce-marketing/google-universal-cart-launch-us-search-gemini/).

L'annonce portait sur ce qui avait été présenté à Google I/O le 19 mai 2026 : un panier qui porte des articles de plusieurs marchands, qui déclenche des alertes de baisse de prix et de retour en stock, qui affiche les codes promo disponibles, et qui propose une carte de paiement via Google Wallet selon les avantages. Deux chemins de finalisation coexistent, un paiement avec Google Pay à l'intérieur du panier, ou un transfert du contenu du panier vers le site du marchand où le checkout natif s'exécute. Le transfert est unidirectionnel et sans synchronisation. Le marchand reste merchant of record. YouTube et Gmail, cités en mai, ne font pas partie de ce rollout. L'intégration via le Merchant Center Integration Hub et le protocole UCP (Universal Checkout Protocol) sont déployés par phases, en programme d'accès anticipé.

Pour l'écosystème marchand, c'est le quatrième rail de checkout agentique visible en moins de deux semaines, après les trois annonces du 5 au 9 octobre (Constructor+Stripe, TikTok Shopping Assistant+Buy Direct, Rezolve RezolvePay) traitées dans l'[édition du 15 octobre après-midi](https://seroundtable.com/google-september-2026-spam-update-phase-3-42239.html). Universal Cart est la position Google : le panier et la découverte restent côté moteur, le checkout peut s'exécuter sur le site marchand. Rattachement doctrine à [[concepts/agentic-search]] (le point d'optimisation se déplace vers le catalogue produit et le flux Merchant Center) et à [[concepts/metriques-visibilite-geo]] (une 3e surface marchande est désormais sans donnée publique d'attribution).

Trois caveats. Un, Google ne communique pas la liste à jour des marchands actifs ni les volumes de transactions. Deux, les frais marchand, l'effet sur le classement produit et les clauses de partage de données ne sont pas documentés publiquement : les textes de Search Engine Journal et de PPC Land signalent explicitement l'absence de cette information. Trois, aucun chiffre d'adoption marchande ni de taux de conversion n'a été publié par un cabinet tiers non vendeur à ce stade.

### GEO / search IA — Google teste une barre latérale AI Mode sur la page des résultats classiques

Le 14 octobre 2026, [Search Engine Roundtable](https://www.seroundtable.com/) a documenté une forme d'affichage inédite : une barre latérale AI Mode intégrée à la gauche de la page des résultats classiques de Google Search. L'observation est pour l'instant mono-source (Barry Schwartz, screenshot et description). Elle n'est pas confirmée par un billet officiel de Google ni par une consigne publique.

Si le test se généralise, cela déplace AI Mode d'un onglet latéral vers un volet permanent au bord gauche. La conséquence directe pour un éditeur serait une réduction mécanique de la surface accordée aux dix liens bleus sur desktop. L'observation reste à ce stade un test, l'échantillon de déploiement n'est pas quantifié, et rien n'indique que la mise en page sera la même sur mobile. Rattachement doctrine à [[concepts/metriques-visibilite-geo]] (une 4e surface prend place sur la page de résultats, sans dimension dédiée dans Search Console).

### Niche SEO — Google Dataset Search ne retourne plus de résultats

Le 15 octobre 2026 à 21h37, [Search Engine Roundtable](https://www.seroundtable.com/) a signalé que Google Dataset Search (datasetsearch.research.google.com) ne retourne plus de résultats, sur plusieurs requêtes testées. Observation mono-source, et aucune communication officielle Google à cette heure, aucune mention sur le Search Status Dashboard.

Pour les équipes recherche, bibliothèques et data science qui dépendent du produit pour trouver des jeux de données structurés, l'interruption est opérationnelle : il faut provisoirement passer par les répertoires de datasets eux-mêmes (Kaggle, HuggingFace Datasets, Zenodo, data.gov) ou par la fonction Scholar. L'ancienneté éventuelle de la panne au moment du constat n'est pas documentée.

À suivre : une communication Google officielle (restauration, cause, calendrier), et une estimation indépendante de la durée.

---

*SyntheticBrain, édition 2026-10-16.*
