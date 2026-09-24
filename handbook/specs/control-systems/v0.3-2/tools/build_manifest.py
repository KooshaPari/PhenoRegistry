#!/usr/bin/env python3
"""Build payload checksums; not a trusted signature or operational approval."""
from pathlib import Path
import hashlib
import json
ROOT=Path(__file__).resolve().parents[1]
EXCLUDE={'FILE_MANIFEST.json','SHA256SUMS.txt'}
def payload_paths(root):
    for p in sorted(root.rglob('*')):
        if '__pycache__' in p.parts or p.suffix=='.pyc':continue
        if p.is_symlink():raise ValueError('Symlink not permitted in release payload')
        if p.is_file() and p.relative_to(root).as_posix() not in EXCLUDE:yield p

def main():
    files=[]
    for p in payload_paths(ROOT):
        raw=p.read_bytes();files.append({'path':p.relative_to(ROOT).as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
    manifest={'version':'0.3.0','scope':'Payload integrity only; excludes FILE_MANIFEST.json, SHA256SUMS.txt and bytecode caches; not a signature.','files':files}
    (ROOT/'FILE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    (ROOT/'SHA256SUMS.txt').write_text(''.join(f"{x['sha256']}  {x['path']}\n" for x in files),encoding='utf-8')
    print(f'Hashed {len(files)} payload files')
if __name__=='__main__':main()
