import os
import re

matches = []
for root, dirs, files in os.walk('.'):
    if any(p in root for p in ['.git', 'node_modules', 'graphify-out', '.gemini']):
        continue
    for f in files:
        if f.endswith(('.js', '.html', '.json', '.ts', '.tsx', '.css')):
            path = os.path.join(root, f)
            try:
                content = open(path, encoding='utf-8', errors='ignore').read()
                found = re.findall(r'(?:aditya|shelke)', content, re.I)
                if found:
                    matches.append((path, len(found)))
            except:
                pass

print("Files containing aditya/shelke:")
for m in matches:
    print(f"  {m[0]}: {m[1]} matches")
