import numpy as np

with open('input.txt','r') as file:
    board = np.array([list(line.strip()) for line in file])

start = tuple(np.argwhere(board=='S')[0])
board[start] = '.'

h, w = board.shape
possible_tiles = set()
possible_tiles.add(start)
dirs = [(0,1), (0,-1), (1,0), (-1,0)]

max_step = 64
for i in range(max_step):
    nxt_possible_tiles = set()
    for cur_pos in possible_tiles:
        for dir in dirs:
            neighb = cur_pos[0]+dir[0], cur_pos[1]+dir[1]
            if 0 <= neighb[0] < h and 0 <= neighb[1] < w and board[neighb] == '.':
                nxt_possible_tiles.add(neighb)

    possible_tiles = nxt_possible_tiles.copy()

print('Part1: ', len(possible_tiles))