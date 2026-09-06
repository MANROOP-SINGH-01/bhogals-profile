import os
import re

chunks_dir = '_next/static/chunks'
chunk_files = [os.path.join(chunks_dir, f) for f in os.listdir(chunks_dir) if f.endswith('.js')]

print(f"Total chunk files: {len(chunk_files)}")

asset_refs = set()
chunk_refs = set()

# Pattern for static/media, sounds, models, glb, hdr, etc.
patterns = [
    r'static/media/[a-zA-Z0-9_\.\-]+',
    r'sounds/[a-zA-Z0-9_\.\-/]+',
    r'static/chunks/[a-zA-Z0-9_\.\-]+',
    r'[a-zA-Z0-9_\.\-]+\.(?:glb|gltf|hdr|bin|mp3|wav|png|jpg|woff2)'
]

for cf in chunk_files:
    try:
        with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            for p in patterns:
                for match in re.findall(p, content):
                    if 'static/chunks/' in match:
                        chunk_refs.add(match)
                    else:
                        asset_refs.add(match)
    except Exception as e:
        print(f"Error reading {cf}: {e}")

print(f"Found {len(chunk_refs)} chunk references in chunks")
print(f"Found {len(asset_refs)} asset references in chunks")

# Check which chunk refs are missing
missing_chunks = []
for cr in sorted(chunk_refs):
    local_path = os.path.join('_next', cr)
    if not os.path.exists(local_path):
        missing_chunks.append(cr)

print(f"Missing chunks count: {len(missing_chunks)}")
for mc in missing_chunks[:20]:
    print(f"  MISSING CHUNK: {mc}")

# Check which asset refs might be missing
missing_assets = []
for ar in sorted(asset_refs):
    # try various locations: root, _next/, _next/static/, public/
    possible = [
        ar,
        os.path.join('_next', ar),
        os.path.join('_next/static/media', ar),
        os.path.join('sounds', ar)
    ]
    if not any(os.path.exists(p) for p in possible):
        missing_assets.append(ar)

print(f"Missing asset candidate count: {len(missing_assets)}")
for ma in missing_assets[:25]:
    print(f"  Potential missing asset: {ma}")
