"""Durable strategy team coordinator. CLI mutates only its own data directory."""
from __future__ import annotations
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import uuid

from paths import pid_alive, team_root, vault_root

ROLES = ('pilote', 'go-to-market', 'business', 'recherche', 'strategie-mot-cle', 'diagnostic-seo', 'visibilite-ia', 'architecture-roadmap', 'qualite')
PHASES = ('intentions', 'questions', 'preuves')


def now():
    return datetime.now(timezone.utc).isoformat()


def dump(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def sha(value):
    return hashlib.sha256(dump(value).encode()).hexdigest()


class Team:
    def __init__(self, root=None):
        self.root = Path(root or team_root()).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        with self.db() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS projects(id TEXT PRIMARY KEY, data TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS missions(id TEXT PRIMARY KEY, project_id TEXT NOT NULL, data TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS history(mission_id TEXT, version INTEGER, data TEXT, archived_at TEXT);
                CREATE TABLE IF NOT EXISTS events(seq INTEGER PRIMARY KEY AUTOINCREMENT, project_id TEXT, mission_id TEXT, action TEXT, detail TEXT, created TEXT);
            ''')

    @contextmanager
    def db(self):
        db = sqlite3.connect(self.root / 'team.sqlite3', timeout=30)
        try:
            db.execute('BEGIN IMMEDIATE')
            yield db
            db.commit()
        except BaseException:
            db.rollback()
            raise
        finally:
            db.close()

    def _get(self, db, table, identity):
        row = db.execute('SELECT data FROM ' + table + ' WHERE id=?', (identity,)).fetchone()
        if not row:
            raise ValueError('Projet ou mission introuvable : ' + identity)
        return json.loads(row[0])

    def _save(self, db, mission):
        mission['updated'] = now()
        db.execute('INSERT OR REPLACE INTO missions VALUES(?,?,?)', (mission['id'], mission['project_id'], dump(mission)))

    def _event(self, db, project_id, mission_id, action, detail):
        db.execute('INSERT INTO events(project_id,mission_id,action,detail,created) VALUES(?,?,?,?,?)', (project_id, mission_id, action, dump(detail), now()))

    def _missions(self, db, project_id):
        return [json.loads(row[0]) for row in db.execute('SELECT data FROM missions WHERE project_id=? ORDER BY rowid', (project_id,))]

    def _new(self, db, project_id, role, phase, subject, depends):
        m = dict(id=uuid.uuid4().hex, project_id=project_id, role=role, phase=phase, subject=subject,
                 depends=list(depends), status='queued', version=1, result=None, artifact_path=None,
                 sha=None, execution=None, approval=None, correction=None, source_files=[], created=now(), updated=now())
        self._save(db, m)
        self._event(db, project_id, m['id'], 'created', {'role': role, 'phase': phase})
        return m

    def start(self, brief):
        if not isinstance(brief, dict):
            raise ValueError('Brief JSON objet requis.')
        for key in ('name', 'site', 'objective', 'request'):
            if not isinstance(brief.get(key), str) or not brief[key].strip():
                raise ValueError('Champ requis : ' + key)
        if brief.get('mode') not in ('seo', 'geo', 'seo-geo'):
            raise ValueError('Mode attendu : seo, geo ou seo-geo.')
        version = brief.get('workflow_version', 4)
        if type(version) is not int or version not in (1, 2, 3, 4):
            raise ValueError('Version workflow attendue : 1, 2, 3 ou 4.')
        keywords = brief.get('seeds', brief.get('keywords', [])) if version >= 3 else brief.get('keywords')
        if not isinstance(keywords, list) or (version < 3 and not 5 <= len(keywords) <= 10):
            raise ValueError('Fournir de 5 à 10 mots-clés business validés pour le workflow historique.')
        if any(not isinstance(k, str) or not k.strip() for k in keywords):
            raise ValueError('Chaque mot-clé indicatif doit être une chaîne non vide.')
        keywords = [' '.join(k.split()) for k in keywords]
        if len(set(k.casefold() for k in keywords)) != len(keywords):
            raise ValueError('Les mots-clés doivent être uniques.')
        vault_input = brief.get('vault', str(vault_root()))
        if not isinstance(vault_input, str) or not vault_input.strip():
            raise ValueError('Chemin de coffre invalide.')
        vault = Path(vault_input).expanduser().resolve()
        if not vault.is_dir() or not (vault / 'AGENTS.md').is_file():
            raise ValueError('Le coffre doit exister et contenir AGENTS.md.')
        brief = dict(brief, vault=str(vault), workflow_version=version)
        if version >= 3:
            brief.pop('keywords', None)
            brief['seeds'] = keywords
        else:
            brief['keywords'] = keywords
        p = dict(id=uuid.uuid4().hex, brief=brief, name=brief['name'], site=brief['site'], mode=brief['mode'], created=now())
        with self.db() as db:
            db.execute('INSERT INTO projects VALUES(?,?)', (p['id'], dump(p)))
            m = self._new(db, p['id'], 'pilote', 'cadrage', {'seeds' if version >= 3 else 'keywords': keywords}, [])
        return dict(project=p, mission=m)

    def _integrity(self, mission):
        result = mission['result']
        if not result or sha(result) != mission['sha']:
            raise ValueError('Version du livrable invalide : ' + mission['id'])
        artifact = Path(mission['artifact_path']).resolve()
        artifact.relative_to(self.root)
        if not artifact.is_file() or artifact.read_text(encoding='utf-8') != result['artifact_markdown']:
            raise ValueError('Livrable modifié ou absent : ' + mission['id'])
        for source in mission.get('source_files', []):
            path = Path(source['path'])
            if str(path.resolve()) != source['resolved_path'] or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != source['sha256']:
                raise ValueError('Pièce source modifiée ou absente : ' + source['path'])

    def _approved(self, db, identity, seen=None):
        seen = set() if seen is None else seen
        if identity in seen:
            raise ValueError('Cycle de dépendances.')
        seen.add(identity)
        m = self._get(db, 'missions', identity)
        if m['status'] != 'approved' or not m['approval'] or m['approval']['sha'] != m['sha']:
            raise ValueError('Validation requise : ' + identity)
        self._integrity(m)
        for dep in m['depends']:
            self._approved(db, dep, seen.copy())
        return m

    def _upstream(self, db, m):
        collected = {}
        def visit(identity):
            item = self._approved(db, identity)
            for dep in item['depends']:
                if dep not in collected:
                    visit(dep)
            collected[identity] = item
        for dep in m['depends']:
            visit(dep)
        return list(collected.values())

    def _validate_keyword(self, db, m, result):
        if m['role'] == 'strategie-mot-cle' and result['status'] == 'review':
            from keyword_adapter import validate
            validate({'project': self._get(db, 'projects', m['project_id']), 'mission': m,
                      'upstream': self._upstream(db, m)}, result)

    def _validate_stage(self, db, m, result, execution=None):
        project = self._get(db, 'projects', m['project_id'])
        if project['brief'].get('workflow_version', 1) in (2, 3, 4) and m['role'] != 'strategie-mot-cle':
            from contracts import validate
            trace = execution if execution is not None else m.get('execution') or {}
            validate({'project': project, 'mission': m, 'upstream': self._upstream(db, m),
                      'workspace': trace.get('workspace')}, result)

    def _check_workflow(self, db, m):
        from orchestration import check_mission
        check_mission(self, db, m)

    def _needs_bundle(self, db, mission):
        project = self._get(db, 'projects', mission['project_id'])
        if project['brief'].get('workflow_version', 1) >= 3:
            return mission['phase'] == 'consolidation'
        return mission['role'] == 'architecture-roadmap'

    def _check_portfolio(self, db, m, result):
        from orchestration import check_portfolio_revision
        check_portfolio_revision(self._get(db, 'projects', m['project_id']),
                                 self._missions(db, m['project_id']), m, result)

    def _ready(self, db, m):
        self._check_workflow(db, m)
        if m['status'] != 'queued':
            raise ValueError('Mission non disponible : ' + m['status'])
        for dep in m['depends']:
            self._approved(db, dep)
        if self._needs_bundle(db, m):
            self._bundle(db, m['project_id'])

    def add_mission(self, project_id, role, phase, subject=None, depends=None):
        if role not in ROLES or not isinstance(phase, str) or not phase.strip():
            raise ValueError('Rôle ou phase invalide.')
        if role == 'strategie-mot-cle':
            raise ValueError('Utiliser fanout puis advance pour les missions par mot-clé.')
        subject, depends = subject or {}, depends or []
        if not isinstance(subject, dict) or not depends:
            raise ValueError('Objet subject et dépendances explicites requis.')
        with self.db() as db:
            project = self._get(db, 'projects', project_id)
            if project['brief'].get('workflow_version', 1) in (2, 3, 4):
                raise ValueError('Workflow structuré : utiliser prepare pour créer les missions du graphe.')
            for dep in depends:
                m = self._get(db, 'missions', dep)
                if m['project_id'] != project_id:
                    raise ValueError('Dépendance hors projet.')
            if role == 'architecture-roadmap':
                bundle = self._bundle(db, project_id)
                depends = list(dict.fromkeys(list(depends) + [entry['phases'][-1]['id'] for entry in bundle['keywords']]))
            return self._new(db, project_id, role, phase, subject, depends)

    def fanout(self, project_id):
        with self.db() as db:
            p = self._get(db, 'projects', project_id)
            missions = self._missions(db, project_id)
            if p['brief'].get('workflow_version', 1) >= 3:
                from orchestration import portfolio
                keywords = portfolio(p, missions, approved_only=True)
                predecessor = next(m for m in missions if m['phase'] == 'priorisation' and m['role'] == 'business')
            else:
                keywords = p['brief']['keywords']
                predecessor = next(m for m in missions if m['phase'] == 'cadrage' and m['role'] == 'pilote')
            self._approved(db, predecessor['id'])
            result = []
            for keyword in keywords:
                existing = next((m for m in missions if m['role'] == 'strategie-mot-cle' and m['phase'] == 'intentions' and m['subject']['keyword'] == keyword), None)
                result.append(existing or self._new(db, project_id, 'strategie-mot-cle', 'intentions', {'keyword': keyword, 'agent_key': project_id + ':keyword-' + str(keywords.index(keyword) + 1)}, [predecessor['id']]))
            return result

    def advance(self, identity):
        with self.db() as db:
            m = self._approved(db, identity)
            if m['role'] != 'strategie-mot-cle' or m['phase'] not in PHASES[:-1]:
                raise ValueError('Seules intentions et questions peuvent avancer.')
            phase = PHASES[PHASES.index(m['phase']) + 1]
            existing = next((n for n in self._missions(db, m['project_id']) if n['role'] == m['role'] and n['phase'] == phase and n['subject'].get('keyword') == m['subject']['keyword']), None)
            return existing or self._new(db, m['project_id'], m['role'], phase, dict(m['subject']), [identity])

    def _bundle(self, db, project_id):
        p = self._get(db, 'projects', project_id)
        missions = self._missions(db, project_id)
        from orchestration import portfolio
        keywords = portfolio(p, missions, approved_only=True)
        if p['brief'].get('workflow_version', 1) >= 3:
            selected = next(m for m in missions if m['phase'] == 'priorisation')
            self._approved(db, selected['id'])
        entries = []
        for keyword in keywords:
            phases = []
            for phase in PHASES:
                matches = [m for m in missions if m['role'] == 'strategie-mot-cle' and m['subject'].get('keyword') == keyword and m['phase'] == phase]
                if len(matches) != 1:
                    raise ValueError('Stratégie incomplète : ' + keyword + ' / ' + phase)
                approved = self._approved(db, matches[0]['id'])
                self._validate_keyword(db, approved, approved['result'])
                phases.append(approved)
            entries.append({'keyword': keyword, 'phases': phases})
        return {'project_id': project_id, 'keywords': entries, 'generated': now()}

    def bundle(self, project_id):
        with self.db() as db:
            return self._bundle(db, project_id)

    @staticmethod
    def validate_result(result):
        if not isinstance(result, dict):
            raise ValueError('Résultat objet requis.')
        required = ('status', 'summary', 'artifact_markdown', 'facts', 'blockers', 'next_actions')
        if any(k not in result for k in required) or result['status'] not in ('review', 'blocked'):
            raise ValueError('Résultat incomplet ou statut invalide.')
        for key in ('summary', 'artifact_markdown'):
            if not isinstance(result[key], str) or not result[key].strip():
                raise ValueError('Texte requis : ' + key)
        for key in ('facts', 'blockers', 'next_actions'):
            if not isinstance(result[key], list):
                raise ValueError('Liste requise : ' + key)
        if 'source_files' in result:
            raise ValueError('Les empreintes des sources sont produites par le contrôleur.')
        if '_execution' in result:
            raise ValueError('La trace doit provenir du fournisseur, séparément du livrable.')
        return result

    def _source_snapshot(self, db, m, result, execution):
        project = self._get(db, 'projects', m['project_id'])
        if project['brief'].get('workflow_version', 1) not in (2, 3, 4) or m['role'] == 'strategie-mot-cle' or result['status'] != 'review':
            return []
        vault = Path(project['brief']['vault']).resolve()
        roots = [vault]
        if execution and execution.get('workspace'):
            roots.append(Path(execution['workspace']).resolve())
        paths = {}
        def walk(value):
            if isinstance(value, dict):
                for field, child in value.items():
                    if field in ('source_file', 'trace_file', 'business_dataset') and child is not None:
                        if not isinstance(child, str) or not child.strip():
                            raise ValueError('Référence fichier source invalide : ' + field)
                        raw = Path(child).expanduser()
                        raw = raw if raw.is_absolute() else vault / raw
                        resolved = raw.resolve()
                        if not any(resolved.is_relative_to(root) for root in roots) or not resolved.is_file():
                            raise ValueError('Pièce source absente ou hors périmètre : ' + child)
                        paths[str(raw)] = {'path': str(raw), 'resolved_path': str(resolved),
                                           'sha256': hashlib.sha256(resolved.read_bytes()).hexdigest()}
                    else:
                        walk(child)
            elif isinstance(value, list):
                for child in value:
                    walk(child)
        walk(result.get('stage_payload', {}))
        return [paths[name] for name in sorted(paths)]

    def _submit(self, db, m, result, execution=None):
        self.validate_result(result)
        self._check_workflow(db, m)
        if m['status'] not in ('queued', 'running'):
            raise ValueError('Réviser avant de remplacer un livrable existant.')
        for dep in m['depends']:
            self._approved(db, dep)
        if self._needs_bundle(db, m):
            self._bundle(db, m['project_id'])
        self._validate_keyword(db, m, result)
        self._validate_stage(db, m, result, execution)
        self._check_portfolio(db, m, result)
        source_files = self._source_snapshot(db, m, result, execution)
        folder = self.root / 'artifacts' / m['id']
        folder.mkdir(parents=True, exist_ok=True)
        artifact = folder / ('v%s.md' % m['version'])
        if artifact.exists():
            raise ValueError('Version de livrable déjà présente.')
        artifact.write_text(result['artifact_markdown'], encoding='utf-8')
        m.update(status=result['status'], result=result, artifact_path=str(artifact), sha=sha(result), execution=execution, source_files=source_files)
        self._save(db, m)
        self._event(db, m['project_id'], m['id'], 'submitted', {'sha': m['sha'], 'execution': execution})
        return m

    def submit(self, identity, result, execution=None):
        with self.db() as db:
            m = self._get(db, 'missions', identity)
            if m['status'] == 'running':
                raise ValueError('Mission en cours : seul son fournisseur peut remettre le résultat.')
            return self._submit(db, m, result, execution)

    def approve(self, identity, fingerprint, message, user_approved=False):
        if not user_approved or not isinstance(message, str) or not message.strip():
            raise ValueError('Accord humain explicite et message exact requis.')
        with self.db() as db:
            m = self._get(db, 'missions', identity)
            if m['status'] != 'review' or fingerprint != m['sha']:
                raise ValueError('Version non présentée ou empreinte incorrecte.')
            self._integrity(m)
            self._check_workflow(db, m)
            self._validate_keyword(db, m, m['result'])
            self._validate_stage(db, m, m['result'])
            self._check_portfolio(db, m, m['result'])
            for dep in m['depends']:
                self._approved(db, dep)
            if self._needs_bundle(db, m):
                self._bundle(db, m['project_id'])
            m.update(status='approved', approval={'sha': fingerprint, 'message': message, 'at': now()})
            self._save(db, m)
            self._event(db, m['project_id'], identity, 'approved', m['approval'])
            return m

    def revise(self, identity, message):
        if not message.strip():
            raise ValueError('Consigne de correction requise.')
        with self.db() as db:
            m = self._get(db, 'missions', identity)
            missions = self._missions(db, m['project_id'])
            affected = {identity}
            changed = True
            while changed:
                changed = False
                for item in missions:
                    if set(item['depends']) & affected and item['id'] not in affected:
                        affected.add(item['id'])
                        changed = True
            # Consolidations depend on the complete portfolio even if not named explicitly.
            project = self._get(db, 'projects', m['project_id'])
            if m['role'] == 'strategie-mot-cle' and project['brief'].get('workflow_version', 1) < 3:
                affected.update(n['id'] for n in missions if n['role'] == 'architecture-roadmap')
                while True:
                    added = {n['id'] for n in missions if set(n['depends']) & affected} - affected
                    if not added:
                        break
                    affected.update(added)
            if any(n['status'] == 'running' for n in missions if n['id'] in affected):
                raise ValueError('Attendre la fin des missions en cours avant correction.')
            for item in missions:
                if item['id'] not in affected:
                    continue
                db.execute('INSERT INTO history VALUES(?,?,?,?)', (item['id'], item['version'], dump(item), now()))
                item.update(version=item['version'] + 1, status='queued', previous_result=item['result'], result=None,
                            sha=None, artifact_path=None, approval=None, execution=None, source_files=[],
                            correction=message if item['id'] == identity else 'Entrée révisée : ' + identity)
                self._save(db, item)
                self._event(db, item['project_id'], item['id'], 'revised', {'reason': item['correction']})
            return {'affected': sorted(affected)}

    def retry(self, identity):
        with self.db() as db:
            m = self._get(db, 'missions', identity)
            if m['status'] != 'failed':
                raise ValueError('retry réservé aux échecs techniques ; utiliser revise pour un blocage métier.')
            m['status'] = 'queued'
            self._save(db, m)
            self._event(db, m['project_id'], identity, 'retry', {})
            return m

    def recover(self, identity):
        with self.db() as db:
            m = self._get(db, 'missions', identity)
            if m['status'] != 'running':
                raise ValueError('recover réservé aux missions interrompues en cours.')
            pid = m.get('owner_pid')
            if not isinstance(pid, int) or pid <= 0:
                raise ValueError('PID propriétaire absent ; vérifier manuellement le processus.')
            if pid_alive(pid):
                raise ValueError('Processus propriétaire toujours actif ; attendre sa fin.')
            m.update(status='failed', error='Processus propriétaire arrêté ; reprise explicite requise.')
            self._save(db, m)
            self._event(db, m['project_id'], identity, 'recovered', {'owner_pid': pid})
            return m

    def run(self, identity, provider=None):
        with self.db() as db:
            m = self._get(db, 'missions', identity)
            self._ready(db, m)
            project = self._get(db, 'projects', m['project_id'])
            upstream = self._upstream(db, m)
            m['status'] = 'running'
            m['owner_pid'] = os.getpid()
            m['attempt_id'] = uuid.uuid4().hex
            self._save(db, m)
            self._event(db, m['project_id'], identity, 'started', {})
        workspace = self.root / 'workspaces' / identity / ('v%s-%s' % (m['version'], uuid.uuid4().hex))
        workspace.mkdir(parents=True, exist_ok=False)
        try:
            if provider is None:
                from providers import run as provider
            result = provider({'project': project, 'mission': m, 'upstream': upstream}, workspace)
            result = dict(result)
            execution = result.pop('_execution', None)
            if not isinstance(execution, dict):
                raise ValueError('Trace du fournisseur absente.')
            with self.db() as db:
                current = self._get(db, 'missions', identity)
                if current['status'] != 'running' or current.get('attempt_id') != m['attempt_id'] or current['version'] != m['version']:
                    raise ValueError('La tentative ne possède plus cette mission.')
                return self._submit(db, current, result, execution)
        except BaseException as exc:
            with self.db() as db:
                current = self._get(db, 'missions', identity)
                if current['status'] == 'running' and current.get('attempt_id') == m['attempt_id'] and current['version'] == m['version']:
                    current.update(status='failed', error=type(exc).__name__ + ': ' + str(exc)[:600])
                    self._save(db, current)
                    self._event(db, current['project_id'], identity, 'failed', {'error': current['error']})
            raise

    def prepare(self, project_id):
        from orchestration import prepare
        return prepare(self, project_id)

    def run_ready(self, project_id, max_jobs=1, workers=1, provider=None):
        from orchestration import run_ready
        return run_ready(self, project_id, max_jobs, workers, provider)

    def next(self, project_id):
        with self.db() as db:
            project = self._get(db, 'projects', project_id)
        if project['brief'].get('workflow_version', 1) in (2, 3, 4):
            from orchestration import inspect
            return inspect(self, project_id)
        with self.db() as db:
            self._get(db, 'projects', project_id)
            missions = self._missions(db, project_id)
            ready, review, blocked = [], [], []
            for m in missions:
                if m['status'] == 'review':
                    review.append(m)
                elif m['status'] == 'queued':
                    try:
                        self._ready(db, m)
                        ready.append(m)
                    except ValueError as exc:
                        blocked.append(dict(m, blocking_reason=str(exc)))
                elif m['status'] in ('blocked', 'failed', 'running'):
                    blocked.append(m)
            recommendation = 'Présenter les livrables à valider.' if review else 'Exécuter une mission disponible.' if ready else 'Examiner les blocages.' if blocked else 'Créer les missions de la phase suivante dans le périmètre validé.'
            return {'project_id': project_id, 'ready': ready, 'review': review, 'blocked': blocked, 'recommendation': recommendation}

    def status(self, project_id=None):
        with self.db() as db:
            projects = [json.loads(r[0]) for r in db.execute('SELECT data FROM projects ORDER BY rowid')]
            if project_id:
                projects = [self._get(db, 'projects', project_id)]
            missions = [m for p in projects for m in self._missions(db, p['id'])]
            events = [dict(seq=r[0], project_id=r[1], mission_id=r[2], action=r[3], detail=json.loads(r[4]), created=r[5]) for r in db.execute('SELECT * FROM events ORDER BY seq DESC LIMIT 100') if not project_id or r[1] == project_id]
            return {'projects': projects, 'missions': missions, 'events': events}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=None, help='dossier des données (défaut : wiki/projets/team-strategie/data du coffre)')
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('start'); p.add_argument('brief', type=Path)
    p = sub.add_parser('status'); p.add_argument('project', nargs='?')
    for command in ('next', 'fanout', 'bundle', 'prepare'):
        p = sub.add_parser(command); p.add_argument('project')
    for command in ('advance', 'retry', 'recover', 'run'):
        p = sub.add_parser(command); p.add_argument('mission')
    p = sub.add_parser('run-ready'); p.add_argument('project'); p.add_argument('--max-jobs', type=int, default=1); p.add_argument('--workers', type=int, default=1)
    p = sub.add_parser('add-mission'); p.add_argument('project'); p.add_argument('--role', required=True, choices=ROLES); p.add_argument('--phase', required=True); p.add_argument('--subject', type=Path); p.add_argument('--depends', nargs='+', required=True)
    p = sub.add_parser('submit'); p.add_argument('mission'); p.add_argument('result', type=Path)
    p = sub.add_parser('approve'); p.add_argument('mission'); p.add_argument('sha'); p.add_argument('--message', required=True); p.add_argument('--user-approved', action='store_true')
    p = sub.add_parser('revise'); p.add_argument('mission'); p.add_argument('--message', required=True)
    args = parser.parse_args()
    team = Team(args.root)
    try:
        if args.command == 'start': result = team.start(json.loads(args.brief.read_text(encoding='utf-8')))
        elif args.command == 'status': result = team.status(args.project)
        elif args.command in ('next', 'fanout', 'bundle', 'prepare'): result = getattr(team, args.command)(args.project)
        elif args.command in ('advance', 'retry', 'recover', 'run'): result = getattr(team, args.command)(args.mission)
        elif args.command == 'run-ready': result = team.run_ready(args.project, args.max_jobs, args.workers)
        elif args.command == 'add-mission': result = team.add_mission(args.project, args.role, args.phase, json.loads(args.subject.read_text(encoding='utf-8')) if args.subject else {}, args.depends)
        elif args.command == 'submit': result = team.submit(args.mission, json.loads(args.result.read_text(encoding='utf-8')))
        elif args.command == 'approve': result = team.approve(args.mission, args.sha, args.message, args.user_approved)
        elif args.command == 'revise': result = team.revise(args.mission, args.message)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, RuntimeError) as exc:
        parser.exit(1, str(exc) + '\n')


if __name__ == '__main__':
    main()
