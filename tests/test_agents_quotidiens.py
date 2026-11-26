import sys, tempfile, unittest
from datetime import date, datetime, timedelta
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import agents_quotidiens as aq, alertes_gsc, notifier  # noqa: E402

AUJ = date(2026, 11, 26)
FIN = AUJ - timedelta(days=3)


class FausseGsc:
    """A = 7 jours au FIN, B = 7 jours d'avant."""
    def __init__(self, clics_a=10, clics_b=30, pages_a=None, pages_b=None, req_a=None, req_b=None, fin=FIN):
        self.c, self.fin = (clics_a, clics_b), fin
        self.p, self.q = (pages_a or [], pages_b or []), (req_a or [], req_b or [])

    def lignes(self, site, debut, fin, dims):
        if dims == ['date']:
            out = []
            for i in range(14):
                d = self.fin - timedelta(days=i)
                c = self.c[0] / 7 if i < 7 else self.c[1] / 7
                out.append({'keys': [d.isoformat()], 'clicks': c, 'impressions': c * 20, 'position': 5})
            return out
        a = fin == self.fin
        src = self.p if dims == ['page'] else self.q
        return [{'keys': [k], 'clicks': c, 'impressions': i, 'position': p} for k, c, i, p in src[0 if a else 1]]


class Alertes(unittest.TestCase):
    def types(self, gsc):
        return [a['type'] for a in alertes_gsc.analyser(gsc, 'https://ex.fr/', AUJ)[0]]

    def test_baisse_du_site(self):
        self.assertIn('Trafic', self.types(FausseGsc(10, 30)))

    def test_petit_site_sans_conclusion(self):
        self.assertEqual(self.types(FausseGsc(2, 8)), [])

    def test_page_top10_requete(self):
        g = FausseGsc(30, 30,
                      pages_a=[('https://ex.fr/a', 5, 200, 14.0), ('https://ex.fr/b#x', 0, 0, 30)],
                      pages_b=[('https://ex.fr/a', 25, 200, 6.0), ('https://ex.fr/b#x', 50, 300, 2)],
                      req_a=[('seo lyon', 1, 60, 15.0), ('loin', 1, 60, 60.0)],
                      req_b=[('seo lyon', 5, 80, 8.0), ('loin', 1, 80, 50.0)])
        als = alertes_gsc.analyser(g, 'https://ex.fr/', AUJ)[0]
        self.assertEqual(sorted({a['type'] for a in als}), ['Page', 'Position', 'Top 10'])
        self.assertFalse(any('#' in a['cle'] for a in als), 'URL à fragment écartée')
        self.assertFalse(any('loin' in a['texte'] for a in als), 'requête hors top 20 écartée')

    def test_recul_minime_hors_alerte(self):
        g = FausseGsc(30, 30, pages_a=[('https://ex.fr/a', 20, 200, 10.5)], pages_b=[('https://ex.fr/a', 20, 200, 9.5)])
        self.assertNotIn('Top 10', self.types(g))

    def test_donnee_gelee(self):
        self.assertEqual(self.types(FausseGsc(fin=AUJ - timedelta(days=8))), ['Donnée'])


class Notifier(unittest.TestCase):
    def test_whatsapp_coupe(self):
        t = notifier.texte_whatsapp('Titre', ['x' * 100] * 40)
        self.assertLessEqual(len(t), notifier.WHATSAPP_MAX)
        self.assertIn('de plus', t)

    def test_reglages_manquants(self):
        self.assertEqual(notifier.manquants({'CANAL': 'whatsapp', 'WHATSAPP_NUMERO': '+33600000000'}), ['CALLMEBOT_APIKEY'])
        self.assertIn('GMAIL_ADRESSE', notifier.manquants({}))

    def test_un_canal_en_panne_n_arrete_pas_l_autre(self):
        with mock.patch.object(notifier, 'envoyer_gmail', side_effect=OSError('smtp')), \
             mock.patch.object(notifier, 'envoyer_whatsapp', return_value=None):
            r = notifier.envoyer({'CANAL': 'gmail,whatsapp'}, 't', ['l'])
        self.assertEqual(r['whatsapp'], 'ok')
        self.assertIn('smtp', r['gmail'])


class Passage(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def lancer(self, heure, etat=None):
        if etat:
            aq.ecrire_etat(self.root, etat)
        now = datetime(2026, 11, 26, heure, 5).astimezone()
        with mock.patch.object(aq, 'maintenant', return_value=now), \
             mock.patch.object(aq, 'alertes', return_value=0) as a, mock.patch.object(aq, 'recap', return_value=0) as r:
            aq.planifie(self.root, {})
        return a.called, r.called, r.call_args

    def test_heures(self):
        self.assertEqual(self.lancer(8)[:2], (False, False))
        self.assertEqual(self.lancer(9)[:2], (True, False))
        self.assertEqual(self.lancer(21)[:2], (True, True))

    def test_une_fois_par_jour(self):
        self.assertEqual(self.lancer(21, {'alertes_jour': '2026-11-26', 'recap_jour': '2026-11-26'})[:2], (False, False))

    def test_recap_de_la_veille_rattrape(self):
        a, r, args = self.lancer(8, {'recap_jour': '2026-11-24'})
        self.assertTrue(r)
        self.assertEqual(args.kwargs['jour'], date(2026, 11, 25))

    def test_plist(self):
        p = aq.plist(self.root)
        self.assertIn('<integer>5</integer>', p)
        self.assertIn('planifie', p)
        self.assertIn(aq.ident(self.root), p)

    def test_recap_sans_matiere(self):
        out = aq.brut([], [], [])
        self.assertEqual(out, [])

    def test_env(self):
        (self.root / '.env.local').write_text('CANAL=whatsapp  # commentaire\n# x=1\nALERTES_HEURE="8"\n')
        cfg = aq.lire_env(self.root)
        self.assertEqual((cfg['CANAL'], cfg['ALERTES_HEURE']), ('whatsapp', '8'))


if __name__ == '__main__':
    unittest.main()
