from collections import defaultdict
from itertools import permutations
import re

graph = defaultdict(dict)
with open('input') as file:
    for line in file.readlines():
        n1,n2,w = re.split(r' to | = ', line)
        graph[n1][n2] = int(w)
        graph[n2][n1] = int(w)

nodes = list(graph)
shortest = float('inf')
longest = 0
for perm in permutations(nodes):
    dist = 0
    for i in range(1,len(perm)):
        dist += graph[perm[i-1]][perm[i]]
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print('Part1:', shortest)
print('Part2:', longest)