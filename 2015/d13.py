from collections import defaultdict
from itertools import permutations

persons = defaultdict(dict)

with open('input') as file:
    inp = file.readlines()
    for line in inp:
        fname, _, sign, num, *others, sname = line.split()
        persons[fname][sname[:-1]] = int(num) if sign == 'gain' else -int(num)
    
def find_opt_happiness(persons):
    opt_happiness = 0
    for table in permutations(persons.keys()):
        happiness = 0
        for i in range(len(table)):
            happiness += persons[table[i]][table[i-1]]
            if i == len(table)-1: i = -1
            happiness += persons[table[i]][table[i+1]]
        if happiness > opt_happiness:
            opt_happiness = happiness
    return opt_happiness

print('Part1:', find_opt_happiness(persons))

persons['me'] = {fname:0 for fname in persons.keys()}
for person in persons:
    if person != 'me':
        persons[person]['me'] = 0

print('Part2:', find_opt_happiness(persons))