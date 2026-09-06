import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = '<li><a href="#graphify" class="relative font-mono text-[0.8rem] uppercase tracking-widest transition-colors duration-200 text-accent hover:text-white"><span class="relative">Graphify</span></a></li>'
if target in c:
    c = c.replace(target, '')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Nav cleaned!')
else:
    print('Target not in index.html')
