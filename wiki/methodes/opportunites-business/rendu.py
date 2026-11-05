"""Common Markdown projection. Reads common results; never recalculates.

Usage: python3 rendu.py result.json --audience audit|geo [--output new-preview.md]
HTML dashboards use integration.py with the same calculated result.
"""
import argparse
import html
import json
import sys
from decimal import Decimal, ROUND_HALF_UP

from common import load, write_output


def text(value):
    return html.escape(str(value)).replace('|','&#124;').replace('\n',' ')


def value(cell):
    if cell['value'] is None:
        return 'Non estimable avec les données disponibles'
    number=Decimal(str(cell['value']))
    if cell['unit'] in ('EUR','USD','CHF','GBP'):
        shown=format(number.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP),'f')
    else:
        shown=format(number,'f')
        if '.' in shown: shown=shown.rstrip('0').rstrip('.')
    return shown.replace('.',',')+' '+text(cell['unit'])


def render(result, audience):
    label='Audit V2' if audience=='audit' else 'Stratégie GEO'
    rows=['---','type: query','title: "Synthèse des opportunités — '+label+' — '+text(result['project_id'])+'"',
          'tags: [seo, geo, business, test]','created: 2026-11-05','updated: 2026-11-05','sources: 1',
          'confidence: high','status: draft','---','', '# Synthèse des opportunités — '+label,'',
          text(result['dataset_notice']),'',
          'Projection du résultat commun. Méthode : [[methodes/opportunites-business]]. '
          'Origine : [[sources/2026-11-05-inspection-workflows-opportunites-business]].','',
          'Projet : '+text(result['project_id'])+'. Validation effective : '+text(result['validation'])+'.','',
          'Empreinte des données : `'+result['content_sha256']+'`.','',
          '## Opportunités et conditions','',
          '| Opportunité | Ordre proposé | Justification | Condition | Validation |', '|---|---|---|---|---|']
    labels={'no_capacity':'Capacité nulle','capacity_unknown':'Capacité inconnue','dependencies_pending':'Dépendances en attente',
            'awaiting_validation':'Validation attendue','ready_for_planning':'Prêt à planifier',
            'investigate':'Investigation requise','defer':'Report proposé','exclude':'Exclusion proposée'}
    for o in result['planning']:
        rows.append('| '+text(o['opportunity_id'])+' | '+('Non retenu' if o['rank'] is None else str(o['rank']))+
                    ' | '+text(o['priority_reason'])+' | '+text(labels[o['state']])+' | '+text(o['validation'])+' |')
    rows += ['', 'Aucune date n’est attribuée par le calculateur. Les actions restent soumises à leurs dépendances et validations.','',
             '## Scénarios sur l’horizon défini','',
             'Potentiel et réalisation sous capacité sont séparés. Les scénarios sont des alternatives ; leurs valeurs ne s’additionnent pas.','',
             '| Scénario | Horizon | Clients additionnels potentiels | CA additionnel potentiel | Contribution additionnelle après investissement | Clients additionnels sous capacité |',
             '|---|---|---|---|---|---|']
    for s in result['scenarios']:
        potential=s['incremental_potential']; deliverable=s['incremental_deliverable']
        rows.append('| '+text(s['name'])+' | '+text(s['horizon']['start'])+' → '+text(s['horizon']['end'])+' | '+
                    ' | '.join(value(x) for x in [potential['clients'],potential['revenue'],potential['contribution_after_investment'],deliverable['clients']])+' |')
        if s['conditional_on_action_ids']:
            rows += ['', 'Condition du scénario '+text(s['name'])+' : '+', '.join(text(x) for x in s['conditional_on_action_ids'])+'.','']
    if not result['scenarios']: rows += ['', 'Aucun scénario économique renseigné.']
    rows += ['', '## Demande et doubles comptes','', '| Agrégat | Résultat | Mesures uniques | Limites |','|---|---|---|---|']
    for a in result['aggregates']:
        rows.append('| '+text(a['id'])+' | '+value(a['result'])+' | '+str(a['unique_counting_keys'])+' | '+text('; '.join(a['result']['missing']) or a['rationale'])+' |')
    if not result['aggregates']: rows += ['', 'Aucun total demandé ; les observations individuelles conservent leur portée.']
    rows += ['', '## Visibilité sur les panels','']
    if not result['panels']: rows += ['Aucun relevé de visibilité fourni. Aucune absence de marque n’est déduite.']
    for p in result['panels']:
        rows += ['### '+text(p['engine'])+' — '+text(p['kind']),'',
                 text(p['country'])+' · '+text(p['language'])+' · '+text(p['mode'])+' · '+text(p['period']['start'])+' → '+text(p['period']['end']), '',
                 '| Question | Acteur | Mention : réponses positives / évaluées | Citation : réponses positives / évaluées |', '|---|---|---|---|']
        for q in p['questions']:
            for a in q['actors']:
                def ratio(key):
                    r=a['rates'].get(key)
                    return 'Non évalué' if r is None or r['value'] is None else str(r['numerator'])+'/'+str(r['denominator'])
                rows.append('| '+text(q['question']['text'])+' | '+text(a['actor_id'])+' | '+ratio('mentioned')+' | '+ratio('cited')+' |')
        for q in p['questions']:
            if q['sample_limit']: rows += ['', text(q['sample_limit'])]
        rows += ['',text(p['interpretation']),'']
    rows += ['', '## Provenance','',
             'Les formules, paramètres, sources, valeurs exactes et motifs de non-calcul sont conservés dans le résultat JSON. '
             'Seules les valeurs monétaires de cet aperçu sont arrondies à deux décimales.','',
             'Aucun outil externe appelé par ce calculateur. Aucun résultat réel d’acquisition déduit des jeux fictifs.','']
    return '\n'.join(rows)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input');parser.add_argument('--audience',choices=['audit','geo'],required=True);parser.add_argument('--output')
    args=parser.parse_args()
    try:
        content=render(load(args.input),args.audience)
        if args.output:write_output(args.output,content,args.input);print('Écrit : '+args.output)
        else:print(content,end='')
        return 0
    except (ValueError,OSError,KeyError) as error:
        print(str(error),file=sys.stderr);return 2


if __name__=='__main__':sys.exit(main())
