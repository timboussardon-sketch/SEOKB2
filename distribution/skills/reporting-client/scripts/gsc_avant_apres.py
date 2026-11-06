"""Relevé Search Console avant / après pour le skill reporting-client.

Usage :
  python3 gsc_avant_apres.py <propriété> <dossier_sortie> [--pivot YYYY-MM-DD] [--urls urls.json] [--creds identifiants.json]

<propriété>  ex. https://monsite.fr/ ou sc-domain:monsite.fr
--pivot      date de démarrage de la prestation. Avant = 91 jours qui précèdent, après = 91 jours qui suivent
             (tronqués à la dernière date disponible, flag `apres_incomplet`).
             Sans --pivot : trimestre contre trimestre précédent (91 jours chacun, finissant à la dernière date).
--urls       JSON {"https://site/page": "YYYY-MM-DD"} : dates de publication. Pour chaque URL, 91 jours avant
             contre 91 jours après sa publication (flag `apres_incomplet` si la fenêtre n'est pas écoulée).

Écrit <dossier_sortie>/gsc-avant-apres.json. Lecture seule, aucun chiffre estimé.
Identifiants : --creds <fichier>, sinon la variable GSC_CREDENTIALS, sinon ~/.config/organikk-gsc/oauth-user-credentials.json.
Fichier JSON d'identifiants OAuth utilisateur : client_id, client_secret, refresh_token, quota_project_id.
"""
import json, os, sys, argparse, urllib.request, urllib.parse
from datetime import date, timedelta
from pathlib import Path

CREDS = Path(os.environ.get('GSC_CREDENTIALS') or Path.home() / '.config' / 'organikk-gsc' / 'oauth-user-credentials.json')
FENETRE = 91


def token(creds=CREDS):
    c = json.loads(Path(creds).expanduser().read_text())
    data = urllib.parse.urlencode({'client_id': c['client_id'], 'client_secret': c['client_secret'],
                                   'refresh_token': c['refresh_token'], 'grant_type': 'refresh_token'}).encode()
    return json.load(urllib.request.urlopen('https://oauth2.googleapis.com/token', data))['access_token'], c['quota_project_id']


def query(site, tok, start, end, dims, filters=None):
    rows, offset = [], 0
    while True:
        body = {'startDate': str(start), 'endDate': str(end), 'dimensions': dims, 'rowLimit': 25000,
                'startRow': offset, 'dataState': 'final'}
        if filters:
            body['dimensionFilterGroups'] = [{'filters': filters}]
        req = urllib.request.Request(
            'https://searchconsole.googleapis.com/webmasters/v3/sites/' + urllib.parse.quote(site, safe='') + '/searchAnalytics/query',
            json.dumps(body).encode(),
            {'Authorization': 'Bearer ' + tok[0], 'x-goog-user-project': tok[1], 'Content-Type': 'application/json'})
        batch = json.load(urllib.request.urlopen(req)).get('rows', [])
        rows += batch
        if len(batch) < 25000:
            return rows
        offset += 25000


def fenetres(pivot, last):
    """(avant, apres, apres_incomplet) autour d'une date pivot."""
    avant = (pivot - timedelta(days=FENETRE), pivot - timedelta(days=1))
    fin = pivot + timedelta(days=FENETRE - 1)
    return avant, (pivot, min(fin, last)), fin > last


def releve(site, tok, a, b):
    return {'total': query(site, tok, a, b, []), 'pages': query(site, tok, a, b, ['page']),
            'requetes': query(site, tok, a, b, ['query']), 'pages_requetes': query(site, tok, a, b, ['page', 'query'])}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('site'); ap.add_argument('sortie')
    ap.add_argument('--pivot'); ap.add_argument('--urls'); ap.add_argument('--creds', default=CREDS)
    a = ap.parse_args()
    out = Path(a.sortie); out.mkdir(parents=True, exist_ok=True)
    tok = token(a.creds)
    today = date.today()
    last = max(date.fromisoformat(r['keys'][0]) for r in query(a.site, tok, today - timedelta(days=10), today, ['date']))
    if a.pivot:
        pivot = date.fromisoformat(a.pivot)
        avant, apres, incomplet = fenetres(pivot, last)
        mode = 'pivot'
    else:
        apres, avant, incomplet, mode = (last - timedelta(days=FENETRE - 1), last), (last - timedelta(days=2 * FENETRE - 1), last - timedelta(days=FENETRE)), False, 'trimestre'
    dump = {'site': a.site, 'releve_le': str(today), 'derniere_date': str(last), 'mode': mode, 'pivot': a.pivot,
            'periodes': {'avant': [str(avant[0]), str(avant[1])], 'apres': [str(apres[0]), str(apres[1])]},
            'apres_incomplet': incomplet,
            'avant': releve(a.site, tok, *avant), 'apres': releve(a.site, tok, *apres)}
    if a.urls:
        dump['urls'] = {}
        for url, d in json.loads(Path(a.urls).read_text()).items():
            av, ap_, inc = fenetres(date.fromisoformat(d), last)
            f = [{'dimension': 'page', 'operator': 'equals', 'expression': url}]
            dump['urls'][url] = {'publiee_le': d, 'avant': [str(x) for x in av], 'apres': [str(x) for x in ap_], 'apres_incomplet': inc,
                                 'total_avant': query(a.site, tok, *av, [], f), 'total_apres': query(a.site, tok, *ap_, [], f),
                                 'requetes_apres': query(a.site, tok, *ap_, ['query'], f)}
    (out / 'gsc-avant-apres.json').write_text(json.dumps(dump, ensure_ascii=False))
    print('dernière date', last, '| mode', mode, '| périodes', dump['periodes'], '| après incomplet' if incomplet else '')
    for k in ('avant', 'apres'):
        print(k, dump[k]['total'], len(dump[k]['pages']), 'pages', len(dump[k]['requetes']), 'requêtes')


if __name__ == '__main__':
    main()
