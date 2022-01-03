import numpy as np
from copy import deepcopy
import math

map_board = []
with open('input', 'r') as file:
    input = file.readlines()
    for line in input:
        map_board.append([1 if a=='#' else 0 for a in line.strip()])

map_board = np.array(map_board)

def count_trees(board, right, down):
    i,j = 0,0
    trees = 0
    while 1:
        if board[i,j] == 1:
            trees += 1
        i += down
        j += right
        
        if j >= board.shape[1]:
            board = np.hstack((board, board))     
        if i >= board.shape[0]:
            return trees

trs = []    
phases = [(1,1),(3,1),(5,1),(7,1),(1,2)]
for phase in phases:
    trs.append(count_trees(deepcopy(map_board), *phase))        

print(math.prod(trs))