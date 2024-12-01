import numpy as np

with open('input.txt','r') as file:
    board = np.array([list(line.strip()) for line in file])

def find_energetic(beams):
    energetic_tiles = set()
    visited = set()
    while beams:
        next_beams = []
        for beam in beams:
            x,y,dirx,diry = beam
            nxt_beam = x+dirx,y+diry
            
            if beam in visited:
                continue
            
            if (x >= 0 and x < board.shape[0] and
                y >= 0 and y < board.shape[1]):
                energetic_tiles.add((x,y))
                visited.add(beam)
            else:
                continue
            
            if board[x,y] == '.':
                next_beams.append((*nxt_beam,dirx,diry))
                
            if board[x,y] == '|':
                if dirx == 0:
                    next_beams.append((x+1,y,1,0))
                    next_beams.append((x-1,y,-1,0))
                elif diry == 0:
                    next_beams.append((*nxt_beam,dirx,diry))
                    
            if board[x,y] == '-':
                if diry == 0:
                    next_beams.append((x,y+1,0,1))
                    next_beams.append((x,y-1,0,-1))
                elif dirx == 0:
                    next_beams.append((*nxt_beam,dirx,diry))
                    
            if board[x,y] == '\\':
                next_beams.append((x+diry,y+dirx,diry,dirx))
                    
            if board[x,y] == '/':
                next_beams.append((x-diry,y-dirx,-diry,-dirx))
                    
        beams = next_beams        
    
    return len(energetic_tiles)
    
print('Part1: ', find_energetic([(0,0,0,1)]))
            
edge_beams = []
for i in range(board.shape[0]):
    edge_beams.append((0,i,1,0))            
    edge_beams.append((board.shape[1]-1,i,-1,0))
    
for j in range(board.shape[1]):
    edge_beams.append((j,0,0,1))
    edge_beams.append((j,board.shape[0]-1,0,-1))

most_energetic = 0    
for beam in edge_beams:
    most_energetic = max(most_energetic, find_energetic([beam]))
    
print('Part2: ', most_energetic)