import os
import re

chunks_dir = '_next/static/chunks'
chunk_files = [os.path.join(chunks_dir, f) for f in os.listdir(chunks_dir) if f.endswith('.js')]

found = []
for cf in chunk_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        matches = re.findall(r'["\'](/[^"\']+\.(?:glb|gltf|hdr|bin|png|jpg|mp3|wav|json|svg))["\']', content)
        for m in matches:
            found.append(m)

print("Unique absolute asset paths in chunks:")
for p in sorted(set(found)):
    exists = os.path.exists(p.lstrip('/'))
    print(f"  {p} -> exists: {exists}")
