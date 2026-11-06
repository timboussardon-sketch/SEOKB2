---
name: audit-complet-v2
description: "Audit SEO complet d'un site en 9 phases (GSC, crawl, Lighthouse). « audit complet », « audit SEO de [site] »."
---

# Skill — Audit complet V2 (routeur vers le workflow)

## Quand utiliser ce skill

Audit SEO complet d'un site, exécuté selon le workflow canonique : `audit-complet-v2/workflow-audit.md` (9 phases, dérivé de la méthodologie « Workflow V3 » d'Organikk, avril 2026 ; barème du Score SEO global en Phase 7A). Ce skill est un routeur : il ne contient pas la méthode, il OBLIGE à ouvrir le fichier du workflow et à suivre ses 9 phases dans l'ordre, chacune branchée sur le skill dédié (indexation-check, seo-core-web-vitals, seo-quick-win, seo-structure-hn, seo-contenu-pertinence, seo-cannibalisation, maillage-systeme, maillage-interne-gsc, seo-top20-mots-cles-business). 100 % données Google (GSC + crawl + Lighthouse + données terrain CrUX), aucun outil payant tiers, aucun chiffre estimé. Règle mère : un fait mesuré n'est pas automatiquement un frein SEO démontré, chaque finding s'écrit en trois temps (observation prouvée → conséquence justifiée → bénéfice attendu). Sortie obligatoire, toujours les deux : un rapport de pré-décision (diagnostic principal, 3 à 5 chiffres, Score SEO global sur 100 pondéré avec confiance séparée et dimensions non évaluées nommées, 3 problèmes maximum, plan 30 jours avec 3 P1 maximum, opportunités, ce que les données ne permettent pas de conclure) ET un dashboard HTML publié en artifact, pixel perfect sur `reference-dashboard-organikk-co.html` (dans ce dossier, audit organikk.co du 28/09/2026), 8 onglets (Fiche d'identité, Résumé, Indexation, Maillage interne, Contenu et pertinence, Vitesse, Données structurées, Mots-clés business), chaque phase avec une sortie visible, une infobulle de calcul sur chaque score. Sans les deux, l'audit n'est pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "audit de mon site", "audit du site [X]", "audit complet", "audit complet V2", "audite [site ou URL]", "fais l'audit de [site]", "lance l'audit", "lance le workflow audit", "workflow audit complet", "audit SEO de [site]", ou quand il donne une URL de site en demandant un état des lieux global.

NE PAS utiliser ce skill (prendre le skill dédié) quand la demande porte sur UNE seule dimension : indexation seule → indexation-check ; contenu d'une page → seo-contenu-pertinence ; GEO / visibilité IA → seo-geo-audit ; pré-audit avant call commercial → seo-pre-audit ou audit-pre-call ; maillage seul → maillage-systeme / maillage-interne-gsc.

## RÈGLE FONDAMENTALE — comment on écrit un audit

Le 29/09/2026 au soir, en rejetant le style de tous les audits de la journée. Elle passe avant la méthode, avant le score, avant tout. Un audit qui ne la respecte pas ne se montre pas.

> « Arrête de parler comme une IA. Écris comme un expert SEO qui parle à un client : phrases simples, constats directs, pas de jargon inutile, pas de surjustification, pas de formulations du type "écart de contenu", "impact non démontré", "point de mesure" ou "correction certaine".
>
> Tu vois un problème → tu le dis. Tu sais quoi faire → tu donnes l'action. Tu n'as pas assez de données → tu le dis simplement.
>
> Pas besoin de transformer chaque constat en mini-thèse. »

Et, dans le même échange : **« FAIS DES PARAGRAPHES pour aérer les textes, c'est une règle fondamentale. »** Avec une capture d'un bloc de six phrases collées, légendée « interdit ».

Son diagnostic complet, à relire avant d'écrire : « Le problème n'est pas le fond, c'est la manière d'écrire. Tout est sur-structuré, sur-justifié et artificiellement précis. On sent le modèle qui veut prouver chaque phrase au lieu de simplement expliquer ce qui ne va pas. Il faut arrêter d'écrire comme un rapport qui cherche à se défendre devant un tribunal. Donne-moi les faits, ce qu'ils impliquent et ce qu'on fait. Point. »

### Le registre, son exemple mot pour mot

> 56 pages ont juste « SPREAD » comme title → à corriger.
>
> 58 pages n'ont pas de meta description → à corriger, priorité faible.
>
> Les pages offres sont déjà solides → inutile de les gonfler davantage.
>
> Plusieurs chiffres marketing ne sont pas reliés à une preuve → ajouter la source ou le cas client.
>
> La page tarifs n'affiche aucun prix → tester une fourchette ou un prix d'entrée.
>
> Les H3 manquants et sauts H2 → H4 sont secondaires.

### Des paragraphes, toujours

Un constat par paragraphe `<p>`, deux à trois phrases au maximum. Jamais six phrases dans le même bloc. Le découpage compte plus que la marge : un pavé reste un pavé avec 26 px autour.

Côté CSS, l'aération est dans `CSS_MINIS` de `cartes.py`, injectée par `assemble.py`. Piège à connaître : les onglets 2 à 7 vivent dans `.dashwrap`, pas dans `.markdown` ; une règle qui ne vise que `.markdown` ne s'applique pas et les paragraphes sortent à 0 px. Les sélecteurs visent les deux et forcent en `!important` : 26 px entre deux paragraphes, 60 px avant un h3, 48 px avant un h4, 44 px avant un `details.repli`. Se vérifie avec `getComputedStyle`, pas à l'œil.

### Ce qui est supprimé

**Les étiquettes de statut.** Plus de `<span class="tag">mesuré</span>` / déduit / hypothèse / non testable en tête de paragraphe, plus de légende qui les explique. Essayées le 29/09 à sa demande, rejetées le soir même : « les répétitions de "mesuré" sont typiques ». La rigueur reste dans le fond : on n'affirme pas une cause non démontrée, on écrit « à tester » ou « je ne sais pas pourquoi, il faudrait la Search Console ». On ne la balise plus. Contrôle : `grep -cE 'class="tag">(mesuré|déduit|hypothèse|non testable)'` = 0. Attention, la classe `tag` sert aussi aux variantes de mots-clés du top 20 : le grep nu sur `class="tag"` ne rendra jamais 0.

**Les formulations qu'il a citées** : « écart de contenu », « écart de contenu face à ce qu'un prospect vient chercher », « impact non démontré », « ce n'est pas un frein SEO démontré », « correction certaine », « levier mineur », « point de mesure », « dans la SERP observée depuis le point de mesure », « un rôle que les autres pages n'ont pas ? ».

**Les interdits déjà en vigueur** : « laboratoire », le motif « X, mais Y », « Ce que j'ai vérifié », « Ma priorité », « sur le plan technique », « ce que Google voit réellement ».

### Ce qui remplace

| Au lieu de | Écrire |
|---|---|
| « 6e dans la SERP observée depuis le point de mesure » | « 6e dans la SERP que j'ai lue », ou « 6e depuis les États-Unis » |
| une note de méthode sur le lieu de mesure, à chaque chiffre | une phrase, une fois par onglet : « J'ai lu ces résultats depuis les États-Unis, pas depuis la France : sur une recherche locale l'ordre peut différer. » |
| « aucun prix : écart de contenu, test business, impact SEO non démontré » | « La page tarifs n'affiche aucun prix. À tester : une fourchette ou un prix d'entrée. » |
| « Un rôle que les autres pages n'ont pas ? » (en-tête du tableau Contenu) | « Fait doublon avec une autre page ? » |
| un paragraphe qui explique pourquoi on ne peut pas conclure | « à tester », ou « je ne sais pas pourquoi, il faudrait la Search Console » |

Les trois familles **Corrections / Optimisations / Tests business** restent : elles trient les actions. Ne pas les commenter.

## Quel modèle pour quelle étape, et pourquoi ça compte

Un audit produit **26 Mo de relevés** : un rapport Lighthouse pèse 800 à 950 Ko, PageSpeed 9,7 Mo, le graphe de maillage 12 Mo. Si un modèle les ouvre, il avale des millions de jetons pour en tirer trente chiffres.

`digest.py <dossier>` réduit tout ça à 5 Ko. **Aucun agent n'ouvre `lh/`, `psi/`, `maillage/` ni `crawl-initial.json` avec Read.** Un chiffre qui manque s'extrait en trois lignes de Python, jamais en lisant le JSON.

Collecte et rédaction peuvent tourner dans des sous-agents séparés si ta configuration en propose. Sinon tout tourne dans la session : garde alors les relevés lourds hors de la conversation et lis `digest.py`.

## Deux règles, non négociables

**La méthode vit dans `workflow-audit.md`, pas ici.** Ouvrir `audit-complet-v2/workflow-audit.md` et suivre ses 9 phases dans l'ordre. Ce skill ne duplique pas le fichier pour ne jamais diverger de lui : le workflow décide, jamais l'IA. Ne jamais improviser le cadre, les critères ou la priorisation d'un audit.

**Un fait mesuré n'est pas automatiquement un frein SEO démontré**. Chaque finding s'écrit en trois temps : observation prouvée → conséquence ou risque justifié → bénéfice attendu de la correction. « Aucun H1 détecté » est un fait ; « cela bloque la progression SEO » est une interprétation à justifier. Seul un finding complet pèse sur le score ou déclenche une action. L'audit ne cherche pas à être plus volumineux, il cherche à choisir la bonne action.

**Écrire comme un consultant SEO qui explique à son client, pas comme un logiciel d'audit**. Le client doit pouvoir reprendre le texte en rendez-vous sans traduire chaque phrase. Garder les chiffres, les URL, les exemples et la précision ; changer la manière de les expliquer : un langage naturel n'est pas une analyse moins détaillée. Ne pas transformer une recommandation en succession d'étiquettes : pas de cases « dépendance », « confiance », « risque », « signal attendu » remplies systématiquement ; les limites et les vérifications s'intègrent dans les phrases quand elles apportent quelque chose. Verbes directs (« ajouter un lien », « vérifier les recherches », « expliquer la différence entre deux chiffres »), jamais d'abstractions (« établir le ciblage », « mettre les chiffres en cohérence », « appeler la candidature depuis elle »). Pas de bénéfice commercial automatique : expliquer le lien concret avec le parcours du visiteur, sans promettre des clics ou des ventes. Distinguer une erreur confirmée d'un point à vérifier : « 100 entreprises accompagnées » et « 14 missions B2B » ne sont pas forcément contradictoires, il faut d'abord savoir ce que chaque chiffre recouvre.

Ne plus écrire : « Dépendance : aucune. Test de validation : recrawl du graphe. Effort faible, confiance forte, risque faible. » Écrire : « On peut faire cette modification tout de suite. Ensuite, on relancera le crawl pour vérifier que les liens sont bien en place. » Ne plus écrire « Ce qui se décide sans ces données / Ce qui attend des preuves », mais : « On peut déjà clarifier le rôle de ces deux pages. En revanche, on manque encore d'informations pour choisir les recherches à cibler ou décider de les fusionner. »

**Ne pas condenser toute l'analyse en quelques paragraphes**. Le principe pour tout le rapport : **n'essaie pas de montrer tout ce que tu as analysé, fais comprendre ce que tu as trouvé.** Les données prouvent le constat, elles ne deviennent pas le texte. Règles :

- Une idée principale par phrase. Phrases courtes.
- Commencer par le constat le plus important, puis les chiffres qui permettent de le comprendre, puis pourquoi c'est un problème seulement quand ce n'est pas évident, puis ce qu'il faut faire (une liste « À faire » numérotée en fin de section).
- Ne pas mettre toutes les nuances, preuves et réserves dans la même phrase. Ne pas répéter « Google », « indexation », « pages » quand le contexte est évident.
- Interdits : « les anomalies qui restent touchent… », « ce que Google voit réellement », « le score de cette dimension est pénalisé surtout par… », « Ce que j'ai vérifié », « Ma priorité », « Ce n'est pas une validation de… », « sur le plan technique », « selon la langue du navigateur » quand on peut le dire plus naturellement.
- Aucun paragraphe n'est une démonstration méthodologique. Méthode et limites vont dans une petite note séparée, seulement quand elles sont nécessaires.
- Pas de gras au milieu de longs paragraphes pour fabriquer une hiérarchie. Pas de ton « expert » : précis et normal.

L'exemple attendu, à reproduire pour chaque onglet (constat → chiffres → problèmes → À faire → phrase de clôture) :

> Dans l'ensemble, l'indexation du site est bonne. Sur les 30 pages présentes dans le sitemap, 22 sont indexées.
>
> Aucun problème technique majeur ne bloque Google : les 30 pages répondent correctement, aucune n'est bloquée par le robots.txt et les 5 pages analysées en détail peuvent bien être explorées et indexées.
>
> Le problème concerne surtout 8 pages du sitemap qui ne sont toujours pas indexées. Deux sont des pages d'offre, donc je commencerais par celles-ci.
>
> Il y a aussi un problème à corriger sur certaines versions FR/EN : 3 pages ne répondent pas de la même manière selon la langue du navigateur.
>
> Enfin, 76 anciennes URL redirigent aujourd'hui vers une page d'offre sans rapport avec leur ancien contenu. Il faudra revoir ces redirections plutôt que de toutes les envoyer au même endroit.
>
> ### À faire
> 1. Vérifier pourquoi les 2 pages d'offre ne sont pas indexées et les traiter en priorité.
> 2. Corriger le comportement des versions FR/EN.
> 3. Reprendre les 76 anciennes URL et décider lesquelles doivent être redirigées, supprimées ou conservées.
>
> Sur les 30 pages du sitemap, 22 sont donc correctement indexées. Le problème existe. Il est concentré sur quelques groupes d'URL bien identifiés.

Ce qu'il remplace : « Google indexe correctement la majorité de ce que vous lui déclarez : 22 des 30 pages du sitemap sont indexées, les 30 répondent normalement sans rien lui interdire, le fichier robots.txt n'exclut rien, et les cinq pages étudiées sont impeccables, y compris dans ce que Google voit réellement de leur contenu. »

Le ton attendu, exemple à suivre :

> **1. Ajouter des liens vers les pages Audit SEO et Bootcamp**
> Sur les 30 pages analysées, aucune ne contient de lien vers /audit-seo/. Pourtant, la page /methode/ présente déjà l'audit comme la première étape de l'accompagnement. C'est un endroit logique pour proposer au lecteur de découvrir cette offre.
> Pour le Bootcamp, le seul lien vers /bootcamp/ vient du plan du site. Le menu « Bootcamp », présent sur 26 pages, envoie directement vers la candidature, sans passer par la page de présentation.
> Je te recommande donc d'ajouter un lien vers l'audit depuis /methode/ et /systeme/, puis de faire pointer le menu vers /bootcamp/. Le visiteur pourra ainsi découvrir le programme avant d'accéder à la candidature.
> Ces modifications peuvent être faites dès maintenant. Une fois les liens ajoutés, on relancera le crawl pour vérifier qu'ils pointent bien vers les bonnes pages.

Cette règle s'applique au dashboard et à tout texte lu par le client. Le rapport de pré-décision (`wiki/audit/`), lu par l'utilisateur, garde ses tables et ses champs.

**L'ordre de lecture est celui de l'impact** (relecture d'expert, 28/09/2026) : constat brut → impact business → diagnostic → preuve → action → limite de la conclusion. Chaque onglet s'ouvre sur un diagnostic que le client comprend en quinze secondes (« Indexation : 3 pages d'offre ne sont pas indexées », puis la ligne de chiffres), pas sur un relevé technique. Les findings se classent impact business → problème SEO → anomalie technique, jamais sitemap → indexation → canonical. Quand les données éliminent déjà une hypothèse pour une page (12 liens entrants et non indexée : ce n'est pas le maillage), les cas se dissocient page par page avec leur signal principal et leur action, au lieu d'une recommandation générique. Un score qui surprend (« 22 sur 29 indexées, pourquoi 34 ? ») affiche sa raison principale à côté de lui. Une cause déjà comptée dans un finding n'est pas un second finding. Pas d'accumulation de problèmes : la conclusion juste est souvent « la majorité fonctionne, les anomalies restantes touchent des pages commerciales », plus précise et plus inquiétante pour les bonnes raisons. Les constats qui répondent à une autre question (des requêtes business sans impression relèvent des mots-clés, pas de l'indexation) changent d'onglet.

## Règles obligatoires dans TOUS les audits. Interdit de ne pas les respecter.

Elles s'appliquent à chaque audit, quel que soit le site, avec ou sans Search Console. Un livrable qui en manque une n'est pas terminé et ne se montre pas.

1. **Le top 20 des mots-clés business est toujours dans l'onglet 7.** Il ne dépend pas de la Search Console : il vient de Google Keyword Planner (exports CSV de Google Keyword Planner que l'utilisateur fournit : deux passes d'idées, une passe de métriques exactes ; `planner_csv.py` les convertit en `planner.json`) puis de la chaîne des cinq skills mots-clés (`seo-recherche-mots-cles`, `seo-clustering-mots-cles`, `seo-mots-cles-resistants-ia`, `seo-mots-cles-decisionnels`, `seo-modeles-pseo`). Tableau : rang, mot-clé (variantes regroupées), déjà sur le site ?, volume/mois, CPC, note /10 (outil de tri, dit comme tel), clic après réponse IA, Search Console 90 j (sans Search Console, la colonne devient « Concurrence Ads », lue dans Keyword Planner), décision. Le tableau se génère depuis les données du site. Les gros volumes écartés vont dans un tableau à part avec la raison. La trace part dans `wiki/keywords/recherche-AAAA-MM-JJ-<site>-google-ads.md`. Écrire « non testable » à la place de ce tableau est une faute (29/09 : trois audits publiés sans lui, « MAIS OU SONT LES 20 mots clés business ???? »).
2. **Le mot « laboratoire » est interdit.** Écrire « test », « test Google » (PageSpeed Insights), « depuis mon poste » (Lighthouse local). Phrase fixe sans terrain : « Expérience réelle non évaluée ; les mesures de test, elles, sont disponibles. »
3. **Onglet Contenu, tableau page par page, en-têtes en mots de client** : Page · Ce que Google affiche sur cette recherche · Ce qu'est la page · Ce qu'un prospect cherche et ne trouve pas · Chiffres et promesses sans preuve · Fait doublon avec une autre page ? · Titre et description dans Google · Verdict. Jamais « Question sans réponse », « Affirmations sans appui », « valeur propre », « intention » (29/09 : « on comprend rien »).
4. **Onglet Vitesse en cartes de score, pas en tableau de chiffres.** `cartes.py` (dans ce dossier) : `cartes_terrain(mobile, desktop, note)` donne une carte par mesure réelle (affichage, réactivité, stabilité) ou une carte « n. d. » ; `cartes_pages(pages, principal)` donne une carte par page avec le score en gros, le temps d'affichage, puis ordinateur, mon poste, serveur et ce qui bloque en ligne source. Les tableaux restent possibles en complément replié, jamais seuls.
5. **Pied de la barre latérale** : une seule ligne, sans bouton de prise de rendez-vous. Rien d'autre.
6. **Le motif « X, mais Y » est interdit**. Deux phrases, ou « Seul problème : », « En revanche, », « lui, ». Écrire « Indexation : 61 pages sans problème. L'accueil dépend entièrement du JavaScript. », jamais « 61 pages propres, mais l'accueil n'existe qu'après JavaScript ». Vérification mécanique avant de montrer : `grep -c ", mais "` sur le HTML doit rendre 0.
7. **Ton** : les règles d'écriture ci-dessus (constat → chiffres → À faire, phrases courtes, pas de démonstration de méthode) valent pour chaque onglet et pour le rapport.

### Règles système ajoutées le 29/09/2026

Trois règles mères, puis leurs applications. Toutes obligatoires.

- **Une observation certaine ne rend pas son impact SEO certain.** Un prix absent, un H1 → H3, un contenu rendu côté client sont des mesures ; leur effet sur le classement est une déduction ou une hypothèse, et se dit comme tel. Seule une gravité mesurée retire des points, jamais un effet supposé.
- **Une corrélation dans la SERP ne s'écrit jamais comme une causalité sans preuve.** « 3 liens internes » et « absente des 9 premiers » sont deux mesures ; « absente parce que 3 liens » est une hypothèse à tester (renforcer, puis relire la SERP). Formulation imposée : « hypothèse à tester », jamais « explique », « à cause de », « les 3 liens qu'elle reçoit, peut-être ».
- **Une métrique a une définition unique et une valeur cohérente dans tout le rapport.** Un comptage de mots (contenu principal, hors menu, pied et bandeaux, code initial ; accueil rendu client : « 0 → 2 849 »), une position, un temps serveur gardent la même définition de l'onglet 0 à l'onglet 7. Trois mesures « serveur » existent et ne se confondent pas : premier octet depuis mon poste (Lighthouse, navigation complète), traitement serveur seul (`server-response-time`, ligne source des cartes), premier octet du test Google (mesuré depuis le réseau de Google, contre un cache). Le rapport les nomme et dit laquelle il utilise.

Applications :

8. **Ton et mise en page** : voir la RÈGLE FONDAMENTALE en tête de ce fichier. Elle prime sur tout le reste. Contrôle avant de montrer : `grep -cE 'class="tag">(mesuré|déduit|hypothèse|non testable)'` = 0, `grep -c 'point de mesure'` = 0, `grep -c ', mais '` = 0, et une capture par onglet pour vérifier l'aération.
9. **Sans Search Console, l'onglet 2 s'appelle « Indexabilité »**, dans la barre latérale (`assemble.py` le fait quand `GSC=False`), la carte, le tableau du score et le titre de l'onglet. Il mesure ce qui peut empêcher l'indexation, pas l'indexation. Formule : « N pages sans blocage technique d'indexation détecté », jamais « sans problème d'indexation ». Les adresses inventées se jugent sur le **code HTTP** (404 ou 410 vérifié dans `soft404.txt`), jamais sur l'affichage d'une page « introuvable ».
10. **Rendu côté client** : écrire « le contenu principal et les liens de l'accueil dépendent du JavaScript », jamais « l'accueil dépend entièrement du JavaScript » (le menu et le H1 sont dans le code initial).
11. **Le score s'appelle « Santé technique et on-page du périmètre audité »**, jamais « Score SEO » : il dit l'état des pages, pas la place dans Google. **Couverture et confiance** s'affichent à part (pages lues / contrôlées, données non observées nommées : indexation réelle, recherches, clics, visiteurs réels, conversions). Une dimension non observable faute de données ne reçoit pas une note élevée par défaut : elle est notée sur ce qui est mesurable et dit ce qui ne l'est pas (Indexabilité ≠ indexation).
12. **Pondération des défauts** : un défaut Hn mineur (H1 → H3 sans H2) vaut −2 au plus sur sa dimension à 10 %, jamais −5 ; il ne pèse pas comme un rendu client ou un défaut d'architecture. L'absence de prix, une promesse absente, un contenu que les pages affichées donnent et pas le site : **écart de contenu / opportunité business / test CRO-SEO**, jamais « le problème principal », jamais une pénalité (29/09 : −12 retirés pour un prix absent, refusé).
13. **Les recommandations se classent en trois familles** : **Corrections** (défaut mesuré, résultat certain : texte de démonstration lu par Google, rendu serveur du contenu principal, formules absentes de la page qui les vend), **Optimisations** (amélioration attendue, résultat à observer : renforcement du maillage, H2 manquant), **Tests business** (contenu et conversion, hors score : ajout de prix, page prix). Un dashboard qui met le prix en Correction SEO certaine est faux.
14. **Maillage** : jamais « 90 à 110 liens sortants diluent tout ». Écrire sur la hiérarchie et la distribution : « la hiérarchie des liens ne suit pas celle des offres », « la page hiérarchise ce qu'elle relie ».
15. **SERP** : une position s'écrit « 6e dans la SERP observée depuis le point de mesure », jamais « 6e sur Google ». Le point de mesure est nommé (ce poste sort aux États-Unis ou ailleurs, jamais en France : Google renvoie une page sans résultats à `curl` avec `gl=fr`). Une SERP locale (ville, département) se relit depuis la France avant de conclure ; tant que ce n'est pas fait, le rapport le dit dans chaque onglet qui la cite. **La même requête, au mot près, partout** : « développeur web freelance site vitrine sur mesure » ne devient pas « site vitrine sur mesure » deux onglets plus loin.
16. **Onglet Vitesse** : en plus des cartes, un tableau « D'où vient le temps, page par page » : élément principal (nœud LCP, `lcp-breakdown-insight` de Lighthouse 13), premier octet, délai de chargement, durée de chargement, attente du rendu, affichage. Un élément texte a délai et durée à 0, le dire. Le texte parle du « H1 » ou du « paragraphe principal », pas du « titre » (ambigu avec le title).
19. **La confiance s'affiche et s'explique, en texte visible**. Une confiance rangée dans une infobulle au survol ne compte pas comme affichée. Il faut, sans survol : la confiance globale **à côté du score global partout où le score apparaît** (carte Site, tête du Résumé, texte du bouton « Copier le résumé pour Claude ») ; une phrase qui dit **ce que la confiance mesure** — non pas l'état du site, mais sur combien de preuves directes le score repose ; une **échelle de lecture de la confiance** affichée comme celle du score (au-dessus de 85 %, preuves directes et complètes ; de 60 à 85 %, un échantillon ou des mesures de test seules ; en dessous de 60 %, il faut les données manquantes avant de décider) ; et **par dimension, la raison de sa confiance en clair dans le tableau ou juste en dessous** : ce qui a été mesuré, sur combien de pages, ce qui manque, nommé. Le calcul de la confiance globale reste montré (moyenne pondérée par les mêmes poids que le score, et la renormalisation dite quand une dimension sort du total). Les infobulles restent, en plus du texte, jamais à sa place.

20. **Le vocabulaire de méthode ne sort pas sur la page**. Trois règles : un problème vu se dit ; une action connue se donne ; une donnée qui manque se dit simplement. Interdits dans tout texte lu par le client : « écart de contenu », « impact non démontré », « point de mesure », « correction certaine », « portée stratégique », « gravité mesurée », « finding en trois temps », et « non testable » partout où « je n'ai pas la donnée » suffit. Les statuts mesuré / déduit / hypothèse restent une discipline de raisonnement : ils se disent en français dans la phrase (« à vérifier », « c'est ma piste, pas une certitude »), ils ne s'affichent plus comme des étiquettes. La doctrine ne change pas, seule sa mise en mots change : on ne confond toujours pas une mesure et son effet, et chaque chiffre garde sa base.

21. **Faire des paragraphes pour aérer**. Une idée par paragraphe, deux à quatre lignes, une ligne blanche entre chaque. Un paragraphe qui enchaîne trois constats devient trois paragraphes. Jamais de pavé de six phrases, même bien écrit, dans aucun onglet. Le format attendu est un constat suivi de son action, ligne par ligne : « 58 pages n'ont pas de meta description → à corriger, priorité faible », « la page tarifs n'affiche aucun prix → tester une fourchette ou un prix d'entrée », « les sauts H2 → H4 sont secondaires ».

22. **La confiance suit ce qui a été mesuré, et le maillage n'est pas une dimension comme les autres** (constat du 29/09/2026 au soir : sur dix-huit audits du jour, onze sortaient à exactement 70 % de confiance globale, et neuf portaient le même vecteur 60/60/70/90/90/80). Trois règles.

    **Le maillage suit la part du site crawlée, sans exception.** C'est un graphe : un crawl partiel donne un graphe partiel, et ce qu'on dit des pages orphelines, des impasses ou de la hiérarchie des liens ne vaut que sur ce qui a été parcouru. 400 pages crawlées sur 685, c'est 58 % de confiance sur cette dimension, pas 80 %.

    **Les cinq autres dimensions se calculent sur ce qui a été mesuré pour elles, et le livrable dit la taille de l'échantillon.** Ce sont des contrôles page par page : sur un site à gabarits, 200 pages homogènes disent beaucoup des 685. Ne pas appliquer mécaniquement la part du site à ces dimensions. Un audit qui annoncerait 29 % de confiance sur l'indexabilité après avoir contrôlé 200 pages identiques serait aussi faux qu'un audit qui annoncerait 90 % après en avoir vu dix. Ce qui compte est de nommer l'échantillon : « contrôlé sur 200 des 685 pages, toutes bâties sur le même gabarit ».

    **Le vecteur ne se recopie jamais d'un audit à l'autre.** Seules les valeurs qui viennent d'une cause commune se répètent légitimement : sans accès à la Search Console, l'indexabilité et le contenu plafonnent partout, et c'est normal. Tout le reste se calcule site par site. Deux audits de sites différents qui sortent le même vecteur : il a été recopié. Avant de rendre, comparer le vecteur de confiance au vecteur de couverture.

18. **Chaque onglet s'ouvre sur des mini-cartes puis un graphique, sans jargon**. Composants dans `cartes.py` (ce dossier), CSS injecté par `assemble.py` (`CSS_MINIS`) : `minis([(valeur, phrase en mots de client, ton)])` donne 3 ou 4 cartes **en bleu Organikk grainé** (dégradé outremer #2f4fe0 → #7fa0ff avec le grain de la DA, texte blanc, sans bord gauche coloré : l'utilisateur a refusé le liseré épais du 29/09) où le ton ne colore qu'un point devant la phrase (vert / orange / rouge / bleu / gris ; la phrase dit ce que le chiffre veut dire pour le client : « pages que Google peut lire et garder », pas « URL en 200 ») ; `barres(titre, [(libellé, valeur, ton)], unité, seuil=…, ton=fonction)` donne un graphique en barres avec repère pointillé (2,5 s pour l'affichage) ; `pile(titre, segments)` une répartition (liens du menu / bandeaux / texte, pages par famille) ; `graf_vitesse(PAGES)`, `graf_vitesse_poste(PAGES)`, `graf_volumes(D)` sont automatiques (le dernier lit `top20_rows.json` écrit par `top20.py`). Par onglet : Fiche = pages du sitemap, pages lues, accès Search Console, technologie + répartition par famille ; Résumé = barres « où chaque sujet en est, sur 100 » sous le tableau du score ; Indexabilité = pages lisibles, bloquées, fausses adresses, rendu JavaScript + mots avant JavaScript par page ; Liens = liens du texte, min vers les offres, max, contact + barres reçus par page et pile menu / bandeaux / texte ; Contenu = corrections certaines, écarts, pages sans rien à corriger, Hn + mots par page ; Vitesse = test Google, mon poste, pages qui attendent le JavaScript, visiteurs réels + les deux graphiques automatiques ; Données structurées = pages valides, contradictions, fil d'Ariane, corrections + types par pages ; Mots-clés = recherches lues, présence, 20 triés, la plus demandée + volumes du top 20. Dans une vue en f-string, écrire `{minis(...)}`, jamais `""" + minis(...) + """` (29/09 : les `{R['g_min']}` sont sortis en clair sur edeveloppe). Vérifier une capture par onglet avant de publier (capture avec Playwright).
17. **Top 20 : la formule est écrite dans le tableau** (`top20.py`) : note = proximité business × intention × faisabilité ÷ 12,5, trois composantes de 1 à 5, arrondie, 5 × 5 × 5 = 10 ; aucun bonus stratégique dans la note, la colonne Décision porte les raisons hors note ; le volume n'entre pas. La colonne s'appelle **« Probabilité estimée de clic après réponse IA »** (jamais « Clic après réponse IA », ce n'est pas une mesure) et la méthode fort / moyen / faible est écrite au-dessus du tableau (prestataire, lieu, achat → forte ; guide, méthode → moyenne ; définition, comparatif → faible).

## Les fichiers de ce dossier

- `base-reference.html` : la coque du dashboard (8 onglets, DA outremer). Ne pas la modifier.
- `assemble.py` : remplit la coque. `python3 assemble.py <site> <chemin/vues.py> <sortie.html>`. Le module de vues expose `SITE`, `DATE`, `SOUS_TITRE` (facultatif), `GSC` (True / False) et `V`, la liste des 8 onglets en HTML (0 Fiche d'identité à 7 Mots-clés business).
- `cartes.py` : mini-cartes et graphiques (`minis`, `barres`, `pile`, `graf_vitesse`, `graf_vitesse_poste`, `graf_volumes`), importé par `assemble.py` et par les vues.
- `planner_csv.py` : convertit les exports CSV de Keyword Planner en `planner.json`. `python3 planner_csv.py <dossier-audit>/<site> --idees idees.csv [idees2.csv] [--exacts metriques.csv]`. Une fourchette ou une cellule vide reste « non mesuré », jamais 0.
- `top20.py` : le tableau du top 20 de l'onglet 7. `python3 top20.py <dossier-audit> <site> [date du relevé]`. Il lit `<dossier-audit>/<site>/planner.json` (export Keyword Planner) et `top20_site.py` (vos 20 lignes notées), et écrit `top20.html` et `top20_rows.json` (lu par `graf_volumes`).
- `reference-dashboard-organikk-co.html` : un audit terminé, le modèle visuel à atteindre.
- `workflow-audit.md` : les 9 phases de la méthode.

## Le squelette : phases, skills, onglets

| Phase du workflow | Skill | Où ça s'affiche | Source |
|---|---|---|---|
| 0 · Positionnement | prompt du fichier ; `seo-top20-mots-cles-business` si l'utilisateur ne fournit pas les requêtes business | Onglet 7 Mots-clés business ; nourrit toutes les autres phases | GSC + recherche web |
| 1 · Indexation | `indexation-check`, avec son contrôle du rendu et le relevé des actions manuelles / problèmes de sécurité | Onglet 2 | sitemap + URL + inspection Google |
| 1bis · Vitesse | `seo-core-web-vitals` : Lighthouse pour le diagnostic, données terrain p75 pour l'évaluation | Onglet 5 | Lighthouse local + API PageSpeed Insights |
| 2 · Quick Wins | `seo-quick-win` | Onglet 7, section « Gains rapides » ; actions prioritaires reprises dans le Résumé | GSC + Chrome |
| 3 · Contenu | `seo-contenu-pertinence` sur les pages prioritaires, `seo-structure-hn` sur le sitemap complet en sous-contrôle | Onglet 4 Contenu et pertinence | crawl + GSC + recherche web SERP |
| 4 · Cannibalisations | `seo-cannibalisation`, trois états, aucun seuil de taille | Onglet 7, section « Coexistences et cannibalisations » | GSC + Chrome |
| 5 · Maillage | `maillage-systeme` (structure, sans GSC) puis `maillage-interne-gsc` (data) | Onglet 3 | crawl liens + GSC |
| 6 · Synthèse | prompt du fichier, six passes | Onglet 1 Résumé | objets des phases 0 à 5 |
| 7 · Rapport + score | prompt du fichier, grille pondérée de l'Étape 7A, quality gate, reviewer | Onglet 1 Résumé + rapport `wiki/audit/` | objets de la phase 6 |

Une phase nourrit la suivante : ne pas paralléliser ce qui dépend d'une phase amont. Les onglets 0 (Fiche d'identité) et 6 (Données structurées) n'ont pas de phase du workflow : leur contenu est défini ci-dessous.

## Données et pré-requis

- **Objectifs business confirmés par le client**, recueillis avant l'audit : offres prioritaires, marchés réellement servis, type de conversion (rendez-vous, devis, vente, inscription). Ils s'écrivent dans la Fiche d'identité, séparés de ce que le site dit de lui-même.
- **Données de conversion** (GA4, CRM, formulaire) quand elles existent et sont fiables. Sinon, le Résumé porte la phrase fixe (voir bloc « Ce qui progresse »).
- **GSC** en priorité par le MCP du site s'il existe (ex. `gsc-organikk`), sinon API ou export. Avec l'accès à la propriété : rapports Actions manuelles et Problèmes de sécurité de l'interface, l'inspection d'URL ne les couvre pas.
- **Lighthouse** en local au terminal ; clé API PageSpeed Insights pour les données terrain. Sans terminal : Phase 1bis « non testable », dite comme telle.
- Aucun chiffre estimé ou inventé. « Non indexée » et « non testable » restent deux états distincts.

## Orchestration

Le multi-agents (outil Workflow) est autorisé pour la collecte à l'échelle, à une condition : les phases, critères et consignes de chaque agent viennent du fichier workflow et des skills dédiés, pas de la tête de Claude. Contre-vérifier les constats critiques et hauts avant publication : un vérificateur reproduit chaque preuve.

## Discipline de précision 

À appliquer à toutes les phases.

- **Cohérence numérique entre bases.** Chaque pourcentage ou ratio nomme sa base (sur combien de pages, quel périmètre) ; deux chiffres voisins restent arithmétiquement compatibles avant publication.
- **Un échantillon ne devient jamais une conclusion globale sans le dire.** 4 pages sur 22 confirmées « inconnues de Google » : le problème est confirmé sur les 4 testées, pas sur les 22. Le gabarit commun justifie de vérifier le reste en priorité, jamais d'extrapoler.
- **Une métrique répond à la question de sa section.** Une URL rejoint le sitemap sur une question binaire (canonique, indexable, voulue dans Google), pas sur ses impressions ou ses liens entrants.
- **Une classification d'outil tiers se décompose en faits.** Le `coverageState` de Google est une étiquette : statut HTTP observé, contenu servi, canonical calculé, puis l'étiquette, quatre faits distincts.
- **La sévérité suit la preuve d'impact.** Un mismatch de canonicalisation est une incohérence à nettoyer, pas une catastrophe, sauf preuve chiffrée. Citer la recommandation officielle de Google quand elle existe plutôt qu'assumer le pire.

## Sortie 1 — le rapport de pré-décision

Fichier `wiki/audit/YYYY-MM-DD-slug.md`, format `audit-complet-v2/rapport-audit-seo-format.md` (`audit-complet-v2/rapport-audit-seo-format.md`). Dans cet ordre :

1. Diagnostic principal : une phrase, la cause structurante, pas une liste d'erreurs.
2. Les chiffres à retenir : 3 à 5, ceux qui illustrent le diagnostic.
3. Score SEO global sur 100, pondéré par dimension, confiance séparée en %, dimensions non évaluées nommées et score dit « partiel » le cas échéant (grille : workflow, Phase 7A). Chaque dimension reste factuelle dans son onglet ; seule la synthèse porte un score et une lecture.
4. Problèmes (3 maximum) et opportunités (5 maximum), séparés : Preuve (2 à 4 données), Pourquoi c'est important, Action, Confiance (forte / moyenne / faible). Chaque problème en trois temps : observation prouvée → conséquence ou risque justifié → bénéfice attendu.
5. Actions P1 / P2 / P3, 3 P1 maximum : pourquoi, preuve, signal attendu (jamais un résultat chiffré promis), **dépendance préalable**, **test de validation** (ce qui distingue « correction appliquée » de « résultat SEO observé »), effort Faible / Moyen / Élevé (jamais en heures), confiance, risque Faible / Moyen / Élevé. Toute action à risque élevé (suppression, 301, fusion, changement d'URL) porte « À valider avant déploiement » et sa checklist.
6. Ce que les données ne permettent pas de conclure, avec « données insuffisantes » ou « ne rien faire » quand c'est le cas, et toujours la ligne « Autorité externe non évaluée » quand aucune donnée de liens n'a été regardée.

Puis le plan des 30 prochains jours (Maintenant, 3 actions max · Ensuite · À surveiller), l'analyse détaillée repliable et les annexes par phase.

**Le barème vit dans le workflow**  : pondération par dimension, pénalités par gravité d'une cause validée, plafonds, confiance séparée, lecture, format de restitution, en Phase 7 Étape 7A. Ce skill l'applique, ne le reproduit pas. Deux règles à ne pas perdre en l'appliquant : l'observation seule ne retire aucun point ; une dimension non évaluée sort du total (poids renormalisés) et s'affiche « non évaluée », jamais 100 par défaut.

**Règles d'écriture.** Chaque information est typée FACT, HYPOTHESIS ou ACTION ; un problème existe une seule fois, les observations qui en parlent fusionnent ; une anomalie n'est pas une priorité par défaut ; les pages business et les tendances GSC passent avant les anomalies techniques secondaires ; jamais de recommandation automatique de fusion, 301, suppression, réécriture ou création de page ; Google n'est jamais anthropomorphisé. Priorisation selon la doctrine du vault : élagage en 301 jamais en 410 quand une page équivalente existe, meta tags en levier mineur, jamais d'achat de lien. Aucun ID technique ni mot anglais (low / medium / high) ; la certitude affichée ne dépasse jamais la couverture des données (« aucun problème majeur détecté sur les URL inspectées », pas « Sain ») ; aucune action sur une page dont les requêtes ne sont pas connues (« à vérifier ») ; le nombre de mots seul n'est jamais un problème. Longueurs : diagnostic 70 mots, 4 chiffres, 3 problèmes de 40 mots, 6 actions, 3 opportunités de 35 mots, le reste replié. Ton factuel, mots bannis de l'utilisateur respectés, pas de tiret cadratin, aucune des phrases « Il est important de », « Il convient de », « Cela peut potentiellement », « Il est intéressant de noter », « Dans le cadre de ».

**Structure d'une priorité dans un onglet** (validée le 23/09/2026, référence [[audit/2026-09-22-organikk-co]]) : une phrase de cadrage, « Ce qu'on observe » (faits chiffrés en liste, pages en code), « Pourquoi c'est prioritaire » (deux phrases), « Action » (liste numérotée courte), « Impact attendu » et « Risque » en gras ; puis « à surveiller avant d'agir » pour la page dont la cause n'est pas isolée ; puis « Autres pages à surveiller » : chiffres séparés par « · », une phrase, verdict en gras (« Aucune action recommandée », « À vérifier avant toute modification »).

## Sortie 2 — le dashboard HTML

Publié en artifact, avec le rapport de pré-décision qui l'alimente. Sans lui, l'audit n'est pas terminé.

**Carte « Site » du Résumé**  : l'anneau porte le score en gros, seul (`.av.score`, sans avatar, sans initiale, sans pastille), avec son infobulle de calcul. Ni logo ni lettre : un logo embarqué se rendait décalé, l'utilisateur a tranché pour le score.

**Référence pixel perfect : `reference-dashboard-organikk-co.html`**, dans ce dossier (audit organikk.co du 28/09/2026, 5 pages, version 8 publiée). 28/09 : « c'est pixel perfect ce que chaque audit doit donner ». Chaque audit part de ce fichier, en garde la coque telle quelle (CSS, sidebar, cartes, tableaux, pastilles, infobulles `.aide`, blocs repliés `details.repli`, JS de navigation, retouche visuelle du 28/09 : cartes-liens sans soulignement, nombres à 44 px, légende courte puis détail en gris, pastilles du profil en lignes, ombres douces) et ne remplace que le contenu. Ne jamais redessiner la DA. `assemblage-exemple-organikk-co.py` montre comment le contenu de chaque vue a été injecté dans la coque (`view(n, html)`) : reproduire cette mécanique, pas réécrire l'HTML à la main. Toute correction demandée sur un onglet se répercute dans le skill dédié ET dans la référence.

**Ce que la référence contient, et que chaque audit reproduit onglet par onglet :**

- **0 Fiche d'identité** : titre « site : N pages auditées, sur M déclarées au sitemap », périmètre avec les bases nommées, « ce que le site dit de lui-même » (table), « objectifs business, à confirmer par le client » (bloc séparé, avec la phrase qui dit s'ils ont été confirmés), les pages du périmètre avec impressions / clics / position, « comment cet audit a été mené », sources datées (dont Keyword Planner si utilisé).
- **1 Résumé** : bouton « Copier le résumé pour Claude » avec le texte brut ; carte Site (gros score dans l'anneau + infobulle, deux lignes de contexte, trois pastilles chiffre en gras) ; six cartes-chiffres cliquables (Indexation, Contenu, Maillage, Vitesse, Données structurées, Mots-clés), chacune avec titre en noir, nombre, légende courte, détail gris, infobulle ; carte Mesures connectées ; Diagnostic principal ; bloc « Ce qui progresse, régresse et compte pour l'activité » (table A → B, une phrase par mouvement, phrase fixe sans conversion) ; Score SEO (table dimension / score / poids / contribution / confiance, infobulle sur chaque score, chaque confiance et le global, paragraphe des pénalités) ; État par zone ; Les trois actions (dépendance, test de validation, effort, certitude, risque) ; Ce qui bloque (barres, infobulle par ligne) ; Sortie visible de chaque phase (table des 9 phases + analyses conditionnelles) ; Ce que cet audit ne peut pas voir (dont « Autorité externe non évaluée »).
- **2 Indexation** : titre en diagnostic, ligne des comptes, paragraphe lisible en quinze secondes avec la raison du score, périmètre ; findings en trois temps classés par impact avec les cas dissociés page par page (table page / rôle / signal principal / action) ; « Ce qui ne bloque pas » ; conclusion ; preuves repliées (inspection Google de tout le sitemap en deux colonnes sitemap / pages référentes, contrôles HTTP-robots-404, rendu sur deux versions, état HTTP des URL hors sitemap) ; ce que les données ne permettent pas de conclure.
- **3 Maillage interne** : table des liens du corps par page (entrants, sources, ancres, navigation, sortants), ce que Search Console ajoute, priorités par rang justifié (observation, conséquence, bénéfice, test).
- **4 Contenu et pertinence** : table par page (format attendu SERP, format servi, question sans réponse, affirmations non étayées, valeur propre, title / meta, verdict) ; ce qui bloque en trois temps ; ce qui n'est pas retenu ; sous-contrôle Hn en table.
- **5 Vitesse** : terrain d'abord (table p75 mobile / ordinateur avec périmètre URL ou origine), test ensuite (table par page), qualité de la mesure (variance, mesures écartées), décomposition du LCP, priorités, non retenu, ce que la mesure ne permet pas de conclure.
- **6 Données structurées** : table des trois contrôles (validité, correspondance au visible, fonctionnalité visée), le point le plus net, note de clôture.
- **7 Mots-clés business** : verdict en deux phrases + « Diagnostic partiel », les décisions proposées (impact, certitude, effort), ce que l'analyse ne permet pas de conclure, table recherche → offre → résultat commercial → reste à établir, preuves par opportunité, **top 20 avec volume, CPC, note /10, clic après réponse IA, Search Console, décision** (Keyword Planner + chaîne des cinq skills ; l'utilisateur le demande explicitement, le nommer outil de tri), exclusions et vérifications repliées.

### Les 8 onglets, dans cet ordre

| # | Onglet | Ce qu'il porte |
|---|--------|----------------|
| 0 | Fiche d'identité | Ce que le site dit de lui-même (promesse, hébergement, robots), familles de pages avec leur nombre, méthode et sources datées. **Objectifs business confirmés par le client**, dans un bloc séparé de la promesse affichée. Markdown simple (`.markdown`). |
| 1 | Résumé | Score SEO (grille du workflow), **chaque score avec une infobulle** (composant `.aide` de la coque) qui donne le calcul et le pourquoi : par dimension, le départ à 100, chaque cause retenue avec sa gravité, sa portée et ses points, ce qui a été vu mais non retenu ; par confiance, ce qui a été mesuré et ce qui manque ; sur le global, l'arithmétique pondérée et les plafonds testés ; sur chaque ligne de « Ce qui bloque », la gravité et pourquoi pas le cran au-dessus. Bloc **« Ce qui progresse, régresse et compte pour l'activité »**, État par zone (Zone / État / Pourquoi), Diagnostic principal, Les trois actions à faire maintenant (dont celles venues des Gains rapides et des cannibalisations quand elles sont prioritaires), Ce qui bloque, Ce que ça ne permet pas de conclure (avec « Autorité externe non évaluée » le cas échéant), analyses conditionnelles déclenchées ou non et pourquoi. |
| 2 | Indexation | `indexation-check`, section « La preuve, la conclusion et la priorité doivent correspondre » (28/09) : verdict en tête, qui peut être « aucun défaut confirmé » ; findings établis en trois temps ; « ce qui ne bloque pas » (hors sitemap = constat, champ `indexed` obsolète exclu) ; conclusion ; preuves repliées (inspection Google de tout le sitemap avec `sitemap` et `referringUrls` en deux colonnes, contrôles HTTP et robots évalués, rendu sur deux versions comparées texte et destinations, état HTTP actuel des URL hors sitemap). Vérifications ouvertes terminées avant livraison, ou périmètre assumé dans le titre. Actions manuelles et sécurité : non vérifiés, interface requise. |
| 3 | Maillage interne | `maillage-systeme` (piliers, hubs, orphelines, impasses, ancres ; comptage par sources distinctes et liens du corps) chaîné avec `maillage-interne-gsc` (hiérarchie mère / fille, pages fortes sous-liées, tendances). Priorité justifiée par rangs, pas de score. |
| 4 | Contenu et pertinence | `seo-contenu-pertinence` sur les pages business prioritaires + un échantillon motivé des autres familles (intention et format lus sur la SERP réelle, question importante sans réponse, crédibilité des affirmations qui pèsent, valeur propre, title et meta systématiques), chaîné avec `seo-structure-hn` sur le sitemap complet (huit observations Hn, gravité jamais automatique). Aucune page notée sans savoir quelle version a été lue. |
| 5 | Vitesse | `seo-core-web-vitals`, gabarit « Output obligatoire » : Lighthouse pour le diagnostic (LCP décomposé, alerte redirections), **données terrain LCP / INP / CLS au 75e percentile** avec leur périmètre (URL ou origine, mobile ou desktop, 28 jours) pour l'évaluation. Mobile par défaut, desktop si l'usage ou les résultats le justifient. Sans terrain : « Expérience réelle non évaluée ; les mesures de test, elles, sont disponibles. » |
| 6 | Données structurées | Pas de skill d'audit dédié ; protocole ci-dessous. |
| 7 | Mots-clés business | `seo-top20-mots-cles-business`, section « Ce que le client lit » (28/09) : un verdict en tête (« Diagnostic partiel » si requêtes ou conversions manquent), jamais de note sur cet onglet ; les décisions proposées avec, pour chacune, l'offre, l'action justifiée et le résultat commercial à suivre (impact attendu, certitude, effort, séparés) ; ce que l'analyse ne permet pas de conclure ; le tableau recherche → offre → résultat commercial → reste à établir ; les preuves regroupées par opportunité (une page une seule fois) ; exclusions et vérifications repliées. Les sorties de `seo-quick-win` et `seo-cannibalisation` s'y fondent sans leurs noms de phase : des apparitions sans clic s'écrivent « ciblage à vérifier », pas « gain rapide » ; un recouvrement de contenu s'écrit « offre proche, rôle à clarifier », pas « conflit probable » sans requêtes communes. Aucun terme de procédure (portes, phases, capté, exposé) dans le texte client. Requêtes absentes de l'extraction : établir pourquoi, jamais « lire dans l'interface ». |

Chaque onglet suit le gabarit de son skill dédié à la lettre : ce routeur ne les duplique pas, il assemble.

### Chaque phase a une sortie visible

Pour les neuf phases, le livrable dit laquelle de ces quatre formes s'applique, une seule : **résultats** (ce que la phase a trouvé, chiffres et base) · **aucune anomalie retenue** (la phase a tourné sur N pages, rien ne pèse, et pourquoi) · **non testable** (ce qui manquait et ce qu'il faudrait) · **échec d'exécution** (lancée, non aboutie, cause). Une absence de résultat n'est jamais ambiguë. Les Quick Wins et les cannibalisations ont longtemps tourné sans apparaître : la règle vient de là.

### Bloc « Ce qui progresse, régresse et compte pour l'activité » (Résumé, obligatoire)

Répond à une question : où la performance change-t-elle, depuis quand, et quelles pages business sont concernées ?

1. **Périodes comparables** : la période analysée contre la précédente de même durée (90 contre 90), et contre N-1 quand l'activité est saisonnière.
2. **Segments seulement s'ils changent le diagnostic** : familles de pages, marque / hors marque, pays, appareil. Une baisse portée par un seul pays ou le seul mobile n'est pas une baisse du site.
3. **Les positions GSC sont des moyennes**, qui varient selon le lieu, l'appareil et le moment. Un mouvement de position moyenne se qualifie après avoir vu de quelles requêtes il vient (organikk.co, 26/09 : 5,9 → 30,6 par des impressions ajoutées très bas, pas une perte sur les requêtes qui comptent).
4. **Objectifs business confirmés par le client**, pas ce que le site dit de lui-même.
5. **Conversions** : si disponibles et fiables, elles priorisent. Sinon, la phrase fixe : « L'importance commerciale est estimée à partir de l'offre et des objectifs du client ; la contribution aux conversions n'est pas mesurée. »
6. **Potentiel commercial et résultat observé** : deux colonnes, jamais confondues.

GSC ne représente pas tout le marché (requêtes anonymisées, lignes non restituées) : l'absence d'une requête n'écarte rien, la recherche web des intentions non couvertes tourne même avec GSC.

```markdown
## Ce qui progresse, régresse et compte pour l'activité

Période [A] contre [B] (même durée). [Saisonnalité : comparé aussi à N-1 / non pertinent.]

| Page ou famille | Impressions A → B | Clics A → B | Position A → B | Depuis quand | Objectif business lié | Conversions observées |
|---|---:|---:|---:|---|---|---|

[Une phrase par mouvement significatif : de quelles requêtes il vient, quel segment le porte.]

[Sans données de conversion :] L'importance commerciale est estimée à partir de l'offre et des objectifs du client ; la contribution aux conversions n'est pas mesurée.
```

### Données structurées : le protocole (onglet 6)

Trois contrôles, sur les pages business prioritaires et un exemplaire de chaque gabarit :

1. **Validité technique** : JSON-LD ou microdata lisible sans erreur, propriétés obligatoires du type présentes (test des résultats enrichis de Google ou validateur Schema.org, résultat daté).
2. **Correspondance avec le contenu visible** : chaque valeur balisée existe telle quelle sur la page. Un balisage qui dit ce que la page ne montre pas est un défaut, pas une opportunité.
3. **Exigences de la fonctionnalité Google visée** : quel résultat enrichi est cherché, existe-t-il encore pour ce type de site. Un balisage valide ne garantit pas l'affichage.

La question n'est pas « quel pourcentage de pages est balisé » mais **« un balisage pertinent est-il absent ou incorrect sur des pages où il peut réellement servir ? »**. Google a retiré les résultats enrichis FAQ le 7 mai 2026 (source citée par Google for Developers) : une FAQ visible reste utile au lecteur, son balisage `FAQPage` ne se présente plus comme une opportunité d'affichage ; `seo-faq-query`, qui en produit encore, est à relire sur ce point.

### Analyses conditionnelles : des déclencheurs, pas une check-list pour tous

Elles se lancent quand une phase 0 à 5 fait apparaître le déclencheur, et le Résumé dit lesquelles ont été ouvertes et pourquoi, ou pourquoi aucune.

| Déclencheur observé | Analyse à ouvrir |
|---|---|
| Catalogue avec filtres, tris ou variantes produisant des URL distinctes | Facettes et variantes : URL indexables vs canoniques, paramètres, pages de filtre en concurrence |
| Plusieurs langues ou pays servis, `hreflang` présent | Versions linguistiques : cohérence `hreflang`, canonicals croisés, page servie par pays |
| Établissement physique, zone de chalandise, requêtes locales dans la GSC | Présence locale : fiche Google Business Profile, cohérence NAP, pages locales |
| Plusieurs milliers d'URL avec symptômes d'exploration (découvertes non indexées en masse, crawl irrégulier) | Logs serveur : ce que Googlebot explore, à quelle fréquence, ce qu'il ignore |
| Fondamentaux corrects et sites classés sur les requêtes prioritaires visiblement mieux dotés en liens | Autorité externe ciblée : les liens font partie des systèmes de classement, un audit limité au site ne mesure pas ce contexte |

Sans données de liens, le Résumé porte « Autorité externe non évaluée. » Jamais, à sa place, une recommandation de contenu faute d'autre explication.

## Discipline avant publication

Appliquer la discipline de précision à chaque onglet ; vérifier que chaque phase a sa forme de sortie visible ; exécuter `node .claude/skills/redaction-anti-ia/slop.mjs <fichier>` sur le HTML ; publier en artifact ; redonner le lien. Rien n'est envoyé au client depuis la session d'audit.

## Journal des règles du 28/09/2026

Toutes intégrées ci-dessus ; cette liste sert à retrouver d'où elles viennent. Renommage `audit-complet` → `audit-complet-v2`. Onglet Contenu et pertinence (skill `seo-contenu-pertinence`) pour une dimension pesée 20 pts sans protocole. Bloc « Ce qui progresse ». Contrôle du rendu et données terrain. Gravités, quotas, seuils et pourcentages de fiabilité corrigés dans les skills dédiés ; barème déplacé dans le vault ; finding en trois temps ; dépendance et test de validation ; sortie visible par phase ; Gains rapides et Coexistences dans l'onglet 7 ; protocole données structurées ; analyses conditionnelles ; autorité externe. Infobulle sur chaque score. Score en gros dans l'anneau. Onglet Mots-clés business réécrit pour le client (vocabulaire, verdict sans note, requêtes absentes ≠ lisibles dans l'interface, apparitions sans clic ≠ gain rapide, recouvrement ≠ conflit, impressions ≠ marché) puis top 20 scoré. Onglet Indexation : « rien de confirmé » autorisé, hors sitemap = constat, champ `indexed` obsolète, deux versions de rendu, `referringUrls`, robots évalué, vérifications terminées, titre en diagnostic, cas dissociés, test selon la langue du navigateur. Ordre de lecture par l'impact. Retouche visuelle de la coque.

## Où ce skill dépasse le fichier workflow (état au 28/09/2026)

Portés dans le workflow : la grille du Score SEO global (Phase 7A) et la Phase 4 sans seuil de taille, en trois états. Restent définis ici, en attente d'une décision de l'utilisateur pour les porter : l'onglet Contenu et pertinence (la Phase 3 du vault reste « architecture Hn »), le bloc « Ce qui progresse », le contrôle du rendu, les données terrain et « mobile par défaut, desktop si justifié » (la Phase 1bis du vault dit encore « TBT suffisant pour 80 % des cas »), les objectifs business confirmés et les conversions dans la checklist pré-audit, le protocole données structurées, les analyses conditionnelles et l'autorité externe.

## Vérification finale (obligatoire)

Avant de présenter le livrable comme terminé : lancer `verificateur-livrable` avec les 6 sections de le skill `verification-livrable` (demande de tous les skills utilisés, livrables, sources, contraintes). Corriger les ❌, relancer le vérificateur sur la nouvelle version, recopier le dernier tableau dans la réponse. Un hook refuse la fin de la réponse tant que ce n'est pas fait.
