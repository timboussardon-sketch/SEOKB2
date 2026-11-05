"""Insert shared Markdown blocks into an authored report, preserving technical body."""
import argparse
from pathlib import Path
from common import write_output
from integration import load_bundle, record_execution
from rendu import render, text

CONTEXT='<!-- business-context -->'
SUMMARY='<!-- business-summary -->'


def assemble_report(bundle, body, audience):
    if body.count(CONTEXT)!=1 or body.count(SUMMARY)!=1 or body.index(CONTEXT)>body.index(SUMMARY):
        raise ValueError('Un marqueur contexte puis un marqueur synthèse sont requis, chacun une fois.')
    d=bundle['data']
    context=['## Contexte et périmètre', '', text(d['dataset_notice']), '']
    for s in d['scopes']:
        context += [text(s['description'])+' · '+text(', '.join(s['segments']))+' · '+text(', '.join(s['countries']))+' · '+text(', '.join(s['languages'])),'',text('; '.join(s['limitations'])),'']
    section=['## Demande et position observées','',
             '| Besoin | Nature | Date | Sources |','|---|---|---|---|']
    for n in d['needs']:
        section += ['| '+' | '.join(text(x) for x in [n['text'],n['kind'],n['date'],', '.join(n['source_ids'])])+' |']
    section += ['', 'La demande documentée n’est pas un marché exhaustif. Les volumes, occurrences de questions et citations ne sont pas additionnés.','']
    for a in d['actors']:
        section += [text(a['name'])+' — '+text(', '.join(a['roles']))+' — '+text(', '.join(a['urls']))+' ; sources : '+text(', '.join(a['source_ids'])), '']
    if not d['actors']:section+=['Concurrence non observée dans ce dossier.','']
    # Strip only frontmatter; financial values are the same projection used in B.
    projection=render(bundle['result'],audience).split('---',2)[2].strip()
    section+=[projection,'','## Actions et moyens','',
              '| Action | Responsable proposé | Dépendances | Effort / coût : références | Date justifiée |','|---|---|---|---|---|']
    for a in d['actions']:
        section+=['| '+' | '.join(text(x if x is not None else 'Non renseigné') for x in [a['title'],a['owner'],', '.join(a['dependencies']),str(a['effort_metric_id'])+' / '+str(a['cost_metric_id']),a['planned_date']])+' |']
    section+=['','Les valeurs et sources de ces références sont conservées dans le résultat commun. Aucun calendrier ni budget par défaut.','']
    for o in d['opportunities']:
        m=o['measurement']
        section += ['### Suivi : '+text(o['title']),'',text(m['indicator'])+' ; '+text(m['formula']), '',
                    'Poursuivre : '+text(m['continue_if'])+' Réviser : '+text(m['revise_if'])+' Arrêter : '+text(m['stop_if']),
                    '', 'Responsable : '+text(m['owner'])+' ; revue : '+text(m['review_date'])+' ; attribution : '+text(m['attribution']), '']
    return body.replace(CONTEXT,'\n'.join(context)).replace(SUMMARY,'\n'.join(section))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input');p.add_argument('--body',required=True);p.add_argument('--output',required=True)
    p.add_argument('--audience',choices=['audit','geo'],required=True)
    a=p.parse_args();b=load_bundle(a.input)
    output=assemble_report(b,Path(a.body).read_text(),a.audience)
    write_output(a.output,output,a.input);record_execution(b,__file__,a.output,[a.body])


if __name__=='__main__':main()
