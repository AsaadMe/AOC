from math import prod
from string import digits, punctuation
punctuation = punctuation.replace('.','')

with open('input.txt','r') as file:
    board = [['.']+list(a)+['.'] for a in file.read().splitlines()]
    board = [['.']*len(board[0])]+board+[['.']*len(board[0])]

col, row = len(board[0]), len(board)
adj_ind = ((0,-1),(0,1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))
part_nums = []

for i in range(1,row-1):
    num_stack = []
    adjs = ''
    for j in range(1,col-1):
        if board[i][j] in digits:
            num_stack.append(board[i][j])
            adjs += ''.join([board[i+dir[0]][j+dir[1]] for dir in adj_ind])
            if board[i][j+1] not in digits:
                #test adjs
                if any([a in punctuation for a in adjs]):
                    part_nums.append(int(''.join(num_stack)))
                    
                num_stack.clear()
                adjs = ''
                    
                                       
print('Part1: ', sum(part_nums))


def find_parts(board, astr_pos):
    i,j = astr_pos
    parts = []
    
    #right
    part = ''
    while board[i][j+1] in digits:
        part += board[i][j+1]
        j+=1
    parts.append(part)
    i,j = astr_pos
    
    #left
    part = ''
    while board[i][j-1] in digits:
        part = board[i][j-1]+part
        j-=1
    parts.append(part)
    i,j = astr_pos
    
    #up-down
    for ud in (1,-1):
        if board[i+ud][j] in digits:
            part = board[i+ud][j]
        else:
            part = '.'
        while board[i+ud][j+1] in digits:
            part += board[i+ud][j+1]
            j+=1
        i,j = astr_pos
        while board[i+ud][j-1] in digits:
            part = board[i+ud][j-1]+part
            j-=1
            
        part = part.split('.')
        parts.extend(part) 
        i,j = astr_pos
    
    return [a for a in parts if a]

ans2 = 0
for i in range(1,row-1):
    
    for j in range(1,col-1):
        
        if board[i][j] == '*':
            parts = find_parts(board, (i,j))
            if len(parts) >1:
                ans2 += prod(map(int,parts))
                
print('Part2: ', ans2)