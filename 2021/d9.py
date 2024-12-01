from math import prod

with open('input') as file:
    board = [list(map(int, list(line.strip()))) for line in file.readlines()]

h,w = len(board),len(board[0])

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
lowpoints = []
for i in range(h):
    for j in range(w):
        neighs = [(i+x,j+y) for x,y in dirs if (0 <= i+x < h and 0 <= j+y < w)]
        if all([board[nx][ny] > board[i][j] for nx,ny in neighs]):    
            lowpoints.append((i,j))

print('Part1:', sum([1+board[i][j] for i,j in lowpoints]))

all_basins = []
for i,j in lowpoints:
    basins = [(i,j)]
    basincount = 0
    visited = set()
    visited.add((i,j))
    while basins:
        curx,cury = basins.pop(0)
        basincount += 1
        neighs = [(x+curx,y+cury) for x,y in dirs if (0 <= x+curx < h and 0 <= y+cury < w)]
        for nx,ny in neighs:
            if board[nx][ny] != 9 and (nx,ny) not in visited:
                visited.add((nx,ny))
                basins.append((nx,ny))

    all_basins.append(basincount)

print('Part2:', prod(sorted(all_basins)[-1:-4:-1]))