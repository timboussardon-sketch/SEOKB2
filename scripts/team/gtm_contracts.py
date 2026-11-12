"""Commercial phases and the versioned handoff consumed by the SEO/GEO team."""
from datetime import date

PHASES = ('gtm-diagnostic', 'gtm-offre', 'gtm-parcours', 'gtm-transmission')
STAGES = ('discovery', 'evaluation', 'purchase', 'activation', 'retention')


def validate(task, payload):
    from contracts import require, text, strings, array, source, get_stage
    phase = task['mission']['phase']
    require(task['project']['brief'].get('workflow_version', 1) >= 4, 'Go-to-market : workflow 4 requis')
    require(payload.get('decision_status') == 'proposed', 'La proposition GTM ne peut pas se valider elle-même')
    strings(payload.get('unknowns'), 'unknowns', False)
    previous = 'cadrage' if phase == PHASES[0] else PHASES[PHASES.index(phase)-1]
    prior = get_stage(task, previous)
    previous_ids = {m['id'] for m in task['upstream'] if m['phase'] == previous}
    require(any(r['mission_id'] in previous_ids for r in payload['source_refs']), 'Référence à la phase GTM précédente requise')

    def rows(value, fields, label):
        array(value, label)
        for row in value:
            require(isinstance(row, dict), label + ' : objet requis')
            for field in fields:
                text(row.get(field), label + '.' + field)

    def unique(values, label):
        require(len(values) == len(set(values)), label + ' : identifiants dupliqués')

    if phase == 'gtm-diagnostic':
        sources = payload.get('sources')
        array(sources, 'sources', False)
        for item in sources:
            for field in ('id', 'title', 'author', 'document_date', 'consulted_at', 'scope', 'access'):
                text(item.get(field), 'source.' + field)
            date.fromisoformat(item['consulted_at'])
            source(task, item)
        source_ids = [s['id'] for s in sources]
        unique(source_ids, 'sources')
        claims = payload.get('claims')
        rows(claims, ('id', 'claim', 'status', 'limit'), 'claims')
        unique([c['id'] for c in claims], 'claims')
        for claim in claims:
            require(claim['status'] in ('observed', 'declared', 'inferred', 'hypothesis', 'missing'), 'Statut de preuve GTM invalide')
            strings(claim.get('source_ids'), 'claim.source_ids', claim['status'] in ('observed', 'declared', 'inferred'))
            require(set(claim['source_ids']).issubset(source_ids), 'Source GTM inconnue')
        rows(payload.get('research_log'), ('query', 'result', 'access'), 'research_log')
        strings(payload.get('contradictions'), 'contradictions', False)
        text(payload.get('diagnosis'), 'diagnosis')
        return

    diagnostic = get_stage(task, 'gtm-diagnostic')
    claim_ids = {c['id'] for c in diagnostic['claims']}
    if phase == 'gtm-offre':
        segments = payload.get('segments')
        rows(segments, ('id', 'offer', 'segment', 'problem', 'trigger', 'positioning', 'message', 'capacity', 'priority', 'reason'), 'segments')
        unique([s['id'] for s in segments], 'segments')
        require(any(s['priority'] == 'proposed' for s in segments), 'Au moins un segment GTM proposé requis')
        for segment in segments:
            require(segment['priority'] in ('proposed', 'deferred'), 'Priorité GTM invalide')
            for field in ('markets', 'zones', 'languages', 'alternatives', 'terms', 'exclusions', 'objections'):
                strings(segment.get(field), 'segment.' + field, field not in ('exclusions', 'objections'))
            roles = segment.get('buyer_roles')
            require(isinstance(roles, dict), 'Rôles acheteurs requis')
            for field in ('user', 'decision_maker', 'payer'):
                text(roles.get(field), 'buyer_roles.' + field)
            strings(segment.get('claim_ids'), 'segment.claim_ids')
            require(set(segment['claim_ids']).issubset(claim_ids), 'Affirmation GTM inconnue')
            price = segment.get('price')
            require(isinstance(price, dict), 'Prix GTM structuré requis')
            require(price.get('status') in ('displayed', 'paid', 'proposed', 'unknown'), 'Statut prix requis')
            text(price.get('basis'), 'Justification et source du prix')
            amount = price.get('amount')
            require(amount is None or (type(amount) in (int, float) and amount >= 0), 'Prix numérique positif ou null requis')
            require(price['status'] != 'unknown' or amount is None, 'Prix inconnu : conserver null')
            for field in ('currency', 'unit'):
                text(price.get(field), 'price.' + field)
        return

    offers = get_stage(task, 'gtm-offre')['segments']
    selected = {s['id']: s for s in offers if s['priority'] == 'proposed'}
    if phase == 'gtm-parcours':
        journey = payload.get('journey')
        rows(journey, ('gtm_id', 'stage', 'buyer_action', 'proof', 'objection', 'destination', 'next_action', 'owner', 'measure'), 'journey')
        pairs = [(j['gtm_id'], j['stage']) for j in journey]
        unique(pairs, 'journey')
        require(set(pairs) == {(sid, stage) for sid in selected for stage in STAGES}, 'Parcours complet requis pour chaque segment proposé')
        channels = payload.get('channels')
        rows(channels, ('gtm_id', 'channel', 'role', 'status', 'reason', 'message', 'proof', 'destination', 'next_action', 'measure'), 'channels')
        for c in channels:
            require(c['gtm_id'] in selected, 'Canal hors segment proposé')
            require(c['status'] in ('measured', 'observed', 'hypothesis'), 'Acquisition mesurée, présence observée ou hypothèse à distinguer')
        require({c['gtm_id'] for c in channels} == set(selected), 'Canaux incomplets pour les segments proposés')
        for field in ('bottleneck', 'capacity', 'economics', 'deferred_channels'):
            text(payload.get(field), field)
        return

    rows(payload.get('experiments'), ('id', 'gtm_id', 'hypothesis', 'method', 'metric', 'denominator', 'baseline', 'threshold', 'owner', 'capacity', 'window', 'stop_condition'), 'experiments')
    unique([e['id'] for e in payload['experiments']], 'experiments')
    for experiment in payload['experiments']:
        require(experiment['gtm_id'] in selected, 'Expérience hors segment proposé')
        require('budget_cap' in experiment, 'Plafond proposé ou null requis')
        cap = experiment['budget_cap']
        require(cap is None or (type(cap) in (int, float) and cap >= 0), 'Budget proposé positif ou null requis')
        text(experiment.get('budget_unit'), 'Devise du budget ou inconnu')
        decisions = experiment.get('decisions')
        require(isinstance(decisions, dict), 'Décisions possibles requises')
        for decision in ('continue', 'modify', 'stop', 'inconclusive'):
            text(decisions.get(decision), 'experiment.decisions.' + decision)
    handoff = payload.get('handoff')
    require(isinstance(handoff, dict), 'Transmission GTM requise')
    require(type(handoff.get('version')) is int and handoff['version'] > 0, 'Version de transmission requise')
    date.fromisoformat(handoff.get('date', ''))
    entries = handoff.get('entries')
    rows(entries, ('gtm_id', 'offer', 'segment', 'conversion', 'destination', 'seo_geo_role', 'proofs', 'limits', 'owner', 'measurement'), 'handoff.entries')
    unique([h['gtm_id'] for h in entries], 'handoff')
    require({h['gtm_id'] for h in entries} == set(selected), 'Transmission : couverture des segments proposés requise')
    for entry in entries:
        original = selected[entry['gtm_id']]
        require(all(entry[f] == original[f] for f in ('offer', 'segment')), 'Offre ou segment modifié sans révision GTM')
    rows(payload.get('roadmap'), ('action', 'owner', 'dependency', 'capacity', 'done_when'), 'roadmap')
    text(payload.get('measurement'), 'measurement')


# Compact examples describe the payload; instructions keep source truth upstream.
SCHEMAS = {
    'gtm-diagnostic': {
        'diagnosis': 'activité, maturité et lacunes', 'sources': [{'id': 'S-001', 'title': '', 'author': '', 'document_date': 'date ou inconnue', 'consulted_at': 'YYYY-MM-DD', 'scope': '', 'access': '', 'source_file': 'pièce dans le coffre ou workspace', 'excerpt': 'extrait exact'}],
        'claims': [{'id': 'F-001', 'claim': '', 'status': 'observed|declared|inferred|hypothesis|missing', 'source_ids': ['S-001'], 'limit': ''}],
        'research_log': [{'query': '', 'result': '', 'access': ''}], 'contradictions': []},
    'gtm-offre': {'segments': [{'id': 'GTM-001', 'offer': '', 'segment': '', 'markets': [''], 'zones': [''], 'languages': [''], 'buyer_roles': {'user': '', 'decision_maker': '', 'payer': ''}, 'problem': '', 'trigger': '', 'alternatives': [''], 'positioning': '', 'message': '', 'claim_ids': ['F-001'], 'price': {'status': 'unknown', 'amount': None, 'currency': 'inconnue', 'unit': 'inconnue', 'basis': 'source et portée ou lacune'}, 'terms': [''], 'capacity': 'connue ou inconnue', 'exclusions': [], 'objections': [], 'priority': 'proposed|deferred', 'reason': ''}]},
    'gtm-parcours': {'journey': [{'gtm_id': 'GTM-001', 'stage': '|'.join(STAGES), 'buyer_action': '', 'proof': '', 'objection': '', 'destination': '', 'next_action': '', 'owner': '', 'measure': ''}], 'channels': [{'gtm_id': 'GTM-001', 'channel': '', 'role': '', 'status': 'measured|observed|hypothesis', 'reason': '', 'message': '', 'proof': '', 'destination': '', 'next_action': '', 'measure': ''}], 'bottleneck': 'preuve ou inconnu', 'capacity': '', 'economics': 'formules, données, calculs exécutés ou non calculable', 'deferred_channels': ''},
    'gtm-transmission': {'experiments': [{'id': 'T-001', 'gtm_id': 'GTM-001', 'hypothesis': '', 'method': '', 'metric': '', 'denominator': '', 'baseline': 'connue ou inconnue', 'threshold': 'proposé, justifié ou à définir', 'owner': '', 'budget_cap': None, 'budget_unit': 'inconnue', 'capacity': '', 'window': '', 'stop_condition': '', 'decisions': {'continue': '', 'modify': '', 'stop': '', 'inconclusive': ''}}], 'handoff': {'version': 1, 'date': 'YYYY-MM-DD', 'entries': [{'gtm_id': 'GTM-001', 'offer': 'reprendre offre approuvée', 'segment': 'reprendre segment approuvé', 'conversion': '', 'destination': '', 'seo_geo_role': '', 'proofs': '', 'limits': '', 'owner': '', 'measurement': ''}]}, 'roadmap': [{'action': '', 'owner': '', 'dependency': '', 'capacity': '', 'done_when': ''}], 'measurement': ''},
}
for schema in SCHEMAS.values():
    schema.update(decision_status='proposed', unknowns=[])

MISSIONS = {
    'gtm-diagnostic': 'Appliquer uniquement les sections 1–2 du skill go-to-market. Rechercher dans le périmètre client, lire les pièces, dater les sources et distinguer offre, besoin exprimé, comportement et résultat. Conserver contradictions et accès manquants. Une page web se conserve comme note sourcée dans le workspace avec URL, date et extrait ; aucune écriture raw/. Réutiliser un dossier GTM existant en vérifiant sa fraîcheur et ses validations.',
    'gtm-offre': 'Appliquer les sections 3–4 : comparer les segments, leurs rôles acheteurs, alternatives, positionnement, offre et prix. Référencer les claims du diagnostic. Les choix restent proposés ; prix affiché, payé, proposé ou inconnu sont distincts. Comparer les alternatives reportées sans quota artificiel.',
    'gtm-parcours': 'Appliquer les sections 5–6 : parcours commercial de la découverte à la fidélisation pour chaque segment proposé, canaux, goulot et moyens. Les stages discovery/evaluation/purchase/activation/retention sont des clés de données ; écrire le livrable en français. Justifier l’absence éventuelle d’une action récurrente. Aucun canal SEO/GEO imposé sans justification. Exécuter les calculs possibles et conserver les autres inconnus.',
    'gtm-transmission': 'Appliquer les sections 7–8 et references/passage-seo-geo.md : expériences proposées, mesure, roadmap conditionnelle et fiche partagée versionnée. Conserver offre et segment approuvés ; référencer les phases précédentes pour rôles, marché, langues, prix, objections et moyens sans recopier ni réinventer ces données. Définir conversion et place du SEO/GEO ; une offre ou une formulation ne prouve pas la demande. Aucune expérience terrain ni transmission à une autre team lancée par cette sous-mission.',
}
