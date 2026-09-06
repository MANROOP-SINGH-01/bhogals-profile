with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

marker = '<script>\n(function() {\n  function injectGraphify()'
if marker in c:
    idx = c.index(marker)
    c = c[:idx] + '</body></html>\n'
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Graphify script completely removed from index.html!")
else:
    print("Marker not found in index.html")
