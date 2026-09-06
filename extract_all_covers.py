import json
import re

with open('_next/static/chunks/3zvdygm9kdu4r.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Let's extract the list of games
idx = content.find('b=[{title:')
if idx != -1:
    end_idx = content.find('],E=', idx)
    print("Found games array definition from", idx, "to", end_idx)
    raw = content[idx+2:end_idx+1]
    
    # Let's extract all cover values
    covers = re.findall(r'cover:\s*["\']([^"\']+)["\']', raw)
    titles = re.findall(r'title:\s*["\']([^"\']+)["\']', raw)
    print(f"Total games: {len(titles)}")
    for t, c in zip(titles, covers):
        print(f"  {c}.jpg -> {t}")
