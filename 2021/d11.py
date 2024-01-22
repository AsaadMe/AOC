from copy import deepcopy

with open('input') as file:
    inp = file.readlines()
    board = [list(map(int,line.strip())) for line in inp]

def step(board):
    nxt_board = deepcopy(board)
    dirs = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
    flashed = set()
    stack = []
    for i in range(len(board)):
        for j in range(len(board[i])):            
            nxt_board[i][j] += 1
            if nxt_board[i][j] >= 10:
                stack.append((i,j))
    
    while stack:
        x,y = stack.pop()
        nxt_board[x][y] = 0
        flashed.add((x,y))
        neighs = [(x+dirx,y+diry) for dirx,diry in dirs 
                    if 0<=x+dirx<len(board) and 0<=y+diry<len(board[0])]
        
        for nx,ny in neighs:
            if (nx,ny) not in flashed:
                nxt_board[nx][ny] += 1
                if nxt_board[nx][ny] >= 10 and (nx,ny) not in stack:
                    stack.append((nx,ny))

    return nxt_board, len(flashed)

ans1 = 0
board1 = deepcopy(board)
for _ in range(100):
    board1, count = step(board1)
    ans1 += count

print('Part1:', ans1)

i = 1
board2 = deepcopy(board)
while True:
    board2, count = step(board2)
    if count == len(board)*len(board[0]):
        print('Part2:', i)
        break
    i += 1