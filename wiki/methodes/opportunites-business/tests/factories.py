"""Explicit synthetic test data. No fixture is a commercial prediction."""
from copy import deepcopy
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from common import fingerprint

HORIZON={'start':'2026-11-01','end':'2026-11-30'}
BASELINE={'start':'2026-10-01','end':'2026-10-30'}


def approval():
    return {'status':'proposed','reviewer':None,'date':None,'message':None,'content_sha256':None}


def source(id='source-test',kind='fixture',origin='tests/factories.py',locator='Données fictives réservées aux tests'):
    return {'id':id,'kind':kind,'origin':origin,'collected_at':'2026-11-05','document_date':None,
            'locator':locator,'sha256':None,'limitations':['Aucune mesure client ; jeu fictif.']}


def metric(id,value,quantity,unit,channel='operations',period=None,status='hypothesis',key=None,currency=None):
    return {'id':id,'value':value,'quantity':quantity,'unit':unit,'channel':channel,
            'status':'unavailable' if value is None else status,'scope_id':'scope-main',
            'period':deepcopy(period or HORIZON),'currency':currency,'source_ids':['source-test'],
            'locator':'tests/factories.py : '+id,'rationale':'Valeur fictive fixée pour contrôler un calcul exact.',
            'author':'Fixture de test','counting_key':key}


def base():
    gate=lambda: {'status':'satisfied','rationale':'Condition explicitement posée par le jeu de test.','source_ids':['source-test']}
    action={'id':'action-page','title':'Documenter le besoin vérifié','kind':'existing_page','source_ids':['source-test'],
            'rationale':'Action fictive servant au test.','urls':[],'status':'proposed','owner':None,'dependencies':[],
            'effort_metric_id':None,'cost_metric_id':None,'planned_date':None,'date_basis_source_ids':[], 'validation':approval()}
    opp={'id':'opp-main','title':'Opportunité de test','offer_id':'offer-main','scope_id':'scope-main',
         'need_ids':['need-main'],'group_ids':[],'actor_ids':[],'source_ids':['source-test'],'urls':[],
         'gates':{'offer':gate(),'business_intent':gate(),'demonstrated_opportunity':gate()},
         'decision':'retain','priority_reason':'Ordre fictif justifié par la dépendance commerciale du cas.','feasibility':'À confirmer avec le responsable.',
         'action_ids':['action-page'],'scenario_ids':[],
         'measurement':{'indicator':'Clients qualifiés','formula':'Clients confirmés dans le CRM sur la période définie.',
                        'source_ids':['source-test'],'baseline_metric_id':None,'owner':None,'review_date':None,
                        'attribution':'Aucune attribution réelle : jeu de test.','continue_if':'Hypothèses confirmées par la mesure.',
                        'revise_if':'Conversion différente du scénario.','stop_if':'Capacité indisponible.', 'limitations':['Jeu fictif.']},
         'validation':approval()}
    return {'schema_version':'0.1.0','method_version':'0.1.0','project_id':'synthetic-business',
            'dataset_kind':'synthetic_test','dataset_notice':'DONNÉES FICTIVES DE TEST — aucune prévision client.',
            'scopes':[{'id':'scope-main','offer_ids':['offer-main'],'segments':['Segment fictif'],'countries':['FR'],
                       'languages':['fr'],'description':'Périmètre réservé au test.','limitations':['Ne représente aucun marché.']}],
            'offers':[{'id':'offer-main','name':'Offre fictive','description':'Offre de test','source_ids':['source-test'],
                       'status':'hypothesis','commercial_objective':'Tester le contrat de données','conversion':'Demande qualifiée','constraints':[]}],
            'sources':[source()], 'metrics':[],
            'needs':[{'id':'need-main','text':'Besoin fictif explicitement identifié','kind':'hypothesis','scope_id':'scope-main',
                      'source_ids':['source-test'],'locator':'tests/factories.py','metric_ids':[],'date':'2026-11-05'}],
            'groups':[],'actors':[],'actions':[action],'opportunities':[opp],'scenarios':[], 'aggregates':[], 'panels':[],
            'explored_need_ids':['need-main'],'retained_opportunity_ids':['opp-main'],'priority_order':['opp-main'],
            'production_capacity_id':None,'validation':approval()}


def empty_funnel():
    return {k:None for k in ['traffic','qualified_lead_rate','closing_rate','revenue_per_client','variable_cost_per_client']}


def sufficient():
    d=base()
    d['metrics']=[metric('current-traffic',1000,'sessions','sessions','analytics',BASELINE,'observed'),
                  metric('current-qualified',0.1,'qualified_lead_rate','qualified_leads/session','analytics',BASELINE,'observed'),
                  metric('current-closing',0.2,'closing_rate','clients/qualified_lead','crm',BASELINE,'observed'),
                  metric('unit-revenue',1000,'revenue_per_client','EUR/client',currency='EUR'),
                  metric('unit-variable',400,'variable_cost_per_client','EUR/client',currency='EUR'),
                  metric('investment',500,'investment_cost','EUR',currency='EUR'),
                  metric('capacity-clients',5,'client_capacity','clients'),
                  metric('capacity-production',8,'production_capacity','hours/week')]
    d['production_capacity_id']='capacity-production'
    for name,traffic in [('prudent',100),('central',200),('favorable',400)]:
        mid='traffic-'+name
        d['metrics'].append(metric(mid,traffic,'sessions','sessions','analytics'))
        current={'traffic':'current-traffic','qualified_lead_rate':'current-qualified','closing_rate':'current-closing',
                 'revenue_per_client':'unit-revenue','variable_cost_per_client':'unit-variable'}
        future=dict(current,traffic=mid)
        d['scenarios'].append({'id':'scenario-'+name,'opportunity_ids':['opp-main'],'name':name,'model':'acquisition_only',
            'scope_id':'scope-main','horizon':deepcopy(HORIZON),'currency':'EUR','current':current,'future':future,
            'investment_cost_id':'investment','client_capacity_id':'capacity-clients',
            'revenue_basis':'Jeu fictif : revenu reconnu par nouveau client sur l’horizon de 30 jours ; aucune LTV extrapolée.',
            'cost_basis':'Coût variable de livraison par client ; investissement additionnel total du même horizon, hors livraison.',
            'investment_includes_delivery_costs':False,'transfer_rationale':'Hypothèses fictives ; taux inchangés pour isoler le trafic.',
            'requires_action_ids':['action-page'],'validation':approval()})
    d['opportunities'][0]['scenario_ids']=[s['id'] for s in d['scenarios']]
    return d


def without_numbers():
    d=base(); d['metrics']=[metric('unavailable-volume',None,'search_volume','searches/month','google_search'),
                           metric('unavailable-conversion',None,'qualified_lead_rate','qualified_leads/session','analytics')]
    d['needs'][0]['metric_ids']=['unavailable-volume']
    s=sufficient()['scenarios'][0]
    s['current']=empty_funnel();s['future']=empty_funnel();s['future']['qualified_lead_rate']='unavailable-conversion'
    s['investment_cost_id']=None;s['client_capacity_id']=None
    d['scenarios']=[s];d['opportunities'][0]['scenario_ids']=[s['id']]
    d['opportunities'][0]['decision']='investigate'; d['opportunities'][0]['gates']['demonstrated_opportunity']['status']='not_established'
    d['retained_opportunity_ids']=[];d['priority_order']=[]
    return d


def double_counting():
    d=base()
    d['metrics']=[metric('variant-a',100,'search_volume','searches/month','google_search',key='provider-bundle-a'),
                  metric('variant-b',100,'search_volume','searches/month','google_search',key='provider-bundle-a'),
                  metric('independent-c',50,'search_volume','searches/month','google_search',key='provider-bundle-c'),
                  metric('ia-count',3,'ia_citations','citations','ia',key='ia-three-responses')]
    d['aggregates']=[{'id':'variants-dedup','metric_ids':['variant-a','variant-b'],'independence':'unknown','rationale':'Même mesure fournisseur.','source_ids':['source-test']},
                     {'id':'disjoint-total','metric_ids':['variant-a','variant-b','independent-c'],'independence':'documented_disjoint','rationale':'Indépendance posée par le jeu de test.','source_ids':['source-test']},
                     {'id':'unknown-overlap','metric_ids':['variant-a','independent-c'],'independence':'unknown','rationale':'Chevauchement inconnu.','source_ids':[]},
                     {'id':'mixed-google-ia','metric_ids':['variant-a','ia-count'],'independence':'documented_disjoint','rationale':'Mélange volontairement invalide pour vérifier le refus du total.','source_ids':['source-test']}]
    return d


def commercial_blocker():
    d=sufficient();d['project_id']='synthetic-commercial-blocker';s=d['scenarios'][1]
    d['scenarios']=[s];d['opportunities'][0]['scenario_ids']=[s['id']]
    s['model']='full_funnel';s['future']['traffic']='future-total';s['future']['qualified_lead_rate']='future-qualified';s['future']['closing_rate']='future-closing'
    d['metrics'] += [metric('future-total',1100,'sessions','sessions','analytics'),
                     metric('future-qualified',0.2,'qualified_lead_rate','qualified_leads/session','analytics'),
                     metric('future-closing',0.3,'closing_rate','clients/qualified_lead','crm')]
    next(m for m in d['metrics'] if m['id']=='capacity-clients')['value']=25
    next(m for m in d['metrics'] if m['id']=='capacity-production')['value']=0
    a=deepcopy(d['actions'][0]);a.update(id='action-sales',title='Vérifier la qualification et la relance des demandes',kind='sales_followup',status='blocked')
    d['actions'].append(a);d['actions'][0]['dependencies']=['action-sales']
    s['requires_action_ids']=['action-sales','action-page']
    s['transfer_rationale']='Hypothèse de test : la hausse des taux dépend du suivi commercial ; aucune causalité établie sur un client.'
    d['opportunities'][0]['action_ids'].append('action-sales')
    return d


def with_panel():
    d=base()
    d['actors']=[{'id':i,'name':i,'domain':i+'.example','roles':[role], 'source_ids':['source-test'],
                  'urls':['https://'+i+'.example'],'rationale':'Acteur fictif.'}
                 for i,role in [('brand','client'),('competitor','ia_source')]]
    def detection(actor,mention,citation=False,recommended=False):
        return {'actor_id':actor,'mentioned':mention,'cited':citation,'recommended':recommended,'position':None,
                'source_ids':['source-test'],'excerpt':'Extrait fictif.' if mention or citation else None,
                'urls':['https://'+actor+'.example'] if citation else []}
    d['panels']=[{'id':'panel-test','kind':'ia','scope_id':'scope-main','engine':'Moteur fictif','model':'Modèle fictif','mode':'Test hors ligne',
                  'country':'FR','language':'fr','device':'test','period':deepcopy(HORIZON),'top_n':None,'planned_repeats':4,
                  'actor_ids':['brand','competitor'],'questions':[{'id':'q-one','text':'Question de test','need_id':'need-main'}],
                  'responses':[{'id':'r-one','question_id':'q-one','date':'2026-11-05','status':'valid','error':None,'source_ids':['source-test'],
                                'detections':[detection('brand',True,True),detection('competitor',True)]},
                               {'id':'r-two','question_id':'q-one','date':'2026-11-05','status':'valid','error':None,'source_ids':['source-test'],
                                'detections':[detection('brand',False),detection('competitor',True)]},
                               {'id':'r-error','question_id':'q-one','date':'2026-11-05','status':'error','error':'Échec simulé','source_ids':['source-test'],'detections':[]}],
                  'validation':approval()}]
    return d


def approve_for_test(d):
    """Simulation of an approval, never used on real input."""
    digest=fingerprint(d)
    def walk(x):
        if isinstance(x,dict):
            if 'validation' in x:
                x['validation']={'status':'approved','reviewer':'TEST UNIQUEMENT','date':'2026-11-05',
                                 'message':'Accord fictif de test','content_sha256':digest}
            for k,v in x.items():
                if k!='validation':walk(v)
        elif isinstance(x,list):
            for y in x:walk(y)
    walk(d)
    return d
