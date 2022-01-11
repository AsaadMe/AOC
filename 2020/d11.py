import numpy as np
import itertools
from copy import deepcopy

with open('2020/input.txt','r') as file:
    input = file.readlines()
    input = np.array([list(a.strip()) for a in input])

def get_neighbors(board, i,j): # for part1
    neighs = []
    combs = list(itertools.product([-1,0,1], repeat=2))
    combs.remove((0,0))
    for x,y in combs:
        if 0 <= x+i <= board.shape[0]-1 and 0 <= y+j <= board.shape[1]-1:
            neighs.append(board[i+x,j+y])
        
    return neighs

def get_true_neighbors(board, i,j): # for part2
    neighs = []
    combs = list(itertools.product([-1,0,1], repeat=2))
    combs.remove((0,0))
    for x,y in combs:
        xt = x
        yt = y
        while True:
            if 0 <= x+i <= board.shape[0]-1 and 0 <= y+j <= board.shape[1]-1:
                if board[i+x,j+y] != '.':
                    neighs.append(board[i+x,j+y])
                    break
                else:
                    x += xt
                    y += yt
            else:
                break
    
    return neighs    

def step_p1(board):
    next_board = deepcopy(board)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            neighs = get_neighbors(board, i,j)
            if board[i,j] == 'L' and '#' not in neighs:
                next_board[i,j] = '#'
            elif board[i,j] == '#' and neighs.count('#') >= 4:
                next_board[i,j] = 'L'
                
    return next_board

def step_p2(board):
    next_board = deepcopy(board)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            neighs = get_true_neighbors(board, i,j)
            if board[i,j] == 'L' and '#' not in neighs:
                next_board[i,j] = '#'
            elif board[i,j] == '#' and neighs.count('#') >= 5:
                next_board[i,j] = 'L'
                
    return next_board

def part1():
    board = input
    while True:
        next_board = step_p1(board)
        if np.array_equal(next_board, board):
            board = next_board
            break
        else:
            board = next_board
            
    print('Part1:', list(board.flatten()).count('#'))

def part2():
    board = input
    while True:
        next_board = step_p2(board)
        if np.array_equal(next_board, board):
            board = next_board
            break
        else:
            board = next_board
            
    print('Part2:', list(board.flatten()).count('#'))

    
part1()
part2()