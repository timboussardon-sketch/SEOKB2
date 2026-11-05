---
title: "Jour 2 Semaine 3 — Cannibalisation + Maillage GSC (bundle 2 skills + pédagogie)"
bootcamp: 4
semaine: 3
jour: 2
type: skill-distribuable
usage: "Bundle Drive S3 — un seul export GSC, deux lectures. seo-cannibalisation (pack des 9 #3, re-bundle/vérif) + maillage-interne-gsc (hors pack, vraie install). À dérouler dans l'ordre : cannibalisation d'abord, maillage ensuite."
related:
  - "[[sequencage-semaine-3]]"
  - "[[workflow-audit-bootcamp4]]"
  - "[[skill-maillage-systeme]]"
  - "[[skill-audit-engine-pipeline]]"
  - "[[session-3-audit-prep]]"
---

# Jour 2 — Semaine 3 : un export GSC, deux lectures

Salut à tous,

Jour 2. Vous avez votre export GSC posé depuis hier. Aujourd'hui on ne ré-exporte rien : on lit la même matière première deux fois, sous deux angles, avec deux skills qui se chaînent. La cannibalisation lit l'export **par requête** (quelles requêtes déclenchent 2+ URLs). Le maillage lit le même export **par page** (qui mérite d'être mère, qui est sous-maillée). Même fichier, deux questions.

L'ordre n'est pas négociable, et c'est tout l'enjeu de la journée. **Cannibalisation d'abord, maillage ensuite.** Si vous lancez le maillage avant d'avoir trié les conflits, vous allez bétonner des liens vers une page qui n'aurait jamais dû se battre avec une autre. Vous renforcez le problème au lieu de le régler.

## Pourquoi la cannibalisation passe avant le maillage

Une cannibalisation a deux causes racines possibles : **contenu** ou **maillage**. C'est le skill cannibalisation qui tranche laquelle. Le croisement clé (à faire avec votre audit Hn d'hier) : si les H1/H2 des deux pages se chevauchent, c'est un problème de contenu, on différencie ou on fusionne. Si les Hn sont distincts mais Google hésite quand même entre les deux URLs, ce n'est pas un problème de contenu : **c'est un problème de maillage**. Et ça, ça ne se règle pas en fusionnant, ça se règle en désignant clairement la page mère par les liens internes.

Donc les conflits classés "root cause = maillage" par le premier skill deviennent directement des entrées du plan du second skill. La cannibalisation produit le diagnostic. Le maillage produit l'action structurelle. L'un sans l'autre, vous fusionnez des pages qu'il fallait garder, ou vous maillez dans le vide.

Le seul cas qui inverse la logique : la **Triade SERP**. Si la cannibalisation détecte deux URLs légitimement positionnées sur deux intentions distinctes derrière une requête ambiguë, aucune action côté cannibalisation, et le maillage doit au contraire les différencier davantage par les ancres (deux promesses distinctes, jamais la même ancre vers les deux). C'est le seul cas où "deux pages sur une requête" n'est pas un bug.

## Cas pratique enchaîné (site artisan plombier)

GSC, requête "débouchage canalisation", déclenche 2 URLs : `/debouchage-canalisation` (page service, intention Do) et `/blog/comment-deboucher-une-canalisation` (article, intention Know). Positions 8 et 11, impressions cumulées fortes, CTR au sol.

**Skill cannibalisation.** Type B (même intention dominante "débouchage", micro-intentions différentes : Do "je veux un plombier" vs Know "je veux le faire moi-même"). Croisement Hn (audit d'hier) : les Hn sont distincts. Donc root cause = maillage, pas contenu. Action : ni 301, ni fusion. On passe la main.

**Handoff vers le skill maillage.** La page Do `/debouchage-canalisation` devient **page mère** (requête transactionnelle, business value). L'article `/blog/...` devient **fille**. Règle Know vers Do : l'article doit pointer vers le service avec une ancre qui porte l'intention Do ("faire intervenir un plombier pour un débouchage"), jamais "cliquez ici", jamais la même ancre que les autres pages filles. On coupe les liens internes transactionnels qui pointaient vers l'article (ils nourrissaient la mauvaise page), on draine les liens du cluster vers la mère.

**Résultat.** Google arrête d'hésiter parce que le maillage a tranché pour lui qui est la mère. Le CTR remonte sur la Do, l'article garde son trafic Know mais alimente le funnel au lieu de le siphonner.

## Livrable du Jour 2

Un fichier dans `audit/` qui contient, dans cet ordre : la liste des cannibalisations avec type (A/B/C/Triade) et root cause (contenu ou maillage), puis le plan de maillage où chaque conflit "root cause = maillage" apparaît comme une action (mère désignée, ancre, liens à couper, liens à créer). Une cannibalisation classée "maillage" qui n'a pas sa contrepartie dans le plan de maillage = livrable incomplet.

Pré-condition cannibalisation : moins de 10 URLs dans votre GSC, on documente un diagnostic de "sous-granularité" (constat valide, pas un échec) et on passe direct au maillage structurel.

---

## Procédure d'install / vérification

Deux skills. Le premier est dans le pack des 9 (vérification), le second est une vraie nouvelle install.

**1. `seo-cannibalisation`** — pack des 9 (#3). Vous l'avez normalement déjà. Vérifiez que `~/.claude/skills/seo-cannibalisation/SKILL.md` correspond au bloc ci-dessous. S'il est plus court, écrasez-le.

**2. `maillage-interne-gsc`** — hors pack des 9. À installer : dossier `~/.claude/skills/maillage-interne-gsc/`, `SKILL.md` = le second bloc ci-dessous.

Ne le confondez pas avec `maillage-systeme` (pack #4, passe structurelle sans GSC) : celui d'aujourd'hui est la passe **data**, il a besoin de l'export GSC. Relancez Claude, vérifiez avec `/skills`.

GSC, install ou skill qui coince ? MP aujourd'hui, pas vendredi.

=====

---
name: seo-cannibalisation
description: |
  Audit de cannibalisation SEO depuis les données GSC. Identifie les pages en compétition interne sur les mêmes mots-clés ou intentions, classifie le type de conflit (mot-clé exact, même intention, proximité sémantique, Triade SERP), analyse les métriques, recommande l'action (301, fusion, différenciation, maillage croisé, ou aucune action si Triade SERP). Sortie obligatoire en plus du tableau : un doc final d'une page, résumé + score + 5 actions prioritaires ; sans lui le skill n'a pas terminé.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "cannibalisation", "deux pages sur le même mot-clé", "je rankais mieux avant", "pages en compétition interne", "keyword cannibalism", "audit cannibalisation".
---

# Skill — Cannibalisation SEO

## Quand déclencher

Deux pages se concurrencent sur les mêmes mots-clés ou intentions. Chutes de positions inexpliquées, CTR qui stagne malgré le volume.

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Export GSC Requêtes — filtré par URL, 90j | Oui |
| Liste des URLs (scraping ou sitemap) | Recommandé |
| Contexte stratégique (pilier vs satellite) | Recommandé |

## Pipeline (5 étapes)

1. **Identifier les conflits** — requêtes qui déclenchent 2+ URLs dans la GSC
2. **Classifier le type** :
   - **(A) Mot-clé exact** — deux pages sur la même requête précise
   - **(B) Même intention** — deux pages répondent à la même intention
   - **(C) Proximité sémantique** — sujets proches sans conflit direct
   - **(Triade SERP)** — opportunité, pas conflit
3. **Analyser les métriques** — position, impressions, clics, CTR par page
4. **Évaluer l'architecture** — pilier vs satellite, objectif business
5. **Recommander l'action** :

| Situation | Action |
|-----------|--------|
| Type A + perdante faible | Redirection 301 |
| Type A + deux fortes | Fusion + 301 |
| Type B + micro-intentions distinctes | Différenciation + maillage croisé |
| Type C | Renforcement maillage vers pilier |
| Triade SERP | Aucune action — optimiser chaque angle |

## Doc final en sortie (obligatoire)

Ce skill n'a pas terminé tant que le doc final n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau. Une page, `wiki/audit/YYYY-MM-DD-slug-cannibalisation-resume.md`, dans cet ordre :

1. Périmètre : site ou thématique, date, période de données, nombre d'éléments analysés
2. Score : score sur 10 = part des requêtes business sans conflit interne, le chiffre source, les 3 conflits les plus coûteux
3. Actions prioritaires : 5 au maximum, numérotées dans l'ordre d'exécution, une ligne chacune avec la page, l'effort et qui la fait

Aucune phrase sans chiffre ou constat derrière. Pas d'introduction, pas de conclusion. Dans le workflow complet, ce doc nourrit la Phase 7 de l'audit ou le doc final du workflow mots-clés.

## Output obligatoire

```
CANNIBALISATION DÉTECTÉE
Requête : '[requête]' — Type : (A/B/C/Triade)
| URL | Position | Impressions | Clics | CTR | Statut |

→ Diagnostic : [explication]
→ Action : [action précise + 3 étapes d'implémentation]
```

## Règles absolues

- Ne pas recommander une 301 sans analyser les métriques des deux pages
- Ne pas traiter toutes les cannibalisations de la même façon
- Ne pas confondre duplication de contenu et cannibalisation
- Ne pas fusionner des pages avec micro-intentions distinctes
- Identifier les Triades SERP comme opportunités, pas comme problèmes

## Sauvegarde

Output dans `wiki/cannibalisation/YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`triade-serp` · `rrf` · `maillage-interne` · `intention-recherche` · `gsc-export`



## Phase apprentissage (boucle)

Cette phase tourne APRES la production. Elle ne change jamais le code du skill toute seule.

1. **Briefing memoire** (debut de run, AVANT de produire) : lire `/Users/timothee/Code/seo-kb/loops/seo-cannibalisation/manifest.yml` puis
   `/Users/timothee/Code/seo-kb/loops/seo-cannibalisation/memory/` (directives, score-grid, wording_rules, questions) et `/Users/timothee/Code/seo-kb/loops/seo-cannibalisation/ledgers/said_index.jsonl`
   pour ne pas repeter un angle deja couvert.

2. **Production** : faire le travail du skill normalement, en appliquant directives + score-grid.

3. **Ledger date** (append-only, jamais reecrire) dans `/Users/timothee/Code/seo-kb/loops/seo-cannibalisation/ledgers/` :
   - `runs.jsonl` : 1 ligne {date, ce qui a ete produit, `capture_mode`: "native"}.
   - `claims.jsonl` : 1 ligne par fait/chiffre, avec sources (>=2 dont 1 primaire) et `capture_mode`.
   - `predictions.jsonl` : si le run produit du mesurable, 1 pari date {id, enonce, `resolve_by`: AAAA-MM-JJ (J+30 ou J+90)}.
   - `said_index.jsonl` : angles/sujets couverts ce run.
   - `mistakes.jsonl` : ce qui a sous-performe (rempli a la resolution, pas a la prod).

4. **Gate** : lancer `../_loop-kit/validate.sh /Users/timothee/Code/seo-kb/loops/seo-cannibalisation` (ou `./validate.sh`). Si echec : corriger, ne pas commit.
   Optionnel : `../_loop-kit/eval_health.py /Users/timothee/Code/seo-kb/loops/seo-cannibalisation` pour le signal OK / WATCH / ESCALATE.

5. **Propositions de code** : si la boucle "voudrait" changer le skill (nouvelle regle, seuil, formulation),
   elle NE le fait pas. Elle ecrit le diff propose + la raison dans `/Users/timothee/Code/seo-kb/loops/seo-cannibalisation/memory/questions.md`. Tim tranche a la revue.

Regle d'or : **autonome sur la data, supervise sur le code.**

=====

---
name: maillage-interne-gsc
description: |
  Analyse et optimisation du maillage interne depuis les données GSC. Hiérarchie page mère/fille/petite-fille selon la méthode Boussardon. Pipeline en 5 étapes : récupérer GSC → diagnostiquer la structure (mères potentielles, sous-maillées, orphelines) → construire le plan de maillage avec règles Know→Do → prioriser par score urgence → générer recommandations (page source, destination, ancre, contexte). Sortie obligatoire en plus du tableau : un doc final d'une page, résumé + score + 5 actions prioritaires ; sans lui le skill n'a pas terminé.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "maillage interne", "liens internes", "cocon SEO", "pages orphelines", "GSC + structure de site", quand un fichier GSC est uploadé.
---

# Skill — Maillage Interne GSC

## Quand déclencher

Analyse et optimisation du maillage interne depuis les données GSC. Hiérarchie page mère/fille/petite-fille.

## Philosophie

> "Le maillage interne, c'est la puissance. Et ça part de tes mots-clés."

- Page mère = au moins 5 citations depuis des pages filles/petites-filles
- Le maillage part de la stratégie de mots-clés → le cocon est la conséquence
- Priorité : transactionnel > décisionnel > informationnel
- Maillage par intention (Know → Do) en plus du maillage sémantique

## Input requis

| Source | Obligatoire |
|--------|-------------|
| Export GSC Pages — URL, Clics, Impressions, CTR, Position | Oui |
| Export GSC Requêtes par page | Recommandé |
| Période 3-6 mois | Recommandé |

## Pipeline (5 étapes)

1. **Récupérer les données GSC** — export Pages + Requêtes par URL
2. **Diagnostiquer la structure** :
   - Pages mères potentielles (impressions élevées, pos 4-15, requête transactionnelle)
   - Pages sous-maillées (bonne position mais CTR faible)
   - Pages orphelines (aucune thématique secondaire dans GSC)
3. **Construire le plan de maillage** — hiérarchie mère/fille/petite-fille + règles Know→Do
4. **Prioriser** — score urgence = (Impressions × 0.4) + (Potentiel position × 0.4) + (Business value × 0.2)
5. **Générer les recommandations** — page source + page destination + ancre + contexte + priorité

## Structure hiérarchique

```
Page Mère (mot-clé principal business)
├── Page Fille 1 (requête secondaire transactionnelle)
│   ├── Page Petite-Fille A (longue traîne / micro-intention)
│   └── Page Petite-Fille B
└── Page Fille 2
```

Règle Know → Do : chaque page Know doit pointer vers au moins 1 page Do thématiquement reliée.

## Doc final en sortie (obligatoire)

Ce skill n'a pas terminé tant que le doc final n'est pas écrit. Il fait partie de la sortie, au même titre que le tableau. Une page, `wiki/maillage/YYYY-MM-DD-slug-gsc-resume.md`, dans cet ordre :

1. Périmètre : site ou thématique, date, période de données, nombre d'éléments analysés
2. Score : score sur 10 = part des pages business qui reçoivent des liens internes, le chiffre source, les 3 pages business les moins reliées
3. Actions prioritaires : 5 au maximum, numérotées dans l'ordre d'exécution, une ligne chacune avec la page, l'effort et qui la fait

Aucune phrase sans chiffre ou constat derrière. Pas d'introduction, pas de conclusion. Dans le workflow complet, ce doc nourrit la Phase 7 de l'audit ou le doc final du workflow mots-clés.

## Output obligatoire

Pour chaque action :
- Page source (intention Know/Do/Know+Do)
- Page destination + intention
- Nature du lien (sémantique ou intentionnel Know→Do)
- Ancre recommandée (jamais "cliquez ici")
- Contexte d'insertion
- Priorité (Haute/Moyenne/Faible)

## Règles absolues

- Ne pas automatiser à 100% — le maillage part de la stratégie, pas des outils
- Ne pas mailler sans tenir compte de l'intention (sémantique ≠ intentionnel)
- Ne pas répéter la même ancre sur toutes les pages filles
- 10 citations minimum pour une page mère "active"

## Sauvegarde

Output dans `wiki/maillage/YYYY-MM-DD-slug.md` selon hook §7 AGENTS.md.

## Concepts liés

`cocon-semantique` · `pagerank-interne` · `intention-recherche` · `cannibalisation` · `gsc-export`



## Phase apprentissage (boucle)

Cette phase tourne APRES la production. Elle ne change jamais le code du skill toute seule.

1. **Briefing memoire** (debut de run, AVANT de produire) : lire `/Users/timothee/Code/seo-kb/loops/maillage-interne-gsc/manifest.yml` puis
   `/Users/timothee/Code/seo-kb/loops/maillage-interne-gsc/memory/` (directives, score-grid, wording_rules, questions) et `/Users/timothee/Code/seo-kb/loops/maillage-interne-gsc/ledgers/said_index.jsonl`
   pour ne pas repeter un angle deja couvert.

2. **Production** : faire le travail du skill normalement, en appliquant directives + score-grid.

3. **Ledger date** (append-only, jamais reecrire) dans `/Users/timothee/Code/seo-kb/loops/maillage-interne-gsc/ledgers/` :
   - `runs.jsonl` : 1 ligne {date, ce qui a ete produit, `capture_mode`: "native"}.
   - `claims.jsonl` : 1 ligne par fait/chiffre, avec sources (>=2 dont 1 primaire) et `capture_mode`.
   - `predictions.jsonl` : si le run produit du mesurable, 1 pari date {id, enonce, `resolve_by`: AAAA-MM-JJ (J+30 ou J+90)}.
   - `said_index.jsonl` : angles/sujets couverts ce run.
   - `mistakes.jsonl` : ce qui a sous-performe (rempli a la resolution, pas a la prod).

4. **Gate** : lancer `../_loop-kit/validate.sh /Users/timothee/Code/seo-kb/loops/maillage-interne-gsc` (ou `./validate.sh`). Si echec : corriger, ne pas commit.
   Optionnel : `../_loop-kit/eval_health.py /Users/timothee/Code/seo-kb/loops/maillage-interne-gsc` pour le signal OK / WATCH / ESCALATE.

5. **Propositions de code** : si la boucle "voudrait" changer le skill (nouvelle regle, seuil, formulation),
   elle NE le fait pas. Elle ecrit le diff propose + la raison dans `/Users/timothee/Code/seo-kb/loops/maillage-interne-gsc/memory/questions.md`. Tim tranche a la revue.

Regle d'or : **autonome sur la data, supervise sur le code.**

=====

## Note pour Tim (interne)

- **Écart de séquençage à trancher.** `[[sequencage-semaine-3]]` (bootcamp 4) place aujourd'hui cannibalisation en **J3** (Phase 4) et maillage en **J4** (Phase 5, passe data 5C = `maillage-interne-gsc`). Ce bundle les fusionne en **J2**. Si c'est un re-séquençage volontaire de la S3 (workflow audit resserré), il faut mettre à jour `sequencage-semaine-3.md` en cohérence (J2 ne peut plus être quick wins + Hn) ou décaler. Si c'est un nouveau cohort / bootcamp 5, repasser la frontmatter `bootcamp:` et déplacer le fichier. Tel quel, ce doc contredit le J2 du séquençage existant : à réconcilier avant distribution Drive.
- **Statut pack des deux skills.** `seo-cannibalisation` = pack des 9 (#3), donc re-bundle/vérification, pas nouvelle install (présenter comme "vérification" pour ne pas affoler, cf. logique [[skill-maillage-systeme]] §note). `maillage-interne-gsc` = hors pack, vraie nouvelle install (à ne pas confondre avec `maillage-systeme` #4, passe structurelle). Message week-end dédié sinon ça bloque au J2.
- **Normalisations appliquées au verbatim canonique** (les fichiers `~/.claude/skills/.../SKILL.md` ne sont PAS modifiés) : (1) em-dashes retirés des deux blocs (règle maison contenu Organikk) ; (2) "méthode Boussardon" → "méthode Organikk" dans la description de `maillage-interne-gsc` (rebrand) ; (3) section "Sauvegarde" : chemin vault `wiki/maillage/` + référence "hook §7 AGENTS.md" remplacés par `audit/` (convention bootcamp, le vault n'existe pas chez les participants). Si tu régénères ce fichier depuis le canonique, re-appliquer ces 3 passes. Mieux : si tu veux, je nettoie aussi les SKILL.md canoniques (em-dash + rebrand) pour ne plus avoir à le refaire.
- **Ajouts pédagogiques hors canonique** : section "Croisement obligatoire avec l'audit Hn" (cannibalisation) et "Reprise des conflits du skill cannibalisation" (maillage) ne sont pas dans les SKILL.md sources. Ils matérialisent le chaînage J2. Si tu valides, on peut les remonter dans les skills canoniques pour rendre le handoff natif (sinon ils ne valent que dans le contexte de ce bundle).
- **Cas pratique** = artisan plombier (aligné persona Cécile / anti-ChatGPT, cf. [[session-3-audit-prep]]). Pages et slugs inventés mais réalistes, à remplacer par un vrai cas au call si tu veux la démo live.
