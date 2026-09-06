with open('_next/static/chunks/3id5ud61v2318.js', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("aditya.rig", "manroop.rig")
c = c.replace("/home/aditya", "/home/manroop")
c = c.replace("adityashelke", "manroopsinghbhogal")
c = c.replace("aditya", "manroop")

with open('_next/static/chunks/3id5ud61v2318.js', 'w', encoding='utf-8') as f:
    f.write(c)

print("Rebranded 3id5ud61v2318.js (hero 3D monitor boot sequence)!")
