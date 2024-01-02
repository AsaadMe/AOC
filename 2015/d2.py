from math import prod
from itertools import combinations

ans = 0
ribbon = 0
for box in open('input','r'):
    dims = [int(a) for a in box.split('x')]

    smallest = float('inf')
    sumarea = 0
    for a1,a2 in combinations(dims,2):
        area = a1*a2
        if area < smallest: smallest = area
        sumarea += 2*area

    ribbon += sum(sorted(dims)[:2])*2 + prod(dims)

    ans += sumarea + smallest

print('Part1:', ans)
print('Part2:', ribbon)