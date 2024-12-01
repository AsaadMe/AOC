from collections import defaultdict

with open('2019/input.txt','r') as file:
    path1, path2 = [a.strip().split(',') for a in file.readlines()]

board = defaultdict(lambda: ['', defaultdict(int)])

def walk(path, mark:str):
    cou = 0
    cur_pos = [0,0]
    for ins in path:
        dir, val = ins[0], ins[1:]
        val = int(val)
        if dir == 'U':
            for i in range(1,val+1):
                board[(cur_pos[0]-i,cur_pos[1])][0] += mark
                board[(cur_pos[0]-i,cur_pos[1])][1][mark] = cou + i
            cur_pos[0] -= i
        if dir == 'D':
            for i in range(1,val+1):
                board[(cur_pos[0]+i,cur_pos[1])][0] += mark
                board[(cur_pos[0]+i,cur_pos[1])][1][mark] = cou + i
            cur_pos[0] += i
        if dir == 'R':
            for i in range(1,val+1):
                board[(cur_pos[0],cur_pos[1]+i)][0] += mark
                board[(cur_pos[0],cur_pos[1]+i)][1][mark] = cou + i
            cur_pos[1] += i
        if dir == 'L':
            for i in range(1,val+1):
                board[(cur_pos[0],cur_pos[1]-i)][0] += mark
                board[(cur_pos[0],cur_pos[1]-i)][1][mark] = cou + i
            cur_pos[1] -= i
            
        cou += val
        
walk(path1,'p1')
walk(path2,'p2')

close_intersec1 = sorted([k for k,v in board.items() if v[0]=='p1p2'], key=lambda x: abs(x[0])+abs(x[1]))[0]
print('Part1:', abs(close_intersec1[0])+abs(close_intersec1[1]))

close_intersec2 = sorted([v[1] for k,v in board.items() if v[0]=='p1p2'], key=lambda x: x['p1']+x['p2'])[0]
print('Part2:', sum(close_intersec2.values()))