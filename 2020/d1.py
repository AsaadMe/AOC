import itertools

with open('2020/input', 'r') as file:
    input = file.readlines()
    input = [int(a.strip()) for a in input]
    
for l1, l2, l3 in itertools.combinations(input, 3):
    if l1 + l2 + l3 == 2020:
        print(l1*l2*l3)