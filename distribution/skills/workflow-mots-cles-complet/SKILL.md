---
name: workflow-mots-cles-complet
description: "Workflow mots-clés en 14 étapes jusqu'au rapport de pré-décision. « workflow mots-clés complet », « les 14 étapes »."
---

# Skill — Workflow mots-clés complet (14 étapes)

## Quand utiliser ce skill

Lance le workflow mots-clés complet du vault, de bout en bout : les 14 étapes de `.seokb/base/wiki/methodes/workflow-mots-cles-complet.md` (version du 24 septembre 2026), dans l'ordre, chacune branchée sur son skill, chacune écrivant son fichier dans le wiki avec son `statut_decision`, jusqu'au rapport de pré-décision, seule sortie visible. Ce skill est un routeur : la méthode est dans le fichier du vault et dans `.seokb/base/wiki/methodes/rapport-mots-cles-format.md`, il oblige à les ouvrir et à ne sauter aucune étape. Il ajoute ce que le fichier ne fait pas : le skill de l'étape 6, le fichier de logs, le contrôle mécanique du rapport (`controle-rapport.py`) et la vérification finale.

TOUJOURS utiliser ce skill quand l'utilisateur dit : "workflow mots-clés complet", "lance le workflow mots-clés", "lance tout le workflow", "fais tout le workflow mots-clés", "les 14 étapes", "rapport de pré-décision mots-clés", "recherche de mots-clés de A à Z", "workflow keyword complet", ou donne un site client en demandant la recherche de mots-clés complète avec pré-décision par page.

NE PAS utiliser pour une seule étape : liste de mots-clés seule → seo-recherche-mots-cles ; clustering seul → seo-clustering-mots-cles ; brief d'une page déjà validée → seo-brief-contenu ; mots-clés business d'un audit → seo-top20-mots-cles-business. `kw-research-workflow` n'est que l'étape 1 de ce workflow.

## Avant la première étape

1. Ouvrir et lire en entier, dans cette session :
   - `.seokb/base/wiki/methodes/workflow-mots-cles-complet.md` (les 14 étapes, la quality gate) ;
   - `.seokb/base/wiki/methodes/rapport-mots-cles-format.md` (le format du rapport) ;
   - la référence exécutée, si ton coffre la contient (le coffre seo-kb d'Organikk l'a) : `wiki/keywords/2026-09-23-organikk-rapport-decision.md`, ses logs `2026-09-23-organikk-workflow-complet.md` et l'annexe `wiki/keywords/annexes/decisions-2026-09-24-organikk.json`. Sinon, les gabarits de ce skill suffisent.
   Si le fichier du vault a changé de version, il prime sur ce skill.
2. Cadrer avec l'utilisateur, en une seule question groupée, ce qui manque parmi : site, offre et point de conversion (appel, devis, achat), marché ou ville, vault du client (chemin), données disponibles (Keyword Planner, Search Console, transcripts). Ne pas redemander ce que le vault du client dit déjà.
3. Fixer le `slug` (`<client>` ou `<client>-<marché>`) et la date du jour `YYYY-MM-DD`. Tous les fichiers de la passe portent ce slug et cette date.

Où écrire : dans le vault du client s'il en a un (`wiki/keywords/`, `wiki/queries/`, `wiki/clusters/`, `wiki/briefs/`), sinon dans `wiki/` aux mêmes chemins. Un seul des deux par passe.

## Les 14 étapes

Une étape = invoquer le skill nommé avec l'outil Skill, appliquer ses règles, écrire sa sortie au chemin indiqué. Chaque fichier commence par un frontmatter avec `statut_decision`, `rapport:` (lien vers le futur rapport) et la ligne d'avertissement de la référence :

> **Statut : HYPOTHÈSE.** Sortie amont du workflow mots-clés. La pré-décision finale est dans [[keywords/YYYY-MM-DD-slug-rapport-decision]] ; ce fichier ne peut pas la contredire.

| # | Skill à invoquer | Sortie | Statut |
|---|---|---|---|
| 1 | `kw-research-workflow` | `queries/kw-research-YYYY-MM-DD-slug.md` + CSV dans `keywords/annexes/` | RAW |
| 2 | `seo-quick-win` (+ content gaps Search Console) | `keywords/YYYY-MM-DD-slug-search-console.md` | RAW |
| 3 | `seo-mots-cles-overview` | `keywords/YYYY-MM-DD-slug-overview.md` | HYPOTHÈSE |
| 4 | `seo-recherche-mots-cles` | `keywords/recherche-YYYY-MM-DD-slug.md` | HYPOTHÈSE |
| 5 | `seo-mots-cles-resistants-ia` | `keywords/YYYY-MM-DD-slug-resistants-ia.md` | HYPOTHÈSE |
| 6 | filtre des 4 piliers (voir plus bas), avec `seo-top20-mots-cles-business` si la Search Console est disponible | `keywords/YYYY-MM-DD-slug-mots-cles-business.md` | HYPOTHÈSE |
| 7 | `seo-clustering-mots-cles` | `keywords/clusters-YYYY-MM-DD-slug.md` | HYPOTHÈSE |
| 8 | `seo-mots-cles-decisionnels` | `keywords/decisionnels-YYYY-MM-DD-slug.md` | HYPOTHÈSE |
| 9 | `seo-cluster-aeo` | `clusters/YYYY-MM-DD-slug.md` | HYPOTHÈSE, BLOQUÉ si le pilier l'est |
| 10 | `seo-modeles-pseo` puis `seo-programmatique-pseo` | `queries/pseo-YYYY-MM-DD-slug.md` | HYPOTHÈSE |
| 11 | `seo-peurs-objections` | `queries/peurs-YYYY-MM-DD-slug.md` | VALIDÉ si verbatims réels |
| 12 | `seo-entites-vectorielles` | `queries/entites-YYYY-MM-DD-slug.md` | HYPOTHÈSE |
| 13 | `seo-brief-contenu` | `briefs/YYYY-MM-DD-slug.md` | VALIDÉ seulement si la pré-décision URL du cluster est VALIDÉ, sinon fichier marqué BLOQUÉ sans plan Hn |
| 14 | rapport de pré-décision (ce skill) | `keywords/YYYY-MM-DD-slug-rapport-decision.md` + `keywords/annexes/decisions-YYYY-MM-DD-slug.json` + `keywords/annexes/scores-YYYY-MM-DD-slug.json` | PRÉ-DÉCISION FINALE |

Plus le fichier de logs `keywords/YYYY-MM-DD-slug-workflow-complet.md` : le tableau des 13 sorties amont avec leur statut, mis à jour à chaque étape. Gabarit : `2026-09-23-organikk-workflow-complet.md`.

### Enchaînement

- Les étapes tournent dans l'ordre. Chacune lit les sorties des précédentes, jamais leur résumé de mémoire.
- Une étape sans donnée (pas de Search Console, pas de transcript) n'est pas sautée : son fichier est écrit avec `statut_decision: BLOQUÉ` et la donnée qui manque. Le rapport le dit.
- Aucun volume estimé, nulle part. Un volume vient d'un export Keyword Planner ou de la Search Console, avec son fichier source cité ; sinon « non mesuré ».
- Étape 13 : un brief par cluster prioritaire dont la pré-décision provisoire est VALIDÉ. Les autres clusters prioritaires ont un fichier BLOQUÉ qui dit par quoi.
- Quand le rapport tranche, revenir sur les sorties amont qu'il contredit et passer leur `statut_decision` à OBSOLÈTE (ou noter « (top 5 obsolète) » dans les logs pour une partie seulement), comme dans la référence.

### Étape 6 : le filtre des 4 piliers

Le fichier du vault ne nomme pas de skill pour cette étape. Méthode de la session 1 du bootcamp, telle qu'appliquée dans `2026-09-23-organikk-mots-cles-business.md` : chaque requête candidate (issue des étapes 1 à 5) passe les quatre piliers pour entrer dans la roadmap.

| Pilier | Question |
|---|---|
| Surprise Gap | ChatGPT peut-il répondre à la place de la page, et peut-on faire mieux que lui ? |
| Grounding | Le vault a-t-il la matière propriétaire (documents par type, verbatims, cas) ? |
| pSEO | La requête se décline-t-elle en template + variable ? |
| AEO | Intention Do, Know ou Know-Simple ? |

Sortie : un tableau Requête candidate / 4 piliers / Verdict (Retenu n°X, En attente : raison, Écarté : raison), 3 à 5 retenues. Ordre d'attaque : décisionnel, actionnel, transactionnel, informationnel en dernier. Avec une Search Console, `seo-top20-mots-cles-business` fournit les intentions déjà captées et les pages qui sous-performent avant le filtre.

## Étape 14 : le rapport

Suivre `rapport-mots-cles-format.md` à la lettre. Ordre visible : Synthèse (diagnostic en trois lignes, pré-décision par marché, ce qui est bloqué et par quoi, à ne pas produire maintenant, fiabilité), puis Analyse technique. Les logs restent dans leur fichier, jamais dans le rapport.

L'annexe `decisions-*.json` porte un objet par cluster, avec ces clés au minimum : `cluster`, `url`, `matiere`, `serp`, `statut` (VALIDÉ, À VÉRIFIER, BLOQUÉ, REJETÉ), `reason`, `allowed_actions`, `forbidden_actions`. Aucune création de page ne passe VALIDÉ sans SERP lue. Une page existante à renforcer peut être VALIDÉ avec une SERP à vérifier (cas « Prix » de la référence) : `reason` est alors facultative, et `allowed_actions` / `forbidden_actions` le sont pour un cluster REJETÉ.

Rédaction : `ton-de-voix` et `redaction-anti-ia` s'appliquent à la synthèse. Pas d'identifiant technique ni de mot anglais dans la synthèse.

## Contrôles avant de rendre

1. Contrôle mécanique du rapport et de ses annexes :

   ```
   python3 <dossier de ce skill>/controle-rapport.py <rapport.md>
   ```

   Le script est livré avec ce skill. S'il manque dans le dossier du skill, le recréer à partir de la section « Annexe : controle-rapport.py » en bas de ce fichier.

   Il sort 1 sur un BLOQUANT : section obligatoire absente, « à trancher », annexe `decisions` manquante ou illisible, cluster sans statut, raison ou actions, statut hors liste, brief VALIDÉ sur un cluster non VALIDÉ, sortie amont absente des logs. Il liste les À LIRE (« cannibalisation », « occurrence », « placer en title/H2/FAQ ») : un grep ne sait pas si la phrase les nie ou les affirme, la lecture tranche.
2. `node <dossier des skills>/redaction-anti-ia/slop.mjs <rapport.md>` (le script du skill `redaction-anti-ia`).
3. Commit dans le repo du vault, avec les 13 sorties, les logs et les annexes.
4. Tâche profonde : lancer le vérificateur de livrable (agent `verificateur-livrable`, ou skill `verification-livrable`) avec ses 6 sections : DEMANDE UTILISATEUR, TYPE DE TÂCHE, SKILLS UTILISÉS, LIVRABLES À VÉRIFIER, SOURCES ET DONNÉES UTILISÉES, CONTRAINTES PARTICULIÈRES. Livrables : le rapport, les deux annexes JSON, les logs et chacune des 13 sorties amont (chemins absolus). Skills utilisés : ce skill et les 14 skills invoqués, avec leurs chemins. Corriger, relancer jusqu'à 0 ❌, recopier le dernier tableau dans la réponse finale.

## Réponse à l'utilisateur

Le diagnostic en trois lignes, le tableau de pré-décision par marché, ce qui attend sa décision (positionnement) et ce qui attend une lecture de SERP, puis le tableau du vérificateur. Pas le détail des 13 étapes : il est dans les logs.

## Annexe : controle-rapport.py

Copie exacte du script livré avec ce skill. À écrire dans le dossier du skill s'il manque.

```python
#!/usr/bin/env python3
"""Contrôle mécanique du rapport de pré-décision du workflow mots-clés complet.

Usage : python3 controle-rapport.py <wiki>/keywords/YYYY-MM-DD-slug-rapport-decision.md

Lit le frontmatter du rapport (decisions:, logs:), l'annexe decisions-*.json, le fichier
de logs et les briefs qu'il cite. Sort 1 sur un BLOQUANT, 0 sinon. Les À LIRE ne
bloquent pas : un grep ne sait pas si la phrase nie ou affirme, la lecture tranche.
"""
import json, os, re, sys

STATUTS = {'VALIDÉ', 'À VÉRIFIER', 'BLOQUÉ', 'REJETÉ'}
CLES = ['cluster', 'url', 'matiere', 'serp', 'statut', 'reason', 'allowed_actions', 'forbidden_actions']
SECTIONS = [
    (r'^#+ .*Pré-décision par marché', 'Pré-décision par marché'),
    (r'^#+ .*Ce qui est bloqué', 'Ce qui est bloqué, et par quoi'),
    (r'^#+ .*À ne pas produire', 'À ne pas produire maintenant'),
    (r'Fiabilité', 'Fiabilité de l\'analyse'),
    (r'^# Analyse technique', 'Analyse technique'),
]
A_LIRE = [
    (r'(?i)cannibalis', 'cannibalisation : interdit sans SERP ni conflit GSC'),
    (r'(?i)occurrences?\b', 'matière comptée en occurrences ?'),
    (r'(?i)\bplacer\b[^.\n]{0,60}\b(title|H2|FAQ)\b', 'requête secondaire placée en title / H2 / FAQ ?'),
]

bloquants, a_lire = [], []


def frontmatter(texte):
    m = re.match(r'---\n(.*?)\n---', texte, re.S)
    fm = {}
    if m:
        for ligne in m.group(1).splitlines():
            if ':' in ligne and not ligne.startswith(' '):
                k, v = ligne.split(':', 1)
                fm[k.strip()] = v.strip().strip('"')
    return fm


def cible(lien, wiki):
    m = re.search(r'\[\[([^\]|#]+)', lien or '')
    if not m:
        return None
    p = os.path.join(wiki, m.group(1))
    for essai in (p, p + '.md'):
        if os.path.exists(essai):
            return essai
    return p


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    rapport = os.path.abspath(sys.argv[1])
    wiki = os.path.dirname(os.path.dirname(rapport))
    texte = open(rapport, encoding='utf-8').read()
    fm = frontmatter(texte)
    corps = texte[texte.find('\n---', 3) + 4:] if texte.startswith('---') else texte

    if fm.get('statut_decision') != 'PRÉ-DÉCISION FINALE':
        bloquants.append(f"statut_decision = {fm.get('statut_decision')!r}, attendu 'PRÉ-DÉCISION FINALE'")
    for motif, nom in SECTIONS:
        if not re.search(motif, corps, re.M):
            bloquants.append(f'section absente : {nom}')
    for n, ligne in enumerate(texte.splitlines(), 1):
        if re.search(r'(?i)à trancher', ligne):
            bloquants.append(f'l. {n} : « à trancher » interdit (typer : décision stratégique requise, ou analyse SERP de N requêtes)')
        for motif, quoi in A_LIRE:
            if re.search(motif, ligne):
                a_lire.append(f'l. {n} : {quoi} → {ligne.strip()[:140]}')

    # Annexe decisions
    statuts = {}
    chemin = cible(fm.get('decisions'), wiki)
    if not chemin or not os.path.exists(chemin):
        bloquants.append(f"annexe decisions introuvable (frontmatter decisions: {fm.get('decisions')!r})")
    else:
        try:
            d = json.load(open(chemin, encoding='utf-8'))
            clusters = d['clusters'] if isinstance(d, dict) else d
        except Exception as e:
            bloquants.append(f'annexe decisions illisible : {e}')
            clusters = []
        if not clusters:
            bloquants.append('annexe decisions : aucun cluster')
        for c in clusters:
            nom = c.get('cluster', '?')
            requises = [k for k in CLES
                        if not (k == 'reason' and c.get('statut') == 'VALIDÉ')
                        and not (k in ('allowed_actions', 'forbidden_actions') and c.get('statut') == 'REJETÉ')]
            manque = [k for k in requises if k not in c or c[k] in ('', None)]
            if manque:
                bloquants.append(f'cluster « {nom} » : clés manquantes {manque}')
            if c.get('statut') not in STATUTS:
                bloquants.append(f"cluster « {nom} » : statut {c.get('statut')!r} hors {sorted(STATUTS)}")
            if c.get('statut') == 'VALIDÉ' and re.search(r'(?i)non vérifiée|à vérifier', str(c.get('serp', ''))):
                if re.search(r'(?i)nouvelle|créer|aucune', str(c.get('url', ''))):
                    bloquants.append(f'cluster « {nom} » : création VALIDÉ alors que la SERP est « {c.get("serp")} »')
                else:
                    a_lire.append(f'cluster « {nom} » : VALIDÉ sur une page existante, SERP « {c.get("serp")} » (renforcer, pas créer ?)')
            statuts[nom] = c.get('statut')

    # Logs et briefs
    logs = cible(fm.get('logs'), wiki)
    if not logs or not os.path.exists(logs):
        bloquants.append(f"fichier de logs introuvable (frontmatter logs: {fm.get('logs')!r})")
    else:
        lt = open(logs, encoding='utf-8').read()
        lignes = [l for l in lt.splitlines() if re.match(r'\|\s*\d+\s*\|', l)]
        ordres = {int(re.match(r'\|\s*(\d+)', l).group(1)) for l in lignes}
        absents = sorted(set(range(1, 15)) - ordres)
        if absents:
            bloquants.append(f'logs : étapes absentes {absents}')
        for l in lignes:
            if not re.search(r'\[\[', l) and not re.search(r'BLOQUÉ', l):
                a_lire.append(f'logs : étape sans lien vers sa sortie → {l[:120]}')
        valides = {n for n, s in statuts.items() if s == 'VALIDÉ'}
        for lien in re.findall(r'\[\[(briefs/[^\]|#]+)', lt):
            p = cible(f'[[{lien}]]', wiki)
            if p and os.path.exists(p):
                sb = frontmatter(open(p, encoding='utf-8').read()).get('statut_decision')
                if sb == 'VALIDÉ' and not valides:
                    bloquants.append(f'brief {lien} VALIDÉ alors qu\'aucun cluster n\'est VALIDÉ')
            else:
                bloquants.append(f'brief cité dans les logs introuvable : {lien}')

    print(f'Rapport : {rapport}')
    print(f'Clusters : {len(statuts)} ' + ', '.join(f'{n} = {s}' for n, s in statuts.items()))
    for b in bloquants:
        print('BLOQUANT ', b)
    for a in a_lire:
        print('À LIRE   ', a)
    print(f'{len(bloquants)} bloquant(s), {len(a_lire)} à lire')
    sys.exit(1 if bloquants else 0)


if __name__ == '__main__':
    main()
```
