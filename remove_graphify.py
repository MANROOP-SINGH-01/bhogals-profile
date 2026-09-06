import sys

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

start_marker = '<!-- GRAPHIFY INTERACTIVE KNOWLEDGE GRAPH SECTION -->'
end_marker = '<section id="contact"'

if start_marker in c:
    p1 = c.index(start_marker)
    p2 = c.index(end_marker, p1)
    new_c = c[:p1] + c[p2:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_c)
    print('Removed graphify section successfully! New length:', len(new_c))
else:
    print('start_marker not found')
