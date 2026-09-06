with open('_next/static/chunks/3zvdygm9kdu4r.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

idx = content.find('valorant')
print("Found 'valorant' at:", idx)
start = max(0, idx - 200)
end = min(len(content), idx + 1500)
print(content[start:end])
