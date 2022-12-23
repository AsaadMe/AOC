import re

with open('2022/input.txt','r') as file:
    tiles, insts = file.read().split('\n\n')
    insts = re.split(r'(\D+)', insts)
    tiles = tiles.splitlines()

def draw_board(board):
    for j in range(1,max([a[1] for a in board])+1):
        for i in range(1,max([a[0] for a in board])+1):
            print(board.get((i,j), ' '), end='')
        print()
        
def cycle_dir(cur_dir, inst):
    dirs = 'RDLU'*2
    if inst == 'R':
        return dirs[dirs.index(cur_dir)+1]
    elif inst == 'L':
        return dirs[dirs.index(cur_dir,3)-1]
        
# top-left = (1,1)    
board = {}

for j, line in enumerate(tiles,1):
    sp = line.count(' ')
    line = line.strip()
    for i, c in enumerate(line,1):
        board[(i+sp,j)] = c
    
mv = {'R':(1,0), 'L':(-1,0), 'U':(0,-1), 'D':(0,1)}
cur_pos = (min([a[0] for a in board if a[1]==1]), 1)
cur_dir = 'R'

for inst in insts:
    if inst.isnumeric():
        for _ in range(int(inst)):
            nxt_pos = (cur_pos[0]+mv[cur_dir][0], cur_pos[1]+mv[cur_dir][1])
            if nxt_pos not in board:
                match cur_dir:
                    case 'R':
                        nxt_pos = (min([a[0] for a in board if a[1]==cur_pos[1]]), cur_pos[1])
                    case 'U':
                        nxt_pos = (cur_pos[0], max([a[1] for a in board if a[0]==cur_pos[0]]))
                    case 'L':
                        nxt_pos = (max([a[0] for a in board if a[1]==cur_pos[1]]), cur_pos[1])
                    case 'D':
                        nxt_pos = (cur_pos[0], min([a[1] for a in board if a[0]==cur_pos[0]]))
                    
            if board[nxt_pos] == '#':
                break
            else:
                cur_pos = nxt_pos
    else:
        cur_dir = cycle_dir(cur_dir, inst)

dir_score = {'R':0, 'D':1, 'L':2, 'U':3}        
print('Part1:', 1000*cur_pos[1] + 4*cur_pos[0] + dir_score[cur_dir])