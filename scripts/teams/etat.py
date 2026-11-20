#!/usr/bin/env python3
"""État d'un projet de team (mots-clés) : phases, livrables, accords de l'utilisateur.

  etat.py init <team> <dossier> --nom NOM [--site SITE]
  etat.py status <dossier>
  etat.py suivante <dossier>
  etat.py demarre <dossier> <phase>
  etat.py livre <dossier> <phase> <fichier>...
  etat.py valide <dossier> <phase> --message "accord exact de l'utilisateur"
  etat.py corrige <dossier> <phase> --message "correction exacte de l'utilisateur"
  etat.py sans-objet <dossier> <phase> --message "décision exacte de l'utilisateur"
  etat.py liste

L'état vit dans <dossier>/.team/etat.json. Le registre des projets vit dans
<coffre>/.seokb/teams/registre.json (il porte des noms de clients).
Un accord porte sur l'empreinte exacte des fichiers livrés : un fichier modifié après
sa présentation refuse la validation, il faut le relivrer.
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Installé : <coffre>/.seokb/runtime/teams/etat.py. Dans le dépôt : scripts/teams/etat.py.
ICI = Path(__file__).resolve()
COFFRE = ICI.parents[3] if ICI.parents[2].name == '.seokb' else ICI.parents[2]
SKILLS = COFFRE / '.claude' / 'skills' if (COFFRE / '.claude' / 'skills' / 'team-mots-cles').is_dir() else COFFRE / 'distribution' / 'skills'
REGISTRE = COFFRE / '.seokb' / 'teams' / 'registre.json'
TEAMS = {
    'mots-cles': SKILLS / 'team-mots-cles' / 'phases.json',
}
OK = {'valide', 'sans-objet'}


def maintenant():
    return datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')


def empreinte(fichiers):
    h = hashlib.sha256()
    for f in sorted(str(Path(x).resolve()) for x in fichiers):
        p = Path(f)
        if not p.is_file():
            sys.exit(f'Fichier introuvable : {f}')
        h.update(f.encode())
        h.update(hashlib.sha256(p.read_bytes()).digest())
    return h.hexdigest()


def chemin(dossier):
    return Path(dossier).resolve() / '.team' / 'etat.json'


def lire(dossier):
    c = chemin(dossier)
    if not c.exists():
        sys.exit(f'Aucun projet de team dans {dossier} : lancer init.')
    return json.loads(c.read_text(encoding='utf-8'))


def ecrire(dossier, etat):
    c = chemin(dossier)
    c.parent.mkdir(parents=True, exist_ok=True)
    tmp = c.with_suffix('.tmp')
    tmp.write_text(json.dumps(etat, ensure_ascii=False, indent=2), encoding='utf-8')
    tmp.replace(c)


def phase(etat, pid):
    for p in etat['phases']:
        if p['id'] == pid:
            return p
    sys.exit(f"Phase inconnue : {pid}. Phases : {', '.join(p['id'] for p in etat['phases'])}")


def satisfaite(p):
    return p['statut'] in OK or (p['statut'] == 'livre' and not p['validation'])


def dependantes(etat, pid):
    trouvees, file = [], [pid]
    while file:
        courant = file.pop()
        for p in etat['phases']:
            if courant in p['depend'] and p['id'] not in trouvees:
                trouvees.append(p['id'])
                file.append(p['id'])
    return trouvees


def journal(etat, action, pid, message=''):
    etat['journal'].append({'date': maintenant(), 'action': action, 'phase': pid, 'message': message})


def exiger_message(args):
    if not (args.message or '').strip():
        sys.exit('--message obligatoire : recopier les mots exacts de l’utilisateur.')


def cmd_init(args):
    if args.team not in TEAMS:
        sys.exit(f"Team inconnue : {args.team}. Teams : {', '.join(TEAMS)}")
    if chemin(args.dossier).exists():
        sys.exit(f'Projet déjà présent : {chemin(args.dossier)}. Reprendre avec status.')
    modele = json.loads(TEAMS[args.team].read_text(encoding='utf-8'))
    phases = [dict(p, statut='attente', fichiers=[], empreinte=None) for p in modele['phases']]
    etat = {'team': args.team, 'nom': args.nom, 'site': args.site, 'dossier': str(Path(args.dossier).resolve()),
            'cree': maintenant(), 'phases': phases, 'journal': []}
    journal(etat, 'init', '-', args.nom)
    ecrire(args.dossier, etat)
    REGISTRE.parent.mkdir(parents=True, exist_ok=True)
    registre = json.loads(REGISTRE.read_text(encoding='utf-8')) if REGISTRE.exists() else []
    registre.append({'team': args.team, 'nom': args.nom, 'site': args.site, 'dossier': etat['dossier'], 'cree': etat['cree']})
    REGISTRE.write_text(json.dumps(registre, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Projet {args.team} « {args.nom} » créé : {chemin(args.dossier)}')
    cmd_suivante(args)


def cmd_status(args):
    etat = lire(args.dossier)
    print(f"Team {etat['team']} — {etat['nom']} ({etat.get('site') or 'site non renseigné'})")
    for p in etat['phases']:
        accord = ' [accord de l’utilisateur]' if p['validation'] else ''
        deps = f" ← {', '.join(p['depend'])}" if p['depend'] else ''
        print(f"  {p['statut']:<10} {p['id']:<20} {p['titre']} · {p['role']}{accord}{deps}")
    cmd_suivante(args)


def cmd_suivante(args):
    etat = lire(args.dossier)
    index = {p['id']: p for p in etat['phases']}
    attend_accord = [p for p in etat['phases'] if p['statut'] == 'livre' and p['validation']]
    en_cours = [p for p in etat['phases'] if p['statut'] == 'en-cours']
    pretes = [p for p in etat['phases']
              if p['statut'] in ('attente', 'corriger', 'a-revoir')
              and all(satisfaite(index[d]) for d in p['depend'])]
    if all(satisfaite(p) for p in etat['phases']):
        print('Toutes les phases sont terminées.')
        return
    for p in attend_accord:
        print(f"ATTEND TON ACCORD : {p['id']} — {p['accord']}")
    for p in en_cours:
        print(f"EN COURS : {p['id']} ({p['role']})")
    for p in pretes:
        print(f"PRÊTE : {p['id']} — {p['titre']} · {p['role']}")
    if not (attend_accord or en_cours or pretes):
        print('Aucune phase disponible : vérifier les phases à revoir ou à corriger.')


def cmd_demarre(args):
    etat = lire(args.dossier)
    p = phase(etat, args.phase)
    index = {x['id']: x for x in etat['phases']}
    manque = [d for d in p['depend'] if not satisfaite(index[d])]
    if manque:
        sys.exit(f"{p['id']} attend : {', '.join(manque)}")
    if p['statut'] not in ('attente', 'corriger', 'a-revoir'):
        sys.exit(f"{p['id']} est « {p['statut']} » : rien à démarrer.")
    p['statut'] = 'en-cours'
    journal(etat, 'demarre', p['id'])
    ecrire(args.dossier, etat)
    print(f"{p['id']} en cours ({p['role']}).")


def cmd_livre(args):
    etat = lire(args.dossier)
    p = phase(etat, args.phase)
    if p['statut'] in OK:
        sys.exit(f"{p['id']} est déjà « {p['statut']} ». Une correction de l’utilisateur passe par corrige.")
    p['fichiers'] = [str(Path(f).resolve()) for f in args.fichiers]
    p['empreinte'] = empreinte(p['fichiers'])
    p['statut'] = 'livre'
    journal(etat, 'livre', p['id'], p['empreinte'])
    ecrire(args.dossier, etat)
    if p['validation']:
        print(f"{p['id']} livrée, empreinte {p['empreinte'][:12]}. À montrer à l’utilisateur : {p['accord']}")
    else:
        print(f"{p['id']} livrée, empreinte {p['empreinte'][:12]}.")
    cmd_suivante(args)


def cmd_valide(args):
    exiger_message(args)
    etat = lire(args.dossier)
    p = phase(etat, args.phase)
    if p['statut'] != 'livre':
        sys.exit(f"{p['id']} est « {p['statut']} » : seule une phase livrée se valide.")
    if empreinte(p['fichiers']) != p['empreinte']:
        sys.exit(f"{p['id']} : un fichier a changé depuis la livraison. Relivrer puis remontrer à l’utilisateur.")
    p['statut'] = 'valide'
    p['accord_recu'] = {'date': maintenant(), 'message': args.message, 'empreinte': p['empreinte']}
    journal(etat, 'valide', p['id'], args.message)
    ecrire(args.dossier, etat)
    print(f"{p['id']} validée.")
    cmd_suivante(args)


def cmd_corrige(args):
    exiger_message(args)
    etat = lire(args.dossier)
    p = phase(etat, args.phase)
    p.setdefault('historique', []).append({'date': maintenant(), 'statut': p['statut'], 'empreinte': p['empreinte'], 'correction': args.message})
    p['statut'] = 'corriger'
    p['correction'] = args.message
    revues = []
    for pid in dependantes(etat, p['id']):
        d = phase(etat, pid)
        if d['statut'] in ('livre', 'valide', 'en-cours', 'sans-objet'):
            d['statut'] = 'a-revoir'
            revues.append(pid)
    journal(etat, 'corrige', p['id'], args.message)
    ecrire(args.dossier, etat)
    print(f"{p['id']} à corriger." + (f" À revoir ensuite : {', '.join(revues)}" if revues else ''))


def cmd_sans_objet(args):
    exiger_message(args)
    etat = lire(args.dossier)
    p = phase(etat, args.phase)
    if not p.get('optionnelle'):
        sys.exit(f"{p['id']} n'est pas optionnelle : elle ne peut pas être sautée.")
    p['statut'] = 'sans-objet'
    p['accord_recu'] = {'date': maintenant(), 'message': args.message}
    journal(etat, 'sans-objet', p['id'], args.message)
    # Une phase optionnelle qui ne dépend que de phases sautées est sautée avec elles.
    for pid in dependantes(etat, p['id']):
        d = phase(etat, pid)
        if d.get('optionnelle') and all(phase(etat, x)['statut'] == 'sans-objet' for x in d['depend']):
            d['statut'] = 'sans-objet'
            journal(etat, 'sans-objet', d['id'], f"suit {p['id']}")
    ecrire(args.dossier, etat)
    print(f"{p['id']} sans objet.")
    cmd_suivante(args)


def cmd_liste(args):
    if not REGISTRE.exists():
        print('Aucun projet.')
        return
    for r in json.loads(REGISTRE.read_text(encoding='utf-8')):
        c = Path(r['dossier']) / '.team' / 'etat.json'
        etat = json.loads(c.read_text(encoding='utf-8')) if c.exists() else None
        resume = 'état introuvable' if etat is None else ', '.join(
            f"{p['id']}={p['statut']}" for p in etat['phases'] if p['statut'] not in ('attente',) and not satisfaite(p)) or 'à jour'
        print(f"{r['team']:<10} {r['nom']:<30} {r['dossier']}  [{resume}]")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('init'); s.add_argument('team'); s.add_argument('dossier'); s.add_argument('--nom', required=True); s.add_argument('--site')
    for nom in ('status', 'suivante'):
        s = sub.add_parser(nom); s.add_argument('dossier')
    s = sub.add_parser('demarre'); s.add_argument('dossier'); s.add_argument('phase')
    s = sub.add_parser('livre'); s.add_argument('dossier'); s.add_argument('phase'); s.add_argument('fichiers', nargs='+')
    for nom in ('valide', 'corrige', 'sans-objet'):
        s = sub.add_parser(nom); s.add_argument('dossier'); s.add_argument('phase'); s.add_argument('--message', required=True)
    sub.add_parser('liste')
    args = ap.parse_args()
    {'init': cmd_init, 'status': cmd_status, 'suivante': cmd_suivante, 'demarre': cmd_demarre, 'livre': cmd_livre,
     'valide': cmd_valide, 'corrige': cmd_corrige, 'sans-objet': cmd_sans_objet, 'liste': cmd_liste}[args.cmd](args)


if __name__ == '__main__':
    main()
