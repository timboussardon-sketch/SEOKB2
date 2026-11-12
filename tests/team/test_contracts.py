import _env  # noqa: F401  (coffre de test installé, chemins de scripts/team)
import copy
import json
from pathlib import Path
import tempfile
import unittest

import contracts


def fixture(task, source_file=None):
    """Synthetic payload for integration tests only; never a client strategy."""
    phase = task['mission']['phase']
    keywords = task['project']['brief']['keywords']
    refs = [{'mission_id': m['id'], 'sha': m['sha']} for m in task.get('upstream', []) if m.get('status') == 'approved']
    if phase == 'cadrage':
        payload = {'business': dict(offer='Offre test', audience='Audience test', problem='Problème test', conversion='Conversion test'), 'keywords':keywords, 'sources':[], 'user_context':task['project']['brief']['request'], 'unknowns':[]}
    elif phase == 'diagnostic':
        payload = {'checks':[dict(area=a,url='https://example.invalid/',status='not_tested',finding='Non testé',reason='Fixture synthétique sans collecte') for a in ('indexation','performance','contenu','maillage','conversion')], 'actions':[]}
    elif phase == 'panel':
        qs=[]
        for m in task['upstream']:
            if m.get('role') == 'strategie-mot-cle' and m.get('phase') == 'questions':
                q=m['result']['keyword_payload']['questions'][0]
                qs.append(dict(id='p'+str(len(qs)+1),keyword=m['subject']['keyword'],question_id=q['id'],original_question=q['question'],question=q['question'],adaptation_reason='Texte inchangé'))
        payload = {'questions':qs,'protocol':dict(engines=['moteur test'],mode='API test',country='FR',language='fr',repetitions=1,paid=False,estimated_cost=None)}
    elif phase == 'observations':
        panel = contracts.get_stage(task,'panel')
        require_file = Path(source_file)
        rows = [dict(question_id=q['id'],question=q['question'],engine='moteur test',repetition=1,mode='API test',status='ok',date='2026-11-06',provider='synthetic-test',model='synthetic-test',source_file=str(require_file),response='Réponse synthétique de test sans lien.',links=[],cited=False,provenance='imported_original',import_origin='Fixture synthétique créée pour test isolé',source_id='test-'+q['id']) for q in panel['questions']]
        require_file.write_text(json.dumps({'records':[dict(question=r['question'],response=r['response'],links=r['links'],provider=r['provider'],model=r['model'],mode=r['mode'],collected_at=r['date'],source_id=r['source_id']) for r in rows]}))
        payload = {'observations':rows, 'limitations':['Réponses fictives, test isolé']}
    elif phase == 'opportunites':
        payload = {'opportunities':[dict(id='o1',keyword_refs=keywords,need='Besoin test',offer='Offre test',conversion='Conversion test',reason='Raison test',condition='À examiner',demand_status='hypothesis',source_refs=refs,unknowns=[])], 'exclusions':[], 'business_dataset':None,'estimation_limit':'Non estimable avec les fixtures synthétiques'}
    elif phase == 'architecture':
        payload = {'destinations':[dict(id='u1',keyword_refs=keywords,status='candidate',url='https://example.invalid/test',action='creer',reason='Proposition test',source_refs=refs)], 'overlap_review':'Une destination commune proposée pour le test'}
    elif phase == 'roadmap':
        payload = {'capacity':dict(confirmed=False,description='Capacité inconnue pour le test'),'actions':[dict(id='a1',title='Action test',target='Page test',reason='Raison test',done_when='Contrôle test',expected_effect='Effet test',keyword_refs=keywords,depends_on=[],owner=None,effort=None,due=None,source_refs=refs)],'measurement':'Mesure test','distribution':'Distribution non prévue pour la fixture'}
    elif phase == 'synthese':
        ids=contracts.SEO_SECTIONS if task['project']['brief']['mode']=='seo' else contracts.GEO_SECTIONS
        payload = {'sections':[dict(id=i,content='Contenu synthétique '+i,source_refs=refs) for i in ids], 'limits':['Test synthétique']}
    elif phase == 'controle':
        payload = {'verdict':'conforme','checks':dict(coverage=True,provenance=True,validations=True),'findings':[]}
    else:
        raise ValueError(phase)
    payload['source_refs']=refs
    return dict(status='review',summary='Fixture synthétique de test',artifact_markdown='# Test\nFixture synthétique, aucun client réel',facts=[],blockers=[],next_actions=[],stage_payload=payload)


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.vault=Path(self.temp.name)
        self.file=self.vault/'response.txt';self.file.write_text('Réponse synthétique de test sans lien.')
        self.brief=dict(vault=str(self.vault),mode='seo-geo',keywords=['mot '+str(i) for i in range(5)],site='example.invalid',request='Contexte synthétique du test',sources=[str(self.file)])
        self.upstream=[dict(id='c1',phase='cadrage',role='pilote',sha='test-sha',status='approved',result={})]

    def tearDown(self):self.temp.cleanup()

    def task(self,phase):return dict(project={'brief':self.brief},mission={'phase':phase,'role':contracts.PHASE_ROLES[phase]},upstream=self.upstream)

    def test_blocked_requires_explanation(self):
        with self.assertRaises(ValueError):contracts.validate(self.task('diagnostic'),dict(status='blocked',blockers=[]))
        contracts.validate(self.task('diagnostic'),dict(status='blocked',blockers=['Source absente']))

    def test_cadrage_preserves_exact_keywords_and_context(self):
        t=self.task('cadrage');t['upstream']=[];r=fixture(t);contracts.validate(t,r)
        r['stage_payload']['keywords']=list(reversed(self.brief['keywords']))
        with self.assertRaises(ValueError):contracts.validate(t,r)

    def test_stale_reference_rejected(self):
        t=self.task('diagnostic');r=fixture(t);contracts.validate(t,r)
        r['stage_payload']['source_refs'][0]['sha']='wrong'
        with self.assertRaises(ValueError):contracts.validate(t,r)

    def test_observation_requires_response_evidence(self):
        panel=dict(questions=[dict(id='p1',question='Question exacte')],protocol=dict(engines=['moteur test'],repetitions=1,mode='API test'))
        self.upstream=[dict(id='p1',phase='panel',role='visibilite-ia',sha='panel-sha',status='approved',result={'stage_payload':panel})]
        t=self.task('observations');r=fixture(t,self.file);contracts.validate(t,r)
        r['stage_payload']['observations'][0]['response']='Texte inventé'
        with self.assertRaises(ValueError):contracts.validate(t,r)

    def test_all_errors_cannot_be_a_completed_observation(self):
        self.upstream=[dict(id='p1',phase='panel',role='visibilite-ia',sha='p-sha',status='approved',result={'stage_payload':dict(questions=[dict(id='p1',question='Q')],protocol=dict(engines=['moteur test'],repetitions=1,mode='API test'))})]
        t=self.task('observations');r=fixture(t,self.file);row=r['stage_payload']['observations'][0]
        row.update(status='error',response=None,links=[],cited=False,error='Panne')
        with self.assertRaises(ValueError):contracts.validate(t,r)
        row['cited']=None
        with self.assertRaises(ValueError):contracts.validate(t,r)


    def test_omitted_citation_is_rejected(self):
        self.upstream=[dict(id='p1',phase='panel',role='visibilite-ia',sha='p-sha',status='approved',result={'stage_payload':dict(questions=[dict(id='p1',question='Q')],protocol=dict(engines=['moteur test'],repetitions=1,mode='API test'))})]
        t=self.task('observations');r=fixture(t,self.file);row=r['stage_payload']['observations'][0]
        row['response']='Consultez https://example.invalid/offre.'
        receipt=json.loads(self.file.read_text());receipt['records'][0]['response']=row['response'];self.file.write_text(json.dumps(receipt))
        with self.assertRaises(ValueError):contracts.validate(t,r)

    def test_new_collection_without_real_tool_trace_is_rejected(self):
        self.upstream=[dict(id='p1',phase='panel',role='visibilite-ia',sha='p-sha',status='approved',result={'stage_payload':dict(questions=[dict(id='p1',question='Q')],protocol=dict(engines=['moteur test'],repetitions=1,mode='API test'))})]
        t=self.task('observations');r=fixture(t,self.file);r['stage_payload']['observations'][0]['provenance']='collected'
        with self.assertRaises(ValueError):contracts.validate(t,r)

    def test_roadmap_rejects_missing_keyword_cycle_or_calendar(self):
        t=self.task('roadmap');r=fixture(t);contracts.validate(t,r)
        for key,value in [('keyword_refs',self.brief['keywords'][:-1]),('depends_on',['a1']),('due','2026-12-01')]:
            bad=copy.deepcopy(r);bad['stage_payload']['actions'][0][key]=value
            with self.assertRaises(ValueError):contracts.validate(t,bad)

    def test_generic_synthesis_and_quality_rejected(self):
        t=self.task('synthese');r=fixture(t);contracts.validate(t,r)
        r['stage_payload']['sections'].pop()
        with self.assertRaises(ValueError):contracts.validate(t,r)
        t=self.task('controle');r=fixture(t);r['stage_payload']['checks']['coverage']=False
        with self.assertRaises(ValueError):contracts.validate(t,r)

    def test_qualitative_opportunity_cannot_smuggle_score(self):
        t=self.task('opportunites');r=fixture(t);contracts.validate(t,r)
        r['stage_payload']['opportunities'][0]['score']=90
        with self.assertRaises(ValueError):contracts.validate(t,r)

if __name__=='__main__':unittest.main()
