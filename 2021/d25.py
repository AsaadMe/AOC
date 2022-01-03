import numpy as np
from copy import deepcopy

with open('input', 'r') as file:
    input = file.readlines()
    inp = [list(a.strip()) for a in input]
    board = np.array(inp)
    

def step(board):
    h,w = board.shape
    next_board = deepcopy(board)
    for i in range(0,h):
        for j in range(0,w):
            if j == w-1:
                if board [i,j] == '>' and board[i,0] == '.':
                    next_board[i,j] = '.'
                    next_board[i,0] = '>'
            
            else:
                if board [i,j] == '>' and board[i,j+1] == '.':
                    next_board[i,j] = '.'
                    next_board[i,j+1] = '>'
    
    next2_board = deepcopy(next_board)                
    for i in range(0,h):
        for j in range(0,w):                
            if i == h-1:
                if next_board [i,j] == 'v' and next_board[0,j] == '.':
                    next2_board[i,j] = '.'
                    next2_board[0,j] = 'v'
            
            else:
                if next_board [i,j] == 'v' and next_board[i+1,j] == '.':
                    next2_board[i,j] = '.'
                    next2_board[i+1,j] = 'v'
                        
    return next2_board

i = 0
while True:
    i+=1
    new_board = step(board)
    if np.array_equal(new_board, board):
        print(i)
        break
    else:
        board = new_board
