"""Explicit, reversible reuse. No collection and no guessed legacy conversion.

reuse: exact contract bytes plus review receipt.
legacy: curated contract plus explicit JSON pointer mappings, original preserved.
"""
import argparse
import hashlib
import json
from datetime import date
from pathlib import Path
from common import load, dump
from valider import validate


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pointer(data, path):
    if not path.startswith('/'):raise ValueError('JSON pointer absolu requis.')
    for part in path[1:].split('/'):
        part=part.replace('~1','/').replace('~0','~')
        data=data[int(part)] if isinstance(data,list) else data[part]
    return data


def import_contract(source, output, review, contract=None, mapping=None):
    source=Path(source).resolve();output=Path(output).resolve()
    if output.exists() or 'raw' in output.parts:raise ValueError('Un nouveau dossier hors raw/ est requis.')
    r=load(review)
    if r.get('source_sha256')!=sha(source):raise ValueError('La relecture ne porte pas sur cette source.')
    if not r.get('reviewer') or not r.get('rationale') or r.get('scope_compatible') is not True:
        raise ValueError('Auteur, justification et périmètre compatible requis ; sinon préparer un nouveau cadrage.')
    date.fromisoformat(r['date'])
    if r.get('freshness') not in ('retained_with_limits','current_for_scope'):
        raise ValueError('Fraîcheur non confirmée pour le périmètre ; collecte à proposer.')
    original=load(source);input_path=Path(contract).resolve() if contract else source
    data=load(input_path)
    checked=validate(data)
    if not checked['valid']:raise ValueError('; '.join(str(e) for e in checked['errors']))
    links=[]
    if contract:
        if not mapping:raise ValueError('Correspondance explicite requise pour un ancien format.')
        links=load(mapping)
        available={m['id']:m for m in data['metrics'] if m['value'] is not None and m['status']!='hypothesis'}
        if len({x['metric_id'] for x in links})!=len(links):raise ValueError('Correspondance dupliquée.')
        if set(available)!={x['metric_id'] for x in links}:raise ValueError('Chaque métrique disponible non hypothétique exige une correspondance.')
        for link in links:
            m=available[link['metric_id']]
            if not link.get('rationale'):raise ValueError('Justification de correspondance requise.')
            if pointer(original,link['pointer'])!=m['value']:raise ValueError('Valeur modifiée pendant l’import : '+m['id'])
            if not any(s['id'] in m['source_ids'] and s['sha256']==sha(source) and s['origin']==str(source) for s in data['sources']):
                raise ValueError('Empreinte et chemin originaux manquants : '+m['id'])
        if any(v.get('status')=='approved' for v in validations(data)):
            raise ValueError('Les accords historiques restent dans l’original ; une adaptation ne transfère pas leur approbation.')
    receipt={'mode':'legacy_explicit' if contract else 'audit_to_geo',
             'source_path':str(source),'source_sha256':sha(source),
             'contract_sha256':sha(input_path),'review':r,'mapping':links,
             'dates_refreshed':False,'approvals_granted':False,'new_collection':False,
             'rollback':'Conserver le dossier source ; retirer cette nouvelle version du point d’entrée sans effacer les archives.'}
    output.mkdir(parents=True)
    (output/'opportunites-business.json').write_bytes(input_path.read_bytes())
    (output/'original.json').write_bytes(source.read_bytes())
    (output/'import.json').write_text(dump(receipt),encoding='utf-8')
    return receipt


def validations(obj):
    if isinstance(obj,dict):
        for k,v in obj.items():
            if k=='validation':yield v
            else:yield from validations(v)
    elif isinstance(obj,list):
        for v in obj:yield from validations(v)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source');p.add_argument('--output',required=True);p.add_argument('--review',required=True)
    p.add_argument('--contract');p.add_argument('--mapping')
    a=p.parse_args();import_contract(a.source,a.output,a.review,a.contract,a.mapping)


if __name__=='__main__':main()
