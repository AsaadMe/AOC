import sys
sys.setrecursionlimit(5000)
import numpy as np

with open('input.txt','r') as file:
    board = np.array([list(line.strip()) for line in file])

start = (0,1)
endpos = (board.shape[0]-1,-2)

def dfs_step(curpos,visited):
    if curpos == endpos:
        return 0,1
    elif curpos not in visited:
        nvisited = visited.copy()
        nvisited.append(curpos)
        match board[curpos]:
            case '>':
                steps, end = dfs_step((curpos[0],curpos[1]+1),nvisited)
                if end:
                    return (steps + 1),1
            case '<':
                steps, end = dfs_step((curpos[0],curpos[1]-1),nvisited)
                if end:
                    return (steps + 1),1
            case 'v':
                steps, end = dfs_step((curpos[0]+1,curpos[1]),nvisited)
                if end:
                    return (steps + 1),1
            case '^':
                steps, end = dfs_step((curpos[0]-1,curpos[1]),nvisited)
                if end:
                    return (steps + 1),1
            case _:
                maxsteps = 0
                dirs = [(0,1),(0,-1),(1,0),(-1,0)]
                for neighb in [(curpos[0]+dir[0],curpos[1]+dir[1]) for dir in dirs]:
                    nx, ny = neighb
                    if ((0 <= nx < board.shape[0]) and 
                        (0 <= ny < board.shape[1]) and
                        (board[neighb] != '#')):
                        steps, end = dfs_step(neighb,nvisited)
                        if end and steps > maxsteps:
                            maxsteps = steps

                return 1+maxsteps,1
                
            
    return 0,0

print('Part1: ', dfs_step(start,[])[0]-1)

board[(board == '>')| (board == '<')|(board == 'v')|(board == '^')] = '.'

print('Part2: ', dfs_step(start,[])[0]-1) # Wrong
