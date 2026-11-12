"""Synthetic business data; no client, model call or commercial action."""
import _env  # noqa: F401  (coffre de test installé, chemins de scripts/team)
import copy
from pathlib import Path
import tempfile
import unittest

import contracts
from gtm_contracts import PHASES, STAGES
from providers import build_prompt
from team import Team
from test_contracts_v3 import fixture_v3


def fixture_v4(task, source_file=None):
    phase = task['mission']['phase']
    if phase not in PHASES:
        result = fixture_v3(task, source_file)
        if phase == 'exploration':
            for candidate in result['stage_payload']['candidates']:
                candidate['gtm_ids'] = ['GTM-001']
                candidate['offer'] = 'Accompagnement test'
        if phase == 'opportunites':
            for item in result['stage_payload']['opportunities']:
                item.update(offer='Accompagnement test', conversion='Demande qualifiée')
        return result
    refs = [{'mission_id': m['id'], 'sha': m['sha']} for m in task['upstream']]
    if phase == 'gtm-diagnostic':
        path = Path(task['project']['brief']['vault']) / 'raw/clients/call.md'
        p = dict(diagnosis='Le client test cherche à réduire les erreurs.',
                 sources=[dict(id='S-001', title='Entretien synthétique', author='Fixture', document_date='2026-11-07', consulted_at='2026-11-07', scope='Cas fictif uniquement', access='Fichier local', source_file=str(path), excerpt='Le client veut réduire les erreurs.')],
                 claims=[dict(id='F-001', claim='Le client test décrit des erreurs.', status='declared', source_ids=['S-001'], limit='Fixture, pas une demande réelle')],
                 research_log=[dict(query='Dossier test', result='Entretien fictif', access='Local')], contradictions=[])
    elif phase == 'gtm-offre':
        p = dict(segments=[dict(id='GTM-001', offer='Accompagnement test', segment='PME test', markets=['Services'], zones=['France'], languages=['fr'], buyer_roles=dict(user='Équipe', decision_maker='Dirigeant', payer='Entreprise'), problem='Erreurs de traitement', trigger='Reprise manuelle répétée', alternatives=['Processus interne'], positioning='Accompagnement opérationnel', message='Mettre en place un processus vérifiable', claim_ids=['F-001'], price=dict(status='unknown', amount=None, currency='EUR', unit='mission', basis='Aucun devis dans le test'), terms=['À préciser'], capacity='Inconnue', exclusions=[], objections=['Temps de mise en place'], priority='proposed', reason='Besoin déclaré dans la fixture')])
    elif phase == 'gtm-parcours':
        p = dict(journey=[dict(gtm_id='GTM-001', stage=s, buyer_action='Examiner un cas', proof='Cas à collecter', objection='Manque de temps', destination='Rendez-vous proposé', next_action='Préciser le besoin', owner='Rôle à attribuer', measure='Événement daté') for s in STAGES], channels=[dict(gtm_id='GTM-001', channel='Partenariat', role='Accès aux acheteurs', status='hypothesis', reason='Accès non testé', message='Cas opérationnel', proof='À collecter', destination='Rendez-vous', next_action='Qualifier', measure='Demandes qualifiées')], bottleneck='Inconnu', capacity='Inconnue', economics='Non calculable : coûts absents', deferred_channels='Publicité : budget inconnu')
    else:
        p = dict(experiments=[dict(id='T-001', gtm_id='GTM-001', hypothesis='La mise en place motive la décision', method='Entretien puis proposition séparée', metric='Engagements', denominator='Propositions effectivement remises', baseline='Inconnue', threshold='À définir avec le budget', owner='Responsable proposé', budget_cap=None, budget_unit='EUR', capacity='À confirmer', window='Après validation des moyens', stop_condition='Capacité dépassée', decisions={'continue':'Signal confirmé', 'modify':'Autre frein', 'stop':'Besoin absent', 'inconclusive':'Données insuffisantes'})], handoff=dict(version=1, date='2026-11-07', entries=[dict(gtm_id='GTM-001', offer='Accompagnement test', segment='PME test', conversion='Demande qualifiée', destination='Page existante à vérifier', seo_geo_role='Tester la demande sans présumer le canal', proofs='Entretien synthétique F-001', limits='Pas de demande mesurée', owner='Responsable proposé', measurement='Demandes puis commandes')]), roadmap=[dict(action='Vérifier les moyens', owner='Responsable proposé', dependency='Cadrage approuvé', capacity='À préciser', done_when='Capacité documentée')], measurement='Ne pas assimiler les clics aux ventes')
    p.update(source_refs=refs, decision_status='proposed', unknowns=['Données synthétiques'])
    return dict(status='review', summary='Fixture GTM', artifact_markdown='# Fixture GTM\nAucun client réel.', facts=[], blockers=[], next_actions=[], stage_payload=p)


class GTMTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / 'AGENTS.md').write_text('Fixture technique')
        (self.root / 'raw/clients').mkdir(parents=True)
        self.source = self.root / 'raw/clients/call.md'
        self.source.write_text('Le client veut réduire les erreurs.')
        self.team = Team(self.root / 'data')
        self.brief = dict(name='Fixture', site='https://example.invalid', objective='Essai technique', request='Contexte test', mode='seo', vault=str(self.root))
        created = self.team.start(self.brief)
        self.project = created['project']['id']
        self.cadrage = created['mission']

    def tearDown(self):
        self.tmp.cleanup()

    def task(self, mission):
        with self.team.db() as db:
            return dict(project=self.team._get(db, 'projects', self.project), mission=mission, upstream=self.team._upstream(db, mission))

    def approve(self, mission):
        submitted = self.team.submit(mission['id'], fixture_v4(self.task(mission)))
        return self.team.approve(mission['id'], submitted['sha'], 'Accord synthétique isolé', True)

    def to_phase(self, phase):
        for _ in range(8):
            ready = self.team.prepare(self.project)['next']['ready']
            for mission in ready:
                if mission['phase'] == phase:
                    return mission
                self.approve(mission)
        self.fail('Phase non atteinte')

    def test_default_and_each_human_gate_before_seo(self):
        self.assertEqual(self.team.status()['projects'][0]['brief']['workflow_version'], 4)
        self.approve(self.cadrage)
        keys = []
        for phase in PHASES:
            ready = self.team.prepare(self.project)['next']['ready']
            self.assertEqual([m['phase'] for m in ready], [phase])
            keys.append(ready[0]['subject']['agent_key'])
            submitted = self.team.submit(ready[0]['id'], fixture_v4(self.task(ready[0])))
            self.assertEqual(self.team.prepare(self.project)['created'], [])
            with self.assertRaises(ValueError): self.team.fanout(self.project)
            self.team.approve(submitted['id'], submitted['sha'], 'Accord simulé', True)
        self.assertEqual(len(set(keys)), 1)
        following = self.team.prepare(self.project)['next']['ready']
        self.assertEqual({m['phase'] for m in following}, {'diagnostic', 'exploration'})
        for mission in following:
            task = self.task(mission)
            self.assertTrue(all(p in [m['phase'] for m in task['upstream']] for p in PHASES))
            contracts.validate(task, fixture_v4(task))

    def test_history_v3_is_not_migrated(self):
        old = self.team.start(dict(self.brief, workflow_version=3))
        self.project = old['project']['id']
        self.approve(old['mission'])
        self.assertEqual({m['phase'] for m in self.team.prepare(self.project)['created']}, {'diagnostic', 'exploration'})
        self.assertEqual(self.team.status(self.project)['projects'][0]['brief']['workflow_version'], 3)

    def test_sources_and_proposed_status_are_checked(self):
        mission = self.to_phase('gtm-diagnostic')
        task = self.task(mission)
        result = fixture_v4(task)
        for mutate in [lambda p: p.update(decision_status='validated'), lambda p: p['claims'][0].update(source_ids=['missing']), lambda p: p['sources'][0].update(excerpt='Citation inventée')]:
            bad = copy.deepcopy(result); mutate(bad['stage_payload'])
            with self.assertRaises(ValueError): contracts.validate(task, bad)

    def test_handoff_rejects_changed_offer_and_skipped_predecessor(self):
        task = self.task(self.to_phase('gtm-transmission'))
        result = fixture_v4(task)
        contracts.validate(task, result)
        bad = copy.deepcopy(result); bad['stage_payload']['handoff']['entries'][0]['offer'] = 'Autre offre'
        with self.assertRaises(ValueError): contracts.validate(task, bad)
        bad = copy.deepcopy(result); bad['stage_payload']['source_refs'] = [bad['stage_payload']['source_refs'][0]]
        with self.assertRaises(ValueError): contracts.validate(task, bad)

    def test_correction_invalidates_seo_and_source_changes_block_consumption(self):
        self.to_phase('diagnostic')
        missions = self.team.status(self.project)['missions']
        seo = next(m for m in missions if m['phase'] == 'diagnostic')
        self.source.write_text('Une source modifiée après validation.')
        with self.assertRaises(ValueError): self.team.submit(seo['id'], fixture_v4(self.task(seo)))
        self.source.write_text('Le client veut réduire les erreurs.')
        offer = next(m for m in missions if m['phase'] == 'gtm-offre')
        affected = self.team.revise(offer['id'], 'Correction test')['affected']
        self.assertIn(seo['id'], affected)
        self.assertNotIn(self.cadrage['id'], affected)
        self.assertEqual([m['phase'] for m in self.team.next(self.project)['ready']], ['gtm-offre'])

    def test_exploration_cannot_drop_or_invent_gtm_mapping(self):
        task = self.task(self.to_phase('exploration'))
        for ids in [[], ['GTM-inconnu']]:
            result = fixture_v4(task); result['stage_payload']['candidates'][0]['gtm_ids'] = ids
            with self.assertRaises(ValueError): contracts.validate(task, result)

    def test_offer_and_conversion_cannot_drift_from_gtm(self):
        task = self.task(self.to_phase('exploration'))
        result = fixture_v4(task)
        result['stage_payload']['candidates'][0]['offer'] = 'Vente de véhicules électriques'
        with self.assertRaisesRegex(ValueError, 'Offre candidate'): contracts.validate(task, result)
        self.approve(task['mission'])
        task = self.task(self.to_phase('opportunites'))
        for field in ('offer', 'conversion'):
            result = fixture_v4(task)
            result['stage_payload']['opportunities'][0][field] = 'Valeur étrangère au GTM'
            with self.assertRaisesRegex(ValueError, 'Offre ou conversion'): contracts.validate(task, result)

    def test_provider_loads_installed_skill_and_phase_references(self):
        for phase in PHASES:
            task = self.task(self.to_phase(phase))
            prompt, methods, _ = build_prompt(task)
            paths = [m['path'] for m in methods]
            self.assertTrue(any(p.endswith('/go-to-market/SKILL.md') for p in paths))
            self.assertTrue(all(m['sha256'] for m in methods))
            if phase == 'gtm-transmission':
                self.assertTrue(any(p.endswith('/passage-seo-geo.md') for p in paths))
            self.assertIn(task['mission']['phase'], prompt)


if __name__ == '__main__': unittest.main()
