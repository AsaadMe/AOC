from itertools import combinations
import numpy as np

with open('2023/input.txt','r') as file:
    inp = file.readlines()
    inp = np.array([list(a.strip()) for a in inp])
    inp2 = inp.copy()

board = inp.copy()
j = 0
for i in range(inp.shape[0]):
    if all([a=='.' for a in inp[i,:]]):
        board = np.insert(board, i+j, '.', axis=0)        
        j += 1 
        
inp = board.copy()
j = 0
for i in range(inp.shape[1]):
    if all([a=='.' for a in inp[:,i]]):
        board = np.insert(board, i+j, '.', axis=1)        
        j += 1  

glxys = []
for i in range(board.shape[0]):
    for j in range(board.shape[1]):
        if board[i,j] == '#':
            glxys.append((i,j)) 

ans1 = 0
for p1,p2 in combinations(glxys, 2):
    ans1 += abs(p1[0]-p2[0])+abs(p1[1]-p2[1])                     

print('Part1: ', ans1)

###########################################

glxys = []
for i in range(inp2.shape[0]):
    for j in range(inp2.shape[1]):
        if inp2[i,j] == '#':
            glxys.append([i,j]) 
            
glxys = np.array(glxys, dtype=float)
x_empty = set(range(inp2.shape[0])) - set(glxys[:,0])
y_empty = set(range(inp2.shape[1])) - set(glxys[:,1])


n = 1000000 - 1
for st, x in enumerate(sorted(x_empty)):
    for i in range(len(glxys)):
        if glxys[i][0] >= x+st*n:
            glxys[i][0] += n
    

for st, y in enumerate(sorted(y_empty)):
    for i in range(len(glxys)):
        if glxys[i][1] >= y+st*n:
            glxys[i][1] += n
    
    
ans2 = []
for p1,p2 in combinations(glxys, 2):
    ans2.append(abs(p1[0]-p2[0])+abs(p1[1]-p2[1]))  
    # print(ans2)           
            
print('Part2: ', sum(ans2))