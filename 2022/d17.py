from functools import cache
from itertools import cycle

with open('2022/input.txt', 'r') as file:
    jet_inst = file.readline()
    jet_inst_size = len(jet_inst)
    # jet_inst = cycle(jet_inst)


# bottom-left corner of rock -> rock pixels
rock_funcs = [lambda x,y:set([(x+i,y) for i in range(4)]),
        lambda x,y:{(x+1,y+2),(x+1,y)} | set([(x+i,y+1) for i in range(3)]),
        lambda x,y:set([(x+i,y) for i in range(3)]) | set([(x+2,y+i) for i in range(1,3)]),
        lambda x,y:set([(x,y+i) for i in range(4)]),
        lambda x,y:{(x,y),(x+1,y),(x,y+1),(x+1,y+1)}]

def draw_board(board):
    for j in range(max([a[1] for a in board]),-1,-1):
        for i in range(7):
            if (i,j) in board:
                print('#', end='')
            else:
                print('.', end='')
        print()

def spawn_point(screen):  
    return (2,max(screen,key=lambda x:x[1],default=(0,-1))[1]+4)

def horiz_rock(rock:set[tuple], direction):
    nxt_rock = set()
    if direction == 1 and max(rock,key=lambda x:x[0])[0] < wall[1]:
        for q in rock:
            nxt_rock.add((q[0]+1,q[1]))
        if all([1 if a not in screen else 0 for a in nxt_rock ]):
            return nxt_rock
    elif direction == -1 and min(rock,key=lambda x:x[0])[0] > wall[0]:
        for q in rock:
            nxt_rock.add((q[0]-1,q[1]))
        if all([1 if a not in screen else 0 for a in nxt_rock ]):
            return nxt_rock
    return rock

def vertic_rock(rock:set[tuple], screen):
    nxt_rock = set()
    for q in rock:
        nxt_rock.add((q[0],q[1]-1))
    if min(nxt_rock,key=lambda x:x[1])[1] >= 0 and all([1 if a not in screen else 0 for a in nxt_rock ]):
        return (0, nxt_rock)
    else:
        return (1, rock)

def normal(screen):
    if screen:
        if m := max([b for a,b in screen]) >= 100:
            return {(a,b-m+30) for a,b in screen if b >= m-30}
    return screen

screen = set()    
wall = (0,6)
rock_count_limit = 2022

@cache
def step_rock(screen, insts, rock):
    screen, rock = set(screen), set(rock)
    i = 0
    while True:
        change_x = 1 if insts[i] == '>' else -1
        i += 1
        rock = horiz_rock(rock, change_x)
        stop, rock = vertic_rock(rock, screen)
        if stop:
            screen |= rock
            return (screen, insts[i:]+insts[:i])
        
        
rock_count = 0
ans = 0
insts = jet_inst
for rock_func in cycle(rock_funcs):
    rock_count += 1
    
    # screen = normal(screen)
    rock = rock_func(*spawn_point(screen))
    screen, insts = step_rock(tuple(sorted(screen)), insts, tuple(sorted(rock)))
        
    if rock_count >= rock_count_limit:
        break
    
print('Part1:', max([a[1] for a in screen])+1)

    
