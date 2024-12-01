import numpy as np
from copy import deepcopy

with open('2020/input.txt','r') as file:
    input = file.readlines()

inp = []
for line in input:
    inp.append([1 if a=='#' else 0 for a in line.strip()])
inp = np.array(inp)

def part1():
    space = np.zeros((inp.shape[0],)*3)
    space[:,:,0] = inp


    def get_neighbors(point):
        x,y,z = point
        neighs = []
        for cx in (-1, 0, +1):
            for cy in (-1, 0, +1):
                for cz in (-1, 0, +1):
                    neighs.append((x+cx, y+cy, z+cz))
        
        neighs.remove(point)
        return neighs

                
    def cycle_step(space_map):
        space_map = np.pad(space_map, 2)
        next_map = deepcopy(space_map)
        h,w,d = space_map.shape
        
        for i in range(1,h-1):
            for j in range(1,w-1):
                for k in range(1,d-1):
                    neighs = get_neighbors((i,j,k))
                    rule = sum([space_map[x,y,z] for x,y,z in neighs])
                    
                    if space_map[i,j,k] == 1 and not (rule == 2 or rule == 3):
                        next_map[i,j,k] = 0    
                    
                    elif space_map[i,j,k] == 0 and rule == 3:
                        next_map[i,j,k] = 1
        return next_map


    for _ in range(6):
        space = cycle_step(space)            
    print(space.sum())
        

def part2():
    space = np.zeros((inp.shape[0],)*4)
    space[:,:,0,0] = inp


    def get_neighbors(point):
        x,y,z,w = point
        neighs = []
        for cx in (-1, 0, +1):
            for cy in (-1, 0, +1):
                for cz in (-1, 0, +1):
                    for cw in (-1, 0, +1):
                        neighs.append((x+cx, y+cy, z+cz, w+cw))
        
        neighs.remove(point)
        return neighs

                
    def cycle_step(space_map):
        space_map = np.pad(space_map, 2)
        next_map = deepcopy(space_map)
        h,w,d,q = space_map.shape
        
        for i in range(1,h-1):
            for j in range(1,w-1):
                for k in range(1,d-1):
                    for l in range(1,q-1):
                        neighs = get_neighbors((i,j,k,l))
                        rule = sum([space_map[x,y,z,w] for x,y,z,w in neighs])
                        
                        if space_map[i,j,k,l] == 1 and not (rule == 2 or rule == 3):
                            next_map[i,j,k,l] = 0    
                        
                        elif space_map[i,j,k,l] == 0 and rule == 3:
                            next_map[i,j,k,l] = 1
        return next_map


    for _ in range(6):
        space = cycle_step(space)            
    print(space.sum())

part1()    
part2()