import numpy as np
import heapq

with open('input.txt','r') as file:
    board = np.array([list(line.strip()) for line in file],dtype=int)

def solve(board, max_straight, must_go):   
    queue = [] 
    cost = 0 
    pos = (0,0)
    goal = (board.shape[0]-1,board.shape[1]-1)
    dir = None 
    straight_steps = 0 
    must_go = must_go
    max_straight = max_straight
    heapq.heappush(queue, (cost, pos, dir, straight_steps)) 

    seen = set()

    while queue:
        cost, pos, dir, straight_steps = heapq.heappop(queue)
        
        if pos == goal and straight_steps >= must_go:
            return cost
        
        if (pos, dir, straight_steps) in seen: 
            continue
        
        seen.add((pos, dir, straight_steps)) 
        
        next_states = [] 
        if dir is None: 
            for dir in ((0, 1), (1, 0), (0, 1), (-1, 0)):
                neighbour = pos[0]+dir[0],pos[1]+dir[1]
                next_states.append((neighbour, dir, 1))
        else:
            if straight_steps >= must_go:  
                next_states.append(((pos[0]-dir[1], pos[1]+dir[0]), (-dir[1], dir[0]), 1)) 
                next_states.append(((pos[0]+dir[1], pos[1]-dir[0]), (dir[1], -dir[0]), 1)) 
            
            if straight_steps < max_straight: 
                next_states.append(((pos[0]+dir[0], pos[1]+dir[1]), dir, straight_steps+1))
            
        for neighbour, dir, new_steps in next_states:
            if 0 <= neighbour[0] < board.shape[0] and 0 <= neighbour[1] < board.shape[1]:
                new_cost = cost + board[neighbour[0]][neighbour[1]]
                
                heapq.heappush(queue, (new_cost, neighbour, dir, new_steps))
                

print('Part1: ', solve(board, 3, 0))
print('Part2: ', solve(board, 10, 4))