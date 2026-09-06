with open('_next/static/chunks/3zvdygm9kdu4r.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

idx = content.find('Pull one out')
# Let's search backward for 'let b=' or games list definition
pos = content.rfind('=[', 0, idx)
print("Position of '=[' before 'Pull one out':", pos)
if pos != -1:
    print(content[pos-50:pos+1500])

# Let's search for games array or titles
import re
titles = re.findall(r'title:\s*["\']([^"\']+)["\']', content)
print("Titles found in 3zvdygm9kdu4r.js:", titles[:20])

covers = re.findall(r'cover:\s*["\']([^"\']+)["\']', content)
print("Covers found:", covers[:20])

# Let's check image paths or covers in 3zvdygm9kdu4r.js
imgs = re.findall(r'["\'](/[^"\']+\.(?:png|jpg|jpeg|webp))["\']', content)
print("Images found:", set(imgs))
