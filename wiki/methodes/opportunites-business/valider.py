"""Validate structure, references, units and human approvals before calculation.

Usage: .venv/bin/python valider.py dossier.json
Dependency: jsonschema (already present in seo-kb/.venv).
Does not verify truth of source material or approve any business decision.
"""
import argparse
import datetime as dt
from decimal import Decimal
import json
import sys
from urllib.parse import urldefrag, urlsplit

from jsonschema import Draft202012Validator, FormatChecker
from common import ROOT, dump, effective_validation, fingerprint, load

COLLECTIONS = ('scopes', 'offers', 'sources', 'metrics', 'needs', 'groups', 'actors',
               'actions', 'opportunities', 'scenarios', 'aggregates', 'panels')
FUNNEL_QUANTITIES = {'traffic': ('sessions', 'sessions'),
                     'qualified_lead_rate': ('qualified_lead_rate', 'qualified_leads/session'),
                     'closing_rate': ('closing_rate', 'clients/qualified_lead'),
                     'revenue_per_client': ('revenue_per_client', '{currency}/client'),
                     'variable_cost_per_client': ('variable_cost_per_client', '{currency}/client')}


def validate(data):
    errors, warnings = [], []
    def fail(where, message): errors.append({'path': where, 'message': message})
    schema = load(ROOT / 'schema.json')
    Draft202012Validator.check_schema(schema)
    for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data):
        fail('/' + '/'.join(map(str, error.absolute_path)), error.message)
    if errors:
        return {'valid': False, 'errors': errors, 'warnings': [], 'content_sha256': None}

    digest = fingerprint(data)
    indexes = {}
    for name in COLLECTIONS:
        indexes[name] = {}
        for value in data[name]:
            if value['id'] in indexes[name]: fail(name, 'Identifiant dupliqué : ' + value['id'])
            indexes[name][value['id']] = value

    def refs(values, collection, where):
        if len(values) != len(set(values)): fail(where, 'Référence dupliquée.')
        for value in values:
            if value not in indexes[collection]: fail(where, 'Référence inconnue : ' + str(value))

    def walk(value, path=''):
        if isinstance(value, dict):
            if 'source_ids' in value:
                refs(value['source_ids'], 'sources', path + '/source_ids')
            if 'scope_id' in value:
                refs([value['scope_id']], 'scopes', path + '/scope_id')
            if set(value) == {'start', 'end'} and value['end'] < value['start']:
                fail(path, 'Période inversée.')
            if 'validation' in value:
                v = value['validation']
                if v['status'] == 'approved':
                    if any(v[k] is None for k in ('reviewer', 'date', 'message', 'content_sha256')):
                        fail(path + '/validation', 'Accord incomplet : auteur, date, message et empreinte requis.')
                    elif effective_validation(v, digest) == 'needs_revision':
                        warnings.append({'path': path + '/validation', 'message': 'Accord périmé : contenu modifié ; statut effectif needs_revision.'})
            for key, child in value.items(): walk(child, path + '/' + key)
        elif isinstance(value, list):
            for i, child in enumerate(value): walk(child, path + '/' + str(i))
    walk(data)
    for source in data['sources']:
        if source['kind'] == 'fixture' and data['dataset_kind'] != 'synthetic_test':
            fail('sources/' + source['id'], 'Source fictive interdite dans un dossier réel ou documentaire.')
    for scope in data['scopes']: refs(scope['offer_ids'], 'offers', scope['id'])
    metrics = indexes['metrics']
    for m in data['metrics']:
        path = 'metrics/' + m['id']
        if (m['status'] == 'unavailable') != (m['value'] is None):
            fail(path, 'Une valeur absente exige unavailable ; une donnée disponible exige une valeur.')
        if m['status'] in ('observed', 'estimated') and not m['source_ids']:
            fail(path, 'Source obligatoire pour une mesure ou estimation.')
        if m['status'] == 'hypothesis' and not m['author']:
            fail(path, 'Auteur obligatoire pour une hypothèse.')
        if m['value'] is not None and not Decimal(str(m['value'])).is_finite():
            fail(path, 'Valeur non finie.')
        if m['quantity'] in ('qualified_lead_rate', 'closing_rate') and m['value'] is not None and m['value'] > 1:
            fail(path, 'Un taux doit être entre 0 et 1.')
        expected_units = {'search_volume':'searches/month', 'gsc_clicks':'clicks', 'gsc_impressions':'impressions',
                          'sessions':'sessions', 'qualified_lead_rate':'qualified_leads/session',
                          'closing_rate':'clients/qualified_lead', 'client_capacity':'clients',
                          'production_capacity':'hours/week', 'effort':'hours', 'client_questions':'questions',
                          'ia_citations':'citations'}
        if m['quantity'] in expected_units and m['unit'] != expected_units[m['quantity']]:
            fail(path, 'Unité incompatible avec la quantité.')
        if m['quantity'] in ('revenue_per_client', 'variable_cost_per_client', 'investment_cost'):
            expected = (m['currency'] or '') + ('/client' if m['quantity'] != 'investment_cost' else '')
            if m['currency'] is None or m['unit'] != expected: fail(path, 'Devise/unité monétaire obligatoire.')
        elif m['currency'] is not None:
            fail(path, 'Devise inattendue pour une donnée non monétaire.')
        expected_channel = {'search_volume':'google_search','gsc_clicks':'google_search','gsc_impressions':'google_search',
                            'sessions':'analytics','qualified_lead_rate':'analytics','closing_rate':'crm',
                            'client_questions':'client_exchange','ia_citations':'ia'}
        if m['quantity'] in expected_channel and m['channel'] != expected_channel[m['quantity']]:
            fail(path, 'Canal incompatible avec la quantité ; aucune conversion IA → trafic.')

    for n in data['needs']:
        refs(n['metric_ids'], 'metrics', n['id'])
        if n['kind'] == 'measured_search' and not any(metrics.get(i, {}).get('quantity') in
                ('search_volume','gsc_clicks','gsc_impressions') and metrics.get(i, {}).get('status') in
                ('observed','estimated') for i in n['metric_ids']):
            fail(n['id'], 'Demande de recherche mesurée sans mesure de recherche.')
    for g in data['groups']:
        refs(g['need_ids'], 'needs', g['id'])
        if g['method'] == 'serp_overlap' and g['serp_evidence'] is None:
            fail(g['id'], 'Regroupement SERP sans preuve de comparaison.')
        if g['method'] == 'serp_overlap' and g['serp_evidence'] is not None:
            evidence=g['serp_evidence']
            rows=evidence['results_by_need']
            if len(rows)!=len(g['need_ids']) or {x['need_id'] for x in rows}!=set(g['need_ids']):
                fail(g['id'], 'Un relevé SERP par besoin du groupe est requis.')
            for row in rows:
                need=indexes['needs'].get(row['need_id'])
                if need and need['scope_id']!=evidence['scope_id']:
                    fail(g['id'], 'Comparaison SERP entre périmètres incompatibles.')
                normalized=[urldefrag(u)[0] for u in row['urls']]
                if len(normalized)!=len(set(normalized)) or len(normalized)>evidence['depth']:
                    fail(g['id'], 'URL SERP dupliquée ou profondeur dépassée.')
                if any(urlsplit(u).scheme not in ('http','https') or not urlsplit(u).netloc for u in normalized):
                    fail(g['id'], 'URL de résultat SERP invalide.')
                for sid in row['source_ids']:
                    if sid in indexes['sources'] and indexes['sources'][sid]['kind'] not in ('serp','fixture'):
                        fail(g['id'], 'Source de relevé SERP requise pour la comparaison.')

    capid = data['production_capacity_id']
    if capid is not None: refs([capid], 'metrics', 'production_capacity_id')
    cap = metrics.get(capid)
    if cap and cap['quantity'] != 'production_capacity': fail('production_capacity_id', 'Capacité de production attendue.')
    actions = indexes['actions']
    for a in data['actions']:
        refs(a['dependencies'], 'actions', a['id'])
        for field, quantity in [('effort_metric_id','effort'), ('cost_metric_id','investment_cost')]:
            if a[field] is not None:
                refs([a[field]], 'metrics', a['id'])
                if a[field] in metrics and metrics[a[field]]['quantity'] != quantity:
                    fail(a['id'], 'Quantité incorrecte pour ' + field)
        if a['status'] in ('approved','done') and a['validation']['status'] != 'approved':
            fail(a['id'], 'Action approuvée/terminée sans accord explicite conservé.')
        if a['planned_date'] is not None:
            if cap is None or cap['value'] is None or cap['value'] <= 0:
                fail(a['id'], 'Date planifiée sans capacité positive connue.')
            if not a['date_basis_source_ids']: fail(a['id'], 'Date planifiée sans origine.')
        refs(a['date_basis_source_ids'], 'sources', a['id'])
    visiting, seen = set(), set()
    def visit(i):
        if i in visiting: fail(i, 'Dépendance cyclique.'); return
        if i in seen or i not in actions: return
        visiting.add(i)
        for dependency in actions[i]['dependencies']: visit(dependency)
        visiting.remove(i); seen.add(i)
    for i in actions: visit(i)

    for o in data['opportunities']:
        for field, collection in [('need_ids','needs'),('group_ids','groups'),('actor_ids','actors'),
                                   ('action_ids','actions'),('scenario_ids','scenarios')]: refs(o[field], collection, o['id'])
        refs([o['offer_id']], 'offers', o['id'])
        if o['scope_id'] in indexes['scopes'] and o['offer_id'] not in indexes['scopes'][o['scope_id']]['offer_ids']:
            fail(o['id'], 'Offre hors du périmètre.')
        for gate in o['gates'].values():
            if gate['status'] == 'satisfied' and not gate['source_ids']: fail(o['id'], 'Porte satisfaite sans preuve.')
        if o['decision'] == 'retain' and any(g['status'] != 'satisfied' for g in o['gates'].values()):
            fail(o['id'], 'Retenir exige les trois portes satisfaites ; sinon investiguer ou reporter.')
        baseline = o['measurement']['baseline_metric_id']
        if baseline is not None: refs([baseline], 'metrics', o['id'])

    for s in data['scenarios']:
        refs(s['opportunity_ids'], 'opportunities', s['id'])
        refs(s['requires_action_ids'], 'actions', s['id'])
        for side in ('current','future'):
            for key, metric_id in s[side].items():
                if metric_id is None: continue
                refs([metric_id], 'metrics', s['id'])
                m = metrics.get(metric_id)
                if not m: continue
                quantity, unit = FUNNEL_QUANTITIES[key]
                if m['quantity'] != quantity or m['unit'] != unit.format(currency=s['currency']):
                    fail(s['id'], 'Quantité/unité incompatible pour ' + side + '.' + key)
                if m['scope_id'] != s['scope_id']: fail(s['id'], 'Paramètre hors périmètre : ' + metric_id)
                if side == 'future' and key in ('revenue_per_client','variable_cost_per_client') and m['period'] != s['horizon']:
                    fail(s['id'], 'Valeur par client non définie sur l’horizon du scénario.')
                if key == 'traffic':
                    if side == 'future' and m['period'] != s['horizon']: fail(s['id'], 'Trafic futur hors horizon.')
                    days = lambda p: (dt.date.fromisoformat(p['end']) - dt.date.fromisoformat(p['start'])).days
                    if side == 'current' and days(m['period']) != days(s['horizon']):
                        fail(s['id'], 'Périodes actuelle/future de durées différentes : normalisation explicite requise.')
        for key, quantity, unit in [('investment_cost_id','investment_cost',s['currency']),
                                     ('client_capacity_id','client_capacity','clients')]:
            mid = s[key]
            if mid is None: continue
            refs([mid], 'metrics', s['id']); m = metrics.get(mid)
            if m and (m['quantity'] != quantity or m['unit'] != unit or m['scope_id'] != s['scope_id'] or m['period'] != s['horizon']):
                fail(s['id'], 'Coût/capacité incompatible avec périmètre, unité ou horizon.')
        for oid in s['opportunity_ids']:
            o = indexes['opportunities'].get(oid)
            if o and (s['id'] not in o['scenario_ids'] or o['scope_id'] != s['scope_id']):
                fail(s['id'], 'Lien scénario/opportunité non réciproque ou hors périmètre.')
    for o in data['opportunities']:
        for sid in o['scenario_ids']:
            if sid in indexes['scenarios'] and o['id'] not in indexes['scenarios'][sid]['opportunity_ids']:
                fail(o['id'], 'Lien opportunité/scénario non réciproque.')
    for a in data['aggregates']:
        refs(a['metric_ids'], 'metrics', a['id'])
        if a['independence'] == 'documented_disjoint' and not a['source_ids']:
            fail(a['id'], 'Indépendance des mesures sans source.')

    for panel in data['panels']:
        refs(panel['actor_ids'], 'actors', panel['id'])
        scope=indexes['scopes'].get(panel['scope_id'])
        if scope and (panel['country'] not in scope['countries'] or panel['language'] not in scope['languages']):
            fail(panel['id'], 'Pays/langue du panel hors périmètre.')
        if panel['kind'] == 'serp' and panel['top_n'] is None: fail(panel['id'], 'Profondeur SERP absente.')
        questions = {q['id']:q for q in panel['questions']}
        if len(questions) != len(panel['questions']): fail(panel['id'], 'Question dupliquée.')
        for q in panel['questions']: refs([q['need_id']], 'needs', panel['id'])
        response_ids = set()
        for r in panel['responses']:
            if r['id'] in response_ids: fail(panel['id'], 'Réponse/relevé dupliqué : ' + r['id'])
            response_ids.add(r['id'])
            if r['question_id'] not in questions: fail(panel['id'], 'Question inconnue dans un relevé.')
            if not panel['period']['start'] <= r['date'] <= panel['period']['end']:
                fail(panel['id'], 'Relevé hors période du panel.')
            actors = [d['actor_id'] for d in r['detections']]
            if r['status'] == 'error':
                if not r['error'] or actors: fail(panel['id'], 'Échec : motif requis et aucune détection.')
                continue
            if r['error'] is not None: fail(panel['id'], 'Un relevé valide ne porte pas de motif d’échec.')
            if len(actors) != len(set(actors)) or set(actors) != set(panel['actor_ids']):
                fail(panel['id'], 'Chaque acteur évalué doit apparaître une fois, absence explicitement false/null.')
            for d in r['detections']:
                if d['recommended'] is True and d['mentioned'] is not True: fail(panel['id'], 'Recommandation sans mention.')
                if any(d[k] is True for k in ('mentioned','cited','recommended')) and (not d['source_ids'] or not d['excerpt']):
                    fail(panel['id'], 'Présence positive sans source et extrait.')
                if d['cited'] is True and not d['urls']: fail(panel['id'], 'Citation sans URL.')
                if panel['kind'] == 'serp':
                    if d['mentioned'] is True and (d['position'] is None or d['position'] > panel['top_n'] or not d['urls']):
                        fail(panel['id'], 'Présence SERP sans URL/position dans la profondeur contrôlée.')
                    if d['cited'] is not None or d['recommended'] is not None: fail(panel['id'], 'Une SERP ne constitue pas une recommandation IA.')
    for field, collection in [('explored_need_ids','needs'),('retained_opportunity_ids','opportunities'),('priority_order','opportunities')]:
        refs(data[field], collection, field)
    if set(data['priority_order']) != set(data['retained_opportunity_ids']):
        fail('priority_order', 'L’ordre doit couvrir exactement les opportunités retenues.')
    for oid in data['retained_opportunity_ids']:
        if indexes['opportunities'].get(oid, {}).get('decision') != 'retain': fail(oid, 'Opportunité retenue avec un autre verdict.')
    for o in data['opportunities']:
        if not set(o['need_ids']).issubset(set(data['explored_need_ids'])): fail(o['id'], 'Besoin hors périmètre exploré.')
    return {'valid': not errors, 'errors': errors, 'warnings': warnings, 'content_sha256': digest}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    args = parser.parse_args()
    try:
        result = validate(load(args.input))
        print(dump(result), end='')
        return 0 if result['valid'] else 2
    except (ValueError, OSError) as error:
        print(dump({'valid':False,'errors':[str(error)]}), end=''); return 2


if __name__ == '__main__':
    sys.exit(main())
