import numpy as np
from copy import deepcopy
with open('input.txt', 'r') as file:
    inp = file.readlines()

def make_board(inp):
    board = set()
    board.add((0,0))  
    curpos = (0,0)  
    
    for line in inp:
        dir, size, color = line.split()
        size = int(size)
            
        if dir == 'R':
            for i in range(1,size+1):
                board.add((curpos[0], curpos[1]+i))
            curpos = (curpos[0], curpos[1]+i)
        if dir == 'L':
            for i in range(1,size+1):
                board.add((curpos[0], curpos[1]-i))
            curpos = (curpos[0], curpos[1]-i)
        if dir == 'U':
            for i in range(1,size+1):
                board.add((curpos[0]-i, curpos[1]))
            curpos = (curpos[0]-i, curpos[1])
        if dir == 'D':
            for i in range(1,size+1):
                board.add((curpos[0]+i, curpos[1]))
            curpos = (curpos[0]+i, curpos[1])
            
    min_x = -min(board, key=lambda x: x[0])[0]        
    min_y = -min(board, key=lambda x: x[1])[1]  
    
    normalized_board = set()
    for point in board:
        normalized_board.add((point[0]+min_x,point[1]+min_y))
    return normalized_board

def draw_board(board, tofile=False):
    with open('out2.txt','w') as out:
        for i in range(max(board, key=lambda x: x[0])[0]+1):
            for j in range(max(board, key=lambda x: x[1])[1]+1):
                if (i,j) in board:
                    if tofile:
                        out.write('#')
                    else:
                        print('#', end='')
                else:
                    if tofile:
                        out.write('.')
                    else:
                        print('.', end='')
            if tofile:
                out.write('\n')
            else:
                print()
        
        
def part1_buggy(board):
    nxt_board = board.copy()
    tmp_energic = set()
    inside = False
    lastin = False
    ans = 0
    tmp_ans = 0
    for i in range(1,max(board, key=lambda x: x[0])[0]):
        for j in range(max(board, key=lambda x: x[1])[1]+1):
            if (i,j) in board and not inside:
                lastin = True
                tmp_energic = set()
                tmp_ans = 0
            elif (i,j) not in board and lastin:
                inside = True
                tmp_ans += 1
                tmp_energic.add((i,j))
            elif (i,j) in board and inside:
                inside = False
                lastin = False
                ans += tmp_ans
                nxt_board |= tmp_energic
        tmp_energic = set()
        tmp_ans = 0
        lastin = False 
        inside = False  
    draw_board(nxt_board, tofile=True)    
    return ans+len(board)

def part1(board):
    loc = (0, 0)
    x = []
    y = []
    dirs = {"U": (1, 0), "D": (-1, 0), "R": (0, 1), "L": (0, -1)}
    
    for line in open('input.txt','r'):
        a, b, _ = line.strip().split()
        dir = dirs[a]
        size = int(b)
        loc = (loc[0]+size*dir[0], loc[1]+size*dir[1])
        x.append(loc[0])
        y.append(loc[1])
        
    # shoelace
    area = 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
    
    # pick's: A = i + b/2 - 1
    I = area + 1 - len(board) // 2
    return I + len(board)


def part2():
    loc = (0, 0)
    x = []
    y = []
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    b = 0
    
    for line in open('input.txt','r'):
        _, _, color = line.strip().split()
        dir = dirs[int(color[-2])]
        size = int(color[-7:-2], 16)
        b += size
        loc = (loc[0]+size*dir[0], loc[1]+size*dir[1])
        x.append(loc[0])
        y.append(loc[1])
    x = np.array(x,dtype=np.int64)
    y = np.array(y,dtype=np.int64)
        
    area = 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
    I = area + 1 - b // 2
    return I + b

board = make_board(inp)
print('Part1: ', part1(board))
print('Part1: ', part2())