---
name: reporting-client
description: "Reporting client en 4 blocs : GSC avant/après, stratégie GEO, citations IA, URL publiées. « reporting client », « report mensuel »."
---

# Reporting client

## Quand utiliser ce skill

Reporting client d'une prestation SEO/GEO, en quatre blocs enchaînés : (1) Search Console avant /
après 3 mois sur le site et sur les pages, (2) stratégie GEO relancée sur la base du constat,
(3) citations IA mesurées par geo-citations, (4) liste des URL publiées avec leur statut réel.
Chaque chiffre vient de Search Console, d'un relevé daté ou du journal de prestation, jamais
d'une estimation. Sortie : un rapport markdown et un PDF client (gabarit template/rapport_pdf.py).
TOUJOURS utiliser ce skill, en entier (les quatre blocs), quand l'utilisateur dit :
"résumé client", "reporting client", "report client", "report mensuel", "/reporting-client",
"résumé de [client]", "reporting de [client]", "report de [client]", "bilan de la prestation".

## Règle fondamentale

Chaque étape du skill est exécutée telle qu'écrite. Aucun résumé, aucun raccourci, aucune étape sautée ni condensée : les quatre blocs, tous leurs points, toutes les commandes, tous les contrôles, y compris le bloc 2 et le bloc 3 en entier. Un point qu'on ne peut pas exécuter (donnée absente, outil indisponible) se dit explicitement avec la raison ; il ne se remplace pas par une version abrégée. Cette règle porte sur l'exécution, pas sur la longueur du texte : un trou reste `[MATIÈRE MANQUANTE]`, jamais une phrase de remplissage.

Un reporting répond à une question : qu'a produit la prestation, mesuré, et qu'est-ce qu'on fait ensuite.
Il ne démontre pas que la prestation marche. Quand les données ne tranchent pas, il l'écrit.

Ce skill orchestre. Il ne remplace ni `strategie-geo` ni `geo-citations` : il les lance dans l'ordre et consolide.

## Avant de commencer

1. Identifier le client : slug, domaine, propriété Search Console (`https://domaine/` ou `sc-domain:domaine`).
2. Lire le journal de prestation du client dans le coffre : date de démarrage, étapes, accès GSC. Si le client a son propre coffre, lire son `AGENTS.md` et ouvrir son tableau de bord (skill `tableau-de-bord-projet`).
3. Fixer la **date pivot** : démarrage de la prestation, ou date de la première mise en ligne mesurable. Sans date écrite dans le journal, la demander à l'utilisateur. Ne pas la deviner.
4. Les mots « résumé client », « reporting client », « report client » et « report mensuel » lancent les quatre blocs à la suite, dans une seule exécution. Seuls arrêts : le go sur le coût de `geo-citations` (bloc 3), les validations propres à `strategie-geo` (bloc 2) et une donnée qui manque et que seul l'utilisateur a (date pivot, accès GSC).

## Bloc 1 — Search Console, avant / après 3 mois

```
python3 <dossier du skill reporting-client>/scripts/gsc_avant_apres.py <propriété> <dossier> --pivot YYYY-MM-DD [--urls urls.json] [--creds identifiants.json]
```

Accès : identifiants OAuth utilisateur de l'API Search Console, en JSON (`client_id`, `client_secret`, `refresh_token`, `quota_project_id`). Le script les lit dans `--creds`, sinon dans la variable `GSC_CREDENTIALS`, sinon dans `~/.config/organikk-gsc/oauth-user-credentials.json`. Sans accès API : le dire, et faire la comparaison dans l'interface Search Console (Performances → Date → Comparer), en notant que le relevé est manuel et daté.

Sortie : `<dossier>/gsc-avant-apres.json`. Fenêtres de 91 jours : avant = les 91 jours qui précèdent le pivot, après = les 91 qui suivent. Sans `--pivot`, trimestre contre trimestre précédent. `--urls` prend `{url: date de publication}` et compare chaque page à sa propre date.

À sortir du JSON, avec les mêmes colonnes pour le site et pour les pages :

- **Site** : clics, impressions, CTR, position moyenne (pondérée par les impressions), avant, après, écart absolu et en %.
- **Pages** : les 10 qui gagnent le plus de clics, les 10 qui en perdent le plus, les pages apparues (0 impression avant) et disparues. Une page qui a changé d'URL ou de rôle se signale, pas se compare.
- **Requêtes** : séparer marque et hors marque. Sans cette séparation, la hausse de marque masque l'érosion hors marque.
  Hors marque = total du site moins les requêtes de marque. Les requêtes que Google n'affiche pas (anonymisées) sont comptées dans le hors marque, jamais sur une ligne séparée. Contrôle : marque + hors marque = total du site sur chaque période.
- **Pages publiées pendant la prestation** : avant / après à leur propre date, si `--urls`.

Garde-fous :

- `apres_incomplet: true` → la fenêtre n'est pas écoulée. Écrire « fenêtre de N jours sur 91 » à côté de chaque chiffre concerné, et ne conclure ni à un gain ni à une perte.
- Une URL publiée il y a moins de 91 jours n'a pas de « après 3 mois ». Elle apparaît dans la liste du bloc 4, pas dans la conclusion du bloc 1.
- Le CTR qui baisse avec des impressions qui montent est un signal fréquent d'élargissement de la requête, pas une dégradation. Le dire seulement si les requêtes le montrent.
- Saisonnalité : si le client est saisonnier, ajouter le même trimestre N-1 (le relevé 16 mois le permet). Sinon écrire « saisonnalité non contrôlée ».
- Corrélation n'est pas causalité. Une hausse après la mise en ligne d'une page est une observation, la cause reste une hypothèse tant qu'un autre facteur (mise à jour d'algo, saisonnalité, campagne) n'est pas écarté. Citer ce qui a été vérifié.
- Santé de la collecte avant d'interpréter une absence de données : dernière date disponible, propriété correcte.

## Bloc 2 — Stratégie GEO

Lancer `strategie-geo` en mode révision de la stratégie existante (« Améliorer une stratégie GEO existante », cas listé dans son déclenchement). Nommer le skill et son `SKILL.md` au lancement, et distinguer dans le compte rendu méthode lue, workflow local exécuté, outil externe appelé.

Entrée à lui donner : la stratégie précédente du client et le constat du bloc 1. Sortie : ce qui change dans les priorités, avec le constat qui le justifie. Pas de stratégie refaite de zéro si rien dans le bloc 1 ne l'impose.

`strategie-geo` a ses propres validations de phase : elles s'appliquent. Si aucune stratégie n'existe pour ce client, le dire et proposer de la construire à part, pas de la fabriquer dans un reporting.

## Bloc 3 — Citations GEO

Lancer `geo-citations`. Règles reprises de son SKILL.md, sans exception :

- Annoncer `mots-clés × moteurs × runs = N appels` et attendre le go de l'utilisateur avant de lancer le relevé. Chaque run est payant.
- Minimum 30 runs par mot-clé et par moteur. En dessous : « ceci n'est pas un échantillon crédible ».
- Questions fournies par l'utilisateur ou issues de la GSC réelle. Jamais inventées.
- Présence, mention et fréquence dans le temps restent trois indicateurs séparés, sans score composite.

L'évolution n'est donnée que si le relevé précédent est comparable (mêmes moteurs, mêmes questions). Sinon : « non comparable » et la raison. Premier relevé du client : c'est une base, pas un avant / après.

Reprendre du rapport : taux par moteur, domaines cités à la place du client.

Si l'outil de relevé n'est pas installé : le dire, écrire le bloc en `[MATIÈRE MANQUANTE]` avec ce qu'il faut pour le produire. Pas de citation estimée à la main.

## Bloc 4 — URL publiées

Tableau : URL, titre ou intention, date de mise en ligne, statut HTTP relevé aujourd'hui, présence dans le sitemap, impressions GSC sur la période.

- **Source de la liste** : journal de prestation, livrables du coffre client, relevés datés, sitemap du site. Une page écrite n'est pas une page publiée.
- **Date de mise en ligne** : celle d'une source (journal, CMS, relevé daté, Wayback). Sinon `[DATE MANQUANTE]`.
- **Statut** : `curl -sIL -o /dev/null -w "%{http_code}"` sur chaque URL, date du relevé indiquée. 200 / redirection / 404 se disent tels quels. Des adresses notées comme publiées dans un journal reviennent parfois en 404 : la liste du journal ne suffit pas.
- **Écrites non publiées** : section séparée, avec le blocage connu (relecture, prix à confirmer, CMS). Ne pas les mêler aux publiées.
- Impressions à 0 sur une URL en 200 : « pas encore affichée dans Search Console », sans en déduire un problème d'indexation. Pour l'indexation, passer par `indexation-check`.

## Sortie

Fichier : `wiki/reporting-client/YYYY-MM-DD-<client>.md` dans le coffre, frontmatter standard (`type: audit`, tags `reporting`, `<client>`), wikilinks vers la stratégie GEO, le journal de prestation et les relevés. Données brutes à côté : `raw/data/reporting-<client>/` (JSON GSC, relevé geo-citations). Pour un client avec son propre coffre, copier aussi le reporting dans ce coffre et mettre à jour son tableau de bord.

PDF client : gabarit `template/rapport_pdf.py`. Il donne la couverture outremer grainée avec ta marque et ton logo (`MARQUE`, `LOGO_SVG`, à remplacer en tête du fichier ; `cover`), l'encadré « Résumé » en page 2 (`resume`), les tableaux à écarts ▲ vert / ▼ rouge (`table`, `delta`, `LEG` ; position : plus bas = vert) et le rendu par Chrome headless (`rendre`). Usage :

```python
import sys; sys.path.insert(0, '<dossier du skill reporting-client>/template')
from rapport_pdf import *
corps = resume(pages, positions, source_positions, clics_avant, clics_apres, periodes)
corps += '<h2 class="brk">Search Console, avant / après 3 mois</h2>' + table([...], [...]) + LEG  # puis blocs 2, 3, 4, limites
rendre(document(client, domaine, titre_periodes, donnees_arretees, sources, date, corps), 'reporting.html', 'reporting.pdf')
```

Contrôler ensuite la couverture : aucune bande blanche, pas de page vide en 2.

Le Résumé sert d'appui pendant le call de reporting. Il contient exactement : nombre de pages créées (en ligne / pas en ligne, relevé HTTP daté), positions des mots-clés business (tableau, avec la source et la date des positions), écart de clics Search Console entre les deux périodes comparées. Chiffres seulement, identiques à ceux des sections.

Structure, dans cet ordre : couverture, résumé, bloc 1, bloc 2, bloc 3, bloc 4, limites. Un bloc sans matière s'écrit `[MATIÈRE MANQUANTE]` avec ce qu'il faut aller chercher. Pas de conclusion qui répète la synthèse.

Tracer ensuite dans le journal de prestation du client et dans `wiki/log.md` (`## [YYYY-MM-DD] reporting | <client>`).

## Rédaction

Ce qui part chez le client passe par `ton-de-voix` avant écriture, puis `redaction-anti-ia` et `node .claude/skills/redaction-anti-ia/slop.mjs <fichier>` après. Les tableaux de chiffres restent des tableaux, la lecture autour est en prose courte.

Aucun envoi au client sans l'accord de l'utilisateur.

## Vérification finale (obligatoire)

Avant de présenter le reporting comme terminé : lancer `verification-livrable`. Corriger les ❌, relancer sur la nouvelle version, recopier le dernier tableau.
