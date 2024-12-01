from copy import deepcopy
from collections import defaultdict

with open('2020/input.txt','r') as file:
    input = [l.strip() for l in file.readlines()]
    
hexes = defaultdict(lambda: 'white') # initial all white
for line in input:
    line = list(line)
    addr = [0,0,0]  # https://i.stack.imgur.com/ySmUn.png
    direction = ''
    while line:
        direction += line.pop(0)
        if direction == 'e':
            addr[0] += 1
            addr[1] -= 1
        elif direction == 'se':
            addr[1] -= 1
            addr[2] += 1
        elif direction == 'sw':
            addr[0] -= 1
            addr[2] += 1
        elif direction == 'w':
            addr[0] -= 1
            addr[1] += 1
        elif direction == 'nw':
            addr[1] += 1
            addr[2] -= 1
        elif direction == 'ne':
            addr[0] += 1
            addr[2] -= 1
        else:
            continue
        
        if not line:
            addr = tuple(addr)
            if addr not in hexes:
                hexes[addr] = 'black'
            else:
                if hexes[addr] == 'white':
                    hexes[addr] = 'black'
                elif hexes[addr] == 'black':
                    hexes[addr] = 'white'
                    
        direction = ''
        
ans = sum([1 for v in hexes.values() if v=='black'])
print('Part1:', ans)

for i in range(100):
    next_hexes = deepcopy(hexes)
    to_check = set()
    for bhx,bhy,bhz in [k for k,v in hexes.items() if v=='black']:
        for x,y,z in [(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0),(0,1,-1),(1,0,-1),(0,0,0)]:
            to_check.add((bhx+x, bhy+y, bhz+z))
            
    for x,y,z in to_check:
        black_count = 0
        for nbx,nby,nbz in [(1,-1,0),(0,-1,1),(-1,0,1),(-1,1,0),(0,1,-1),(1,0,-1)]:
            if hexes[(x+nbx, y+nby, z+nbz)] =='black':
                black_count += 1
        
        if hexes[(x,y,z)]=='black' and (black_count==0 or black_count > 2):
            next_hexes[(x,y,z)] = 'white'
        elif hexes[(x,y,z)]=='white' and black_count==2:
            next_hexes[(x,y,z)] = 'black'
            
    hexes = next_hexes
    
ans = sum([1 for v in hexes.values() if v=='black'])
print('Part2:', ans)