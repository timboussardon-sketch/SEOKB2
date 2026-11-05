---
date: 2026-10-01
pilier_info_du_jour: GEO / search IA
piliers_breves: [Business SEO, Niche SEO]
format: digest
version: v2
---

# Algorithme — Édition du 1er octobre 2026 (après-midi)

**Points capitaux**

- Google ouvre à tous les utilisateurs les capacités de surveillance d'AI Mode (Information Agents), jusqu'ici réservées aux abonnés Ultra et Pro, d'après l'annonce de Robby Stein (VP Product Google Search) sur X le 28 septembre 2026 et le relais de Search Engine Roundtable le 29.
- Cette fonction ouvre un canal où un agent Google interroge l'index « 24/7 » sur un sujet défini par l'utilisateur, sans trace mesurable côté site aujourd'hui dans la Search Console.
- D'après The Information rapporté par Barry Schwartz le 30 septembre, les paiements d'AI Contribution versés aux 100 éditeurs pilotes s'élèvent en moyenne à 0,1 % de leurs revenus publicitaires, sans méthode de calcul publiée.
- Google Maps impose depuis le 30 septembre une connexion à un compte Google pour consulter l'intégralité des avis et photos d'une fiche, un changement observé par plusieurs comptes professionnels et probablement destiné à freiner les scrapers IA.
- Les fonctions SEO/GEO ajoutées en septembre (Information Agents, 0,1 % pub, login reviews) renvoient toutes à la même asymétrie : plus la lecture et la découverte des contenus se font dans les produits Google, moins les éditeurs disposent d'outils d'instrumentation côté site.

---

## Info du jour — GEO / search IA

### Information Agents AI Mode : ouverture à tous les utilisateurs, et ce que ça fait au suivi de citation

**Les faits.** Le 28 septembre 2026, Robby Stein, VP Product de Google Search, a annoncé sur X que les capacités de surveillance d'AI Mode (« Information Agents ») sortaient de leur périmètre payant pour être déployées à tous les utilisateurs via l'application Google. Barry Schwartz a repris l'annonce dès le lendemain sur Search Engine Roundtable ([seroundtable.com/google-ai-mode-monitoring-capabilities-42179](https://www.seroundtable.com/google-ai-mode-monitoring-capabilities-42179.html)). Le mécanisme décrit par Google : l'utilisateur demande à AI Mode de surveiller un sujet, et le système « continuously checks across changing info on the web like sites, forums and social posts » (verbatim Robby Stein X, repris par Schwartz). Trois exemples sont donnés : nouveaux restaurants ou pop-ups à proximité, événements familiaux locaux, alertes de réapprovisionnement et de baisse de prix.

Jusqu'au 28 septembre, cette surveillance était réservée aux abonnés Google AI Ultra (déploiement global pour Ultra confirmé le 12 juin 2026 d'après [Search Engine Journal](https://www.searchenginejournal.com/google-rolls-out-ai-mode-information-agents-to-ultra-subscribers/579085/)) et élargie aux abonnés Pro ensuite. Le périmètre géographique du déploiement « everyone » n'est pas précisé par Robby Stein, hors mention de l'application Google. Reprise tier 2 par [Search Engine Roundtable](https://www.seroundtable.com/google-ai-mode-monitoring-capabilities-42179.html) et [relevantaudience.com](https://www.relevantaudience.com/ai/ai-mode-information-agents-global/) (à vérifier côté URLs tierces, Schwartz reste la source primaire du relais).

**Pilier.** Cette édition s'ancre sur **GEO / search IA**. Un agent de surveillance interne à Google qui boucle sur des sites, forums et plateformes sociales modifie la définition même d'une « citation IA » : la requête n'est plus initiée par l'utilisateur à chaque lecture, elle est initiée par l'agent, et le format de réponse n'est pas une page générative affichée, c'est une notification envoyée à l'utilisateur. Le concept de visibilité dans la réponse générative ([[concepts/metriques-visibilite-geo]]) rencontre ici une mécanique nouvelle : une variante où la citation n'est pas lue en direct par un humain mais reçue en push, sans contexte de session ni d'affichage.

**Lectures opérationnelles pour un consultant SEO/GEO.**

Premièrement, la surveillance d'AI Mode consomme de la fraîcheur. L'intérêt d'un Information Agent pour l'utilisateur est précisément de signaler ce qui a changé. Un site publié il y a six mois sans mise à jour depuis a peu de chances d'être cité dans ce format. L'instrumentation éditoriale « date de dernière modification visible + changelog page » devient un signal plus pertinent qu'auparavant, pour une fenêtre d'usage précise.

Deuxièmement, les trois exemples donnés par Google (restaurants, événements, prix) renvoient à trois verticaux où la fraîcheur et l'inventaire comptent plus que l'autorité : local, événementiel, ecommerce. Ce sont les mêmes verticaux déjà exposés par le filtre multimodal de la Search Console déployé le 24 septembre (voir [édition du 25 septembre](https://algorithme.substack.com)). Les sites qui gagnent une visibilité par Information Agent dans ces verticaux ne le verront nulle part dans leurs outils de mesure actuels.

Troisièmement, les Information Agents ne génèrent pas de clic au moment de la citation. Ils génèrent une notification à l'utilisateur, qui clique ou pas plus tard. La boucle d'attribution organique classique (impression Search Console → clic → session analytique) est ici cassée en deux moments : la citation initiale par l'agent (invisible) et la visite éventuelle de l'utilisateur à retardement (visible mais détachée de la citation). Le lien entre les deux doit se reconstituer autrement, par exemple par un canal de référence Google AI Mode distinct dans les logs serveurs, qui n'existe pas aujourd'hui dans les documents publics Google.

Quatrièmement, le passage du périmètre Ultra/Pro à « tous les utilisateurs » change l'échelle du phénomène. Les Information Agents étaient jusque-là une fonction de niche payante, à faible volume. Le déploiement grand public (« via l'application Google ») multiplie le nombre d'agents actifs d'un ordre de grandeur inconnu mais substantiel. La statistique de référence citée en août 2025 par Google (« over 1 billion monthly AI Mode users » rapportée par plusieurs médias à cette période) donne la taille maximale du nouveau pool d'agents de surveillance potentiels.

Cinquièmement, un Information Agent qui tourne en continu interroge l'index Google selon une fréquence définie côté Google, non côté éditeur. Les logs serveurs devraient théoriquement montrer un pic d'un user-agent Google spécifique à cette fonction, mais aucun user-agent public n'a été documenté par Google pour les Information Agents dans la [documentation officielle crawlers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers) consultée à cette date. L'instrumentation côté serveur reste à construire par les propriétaires de sites, à partir d'inférence sur la cadence et la distribution de requêtes depuis Googlebot et Google-Extended.

**Réserves méthodologiques.** La portée exacte de « everyone » reste imprécise. Robby Stein emploie le mot sans assortir d'une zone géographique ni d'une fenêtre de rollout. L'exemple vidéo de démonstration posté sur X montre un cas unique, pas un panel. Aucune donnée publique n'est disponible sur le taux d'adoption effectif de la fonction par les utilisateurs Ultra et Pro depuis juin 2026, et donc aucune base pour anticiper le taux d'adoption grand public. La fenêtre « sites, forums and social posts » employée par Robby Stein ne précise pas si l'agent se restreint à l'index de Google Search ou s'il interroge aussi des surfaces non indexées (Reddit via accord, YouTube, messageries). Enfin, aucune mesure indépendante n'a encore relié un Information Agent à une visite tierce dans les outils d'analytique côté site.

**Lien doctrine.** La fonction articule deux concepts du vault. [[concepts/agentic-search]] : un Information Agent est, structurellement, un agent qui remplace une partie de l'activité manuelle de l'utilisateur. Ce que décrit le concept pour les agents acheteurs (sélection par l'agent, pas affichage en liste) vaut pour les agents informationnels : la citation est consommée par un agent qui filtre, dédoublonne, sélectionne, avant de produire une notification à l'utilisateur. [[concepts/metriques-visibilite-geo]] : les trois métriques formalisées (Imp_wc, Imp_pos, Subjective Impression) décrivent une visibilité dans une réponse générative lue par un humain. Les Information Agents introduisent un cas où la réponse est consommée par une IA en premier, puis traduite en notification. Les trois métriques existantes ne couvrent pas cette consommation intermédiaire. Un travail doctrinal à prévoir en revue hebdo.

---

## Brève 1 — Business SEO

### AI Contribution Pilot : 0,1 % des revenus publicitaires moyens pour les 100 éditeurs invités

Dans son article du 30 septembre 2026 [seroundtable.com/google-ai-contribution-pilot-01-percent-42188](https://www.seroundtable.com/google-ai-contribution-pilot-01-percent-42188.html), Barry Schwartz rapporte, en s'appuyant sur [The Information](https://www.theinformation.com/), que Google verse en moyenne « one-tenth of 1% of their advertising revenue » aux 100 éditeurs participant au pilote AI Contribution. The Information cite « des personnes familières avec les paiements », et plusieurs participants déclarent au média qu'ils « n'ont aucune idée de la façon dont Google calcule ces paiements ». Variation observée : de moins de 1 000 USD sur plusieurs mois pour les petits sites à plus de 1 million USD par an pour un éditeur. Ces chiffres recoupent partiellement la fourchette publiée par Digiday le 14 septembre 2026 (1 M USD annuels pour une grande publication, 50 000 à 60 000 USD pour les petites, moins de 1 000 USD/mois pour certains), déjà citée dans l'édition du 30 septembre après-midi (brève AI Contribution Pilot).

Le ratio « 0,1 % des revenus publicitaires » est un fait nouveau par rapport à Digiday : il contextualise les montants bruts contre la masse publicitaire de référence de chaque éditeur. The Information et Schwartz restent la source unique de ce ratio ; Google n'a pas confirmé publiquement, et la méthode de calcul reste non divulguée. Lecture pour un consultant Business SEO : la rémunération AI Contribution n'est pas, à ce jour, un substitut économique à la perte de trafic organique causée par les AI Overviews et AI Mode. Un éditeur dont le trafic Google organique a baissé de 33 % entre novembre 2024 et novembre 2025 d'après le Reuters Institute Digital News Report 2026 (déjà couvert le 22 juin 2026) ne compense pas cette perte par 0,1 % de ses revenus publicitaires. La décision d'intégrer ou non le pilote relève, à ce stade, d'une logique d'option (collecter la donnée, apprendre le mécanisme) plus que d'un calcul de retour sur investissement.

---

## Brève 2 — Niche SEO

### Google Maps impose un login pour voir l'intégralité des avis d'une fiche

Le 30 septembre 2026, Google Maps requiert désormais une connexion à un compte Google pour lire et parcourir l'ensemble des avis et photos d'une fiche, pour trier les avis et pour en laisser un, d'après [seroundtable.com/google-maps-account-reviews-42186](https://www.seroundtable.com/google-maps-account-reviews-42186.html). Le changement a été observé par trois comptes professionnels : Syed Amir sur X, Michael B. Snow sur LinkedIn et Jean-Sébastien Girard sur LinkedIn. La page d'invitation à la connexion met en avant la personnalisation (« personalized travel », « saved places ») sans exposer la raison technique. Barry Schwartz formule explicitement l'hypothèse qu'il s'agit de « help prevent AI, bots, and third parties from scraping the Google reviews » (verbatim Schwartz).

Pour un propriétaire de fiche Google Business Profile ou un consultant Local SEO, trois conséquences se dessinent. Un, la lecture publique des avis par un visiteur non connecté est désormais partielle, ce qui réduit le signal de réputation accessible sans friction (le visiteur voit certains avis, pas tous). Deux, les outils tiers qui s'appuient sur du scraping non authentifié pour agréger les avis d'une fiche (plateformes de reputation management, moteurs comparatifs, instrumentations de GEO qui mesurent les sources communautaires citées) voient leur base de collecte restreinte. Trois, la rédaction d'un avis devient conditionnée au login, ce qui filtre les avis spontanés et peut durcir la frontière entre avis authentiques et avis coordonnés, dans un sens comme dans l'autre.

Réserve méthodologique : les trois observations rapportées par Schwartz portent sur une interface web desktop. Le comportement de l'application mobile Google Maps n'est pas documenté par les sources consultées, et aucune communication officielle Google ne confirme le changement ni n'en expose la motivation. L'hypothèse « bloquer les bots IA » reste donc une lecture, pas une confirmation. Un suivi est à prévoir une fois qu'un acteur du reputation management aura mesuré indépendamment la variation du volume d'avis accessibles sans compte avant/après le 30 septembre.

---

## Trois prédictions datées

- **P-2026-10-01-v2-1** (0,45, échéance 2027-03-31) — Au moins un outil tiers GEO (Ahrefs Brand Radar, Semrush AI Toolkit, Profound) publiera un indicateur de citation par Information Agent distinct de la citation par AI Overview et AI Mode, dans un rapport de visibilité IA, d'ici le 31 mars 2027. Résout par observation du changelog produit.
- **P-2026-10-01-v2-2** (0,30, échéance 2027-06-30) — Un éditeur du pilote AI Contribution publiera une analyse chiffrée de ses paiements et de leur variance mensuelle, en nommant son niveau de revenus publicitaires total, d'ici le 30 juin 2027. Résout par parution d'un post signé par un éditeur identifiable.
- **P-2026-10-01-v2-3** (0,55, échéance 2026-12-31) — Un acteur du reputation management local (BrightLocal, Whitespark, Yext ou équivalent) publiera un rapport comparant le nombre d'avis publiquement visibles sur Google Maps avant et après le 30 septembre 2026, sur un échantillon d'au moins 100 fiches, d'ici le 31 décembre 2026. Résout par parution du rapport.

---

## Sources utilisées dans cette édition

- Robby Stein (VP Product Google Search), annonce sur X du 28 septembre 2026, relayée par [Search Engine Roundtable 42179](https://www.seroundtable.com/google-ai-mode-monitoring-capabilities-42179.html) (29 sept).
- [Search Engine Journal 579085](https://www.searchenginejournal.com/google-rolls-out-ai-mode-information-agents-to-ultra-subscribers/579085/) — déploiement Ultra du 12 juin 2026, contexte.
- [Search Engine Roundtable 42188](https://www.seroundtable.com/google-ai-contribution-pilot-01-percent-42188.html) — AI Contribution 0,1 %, 30 sept 2026, rapportant [The Information](https://www.theinformation.com/).
- [Search Engine Roundtable 42186](https://www.seroundtable.com/google-maps-account-reviews-42186.html) — Google Maps login review, 30 sept 2026, avec observations de Syed Amir (X), Michael B. Snow (LinkedIn), Jean-Sébastien Girard (LinkedIn).
- [Barry Schwartz, « October 2026 Google Webmaster Report »](https://www.seroundtable.com/october-2026-google-webmaster-report-42185.html), 1er octobre 2026 — contexte mensuel.
- Documentation Google crawlers consultée : [developers.google.com/search/docs/crawling-indexing/overview-google-crawlers](https://developers.google.com/search/docs/crawling-indexing/overview-google-crawlers).
- Doctrine du vault : [[concepts/agentic-search]], [[concepts/metriques-visibilite-geo]].

---

*Édition du 1er octobre 2026 après-midi, v2 — SyntheticBrain. Draft non envoyé. Ancré sur le pilier GEO / search IA, les brèves relevant de Business SEO (AI Contribution) et de Niche SEO (Google Maps login).*
