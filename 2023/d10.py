from pprint import pprint

board = []

with open('input.txt', 'r') as file:
    for line in file:
        board.append(['.']+list(line.strip())+['.'])
board = [['.']*len(board[0])]+board+[['.']*len(board[0])]

shape = len(board),len(board[0])
        
for i in range(shape[0]):
    for j in range(shape[1]):
        if board[i][j] == 'S':
            start = (i,j)
            
            
def walk(board, start):
    
    dirs = {'-':{'R':(0,1),'L':(0,-1)}, '7':{'R':(1,0),'U':(0,-1)},
            '|':{'U':(-1,0),'D':(1,0)} , 'J':{'D':(0,-1),'R':(-1,0)},
            'L':{'D':(0,1),'L':(-1,0)} ,'F':{'U':(0,1),'L':(1,0)}}
    
    main_dir = {'U':(-1,0), 'D':(1,0), 'R':(0,1), 'L':(0,-1)}
   
    pos = start
    visited = []
    i = 0
    while 1:
        i += 1
        for n, ch in main_dir.items():
            change = 0,0
            npos = pos[0]+ch[0],pos[1]+ch[1]
            ntype = board[npos[0]][npos[1]]
            change = dirs.get(ntype,{}).get(n,(0,0))
            tpos = npos[0]+change[0],npos[1]+change[1]
            ntype = board[tpos[0]][tpos[1]]
                  
            if change != (0,0) and (npos not in visited) and ((npos[0]+change[0],npos[1]+change[1]) not in visited):
                if ((n == 'U' and ntype in '|F7') or
                    (n == 'D' and ntype in '|LJ') or
                    (n == 'R' and ntype in '-J7') or
                    (n == 'L' and ntype in '-FL')):
                    pos = npos[0]+change[0],npos[1]+change[1]
                    print(pos,board[pos[0]][pos[1]])
                    visited.append(npos)
                    visited.append(pos)
                    break
        if pos == start:
            break
        
    return i

# def walk2(board, start):
#     visited = []
#     cur = start
#     dirs = {'-':{'R':(0,1),'L':(0,-1)}, '7':{'R':(1,0),'U':(0,-1)},
#             '|':{'U':(-1,0),'D':(1,0)} , 'J':{'D':(0,-1),'R':(-1,0)},
#             'L':{'D':(0,1),'L':(-1,0)} ,'F':{'U':(0,1),'L':(1,0)}}
    
#     main_dir = {'U':(-1,0), 'D':(1,0), 'R':(0,1), 'L':(0,-1)}
   
#    for n, ch in main_dir.items():
       
            
    
print('Part1:', walk(board, start))