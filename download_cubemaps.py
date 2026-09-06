import urllib.request
import os

files = ['nx.png', 'ny.png', 'nz.png', 'px.png', 'py.png', 'pz.png']
base_url = 'https://aditya-shelke-portfolio.vercel.app/'
headers = {'User-Agent': 'Mozilla/5.0'}

for f in files:
    url = base_url + f
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(f, 'wb') as out:
            data = resp.read()
            out.write(data)
            print(f"Downloaded {f}: {len(data)} bytes")
    except Exception as e:
        print(f"File {f} not on server or error: {e}")
