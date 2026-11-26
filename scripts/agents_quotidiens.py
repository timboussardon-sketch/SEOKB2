#!/usr/bin/env python3
"""Agents quotidiens SEOKB2 : alertes Search Console le matin, récap très simple de la journée le soir.

  python -X utf8 .seokb/runtime/agents_quotidiens.py verifier          réglages + message de test
  python -X utf8 .seokb/runtime/agents_quotidiens.py alertes [--sec]   passe maintenant (--sec : affiche, n'envoie rien)
  python -X utf8 .seokb/runtime/agents_quotidiens.py recap [--sec]
  python -X utf8 .seokb/runtime/agents_quotidiens.py planifier         pose la tâche horaire (après accord de l'élève)
  python -X utf8 .seokb/runtime/agents_quotidiens.py retirer           retire la tâche
  python -X utf8 .seokb/runtime/agents_quotidiens.py planifie          appel de la tâche horaire : chaque agent
                                                                       passe une fois par jour, dès son heure

Réglages : .env.local du coffre (voir le skill agents-quotidiens). État et traces : .seokb/agents-quotidiens/.
Rapports : wiki/pilotage/alertes/AAAA-MM-JJ.md et wiki/pilotage/recap/AAAA-MM-JJ.md.
"""
import argparse, glob, hashlib, json, os, platform, re, shutil, subprocess, sys, traceback
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import alertes_gsc, notifier  # noqa: E402
from xml.sax.saxutils import escape as xml  # noqa: E402

SILENCE_JOURS = 6
AUTO = re.compile(r'^auto: WIP|\(auto\)\s*$|^Merge ')


# ---------- réglages, état, traces ----------

def lire_env(root):
    cfg = {}
    p = root / '.env.local'
    if p.exists():
        for l in p.read_text(encoding='utf-8').splitlines():
            l = l.strip()
            if l and not l.startswith('#') and '=' in l:
                k, v = l.split('=', 1)
                cfg[k.strip()] = v.split(' #')[0].strip().strip('"\'')
    for k in ('GSC_CREDENTIALS',):
        cfg.setdefault(k, os.environ.get(k, ''))
    return cfg


def maintenant(cfg):
    fuseau = cfg.get('FUSEAU')
    if fuseau:
        try:
            from zoneinfo import ZoneInfo
            return datetime.now(ZoneInfo(fuseau))
        except Exception:
            pass
    return datetime.now().astimezone()


def dossier(root):
    d = root / '.seokb' / 'agents-quotidiens'
    d.mkdir(parents=True, exist_ok=True)
    return d


def lire_etat(root):
    try:
        return json.loads((dossier(root) / 'etat.json').read_text(encoding='utf-8'))
    except Exception:
        return {}


def ecrire_etat(root, etat):
    (dossier(root) / 'etat.json').write_text(json.dumps(etat, ensure_ascii=False, indent=1), encoding='utf-8')


def tracer(root, nom, jour, lignes):
    d = dossier(root) / 'logs'
    d.mkdir(exist_ok=True)
    with open(d / f'{nom}-{jour}.log', 'a', encoding='utf-8') as f:
        f.write(f'=== {datetime.now():%Y-%m-%d %H:%M} ===\n' + '\n'.join(lignes) + '\n')


def rapport(root, sous_dossier, jour, titre, lignes):
    d = root / 'wiki' / 'pilotage' / sous_dossier
    d.mkdir(parents=True, exist_ok=True)
    p = d / f'{jour}.md'
    p.write_text(f'---\ntype: register\ntitle: {titre}\ncreated: {jour}\nstatus: auto-generated\n---\n\n# {titre}\n\n'
                 + '\n'.join(f'- {l.lstrip("- ")}' for l in lignes) + '\n', encoding='utf-8')
    return p


# ---------- alertes ----------

def alertes(root, cfg, sec=False):
    now = maintenant(cfg)
    jour = now.date()
    etat = lire_etat(root)
    creds = cfg.get('GSC_CREDENTIALS')
    if not creds or not Path(creds).expanduser().exists():
        msg = "GSC_CREDENTIALS absent ou introuvable : l'agent ne peut pas lire la Search Console."
        tracer(root, 'alertes', jour, [msg])
        print(msg)
        return 1
    try:
        gsc = alertes_gsc.Gsc(Path(creds).expanduser())
        voulus = [s.strip() for s in cfg.get('ALERTES_SITES', '').split(',') if s.strip()]
        sites = [s for s in gsc.sites() if not voulus or alertes_gsc.nom_site(s) in voulus or s in voulus]
    except Exception as e:
        msg = f'accès Search Console impossible : {e}'
        tracer(root, 'alertes', jour, [msg])
        if not sec and etat.get('alertes_panne') != jour.isoformat():
            notifier.envoyer(cfg, f'Alertes SEO {jour:%d/%m} : agent en panne', [msg])
            etat['alertes_panne'] = jour.isoformat()
            ecrire_etat(root, etat)
        print(msg)
        return 1

    seuil = (jour - timedelta(days=SILENCE_JOURS)).isoformat()
    deja = {k: v for k, v in etat.get('alertes_envoyees', {}).items() if v > seuil}
    nouvelles, trace = [], []
    for site in sites:
        try:
            als, fin = alertes_gsc.analyser(gsc, site, jour)
        except Exception as e:
            trace.append(f'ERREUR {alertes_gsc.nom_site(site)} : {e}')
            continue
        neuves = [a for a in als if a['cle'] not in deja]
        trace.append(f'{alertes_gsc.nom_site(site)} : {len(als)} alerte(s), {len(neuves)} nouvelle(s), donnée au {fin}')
        nouvelles += [(site, fin, a) for a in neuves]

    lignes = [f"{alertes_gsc.nom_site(s)} · {a['type']} : {a['texte']}" for s, _, a in nouvelles]
    nb_sites = len({s for s, _, _ in nouvelles})
    titre = f"Alertes SEO {jour:%d/%m} : {len(lignes)} alerte{'s' if len(lignes) > 1 else ''} sur {nb_sites} site{'s' if nb_sites > 1 else ''}"
    if sec:
        print('\n'.join(trace) + ('\n\n' + titre + '\n' + '\n'.join(lignes) if lignes else '\n\naucune nouvelle alerte'))
        return 0
    if lignes:
        fins = sorted({f for _, f, _ in nouvelles if f})
        p = rapport(root, 'alertes', jour, titre, [f'Période : 7 jours au {fins[-1]:%d/%m} contre les 7 d\'avant'] + lignes if fins else lignes)
        res = notifier.envoyer(cfg, titre, lignes)
        trace.append(f'rapport {p.relative_to(root)} ; envoi {res}')
        if any(v == 'ok' for v in res.values()):
            for _, _, a in nouvelles:
                deja[a['cle']] = jour.isoformat()
    else:
        trace.append('aucune nouvelle alerte, aucun message')
    tracer(root, 'alertes', jour, trace)
    etat.update({'alertes_jour': jour.isoformat(), 'alertes_envoyees': deja})
    ecrire_etat(root, etat)
    return 0


# ---------- récap ----------

def projet_claude(root):
    return Path.home() / '.claude' / 'projects' / re.sub(r'[^A-Za-z0-9]', '-', str(root.resolve()))


def matiere_recap(root, depuis):
    commits = []
    if (root / '.git').exists():
        out = subprocess.run(['git', '-C', str(root), 'log', '--all', '--no-merges', f'--since={depuis.isoformat()}',
                              '--format=%an%x1f%s'], capture_output=True, text=True, encoding='utf-8').stdout
        for l in out.splitlines():
            auteur, _, sujet = l.partition('\x1f')
            if not AUTO.search(sujet):
                commits.append(sujet)
    fichiers = []
    for sous in ('wiki', 'raw'):
        for p in (root / sous).rglob('*.md') if (root / sous).is_dir() else []:
            if p.stat().st_mtime >= depuis.timestamp() and 'pilotage' not in p.parts:
                fichiers.append(p.relative_to(root).as_posix())
    demandes = []
    for f in glob.glob(str(projet_claude(root) / '*.jsonl')):
        if os.path.getmtime(f) < depuis.timestamp():
            continue
        try:
            for l in open(f, encoding='utf-8'):
                o = json.loads(l)
                if o.get('type') != 'user':
                    continue
                m = o.get('message', {}).get('content')
                if isinstance(m, list):
                    m = ' '.join(x.get('text', '') for x in m if isinstance(x, dict) and x.get('type') == 'text')
                m = (m or '').strip()
                if m and not m.startswith(('<', '/', 'Caveat')):
                    demandes.append(' '.join(m.split())[:200])
                    break
        except Exception:
            continue
    return commits[:80], sorted(fichiers)[:80], demandes[:40]


def condenser(commits, fichiers, demandes):
    claude = shutil.which('claude')
    if not claude:
        raise RuntimeError('commande claude introuvable')
    matiere = ['## Commits'] + [f'- {c[:200]}' for c in commits] + ['## Fichiers du coffre modifiés'] + \
              [f'- {f}' for f in fichiers] + ['## Demandes dans les sessions Claude'] + [f'- {d}' for d in demandes]
    consigne = ("Voici les commits, les fichiers modifiés et les demandes du jour dans un coffre SEO.\n"
                "Écris le récap de la journée : 5 à 10 lignes, une action faite par ligne, commençant par « - ».\n"
                "Chaque ligne nomme le chantier ou le dossier concerné, puis dit ce qui a été fait, au passé composé, en français courant ; regroupe un même chantier en une ligne.\n"
                "Garde les chiffres et les noms tels quels. Rien d'autre : pas de titre, pas d'introduction, pas de conclusion. N'invente rien.\n\n"
                + '\n'.join(matiere))
    r = subprocess.run([claude, '-p', '--model', 'haiku'], input=consigne, capture_output=True, text=True,
                       encoding='utf-8', timeout=300, cwd=str(Path.home()))
    lignes = [l.strip() for l in r.stdout.splitlines() if l.strip().startswith('-')]
    if r.returncode != 0 or not lignes:
        raise RuntimeError(f'claude exit {r.returncode}')
    return [l.lstrip('- ').strip() for l in lignes[:10]]


def brut(commits, fichiers, demandes):
    out = [c for c in commits[:6]]
    if fichiers:
        out.append(f"{len(fichiers)} note(s) modifiée(s), dont {', '.join(fichiers[:3])}")
    if demandes:
        out.append(f'{len(demandes)} session(s) Claude, dont « {demandes[0][:120]} »')
    return out[:10]


def recap(root, cfg, sec=False, jour=None):
    now = maintenant(cfg)
    jour = jour or now.date()
    etat = lire_etat(root)
    debut = now.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=(now.date() - jour).days)
    depuis = datetime.fromisoformat(etat['recap_fin']) if etat.get('recap_fin') else debut
    depuis = max(depuis, now - timedelta(hours=36))
    commits, fichiers, demandes = matiere_recap(root, depuis)
    trace = [f'depuis {depuis:%d/%m %H:%M} : {len(commits)} commits, {len(fichiers)} notes, {len(demandes)} sessions']
    if not (commits or fichiers or demandes):
        lignes = ["Aucune action enregistrée aujourd'hui dans le coffre."]
    else:
        try:
            lignes = condenser(commits, fichiers, demandes)
        except Exception as e:
            trace.append(f'condensation impossible, liste brute : {e}')
            lignes = brut(commits, fichiers, demandes)
    titre = f'Récap du {jour:%d/%m}'
    if sec:
        print(titre + '\n' + '\n'.join('- ' + l for l in lignes) + '\n\n' + '\n'.join(trace))
        return 0
    p = rapport(root, 'recap', jour, titre, lignes)
    res = notifier.envoyer(cfg, titre, lignes)
    trace.append(f'rapport {p.relative_to(root)} ; envoi {res}')
    tracer(root, 'recap', jour, trace + lignes)
    etat.update({'recap_jour': jour.isoformat(), 'recap_fin': now.isoformat()})
    ecrire_etat(root, etat)
    return 0


# ---------- passage horaire ----------

def heure(cfg, cle, defaut):
    try:
        return int(cfg.get(cle) or defaut)
    except ValueError:
        return defaut


def planifie(root, cfg):
    now = maintenant(cfg)
    jour = now.date().isoformat()
    etat = lire_etat(root)
    agents = [a.strip() for a in (cfg.get('AGENTS_QUOTIDIENS') or 'alertes,recap').split(',')]
    code = 0
    if 'alertes' in agents and now.hour >= heure(cfg, 'ALERTES_HEURE', 9) and etat.get('alertes_jour') != jour:
        code |= alertes(root, cfg)
    etat = lire_etat(root)
    if 'recap' in agents:
        hier = (now.date() - timedelta(days=1)).isoformat()
        if now.hour >= heure(cfg, 'RECAP_HEURE', 20) and etat.get('recap_jour') != jour:
            code |= recap(root, cfg)
        elif now.hour < 12 and etat.get('recap_jour') and etat['recap_jour'] < hier:
            code |= recap(root, cfg, jour=now.date() - timedelta(days=1))  # ordinateur éteint la veille au soir
    return code


# ---------- planification ----------

def ident(root):
    return 'seokb2.agents-quotidiens.' + hashlib.sha1(str(root.resolve()).encode()).hexdigest()[:8]


def commande(root):
    return [sys.executable, '-X', 'utf8', str(Path(__file__).resolve()), '--coffre', str(root.resolve()), 'planifie']


def plist(root):
    args = ''.join(f'<string>{xml(a)}</string>' for a in commande(root))
    log = dossier(root) / 'logs' / 'tache.log'
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" '
            '"http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0"><dict>'
            f'<key>Label</key><string>{ident(root)}</string><key>ProgramArguments</key><array>{args}</array>'
            f'<key>EnvironmentVariables</key><dict><key>PATH</key><string>{xml(os.environ.get("PATH", "/usr/bin:/bin"))}</string></dict>'
            '<key>StartCalendarInterval</key><dict><key>Minute</key><integer>5</integer></dict>'
            f'<key>WorkingDirectory</key><string>{xml(str(root.resolve()))}</string>'
            f'<key>StandardOutPath</key><string>{xml(str(log))}</string><key>StandardErrorPath</key><string>{xml(str(log))}</string>'
            '</dict></plist>\n')


def planifier(root, retirer=False):
    systeme = platform.system()
    (dossier(root) / 'logs').mkdir(exist_ok=True)
    if systeme == 'Darwin':
        p = Path.home() / 'Library' / 'LaunchAgents' / (ident(root) + '.plist')
        dom = f'gui/{os.getuid()}'
        subprocess.run(['launchctl', 'bootout', f'{dom}/{ident(root)}'], capture_output=True)
        if retirer:
            p.unlink(missing_ok=True)
            return f'Tâche retirée ({p}).'
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(plist(root), encoding='utf-8')
        subprocess.run(['launchctl', 'bootstrap', dom, str(p)], check=True)
        avert = ''
        if any(x in root.resolve().parts for x in ('Documents', 'Desktop', 'Mobile Documents')):
            avert = (" Attention : le coffre est dans Documents, Bureau ou iCloud. macOS peut bloquer la tâche planifiée "
                     "sur ces dossiers ; vérifier .seokb/agents-quotidiens/logs/ après le premier passage.")
        return f'Tâche posée : {p}, réveil toutes les heures à :05.' + avert
    if systeme == 'Windows':
        nom = 'SEOKB2 agents quotidiens ' + ident(root)[-8:]
        if retirer:
            subprocess.run(['schtasks', '/Delete', '/TN', nom, '/F'], capture_output=True)
            return f'Tâche « {nom} » retirée.'
        tr = subprocess.list2cmdline(commande(root))
        subprocess.run(['schtasks', '/Create', '/SC', 'HOURLY', '/MO', '1', '/ST', '00:05', '/TN', nom, '/TR', tr, '/F'], check=True)
        return f'Tâche « {nom} » posée dans le Planificateur de tâches, toutes les heures à :05.'
    ligne = '5 * * * * ' + ' '.join(f'"{a}"' for a in commande(root)) + f' # {ident(root)}'
    ancien = subprocess.run(['crontab', '-l'], capture_output=True, text=True).stdout
    garde = '\n'.join(l for l in ancien.splitlines() if ident(root) not in l)
    nouveau = garde + ('' if retirer else ('\n' if garde else '') + ligne) + '\n'
    subprocess.run(['crontab', '-'], input=nouveau, text=True, check=True)
    return 'Ligne cron retirée.' if retirer else 'Ligne cron posée : toutes les heures à :05.'


# ---------- vérification ----------

def verifier(root, cfg):
    pb = notifier.manquants(cfg)
    if not cfg.get('GSC_CREDENTIALS') and 'alertes' in (cfg.get('AGENTS_QUOTIDIENS') or 'alertes,recap'):
        pb.append('GSC_CREDENTIALS')
    gi = root / '.gitignore'
    if (root / '.git').exists() and '.env' not in (gi.read_text(encoding='utf-8') if gi.exists() else ''):
        with open(gi, 'a', encoding='utf-8') as f:
            f.write('\n# Secrets SEOKB2 (agents quotidiens)\n.env*\n')
        print('.env* ajouté à .gitignore : le mot de passe et les clés ne partiront pas dans git.')
    if pb:
        print('Réglages manquants dans .env.local : ' + ', '.join(pb))
        return 1
    res = notifier.envoyer(cfg, 'SEOKB2 : test des agents quotidiens',
                           ['Ce message vérifie seulement l\'envoi.',
                            f"Alertes à partir de {heure(cfg, 'ALERTES_HEURE', 9)} h, récap à partir de {heure(cfg, 'RECAP_HEURE', 20)} h."])
    print('Envoi de test : ' + json.dumps(res, ensure_ascii=False))
    return 0 if all(v == 'ok' for v in res.values()) else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('action', choices=['verifier', 'alertes', 'recap', 'planifier', 'retirer', 'planifie'])
    ap.add_argument('--sec', action='store_true')
    ap.add_argument('--coffre', default=str(Path(__file__).resolve().parents[2]))
    a = ap.parse_args()
    root = Path(a.coffre).expanduser().resolve()
    cfg = lire_env(root)
    try:
        if a.action == 'verifier':
            return verifier(root, cfg)
        if a.action == 'alertes':
            return alertes(root, cfg, a.sec)
        if a.action == 'recap':
            return recap(root, cfg, a.sec)
        if a.action in ('planifier', 'retirer'):
            print(planifier(root, retirer=a.action == 'retirer'))
            return 0
        return planifie(root, cfg)
    except Exception:
        tracer(root, 'erreur', datetime.now().date(), [traceback.format_exc()])
        raise


if __name__ == '__main__':
    sys.exit(main())
