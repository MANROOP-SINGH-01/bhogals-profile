import urllib.request
import os

url = "https://aditya-shelke-portfolio.vercel.app/models/desk-rig.glb"
target_dir = "models"
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, "desk-rig.glb")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

print(f"Downloading {url} ...")
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp, open(target_path, 'wb') as f:
        data = resp.read()
        f.write(data)
        print(f"SUCCESS! Downloaded {len(data)} bytes to {target_path}")
except Exception as e:
    print(f"Failed to download: {e}")
