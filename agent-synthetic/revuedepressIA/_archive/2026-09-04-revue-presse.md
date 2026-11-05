# Algorithme — édition du 4 septembre 2026

## Résumé (3 à 5 points capitaux)

- Robby Stein, VP Product de Google Search, a reconnu publiquement sur X le 3 septembre 2026 que Gemini 3.8 Flash affiche moins de citations et de liens dans AI Mode que le modèle par défaut : « This isn't working as intended, and we'll roll out a fix soon » ([Search Engine Land](https://searchengineland.com/google-to-fix-citation-bug-with-gemini-3-8-flash-in-ai-mode-486892), [Search Engine Roundtable](https://www.seroundtable.com/google-ai-mode-gemini-38-no-links-42011.html)).
- Le bug ne touche que les abonnés Google AI Pro et Ultra qui ont sélectionné 3.8 Flash via le menu, pas les utilisateurs par défaut, et Google n'a pas donné de calendrier chiffré pour le correctif.
- Pour un audit GEO échantillonné depuis le 2 septembre 2026, toute baseline captée en 3.8 Flash sur des requêtes informationnelles risque de sous-mesurer les citations d'un site par rapport à une mesure sur le modèle par défaut.
- Carrie-Ann Sudlow publie le 3 septembre sur Search Engine Land une liste de sept signaux d'alerte à surveiller avant que le trafic organique ne chute, dont l'instabilité des URL classées et la divergence entre positions, impressions, clics et trafic ([Search Engine Land](https://searchengineland.com/seo-warning-signs-before-organic-traffic-falls-486640)).
- Barry Schwartz documente le 3 septembre des cas de contenu qui apparaît dans les résultats web de Google mais disparaît de l'onglet Actualités, y compris sur son propre site, sans que Google n'ait répondu à sa sollicitation Bluesky ([Search Engine Roundtable](https://www.seroundtable.com/google-news-tab-content-disappearing-42012.html)).

---

## Info du jour — Google reconnaît le bug de citations de Gemini 3.8 Flash dans AI Mode et annonce un correctif rapide (pilier GEO / search IA)

**Le fait.** Le 3 septembre 2026 à 20h25 ET, Barry Schwartz a publié sur Search Engine Land la confirmation par Google que Gemini 3.8 Flash, le modèle déployé la veille dans AI Mode pour les abonnés Google AI Pro et Ultra, présente un défaut de citations sur les requêtes de haut d'entonnoir ([Search Engine Land](https://searchengineland.com/google-to-fix-citation-bug-with-gemini-3-8-flash-in-ai-mode-486892)). Robby Stein, VP Product de Google Search, a répondu sur X à l'observation initiale : « This isn't working as intended, and we'll roll out a fix soon ». L'information a été relayée le même jour sur Search Engine Roundtable et Search Engine Watch ([Search Engine Roundtable](https://www.seroundtable.com/google-ai-mode-gemini-38-no-links-42011.html)).

**Le cycle observation → confirmation en trois jours.** L'anomalie a été repérée d'abord le 3 septembre au matin par Gagan Ghotra sur X, screenshots à l'appui, puis corroborée quelques heures plus tard par Glenn Gabe qui a publié deux captures comparatives entre modèle par défaut et 3.8 Flash. Barry Schwartz a agrégé les observations dans un article publié le 3 septembre 2026 à 7h41 ET sur Search Engine Roundtable, sans réponse Google à ce moment. La confirmation de Robby Stein est intervenue dans la même journée, environ treize heures après la publication initiale de Schwartz.

**Le périmètre exact du bug.** Le défaut de citations n'affecte que les utilisateurs qui ont explicitement sélectionné Gemini 3.8 Flash via le menu du sélecteur de modèles dans AI Mode. Il s'agit d'un choix opt-in réservé aux abonnés payants Google AI Pro et Google AI Ultra. Les utilisateurs qui restent sur le modèle par défaut ne sont pas concernés. Google n'a pas indiqué à ce stade combien de requêtes ont été affectées ni sur quelle proportion d'entre elles les citations ont été supprimées. Google n'a pas non plus précisé si le fix consiste à re-paramétrer le pipeline de citation en aval de la génération ou à ré-entraîner le modèle en amont.

**Ce que cette reconnaissance implique côté mesure GEO.** Deux points opérationnels tombent immédiatement pour tout consultant GEO ou tout outil tiers qui échantillonne AI Mode.

1. Toute mesure de taux de citation captée depuis le 2 septembre 2026 sur un panel de requêtes informationnelles dans AI Mode avec 3.8 Flash sélectionné est biaisée à la baisse. Cette mesure ne peut pas être comparée directement à une baseline captée avant le 2 septembre ni à une mesure sur le modèle par défaut, sans documenter explicitement la variable « modèle utilisé ».
2. La couche de citation dans AI Mode est fonction du modèle qui produit la réponse, pas uniquement du contenu source ni du classement organique de la page. Deux modèles disponibles sur la même surface, via le même menu utilisateur, produisent des sorties structurellement différentes en termes de citations et de liens sortants. Ce n'est plus une hypothèse, c'est un fait mesuré et reconnu par Google.

**Ce que Robby Stein ne dit pas.** La formulation « This isn't working as intended » situe le défaut du côté d'un dysfonctionnement à corriger, pas d'un choix produit assumé. Cela laisse toutefois plusieurs points ouverts. Google ne dit pas si le comportement cible pour 3.8 Flash est le même taux de citations que le modèle par défaut, ou un taux calibré différemment. Google ne dit pas non plus si le correctif s'appliquera rétroactivement aux requêtes déjà servies depuis le 2 septembre 2026, ni si les utilisateurs qui ont vu passer une réponse sans citation seront informés du fait qu'ils ont utilisé une version défaillante du modèle.

**Cadrage historique : ce n'est pas le premier bug de citations documenté publiquement sur AI Mode ou AI Overviews.** Le fait précis à retenir ici tient à la vitesse du cycle observation-reconnaissance. Le repérage par deux figures SEO connues (Ghotra et Gabe), la publication en article par une source SEO de référence (Schwartz), la reprise par une seconde publication indépendante et la réponse d'un VP Product Google se sont enchaînés dans la même fenêtre de 24 heures. Ce cycle court est un signal en soi sur la nature de la boucle d'observation externe qui pèse désormais sur les produits IA de Google.

**Trois lectures opérationnelles pour un consultant SEO ou GEO.**

1. Sur un audit GEO client en cours cette semaine, ajouter au protocole d'échantillonnage AI Mode une variable « modèle utilisé » avec deux niveaux : par défaut, et 3.8 Flash sélectionné. Mesurer les deux en parallèle sur le même set de requêtes. Une divergence de taux de citations entre les deux niveaux confirmera ou infirmera l'observation initiale au-delà des captures qualitatives Ghotra et Gabe.
2. Pour un client qui suivait un panel de requêtes AI Mode avant le 2 septembre 2026, geler la comparaison de séries temporelles sur ce panel jusqu'à ce que Google confirme la fin du déploiement du correctif. Documenter la période 2 septembre - fin du fix comme une fenêtre où les mesures sont non comparables à la baseline pré-2 septembre.
3. Sur un dashboard GEO tiers acheté par un client (Otterly, Profound, Peec AI, seoClarity, autre), demander explicitement à l'éditeur du dashboard quel modèle AI Mode il échantillonne, à quelle fréquence, et si la mesure du 2 septembre 2026 au correctif Google est marquée comme non fiable dans l'historique client.

**Réserves de fact-check.**

- Google n'a pas publié de billet Search Central ni de post blog corporate confirmant le bug au 3 septembre 2026 à 22h. La reconnaissance passe uniquement par un post X de Robby Stein, sans thread détaillé sur le mécanisme.
- Ni Ghotra ni Gabe ne publient de mesure agrégée sur un échantillon documenté. Les observations restent qualitatives, portées par des captures d'écran isolées.
- Le nombre exact de requêtes affectées, la période de déploiement du bug et la date du correctif ne sont pas précisés.

**Prédictions datées.**

- P-2026-09-04-1 : Google publie avant le 30 septembre 2026 un statement public (billet Search Central, post blog, réponse officielle à Barry Schwartz ou à un autre journaliste search) qui confirme la fin du déploiement du correctif Gemini 3.8 Flash citations et donne un cadre temporel de non-comparabilité des mesures GEO sur la période concernée. Confidence 0,55.
- P-2026-09-04-2 : au moins un outil GEO tiers publie avant le 30 novembre 2026 une note technique publique qui documente l'écart de taux de citations mesuré entre modèle par défaut et 3.8 Flash sur un panel de requêtes informationnelles échantillonné entre le 2 septembre 2026 et la date du correctif. Confidence 0,45.
- P-2026-09-04-3 : la version corrigée de Gemini 3.8 Flash présente un taux de citations mesurable inférieur au modèle par défaut d'au moins 10 points de pourcentage sur les requêtes informationnelles échantillonnées après correctif, hypothèse d'un choix produit sous-jacent qui reste caché derrière la formulation « not working as intended ». Confidence 0,30.

**Ancrage doctrine.** [[concepts/metriques-visibilite-geo]] (le fait reconnu par Robby Stein confirme concrètement que la métrique « taux de citations dans AI Mode » est une fonction du modèle qui produit la réponse, pas uniquement du contenu source ni du classement organique ; cela impose de traiter la variable modèle comme une dimension mesurable à part entière dans toute méthodologie GEO), [[concepts/arbitrage-plateforme-publication]] (deux modèles disponibles sur la même surface AI Mode via un menu utilisateur produisent des sorties structurellement différentes en citations et en liens sortants, cas d'arbitrage à documenter dans un rapport client), [[concepts/structural-information-geo]] (la couche de citation reste sensible au comportement du modèle en aval du contenu source ; l'optimisation structurelle du contenu ne suffit pas à garantir la citation si le modèle qui génère la réponse ne les émet pas).

---

## Brèves

### Brève 1 — Sudlow liste sept signaux d'alerte à surveiller avant la chute du trafic organique (pilier Actualité SEO)

**Le fait.** Le 3 septembre 2026, Carrie-Ann Sudlow a publié sur Search Engine Land un article méthodologique qui identifie sept signaux d'alerte précoces à repérer dans les données de performance SEO, avant que la courbe principale de trafic organique ne se retourne ([Search Engine Land](https://searchengineland.com/seo-warning-signs-before-organic-traffic-falls-486640)). L'article a été édité par Angel Niñofranco et relu par Danny Goodwin.

**Les sept signaux listés.**

1. Instabilité des URL classées sur une même requête, qui masque l'incertitude de Google sur la page à privilégier.
2. Impressions en hausse mais clics stagnants, qui signalent une visibilité informationnelle qui obscurcit un déclin commercial parallèle.
3. Analyse de la force des concurrents qui montent : comprendre pourquoi ils gagnent, pas seulement quels mots-clés ils prennent.
4. Pages historiquement fortes qui deviennent relativement plus faibles à contenu inchangé, parce que le standard du marché a monté autour d'elles.
5. Croissance globale du trafic qui cache un déclin commercial : la hausse du trafic informationnel masque la perte de visibilité des pages de service.
6. Chute des leads qui précède la chute du trafic, indiquant un changement dans la composition des requêtes servies plutôt qu'un volume qui baisse.
7. Divergence entre positions, impressions, clics et trafic : quand les quatre métriques racontent des histoires contradictoires, le signal est dans la divergence elle-même.

**Trois verbatim centraux.**

- « A five-position drop across a handful of high-intent searches can matter more commercially than hundreds of new low-value rankings, yet those rankings can make the report look positive. »
- « By the time the main traffic graph turns red, the useful warning may already be months old. »
- « Good SEO analysis isn't about finding a green number to put in a report. »

**Ce qu'un consultant SEO peut en tirer.** L'article n'apporte pas de chiffres empiriques ni de méthodologie mesurée : c'est un cadre de lecture, pas une étude. Il vaut par sa capacité à structurer un audit de santé SEO en amont de la chute, plutôt qu'après. La logique implicite tient en une phrase : dans les données Search Console, la divergence entre les métriques est un signal en soi, indépendamment du niveau absolu de chaque métrique prise isolément.

**Réserves.** L'article est mono-source, sans données quantifiées, sans étude empirique de validation. Chaque signal est illustré par un exemple type, pas par un cas client documenté ni par une mesure agrégée. Le cadre est utile pour poser un questionnaire d'audit, pas pour trancher une hypothèse causale.

**Ancrage doctrine.** [[concepts/triade-serp]] (les divergences entre positions, impressions, clics et trafic listées par Sudlow sont exactement le type de divergence que la lecture croisée de trois signaux Search Console permet de repérer ; le cadre de lecture proposé complète l'approche déjà tenue par le vault pour l'audit d'un site en cours de dégradation).

### Brève 2 — Publishers signalent la disparition intermittente de contenu de l'onglet Actualités Google (pilier Actualité SEO)

**Le fait.** Le 3 septembre 2026, Barry Schwartz a publié sur Search Engine Roundtable une observation portant sur plusieurs éditeurs, dont son propre site, dont le contenu apparaît normalement dans les résultats web de Google Search mais est absent de l'onglet Actualités sur la même requête ([Search Engine Roundtable](https://www.seroundtable.com/google-news-tab-content-disappearing-42012.html)). Schwartz documente un cas où son propre article était présent dans l'onglet Actualités, puis a disparu, puis est revenu vers 16h ET. Il a interrogé Google via Bluesky sans obtenir de réponse au moment de la publication. Mayank Parmar de Windows Latest a contribué à l'identification du signal. Verbatim Schwartz : « I cannot figure out a pattern or anything on why this might be happening ».

**Ce que cela signifie côté éditeur.** L'onglet Actualités de Google Search est une surface de découverte à trafic significatif pour les éditeurs qui produisent du contenu daté (news, revues de presse, dépêches). Une absence intermittente sur cette surface signifie une perte de trafic non détectable via un suivi de positions classique (la page reste indexée dans les résultats web) mais mesurable via Search Console si le rapport de performance distingue les surfaces d'apparition. Pour un éditeur qui alimente une rubrique news, un contrôle Search Console sur la surface « Google News » sur la fenêtre 1er au 3 septembre 2026 peut confirmer ou infirmer l'anomalie sur son propre site.

**Réserves.** Observation mono-source à ce stade, portée par Barry Schwartz et corroborée uniquement par une contribution d'identification de Mayank Parmar. Pas de statement Google au 3 septembre 2026. Pas de mesure agrégée du nombre d'éditeurs affectés ni de la durée moyenne de disparition. Schwartz précise lui-même que le comportement lui semble différent des incidents antérieurs de visibilité de Google News, sans en préciser la nature exacte.

**Ce qu'un consultant SEO peut faire dans la fenêtre.** Ouvrir Search Console sur les propriétés client qui alimentent une rubrique news, filtrer sur la surface « Google News » et sur la fenêtre 1er septembre 2026 à aujourd'hui, comparer avec la fenêtre 1er au 15 août 2026 sur les mêmes requêtes. Documenter la présence ou l'absence de l'anomalie pour le client. Ne rien pousser côté produit avant confirmation Google ou fix, l'anomalie pouvant se résoudre d'elle-même.

**Ancrage doctrine.** [[concepts/metriques-visibilite-geo]] (l'apparition sur une surface Google spécifique comme l'onglet Actualités est une métrique de visibilité distincte du classement organique sur la surface Web ; l'audit d'une régression de trafic doit toujours distinguer la surface d'apparition, pas seulement le rang).

---

*Édition rédigée par SyntheticBrain. Rien n'a été envoyé.*
