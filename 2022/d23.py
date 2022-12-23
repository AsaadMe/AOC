from collections import Counter

board = {}
with open('2022/input.txt','r') as file:
    for j, line in enumerate(file):
        for i, c in enumerate(line.strip()):
            board[(i,j)] = c
    
def draw_board(board):
    for j in range(min([a[1] for a in board]),max([a[1] for a in board])+1):
        for i in range(min([a[0] for a in board]),max([a[0] for a in board])+1):
            print(board.get((i,j), '.'), end='')
        print()
        
        
def check_neighbs(board, p, dir):
    empty_sides = {'N':all([1 if a=='.' else 0 for a in [board.get((p[0]-1,p[1]-1),'.'),board.get((p[0],p[1]-1),'.'),board.get((p[0]+1,p[1]-1),'.')]]),
             'S':all([1 if a=='.' else 0 for a in [board.get((p[0]-1,p[1]+1),'.'),board.get((p[0],p[1]+1),'.'),board.get((p[0]+1,p[1]+1),'.')]]),
             'W':all([1 if a=='.' else 0 for a in [board.get((p[0]-1,p[1]-1),'.'),board.get((p[0]-1,p[1]),'.'),board.get((p[0]-1,p[1]+1),'.')]]),
             'E':all([1 if a=='.' else 0 for a in [board.get((p[0]+1,p[1]-1),'.'),board.get((p[0]+1,p[1]),'.'),board.get((p[0]+1,p[1]+1),'.')]])}
    
    if all(empty_sides.values()):
        return -1
    
    else:
        return empty_sides[dir]


def round(board, dirs_order):
    
    mv = {'N':(0,-1),'S':(0,1),'W':(-1,0),'E':(1,0)}
    nxt_board = board.copy()
    to_change = {}
    for (i,j), v in board.items():
        if v == '#':
            for o in range(4):
                dir = dirs_order[o]
                ch = check_neighbs(board, (i,j), dir)
                if ch == -1:
                    break
                elif ch:
                    to_change[(i,j)] = (i+mv[dir][0],j+mv[dir][1])
                    break

    c = Counter(to_change.values())
    for p,n in to_change.items():
        if c[n] == 1:
            nxt_board[p] = '.'
            nxt_board[n] = '#'
            
    return nxt_board

def part1(board):
    dir_mvs = ['N','S','W','E']
    for _ in range(10):
        board = round(board, dir_mvs)
        dir_mvs.append(dir_mvs.pop(0))

    shape = (max([a[0] for a in board if board[a]=='#'])+1-min([a[0] for a in board if board[a]=='#']),
            max([a[1] for a in board if board[a]=='#'])+1-min([a[1] for a in board if board[a]=='#']))   
     
    print('Part1:', shape[0]*shape[1]-sum([1 for a in board.values() if a=='#']))
    
def part2(board):
    dir_mvs = ['N','S','W','E']
    prev_board = board.copy()
    ans = 0
    while True:
        ans += 1  
        board = round(board, dir_mvs)
        dir_mvs.append(dir_mvs.pop(0))
        if board == prev_board:
            break
        else:
            prev_board = board.copy()
    
     
    print('Part2:', ans)    
    
    
part1(board)
part2(board)