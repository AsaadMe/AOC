from collections import deque

blizzards = set()
with open('2022/input.txt','r') as file:
    lines = file.readlines()[1:-1]
    shape = (len(lines[0].strip())-2, len(lines))
    for j, line in enumerate(lines):
        for i, c in enumerate(line.strip()[1:-1]):
            if c in ['>','<','v','^']:
                blizzards.add(((i,j), c))
            
def draw_board(board):
    board = {m for m,d in board}
    for j in range(shape[1]):
        for i in range(shape[0]):
            if (i,j) in board:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

def step_bliz(blizzards):
    mv = {'>':(1,0),'<':(-1,0),'v':(0,1),'^':(0,-1)}
    nxt_blizzards = set()
    for (i,j), dir in blizzards:
        nxt_bliz = (i+mv[dir][0], j+mv[dir][1])
        if nxt_bliz[0] >= shape[0]:
            nxt_bliz = (0, nxt_bliz[1])
        elif nxt_bliz[0] < 0:
            nxt_bliz = (shape[0]-1, nxt_bliz[1])
        elif nxt_bliz[1] >= shape[1]:
            nxt_bliz = (nxt_bliz[0], 0)
        elif nxt_bliz[1] < 0:
            nxt_bliz = (nxt_bliz[0], shape[1]-1)
            
        nxt_blizzards.add((nxt_bliz,dir))   
             
    return nxt_blizzards    

def get_neigbs(cans, pos):
    i,j = pos
    neigh = [(1,0),(-1,0),(0,1),(0,-1),(0,0)]
    return {(i+p,j+q) for p,q in neigh if (i+p,j+q) in cans}

pos = None
p = None
state = blizzards
bfsq = deque([(state,pos,1)])

while p != (shape[0]-1, shape[1]-1):
    state, pos, minutes = bfsq.popleft()
    minutes += 1
    whole_board = {(i,j) for i in range(shape[0]) for j in range(shape[1])}
    nstate = step_bliz(state)
    cant = {m for m,d in nstate}
    can = whole_board - cant
    
    if pos == None:
        psble_poses = {(0,0)}
    else:
        psble_poses = get_neigbs(can, pos)
        
        
    for p in psble_poses:
        if p == (shape[0]-1, shape[1]-1):
            print('Part1:', minutes)
            break
        
        elif p in can:
            bfsq.append((nstate, p, minutes))
       
    if not bfsq:
        bfsq.append((nstate,pos,minutes))