## NOT WORKING ##

import numbers as np
from copy import deepcopy

board = []
with open('input.txt','r') as file:
    for line in file:
        s,e = line.strip().split('~')
        s = [int(a) for a in s.split(',')]
        e = [int(a) for a in e.split(',')]

        board.append([s,e])

board.sort(key=lambda l:l[0][2])
final_board = [brick for brick in board if brick[0][2]==1]
print(final_board)
max_start_z = max(board, key=lambda l: l[0][2])[0][2]
tallest_z = dict()
for brick in board:
    s,e = brick
    z = max(s[2],e[2])
    if s[2] == e[2]:
        if s[0] == e[0]:
            r = range(e[1]-s[1]+1)
            for y in r:
                if z > tallest_z.get((s[0],y),0):
                    tallest_z[(s[0],y)] = z
        elif s[1] == e[1]:
            r = range(e[0]-s[0]+1)
            for x in r:
                if z > tallest_z.get((x,s[1]),0):
                    tallest_z[(x,s[1])] = z
    else:
        if z > tallest_z.get((s[0],s[1]),0):
                    tallest_z[(s[0],s[1])] = z

for brick in board:
    s,e = brick
    if s[2] == e[2]:
        tallest_pos_z = None
        if s[0] == e[0]:
            r = range(e[1]-s[1]+1)
            nsz = max([tallest_z[(s[0],y)] for y in r]) + 1
            new_brick = [[s[0],s[1],nsz],[e[0],e[1],nsz]]
            tallest_z

        elif s[1] == e[1]:
            r = range(e[0]-s[0]+1)
            nsz = max([tallest_z[(x,s[1])] for x in r]) + 1
            new_brick = [[s[0],s[1],nsz],[e[0],e[1],nsz]]
    else:
        nsz = tallest_z[(s[0],s[1])] + 1
        new_brick = [[s[0],s[1],nsz],[e[0],e[1],e[2]-s[2]+nsz]]
        tallest_z[(s[0],s[1])] = e[2]-s[2]+nsz
        final_board.append(new_brick)


