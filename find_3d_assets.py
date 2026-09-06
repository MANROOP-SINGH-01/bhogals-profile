import os
import re

chunks_dir = '_next/static/chunks'
chunk_files = [os.path.join(chunks_dir, f) for f in os.listdir(chunks_dir) if f.endswith('.js')]

models_and_hdrs = []
for cf in chunk_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        for ext in ['glb', 'gltf', 'hdr']:
            matches = re.findall(rf'["\']([^"\']+\.{ext})["\']', content)
            for m in matches:
                models_and_hdrs.append((cf, m))

print("Models and HDRs found in chunks:")
for cf, m in set(models_and_hdrs):
    print(f"  In {os.path.basename(cf)}: {m}")
