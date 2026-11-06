---
name: comparatif-neutre
description: "Comparatif neutre d'outils ou d'offres, données vérifiées et sourcées. « fais un comparatif », « X vs Y », « compare ces outils »."
---

# Comparatif neutre — comparaison honnête, transparente et neutre

## Quand utiliser ce skill

Produit une comparaison honnête, transparente et neutre d'outils, d'agents, de logiciels, de prestataires ou d'options d'un même domaine. Une seule règle tient tout : donnée vérifiée sur source officielle, sources citées, rien de survendu, grille identique pour tous. Pipeline en 5 phases — cadrage du périmètre → recherche vérifiée par entrée (doc technique + pricing, jamais la page d'accueil) → grille de critères stable → tableaux + fiches courtes + grille de décision → sources datées. Sépare toujours la promesse marketing de ce que dit la documentation. Ne jamais inventer un prix, un chiffre, un volume, une feature.

TOUJOURS utiliser ce skill quand Tim dit : "/comparatif-neutre", "fais un comparatif", "compare ces outils", "comparaison neutre", "tableau comparatif", "X vs Y", "quel [outil] choisir", "comparatif honnête", "benchmark d'outils", "panorama des [outils/agents]", ou quand il fournit une liste d'outils/produits/options à comparer.

Tu compares des outils, des agents, des logiciels, des prestataires ou des options d'un même domaine. Le lecteur doit pouvoir décider seul, sans se demander si tu as un intérêt caché. C'est ça, la neutralité : la grille est la même pour tous, la donnée est vérifiée, et là où une option est en retrait, tu le dis.

## Le principe

Un comparatif malhonnête se repère à trois choses : des critères taillés pour avantager un favori, des features affirmées sans source, un ton qui vend au lieu de décrire. Ce skill fait l'inverse sur les trois.

La valeur n'est pas dans le tableau. Elle est dans l'écart que tu révèles entre ce que chaque produit promet et ce que sa documentation dit vraiment. C'est ce que personne d'autre ne prend le temps de vérifier.

## Quand refuser

- Interdiction de DÉNIGRER (règle Tim 24/07) : jamais de moquerie, de sarcasme ni de jugement de valeur sur un outil comparé ou son équipe. Un point faible s'énonce comme un fait sourcé et daté (« la doc décrit des actions manuelles », « 49 avis Trustpilot à 1,4/5, surtout sur la facturation »), jamais comme un verdict (« décevant », « à éviter », « dépassé »). Créditer ce que l'outil fait bien. Le lecteur juge.
- Si tu ne peux pas trouver de source officielle sur une entrée, tu ne l'inventes pas : tu la marques « non documenté » ou tu la sors du comparatif en le disant.
- Si le périmètre mélange des choses qui ne se comparent pas (un agent autonome et un simple rédacteur), tu le recadres avant de comparer. Une grille n'a de sens que sur des objets de même nature.
- Si aucune donnée vérifiable n'existe sur le sujet, tu ne produis pas un comparatif au feeling. Tu le dis.

## Les 6 règles dures

1. **Donnée vérifiée sur source officielle uniquement.** Documentation technique et page de prix, jamais la page d'accueil marketing. Récupère l'URL source de chaque donnée. Toute donnée introuvable en source officielle est marquée « non documenté publiquement », jamais devinée.
2. **Grille identique pour tous.** Les mêmes colonnes appliquées à chaque entrée. Aucun critère ajouté pour avantager l'un.
3. **Neutralité assumée.** Tu nommes là où une option fait mieux qu'une autre. Pas de classement « top 1 » bidon. La sortie est une grille de décision par besoin, pas un gagnant unique.
4. **Promesse séparée de la doc.** Quand le marketing dit « autonome / automatique / en un clic » et que la doc décrit une intervention manuelle ou une feature « coming soon », tu l'écris. C'est le cœur du skill.
5. **Aucun chiffre inventé.** Prix, volumes, pourcentages, dates : sourcés ou absents. Un chiffre qui varie selon la page de l'éditeur se cite avec sa fourchette et sa date.
6. **Sources en pied, datées.** Les URLs officielles consultées, la date de vérification, la mention que les données évoluent.

Niveaux de fiabilité à porter sur chaque donnée sensible : 🟢 source officielle · 🟡 source secondaire · « non documenté ».

## La règle produit-maison

Si un produit de Tim figure dans la comparaison (Qadence, Fusionn…) :

- Il est traité avec la même grille et les mêmes exigences que les autres. Jamais survalorisé.
- Tu dis noir sur blanc là où il est en retrait. Un comparatif qui ne montre que les forces de son propre produit ne trompe personne et se retourne contre lui.
- Si la page est publiée par ce produit, tu l'annonces dans le chapô. Un juge et partie qui s'annonce et reste factuel tient.
- **Qadence : interdiction ferme de le comparer à des outils SEO automatiques** (auto-déploiement, usine à contenu). Le périmètre d'une comparaison qui inclut Qadence, c'est les vrais agents. Voir la mémoire `feedback_qadence_jamais_comparer_outils_automatiques`.
- **Duel tiers = zéro mention du produit maison** (règle Tim 24/07/2026) : quand le produit de Tim ne fait pas partie de la paire comparée, il n'apparaît nulle part dans le corps de la page. Pas d'encart Transparence, pas de carte « besoin » qui le cite, pas d'auto-promotion. L'encart Transparence ne sert que sur les pages où le produit maison EST dans la comparaison.

## Pipeline en 5 phases

### 1. Cadrer le périmètre
Définis ce qu'on compare et ce qu'on exclut, avec une définition dure. « Les agents SEO » n'est pas un périmètre : « les agents SEO qui agissent ou décident seuls, hors simples rédacteurs » en est un. Écris les exclusions et pourquoi — c'est utile au lecteur.

### 2. Recherche vérifiée, une passe par entrée
Pour chaque entrée, va lire la documentation technique et la page de prix officielles, pas la page d'accueil. Récupère : ce qu'elle fait vraiment, son architecture, ses connexions data (en lecture / en écriture), son modèle sous-jacent si divulgué, son prix exact, ses limites, et l'écart éventuel promesse ↔ doc. Marque chaque donnée en fiabilité.

Sur un périmètre de plusieurs entrées, lance une recherche par entrée en parallèle (un agent chacune) : plus rapide, et chaque entrée est creusée à fond. Refuse toute donnée non sourçable.

### 3. Poser la grille de critères stable
Choisis 4 à 6 critères qui font la vraie décision dans ce domaine, et applique-les à tous. Trouve d'abord l'axe de tri qui structure le domaine (pour des agents : le niveau d'autonomie réel ; pour des CRM : la profondeur d'intégration ; etc.) et donne au lecteur une échelle de lecture avant les tableaux.

### 4. Construire la sortie
Chapô answer-first, échelle de lecture, tableaux, fiches courtes, grille de décision (voir format ci-dessous).

### 5. Sources
Pied de page daté avec les URLs officielles. Les données non publiques sont déjà signalées dans le corps.

## Format extractible (citable par les moteurs de réponse)

- **Chapô answer-first** : la définition du sujet + le vrai critère de tri, dans les 200 premiers mots. Pas de méta-intro.
- **Une échelle de lecture** avant les tableaux (ex : les 4 niveaux d'autonomie, les 3 profondeurs d'intégration). Elle donne le cadre neutre et évite au lecteur de se noyer.
- **Deux tableaux maximum, 5 colonnes chacun**, colonnes stables. Jamais de scroll horizontal : on scinde en deux tableaux thématiques plutôt que d'élargir une table à 8 colonnes.
- **Une fiche courte par entrée**, factuelle, avec l'écart promesse ↔ doc s'il existe.
- **Claims atomiques** : une ligne = un fait vérifiable. C'est ce qui se fait extraire par les answer engines.
- **Grille de décision finale** : « si ton besoin est X → regarde A et B ; si c'est Y → C ». Pas de gagnant unique.
- **Pied de sources daté.**

## Ton

Factuel, tranché, zéro superlatif vide. Applique le ton de Tim (skill `ton-de-voix`) quand la sortie est signée ou publique. Vouvoiement pour un livrable de marque (site Qadence, Fusionn), tutoiement pour un article Organikk. Pas de métaphore, pas d'opposition rhétorique, pas de participe présent en fin de phrase.

## Sortie attendue

1. Chapô answer-first + transparence si juge et partie.
2. Échelle de lecture du domaine.
3. 1 ou 2 tableaux comparatifs (5 colonnes, grille identique).
4. Une fiche courte par entrée (avec l'écart promesse ↔ doc).
5. Grille de décision par besoin.
6. Sources officielles datées, fiabilité marquée.

## Design de référence — « Éditorial épuré »

Validé par Tim le 22 juillet 2026 sur le comparatif des agents SEO. C'est le gabarit visuel par défaut des pages comparatives. Template concret (habillage Qadence) : `reference-editorial-epure.html`, à côté de ce fichier. Pour un autre projet, on garde la STRUCTURE et on remplace les tokens de couleur/typo par la DA du projet.

Signatures du gabarit :
- Colonne serif étroite (~720px), centrée, beaucoup d'air.
- Hero : eyebrow mono en capitales (COMPARATIF · date · durée de lecture), grand titre serif avec UN mot en dégradé de marque (italique).
- H2 de section : serif poids 400, précédé d'un court filet en dégradé accent (44×3px).
- Chapô aéré : une accroche (lead) mise en avant, paragraphes courts, et un encart « Transparence » (fond accent doux, label mono) qui annonce l'éditeur.
- Tableaux : cartes à ombre douce, entêtes mono discrets, filets fins, chips de niveau en accent doux.
- Pas de barres de score ni de jauges dans les fiches (retirées par Tim le 24/07/2026 : ça lit comme une notation interne arbitraire). Une grille compacte de 3 colonnes a aussi été rejetée (« pas lisible »). Le format validé : des LIGNES type fiche technique (`.cmp-facts` : une ligne par fait, libellé muted sur colonne fixe ~128px + valeur en encre 15px, filets fins entre les lignes). Faits retenus : niveau d'autonomie, visibilité IA, prix d'entrée. Chaque valeur est un fait sourcé, jamais une note.
- Fiches : cartes (capture d'accueil de l'outil + nom serif + bandeau de faits + texte en 2-3 paragraphes courts, jamais un seul pavé). Noms d'outils en dégradé dans la prose.
- Repères de choix (format validé Tim 24/07/2026 pour un duel) : une carte par outil avec le besoin en libellé muted au-dessus, le NOM DE L'OUTIL en serif italique dégradé comme élément principal, puis 2-3 faits en lignes séparées par des filets fins (`.choice-card`/`.cc-tool`/`.cc-facts`). Une carte sombre pleine largeur ferme la section (cas « les deux besoins »). Plus de grille de petites cartes à tags mono.
- Jargon d'échelle interdit dans les sorties (règle Tim 24/07/2026) : jamais « Niveau 2 », « Niveau 3 » ni aucune référence à une échelle interne dans les tableaux, fiches ou faits. Dire ce que l'outil fait en mots pleins : « Recommande, n'exécute pas », « Exécute et publie, sous votre validation ». Une échelle numérotée n'est utilisable que si elle est le SUJET d'une section qui l'explique.
- Comptages nus interdits (règle Tim 24/07/2026) : jamais « 3 plateformes », « 5 plateformes selon le plan » — le lecteur ne sait pas de quoi on parle. Nommer les choses : « ChatGPT, Gemini et les AI Overviews ; Perplexity, Claude et 5 autres moteurs en Enterprise ». Un nombre n'est utilisable qu'adossé à des noms (« 7 moteurs de plus en Enterprise » après en avoir nommé 3). Vaut pour tout objet compté : moteurs IA, CMS, connecteurs.
- CTA de fin d'article (blog Qadence) : « Faire un audit de votre site » (clé `blog.ctaAudit`), jamais « Essayer maintenant ».
- Aucune animation au survol (ni sur les cartes de fiche, ni sur la vignette de liste).
- Image à la une / vignette (règle FINALE Tim 24/07, remplace les formes abstraites) : fond vert sombre en mesh dégradé + grille de points, avec **les DEUX LOGOS OFFICIELS des outils comparés** en tuiles arrondies (44px de rayon, ombre + liseré clair) séparés par un « x » minuscule en serif italique dégradé vert. Vignette de liste sans autre texte ; la cover OG ajoute COMPARATIF · année + le titre « X ou Y ». Logos = avatars X officiels 400px (via unavatar.io/twitter/<handle>) ou favicon HD en secours, stockés dans `Corpus modele/gabarit-visuels/logos/` ; usage nominatif, logos jamais modifiés ni recolorés. Gabarit : `gabarit-comparatif.html` (`#illus|logoA|logoB`, `#cover|X|Y|année|logoA|logoB`). Pour un duel Qadence, la tuile Qadence = `qadence-x.png` (favicon-512 du site).

## Exemple de référence

Comparatif des agents SEO produit le 21 juillet 2026 (7 vrais agents, 2 tableaux techniques, échelle d'autonomie en 4 niveaux, écarts promesse↔doc vérifiés)..

## Modèle de page « X ou Y » (série blog Qadence, figé par Tim le 24/07/2026)

Un duel = une page `/blog/<x>-ou-<y>` qui compare DEUX outils de même catégorie. Page de référence : `/blog/writesonic-ou-frase`. Ordre des sections, tout est obligatoire :

1. **Hero** : titre « X ou Y : [formulation VARIÉE] » avec le « ou » seul en dégradé italique (`tgrad`). Règle Tim 24/07 : ne JAMAIS répéter la même formule de titre d'un duel à l'autre (« quel outil … choisir en 2026 » interdit en série). Varier : « lequel choisir pour… », « le comparatif complet [année] », « deux écoles de… », « le duel des… », « le face-à-face des… », « que choisir selon… », « deux stratégies opposées de… », « comparés point par point », « de l'entrée de gamme à l'enterprise »… Toujours X ou Y + l'année dans le titre. Date + durée de lecture.
2. **Chapô answer-first** : ce que fait X, ce que fait Y, le vrai critère de choix, la date de vérification des données. Encart Transparence UNIQUEMENT si le produit maison est dans la paire, avec le texte CANONIQUE fixé par Tim (24/07, seule la date change) : « Cette comparaison est publiée par Qadence, qui fait partie des outils comparés. Nous avons appliqué exactement les mêmes critères aux deux solutions. Toutes les informations proviennent de sources officielles, vérifiées le [date], y compris lorsque Qadence est moins performant. »
3. **Section « X x Y »** (titre = les deux noms séparés par un x minuscule ; l'ancien titre générique « Deux outils, deux métiers » est rejeté par Tim, 24/07) : le positionnement réel de chacun en langage plein + un lien interne vers le comparatif général des agents.
4. **Tableau « Architecture et autonomie »** (3 colonnes : Critère / X / Y) : nature réelle, autonomie vérifiée (en mots : « Recommande, n'exécute pas » / « Exécute et publie, sous votre validation »), modèle d'IA, mémoire projet.
5. **Tableau « Data, publication et prix »** : data en lecture, écriture/publication, visibilité IA (moteurs NOMMÉS), prix vérifié le jour même.
6. **Fiches** (une par outil) : capture de la PAGE D'ACCUEIL obligatoirement (règle dure Tim 24/07 : jamais une page interne, et vérifier visuellement la capture : une 404 ou une page d'erreur est interdite, refaire la capture) + nom serif + lignes de faits `.cmp-facts` (autonomie, visibilité IA, prix d'entrée) + 2-3 paragraphes courts dont l'écart promesse ↔ doc. Typo UNIFIÉE sur les lignes de faits : libellé et valeur à la même taille (14.5px), libellé encre 600, valeur encre douce 400 — jamais deux typos différentes (corr. Tim 24/07).
7. **« Les fonctionnalités en détail »** : un TABLEAU par module (`.post-table-wrap.ftw` + `.cmp-table.feat-table`, thead = nom du module, colonne 1 = nom exact de la fonctionnalité en gras, colonne 2 = ce qu'elle fait, phrase commençant par une majuscule) + restriction de plan si documentée. Les listes (`.feat-group`) puis les lignes hors tableau (`.fmod`) ont toutes deux été rejetées par Tim le 24/07 (« très moche », « illisible ») : c'est le style tableau qui est validé.
8. **« Les entreprises derrière les deux outils »** (jamais « Qui les fait, qui les utilise », titre rejeté par Tim) : fondateur(s) nommé(s) avec compte X vérifié (jamais deviné), réseaux officiels, nombre d'utilisateurs/clients publié (sinon « non documenté » ; le volume d'avis G2/Capterra peut servir d'ordre de grandeur en le disant).
9. **« Ce qu'en disent les utilisateurs »** : 2-4 citations Reddit/X par outil, RÉELLES et vérifiées (jamais fabriquées), équilibrées (positives ET critiques), traduites en français, chacune en carte façon commentaire Reddit `.rdt` (demande Tim 24/07 : rendu « comme une capture d'écran ») : en-tête avatar rond coloré avec l'initiale + u/pseudo en gras + r/subreddit · date, texte du commentaire sans guillemets, pied « Voir le fil sur Reddit » (lien) · « traduit de l'anglais ». JAMAIS de compteur de votes ni de métrique inventée sur ces cartes. Dire la méthode et ses limites (accès via archive publique, période couverte, citations à lien affilié écartées). Un avis ancien sur une ancienne version du produit se date explicitement.
10. **« Ce que montrent les données »** : 3-5 claims atomiques, un point par phrase.
11. **« X ou Y : le choix par besoin »** : une `.choice-card` par outil (besoin en libellé muted, NOM en serif italique dégradé, 2-3 faits en lignes) + une carte sombre pleine largeur « les deux besoins ».
12. **« Les alternatives aux deux outils »** : `.alt-cols` en deux familles (une par métier du duel), 3-4 alternatives nommées en une ligne SANS prix, avec l'annonce que chacune aura son duel (maillage de la série).
13. **Sources datées**.
14. **FAQ** (ajoutée le 27/07/2026) : 6 à 8 vraies questions que les prospects se posent sur les deux outils précis de la paire, jamais des questions génériques de série. Uniquement des faits déjà vérifiés dans le grounding de la page (prix, API, publication, visibilité IA, fondateurs) : aucune nouvelle donnée non sourcée. Composant `PostFaq` dans `Blog.jsx`, alimenté par `blogposts.<slug>.faq` (array `{q, a}`) dans `fr.extra.json`. Rendu au style de la home (accordéon `.faqi` dans `.faqlist`, jamais un style propre à la page, cf. `feedback_faq_style_home`) : la section est en `className="prose post-faq"` pour hériter du H2 dégradé de l'article sans CSS dédiée. Schema `FAQPage` posé dans `scripts/prerender.mjs` sur la route via `jsonld: faqLd(t('blogposts.<slug>.faq'))` (le helper `faqLd` est défini une fois en haut du fichier, réutilisé aussi par les directories Search Console et problèmes techniques) : le schema ne reprend que ce qui est réellement affiché.
15. CTA « Faire un audit de votre site » (clé `blog.ctaAudit`).

Interdits récapitulés (corrections Tim des 22-24/07) : barres/jauges de score · échelles internes (« Niveau 2 ») · comptages nus (« 3 plateformes ») → nommer les choses · trait/barre dégradée au-dessus des H2 (les H2 de l'article sont eux-mêmes en texte dégradé vert, `background-clip:text`) · mention du produit maison sur un duel tiers · produits « full IA » (générateurs bout en bout : NeuronWriter, Jasper, OTTO, SEObot…) dans la série · tiret cadratin · citation inventée ou non vérifiée · prix non re-vérifié le jour de la rédaction · « J'adore » et « J'adorerais » dans tout wording, y compris les traductions d'avis (règle Tim 24/07 : « I love X » → « J'apprécie beaucoup X », « I'd love » → « J'aimerais beaucoup ») · prix affichés en dollars sur les pages FR (règle Tim 24/07 : TOUJOURS l'euro en premier via le taux indicatif du pied de sources, le montant en dollars uniquement entre parenthèses quand on cite la grille officielle, ex. « ≈ 174 € (189 $) »).

Process de production d'un duel : 1 agent de recherche exhaustive PAR outil (fonctionnalités/docs, utilisateurs, fondateur + X, avis Reddit via archive publique si reddit.com bloque) → grounding persisté dans le dossier du projet → captures d'accueil (Chrome headless) → vignette 1600×840 sans texte + OG 2400×1260 titrée (mesh vert sombre, glyphe deux carrés, « ou » dégradé) → intégration : `POSTS` (Blog.jsx) + `blogposts.<slug>` (fr.extra.json) + route prerender.mjs (title/desc/ogImg/article) → rendu local montré → commit, jamais de push sans validation. Skills `ton-de-voix` + `copywriting` chargés avant rédaction.
