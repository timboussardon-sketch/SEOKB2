"""Deterministic common calculations; no network, collection or inferred inputs.

Usage: .venv/bin/python calculer.py dossier.json [--output new-result.json]
Decimal values in results are strings, preserving precision. Unknowns stay null.
"""
import argparse
import hashlib
import sys
from decimal import Decimal, localcontext
from pathlib import Path
from itertools import combinations
from urllib.parse import urldefrag

from common import VERSION, artifact_hashes, dump, effective_validation, load, write_output
from valider import validate


def cell(value, unit, formula, metric_ids=(), missing=(), status='estimated'):
    return {'value': value, 'unit': unit, 'status': status if value is not None else 'unavailable',
            'formula': formula, 'metric_ids': sorted(set(metric_ids)),
            'missing': sorted(set(missing)),
            'message': None if value is not None else 'non estimable avec les données disponibles'}


def operation(formula, inputs, fn, unit):
    ids = [i for x in inputs for i in x['metric_ids']]
    missing = [m for x in inputs for m in x['missing']]
    value = None if any(x['value'] is None for x in inputs) else fn(*[x['value'] for x in inputs])
    return cell(value, unit, formula, ids, missing)


def calculate(data):
    checked = validate(data)
    if not checked['valid']:
        raise ValueError(dump(checked))
    with localcontext() as context:
        context.prec = 40
        return _calculate(data, checked)


def _calculate(data, checked):
    digest = checked['content_sha256']
    metrics = {m['id']: m for m in data['metrics']}
    actions = {a['id']: a for a in data['actions']}

    def param(mid, unit, role):
        if mid is None:
            return cell(None, unit, 'input', missing=[role])
        m = metrics[mid]
        value = Decimal(str(m['value'])) if m['value'] is not None else None
        return cell(value, unit, 'input', [mid], [] if value is not None else [mid], m['status'])

    def funnel(parameters, currency, prefix):
        traffic = param(parameters['traffic'], 'sessions', prefix + '.traffic')
        qualification = param(parameters['qualified_lead_rate'], 'qualified_leads/session', prefix + '.qualified_lead_rate')
        closing = param(parameters['closing_rate'], 'clients/qualified_lead', prefix + '.closing_rate')
        revenue_unit = param(parameters['revenue_per_client'], currency + '/client', prefix + '.revenue_per_client')
        variable_unit = param(parameters['variable_cost_per_client'], currency + '/client', prefix + '.variable_cost_per_client')
        leads = operation('traffic * qualified_lead_rate', [traffic, qualification], lambda t,q:t*q, 'qualified_leads')
        clients = operation('qualified_leads * closing_rate', [leads, closing], lambda l,r:l*r, 'clients')
        revenue = operation('clients * revenue_per_client', [clients, revenue_unit], lambda c,r:c*r, currency)
        variable_cost = operation('clients * variable_cost_per_client', [clients, variable_unit], lambda c,v:c*v, currency)
        contribution = operation('revenue - delivery_variable_cost', [revenue, variable_cost], lambda r,v:r-v, currency)
        return {'traffic':traffic,'qualified_leads':leads,'clients':clients,'revenue':revenue,
                'delivery_variable_cost':variable_cost,'contribution_before_investment':contribution}

    scenarios = []
    for s in data['scenarios']:
        currency = s['currency']
        current = funnel(s['current'], currency, 'current')
        future = funnel(s['future'], currency, 'future')
        capacity = param(s['client_capacity_id'], 'clients', 'client_capacity')
        clients_realizable = operation('min(potential_clients, client_capacity)', [future['clients'],capacity], min, 'clients')
        unserved = operation('potential_clients - deliverable_clients', [future['clients'],clients_realizable], lambda p,r:p-r, 'clients')
        revenue_unit = param(s['future']['revenue_per_client'], currency+'/client', 'future.revenue_per_client')
        variable_unit = param(s['future']['variable_cost_per_client'], currency+'/client', 'future.variable_cost_per_client')
        realized_revenue = operation('deliverable_clients * revenue_per_client', [clients_realizable,revenue_unit], lambda c,r:c*r, currency)
        realized_cost = operation('deliverable_clients * variable_cost_per_client', [clients_realizable,variable_unit], lambda c,v:c*v, currency)
        deliverable = {'clients':clients_realizable,'revenue':realized_revenue,'delivery_variable_cost':realized_cost,
                       'contribution_before_investment': operation('revenue - delivery_variable_cost', [realized_revenue,realized_cost], lambda r,c:r-c, currency)}
        investment = param(s['investment_cost_id'], currency, 'investment_cost')
        if s['model'] == 'full_funnel':
            delta = {k:operation('future.'+k+' - current.'+k, [v,current[k]], lambda f,c:f-c, v['unit']) for k,v in future.items()}
            delta_deliverable = {k:operation('deliverable.'+k+' - current.'+k, [v,current[k]], lambda f,c:f-c, v['unit']) for k,v in deliverable.items()}
        else:
            delta = dict(future)
            delta_deliverable = dict(deliverable)
        for block in (delta, delta_deliverable):
            block['contribution_after_investment'] = operation(
                'incremental_contribution_before_investment - incremental_investment_cost',
                [block['contribution_before_investment'], investment], lambda m,c:m-c, currency)
        blockers = [a for a in s['requires_action_ids'] if actions[a]['status'] != 'done' or
                    effective_validation(actions[a]['validation'],digest) != 'approved']
        approval = effective_validation(s['validation'],digest)
        scenarios.append({'id':s['id'],'name':s['name'],'model':s['model'],'opportunity_ids':s['opportunity_ids'],
                          'scope_id':s['scope_id'],'horizon':s['horizon'],'currency':currency,
                          'validation':approval,'conditional_on_action_ids':blockers,
                          'basis':'Hypothèse conditionnelle, jamais un résultat commercial observé.',
                          'traffic_meaning':'additional_sessions' if s['model']=='acquisition_only' else 'future_total_sessions',
                          'capacity_meaning':'additional_clients_on_horizon' if s['model']=='acquisition_only' else 'total_clients_on_horizon',
                          'capacity_status':capacity['status'], 'current':current,'future_potential':future,
                          'future_deliverable':deliverable,'unserved_clients':unserved,
                          'incremental_potential':delta,'incremental_deliverable':delta_deliverable,
                          'investment_cost':investment,'transfer_rationale':s['transfer_rationale'],
                          'revenue_basis':s['revenue_basis'],'cost_basis':s['cost_basis']})

    aggregates = []
    for a in data['aggregates']:
        rows = [metrics[i] for i in a['metric_ids']]
        sig = lambda m:(m['quantity'],m['unit'],m['channel'],m['scope_id'],m['period']['start'],m['period']['end'],m['currency'])
        reasons = []
        unique = {}
        for m in rows:
            key = m['counting_key']
            if key is None: reasons.append('counting_key absent : ' + m['id']); continue
            if key in unique and (m['value'] != unique[key]['value'] or sig(m) != sig(unique[key])):
                reasons.append('Mesures contradictoires pour la même unité : ' + key)
            else: unique[key] = m
        if len({sig(m) for m in rows}) != 1:
            reasons.append('Quantités, canaux, périmètres, périodes ou unités incompatibles.')
        if any(m['value'] is None for m in rows): reasons.append('Au moins une valeur est indisponible.')
        if len(unique) > 1 and a['independence'] != 'documented_disjoint':
            reasons.append('Chevauchement non résolu : total non calculable.')
        if any(m['quantity'] in ('qualified_lead_rate','closing_rate','revenue_per_client','variable_cost_per_client') for m in rows):
            reasons.append('Un taux ou une valeur par client ne s’additionne pas.')
        value = None if reasons else sum((Decimal(str(m['value'])) for m in unique.values()), Decimal(0))
        aggregates.append({'id':a['id'],'result':cell(value,rows[0]['unit'] if len({sig(m) for m in rows})==1 else 'incompatible',
                          'sum(distinct counting_key) on documented disjoint measurements',a['metric_ids'],reasons),
                          'input_rows':len(rows),'unique_counting_keys':len(unique),
                          'duplicates_not_added':sum(m['counting_key'] is not None for m in rows)-len(unique),'source_ids':a['source_ids'],
                          'rationale':a['rationale']})

    group_checks = []
    for g in data['groups']:
        comparisons=[]
        if g['method']=='serp_overlap':
            evidence=g['serp_evidence']
            for left,right in combinations(evidence['results_by_need'],2):
                a={urldefrag(u)[0] for u in left['urls']};b={urldefrag(u)[0] for u in right['urls']}
                comparisons.append({'left_need_id':left['need_id'],'right_need_id':right['need_id'],
                    'shared_urls':sorted(a&b),'shared_count':len(a&b),'left_count':len(a),'right_count':len(b),
                    'requested_depth':evidence['depth'],'source_ids':sorted(set(left['source_ids']+right['source_ids']))})
        group_checks.append({'id':g['id'],'method':g['method'],
             'serp_observed':g['method']=='serp_overlap','comparisons':comparisons,
             'validation':effective_validation(g['validation'],digest),
             'note':'Un recouvrement observé ne valide pas automatiquement l’intention ni une nouvelle page.'})
    panels = []
    for p in data['panels']:
        by_question = []
        for q in p['questions']:
            responses = [r for r in p['responses'] if r['question_id']==q['id']]
            valid = [r for r in responses if r['status']=='valid']
            actor_results = []
            for actor in p['actor_ids']:
                ds = [(r,next(d for d in r['detections'] if d['actor_id']==actor)) for r in valid]
                rates = {}
                for field in ('mentioned','cited','recommended') if p['kind']=='ia' else ('mentioned',):
                    known = [(r,d) for r,d in ds if d[field] is not None]
                    numerator = sum(d[field] is True for r,d in known)
                    denominator = len(known)
                    rates[field] = {'numerator':numerator,'denominator':denominator,
                        'value':Decimal(numerator)/Decimal(denominator) if denominator else None,
                        'status':'observed' if denominator else 'unavailable',
                        'formula':'positive valid responses / valid responses assessed for '+field,
                        'unit':'ratio','unknown_excluded':len(ds)-denominator,
                        'response_ids':[r['id'] for r,d in known]}
                # Share of voice only on responses where all monitored actors were evaluated.
                complete = [r for r in valid if all(d['mentioned'] is not None for d in r['detections'])]
                pairs = sum(d['mentioned'] is True for r in complete for d in r['detections'])
                actor_pairs = sum(d['actor_id']==actor and d['mentioned'] is True for r in complete for d in r['detections'])
                voice = {'numerator':actor_pairs,'denominator':pairs,
                         'value':Decimal(actor_pairs)/Decimal(pairs) if pairs else None,
                         'status':'observed' if pairs else 'unavailable',
                         'formula':'actor-response pairs / all monitored actor-response pairs',
                         'monitored_actor_ids':p['actor_ids'],'response_ids':[r['id'] for r in complete],
                         'unknown_responses_excluded':len(valid)-len(complete)}
                actor_results.append({'actor_id':actor,'rates':rates,'share_of_voice_on_panel':voice})
            by_question.append({'question':q,'collected_responses':len(responses),'valid_responses':len(valid),
                                'errors_excluded':len(responses)-len(valid),
                                'planned_repeats':p['planned_repeats'],
                                'missing_runs':max(0,p['planned_repeats']-len(responses)),
                                'sample_limit':'Moins de 30 relevés valides : description uniquement, protocole GEO habituel non atteint.' if p['kind']=='ia' and len(valid)<30 else None,
                                'actors':actor_results})
        panels.append({'id':p['id'],'kind':p['kind'],'scope_id':p['scope_id'],'engine':p['engine'],
                       'model':p['model'],'mode':p['mode'],'country':p['country'],'language':p['language'],
                       'device':p['device'],'period':p['period'],'top_n':p['top_n'],'questions':by_question,
                       'validation':effective_validation(p['validation'],digest),
                       'interpretation':'Description du panel observé ; aucune extrapolation à la demande globale, au trafic ou au revenu.'})

    capacity = metrics.get(data['production_capacity_id'])
    capacity_value = capacity['value'] if capacity else None
    planning = []
    order = data['priority_order'] + [o['id'] for o in data['opportunities'] if o['id'] not in data['priority_order']]
    opportunity_by_id = {o['id']:o for o in data['opportunities']}
    for oid in order:
        o = opportunity_by_id[oid]
        dependencies = sorted({d for aid in o['action_ids'] for d in actions[aid]['dependencies']
                               if actions[d]['status']!='done' or effective_validation(actions[d]['validation'],digest)!='approved'})
        approval = effective_validation(o['validation'],digest)
        state = 'awaiting_validation' if approval!='approved' or effective_validation(data['validation'],digest)!='approved' else 'ready_for_planning'
        if dependencies: state='dependencies_pending'
        if capacity_value is None: state='capacity_unknown'
        elif capacity_value==0: state='no_capacity'
        if o['decision']!='retain': state=o['decision']
        planning.append({'opportunity_id':oid,'decision':o['decision'],'rank':data['priority_order'].index(oid)+1 if oid in data['priority_order'] else None,
                         'priority_reason':o['priority_reason'],'validation':approval,'state':state,
                         'dependency_ids':dependencies,'action_ids':o['action_ids'],
                         'dates_assigned_by_calculator':False})
    return {'schema_version':VERSION,'method_version':VERSION,'calculator_version':VERSION,
            'project_id':data['project_id'],'dataset_kind':data['dataset_kind'],'dataset_notice':data['dataset_notice'],
            'content_sha256':digest,'artifact_sha256':artifact_hashes(),
            'validation':effective_validation(data['validation'],digest),'warnings':checked['warnings'],
            'source_snapshot':data['sources'],'metric_snapshot':data['metrics'],
            'panels':panels,'group_checks':group_checks,'aggregates':aggregates,'scenarios':scenarios,'planning':planning,
            'scenario_portfolio_total':None,
            'scenario_total_reason':'Scénarios alternatifs ou chevauchants : aucun total automatique.',
            'external_calls':0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output')
    args = parser.parse_args()
    try:
        result = calculate(load(args.input))
        result['input_file_sha256'] = hashlib.sha256(Path(args.input).read_bytes()).hexdigest()
        content = dump(result)
        if args.output:
            write_output(args.output,content,args.input)
            print('Écrit : ' + args.output)
        else: print(content,end='')
        return 0
    except (ValueError,OSError) as error:
        print(str(error),file=sys.stderr);return 2


if __name__ == '__main__':
    sys.exit(main())
