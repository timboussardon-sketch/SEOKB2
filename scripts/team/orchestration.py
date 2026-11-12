"""Deterministic strategy workflow; creation and execution never approve results."""
from concurrent.futures import ThreadPoolExecutor, as_completed


def enabled(project):
    return project['brief'].get('workflow_version', 1) in (2, 3, 4)


def key(role, phase, keyword=None):
    return (role, phase, keyword if role == 'strategie-mot-cle' else None)


def mission_key(mission):
    return key(mission['role'], mission['phase'], mission.get('subject', {}).get('keyword'))


def specifications_v2(project):
    """Complete DAG. Keyword states are separate; global work consumes all of them."""
    specs = []
    def step(role, phase, label, dependencies=(), keyword=None):
        item = dict(key=key(role, phase, keyword), role=role, phase=phase, label=label,
                    dependencies=list(dependencies), subject={'keyword': keyword} if keyword else {})
        if keyword:
            item['subject']['agent_key'] = project['id'] + ':keyword-' + str(project['brief']['keywords'].index(keyword) + 1)
        specs.append(item)
        return item['key']
    cadrage = step('pilote', 'cadrage', 'Cadrage business et périmètre')
    proofs = []
    for keyword in project['brief']['keywords']:
        previous = cadrage
        for phase in ('intentions', 'questions', 'preuves'):
            previous = step('strategie-mot-cle', phase, keyword + ' — ' + phase, [previous], keyword)
        proofs.append(previous)
    diagnostic = step('diagnostic-seo', 'diagnostic', 'Diagnostic SEO vérifié', [cadrage])
    evidence = proofs + [diagnostic]
    if project['brief']['mode'] in ('seo-geo', 'geo'):
        panel = step('visibilite-ia', 'panel', 'Panel IA et protocole de collecte', evidence)
        observation = step('visibilite-ia', 'observations', 'Observations IA et limites', [panel])
        evidence = [observation]
    opportunities = step('business', 'opportunites', 'Opportunités business et priorités', evidence)
    architecture = step('architecture-roadmap', 'architecture', 'Architecture et destinations', [opportunities])
    roadmap = step('architecture-roadmap', 'roadmap', 'Roadmap commune, distribution et mesure', [architecture])
    synthesis = step('pilote', 'synthese', 'Stratégie client consolidée', [roadmap])
    step('qualite', 'controle', 'Contrôle qualité du dossier final', [synthesis])
    return specs


def portfolio(project, missions, approved_only=False):
    if project['brief'].get('workflow_version', 1) < 3:
        return project['brief']['keywords']
    selected = next((m for m in missions if m['role'] == 'business' and m['phase'] == 'priorisation'), None)
    if selected and selected['status'] == 'approved':
        return selected['result']['stage_payload']['keywords']
    if approved_only:
        raise ValueError('Stratégie globale puis priorisation validées requises avant les agents mot-clé.')
    # Keep the existing graph visible while a priorisation is being corrected.
    starts = [m for m in missions if m['role'] == 'strategie-mot-cle' and m['phase'] == 'intentions']
    return [m['subject']['keyword'] for m in starts]


def check_portfolio_revision(project, missions, mission, result):
    if project['brief'].get('workflow_version', 1) < 3 or mission['phase'] != 'priorisation' or result['status'] != 'review':
        return
    proposed = result.get('stage_payload', {}).get('keywords')
    if not isinstance(proposed, list) or not 5 <= len(proposed) <= 10 or any(not isinstance(k, str) or not k.strip() or k != ' '.join(k.split()) for k in proposed):
        raise ValueError('Priorisation : 5 à 10 mots-clés business distincts et normalisés sont requis.')
    if len(set(k.casefold() for k in proposed)) != len(proposed):
        raise ValueError('Priorisation : mots-clés dupliqués.')
    existing = [m['subject']['keyword'] for m in missions if m['role'] == 'strategie-mot-cle' and m['phase'] == 'intentions']
    if existing and proposed != existing:
        raise ValueError('Le portefeuille a déjà des agents : ouvrir un nouveau projet pour changer les mots-clés ou leur ordre ; historique conservé.')


def specifications(project, missions=()):
    if project['brief'].get('workflow_version', 1) < 3:
        return specifications_v2(project)
    selected = portfolio(project, missions)
    specs = []
    def step(role, phase, label, dependencies=(), keyword=None):
        subject = {'keyword': keyword, 'agent_key': project['id'] + ':keyword-' + str(selected.index(keyword) + 1)} if keyword else {}
        if role == 'go-to-market':
            subject['agent_key'] = project['id'] + ':go-to-market'
        item = dict(key=key(role, phase, keyword), role=role, phase=phase, label=label,
                    dependencies=list(dependencies), subject=subject)
        specs.append(item)
        return item['key']
    cadrage = step('pilote', 'cadrage', 'Cadrage business et périmètre')
    commercial = cadrage
    if project['brief'].get('workflow_version', 1) >= 4:
        for phase, label in (
            ('gtm-diagnostic', 'Go-to-market — diagnostic commercial et preuves'),
            ('gtm-offre', 'Go-to-market — segments, positionnement et offre'),
            ('gtm-parcours', 'Go-to-market — parcours, canaux et moyens'),
            ('gtm-transmission', 'Go-to-market — tests, mesure et cadrage SEO/GEO'),
        ):
            commercial = step('go-to-market', phase, label, [commercial])
    diagnostic = step('diagnostic-seo', 'diagnostic', 'Diagnostic SEO vérifié', [commercial])
    exploration = step('recherche', 'exploration', 'Exploration du marché et des besoins acheteurs', [commercial])
    evidence = [diagnostic, exploration]
    if project['brief']['mode'] in ('seo-geo', 'geo'):
        panel = step('visibilite-ia', 'panel', 'Panel IA et protocole de collecte', evidence)
        observations = step('visibilite-ia', 'observations', 'Observations IA et limites', [panel])
        evidence = [observations]
    opportunities = step('business', 'opportunites', 'Opportunités business et conditions', evidence)
    architecture = step('architecture-roadmap', 'architecture', 'Architecture du site et destinations', [opportunities])
    roadmap = step('architecture-roadmap', 'roadmap', 'Roadmap globale, distribution et mesure', [architecture])
    strategy = step('pilote', 'strategie-globale', 'Stratégie SEO/GEO complète', [roadmap])
    selection = step('business', 'priorisation', 'Sélection des 5 à 10 mots-clés business prioritaires', [strategy])
    proofs = []
    for keyword in selected:
        previous = selection
        for phase in ('intentions', 'questions', 'preuves'):
            previous = step('strategie-mot-cle', phase, keyword + ' — ' + phase, [previous], keyword)
        proofs.append(previous)
    consolidation = step('architecture-roadmap', 'consolidation', 'Consolidation des stratégies mot-clé et roadmap affinée', proofs or [selection])
    step('qualite', 'controle', 'Contrôle qualité du dossier final', [consolidation])
    return specs


def indexed(project, missions):
    specs = {s['key']: s for s in specifications(project, missions)}
    found = {}
    for m in missions:
        identity = mission_key(m)
        if identity not in specs:
            raise ValueError('Mission hors workflow : ' + m['phase'])
        if identity in found:
            raise ValueError('Mission dupliquée dans le workflow : ' + m['phase'])
        found[identity] = m
    return specs, found


def check_mission(team, db, mission):
    project = team._get(db, 'projects', mission['project_id'])
    if not enabled(project):
        return
    specs, found = indexed(project, team._missions(db, mission['project_id']))
    identity = mission_key(mission)
    if identity not in specs:
        raise ValueError('Mission hors workflow.')
    spec = specs[identity]
    if mission['role'] in ('strategie-mot-cle', 'go-to-market') and mission['subject'].get('agent_key') != spec['subject']['agent_key']:
        raise ValueError('Identité d’agent invalide.')
    if any(dep not in found for dep in spec['dependencies']):
        raise ValueError('Phase créée avant ses prérequis.')
    expected = {found[dep]['id'] for dep in spec['dependencies']}
    # Compatibility: the original standalone consolidation explicitly added proofs.
    actual = set(mission['depends'])
    if actual != expected:
        raise ValueError('Dépendances non conformes au workflow : ' + mission['phase'])


def prepare(team, project_id):
    created = []
    with team.db() as db:
        project = team._get(db, 'projects', project_id)
        if not enabled(project):
            raise ValueError('Workflow historique : pas de migration implicite ; utiliser ses commandes dédiées.')
        specs, found = indexed(project, team._missions(db, project_id))
        for spec in specs.values():
            if spec['key'] in found:
                continue
            dependencies = [found.get(dep) for dep in spec['dependencies']]
            if any(dep is None or dep['status'] != 'approved' for dep in dependencies):
                continue
            # Hash/file integrity and recursive approval checks occur before creation.
            for dep in dependencies:
                team._approved(db, dep['id'])
            item = team._new(db, project_id, spec['role'], spec['phase'], spec['subject'],
                             [dep['id'] for dep in dependencies])
            found[spec['key']] = item
            created.append(item)
    return {'project_id': project_id, 'created': created, 'next': inspect(team, project_id)}


def inspect(team, project_id):
    """Pure query over state, including future phases; never creates or approves."""
    with team.db() as db:
        project = team._get(db, 'projects', project_id)
        specs, found = indexed(project, team._missions(db, project_id))
        ready, review, blocked, running, planned = [], [], [], [], []
        for identity, spec in specs.items():
            m = found.get(identity)
            if m is None:
                pending = []
                for dep in spec['dependencies']:
                    prior = found.get(dep)
                    if prior is None or prior['status'] != 'approved':
                        pending.append(specs[dep]['label'])
                    else:
                        try:
                            team._approved(db, prior['id'])
                        except ValueError as exc:
                            pending.append(str(exc))
                planned.append({'role': spec['role'], 'phase': spec['phase'], 'subject': spec['subject'],
                                'label': spec['label'], 'waiting_for': pending,
                                'can_prepare': not pending})
                continue
            named = dict(m, label=spec['label'])
            if m['status'] == 'queued':
                try:
                    team._ready(db, m)
                    ready.append(named)
                except ValueError as exc:
                    blocked.append(dict(named, blocking_reason=str(exc)))
            elif m['status'] == 'review':
                review.append(named)
            elif m['status'] == 'running':
                running.append(named)
            elif m['status'] in ('blocked', 'failed'):
                blocked.append(named)
            elif m['status'] == 'approved':
                try:
                    team._approved(db, m['id'])
                except ValueError as exc:
                    blocked.append(dict(named, blocking_reason=str(exc)))
        complete = False
        final = found.get(key('qualite', 'controle'))
        if final and final['status'] == 'approved' and not (ready or review or blocked or running or planned):
            try:
                team._approved(db, final['id'])
                team._bundle(db, project_id)
                team._validate_stage(db, final, final['result'])
                verdict = final['result'].get('stage_payload', {}).get('verdict')
                complete = verdict == 'conforme'
                if not complete:
                    blocked.append(dict(final, blocking_reason='Le contrôle qualité final ne déclare pas le dossier conforme.'))
            except ValueError as exc:
                blocked.append(dict(final, blocking_reason=str(exc)))
        labels = lambda items: ', '.join(m.get('label', m['phase']) for m in items)
        if review:
            recommendation = 'Présenter pour validation : ' + labels(review)
        elif ready:
            recommendation = 'Exécuter les missions disponibles : ' + labels(ready)
        elif running:
            recommendation = 'Attendre les missions en cours : ' + labels(running)
        elif complete:
            recommendation = 'Stratégie et contrôle final validés. Présenter le dossier ; aucune publication autorisée par cet état.'
        elif any(p['can_prepare'] for p in planned):
            recommendation = 'Préparer : ' + labels([p for p in planned if p['can_prepare']])
        elif blocked:
            recommendation = 'Résoudre les blocages : ' + labels(blocked)
        else:
            recommendation = 'Les prochaines phases attendent les validations de leurs prérequis.'
        return dict(project_id=project_id, ready=ready, review=review, blocked=blocked,
                    running=running, planned=planned, complete=complete, recommendation=recommendation,
                    keyword_portfolio=portfolio(project, list(found.values())),
                    keyword_agents_after='strategie-globale et priorisation validées' if project['brief'].get('workflow_version', 1) >= 3 else 'cadrage validé')


def run_ready(team, project_id, max_jobs=1, workers=1, provider=None):
    if isinstance(max_jobs, bool) or not isinstance(max_jobs, int) or not 1 <= max_jobs <= 20:
        raise ValueError('max_jobs doit être compris entre 1 et 20.')
    if isinstance(workers, bool) or not isinstance(workers, int) or not 1 <= workers <= 3:
        raise ValueError('workers doit être compris entre 1 et 3.')
    prepare(team, project_id)
    # Snapshot once: results from this wave cannot admit another phase in this call.
    snapshot = inspect(team, project_id)['ready'][:max_jobs]
    results, errors = [], []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(team.run, m['id'], provider): m['id'] for m in snapshot}
        for future in as_completed(futures):
            identity = futures[future]
            try:
                results.append(future.result())
            except Exception as exc:
                errors.append({'mission_id': identity, 'error': str(exc)[:600]})
    return dict(project_id=project_id, attempted=[m['id'] for m in snapshot], results=results,
                errors=errors, next=inspect(team, project_id))
