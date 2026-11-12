"""Synthetic contract fixtures for the global-first workflow."""
import _env  # noqa: F401  (coffre de test installé, chemins de scripts/team)
import copy
from pathlib import Path
import tempfile
import unittest

import contracts
from test_contracts import fixture


def fixture_v3(task, source_file=None):
    """Only test data. Optional test_candidate_count/test_selection_count in test brief."""
    phase = task['mission']['phase']
    refs = [{'mission_id':m['id'],'sha':m['sha']} for m in task.get('upstream',[]) if m.get('status')=='approved']
    if phase == 'exploration':
        count=task['project']['brief'].get('test_candidate_count', 7)
        p={'candidates':[dict(keyword='mot '+str(i),offer='Offre test',intent='Intention test '+str(i),demand_status='hypothesis',demand_limit='Candidat synthétique, aucune demande mesurée',source_refs=refs,questions=[dict(id='q1',question='Question exploratoire '+str(i)+' ?',status='hypothesis',gap='Fixture synthétique pour tester le parcours')]) for i in range(count)],'exclusions':[],'unknowns':['Données synthétiques']}
    elif phase == 'priorisation':
        candidates=contracts.candidate_keywords(task)
        globals_=[m for m in task.get('upstream',[]) if m.get('phase')=='strategie-globale' and m.get('status')=='approved']
        if globals_:
            candidates=[item['keyword'] for item in globals_[0]['result']['stage_payload']['candidate_decisions'] if item['status']=='eligible']
        count=task['project']['brief'].get('test_selection_count',5)
        selected=candidates[:count]
        p={'keywords':selected,'selections':[dict(keyword=k,rank=i+1,reason='Raison business synthétique '+str(i),source_refs=refs) for i,k in enumerate(selected)],'excluded_candidates':[k+' : non retenu dans cette fixture' for k in candidates[count:]]}
    elif phase == 'panel':
        cs=contracts.get_stage(task,'exploration')['candidates']
        qs=[]
        for c in cs:
            q=c['questions'][0]
            qs.append(dict(id='p'+str(len(qs)+1),keyword=c['keyword'],question_id=q['id'],original_question=q['question'],question=q['question'],adaptation_reason='Texte inchangé pour test'))
        p={'questions':qs,'protocol':dict(engines=['moteur test'],mode='API test',country='FR',language='fr',repetitions=1,paid=False,estimated_cost=None)}
    else:
        derived=copy.deepcopy(task)
        if phase in ('cadrage','diagnostic'):
            derived['project']['brief']['keywords']=[]
        else:
            derived['project']['brief']['keywords']=contracts.portfolio(task)
        if phase == 'strategie-globale':derived['mission']['phase']='synthese'
        if phase == 'consolidation':derived['mission']['phase']='roadmap'
        r=fixture(derived,source_file)
        if phase == 'strategie-globale':
            r['stage_payload']['candidate_decisions'] = [dict(keyword=k,status='eligible',reason='Admissibilité synthétique étayée pour le test',source_refs=refs) for k in contracts.candidate_keywords(task)]
        if phase == 'cadrage':
            r['stage_payload'].pop('keywords',None)
            r['stage_payload']['exploration_scope']='Offres et besoins du client à explorer avant sélection'
        if phase == 'consolidation':r['stage_payload']['changes_from_global']='Enrichissements issus des stratégies par mot-clé testées'
        return r
    p['source_refs']=refs
    return dict(status='review',summary='Fixture synthétique v3',artifact_markdown='# Test\nFixture de stratégie globale, aucun client réel',facts=[],blockers=[],next_actions=[],stage_payload=p)


class ContractV3Tests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        self.response=self.root/'response.json';self.response.write_text('{}')
        self.brief=dict(workflow_version=3,vault=str(self.root),mode='seo-geo',site='example.invalid',request='Contexte test',sources=[str(self.response)])
        self.upstream=[]

    def tearDown(self):self.tmp.cleanup()

    def task(self,phase):
        return dict(project={'brief':self.brief},mission={'phase':phase,'role':contracts.PHASE_ROLES[phase]},upstream=self.upstream)

    def approve_fixture(self,phase):
        t=self.task(phase);r=fixture_v3(t,self.response);contracts.validate(t,r)
        self.upstream.append(dict(id='id-'+phase,sha='sha-'+phase,status='approved',role=contracts.PHASE_ROLES[phase],phase=phase,result=r))
        return r

    def global_strategy(self):
        for phase in ('cadrage','diagnostic','exploration','panel','observations','opportunites','architecture','roadmap','strategie-globale'):
            self.approve_fixture(phase)

    def test_cadrage_no_keywords_then_global_complete_before_priorities(self):
        self.global_strategy()
        self.assertNotIn('keywords',self.brief)
        r=self.approve_fixture('priorisation')
        self.assertEqual(len(r['stage_payload']['keywords']),5)

    def test_panel_uses_exploration_not_agents(self):
        for phase in ('cadrage','exploration'):self.approve_fixture(phase)
        r=self.approve_fixture('panel')
        self.assertEqual(len(r['stage_payload']['questions']),7)
        self.assertFalse(any(m['role']=='strategie-mot-cle' for m in self.upstream))

    def test_prioritization_before_global_rejected(self):
        for phase in ('cadrage','exploration'):self.approve_fixture(phase)
        t=self.task('priorisation');r=fixture_v3(t)
        with self.assertRaises(ValueError):contracts.validate(t,r)

    def test_prioritization_rejects_new_term_and_unjustified_rank(self):
        self.global_strategy()
        t=self.task('priorisation');r=fixture_v3(t)
        bad=copy.deepcopy(r);bad['stage_payload']['keywords'][0]='terme inventé';bad['stage_payload']['selections'][0]['keyword']='terme inventé'
        with self.assertRaises(ValueError):contracts.validate(t,bad)
        bad=copy.deepcopy(r);bad['stage_payload']['selections'][0]['rank']=2
        with self.assertRaises(ValueError):contracts.validate(t,bad)
        bad=copy.deepcopy(r);bad['stage_payload']['selections'][0]['reason']=''
        with self.assertRaises(ValueError):contracts.validate(t,bad)

    def test_ten_priorities_and_seeds_do_not_override_research(self):
        self.brief.update(keywords=['seed inconnu'],test_candidate_count=12,test_selection_count=10)
        self.global_strategy();r=self.approve_fixture('priorisation')
        self.assertEqual(len(r['stage_payload']['keywords']),10)
        self.assertNotIn('seed inconnu',r['stage_payload']['keywords'])

    def test_global_sections_cannot_cite_only_cadrage(self):
        for phase in ('cadrage','diagnostic','exploration','panel','observations','opportunites','architecture','roadmap'):
            self.approve_fixture(phase)
        t=self.task('strategie-globale');r=fixture_v3(t)
        for section in r['stage_payload']['sections']:
            section['source_refs']=[{'mission_id':'id-cadrage','sha':'sha-cadrage'}]
        with self.assertRaises(ValueError):contracts.validate(t,r)

    def test_prioritization_rejects_globally_excluded_candidate(self):
        self.global_strategy()
        global_payload=self.upstream[-1]['result']['stage_payload']
        global_payload['candidate_decisions'][0]['status']='excluded'
        t=self.task('priorisation');r=fixture_v3(t)
        r['stage_payload']['keywords'][0]='mot 0'
        r['stage_payload']['selections'][0]['keyword']='mot 0'
        with self.assertRaises(ValueError):contracts.validate(t,r)

    def test_global_registry_must_cover_every_candidate(self):
        for phase in ('cadrage','diagnostic','exploration','panel','observations','opportunites','architecture','roadmap'):
            self.approve_fixture(phase)
        t=self.task('strategie-globale');r=fixture_v3(t)
        r['stage_payload']['candidate_decisions'].pop()
        with self.assertRaises(ValueError):contracts.validate(t,r)

    def test_consolidation_requires_every_keyword_strategy(self):
        self.global_strategy();self.approve_fixture('priorisation')
        t=self.task('consolidation');r=fixture_v3(t)
        with self.assertRaises(ValueError):contracts.validate(t,r)
        for i,k in enumerate(contracts.selected_keywords(t)):
            self.upstream.append(dict(id='proof'+str(i),sha='proof-sha'+str(i),status='approved',role='strategie-mot-cle',phase='preuves',subject={'keyword':k},result={}))
        t=self.task('consolidation');r=fixture_v3(t);contracts.validate(t,r)
        bad=copy.deepcopy(r);bad['stage_payload']['actions'][0]['keyword_refs'].pop()
        with self.assertRaises(ValueError):contracts.validate(t,bad)

if __name__=='__main__':unittest.main()
