---
name: indexation-check
description: "Audit d'indexation d'un site en 9 contrôles par URL, sans outil payant. « audit indexation », « mes pages sont-elles indexées »."
---

# Skill — Audit d'indexation Claude

## Quand utiliser ce skill

Audit d'indexation d'un site (B2B / éditorial / pSEO) sans outil tiers payant. Vérifie 9 points sur chaque URL : statut HTTP, blocages techniques, directives noindex, sitemap (présence + lastmod + cohérence), maillage interne entrant, longueur de contenu, statut d'indexation Google estimé. Sortie : rapport markdown avec synthèse, anomalies critiques en tête, anomalies mineures, recommandations priorisées. Distingue strictement "non indexée" et "non testable" (rate-limit Google). Aucune action de forçage, lecture seule sur le web public. Sortie obligatoire en plus du tableau : un rapport de pré-décision (diagnostic, preuves typées, état Critique / À améliorer / Sain, actions P1-P3 avec confiance, effort et risque, jamais de score affiché) ; sans lui le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "audit indexation", "check indexation", "monitoring indexation", "vérifier l'indexation", "mes pages sont-elles indexées", "agent indexation", "routine indexation mensuelle", ou quand il fournit une liste d'URLs / un sitemap / un fichier `urls.txt` / `articles.ts` / `wiki.ts` en demandant un diagnostic d'indexation.

Ce skill est conçu pour tourner en one-shot (audit ponctuel) ou en récurrent mensuel via `/schedule`. Cible : sites de 30 à 1 000 pages. Au-delà, brancher l'API Google Search Console officielle (voir section "Variante haute fiabilité").

## Quand déclencher

- Audit ponctuel d'un site (avant call commercial, après une refonte, après un déploiement de cluster)
- Monitoring mensuel récurrent sur un client en accompagnement
- Diagnostic d'une chute de trafic non expliquée
- Pré-flight d'un projet pSEO (vérifier que la base technique est saine avant de scaler)

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Liste des URLs à monitorer (fichier dans le repo : `urls.txt`, `src/data/wiki.ts`, `src/data/articles.ts`) OU URL du sitemap.xml public du site | Oui |
| Domaine cible (ex : `site-client.fr`) | Oui |
| Périmètre du maillage à crawler (pages hubs : `/`, `/glossaire`, `/wiki`, footer, articles) | Recommandé |
| Service account GSC API (upgrade fiabilité) | Optionnel |

Minimum viable : une liste d'URLs et le domaine. Le reste se déduit.

## Architecture (3 couches)

```
1. Charger la liste des URLs (source de vérité humaine)
        ↓
2. COUCHE A — Audit technique (causes potentielles)
        ↓
3. COUCHE B — Statut d'indexation observable
        ↓
4. COUCHE C — Reporting markdown
```

La séparation causes / statut est volontaire. Le check v1 ne regardait que le statut, donc disait "OK 200" même quand la page portait un `noindex` accidentel. Le check v2 sépare strictement les deux.

## Pipeline (9 checks)

### COUCHE A — Audit technique (causes)

**1. HTTP check (404/500, redirects)**
Pour chaque URL :
```bash
curl -sIL -A "Mozilla/5.0" -o /dev/null -w "%{http_code}|%{url_effective}" {URL}
```
Note le code final ET la chaîne de redirects. 200 attendu. Toute redirection 301→200 systématique = dette à signaler (trailing slash, http→https).

**2. robots.txt non bloquant**
```bash
curl -s https://{domaine}/robots.txt
```
Pour chaque path, vérifie qu'aucune directive `Disallow:` ne le bloque pour `User-agent: *` ni `User-agent: Googlebot`.

**3. Pas de balise noindex (HTML + en-tête HTTP)**
```bash
curl -sL -A "Mozilla/5.0" {URL} | grep -i 'name="robots"'
curl -sIL {URL} | grep -i 'x-robots-tag'
```
Signaler toute présence de `noindex` ou `none`.

**4. Sitemap : présence + fraîcheur**
```bash
curl -s https://{domaine}/sitemap.xml
```
Pour chaque slug attendu, vérifie présence d'une `<loc>` et lis le `<lastmod>` associé. Flagger tout `lastmod` > 6 mois.

**5. Cohérence sitemap ↔ source de vérité**
Diff entre les slugs de la SOT (fichier humain) et les `<loc>` du sitemap :
- Slugs en source mais absents du sitemap → à ajouter au build
- `<loc>` en sitemap mais absente de la source → orpheline sitemap

**6. Maillage interne entrant**
Crawl les pages hubs (`/`, `/glossaire`, `/wiki`, footer, sample d'articles) et compte les liens internes entrants par URL cible.
- 0 lien entrant = orpheline (critique)
- 1 seul lien entrant = sous-maillée (à signaler)

**7. Longueur de contenu (proxy thin content)**
Pour chaque URL, extrais le texte du `<main>` ou `<article>` (à défaut du `<body>` moins `<nav>` et `<footer>`) et compte les mots.
- < 300 mots = thin (à creuser)
- 300-800 = court mais acceptable pour fiche atomique
- > 800 = OK

### COUCHE B — Statut d'indexation (sortie)

**8. Indexation Google estimée (scraping `site:`)**
```bash
curl -sL -A "Mozilla/5.0 (Macintosh...)" "https://www.google.com/search?q=site:{URL}&hl=fr"
```
**Garde-fous obligatoires :**
- Espacer les requêtes de 3 à 5 secondes (`sleep 4`)
- Détecter le blocage : `grep -E 'sorry/index|recaptcha|unusual traffic'`
- Si bloqué : marquer "non testable — rate limit", **pas** "non indexée"
- Retry une fois si réponse vide avant de conclure
- Marquer "indexée" si l'URL apparaît dans le HTML de réponse

Ce que vaut ce signal  : `site:` est un **indice non exhaustif**. Google indique qu'une URL indexée peut ne pas apparaître dans ces résultats. Une absence ne prouve donc pas une non-indexation ; une présence prouve une indexation à la date du test. Le rapport écrit la source (`site:`), la date et la portée (« N URL testées, M bloquées par le rate-limit »), jamais un pourcentage de fiabilité.

### COUCHE C — Reporting

**9. Rapport markdown**
Structure obligatoire :
- Synthèse en tête (X/N par dimension, `✅` pour validé, `⚠️` pour anomalie)
- Anomalies CRITIQUES (action immédiate) — `noindex` accidentel, page orpheline, 404 sur page business
- Anomalies mineures — `lastmod` > 6 mois, sous-maillage, thin content
- Recommandations priorisées (2-5 actions, classées par impact estimé)
- Section "Limites du rapport" (ce qui n'a pas pu être testé et pourquoi)

## Sortie de pré-décision (obligatoire)

Ce skill n'a pas terminé tant que le rapport de pré-décision n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau, et il suit `audit-complet-v2/rapport-audit-seo-format.md` (`audit-complet-v2/rapport-audit-seo-format.md`). Fichier : `wiki/audit/YYYY-MM-DD-slug-indexation-decision.md`.

Ce qu'il contient, dans cet ordre :

1. Diagnostic principal : une phrase, la cause structurante, pas une liste d'erreurs
2. Les chiffres à retenir : 3 à 5, ceux qui illustrent le diagnostic
3. État : Critique, À améliorer ou Sain, calculé sur l'impact SEO réel et le type de page, jamais sur le nombre d'erreurs ; jamais de score sur 10
4. Problèmes (3 maximum) et opportunités (5 maximum), séparés : chacun avec Preuve (2 à 4 données), Pourquoi c'est important, Action, Confiance (forte / moyenne / faible) ; chaque problème s'écrit en trois temps : observation prouvée → conséquence ou risque justifié → bénéfice attendu de la correction (l'observation seule n'est pas un frein SEO démontré)
5. Actions P1 / P2 / P3, 3 P1 maximum : pourquoi, preuve, signal attendu (jamais un résultat chiffré promis), dépendance préalable, test de validation (ce qui distingue « correction appliquée » de « résultat SEO observé »), effort faible / moyen / élevé (jamais en heures), confiance, risque low / medium / high ; toute action high (suppression, 301, fusion, changement d'URL) porte « À valider avant déploiement » et sa checklist
6. Ce que les données ne permettent pas de conclure, et « données insuffisantes » ou « ne rien faire » quand c'est le cas

Sur le périmètre de ce skill, le rapport tranche l'indexation : URLs vues par Google mais en 404 ou redirigées (règle 404 URL par URL : 301 seulement si une page équivalente existe, 410 ou 404 conservée, restaurer, ou à vérifier ; jamais un 301 de dossier à dossier), sitemap, canonicals ; « non indexée » et « non testable » séparés.

Règles : chaque information est typée FACT, HYPOTHESIS ou ACTION, jamais une hypothèse écrite comme un fait ; un problème existe une seule fois (ID), les observations qui parlent du même problème fusionnent ; une anomalie n'est pas une priorité par défaut ; les pages business et les tendances GSC passent avant les anomalies techniques secondaires ; jamais de recommandation automatique de fusion, 301, suppression, réécriture ou création de page ; Google n'est jamais anthropomorphisé. Phrases courtes, une donnée par diagnostic, aucune des phrases « Il est important de », « Il convient de », « Cela peut potentiellement », « Il est intéressant de noter », « Dans le cadre de ».

Restitution (corrections V2 du 23 septembre) : aucun ID technique ni mot anglais (low / medium / high) dans le rapport ; Faible / Moyen / Élevé partout ; la certitude affichée ne dépasse jamais la couverture des données (« aucun problème majeur détecté sur les URL inspectées », pas « Sain ») ; formulations précises (« URL en 404 avec encore des impressions ») ; aucune action proposée sur une page dont les requêtes ne sont pas connues (« à vérifier ») ; le nombre de mots seul n'est jamais un problème ; limites de longueur : diagnostic 70 mots, 4 chiffres, 3 problèmes de 40 mots, 6 actions, 3 opportunités de 35 mots, le reste dans les détails repliés.

Onglet Analyse technique, structure validée le 23 septembre 2026 (référence : [[audit/2026-09-22-organikk-co]]) : chaque priorité = une phrase de cadrage, « Ce qu'on observe » (faits chiffrés en liste, pages en code), « Pourquoi c'est prioritaire » (deux phrases), « Action » (liste numérotée courte), « Impact attendu » et « Risque » en gras ; puis le plan des 30 jours en trois paliers (Priorité immédiate, Deuxième étape, Priorité secondaire), une action par paragraphe en gras suivie d'une phrase ; puis « à surveiller avant d'agir » pour la page dont la cause n'est pas isolée ; puis « Autres pages à surveiller » : chiffres séparés par « · », une phrase, verdict en gras (« Aucune action recommandée », « À vérifier avant toute modification »).

## Sortie obligatoire

Gabarit de l'onglet Indexation. Chaque placeholder `[...]` vient d'une mesure réelle ou n'apparaît pas.

```markdown
# Indexation

[Nombre] pages testées sur [nombre total].

**Sources utilisées :** crawl, sitemap, robots.txt, Search Console, inspection d'URL Google, tests HTTP directs.

**Pages sans défaut d'indexation confirmé :** [XX %]

> Ce pourcentage ne doit compter que les défauts réellement démontrés. Une anomalie potentielle ou extrapolée ne doit pas faire baisser ce chiffre.

---

## Chiffres à retenir

| Mesure | Résultat |
|---|---:|
| **Pages testées** | [XX] |
| **Pages répondant en 200** | [XX / XX] |
| **Pages en noindex** | [XX] |
| **Pages bloquées par robots.txt** | [XX] |
| **Redirections non souhaitées** | [XX] |
| **URL importantes absentes du sitemap** | [XX] |
| **URL du sitemap redirigées** | [XX] |
| **Soft 404 / fallback détectés** | [XX] |
| **URL inspectées individuellement dans Google** | [XX] |

---

# Ce qui bloque réellement

## 1. [Nom précis du problème]

### État constaté

[Décrire uniquement ce qui est objectivement mesuré.]

Exemple :

> 49 URL déclarées au sitemap sans slash final redirigent vers leur version canonique avec slash.

### Preuve

- [crawl]
- [curl / requête HTTP]
- [sitemap]
- [Search Console]
- [inspection Google]

### Impact

[Expliquer la conséquence réellement défendable.]

Exemple :

> Le sitemap ne pointe pas directement vers les URL finales. Google et les autres crawlers doivent donc suivre une redirection avant d'atteindre la version canonique.

Ne pas ajouter de conséquence non démontrée sur le ranking ou le crawl budget.

### Action

[Action précise.]

Exemple :

> Générer le sitemap avec les URL finales réellement servies et canonicalisées.

**Priorité :** [Haute / Moyenne / Faible]
**Effort :** [Faible / Moyen / Fort]
**Confiance :** [Forte / Moyenne / Faible]

---

## 2. [Deuxième problème]

### État constaté

[...]

### Preuve

[...]

### Impact

[...]

### Action

[...]

**Priorité :** [...]
**Effort :** [...]
**Confiance :** [...]

---

## 3. [Troisième problème]

Même structure.

---

# Ce qui va bien

| Contrôle | Résultat | Lecture |
|---|---:|---|
| **HTTP** | [XX / XX] pages répondent en 200 | [sain / réserve] |
| **noindex** | [XX] | [lecture] |
| **robots.txt** | [XX] | [lecture] |
| **canonical** | [XX] | [lecture] |
| **pages business inspectées** | [XX] | [lecture] |

Ce bloc doit éviter de présenter l'audit uniquement sous l'angle des problèmes.

---

# Inspection Google

## URL inspectées individuellement

| URL | Verdict Google | Dernier crawl | Source |
|---|---|---|---|
| `[URL]` | [Indexée / Inconnue / Page avec redirection / Explorée non indexée / etc.] | [date] | Inspection Google |
| `[URL]` | [...] | [...] | [...] |

Ne jamais extrapoler automatiquement le statut d'un cluster entier à partir de quelques URL.

---

## Ce que l'échantillon permet de dire

Exemple :

> 4 pages sur 22 du cluster ont été inspectées individuellement. Les 4 renvoient « URL inconnue de Google ».

Ce qui peut être dit :

> **Le problème est confirmé sur les 4 URL testées.**

Ce qui ne peut pas être dit :

> **Les 22 pages n'ont jamais été vues par Google.**

Pour les autres URL :

> Le même comportement est possible compte tenu de leur architecture commune, mais il n'est pas mesuré individuellement.

---

# Sitemap

## Cohérence du sitemap

Vérifier :

- URL finale ou URL redirigée ;
- statut HTTP ;
- canonical ;
- présence des pages réellement destinées à l'indexation ;
- absence des URL techniques ou non canoniques ;
- date de dernière lecture du sitemap dans Search Console.

| Contrôle | Résultat |
|---|---|
| URL finales déclarées | [XX / XX] |
| URL du sitemap qui redirigent | [XX] |
| pages stratégiques absentes | [XX] |
| URL non destinées à l'indexation présentes | [XX] |
| dernière lecture Search Console | [date] |

---

# Soft 404 et fallback

## Test d'URL inexistantes

Tester au minimum :

- une route racine inventée ;
- une route dans une section existante ;
- une route proche d'une vraie page.

Exemple :

`/page-qui-nexiste-pas-12345`
`/blog/inexistant-999`
`/xyzabc`

Pour chacune, relever :

- statut HTTP ;
- title ;
- canonical ;
- taille HTML ;
- contenu principal ;
- similitude avec la home.

### Conclusion possible

> Les URL inexistantes retournent HTTP 200 et servent le contenu de la page d'accueil.

### Action

> Retourner un vrai 404 pour les routes inconnues avec une page d'erreur dédiée.

Ne pas utiliser automatiquement 410 : réserver le 410 aux ressources connues volontairement supprimées.

---

# Redirections

## Redirections observées

| Type | Nombre | Exemple | Action |
|---|---:|---|---|
| HTTP → HTTPS | [XX] | [...] | [rien / corriger] |
| www → non-www | [XX] | [...] | [...] |
| slash → sans slash | [XX] | [...] | [...] |
| sans slash → slash | [XX] | [...] | [...] |
| ancienne URL → nouvelle | [XX] | [...] | [...] |

Toutes les redirections ne sont pas des problèmes.

Une redirection devient un finding si elle :

- apparaît systématiquement dans le sitemap ;
- crée une chaîne ;
- envoie vers une mauvaise destination ;
- concerne une URL destinée à être canonique ;
- empêche d'accéder au contenu attendu.

---

# Canonicalisation

Vérifier :

- canonical présent ;
- canonical auto-référent lorsque pertinent ;
- canonical vers une URL en 200 ;
- absence de contradiction sitemap / canonical / redirection ;
- absence de canonical vers une page sans rapport.

| Contrôle | Résultat |
|---|---:|
| canonical manquant | [XX] |
| canonical vers autre URL | [XX] |
| canonical vers URL redirigée | [XX] |
| contradiction sitemap / canonical | [XX] |

---

# Pages hors sitemap

Une URL hors sitemap n'est pas automatiquement un défaut.

Pour chaque page :

| URL | Doit être indexée ? | Business ? | Dans sitemap ? | Action |
|---|---|---|---|---|
| `[URL]` | Oui | Oui | Non | Ajouter |
| `[URL]` | Non | Non | Non | Rien |
| `[URL]` | À confirmer | Moyen | Non | Vérifier |

Question centrale :

> **Cette URL fait-elle partie des pages que l'on veut réellement faire découvrir et indexer ?**

---

# Pages à examiner en priorité

| URL | Rôle | État Google | Problème | Priorité |
|---|---|---|---|---|
| `[URL]` | Business | [état] | [problème] | Haute |
| `[URL]` | Cluster | [état] | [problème] | Moyenne |
| `[URL]` | Secondaire | [état] | [problème] | Faible |

La priorité dépend de :

**importance business × gravité technique × niveau de preuve**

Pas uniquement du nombre de pages touchées.

---

# Ce qui a été détecté mais n'est pas retenu

## [Signal]

**Mesure :** [...]

**Pourquoi ce n'est pas retenu :**

[...]

Exemples :

### `lastmod` ancien

> Un `lastmod` de plus de six mois n'est pas un défaut si le contenu n'a pas été modifié.

### Page sous 300 mots

> La longueur du contenu ne détermine pas son indexabilité.

### Absence de Schema.org

> L'absence de données structurées n'empêche pas l'indexation et doit être auditée séparément.

---

# Ce que les données ne permettent pas de conclure

- le statut d'indexation des URL non inspectées individuellement ;
- la cause exacte d'une URL « explorée mais non indexée » sans données complémentaires ;
- qu'un manque de liens internes explique à lui seul une absence d'indexation ;
- qu'un sitemap ancien signifie que Google n'a pas découvert les URL par d'autres moyens ;
- qu'une page hors sitemap est problématique sans connaître son rôle ;
- qu'une URL inconnue de Google l'est uniquement à cause du maillage.

---

# Priorités

## Priorité 1 — [Action]

**État constaté :**
[...]

**Pourquoi maintenant :**
[...]

**Action précise :**
[...]

**Résultat attendu :**
[Résultat technique recherché.]

**Effort :** [...]
**Confiance :** [...]

---

## Priorité 2 — [Action]

[...]

---

## Priorité 3 — [Action]

[...]
```

## Contrôle de cohérence avant publication

JEV doit bloquer la restitution si :

- le nombre de pages annoncé ne correspond pas aux pages réellement inspectées ;
- une extrapolation est présentée comme une mesure ;
- une URL « inconnue de Google » est automatiquement attribuée au maillage ;
- un statut 200 est interprété comme preuve d'indexation ;
- une URL hors sitemap est automatiquement classée comme défaut ;
- un vieux `lastmod` est automatiquement classé comme problème ;
- absence de données structurées ou faible nombre de mots influencent le score d'indexation ;
- une redirection normale est traitée comme anomalie sans expliquer pourquoi ;
- sitemap, canonical et URL finale sont analysés séparément alors qu'ils se contredisent.

## Règles à interdire

Ne jamais conclure automatiquement :

- `HTTP 200 = indexée` ;
- `hors sitemap = problème` ;
- `1 lien entrant = Google ne découvre pas la page` ;
- `URL inconnue = manque de maillage` ;
- `lastmod ancien = sitemap mauvais` ;
- `moins de 300 mots = problème d'indexation` ;
- `pas de Schema = problème d'indexation` ;
- `quelques URL testées = cluster entier dans le même état` ;
- `HTML initial identique ou vide = pré-rendu cassé` (c'est une suspicion, le protocole de rendu tranche) ;
- `inspection d'URL correcte = pas d'action manuelle ni de problème de sécurité` (l'inspection ne les couvre pas).

La logique doit toujours être :

**URL destinée à Search → accessibilité → statut HTTP → robots → canonical → sitemap → état Google → preuve → action**

## Garde-fous (NON-NÉGOCIABLES)

- **Lecture seule** sur le web public. Aucune requête authentifiée non explicitement autorisée.
- **Aucune action de forçage d'indexation.** Pas de soumission GSC, pas de force-crawl.
- **Pas de modification du site.** Pas de PR sur les fichiers source. Sortie limitée à `reports/` ou directement dans la conversation.
- **Distinction stricte** "non indexée" vs "non testable" dans le rapport.
- **Priorité au signalement** : un `noindex` accidentel sur une page business doit remonter en TOP du rapport, pas en ligne 47 du tableau.
- Si un check échoue, continuer les autres et signaler dans la section "Limites".

> Discipline : observation côté agent, décision côté humain. Un agent qui peut "réparer" peut aussi tout casser un dimanche à 3 h du matin.

## Variante haute fiabilité — GSC URL Inspection API

Si l'utilisateur dispose d'un service account Google Cloud + propriété GSC :
1. Lire la clé JSON via secret stocké côté projet
2. Signer un JWT, échanger contre access token
3. POST sur `https://searchconsole.googleapis.com/v1/urlInspection/index:inspect`
4. Statuts officiels disponibles : `INDEXED`, `DISCOVERED_NOT_INDEXED`, `CRAWLED_NOT_INDEXED`, `URL_IS_UNKNOWN_TO_GOOGLE`

Ce que l'API donne, et ce qu'elle ne donne pas : l'état de la **version connue dans l'index** de Google, avec la date du dernier crawl, pas un test en direct de la version actuellement servie. Une URL modifiée hier peut afficher l'état d'avant-hier. Le rapport écrit donc la date de crawl relevée à côté de chaque verdict, et ne présente jamais ce résultat comme une vérification en temps réel. Setup ~30 minutes. Lève le rate-limit de `site:` (limite officielle 2 000 inspections / jour / propriété).

## La preuve, la conclusion et la priorité doivent correspondre 

- **« Ce qui bloque réellement » a le droit de répondre « rien de confirmé ».** La rubrique ne transforme pas un écart de configuration en problème pour avoir quelque chose à afficher. Quand rien n'est démontré, l'onglet s'ouvre sur « Aucun défaut d'indexation confirmé sur les N pages inspectées », puis « Vérifications à terminer ». « Confiance forte » porte sur le décompte, jamais sur un impact non établi.
- **Hors sitemap = constat, pas blocage.** Le sitemap signale à Google les URL qu'on souhaite lui montrer ; ce n'est pas la liste des pages autorisées à apparaître, Google découvre aussi par les liens. Une URL absente du sitemap ne prouve pas que son indexation n'a pas été décidée : écrire « l'audit n'a pas encore confirmé le choix du propriétaire pour ces familles », jamais « la question n'a pas de réponse ». Formulation : « N URL ayant reçu des impressions ne figurent pas dans le sitemap actuel. Cet écart ne démontre pas de problème d'indexation. Vérifier quelles familles doivent y figurer, puis y ajouter leurs URL canoniques. Impact négatif non démontré, choix de configuration à confirmer. » Aucun point retiré pour ce seul écart.
- **Le rapport Performance décrit une activité sur une période**, pas l'inventaire des URL indexées aujourd'hui : « 125 URL ont enregistré des impressions entre le 30 juin et le 27 septembre », jamais « Search Console en sert 125 ». Des impressions passées ne confirment pas un statut au jour de l'audit, et comparer des impressions passées au sitemap actuel ne prouve pas une découverte « par d'autres chemins » si l'ancien sitemap n'est pas connu. Contrôler l'état HTTP actuel de ces URL avant toute lecture : sur organikk.co, 95 des 103 URL hors sitemap étaient déjà redirigées ou en 404.
- **Le champ `contents[].indexed` de l'API Sitemaps est obsolète** (Google demande de ne pas l'utiliser). Ne jamais le lire, ne jamais en tirer « compteur non fiable ». Si un chiffre vient de l'interface, donner le nom exact du rapport, son filtre et sa date ; le rapport Sitemaps montre des pages découvertes, l'indexation se lit dans le rapport d'indexation des pages filtré par sitemap. En attendant : « écart entre les données affichées et les inspections individuelles, origine à vérifier, non utilisé pour conclure ».
- **Le rendu compare deux versions**, HTML initial et DOM après rendu, sur le texte normalisé du contenu principal et sur l'ensemble des destinations des liens du corps, jamais sur un nombre de mots ou de liens (884 = 884 prouve une quantité, pas un texte). L'inspection d'URL ne fournit pas le HTML de la version connue de Google : le statut et la canonical sélectionnée se vérifient séparément par elle. N'écrire « trois versions » que si le HTML exploré a été récupéré dans l'interface. Conclusion : « sur les N pages testées, le contenu principal et les liens utiles sont présents dans le HTML initial, aucun écart observé après rendu », jamais « aucune dépendance au rendu » pour tout le site.
- **Les URL référentes de l'inspection ne mesurent pas le maillage.** Champ `referringUrls` vide = « aucune page référente renseignée », pas « aucune » ; une référente peut être indirecte. `sitemap` et `referringUrls` sont deux champs : deux colonnes, « sitemap signalé » et « pages référentes renseignées ». Le nombre de liens entrants se conclut dans l'onglet Maillage, depuis le crawl.
- **robots.txt : afficher l'évaluation, pas la présence d'un `Allow`.** Groupes présents, règles `Disallow`, règle la plus spécifique applicable à Googlebot, résultat par URL.
- **Terminer les vérifications ouvertes par ses propres mesures** avant d'élargir : inspecter les URL du sitemap non inspectées (au moins celles citées), contrôler les paires avec et sans slash (HTTP, redirections, canonicals déclarées et sélectionnées, période des impressions), inspecter les URL hors sitemap importantes une par une plutôt que traiter le lot comme homogène. Si le périmètre est volontairement limité, le titre l'assume : « diagnostic des N pages prioritaires avec contrôles complémentaires », pas « validation de l'indexation du site ».
- **Une redirection vers une page sans rapport est un finding** : 301 seulement vers la page qui remplace réellement le contenu, sinon 404 ou 410. Un lot d'anciennes URL redirigé vers une page d'offre se relève, se chiffre et se propose en correction « à valider avant déploiement ».
- **Le titre de l'onglet est le diagnostic**, pas un relevé : « Indexation : 3 pages d'offre ne sont pas indexées », puis la ligne des comptes (URL au sitemap · indexées · découvertes non indexées · inconnues · URL avec au moins une impression sur la période). « N URL ont généré au moins une impression sur 90 jours », jamais « servies par Google ». L'onglet répond à une seule question : Google peut-il découvrir, explorer, comprendre et indexer les URL qu'on veut rendre visibles ? Ce qu'obtiennent ces pages une fois indexées relève d'un autre onglet.
- **Dissocier les cas page par page** quand les données le permettent : un tableau page / rôle / signal principal / action prioritaire. 0 lien entrant → liens et sitemap ; 1 lien → découverte ; N liens et non indexée → le maillage n'est pas la cause, examiner contenu, doublon, canonical, rendu, valeur distinctive. Une recommandation générique là où une hypothèse est déjà éliminée est une faute.
- **Tester la réponse selon la langue du navigateur** sur tout site à plusieurs versions : la même URL demandée en `fr-FR` et en `en-US` doit répondre 200 avec le même canonical ; un 302 conditionnel vers l'autre version est un finding (Google déconseille la redirection automatique selon la langue, chaque version doit rester accessible et reliée par `hreflang`). C'est une cause à rattacher au finding de non-indexation quand les URL concernées coïncident, pas un second finding.
- **Restitution courte** : synthèse visible (verdict, findings établis, ce qui ne bloque pas, conclusion), preuves détaillées dans des blocs repliés, sans répéter un même chiffre dans trois tableaux. Les paragraphes « pourquoi le corriger » concluent le diagnostic, ils ne réexpliquent pas le SEO. « 5 inspections Google et contrôles du rendu ; 30 contrôles HTTP et directives » plutôt que « pages testées : 5 ». « Les 3 URL inexistantes testées renvoient une 404 ; ce test ne couvre pas toutes les pages » plutôt que « soft 404 : 0 ». Pas d'octets dans la synthèse client.

## Contrôle du rendu 

Remplace l'ancienne « variante SPA » réservée aux cas extrêmes. Le contrôle tourne sur **les pages importantes et les principaux gabarits** (un exemplaire par famille de pages), pas seulement quand un site a l'air d'une SPA.

Trois versions de la même page, comparées dans cet ordre :

1. **HTML initial** : ce que le serveur sert (`curl -sL -A "Mozilla/5.0" {URL}`).
2. **DOM après rendu** : Playwright ou Chrome headless, chargement complet, attente `networkidle`.
3. **Version observée par Google**, quand l'accès le permet : URL Inspection API (HTML rendu et capture d'écran du dernier crawl) ou l'outil d'inspection dans l'interface Search Console.

Sur chacune des trois, relever les mêmes cinq éléments : **contenu principal** (présent, absent, différent), **liens utiles** (les liens éditoriaux du corps, pas la nav), **title**, **directives robots** (meta et en-tête), **canonical**. Le résultat est un tableau 5 lignes × 3 colonnes par page contrôlée, avec les écarts marqués.

**Ce que le contrôle a le droit de conclure.** Un HTML initial sans contenu principal, ou identique entre plusieurs URL, ne démontre pas un rendu cassé : certaines applications génèrent le contenu principal en JavaScript, et Google utilise le HTML rendu pour l'indexation. La sortie autorisée est :

> Suspicion de dépendance au rendu ou de problème de pré-rendu : vérifier avant de conclure.

Jamais, automatiquement :

> Pré-rendu cassé.

Le finding ne devient un défaut confirmé que si la version 2 ou la version 3 manque effectivement le contenu principal, un lien utile, le title, une directive ou la canonical présents ailleurs, ou porte une valeur différente (canonical qui change entre initial et rendu, noindex injecté en JS, contenu de la home servi sous une autre URL après rendu).

Tant que ce contrôle n'a pas tourné sur une page, son contenu ne se note pas (`seo-contenu-pertinence`, `seo-structure-hn`) : on ne juge pas une réponse dont on ne sait pas quelle version on a lue.

## Actions manuelles et problèmes de sécurité (quand l'accès GSC le permet)

L'inspection d'URL ne couvre ni les actions manuelles ni les problèmes de sécurité : un résultat d'inspection correct ne suffit pas à les exclure. Quand la propriété Search Console est accessible, ouvrir les deux rapports dédiés de l'interface (Sécurité et actions manuelles) et relever ce qu'ils affichent, date comprise. Sans accès : écrire « actions manuelles et problèmes de sécurité non vérifiés, accès Search Console requis », jamais « aucun ».

## Récurrence — programmation via `/schedule`

Pour transformer l'audit ponctuel en monitoring continu :
```
/schedule
```
Choix structurants :
- **Récurrence** : `cron_expression: "0 1 1 * *"` (1er de chaque mois, 01h UTC)
- **Alternative one-shot** : `run_once_at` à J+14 après un déploiement de cluster
- **Modèle** : `claude-sonnet-4-6` (Opus inutile pour ce job)
- **Tools** : `Bash, Read, Write, Edit, Glob, Grep`
- **Environment** : Default Anthropic Cloud

À chaque exécution : 5 à 10 min de tourner-en-fond, rapport posté dans la conversation (ou push d'une PR si configuré côté repo).

## Réutilisation client

Pour appliquer ce skill à un client en accompagnement :
1. Créer un fichier `urls-prio.txt` dans son repo (top 30 pages business) OU pointer le sitemap public
2. Adapter le périmètre du maillage (hubs spécifiques au site)
3. Schedule cron mensuel
4. Inclure le rapport mensuel dans la note de suivi

Coût marginal par client : ~15 min de setup, 0 € récurrent. À facturer dans la rétro mensuelle ou comme bonus différenciant en pitch.

## Concepts liés

`grounding-score` · `passage-ranking`
