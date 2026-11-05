"""Shared JSON/Decimal utilities. No network or modification of input files."""
import hashlib
import json
from decimal import Decimal
from pathlib import Path

VERSION = '0.1.0'
ROOT = Path(__file__).resolve().parent


def load(path):
    def reject(value):
        raise ValueError('Non-finite JSON value: ' + value)
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError('Duplicate JSON key: ' + key)
            out[key] = value
        return out
    return json.loads(Path(path).read_text(encoding='utf-8'), parse_float=Decimal,
                      parse_constant=reject, object_pairs_hook=unique)


def decimal_text(value):
    value = Decimal(str(value))
    if not value.is_finite():
        raise ValueError('Non-finite decimal')
    return format(value, 'f')


def serializable(value):
    if isinstance(value, Decimal):
        return decimal_text(value)
    if isinstance(value, dict):
        return {k: serializable(v) for k, v in value.items()}
    if isinstance(value, list):
        return [serializable(v) for v in value]
    return value


def dump(value):
    return json.dumps(serializable(value), ensure_ascii=False, indent=2, allow_nan=False) + '\n'


def fingerprint(value):
    # Approval binds the entire dossier, excluding approval metadata itself.
    def clean(v):
        if isinstance(v, dict):
            return {k: clean(x) for k, x in sorted(v.items()) if k != 'validation'}
        if isinstance(v, list):
            return [clean(x) for x in v]
        if isinstance(v, (int, float, Decimal)) and not isinstance(v, bool):
            d = Decimal(str(v))
            number = decimal_text(d)
            if '.' in number:
                number = number.rstrip('0').rstrip('.')
            return {'$number': '0' if d == 0 else number}
        return v
    return hashlib.sha256(json.dumps(clean(value), sort_keys=True, ensure_ascii=False,
                                     separators=(',', ':')).encode()).hexdigest()


def effective_validation(validation, digest):
    if validation['status'] == 'approved' and validation['content_sha256'] != digest:
        return 'needs_revision'
    return validation['status']


def artifact_hashes():
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in ('schema.json', 'common.py', 'valider.py', 'calculer.py', 'rendu.py', 'methode.md', 'requirements.txt')}


def write_output(path, content, input_path):
    target = Path(path).resolve()
    source = Path(input_path).resolve()
    if target == source or 'raw' in target.parts:
        raise ValueError('Refus d’écraser l’entrée ou d’écrire dans raw/.')
    if target.exists():
        raise ValueError('Sortie existante : choisir un nouveau chemin pour conserver les versions.')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding='utf-8')
