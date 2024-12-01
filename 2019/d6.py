from functools import cache
from collections import defaultdict
from collections import deque

with open('2019/input.txt', 'r') as file:
    input = [l.strip().split(')') for l in file.readlines()]

@cache    
def count_orbits(planet:str):
    if planet == 'COM':
        return 0
    
    for rel in input:
        if rel[1] == planet:
            direct_orbit = rel[0]
            
    return 1 + count_orbits(direct_orbit)

def part1():
    all_counts = 0
    for _, pl in input:
        all_counts += count_orbits(pl)
        
    print('Part1:', all_counts)
    
def part2(): # iterative bfs
    adj_lists = defaultdict(list)
    for v1,v2 in input:
        if v2 == 'YOU':
            start_node = v1
        elif v2 == 'SAN':
            end_node = v1  
        else:    
            adj_lists[v1].append(v2)
            adj_lists[v2].append(v1)

    q = deque()
    q.append(start_node)
    
    visited = [start_node]
    levels = {a:-1 for a in adj_lists}
    levels[start_node] = 0
    
    while q:
        cur_node = q.popleft()
        
        for neigh in adj_lists[cur_node]:
            if neigh not in visited:
                q.append(neigh)
                visited.append(neigh)
                levels[neigh] = levels[cur_node] + 1

     
    print('Part2:', levels[end_node])
    
part1()
part2()