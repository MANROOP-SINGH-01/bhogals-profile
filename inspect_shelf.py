with open('_next/static/chunks/3zvdygm9kdu4r.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

idx = content.find('Pull one out')
print("Found 'Pull one out' at:", idx)
start = max(0, idx - 4000)
end = min(len(content), idx + 4000)
print(content[start:end])
