#!/usr/bin/env python3
"""Offline illustrative plan consistency; never authorizes or runs applications."""
from __future__ import annotations
import copy
import json
import sys
from graphlib import TopologicalSorter, CycleError
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parent

def validate_plan(manifests: list[dict], plan: dict) -> dict:
    """Validate selected shape/reference invariants; no trust/runtime verdict."""
    errors: list[str] = []
    ms=json.loads((ROOT/'schemas/manifest.schema.json').read_text())
    ps=json.loads((ROOT/'schemas/composition-plan.schema.json').read_text())
    for i, m in enumerate(manifests):
        errors += [f'manifest[{i}]: {e.message}' for e in jsonschema.Draft202012Validator(ms).iter_errors(m)]
    errors += [f'plan: {e.message}' for e in jsonschema.Draft202012Validator(ps).iter_errors(plan)]
    if errors:
        return result(errors)
    def unique(rows: list[dict], key: str, label: str) -> None:
        vals=[x[key] for x in rows]
        if len(vals)!=len(set(vals)):errors.append(f'duplicate {label}')
    unique(manifests,'id','manifest IDs');unique(manifests,'product_id','product IDs')
    unique(plan['package_locks'],'manifest_id','package locks')
    unique(plan['bindings'],'id','binding IDs');unique(plan['mounts'],'id','mount IDs')
    products={m['product_id']:m for m in manifests}
    byid={m['id']:m for m in manifests}
    locks={x['manifest_id']:x['artifact_sha256'] for x in plan['package_locks']}
    for m in manifests:
        unique(m['provided_capabilities'],'id','capability IDs')
        unique(m['host_slots'],'id','slot IDs')
        for c in m['provided_capabilities']:
            if c['data_authority'] not in m['state_authorities']:errors.append('offer owner absent from provider authorities')
    for mid,digest in locks.items():
        if mid not in byid:errors.append('unknown package lock')
        elif byid[mid]['artifact_sha256']!=digest:errors.append('artifact lock mismatch')
    primary=plan['primary_app']
    if primary not in products:errors.append('unknown primary app')
    elif products[primary]['id'] not in locks:errors.append('unlocked primary app')
    bindings={b['id']:b for b in plan['bindings']}
    for b in plan['bindings']:
        if b['principal']!=plan['principal'] or b['workspace']!=plan['workspace']:errors.append('scope mismatch')
        if not b['grant_references']:errors.append('missing grant references')
        if b['consumer'] not in products or b['provider'] not in products:
            errors.append('unknown binding product');continue
        for who in (b['consumer'],b['provider']):
            if products[who]['id'] not in locks:errors.append('unlocked binding product')
        offers=[x for x in products[b['provider']]['provided_capabilities'] if x['id']==b['capability']]
        if len(offers)!=1:errors.append('unknown or ambiguous capability')
        else:
            offer=offers[0]
            if offer['semantic_contract']!=b['semantic_contract']:errors.append('semantic contract mismatch')
            if offer['data_authority']!=b['data_authority']:errors.append('authority substitution')
        if not set(b['depends_on'])<=set(bindings):errors.append('unknown startup dependency')
    try:list(TopologicalSorter({b['id']:b['depends_on'] for b in plan['bindings']}).static_order())
    except CycleError:errors.append('startup cycle')
    mounts={m['id']:m for m in plan['mounts']}
    for m in plan['mounts']:
        if m['binding_id'] not in bindings:
            errors.append('unknown surface binding');continue
        if m['host']!=primary or m['host']!=bindings[m['binding_id']]['consumer']:errors.append('wrong perspective host')
        h=products.get(m['host'])
        slots=[s for s in h['host_slots'] if s['id']==m['slot_id']] if h else []
        if len(slots)!=1:errors.append('unknown host slot')
        elif m['adapter'] not in slots[0]['supported_adapters']:errors.append('unsupported surface adapter')
        if m['parent_mount'] is not None and m['parent_mount'] not in mounts:errors.append('unknown parent mount')
    try:list(TopologicalSorter({m['id']:[] if m['parent_mount'] is None else [m['parent_mount']] for m in plan['mounts']}).static_order())
    except CycleError:errors.append('mount cycle')
    return result(errors)

def result(errors: list[str]) -> dict:
    return {'status':'INVALID' if errors else 'EXAMPLE_RECORDS_CONSISTENT','errors':errors,
            'activation_authorized':False,'grant_authenticity_checked':False,'product_behavior_verified':False,
            'schema_scope':'synthetic-planning-examples-only'}

def main() -> int:
    try:
        manifests=json.loads((ROOT/'examples/manifests.json').read_text())
        out={n:validate_plan(manifests,json.loads((ROOT/f'examples/{n}.json').read_text())) for n in ['perspective-a','perspective-b']}
        print(json.dumps(out,indent=2))
        return 1 if any(x['errors'] for x in out.values()) else 0
    except (OSError,ValueError,jsonschema.exceptions.SchemaError) as e:
        print(json.dumps({'status':'INPUT_ERROR','error':str(e),'activation_authorized':False}));return 2
if __name__=='__main__':sys.exit(main())
