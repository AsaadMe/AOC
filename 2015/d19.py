import re

with open('input') as file:
    rules, molec = file.read().split('\n\n')
    rules = rules.splitlines()

nxt_molecs = set()
for rule in rules:
    f,s = rule.split(' => ')
    tosub = [(a.start(),a.end()) for a in re.finditer(f, molec)]
    for sub in tosub:
        i,j = sub
        nxt_molecs.add(molec[:i]+s+molec[j:])

print('Part1:', len(nxt_molecs))

# Part2: DFS?