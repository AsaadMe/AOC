import re

aunts = []

scan = {"children": 3, "cats": 7, "samoyeds": 2,
        "pomeranians": 3, "akitas": 0, "vizslas": 0,
        "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

with open("input") as file:
    inp = file.readlines()
    for line in inp:
        line.split(':')
        aunts.append({a[0]:int(a[1]) for a in re.findall(r'(\w+): (\d+)', line)})

for aunt in aunts:
    flg1 = True
    flg2 = True
    for el,num in aunt.items():
        if el in scan and num != scan[el]:
            flg1 = False
        if el in ('cats','trees') and el in scan and num <= scan[el]:
            flg2 = False
        if el in ('pomeranians','goldfish') and el in scan and num >= scan[el]:
            flg2 = False
        if el not in ('cats','trees','pomeranians','goldfish') and el in scan and num != scan[el]:
            flg2 = False
    if flg1:
        print('Part1:', aunts.index(aunt)+1)
    if flg2:
        print('Part2:', aunts.index(aunt)+1)