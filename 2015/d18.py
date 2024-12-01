from copy import deepcopy
import numpy as np

with open('input') as file:
    board = np.array([list(line.strip()) for line in file.readlines()])
    h,w = board.shape

dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

def step(board, p2=False):
    if p2:
        for ij in [(0,0),(h-1,w-1),(h-1,0),(0,w-1)]:
            board[ij] = '#'
    next_board = deepcopy(board)
    
    for i in range(h):
        for j in range(w):
            neighbs = [(i+dir[0],j+dir[1]) for dir in dirs if 0<=i+dir[0]<h and 0<=j+dir[1]<w]
            on_neighbs = sum([1 for n in neighbs if board[n]=='#'])
            if board[i,j] == '.' and on_neighbs == 3:
                next_board[i,j] = '#'
            elif board[i,j] == '#' and on_neighbs not in (2,3):
                next_board[i,j] = '.'
    if p2:
        for ij in [(0,0),(h-1,w-1),(h-1,0),(0,w-1)]:
            next_board[ij] = '#'
    return next_board

steps = 100
p1_board = deepcopy(board)
for _ in range(steps):
    p1_board = step(p1_board)

print('Part1:', len(p1_board[p1_board=='#']))

p2_board = deepcopy(board)
for _ in range(steps):
    p2_board = step(p2_board,True)

print('Part2:', len(p2_board[p2_board=='#']))