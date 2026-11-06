---
name: seo-core-web-vitals
description: "Audit Core Web Vitals (LCP, CLS, TBT) via Lighthouse, mobile. « audit CWV », « vitesse de chargement »."
---

# Skill — Audit Core Web Vitals (Lighthouse local)

## Quand utiliser ce skill

Audit Core Web Vitals (LCP, CLS, TBT) d'un site via Lighthouse local sur un échantillon d'URLs depuis sitemap.xml. Mobile-first. Produit un tableau de scores par URL + problèmes récurrents site-wide + plan de correction priorisé pour les 5 pires pages. Sortie obligatoire en plus du tableau : un rapport de pré-décision (diagnostic, preuves typées, état Critique / À améliorer / Sain, actions P1-P3 avec confiance, effort et risque, jamais de score affiché) ; sans lui le skill n'a pas terminé.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "audit Core Web Vitals", "audit CWV", "perf SEO", "LCP CLS TBT", "Lighthouse audit", "vitesse de chargement", "audit performance site", "pourquoi mon site est lent en SEO", "PageSpeed score", "audit perf mobile", "score Lighthouse", "audit Web Vitals".

Skill du périmètre SEO technique. Complémentaire de `indexation-check`, `seo-donnees-structurees`, `seo-cannibalisation`, `maillage-systeme`.

## Quand déclencher

Diagnostic de performance SEO d'un site complet, ou avant intervention technique (refonte, optimisation perf, migration). Toujours mobile (Google = mobile-first indexing).

## Pré-requis (à vérifier en début de skill)

```bash
which lighthouse || echo "MANQUANT — installer : npm install -g lighthouse"
which jq || echo "MANQUANT — installer : brew install jq"
```

Si Lighthouse manque, proposer `npm install -g lighthouse` à l'utilisateur et stopper. Ne pas installer silencieusement.

Alternative sans install globale : remplacer `lighthouse` par `npx lighthouse` dans toutes les commandes (premier lancement plus lent).

## Input requis

| Source | Obligatoire | Défaut |
|--------|-------------|--------|
| URL du sitemap.xml (ex. `https://site.com/sitemap.xml`) | Oui | — |
| Échantillon | Non | 50 URLs |
| Mode `all` (audit toutes les URLs du sitemap) | Non | off |

## Pipeline (5 étapes)

### Étape 1 — Récupérer le sitemap

```bash
SITEMAP_URL="<url>"
curl -sL "$SITEMAP_URL" | grep -oE '<loc>[^<]+</loc>' | sed -E 's|</?loc>||g' > /tmp/cwv-urls.txt
wc -l /tmp/cwv-urls.txt
```

**IMPORTANT (compat BSD/macOS)** : utiliser `sed -E 's|</?loc>||g'` et **PAS** `sed 's|</\?loc>||g'` — le `\?` ne marche pas en sed BSD (macOS) et laisse les balises intactes silencieusement.

**Si le sitemap est un index** (contient `<sitemapindex>` au lieu de `<urlset>`), récupérer le premier sitemap enfant et l'utiliser :

```bash
FIRST_CHILD=$(curl -sL "$SITEMAP_URL" | grep -oE '<loc>[^<]+</loc>' | sed -E 's|</?loc>||g' | head -1)
curl -sL "$FIRST_CHILD" | grep -oE '<loc>[^<]+</loc>' | sed -E 's|</?loc>||g' > /tmp/cwv-urls.txt
```

### Étape 2 — Échantillonner

```bash
TOTAL=$(wc -l < /tmp/cwv-urls.txt | tr -d ' ')
if [ "$TOTAL" -gt 50 ] && [ "$MODE" != "all" ]; then
  head -50 /tmp/cwv-urls.txt > /tmp/cwv-sample.txt
else
  cp /tmp/cwv-urls.txt /tmp/cwv-sample.txt
fi
wc -l /tmp/cwv-sample.txt
```

Les 50 premières URLs du sitemap sont généralement les plus prioritaires (homepage, hubs, top articles). Si l'utilisateur demande `all`, auditer toutes les URLs.

### Étape 3 — Lancer Lighthouse mobile en parallèle (3 workers)

```bash
rm -rf /tmp/cwv-results /tmp/cwv-errors.log
mkdir -p /tmp/cwv-results
cat /tmp/cwv-sample.txt | xargs -I {} -P 3 sh -c '
  url="$1"
  hash=$(echo -n "$url" | md5)
  lighthouse "$url" \
    --output=json \
    --output-path="/tmp/cwv-results/${hash}.json" \
    --only-categories=performance \
    --form-factor=mobile \
    --screenEmulation.mobile=true \
    --chrome-flags="--headless=new --no-sandbox" \
    --quiet 2>/dev/null || echo "FAIL: $url" >> /tmp/cwv-errors.log
' _ {}
echo "Results: $(ls /tmp/cwv-results/ 2>/dev/null | wc -l | tr -d ' ')"
[ -f /tmp/cwv-errors.log ] && echo "Errors:" && cat /tmp/cwv-errors.log
```

**IMPORTANT (zsh-safe)** : utiliser `rm -rf /tmp/cwv-results && mkdir -p /tmp/cwv-results` et **PAS** `rm -f /tmp/cwv-results/*` — le glob vide fait gueuler zsh (`no matches found`) et l'exit code 1 peut interrompre la suite.

**`--headless=new`** (et pas `--headless` legacy) — plus stable depuis Chrome 109+, requis pour Lighthouse 13.

**Compter** : ~15-30 secondes par URL avec 3 workers parallèles. 50 URLs ≈ 5-10 min.

### Étape 4 — Parser les résultats

Pour chaque JSON dans `/tmp/cwv-results/`, extraire avec jq (chemin Lighthouse 13) :

```bash
for f in /tmp/cwv-results/*.json; do
  jq '{
    url: .finalDisplayedUrl,
    lcp_ms: (.audits."largest-contentful-paint".numericValue // 0),
    cls: (.audits."cumulative-layout-shift".numericValue // 0),
    tbt_ms: (.audits."total-blocking-time".numericValue // 0),
    score: ((.categories.performance.score // 0) * 100),
    lcp_element: [.audits."lcp-breakdown-insight".details.items[]? | select(.type == "node") | {selector, snippet, nodeLabel}] | .[0],
    lcp_breakdown: [.audits."lcp-breakdown-insight".details.items[]? | select(.type == "table") | .items[]? | {subpart, label, duration_ms: .duration}],
    opportunities: [.audits | to_entries[] | select(.value.details.type == "opportunity" and (.value.details.overallSavingsMs // 0) > 100) | {id: .key, title: .value.title, savings_ms: .value.details.overallSavingsMs}] | sort_by(-.savings_ms) | .[0:5]
  }' "$f"
done | jq -s '.' > /tmp/cwv-parsed.json
echo "Parsed: $(jq 'length' /tmp/cwv-parsed.json) URLs"
```

**Chemins clés Lighthouse 13** :
- URL finale : `.finalDisplayedUrl` (et **PAS** `.finalUrl` qui peut être null)
- LCP element : `.audits."lcp-breakdown-insight".details.items[] | select(.type == "node")` (et **PAS** `.audits."largest-contentful-paint-element"` qui est null depuis LH 13)
- LCP breakdown (TTFB / render delay / load delay) : `.audits."lcp-breakdown-insight".details.items[] | select(.type == "table") | .items[]` — utile pour diagnostiquer **où** se passe le temps LCP

**Seuils Google (à appliquer pour le verdict)** :

| Métrique | Good | Needs Improvement | Poor |
|----------|------|-------------------|------|
| LCP | < 2500 ms | 2500-4000 ms | > 4000 ms |
| CLS | < 0.1 | 0.1-0.25 | > 0.25 |
| TBT (proxy INP) | < 200 ms | 200-600 ms | > 600 ms |
| Score perf | ≥ 90 | 50-89 | < 50 |

### Étape 5 — Produire le rapport markdown

Voir section "Output obligatoire" ci-dessous.

### Étape 4bis — Détection automatique du pattern "redirect sitemap"

Si l'opportunity `redirects` apparaît sur **>50% des pages auditées** avec un gain moyen >300ms : c'est quasi-certainement un mismatch de trailing slash entre le sitemap et le serveur.

```bash
REDIRECT_COUNT=$(jq -r '.[] | .opportunities[] | select(.id == "redirects") | .id' /tmp/cwv-parsed.json | wc -l | tr -d ' ')
TOTAL=$(jq 'length' /tmp/cwv-parsed.json)
if [ "$REDIRECT_COUNT" -gt $((TOTAL / 2)) ]; then
  echo "⚠️ ALERTE : $REDIRECT_COUNT/$TOTAL pages ont une redirection. Vérifier le trailing slash du sitemap vs serveur."
fi
```

Ce pattern doit être mis EN TÊTE du rapport — c'est le quick win le plus rentable quand il est présent.

### Étape 4ter — Données terrain, LCP / INP / CLS au 75e percentile 

Lighthouse reste pour le diagnostic. L'évaluation des Core Web Vitals, elle, repose sur les données terrain : les ajouter chaque fois qu'elles existent, pour les pages business prioritaires et l'origine.

Source gratuite : l'API PageSpeed Insights, qui renvoie le champ terrain CrUX en plus du test.

```bash
# clé API Google gratuite dans $PSI_KEY ; strategy = mobile, puis desktop si justifié
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${URL}&strategy=mobile&key=${PSI_KEY}" \
| jq '{
    url_scope:    .loadingExperience.id,
    url_lcp_p75:  .loadingExperience.metrics.LARGEST_CONTENTFUL_PAINT_MS.percentile,
    url_inp_p75:  .loadingExperience.metrics.INTERACTION_TO_NEXT_PAINT.percentile,
    url_cls_p75:  .loadingExperience.metrics.CUMULATIVE_LAYOUT_SHIFT_SCORE.percentile,
    url_verdict:  .loadingExperience.overall_category,
    origin_scope: .originLoadingExperience.id,
    origin_lcp_p75: .originLoadingExperience.metrics.LARGEST_CONTENTFUL_PAINT_MS.percentile,
    origin_inp_p75: .originLoadingExperience.metrics.INTERACTION_TO_NEXT_PAINT.percentile,
    origin_cls_p75: .originLoadingExperience.metrics.CUMULATIVE_LAYOUT_SHIFT_SCORE.percentile,
    origin_verdict: .originLoadingExperience.overall_category
  }'
```

Règles de lecture :

- **Le périmètre précède le chiffre** : URL ou origine, mobile ou desktop, 75e percentile, 28 jours. Quand `loadingExperience` est absent et que seul `originLoadingExperience` répond, PageSpeed est retombé sur l'origine : la valeur décrit le site, pas la page, et le rapport l'écrit.
- **Mobile par défaut, desktop aussi** quand l'usage du site ou un écart entre les deux appareils justifie l'analyse.
- **L'INP ne vient que d'ici.** Le TBT du test ne le remplace pas.
- **Sans données terrain** (site trop peu visité, URL sans échantillon) : « Expérience réelle non évaluée ; les mesures de test, elles, sont disponibles. » Ni échec ni validation des Core Web Vitals.
- Ne jamais présenter un écart terrain / test comme une contradiction : les deux répondent à des questions différentes.

## Sortie de pré-décision (obligatoire)

Ce skill n'a pas terminé tant que le rapport de pré-décision n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau, et il suit `audit-complet-v2/rapport-audit-seo-format.md` (`audit-complet-v2/rapport-audit-seo-format.md`). Fichier : `wiki/audit/YYYY-MM-DD-slug-performance-decision.md`.

Ce qu'il contient, dans cet ordre :

1. Diagnostic principal : une phrase, la cause structurante, pas une liste d'erreurs
2. Les chiffres à retenir : 3 à 5, ceux qui illustrent le diagnostic
3. État : Critique, À améliorer ou Sain, calculé sur l'impact SEO réel et le type de page, jamais sur le nombre d'erreurs ; jamais de score sur 10
4. Problèmes (3 maximum) et opportunités (5 maximum), séparés : chacun avec Preuve (2 à 4 données), Pourquoi c'est important, Action, Confiance (forte / moyenne / faible) ; chaque problème s'écrit en trois temps : observation prouvée → conséquence ou risque justifié → bénéfice attendu de la correction (l'observation seule n'est pas un frein SEO démontré)
5. Actions P1 / P2 / P3, 3 P1 maximum : pourquoi, preuve, signal attendu (jamais un résultat chiffré promis), dépendance préalable, test de validation (ce qui distingue « correction appliquée » de « résultat SEO observé »), effort faible / moyen / élevé (jamais en heures), confiance, risque low / medium / high ; toute action high (suppression, 301, fusion, changement d'URL) porte « À valider avant déploiement » et sa checklist
6. Ce que les données ne permettent pas de conclure, et « données insuffisantes » ou « ne rien faire » quand c'est le cas

Sur le périmètre de ce skill, le rapport tranche la performance Lighthouse mobile (jamais « Core Web Vitals » sans CrUX ; INP « non mesuré », TBT proxy technique) : une phrase globale puis Page / LCP / Importance, performance × importance de la page, les pages stratégiques seulement.

Règles : chaque information est typée FACT, HYPOTHESIS ou ACTION, jamais une hypothèse écrite comme un fait ; un problème existe une seule fois (ID), les observations qui parlent du même problème fusionnent ; une anomalie n'est pas une priorité par défaut ; les pages business et les tendances GSC passent avant les anomalies techniques secondaires ; jamais de recommandation automatique de fusion, 301, suppression, réécriture ou création de page ; Google n'est jamais anthropomorphisé. Phrases courtes, une donnée par diagnostic, aucune des phrases « Il est important de », « Il convient de », « Cela peut potentiellement », « Il est intéressant de noter », « Dans le cadre de ».

Restitution (corrections V2 du 23 septembre) : aucun ID technique ni mot anglais (low / medium / high) dans le rapport ; Faible / Moyen / Élevé partout ; la certitude affichée ne dépasse jamais la couverture des données (« aucun problème majeur détecté sur les URL inspectées », pas « Sain ») ; formulations précises (« URL en 404 avec encore des impressions ») ; aucune action proposée sur une page dont les requêtes ne sont pas connues (« à vérifier ») ; le nombre de mots seul n'est jamais un problème ; limites de longueur : diagnostic 70 mots, 4 chiffres, 3 problèmes de 40 mots, 6 actions, 3 opportunités de 35 mots, le reste dans les détails repliés.

Onglet Analyse technique, structure validée le 23 septembre 2026 (référence : [[audit/2026-09-22-organikk-co]]) : chaque priorité = une phrase de cadrage, « Ce qu'on observe » (faits chiffrés en liste, pages en code), « Pourquoi c'est prioritaire » (deux phrases), « Action » (liste numérotée courte), « Impact attendu » et « Risque » en gras ; puis le plan des 30 jours en trois paliers (Priorité immédiate, Deuxième étape, Priorité secondaire), une action par paragraphe en gras suivie d'une phrase ; puis « à surveiller avant d'agir » pour la page dont la cause n'est pas isolée ; puis « Autres pages à surveiller » : chiffres séparés par « · », une phrase, verdict en gras (« Aucune action recommandée », « À vérifier avant toute modification »).

## Output obligatoire

Gabarit de l'onglet Vitesse. Chaque placeholder `[...]` vient d'une mesure réelle ou n'apparaît pas.

```markdown
# Vitesse

[Nombre] pages mesurées sur [nombre total], uniquement sur leur URL canonique.

**Source principale :** [Lighthouse mobile / PageSpeed Insights / CrUX]
**Type de mesure :** [test / terrain]
**Score Lighthouse médian :** [XX]/100

## Chiffres à retenir

| Mesure | Résultat |
|---|---:|
| **Score Lighthouse médian** | [XX]/100 |
| **LCP médian** | [X,XX s] |
| **Pages avec LCP > 4 s** | [XX / XX] |
| **CLS médian** | [X,XXX] |
| **Pages avec CLS > 0,25** | [XX / XX] |
| **TBT médian** | [XX ms] |
| **TTFB médian** | [XXX ms] |
| **Page business la plus exposée** | `[URL]` · [impressions] impressions · LCP [X,XX s] |

---

## Ce que les mesures montrent

### LCP

**[XX sur XX] pages dépassent [seuil].**

LCP médian : **[X,XX s]**
Fourchette observée : **[X,XX s à X,XX s]**

[Interprétation courte.]

Exemple :

> Le problème n'est pas limité à quelques URL : il apparaît sur l'ensemble du gabarit testé. Cela oriente davantage vers une cause commune qu'un problème propre à une seule page.

Ne pas conclure à la cause à ce stade.

---

### CLS

CLS médian : **[X,XXX]**

- [XX] pages dans la zone correcte ;
- [XX] pages à surveiller ;
- [XX] pages dégradées.

[Interprétation.]

Si aucun problème :

> Aucun problème généralisé de stabilité visuelle n'est détecté.

---

### Interactivité

**TBT test :** [XX ms]

Le TBT sert uniquement d'indicateur test. Il ne doit pas être présenté comme une mesure INP réelle.

Si aucune donnée terrain n'est disponible :

> L'INP réel des visiteurs n'est pas mesurable avec ce relevé.

---

## Terrain et test

### Données test

- Lighthouse : [version]
- appareil simulé : [mobile]
- réseau / CPU : [conditions]
- nombre de pages : [XX]
- nombre de passages par page : [X]

### Données terrain

[CrUX disponible / CrUX indisponible]

Si disponible, le périmètre d'abord, sans lui le chiffre ne se lit pas : **[URL / origine] · [mobile / desktop] · 75e percentile · 28 derniers jours**. Une valeur d'origine ne décrit pas la page : le dire quand PageSpeed est retombé sur l'origine faute de données pour l'URL.

| Mesure terrain (p75) | Résultat |
|---|---:|
| LCP | [X,XX s] |
| INP | [XXX ms] |
| CLS | [X,XXX] |
| TTFB | [XXX ms] |

Si indisponible :

> Expérience réelle non évaluée ; les mesures de test, elles, sont disponibles.

Ce n'est ni un échec des Core Web Vitals ni une validation de ceux-ci : l'évaluation des Core Web Vitals repose sur les mesures terrain, et elles manquent.

Ne jamais présenter une différence terrain / test comme une contradiction : les deux mesures répondent à des questions différentes.

---

## Qualité de la mesure

### Variance observée

Une même URL mesurée plusieurs fois donne :

- run 1 : [score / LCP]
- run 2 : [score / LCP]
- run 3 : [score / LCP]

**Lecture :**

> Un score Lighthouse isolé ne doit pas être interprété au point près. La tendance globale, la médiane et les problèmes répétés entre plusieurs pages sont plus fiables que le classement individuel d'une URL.

---

### Mesures écartées

[Décrire ici toute première passe faussée.]

Exemples :

- URL redirigées ;
- mauvaise variante canonique ;
- pages inexistantes servant un fallback ;
- cache différent ;
- timeout ;
- mesure interrompue.

**Pourquoi elles sont écartées :**

[Explication.]

Ne jamais mélanger ces mesures avec le relevé final.

---

## Décomposition du problème

### TTFB

**TTFB médian : [XXX ms]**

Fourchette : [XXX à XXX ms]

**Lecture :**

[correct / à surveiller / dégradé]

Ne conclure à un problème d'hébergement que si les données le permettent.

---

### Temps restant jusqu'au LCP

LCP médian : [X,XX s]
TTFB médian : [X,XX s]

Temps après réponse serveur : **≈ [X,XX s]**

Cela indique que la majeure partie du délai intervient [avant / après] la réponse serveur.

Ne pas attribuer automatiquement ce temps à une cause précise.

Les causes possibles peuvent inclure :

- délai de découverte de la ressource LCP ;
- téléchargement de l'image ou de la police ;
- CSS bloquant ;
- JavaScript ;
- délai de rendu ;
- élément LCP injecté tardivement.

Ces causes restent des hypothèses tant qu'elles ne sont pas mesurées.

---

## Pages à regarder en priorité

| Page | Importance business | Impressions / trafic | LCP | Score | Pourquoi la regarder |
|---|---|---:|---:|---:|---|
| `[URL]` | Forte | [XXX] | [X,XX s] | [XX] | page business exposée |
| `[URL]` | Forte | [XXX] | [X,XX s] | [XX] | même problème |
| `[URL]` | Moyenne | [XXX] | [X,XX s] | [XX] | contrôle du gabarit |

La priorité ne dépend pas uniquement de la page la plus lente.

Croiser :

**gravité technique × importance business × exposition réelle**

---

# Priorités

## 1. [Nom précis du problème]

**État constaté**

[Uniquement les faits mesurés.]

**Preuve**

[Valeurs et pages concernées.]

**Action**

[Action technique précise.]

**Pourquoi le corriger**

[Conséquence défendable.]

**Impact :** [fort / moyen / faible]
**Confiance :** [forte / moyenne / faible]
**Effort :** [faible / moyen / fort]

---

## 2. [Deuxième problème]

Même structure.

---

## 3. [Troisième problème]

Même structure.

---

# Ce qui n'est pas retenu comme problème

### [Signal]

**Mesure :** [valeur]

**Pourquoi il n'est pas retenu :**

[Expliquer pourquoi le signal ne suffit pas.]

Exemples :

> Un score Lighthouse de 68 au lieu de 74 n'est pas en soi une anomalie.

> Une différence entre deux runs ne prouve pas une régression.

> Un TTFB correct n'exclut pas un problème de rendu.

---

# Ce que cette mesure ne permet pas de conclure

- Lighthouse ne mesure pas directement l'expérience réelle de tous les visiteurs.
- TBT n'est pas INP.
- Une corrélation entre une métrique et un composant ne démontre pas sa causalité.
- Une seule passe par URL ne permet pas une comparaison au point près.
- Sans décomposition du LCP, la cause précise ne doit pas être affirmée.
- Sans données CrUX, aucune conclusion sur les Core Web Vitals réels du site ne doit être présentée comme mesurée.
```

## Règles de validation

Un finding de vitesse ne peut être publié que si :

1. la mesure provient de la bonne URL canonique ;
2. les erreurs et redirections parasites ont été écartées ;
3. le problème est reproductible ou visible sur plusieurs pages ;
4. test et terrain ne sont pas mélangés ;
5. la cause n'est pas affirmée sans preuve ;
6. l'impact est distingué du simple score Lighthouse ;
7. les pages business sont prioritaires sur les pages secondaires.

## Règles à interdire

Ne jamais conclure automatiquement :

- `score Lighthouse < 90 = problème` ;
- `TTFB élevé = hébergement mauvais` ;
- `LCP élevé = image trop lourde` ;
- `terrain ≠ test = contradiction` ;
- `une redirection = cause du mauvais score` ;
- `une seule mesure = vérité de la page` ;
- `TBT = INP` ;
- `page la plus lente = priorité SEO n°1`.

Le diagnostic doit toujours suivre :

**mesure → validation de la mesure → localisation du problème → hypothèse de cause → preuve → action**

## Règles absolues

- **Mobile par défaut ; desktop également lorsque son usage ou ses résultats justifient l'analyse** (reformulé le 28/09/2026, remplace « jamais desktop »). Un site B2B lu majoritairement au bureau, ou un écart terrain net entre les deux appareils, justifie la mesure desktop, avec son périmètre écrit.
- **TBT ne remplace pas l'INP.** Le TBT est un indicateur test qui aide à repérer des problèmes de réactivité ; il peut manquer des problèmes d'interaction réels et signaler des blocages que les visiteurs ne rencontrent pas. L'INP ne se lit que dans les données terrain (étape 4ter). Toujours l'écrire dans le rapport.
- **Sans données terrain**, la phrase fixe : « Expérience réelle non évaluée ; les mesures de test, elles, sont disponibles. » Ce n'est ni un échec des Core Web Vitals ni une validation de ceux-ci.
- **Pas de score halluciné** — si une URL échoue (timeout, 404, JS error), la marquer `ERROR` dans le tableau, pas `0` ou un placeholder.
- **Pas de reco sans opportunity Lighthouse correspondante** — ne pas inventer "il faudrait optimiser X" si Lighthouse ne l'a pas remonté pour cette page.
- **Pas d'installation silencieuse** — si Lighthouse manque, demander à l'utilisateur de l'installer.
- **Échantillon honnête** — si l'échantillon est de 50/2000 URLs, le dire clairement, ne pas extrapoler "tout le site" à partir de 2,5% du contenu.

## Edge cases

- **Sitemap index** (sitemapindex au lieu d'urlset) → récupérer le premier child + l'utiliser, signaler à l'utilisateur qu'il peut spécifier un sitemap enfant précis pour cibler.
- **Sitemap protégé** (auth, 403) → demander à l'utilisateur un export local des URLs.
- **Plus de 500 URLs avec mode `all`** → confirmer avec l'utilisateur (sera lent : 500 URLs × ~10s/3 workers ≈ 30 min).
- **Site en SPA ou auth-walled** → certaines pages peuvent timeout, c'est normal, les marquer ERROR.
- **Sitemap multi-langues** → garder tel quel, le rapport montrera les écarts par locale.
