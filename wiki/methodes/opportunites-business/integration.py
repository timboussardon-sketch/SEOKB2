"""Shared integration for Audit/GEO; one calculation per build, no collection.

The input is the versioned contract. Old files are never converted implicitly.
"""
import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path

from common import load, dump, write_output, effective_validation
from calculer import calculate
from rendu import value

INTEGRATION_VERSION = '1.0.0'
GEO_SECTIONS = [
    'Synthèse business', 'Données propriétaires', 'Cinq mots-clés business maximum',
    'Micro-intentions', 'Panel de questions IA', 'Groupes de visibilité',
    'Cartographie des URLs', 'Matrice des preuves', "Plan d’optimisation",
    'Distribution externe', 'Dashboard GEO × business', 'Roadmap sur 90 jours',
    'Top 10 des actions',
]
CSS = '''<style>
.business{line-height:1.6;min-width:0;max-width:100%;overflow-wrap:anywhere}
.business h2{font-size:24px;margin:28px 0 14px}.business h3{font-size:18px;margin:22px 0 12px}
.business p{margin:12px 0}.business article{border:1px solid #e3e7f0;border-radius:14px;padding:18px;margin:16px 0;background:#fff}
.business .business-table{max-width:100%;overflow-x:auto;margin:16px 0}
.business table{border-collapse:collapse;width:100%;font-size:14px}
.business th,.business td{padding:10px;text-align:left;vertical-align:top;border-bottom:1px solid #e3e7f0}
.business th{background:#f5f7fb}.business .notice{padding:14px;border-left:3px solid #325de0;background:#f5f7fb}
.business summary{cursor:pointer;font-weight:600;padding:12px 0}.business pre{white-space:pre-wrap;font-size:12px;max-height:420px;overflow:auto}
.business details{margin:14px 0}.business dl{display:grid;grid-template-columns:minmax(100px,1fr) 3fr;gap:6px 12px}
.business dt{font-weight:600}.business dd{margin:0;min-width:0}
@media(max-width:600px){
.business table thead{display:none}.business table,.business tbody,.business tr,.business td{display:block;width:100%;box-sizing:border-box}
.business tr{border:1px solid #e3e7f0;border-radius:12px;margin:12px 0;padding:10px;background:#fff}
.business td{border:0;padding:8px 0;overflow-wrap:anywhere}.business td::before{content:attr(data-label);display:block;color:#5c667e;font-size:12px;font-weight:600}
.business dl{display:block}.business dd{margin:0 0 14px}.business article{padding:12px}.business h2{font-size:21px}}
</style>'''
LABELS = {
    'observed':'Observé','estimated':'Estimé','hypothesis':'Hypothèse','unavailable':'Indisponible',
    'measured_search':'Recherche mesurée','observed_need':'Besoin observé',
    'retain':'Retenue à validation','investigate':'À investiguer','defer':'Reportée','exclude':'Écartée',
    'approved':'Validé','proposed':'Proposé','needs_revision':'À revalider','rejected':'Refusé',
    'no_capacity':'Capacité nulle','capacity_unknown':'Capacité inconnue',
    'dependencies_pending':'Dépendances en attente','awaiting_validation':'Validation attendue',
    'ready_for_planning':'Prêt à planifier','not_established':'Non établi','satisfied':'Étayé',
    'commercial_competitor':'Concurrent commercial','serp_competitor':'Concurrent SERP',
    'ia_source':'Source citée IA','client':'Entreprise étudiée',
}


def esc(v):
    return html.escape('Non renseigné' if v is None else str(v), quote=True)


def label(v):
    return esc(LABELS.get(v, v))


def table(headers, rows):
    return ('<div class="business-table"><table><thead><tr>' + ''.join('<th>'+esc(h)+'</th>' for h in headers)
            + '</tr></thead><tbody>' + ''.join('<tr>'+''.join('<td data-label="'+esc(headers[i])+'">'+str(v)+'</td>' for i,v in enumerate(row))+'</tr>' for row in rows)
            + '</tbody></table></div>')


def details(title, body):
    return '<details><summary>'+esc(title)+'</summary>'+body+'</details>'


def load_bundle(path):
    path = Path(path).resolve()
    data = load(path)
    result = calculate(data)
    return {'data':data, 'result':result, 'manifest':{
        'integration_version':INTEGRATION_VERSION, 'input_path':str(path),
        'input_file_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'content_sha256':result['content_sha256'], 'method_version':result['method_version'],
        'loaded_files':{str(Path(__file__).resolve()):hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                        **{str(Path(__file__).parent/name):sha for name,sha in result['artifact_sha256'].items()}},
        'external_tools_called':[], 'new_observations_collected':False,
        'collection_attestation_scope':'business module only; upstream workflow collection is not attested by this renderer'}}


def metric(bundle, mid):
    m = next((m for m in bundle['data']['metrics'] if m['id']==mid), None)
    if m is None:
        return 'Non estimable avec les données disponibles'
    shown = 'Non estimable avec les données disponibles' if m['value'] is None else esc(m['value'])+' '+esc(m['unit'])
    return shown+' — '+label(m['status'])+'<small> · '+esc(m['id'])+'</small>'


def context(bundle):
    d = bundle['data']
    rows = [[esc(s['description']),esc(', '.join(s['segments'])),esc(', '.join(s['countries'])),
             esc(', '.join(s['languages'])),esc('; '.join(s['limitations']))] for s in d['scopes']]
    offers = [[esc(o['name']),esc(o['commercial_objective']),esc(o['conversion']),esc('; '.join(o['constraints']))] for o in d['offers']]
    return '<section class="business" data-business-part="context"><h2>Contexte et périmètre business</h2><p class="notice">'+esc(d['dataset_notice'])+'</p>'+table(['Périmètre','Segments','Pays','Langues','Limites'],rows)+table(['Offre','Objectif','Conversion','Contraintes'],offers)+'</section>'


def opportunity_card(bundle, o):
    d, r = bundle['data'], bundle['result']
    p = next(x for x in r['planning'] if x['opportunity_id']==o['id'])
    names = {x['id']:x['name'] for x in d['offers']}
    needs = {x['id']:x for x in d['needs']}
    info = table(['Critère','Conclusion','Preuve'],[[esc(k),label(g['status'])+' — '+esc(g['rationale']),esc(', '.join(g['source_ids']))] for k,g in o['gates'].items()])
    info += '<p>Faisabilité : '+esc(o['feasibility'])+'</p><p>URLs : '+esc(', '.join(o['urls']) or 'Aucune destination arrêtée')+'</p>'
    info += '<p>Sources : '+esc(', '.join(o['source_ids']))+' · Validation : '+label(p['validation'])+'</p>'
    return ('<article data-opportunity-id="'+esc(o['id'])+'"><h3>'+esc(o['title'])+'</h3><p>'+esc(names[o['offer_id']])+' · '+label(o['decision'])+'</p>'
            +'<p>'+esc(' ; '.join(needs[n]['text'] for n in o['need_ids']))+'</p><p><b>'+esc(o['priority_reason'])+'</b></p>'
            +'<p>'+label(p['state'])+'</p>'+details('Preuves, faisabilité et validation',info)+'</article>')


def demand(bundle):
    d = bundle['data']
    body = '<h3>Demande pertinente observée</h3><p>Le périmètre exploré ne constitue pas un marché exhaustif. Les volumes ne représentent pas des personnes uniques.</p>'
    rows = [[esc(n['text']),label(n['kind']),esc(n['date']),'<br>'.join(metric(bundle,m) for m in n['metric_ids']) or 'Aucune mesure disponible',esc(', '.join(n['source_ids']))] for n in d['needs']]
    body += table(['Besoin ou intention','Nature','Date','Mesures distinctes','Sources'],rows) if rows else '<p>Aucun besoin documenté ; cadrage et collecte à compléter.</p>'
    body += '<h3>Client, concurrents et sources visibles</h3>'
    rows = [[esc(a['name']),', '.join(label(role) for role in a['roles']),esc(', '.join(a['urls'])),esc(', '.join(a['source_ids']))] for a in d['actors']]
    body += table(['Acteur','Rôles documentés','URLs','Sources'],rows) if rows else '<p>Concurrence non observée dans ce dossier. Aucune position ni absence du client ne peut en être déduite.</p>'
    return body


def summary(bundle, audience='audit'):
    d, r = bundle['data'], bundle['result']
    rank = {oid:i for i,oid in enumerate(d['priority_order'])}
    ordered = sorted(d['opportunities'],key=lambda o:rank.get(o['id'],len(rank)))
    body = '<section class="business" data-business-part="summary"><h2>Opportunités business</h2>'
    body += '<p class="notice">'+esc(d['dataset_notice'])+'</p><p>Décisions proposées ; validation du dossier : '+label(r['validation'])+'.</p>'
    body += demand(bundle)
    body += '<h3>Opportunités et conditions d’accès</h3>'+''.join(opportunity_card(bundle,o) for o in ordered[:3])
    if len(ordered)>3: body += details('Autres opportunités et exclusions',''.join(opportunity_card(bundle,o) for o in ordered[3:]))
    if not ordered: body += '<p>Aucune opportunité étayée à ce stade ; les investigations restent à définir.</p>'
    body += '<p>'+str(len(d['explored_need_ids']))+' besoins explorés ; '+str(len(d['retained_opportunity_ids']))+' opportunités proposées pour le cycle. Ces comptes ne mesurent pas le volume de demande.</p>'
    body += economics(bundle)+details('Sources, mesures, formules et limites',evidence(bundle))+'</section>'
    return body


def economics(bundle):
    r=bundle['result']
    body='<h3>Valeur commerciale estimable</h3><p>Scénarios alternatifs, jamais additionnés. Les résultats dépendent des hypothèses et des actions indiquées.</p>'
    if not r['scenarios']:return body+'<p>Non estimable avec les données disponibles. Collecter le trafic additionnel envisagé, les taux de qualification et de transformation, la valeur client sur un horizon défini, les coûts et la capacité.</p>'
    rows=[]
    for s in r['scenarios']:
        p=s['incremental_potential'];real=s['incremental_deliverable']
        rows.append([esc(s['name']),esc(s['horizon']['start']+' → '+s['horizon']['end']),value(p['clients']),value(p['revenue']),value(p['contribution_after_investment']),value(real['clients'])])
    body+=table(['Scénario','Horizon','Clients additionnels potentiels','CA additionnel potentiel','Contribution additionnelle après investissement','Clients additionnels sous capacité'],rows)
    for s in r['scenarios']:
        trace = '<p>Conditions : '+esc(', '.join(s['conditional_on_action_ids']) or 'Aucune action conditionnante déclarée')+'</p>'
        trace += '<pre>'+esc(dump(s))+'</pre>'
        body+=details('Hypothèses, actuel / futur et formules : '+s['name'],trace)
    return body


def resources(bundle):
    d=bundle['data'];digest=bundle['result']['content_sha256']
    body='<section class="business" data-business-part="resources"><h2>Moyens, obstacles et mesure</h2><p>Capacité de production : '+metric(bundle,d['production_capacity_id'])+'. Aucun délai de résultat ni calendrier n’est généré.</p>'
    rows=[]
    for a in d['actions']:
        rows.append([esc(a['title']),esc(a['owner']),metric(bundle,a['effort_metric_id']),metric(bundle,a['cost_metric_id']),esc(', '.join(a['dependencies']) or 'Aucune déclarée'),esc(a['planned_date']),label(effective_validation(a['validation'],digest))])
    body+=table(['Action proposée','Responsable','Effort','Coût','Dépendances','Date justifiée','Validation'],rows)
    for o in d['opportunities']:
        m=o['measurement']
        rows=[[k,esc(v)] for k,v in [('Indicateur',m['indicator']),('Formule',m['formula']),('Attribution',m['attribution']),('Responsable',m['owner']),('Prochaine revue',m['review_date']),('Poursuivre si',m['continue_if']),('Réviser si',m['revise_if']),('Arrêter si',m['stop_if'])]]
        body+=details('Suivi : '+o['title'],table(['Mesure et décision','Définition'],rows)+'<p>Baseline : '+metric(bundle,m['baseline_metric_id'])+'</p>')
    return body+'</section>'


def visibility(bundle):
    body='<section class="business" data-business-part="visibility"><h2>Visibilité sur le panel étudié</h2><p>Les mentions et citations IA ne mesurent ni la demande globale, ni le trafic, ni le revenu.</p>'
    for p in bundle['result']['panels']:
        body+='<h3>'+esc(p['engine'])+'</h3><p>'+esc(p['country']+' · '+p['language']+' · '+p['mode'])+' · '+esc(p['period']['start']+' → '+p['period']['end'])+'</p>'
        rows=[]
        for q in p['questions']:
            for a in q['actors']:
                for k,v in a['rates'].items():
                    rows.append([esc(q['question']['text']),esc(a['actor_id']),esc(k),esc(v['numerator']),esc(v['denominator']),value(v)])
        body+=table(['Question','Acteur','Mesure','Numérateur','Dénominateur évalué','Valeur'],rows)
        body+=details('Répétitions, conditions, sources et limites','<pre>'+esc(dump(p))+'</pre>')
    if not bundle['result']['panels']:body+='<p>Aucun relevé fourni. Aucune absence de marque déduite.</p>'
    return body+'</section>'


def evidence(bundle):
    d=bundle['data']
    rows=[[esc(s['origin']),esc(s['collected_at']),esc(s['document_date']),esc(s['locator']),esc('; '.join(s['limitations']))] for s in d['sources']]
    return table(['Source','Collecte d’origine','Document','Localisation','Limites'],rows)+'<p>Les paramètres et traces ci-dessous ne sont pas des résultats commerciaux observés.</p><pre>'+esc(dump({'metrics':d['metrics'],'groups':d['groups'],'result':bundle['result']}))+'</pre>'


def validate_geo(content, state, bundle):
    if state not in ('pending','complete'):raise ValueError('GEO_STATE requis : pending ou complete.')
    if state=='pending':
        return '<section class="business"><h2>Stratégie GEO en attente de validation</h2><p>La collecte de l’audit est réutilisable. La stratégie, la sélection finale, la production et la roadmap restent à valider.</p></section>'+resources(bundle)
    if bundle['result']['validation']!='approved':raise ValueError('Stratégie complète refusée : dossier business non validé ou périmé.')
    headings=re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>',content,re.S|re.I)
    normalize=lambda t:re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]*>',' ',t))).strip().casefold().replace('’',"'")
    headings=[normalize(t) for t in headings]
    pos=0
    for title in GEO_SECTIONS:
        target=normalize(title)
        found=next((i for i in range(pos,len(headings)) if re.sub(r'^\d+[.) —-]*','',headings[i])==target),None)
        if found is None:raise ValueError('Section GEO absente ou hors ordre : '+title)
        pos=found+1
    return content


def attach_audit(views, bundle, state, geo_contract):
    if geo_contract!='geo-business-v1':raise ValueError('Contrat GEO attendu : geo-business-v1.')
    out=dict(views)
    out[0]=out.get(0,'')+CSS+context(bundle)
    # Context precedes the new summary even when the dashboard opens directly on V[1].
    out[1]=CSS+context(bundle)+summary(bundle)+out.get(1,'')
    keyword_marker='<!-- business-opportunities -->'
    if keyword_marker in out.get(7,''):
        out[7]=out[7].replace(keyword_marker,CSS+summary(bundle))
    out[8]=CSS+resources(bundle)+out.get(8,'')
    out[9]=CSS+validate_geo(out.get(9,''),state,bundle)
    return out


def record_execution(bundle, entrypoint, output, extra_files=()):
    manifest=dict(bundle['manifest'])
    manifest['loaded_files']=dict(manifest['loaded_files'])
    for p in [entrypoint,*extra_files]:
        p=Path(p).resolve()
        if p.is_file():manifest['loaded_files'][str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
    for module in list(sys.modules.values()):
        name=getattr(module,'__file__',None)
        if not name:continue
        path=Path(name).resolve()
        if path.is_file() and ('.claude/skills/' in str(path) or 'audits-clients/' in str(path) or 'opportunites-business' in str(path)):
            manifest['loaded_files'][str(path)]=hashlib.sha256(path.read_bytes()).hexdigest()
    manifest['python_version']=sys.version
    manifest['entrypoint']=str(Path(entrypoint).resolve())
    manifest['output_path']=str(Path(output).resolve())
    manifest['output_sha256']=hashlib.sha256(Path(output).read_bytes()).hexdigest()
    manifest['result']=bundle['result']
    write_output(str(output)+'.business.json',dump(manifest),bundle['manifest']['input_path'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input');parser.add_argument('--output',required=True);parser.add_argument('--audience',choices=['audit','geo'],required=True)
    a=parser.parse_args();b=load_bundle(a.input)
    body=context(b)+summary(b,a.audience)+resources(b)+visibility(b)
    page='<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Opportunités business</title>'+CSS+'<body><main style="max-width:1100px;margin:auto;padding:20px">'+body+'</main></body></html>'
    write_output(a.output,page,a.input);record_execution(b,__file__,a.output)


if __name__=='__main__':main()
