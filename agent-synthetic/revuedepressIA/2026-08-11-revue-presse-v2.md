---
date: 2026-08-11
edition: 2026-08-11-v2
pilier_info_du_jour: Actualite SEO
piliers_breves: [GEO, Actualite SEO]
capture_mode: native
draft: true
---

# Algorithme — édition du 11 août 2026 (v2)

*Draft SyntheticBrain. Analyste search / IA. Rien n'a été envoyé.*

## En 3 points

- Le rapport [Generative AI performance de Google Search Console](https://www.seroundtable.com/google-search-console-ai-report-live-41850.html) est passé le 11 août 2026 en accès universel : la fonction, réservée jusqu'ici à un sous-ensemble d'utilisateurs, est apparue dans toutes les propriétés vérifiées par [Barry Schwartz](https://anicca.co.uk/blog/weekly-update-search-marketing-11-08-2026/), sans annonce officielle de Google.
- Le rapport continue de ne pas publier les clics ni les requêtes, deux données pourtant nécessaires pour raccorder l'impression IA à un pipeline commercial.
- Une [étude SE Ranking publiée le 10 août sur 50 006 prompts commerciaux ChatGPT](https://seranking.com/blog/chatgpt-ads-study/) mesure 25,94 % de prompts avec publicité, 14,35 % de publicités hors-sujet et un domaine annonceur cité comme source dans 3,63 % des placements uniquement.
- [Roger Montti a testé le 11 août sur Search Engine Journal](https://www.searchenginejournal.com/wpforms-lite-accused-of-adding-backdoor-i-tested-it-and-was-surprised/585273/) l'accusation de backdoor visant WPForms Lite 2.0.0 et documente un assistant d'installation qui installe 3 plugins depuis un domaine tiers sans notification claire.

## Info du jour — Actualité SEO : le rapport Generative AI de Search Console arrive dans toutes les propriétés, sans clic ni requête

Le 11 août 2026, [Barry Schwartz a constaté sur Search Engine Roundtable](https://www.seroundtable.com/google-search-console-ai-report-live-41850.html) que le rapport « Generative AI performance » de Google Search Console est désormais visible dans toutes les propriétés qu'il administre. Le déploiement est arrivé sans communication officielle de Google : un simple bandeau au moment de la connexion pointe l'utilisateur vers la fonction, positionnée comme onglet dépliable sous le rapport Performance principal ([reprise Anicca, 11 août](https://anicca.co.uk/blog/weekly-update-search-marketing-11-08-2026/)).

Le rapport a été lancé en juin 2026 pour un sous-ensemble d'utilisateurs, d'abord au Royaume-Uni, puis étendu progressivement à d'autres pays début juillet. Le 11 août est la première fois où un observateur régulier de Search Console constate la présence du rapport sur l'intégralité de ses propriétés d'un seul coup. Google n'a pas publié de billet daté pour officialiser cette étape.

Les métriques exposées restent celles annoncées à la sortie : impressions dans les AI Overviews et AI Mode, pages, pays, appareils, dates avec granularité horaire, quotidienne, hebdomadaire, mensuelle. Deux données manquent toujours à l'appel et cette absence est le point que la sortie universelle du rapport ne résout pas : **le rapport ne remonte ni les clics ni les requêtes qui déclenchent l'affichage de la page dans une réponse IA**. Le fait est explicite depuis juin ; il n'est pas modifié par la sortie universelle du 11 août.

Pilier retenu **Actualité SEO** : le rapport est une fonction Google Search Console, pas un changement d'algorithme. L'interdiction du mono-sujet Google en info du jour ne s'applique qu'aux core updates et aux changements de classement. Un rapport de mesure ouvert à toutes les propriétés est un fait d'outil, pas de ranking.

**Ce que cela déplace pour un consultant SEO ou GEO**

1. **La couverture de mesure devient universelle, la lecture opérationnelle reste amputée.** Toute propriété Search Console peut désormais afficher un volume d'impressions dans les fonctions IA. C'est la première donnée Google en propre sur la présence d'une URL dans une réponse générative. Elle ne dit ni qui a cliqué, ni sur quelle formulation utilisateur la page est apparue. Le décrochage entre « impression IA côté Google » et « visite site » reste donc invisible en interne, sauf à croiser avec un outil externe qui mesure les citations et un outil d'analytics qui mesure le trafic référent IA. C'est le prolongement direct de la doctrine [[concepts/metriques-visibilite-geo]] : les métriques de citation finale (position, part de voix, densité) exposées ici par Google ne se relient pas encore à une variable de conversion tant que le clic manque.

2. **La colonne « impressions AI Overviews » de Search Console ne remplace pas un outil GEO.** Un outil GEO tiers (Semrush AI Visibility Toolkit, Ahrefs Brand Radar, Profound, Otterly, MaxAEO, Kasper côté marchand, Similarweb) mesure la formulation exacte de la requête, la position dans la citation, la présence dans plusieurs moteurs simultanément (ChatGPT, Perplexity, Gemini, Claude), la texture cross-modèle. Google Search Console expose uniquement la mesure sur ses propres surfaces (AI Overviews, AI Mode) et sans requête associée. Les deux jeux de mesure restent complémentaires, ne se substituent pas.

3. **Le raccord au pipeline commercial passe par un tiers.** L'absence de clic et de requête impose au consultant qui veut raccorder « présence IA » à « lead entrant » de croiser la donnée impression Search Console avec la donnée trafic référent GA4, filtrée sur les user-agents et paramètres UTM qui identifient un référent IA. Une fiche preuve [[concepts/data-proprietaire]] côté client passe par ce croisement, pas par la lecture directe du rapport Search Console. Concrètement, un audit de mandat SEO en 2026 doit désormais budgeter le temps de croisement entre trois sources non alignées entre elles (rapport GA IA côté Google, outil de mesure GEO tiers pour la formulation, trafic référent GA4).

**Limites à garder en tête**

- Google n'a pas publié de billet officiel daté du 11 août pour confirmer la sortie universelle. Le constat vient de la vérification empirique d'un observateur (Barry Schwartz) sur ses propres propriétés, reprise dans un billet secondaire ([Anicca weekly recap 11 août](https://anicca.co.uk/blog/weekly-update-search-marketing-11-08-2026/)). La bascule est cohérente avec le calendrier annoncé mais non estampillée par Google.
- Le rapport ne s'affiche pas si le site n'a pas reçu suffisamment d'impressions dans les fonctions IA. Un seuil non chiffré publiquement conditionne l'affichage. Un site sans présence IA peut donc avoir la fonction déployée sans voir de donnée.
- L'absence de clic n'est pas un choix technique passager mais une position déclarée dès juin par Google : le rapport ne fournira pas de donnée de clic depuis les réponses IA vers les sites. La sortie universelle du 11 août ne renverse pas cette position.
- Le rapport agrège en une seule métrique « generative AI » les impressions dans AI Overviews et AI Mode, sans séparer les deux surfaces. Un consultant qui veut isoler l'impact d'une intégration AI Mode spécifique doit passer par un outil tiers.

**Prédictions ouvertes issues de ce run**

- **P-2026-08-11-v2-1** : Google publie un billet officiel Search Central daté à moins de 30 jours du 11 août 2026 pour confirmer la sortie universelle du rapport Generative AI performance, avant le 10 septembre 2026. Confidence 0,40.
- **P-2026-08-11-v2-2** : le rapport Generative AI performance n'ajoute toujours pas de donnée de clic ni de requête à la fin de 2026. Confidence 0,80.
- **P-2026-08-11-v2-3** : un outil tiers de mesure GEO à large audience (Semrush, Ahrefs, Profound, Similarweb) publie avant le 31 mars 2027 un connecteur natif qui aligne le rapport Generative AI de Search Console avec sa propre mesure de citation par requête. Confidence 0,55.

## Brève 1 — GEO : SE Ranking mesure 25,94 % de prompts ChatGPT avec publicité et 14,35 % de publicités hors-sujet

Le 10 août 2026, [SE Ranking a publié](https://seranking.com/blog/chatgpt-ads-study/) une étude à grande échelle sur les publicités dans ChatGPT, portant sur 50 006 prompts commerciaux répartis en 20 verticales aux États-Unis, données collectées le 23 juillet 2026. La reprise éditoriale la plus lisible en dehors du billet primaire figure dans le [récapitulatif Anicca du 11 août](https://anicca.co.uk/blog/weekly-update-search-marketing-11-08-2026/).

Les chiffres clés extraits par SE Ranking :

- ChatGPT retourne une publicité sur **25,94 %** des prompts commerciaux mesurés. La fréquence est proche de celle de Google AI Mode (29,45 %) sur le même corpus.
- **14,35 %** des publicités affichées n'ont pas de relation topique mesurable avec la requête (score de similarité comparable à un appariement aléatoire).
- Les catégories les plus décalées : **News & Politics 54,2 %** hors-sujet, **Relationships 51,1 %**. Les mieux appariées : Pets 2,6 %, Travel 4,0 %, Healthcare 5,0 % (côté similarité). À noter que le taux d'apparition dans la santé sur ChatGPT (28,69 %) est près de dix fois supérieur à celui d'AI Mode (2,64 %).
- Le domaine de l'annonceur est cité comme source dans la réponse de ChatGPT dans **3,63 %** des placements (URL exacte : 0,09 %, 12 cas seulement). Autrement dit, dans 96,37 % des cas, la publicité paraît sans que la même page soit sourcée dans la réponse.
- Le corpus d'annonceurs est concentré : 1 159 annonceurs uniques, BestMoney concentre à lui seul 13,56 % des impressions publicitaires ChatGPT du dataset.

**Ce que cela déplace pour un consultant qui prépare un plan média ChatGPT**

- Le décrochage entre « publicité payée » et « citation organique dans la réponse » est un fait mesurable en 2026 : payer un placement dans une conversation ChatGPT ne place pas la marque dans la couche de citations utilisée pour construire la réponse. Les deux surfaces restent séparées à l'intérieur de la même interface. Ce point recoupe la doctrine [[concepts/tabou-visibilite]] : le mot « visibilité » aplatit un décrochage que la mesure sépare (apparition publicitaire vs citation organique dans la réponse).
- Le déséquilibre entre catégories rend un plan média « générique 20 verticales » inutilisable. Un annonceur santé travaille une surface où la publicité apparaît beaucoup plus souvent que la moyenne, un annonceur News & Politics travaille une surface où l'appariement est massivement dégradé. La stratégie descend au niveau de la verticale.
- La concentration BestMoney (13,56 % des placements sur 1 159 annonceurs) indique un marché encore dominé par un petit nombre d'acteurs installés. Un annonceur qui entre maintenant occupe une part de voix mesurable à faible coût de compétition.

Ligne d'attribution retenue : étude primaire vendeur (SE Ranking a un intérêt commercial à documenter le marché ChatGPT ads pour vendre ses outils AI Search Insights), corroborée par la reprise Anicca du 11 août. Chiffres extractibles ligne par ligne du billet primaire, méthodologie déclarée (dataset explicite, date de collecte), mais l'étude reste single-source par nature : une reproduction indépendante par un cabinet tiers (Adthena, Similarweb, Semrush) reste à venir avant de solidifier la mesure.

## Brève 2 — Actualité SEO : Roger Montti teste l'accusation de backdoor WPForms Lite et documente un assistant qui installe 3 plugins sans notification claire

Le 11 août 2026, [Sybre Waaijer, éditeur du plugin The SEO Framework, a publié une accusation](https://www.searchenginejournal.com/wpforms-lite-accused-of-adding-backdoor-i-tested-it-and-was-surprised/585273/) contre WPForms Lite version 2.0.0, en pointant un fichier `wpforms-lite/src/SetupWizard/Bridge.php` qui, selon lui, émet un jeton de connexion d'une heure permettant aux serveurs Awesome Motive d'installer et d'activer des plugins sans consentement explicite ni notification. Le plugin est installé sur plus de 5 millions de sites.

[Roger Montti, sur Search Engine Journal](https://www.searchenginejournal.com/wpforms-lite-accused-of-adding-backdoor-i-tested-it-and-was-surprised/585273/), a installé le plugin pour vérifier le comportement. Son test confirme qu'à l'exécution de l'assistant de configuration, l'utilisateur est redirigé vers `https://wpformsapi.com/setupwizard/v1/welcome` sans notification claire du changement de contexte, et que trois plugins sont installés au cours du parcours : WP Mail SMTP, WPConsent, et WPForms Lite lui-même. Verbatim de Montti dans le corps de l'article : « For most of these screens I had no idea that I was no longer on my site ».

Montti conclut que la qualification de « backdoor » reste discutable au sens strict, dans la mesure où le parcours nécessite l'action d'un administrateur qui déclenche l'assistant. La difficulté centrale n'est pas l'existence d'un accès non autorisé mais le manque de clarté sur le fait que l'utilisateur quitte son propre site pendant la configuration et installe plusieurs plugins depuis un tiers.

**Ce que cela déplace pour un consultant qui audite un site WordPress client**

- Un plugin de formulaire installé sur plus de 5 millions de sites vient d'être documenté publiquement comme redirigeant l'administrateur vers un domaine tiers pendant sa configuration, sans notification visible côté interface. C'est un fait d'audit à consigner pour tout site client sous WPForms Lite : le comportement n'est pas un défaut visible dans le rapport « plugins actifs », il n'apparaît qu'à la première utilisation de l'assistant.
- La conclusion de Montti est aussi opérationnelle qu'éditoriale : une accusation virale contre un plugin installé à grande échelle n'est pas un signal de désinstallation d'urgence. Une désinstallation en panique casse les formulaires actifs, coupe les leads en cours et coûte plus cher que la faille supposée. La bonne procédure reste : vérifier le comportement, isoler la fonction contestée, décider en connaissance de cause.

Ligne d'attribution retenue : source primaire éditoriale (Search Engine Journal, Roger Montti, test personnel du plugin), reprise dans le [récapitulatif Anicca du 11 août](https://anicca.co.uk/blog/weekly-update-search-marketing-11-08-2026/). L'accusation initiale de Sybre Waaijer n'a pas été testée indépendamment par un tiers hors du test de Montti.

## Rappel doctrine

- L'info du jour prolonge [[concepts/metriques-visibilite-geo]] (une nouvelle donnée de citation côté Google, sans clic ni requête) et [[concepts/data-proprietaire]] (le raccord au pipeline commercial reste chez le client, croisement obligatoire avec un outil GEO tiers et GA4).
- La brève 1 croise [[concepts/tabou-visibilite]] (la surface publicitaire et la surface citation restent séparées dans la même interface ChatGPT, le vocabulaire « visibilité » aplatit ce décrochage) et [[concepts/agentic-search]] (la mesure d'appariement topique dans une surface générative devient un point d'audit à part entière).
- La brève 2 ne mobilise pas de concept transverse : c'est un fait d'audit outil WordPress à consigner pour tout mandat sous WPForms Lite.

## Notes d'apprentissage (fin de run)

Grille de score de cette édition à noter dans `memory/calibration.md` :

- source_diversity : 5 sources indépendantes citées avec URL (seroundtable.com, anicca.co.uk, seranking.com, searchenginejournal.com, plus la mention Sybre Waaijer référencée dans le corps SEJ).
- claim_density : 11 claims verified sur le corps, 0 uncertain, 0 refuted.
- novelty_score : 4/5 (sortie universelle GSC AI report 11 août = fait Google factuel non annoncé encore, distinct des sorties partielles de juin et juillet ; étude SE Ranking 10 août = mesure primaire chiffrée fresh ; WPForms Lite backdoor = enquête SEJ du jour même).
- doctrine_fit : 4/5 (metriques-visibilite-geo + data-proprietaire + tabou-visibilite + agentic-search articulés sans forçage).
- redite_risk : faible (aucune redite intra-run, chaque anti-redite explicite dans said_index ; GSC AI report distinct des sorties partielles de juin et juillet couvertes 06-03 puis 07-02, seuil universel jamais atteint dans le ledger).
- clickbait_risk : faible (titre factuel long descriptif structurel).

Sources à ajouter en explore dans `ledgers/sources.jsonl` : seranking.com (trust initial 0,75 primaire vendeur GEO, étude cross-source Anicca, candidate exploit si reproduction indépendante), searchenginejournal.com (déjà connu, +1 hit utile Roger Montti WPForms Lite backdoor test 11 août), anicca.co.uk (trust initial 0,65 secondaire agence UK recap éditorial hebdo cross-source), seroundtable.com (déjà connu, +1 hit utile Barry Schwartz GSC AI report 11 août).

---

*Draft SyntheticBrain. Rien n'a été envoyé.*
