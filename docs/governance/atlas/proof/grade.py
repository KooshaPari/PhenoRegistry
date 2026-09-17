#!/usr/bin/env python3
"""Compute a rubric-bound score from supplied receipts. No product/authority certification.

Usage: python proof/grade.py RUBRIC.json EVIDENCE_INDEX.json --root EVIDENCE_ROOT
Exit 0: consistent records and no failed/missing mandatory criteria in supplied data.
Exit 1: calculated but mandatory criteria blocked/unassessed. Exit 2: invalid input.
Never use this program's exit code alone as release authorization.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from datetime import datetime
from pathlib import Path
from typing import Any
import jsonschema

HERE = Path(__file__).resolve().parent
MAX_JSON_BYTES = 10 * 1024 * 1024
MAX_ARTIFACT_BYTES = 128 * 1024 * 1024


def strict_json(data: bytes) -> Any:
    if len(data) > MAX_JSON_BYTES:
        raise ValueError('JSON input exceeds reference-reader limit')
    def pairs(values):
        out = {}
        for key, val in values:
            if key in out:
                raise ValueError('duplicate JSON key: ' + key)
            out[key] = val
        return out
    def bad_constant(value):
        raise ValueError('nonfinite JSON constant: ' + value)
    result = json.loads(data, object_pairs_hook=pairs, parse_constant=bad_constant)
    def finite(value):
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError('nonfinite JSON number')
        if isinstance(value, dict):
            for child in value.values(): finite(child)
        elif isinstance(value, list):
            for child in value: finite(child)
    finite(result)
    return result


def validate_schema(value: Any, name: str) -> None:
    schema = strict_json((HERE / 'schemas' / (name + '.schema.json')).read_bytes())
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(value)


def utc(value: str) -> datetime:
    dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError('timezone required')
    return dt


def unique(rows: list[dict], key: str, label: str) -> None:
    vals = [r[key] for r in rows]
    if len(vals) != len(set(vals)):
        raise ValueError('duplicate ' + label)


def secure_payload(root: Path, name: str, expected_hash: str, maximum: int) -> bytes:
    """Bounded immutable-file read for trusted, quiescent evaluation inputs.

    Reject symlinks/absolute/traversal paths. Not a sandbox against hostile concurrent
    filesystem mutation: production adapters need handle-based secure acquisition.
    """
    rel = Path(name)
    if rel.is_absolute() or '..' in rel.parts or not rel.parts:
        raise ValueError('unsafe evidence path')
    root = root.resolve()
    p = root
    for part in rel.parts:
        p = p / part
        if p.is_symlink():
            raise ValueError('symlink evidence path')
    if not p.resolve().is_relative_to(root) or not p.is_file():
        raise ValueError('missing or escaped evidence file')
    if p.stat().st_size > maximum:
        raise ValueError('evidence exceeds reference-reader limit')
    data = p.read_bytes()
    if len(data) > maximum or not data:
        raise ValueError('empty or oversized evidence')
    if hashlib.sha256(data).hexdigest() != expected_hash:
        raise ValueError('evidence digest mismatch')
    return data


def grade(rubric: dict, index: dict, root: Path, rubric_bytes: bytes) -> dict:
    """Use declared outcomes; validate selected identity/provenance constraints.

    Does not run native tests, inspect pixels, verify signatures, or approve scope.
    Inputs may be synthetic or real-but-unattested; this status is preserved.
    """
    validate_schema(rubric, 'rubric')
    validate_schema(index, 'evidence-index')
    if strict_json(rubric_bytes) != rubric:
        raise ValueError('rubric bytes differ from parsed rubric')
    if hashlib.sha256(rubric_bytes).hexdigest() != index['rubric_sha256']:
        raise ValueError('rubric fingerprint mismatch')
    unique(rubric['categories'], 'id', 'categories')
    unique(rubric['criteria'], 'id', 'criteria')
    unique(index['receipts'], 'path', 'receipt paths')
    cats = {c['id']: c for c in rubric['categories']}
    criteria = {c['id']: c for c in rubric['criteria']}
    if not math.isclose(sum(c['weight'] for c in cats.values()), 100.0, abs_tol=1e-8, rel_tol=0):
        raise ValueError('category weights must sum to 100')
    for c in criteria.values():
        if c['category_id'] not in cats:
            raise ValueError('unknown criterion category')
        if c['critical'] and (not c['mandatory'] or c['passing_fraction'] != 1):
            raise ValueError('critical criteria require mandatory full satisfaction')
        if c['critical'] and c['allow_probabilistic']:
            raise ValueError('probabilistic-only critical qualification disallowed')
    totals = {cid: sum(c['weight'] for c in criteria.values() if c['category_id'] == cid) for cid in cats}
    if any(v == 0 for v in totals.values()):
        raise ValueError('category without criteria')
    as_of = utc(index['as_of'])
    observations = {}
    receipts_seen = set()
    for ref in index['receipts']:
        raw = secure_payload(root, ref['path'], ref['sha256'], MAX_JSON_BYTES)
        r = strict_json(raw)
        validate_schema(r, 'evaluator-receipt')
        if r['id'] in receipts_seen:
            raise ValueError('duplicate receipt id')
        receipts_seen.add(r['id'])
        cid = r['criterion_id']
        if cid not in criteria:
            raise ValueError('unknown criterion in receipt')
        if cid in observations:
            raise ValueError('multiple outcomes for one criterion require external adjudication')
        observations[cid] = r
    rows = []
    weighted_score = assessed_weight = unknown_weight = 0.0
    failed_mandatory = []; missing_mandatory = []
    for cid, c in criteria.items():
        weight = cats[c['category_id']]['weight'] * c['weight'] / totals[c['category_id']]
        r = observations.get(cid)
        issues = []
        if r is None:
            issues.append('missing outcome')
        else:
            for key in ('scope_id', 'subject_id', 'profile_id', 'source_revision', 'artifact_sha256', 'synthetic'):
                if r[key] != rubric[key]:
                    issues.append(key + ' mismatch')
            if r['oracle_sha256'] != c['oracle_sha256']:
                issues.append('oracle revision mismatch')
            age = (as_of - utc(r['observed_at'])).total_seconds() / 3600.0
            if age < 0:
                issues.append('future evidence')
            elif age > c['max_age_hours']:
                issues.append('stale evidence')
            if r['status'] != 'assessed':
                issues.append('execution ' + r['status'])
            if r['total_units'] != c['max_units']:
                issues.append('denominator mismatch')
            if r['earned_units'] > r['total_units']:
                issues.append('earned units exceed possible units')
            if r['evaluator_kind'] == 'model-assisted' and not c['allow_probabilistic']:
                issues.append('unapproved evaluator class')
            if not set(c['required_actions']) <= set(r['actions']):
                issues.append('required action route absent')
            modalities = set()
            paths = set()
            for art in r['artifacts']:
                # One artifact may support several outcomes but is not multiple
                # independent channels by relabelling the same file inside a receipt.
                if art['path'] in paths:
                    issues.append('duplicate artifact path')
                    continue
                paths.add(art['path'])
                try:
                    secure_payload(root, art['path'], art['sha256'], MAX_ARTIFACT_BYTES)
                    modalities.add(art['modality'])
                except (OSError, ValueError) as exc:
                    issues.append(str(exc))
            if not set(c['required_modalities']) <= modalities:
                issues.append('required observable modality absent')
        accepted = not issues
        fraction = r['earned_units'] / r['total_units'] if accepted else 0.0
        contribution = weight * fraction
        weighted_score += contribution
        if accepted:
            assessed_weight += weight
            if c['mandatory'] and fraction < c['passing_fraction']:
                failed_mandatory.append(cid)
        else:
            unknown_weight += weight
            if c['mandatory']:
                missing_mandatory.append(cid)
        rows.append({'criterion_id': cid, 'category_id': c['category_id'],
                     'effective_weight': weight, 'earned_fraction': fraction,
                     'contribution': contribution, 'evidence_admissible': accepted,
                     'issues': issues, 'outcome': 'UNKNOWN_OR_INADMISSIBLE' if not accepted else
                     ('SATISFIED' if fraction >= c['passing_fraction'] else 'BELOW_REQUIREMENT')})
    letter = next(name for threshold, name in [(95,'A'),(85,'B'),(70,'C'),(50,'D'),(0,'F')] if weighted_score >= threshold)
    gate = 'BLOCKED' if failed_mandatory else ('UNASSESSED' if missing_mandatory else 'NO_RECORDED_MANDATORY_BLOCKER')
    return {
        'status': 'CALCULATED_UNATTESTED',
        'scope_id': rubric['scope_id'], 'subject_id': rubric['subject_id'],
        'rubric_id': rubric['id'], 'rubric_revision': rubric['revision'],
        'rubric_sha256': index['rubric_sha256'], 'as_of': index['as_of'],
        'source_revision': rubric['source_revision'], 'artifact_sha256': rubric['artifact_sha256'],
        'profile_id': rubric['profile_id'], 'synthetic': rubric['synthetic'],
        'score_percent': round(weighted_score, 4), 'letter_grade': letter,
        'headline': f'{weighted_score:.2f}% / {letter} - {gate}', 'gate_state': gate,
        'failed_mandatory': failed_mandatory, 'missing_mandatory': missing_mandatory,
        'assessed_weight_percent': round(assessed_weight, 4),
        'unknown_weight_percent': round(unknown_weight, 4),
        'unknown_perfect_arithmetic_bound': [round(weighted_score,4), round(weighted_score+unknown_weight,4)],
        'bound_is_confidence_interval': False,
        'categories': [{'id': k, 'weight': v['weight'],
                        'score_percent': round(sum(x['contribution'] for x in rows if x['category_id']==k)/v['weight']*100,4)} for k,v in cats.items()],
        'criteria': rows,
        'product_qualified': False, 'producer_authenticity_verified': False,
        'oracle_truth_verified': False, 'approval_authenticity_verified': False,
        'release_authorized': False,
        'limitations': ['Arithmetic and local artifact integrity only; not native tests or image inspection.',
                        'Supplied outcomes/approvals are not authenticated by this program.',
                        'Concurrent hostile filesystem mutation is outside this reference-reader boundary.']}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rubric', type=Path); parser.add_argument('index', type=Path)
    parser.add_argument('--root', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        raw = args.rubric.read_bytes()
        result = grade(strict_json(raw), strict_json(args.index.read_bytes()), args.root, raw)
    except (OSError, ValueError, KeyError, TypeError, jsonschema.ValidationError, jsonschema.SchemaError) as exc:
        print(json.dumps({'status':'INPUT_ERROR','error':str(exc),'product_qualified':False,'release_authorized':False}))
        return 2
    print(json.dumps(result, indent=2))
    return 0 if result['gate_state'] == 'NO_RECORDED_MANDATORY_BLOCKER' else 1


if __name__ == '__main__':
    raise SystemExit(main())
