with open('_next/static/chunks/3zvdygm9kdu4r.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

idx = content.find('G=')
# Let's search around G(e[t++]) or where covers are drawn/loaded
pos = content.find('let G=')
if pos == -1:
    pos = content.find('G=(0,')
if pos == -1:
    pos = content.find('G=')

print("Position:", pos)
print(content[pos-100:pos+2000])
