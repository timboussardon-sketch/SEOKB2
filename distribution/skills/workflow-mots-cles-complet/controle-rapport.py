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
