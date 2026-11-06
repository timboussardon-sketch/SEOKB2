---
type: methode
title: "Format du rapport d'audit SEO : consultant qui priorise, pas crawler qui récite"
slug: rapport-audit-seo-format
created: 2026-09-23
status: stable
confidence: high
sources: 1
tags: [audit, rapport, methode, organikk]
---

# Format du rapport d'audit SEO

Brief du 23 septembre 2026, verbatim. Remplace le « doc final résumé + score » du 22 septembre. S'applique à `audit-complet-v2/workflow-audit.md` Phases 6 et 7, au workflow mots-clés, et à la sortie de chaque skill d'audit.

Le problème actuel n'est pas la collecte de données. La collecte est plutôt bonne. Le problème est la transformation de ces données en rapport. Aujourd'hui, le rapport ressemble trop à un dump d'audit technique : beaucoup de chiffres, énormément de tableaux, des informations répétées et parfois des recommandations trop automatiques. L'objectif est de transformer le système en **consultant SEO qui analyse et priorise**, pas en crawler qui récite ce qu'il trouve.

## 1. Objectif du rapport

Le rapport ne cherche plus à montrer tout ce qui a été analysé. Il répond à quatre questions : que se passe-t-il réellement sur le site ? qu'est-ce qui bloque le plus la progression SEO ? qu'est-ce qu'on doit faire en premier ? pourquoi cette action est prioritaire ? Tout ce qui ne contribue pas à ces quatre réponses va en partie secondaire ou en annexe.

## 2. Plus de score global sur 10, plus de note par phase

Trois niveaux seulement : **Critique**, **À améliorer**, **Sain**. Le niveau se calcule selon l'impact SEO réel, pas selon le nombre d'erreurs.

| Zone | État | Pourquoi |
|---|---|---|
| Architecture | Critique | Les nouvelles pages business sont trop isolées |
| Indexation | À améliorer | Anciennes URL encore présentes dans Google |
| Performance | À améliorer | Quelques pages stratégiques ont un LCP très élevé |
| Structure Hn | Sain | Quelques anomalies mais faible impact global |

## 3. Executive summary en un écran

`# Audit SEO — [domaine]`, période analysée, puis `## Diagnostic principal` : une phrase ou un petit paragraphe qui explique le problème global du site. Le système cherche **une cause structurante**, pas une liste d'erreurs.

## 4. Trois à cinq chiffres clés

Pas 15 métriques. Le moteur sélectionne les chiffres qui illustrent le diagnostic principal ; pas forcément les mêmes d'un site à l'autre.

## 5. Maximum 3 problèmes majeurs

Pour chaque problème : Problème (description simple), Preuve (2 à 4 données maximum), Pourquoi c'est important (impact SEO/business), Action, Confiance (forte / moyenne / faible).

## 6 et 7. Un problème existe une seule fois

Système d'ID de problème (`ISSUE_INTERNAL_LINKING_BUSINESS`, `ISSUE_LEGACY_404`, `ISSUE_HOME_VISIBILITY_DROP`, `ISSUE_CWV_HOME`). Les sections y font référence sans réécrire le diagnostic. Deux observations qui parlent du même problème fusionnent : quatre pages orphelines = un problème « pages commerciales insuffisamment intégrées au maillage », les URL en preuves.

## 8 et 9. Faits, hypothèses, recommandations, confiance

Chaque information est typée : FACT (donnée observée), HYPOTHESIS (interprétation), ACTION (recommandation). Jamais une hypothèse présentée comme un fait. Chaque diagnostic porte `confidence = high | medium | low` : high = plusieurs sources concordent (crawl, GSC, HTML, Lighthouse) ; medium = signal incomplet ; low = peu de données. Les recommandations lourdes exigent une confiance élevée.

## 10. Recommandations automatiques interdites

Jamais automatiquement : fusion de pages parce que deux pages se ressemblent ; 301 parce qu'une URL est 404 ; suppression parce que peu de trafic ; réécriture complète parce que CTR = 0 ; création de page parce qu'un mot-clé n'a pas de page.

## 11. Règle 404

Pour chaque URL en 404 : impressions GSC, clics, requêtes historiques, ancienne intention, destination potentielle, similarité d'intention, backlinks si disponibles. Puis : 301 seulement si une page équivalente existe réellement ; 410 ou 404 conservée si aucun contenu équivalent et plus de raison d'exister ; restaurer si la page répond encore à une intention intéressante ; à vérifier manuellement si les données manquent. Interdit : `/blog/* → /guides/` ou `/outils/* → /audit/` parce que les dossiers semblent proches.

## 12. Cannibalisation

Cinq signaux : même requête GSC sur plusieurs URL ; intentions SERP similaires ; contenu et proposition similaires ; alternance des URL dans Google ; même objectif business. Trois états : **cannibalisation confirmée** (GSC + intention concordante), **chevauchement potentiel** (contenu similaire, pas assez de données), **pages proches mais différenciables**. Fusion recommandée seulement pour confirmée + destination claire. Sinon : vérifier, repositionner, différencier.

## 13 et 14. Quick wins et CTR

Plus jamais « position 4-12 + CTR faible = title à réécrire ». Analyser requêtes réelles, intention, brand / non-brand, type de SERP, impressions, features SERP, cohérence title/requête. Seuils d'impressions (configurables) : < 20 données insuffisantes ; 20 à 100 signal faible ; 100 à 500 exploitable ; 500+ solide. Le benchmark CTR est indicatif : écrire « CTR inférieur au benchmark indicatif », jamais « il manque exactement 13 points ».

## 15. Hiérarchie des données

Niveau 1, comportement Google réel (clics, impressions, positions, requêtes, pages, évolution). Niveau 2, architecture (liens internes, profondeur, orphelines, redirects, sitemap, canonicals). Niveau 3, contenu (H1, Hn, intentions). Niveau 4, technique secondaire (CSS inutilisé, lastmod, Hn mineurs). Le rapport priorise 1 et 2.

## 16, 17, 18, 19. Type de page, poids business, priorité

Classification : homepage, money_page, service_page, pricing, case_study, category, guide, blog, tool, legal, contact, about, utility. `business_weight` de 0 à 1 (homepage 1, service 1, pricing 1, case study 0,8, guide 0,5, blog 0,3, legal 0,05), configurable. Score interne, jamais affiché au client : `priority_score = impact × confidence × business_weight × data_strength ÷ effort` (impact 1 à 5, confidence high 1 / medium 0,7 / low 0,4, effort 1 à 5). Traduit en P1, P2, P3. **Maximum 3 actions P1.**

## 20, 21, 22. Plan 30 jours, format d'action, effort

`# Plan des 30 prochains jours` : Maintenant (3 actions max), Ensuite (3 à 5), À surveiller (signaux à mesurer). Chaque action : ACTION, WHY, EVIDENCE, EXPECTED SIGNAL, EFFORT, CONFIDENCE. Jamais de promesse chiffrée (« +30 % de trafic ») : un signal attendu, pas un résultat garanti. Effort en faible / moyen / élevé, jamais en heures sauf règle configurée.

## 23, 24, 25. Hn, performance, labo contre terrain

Hn : une phrase (« 13 pages présentent une anomalie, X concernent des pages stratégiques »), les pages importantes seulement, le détail en annexe. Performance : une phrase globale puis un tableau Page / LCP / Importance ; ce qui compte est performance × importance de la page. Lighthouse n'est pas les Core Web Vitals terrain : écrire « performance Lighthouse mobile », jamais « le site ne passe pas les Core Web Vitals » sans CrUX. INP non disponible = « non mesuré » ; TBT présenté comme proxy technique uniquement.

## 26, 27. Ce que les données ne permettent pas de conclure, à vérifier avant action

Section obligatoire : requêtes anonymisées, URL non inspectées, absence de CrUX, backlinks non analysés, conversions non disponibles. Et pour toute action irréversible, la checklist à vérifier avant (requêtes, conversions, backlinks, intention, historique, rôle commercial).

## 28, 29, 30, 31, 32, 33, 34. Problème contre opportunité, tendance, migration, clusters, root cause, âge, volume

Problème = dégrade probablement les performances ; opportunité = pourrait être amélioré. Tendance : 28 jours contre 28 précédents, 90 contre 90, par page stratégique, états growing / stable / declining / new / insufficient_data ; les fortes baisses en premier. Beaucoup d'URL qui disparaissent, redirigent ou apparaissent = migration probable, un seul problème global « transition d'architecture encore imparfaitement digérée », pas une anomalie par ancienne URL. Clusters : LEGACY_SITE, INTERNAL_ARCHITECTURE, PERFORMANCE, CONTENT_OVERLAP ; le diagnostic se génère depuis les clusters. Root cause : symptôme → cause possible → preuve → action. `page_age` (< 30 jours, 30 à 90, > 90) : une page récente sans impressions n'est pas un échec. `data_strength` : faible < 20 impressions, moyen 20 à 100, bon 100 à 500, fort 500+.

## 35, 36, 37, 38, 39. Tableaux et interface

Tableaux fournis en données structurées (`columns`, `rows`), jamais générés en Markdown par le LLM ; 5 colonnes maximum. Progressive disclosure : « Voir les données », « Voir les URL concernées », « Voir l'analyse complète », « Voir les données Lighthouse », « Voir toutes les redirections ». Architecture : HEADER, Diagnostic principal, 4 KPI, 3 priorités, Plan 30 jours, Opportunités, À surveiller, puis Analyse détaillée (Indexation, Architecture, Contenu, Performance, Maillage, Cannibalisation), puis Annexes. Navigation sticky.

## 40, 41, 42. Langue

Phrases courtes, pas de répétition, pas de « il est important de », une donnée par diagnostic. Interdit : « Google ne comprend plus le site ». Correct : « Google continue à afficher plusieurs anciennes URL et la home apparaît sur des requêtes peu cohérentes avec l'offre actuelle. » Jamais anthropomorphiser Google : « les signaux observés indiquent », « les données GSC montrent ».

## 43, 44, 45, 46, 47, 48, 49, 50, 51. Risque, validation, pourquoi maintenant, création de page, potentiel, opportunités, labels, ne rien faire, faux problèmes

`risk_level` : low (title, maillage, navigation, Hn), medium (gros changement de contenu, canonical), high (suppression, 301, fusion, changement massif d'URL). Toute action high : « À valider avant déploiement » + checklist. Chaque P1 porte `why_now`. Avant de créer une page : chercher URL existante, intention proche, ancienne URL, contenu réutilisable ; sorties CREATE / EXPAND_EXISTING / REPOSITION / MERGE / NO_ACTION. Opportunités : 5 maximum, chacune avec `potential = high / medium / low`, « pourquoi elle mérite d'être travaillée », « avant modification », « action probable ». Labels : CRITIQUE, OPPORTUNITÉ, À SURVEILLER, DONNÉES INSUFFISANTES, À VALIDER ; très peu de couleurs. Le système sait dire « ne rien faire » et « données insuffisantes ». Faux problèmes : `low_traffic != problem`, `orphan != automatically critical`, le type de page compte.

## 52, 53. Prompt et passes

Le prompt commence par : « Tu es un consultant SEO senior chargé de transformer des données techniques en décisions. Ton rôle n'est pas de restituer toutes les anomalies. Tu dois identifier les quelques phénomènes qui expliquent le mieux les performances du site. » Puis : une anomalie n'est pas une priorité par défaut ; une corrélation n'est pas une causalité ; jamais d'action irréversible sans preuves suffisantes ; jamais le même problème dans plusieurs sections ; « données insuffisantes » écrit explicitement ; pages business et tendances GSC avant les anomalies techniques secondaires.

Sept passes, jamais « fais-moi un rapport » avec toutes les données : 1 normalisation (objets structurés), 2 détection de signaux (observations atomiques), 3 clustering, 4 root cause, 5 priorisation, 6 vérification (contradictions, manque de données), 7 rédaction, seulement à la fin.

## 54, 55, 56. Objets

```json
{"id":"obs_001","type":"internal_linking","url":"/consultant-geo/","fact":"0 internal incoming links","source":"crawl","business_weight":1,"confidence":1}
{"id":"issue_business_pages_underlinked","title":"Pages commerciales insuffisamment intégrées","category":"internal_architecture","severity":"critical","confidence":"high","impact":5,"effort":2,"risk":"low","evidence":["obs_001","obs_002","obs_003"],"recommended_actions":[]}
{"title":"Ajouter des liens vers les pages commerciales","priority":"P1","effort":"low","risk":"low","confidence":"high","why":"...","expected_signal":"...","dependencies":[]}
```

## 57, 58, 59, 60. Validator, quality gate, reviewer, langue

Validator avant génération : indexed + rapport dit non indexée → ERROR ; redirect analysée comme page 200 → ERROR ; peu d'impressions + conclusion forte → WARNING ; 301 sans analyse de destination → WARNING ; fusion sans recouvrement de requêtes → WARNING. Quality gate, le rapport ne sort pas si : aucun diagnostic principal ; plus de 5 P1 ; 301 sans destination ; fusion sans justification ; chiffre sans source ; contradiction importante ; même problème répété ; action sans preuve. Passe critique par une seconde IA : « Tu es reviewer SEO. Cherche uniquement les erreurs de raisonnement du rapport suivant » (causalité abusive, surinterprétation, recommandation risquée, contradiction, données insuffisantes, répétitions, priorité incohérente), corriger avant affichage. Filtre de langue : « Il est important de », « Il convient de », « Cela peut potentiellement », « Il est intéressant de noter », « Dans le cadre de ».

## 61, 62, 63. Deux niveaux, format final

Données brutes exportables (CSV, 404, URL, maillage), jamais dans le rapport principal. Vue dirigeant (diagnostic, KPI, priorités, plan) et vue consultant (toutes les données), switch Synthèse / Détails techniques. Format final : synthèse 1 écran, 3 problèmes, 5 à 8 actions maximum, 3 à 5 opportunités, analyses détaillées repliables, annexes. Pas un mur de 250 lignes.

## 64. Exemple du début de rapport attendu

> # Audit SEO Organikk
> **90 jours analysés**
> ## Le diagnostic
> Le principal enjeu actuel semble être la transition entre l'ancienne architecture du site et le nouveau positionnement commercial. Google continue à conserver plusieurs signaux associés aux anciennes URL tandis que certaines nouvelles pages commerciales restent peu connectées au reste du site. Avant de produire davantage de contenu, la priorité est donc de clarifier l'architecture existante.
> ### Les chiffres à retenir
> **23** anciennes URL en 404 encore observées dans les données Search Console · **9** pages sans lien interne entrant · **5,2 → 32,8** évolution de la position moyenne de la home entre les deux périodes analysées · **4** pages commerciales particulièrement sous-liées
> # Priorité 1 — Stabiliser les anciennes URL
> Analyser les anciennes URL ayant encore des impressions et décider individuellement : redirection, restauration, suppression définitive. À ne pas faire : rediriger automatiquement tout `/blog/` vers `/guides/`.
> # Priorité 2 — Reconnecter les pages commerciales
> Revoir navigation, home, pages mères, footer si pertinent.
> # Priorité 3 — Diagnostiquer la baisse de la home
> Facteurs possibles : changement d'architecture, anciennes redirections, modification du contenu, changement des requêtes associées, performance. Isoler la cause avant toute nouvelle refonte.
> # Plan des 30 prochains jours
> P1 nettoyer les anciennes URL encore visibles · P1 refaire le maillage des pages business · P1 corriger la navigation principale · P2 analyser la baisse de la home · P2 améliorer les performances des pages commerciales lentes · P2 vérifier les chevauchements entre les offres avant toute fusion.

## Principe général

Moins d'informations, mais de meilleures décisions. On doit pouvoir ouvrir le rapport et comprendre en moins de 30 secondes ce qui se passe, pourquoi, et ce qu'on fait maintenant. Les données techniques servent de preuve au diagnostic ; elles ne sont plus le rapport. Le point le plus important est le pipeline en plusieurs passes + objets structurés + quality gate : corriger seulement le prompt ou le design donne un rapport plus joli mais toujours aussi mauvais dans son raisonnement.

---

# Corrections V2, 23 septembre 2026 (brief du verbatim condensé)

La logique est meilleure ; il faut maintenant **simplifier drastiquement la restitution** : peu d'informations visibles, beaucoup de raisonnement derrière. Le client voit le résultat de l'intelligence, pas l'intelligence.

1. **Aucun ID technique dans le rapport** (`ISSUE_...` reste en backend). Le client lit « Pages commerciales trop isolées ».
2. **Jamais low / medium / high** : Faible, Moyen, Élevé, partout.
3. **Diagnostic court** : une conclusion en gras (« Le site est encore entre deux architectures. »), deux lignes de démonstration, une priorité en gras. Distinguer conclusion et démonstration.
4. **Pas de conclusion plus catégorique que la couverture des données.** Pas « l'enjeu n'est pas le contenu » quand le contenu n'a pas été analysé : « les données disponibles font surtout ressortir un problème d'architecture ». Pas « Indexation : Sain » avec 12 URL inspectées sur 141 : « aucun problème majeur détecté sur les URL inspectées ».
5. **Formulations précises** : « 23 URL aujourd'hui en 404 ont encore généré des impressions dans Search Console », pas « Google sert des 404 ».
6. et 7. **KPI = chiffre, label, évolution éventuelle**, jamais un paragraphe ; 4 KPI maximum ; badge « En reprise » possible, le contexte dans le détail.
8. **« État par zone » sort de la synthèse** (il réintroduit les scores). Il vit dans l'analyse technique.
9. et 10. **Priorités visuelles** : titre, une phrase en gras (40 mots max), les URL en preuve, « À faire » en une ligne, `Impact · Effort · Confiance`, bouton « Voir le détail ». Le « pourquoi c'est important » tient en une phrase ; les nombres de liens vont dans « Voir les preuves ».
11. **Confiance forte** en badge ; les sources concordantes au survol ou dans le détail, jamais dans la phrase.
12. et 13. **Plan 30 jours = tableau Priorité / Action / Effort**, 5 à 6 lignes, rien d'autre ; cliquer ouvre le diagnostic. Aucune répétition des priorités. « Pourquoi maintenant » seulement si ce n'est pas évident.
14. et 15. **3 opportunités maximum**, « voir les autres » pour le reste. Le potentiel intègre impressions × intention business × position × tendance × importance de la page × possibilité réelle de progression ; intention inconnue = « potentiel à confirmer », jamais « élevé » sur 78 impressions.
16. et 17. et 18. **Aucune action avant vérification** quand l'intention n'est pas connue (/avis/ : « identifier les requêtes avant toute modification »). **Le nombre de mots seul n'est jamais un problème** (`LOW_WORD_COUNT alone => NO ISSUE`) ; il devient une preuve seulement avec une intention informationnelle non satisfaite, un contenu manifestement incomplet, une mauvaise performance ou une SERP qui demande plus. Une page courte avec 29 % de CTR fonctionne.
19. et 20. **Performance en synthèse** : « la majorité du site est correcte en Lighthouse, deux pages stratégiques ressortent nettement : home 6,8 s, consultant GEO 10,2 s ». Le thread principal, le JS inutilisé, le TBT vont dans « Voir le diagnostic performance ».
21. **Tableaux en données structurées** (colonnes + lignes), jamais une chaîne Markdown produite par le modèle ; le rendu fait le tableau. Headers concaténés = bug bloquant.
22. et 23. **Deux onglets : Synthèse / Analyse technique.** La synthèse tient en exactement 5 sections : Diagnostic (3 à 5 lignes), Chiffres clés (4), Priorités (3 cartes), Plan 30 jours (5 à 6 actions), Opportunités (3). Puis « Voir l'analyse technique ». La synthèse se lit sans descendre dans les données.
24. **Limites** en synthèse : une ligne « Fiabilité de l'analyse : bonne » + une phrase, puis « Voir les limites ».
25. **« À vérifier avant action » attaché à l'action** (badge `Validation requise`, la checklist au clic), pas une section.
26. **Pas de jargon en synthèse** : Submitted and indexed, TBT proxy, thread principal, canonical incohérente, query overlap, sources concordantes. Disponible dans la vue expert.
27. Hiérarchie visuelle : titre du site, période, diagnostic en H2, 4 chiffres, 3 priorités numérotées 01 02 03 avec `Impact · Effort · Validation requise`, plan, 3 opportunités avec « Prochaine étape », bouton « Voir toute l'analyse technique ».
28. Principe : peu d'informations visibles, beaucoup de raisonnement derrière.
29. **Limites strictes** : diagnostic 70 mots max ; 4 KPI ; 3 problèmes ; résumé d'un problème 40 mots ; 6 actions ; 3 opportunités ; description d'opportunité 35 mots. Le surplus va dans les détails.
30. Le rapport principal se comprend en 60 secondes ; l'analyse technique occupe un consultant 20 minutes.

---

# Référence de rédaction pour l'analyse technique (23 septembre 2026)

Le texte de référence pour la partie « priorités en détail, plan 30 jours, pages à surveiller » de l'onglet Analyse technique est celui validé par l'expert de l'utilisateur sur l'audit organikk.co : [[audit/2026-09-22-organikk-co]], sections « Priorité 01 » à « Autres pages à surveiller ». Structure d'une priorité : une phrase de cadrage, « Ce qu'on observe » (listes de faits chiffrés, les pages en code), « Pourquoi c'est prioritaire » (deux phrases), « Action » (liste numérotée courte), « Impact attendu » et « Risque » en gras. Plan : « Priorité immédiate », « Deuxième étape », « Priorité secondaire », une action par paragraphe en gras suivie d'une phrase. Pages à surveiller : chiffres séparés par « · », une phrase, verdict en gras (« Aucune action recommandée », « À vérifier avant toute modification »). Listes à puces autorisées ici : ce sont des faits mesurés, pas de la prose.
