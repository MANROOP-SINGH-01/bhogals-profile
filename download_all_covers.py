import urllib.request
import os
import re

with open('_next/static/chunks/3zvdygm9kdu4r.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

idx = content.find('b=[{title:')
end_idx = content.find('],E=', idx)
raw = content[idx+2:end_idx+1]

covers = re.findall(r'cover:\s*["\']([^"\']+)["\']', raw)

os.makedirs('covers', exist_ok=True)
base_url = 'https://aditya-shelke-portfolio.vercel.app/covers/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

success = 0
failed = []

for c in covers:
    filename = f"{c}.jpg"
    target_path = os.path.join('covers', filename)
    if os.path.exists(target_path) and os.path.getsize(target_path) > 100:
        success += 1
        continue

    url = base_url + filename
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(target_path, 'wb') as out:
            data = resp.read()
            out.write(data)
            success += 1
            print(f"Downloaded {filename} ({len(data)} bytes)")
    except Exception as e:
        failed.append((filename, str(e)))
        print(f"Failed {filename}: {e}")

print(f"\nDone: {success}/{len(covers)} downloaded successfully.")
if failed:
    print(f"Failed count: {len(failed)}")
