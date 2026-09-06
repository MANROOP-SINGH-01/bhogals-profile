with open('_next/static/chunks/3zvdygm9kdu4r.js', 'r', encoding='utf-8') as f:
    c = f.read()

# Notice "ADITYA'S SHELF" -> replace with "MANROOP'S SHELF"
c = c.replace("ADITYA'S SHELF", "MANROOP'S SHELF")
c = c.replace("adityashelke", "manroopsinghbhogal")
c = c.replace("aditya", "manroop")

with open('_next/static/chunks/3zvdygm9kdu4r.js', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated 3zvdygm9kdu4r.js with MANROOP'S SHELF!")
