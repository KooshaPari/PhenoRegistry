#!/usr/bin/env python3
"""Verify payload bytes against the bundled integrity manifest (not a digital signature)."""
from pathlib import Path
import hashlib,json,sys
from build_manifest import payload_paths
ROOT=Path(__file__).resolve().parents[1]
def main():
    try:
        manifest=json.loads((ROOT/'FILE_MANIFEST.json').read_text(encoding='utf-8'))
        expected={entry['path'] for entry in manifest['files']}
        if len(expected)!=len(manifest['files']):raise ValueError('Duplicate manifest entries')
        observed={p.relative_to(ROOT).as_posix() for p in payload_paths(ROOT)}
        if expected!=observed:raise ValueError('Missing or unlisted payload files')
        for entry in manifest['files']:
            path=(ROOT/entry['path']).resolve()
            if not path.is_relative_to(ROOT.resolve()):
                raise ValueError('Manifest path escapes package root')
            raw=path.read_bytes()
            if len(raw)!=entry['bytes'] or hashlib.sha256(raw).hexdigest()!=entry['sha256']:
                raise ValueError('Integrity mismatch: '+entry['path'])
        expected_sums=''.join(f"{x['sha256']}  {x['path']}\n" for x in manifest['files'])
        if (ROOT/'SHA256SUMS.txt').read_text(encoding='utf-8')!=expected_sums:raise ValueError('Checksum list disagrees with manifest')
        print(f"Verified {len(manifest['files'])} payload files. Integrity comparison only; no signature or operational approval.")
        return 0
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print('Manifest verification failed: '+str(exc),file=sys.stderr)
        return 2
if __name__=='__main__':raise SystemExit(main())
