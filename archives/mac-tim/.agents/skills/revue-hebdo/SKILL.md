---
name: revue-hebdo
description: |
  Rituel de décision hebdomadaire du système (vendredi). Distinct de la revue de presse, du lint d'hygiène et de l'algorithme-recap-hebdo. Tranche : promotions draft→stable, hypothèse à tester, lot d'ingest, contradiction à fermer, archivage, fil rouge éditorial, correction récurrente à durcir. Produit une édition dans wiki/revue-hebdo/.

  TOUJOURS utiliser ce skill quand l'utilisateur dit : "revue hebdo", "revue de la semaine", "on fait le point", "rituel hebdo", "qu'est-ce qu'on décide cette semaine", ou quand le LaunchAgent com.timboussardon.revue-hebdo se déclenche.
---

# Revue Hebdo — le rendez-vous de décision

Vault : `/Users/timothee/Code/seo-kb/`. Sortie : `wiki/revue-hebdo/YYYY-Www.md`. Ce n'est PAS la revue de presse (`revue-presse-quotidienne`), ni le lint (`audit-vault-hygiene`), ni la synthèse presse (`algorithme-recap-hebdo`). C'est le moment où le système se reprend en main. Voir `wiki/revue-hebdo/index.md`.

## ÉTAPE 1 — COLLECTE DE L'ÉTAT

```bash
cd /Users/timothee/Code/seo-kb
date -u +%G-W%V
grep "^## \[" wiki/log.md | tail -20
git log --since="8 days ago" --pretty='%ad %s' --date=short
```

Lis l'état des registres : `wiki/ingest-backlog.md` (prochain lot proposé par le dernier sweep), `wiki/hypotheses.md` (tableau de bord), `wiki/contradictions.md` (lignes sans mouvement > 60j), `wiki/corrections-recurrentes.md` (thèmes en statut `récurrente`), la dernière note de résurgence du mercredi si présente.

## ÉTAPE 2 — DÉTECTER LES PROMOTIONS

```bash
grep -rl "status: draft" wiki/ --include="*.md" | head -40
grep -rl "status: stable" wiki/concepts wiki/syntheses --include="*.md"
grep "récurrente" wiki/corrections-recurrentes.md
```

Pour chaque `draft` : mûr pour `stable` ? Pour chaque `stable` sur sujet SEO volatil non touché depuis > 12 mois (`updated:`) : candidat `stale` ? Propose, ne force pas : la décision finale est à Tim, tu prépares le terrain avec une reco tranchée.

Pour chaque thème `récurrente` dans `wiki/corrections-recurrentes.md` : rédige une proposition concrète de durcissement (règle de lint dans `.agents/skills/audit-vault-hygiene/SKILL.md`, contrainte dans le skill concerné, ou clause AGENTS.md), sous forme de diff prêt à valider — jamais appliqué sans le feu vert de Tim.

## ÉTAPE 3 — LES 8 DÉCISIONS

Rédige l'édition en traitant chaque point, une reco nette par point (pas de "on pourrait") :

1. Promotions `draft`→`stable` / `stable`→`stale`
2. L'hypothèse à passer `en-test` cette semaine (une seule) + quelle fiche preuve ouvrir
3. Le lot d'ingest de la semaine prochaine (reprendre la reco du dernier sweep backlog)
4. La contradiction à fermer cette semaine
5. Le draft mort / la note périmée à archiver
6. Le concept de résurgence du mercredi : toujours juste, à challenger, à mettre à jour ?
7. Le fil rouge : un sujet revient-il assez pour un pilier, un post, une prise de position ?
8. La correction récurrente à durcir (si `wiki/corrections-recurrentes.md` en signale une cette semaine, sinon le dire explicitement — pas d'invention)

## ÉTAPE 4 — ÉCRIRE L'ÉDITION

`wiki/revue-hebdo/YYYY-Www.md`, frontmatter `type: revue-presse` n'est PAS adapté ; utiliser `type: register`, `status: stable`. Structure : les 8 décisions, chacune avec la reco et l'action concrète (qui/quoi/quand). Anti-AI-writing §11 strict : prose dense, zéro remplissage, chaque ligne porte une décision.

Mets à jour la table "Éditions" de `wiki/revue-hebdo/index.md`.

## ÉTAPE 5 — LOG + RÉSUMÉ

```
## [YYYY-MM-DD] revue-hebdo | Semaine Www — N décisions
- promotions: a draft→stable, b stable→stale
- hypothèse en test: H-XXX
- lot ingest: …
- contradiction fermée: C-XXX
- correction durcie: [thème] → [validée / reportée / aucune récurrente cette semaine]
```

Si Tim valide une proposition de durcissement (point 8), passe la ligne correspondante de `wiki/corrections-recurrentes.md` à `durcie` avec référence au commit. S'il reporte, laisse `récurrente`.

Termine par : `Revue Www : N décisions — hypothèse H-XXX en test — lot ingest : … — fil rouge : … — durcissement : …`

## CONTRAINTES

- Une reco par décision, tranchée. La revue hebdo décide, elle ne liste pas des options.
- Ne jamais empiéter sur le scope hors périmètre (revue de presse quotidienne, lint hygiène) : si un problème d'hygiène apparaît, le mentionner en une ligne et renvoyer vers `audit-vault-hygiene`, ne pas le traiter ici.
- Pas d'invention : si un registre est vide ou un sweep n'a pas tourné, le dire et recommander de le relancer, ne pas combler.
- Point 8 (correction récurrente) : jamais d'écriture automatique dans un skill ou AGENTS.md. La revue hebdo prépare le diff, elle ne l'applique pas — Tim valide explicitement avant tout commit qui modifie une règle du système.
- Anti-AI-writing §11 sur toute la rédaction.
