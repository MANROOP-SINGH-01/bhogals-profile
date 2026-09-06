import urllib.request
import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all script src and link href
scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)
links = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', html)

print(f"Total scripts in index.html: {len(scripts)}")
print(f"Total links in index.html: {len(links)}")

all_urls = scripts + links
missing = []
for url in all_urls:
    if url.startswith('http'):
        continue
    clean_url = url.split('?')[0]
    local_path = clean_url.lstrip('/')
    if not os.path.exists(local_path):
        print(f"MISSING STATIC FILE: {clean_url} (expected at {local_path})")
        missing.append(clean_url)

print(f"Missing files: {len(missing)}")
