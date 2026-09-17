"""Deliberately bounded toy implementation variants used only by demo_loop.py.

No real user data or production backup system is used. The no-op variant exists
as a negative control; do not copy it into a product.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

def records_digest(records: object) -> str:
    data=json.dumps(records,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
    return hashlib.sha256(data).hexdigest()

def restore_noop(backup: Path, target: Path) -> str:
    # Intentionally wrong: success text without restoring anything.
    return 'restored successfully'

def restore_checked(backup: Path, target: Path) -> str:
    value=json.loads(backup.read_text(encoding='utf-8'))
    records=value['records']
    if records_digest(records)!=value['records_sha256']:
        raise ValueError('backup integrity mismatch')
    target.write_text(json.dumps({'records':records},sort_keys=True),encoding='utf-8')
    return 'restored successfully'
