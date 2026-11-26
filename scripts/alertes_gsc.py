#!/usr/bin/env python3
"""Alertes Search Console : pertes de trafic et de positions, sur règles fixes, sans IA.

Fenêtre A = les 7 derniers jours disponibles (la Search Console a 2 à 3 jours de retard),
fenêtre B = les 7 jours d'avant. Sous les seuils minimaux, on ne conclut rien.
  - Trafic  : clics du site −25 % (B ≥ 20 clics), ou impressions −30 % (B ≥ 300) si le site a peu de clics
  - Page    : clics −30 % ou plus aucun clic (B ≥ 20 clics)
  - Top 10  : page en position ≤ 10 en B, absente en A ou > 10 avec 2 places perdues (B ≥ 100 impressions)
  - Position: requête du top 20 qui perd plus de 3 positions (B ≥ 50 impressions, A ≥ 10)
  - Donnée  : plus aucune donnée depuis 5 jours sur un site qui en avait
Accès : identifiants OAuth utilisateur (client_id, client_secret, refresh_token, quota_project_id),
lecture seule, même fichier que le skill reporting-client (GSC_CREDENTIALS).
"""
import json, urllib.parse, urllib.request
from datetime import date, timedelta

API = 'https://www.googleapis.com/webmasters/v3'
SEUILS = dict(site_clics_min=20, site_clics_baisse=0.25, site_impr_min=300, site_impr_baisse=0.30,
              page_clics_min=20, page_clics_baisse=0.30, top10_impr_min=100, top10_recul_min=2.0,
              req_impr_min=50, req_impr_a_min=10, req_pos_perte=3.0, req_pos_max=20.0,
              donnee_gelee_jours=5, par_type=3)


class Gsc:
    def __init__(self, chemin_identifiants):
        c = json.load(open(chemin_identifiants, encoding='utf-8'))
        self.projet = c.get('quota_project_id', '')
        d = urllib.parse.urlencode({'client_id': c['client_id'], 'client_secret': c['client_secret'],
                                    'refresh_token': c['refresh_token'], 'grant_type': 'refresh_token'}).encode()
        self.jeton = json.load(urllib.request.urlopen('https://oauth2.googleapis.com/token', d, timeout=30))['access_token']

    def _appel(self, chemin, corps=None):
        r = urllib.request.Request(API + chemin, data=json.dumps(corps).encode() if corps else None,
                                   headers={'Authorization': 'Bearer ' + self.jeton, 'x-goog-user-project': self.projet,
                                            'Content-Type': 'application/json'})
        return json.load(urllib.request.urlopen(r, timeout=60))

    def sites(self):
        return sorted(s['siteUrl'] for s in self._appel('/sites').get('siteEntry', []))

    def lignes(self, site, debut, fin, dims):
        chemin = f"/sites/{urllib.parse.quote(site, safe='')}/searchAnalytics/query"
        return self._appel(chemin, {'startDate': debut.isoformat(), 'endDate': fin.isoformat(),
                                    'dimensions': dims, 'rowLimit': 25000}).get('rows', [])


def nom_site(site):
    return site.replace('sc-domain:', '').replace('https://', '').replace('http://', '').rstrip('/')


def chemin(url):
    p = urllib.parse.urlparse(url)
    return (p.path or '/') if p.netloc else url


def pct(a, b):
    return f'{(a - b) / b * 100:+.0f} %' if b else '—'


def analyser(gsc, site, aujourdhui, s=SEUILS):
    """Renvoie (alertes, date de fin des données). Une alerte : {cle, type, texte}."""
    jours = gsc.lignes(site, aujourdhui - timedelta(days=30), aujourdhui, ['date'])
    if not jours:
        return [], None
    fin = max(date.fromisoformat(r['keys'][0]) for r in jours)
    retard = (aujourdhui - fin).days
    if retard >= s['donnee_gelee_jours']:
        return [{'cle': f'{site}|donnee', 'type': 'Donnée',
                 'texte': f'plus aucune donnée Search Console depuis le {fin:%d/%m} ({retard} jours)'}], fin
    a_deb, b_fin = fin - timedelta(days=6), fin - timedelta(days=7)
    b_deb = b_fin - timedelta(days=6)
    al = []

    def somme(deb, f_, k):
        return sum(r[k] for r in jours if deb <= date.fromisoformat(r['keys'][0]) <= f_)

    ca, cb = somme(a_deb, fin, 'clicks'), somme(b_deb, b_fin, 'clicks')
    ia, ib = somme(a_deb, fin, 'impressions'), somme(b_deb, b_fin, 'impressions')
    if cb >= s['site_clics_min'] and ca <= cb * (1 - s['site_clics_baisse']):
        al.append({'cle': f'{site}|site-clics', 'type': 'Trafic',
                   'texte': f"clics du site {ca:.0f} contre {cb:.0f} la semaine d'avant ({pct(ca, cb)})"})
    elif cb < s['site_clics_min'] and ib >= s['site_impr_min'] and ia <= ib * (1 - s['site_impr_baisse']):
        al.append({'cle': f'{site}|site-impr', 'type': 'Trafic',
                   'texte': f"impressions du site {ia:.0f} contre {ib:.0f} la semaine d'avant ({pct(ia, ib)})"})

    # Les URL à fragment (#…) sont des extraits de la même page : on les écarte.
    pa = {r['keys'][0]: r for r in gsc.lignes(site, a_deb, fin, ['page']) if '#' not in r['keys'][0]}
    pb = {r['keys'][0]: r for r in gsc.lignes(site, b_deb, b_fin, ['page']) if '#' not in r['keys'][0]}
    pertes = []
    for url, rb in pb.items():
        c = pa.get(url, {}).get('clicks', 0)
        if rb['clicks'] >= s['page_clics_min'] and c <= rb['clicks'] * (1 - s['page_clics_baisse']):
            pertes.append((rb['clicks'] - c, url, c, rb['clicks']))
    for _, url, c, b in sorted(pertes, reverse=True)[:s['par_type']]:
        quoi = 'plus aucun clic' if c == 0 else f'{c:.0f} clics contre {b:.0f} ({pct(c, b)})'
        al.append({'cle': f'{site}|page|{url}', 'type': 'Page', 'texte': f'{chemin(url)} : {quoi}'})

    sorties = []
    for url, rb in pb.items():
        if rb['position'] <= 10 and rb['impressions'] >= s['top10_impr_min']:
            ra = pa.get(url)
            if ra is None or (ra['position'] > 10 and ra['position'] - rb['position'] >= s['top10_recul_min']):
                sorties.append((rb['impressions'], url, rb['position'], ra['position'] if ra else None))
    for _, url, b, a in sorted(sorties, reverse=True)[:s['par_type']]:
        quoi = 'absente des résultats' if a is None else f'position {a:.1f}'
        al.append({'cle': f'{site}|top10|{url}', 'type': 'Top 10',
                   'texte': f'{chemin(url)} sort du top 10 : {quoi}, contre {b:.1f}'})

    qa = {r['keys'][0]: r for r in gsc.lignes(site, a_deb, fin, ['query'])}
    qb = {r['keys'][0]: r for r in gsc.lignes(site, b_deb, b_fin, ['query'])}
    reculs = []
    for q, rb in qb.items():
        ra = qa.get(q)
        if (rb['impressions'] >= s['req_impr_min'] and rb['position'] <= s['req_pos_max'] and ra
                and ra['impressions'] >= s['req_impr_a_min'] and ra['position'] - rb['position'] > s['req_pos_perte']):
            reculs.append((rb['impressions'], q, rb['position'], ra['position']))
    for _, q, b, a in sorted(reculs, reverse=True)[:s['par_type']]:
        al.append({'cle': f'{site}|req|{q}', 'type': 'Position', 'texte': f'« {q} » : position {a:.1f} contre {b:.1f}'})
    return al, fin
