from collections import defaultdict

with open('input') as file:
    inp = file.readlines()

board = defaultdict(int)
lines = []
for line in inp:
    p1,p2 = line.strip().split(' -> ')
    x1,y1 = map(int, p1.split(','))
    x2,y2 = map(int, p2.split(','))
    lines.append(((x1,y1),(x2,y2)))

for (x1,y1),(x2,y2) in lines:
    if x1==x2:
        for y in range(min((y1,y2)),max((y1,y2))+1):
            board[(x1,y)] += 1

    elif y1==y2:
        for x in range(min((x1,x2)),max((x1,x2))+1):
            board[(x,y1)] += 1

print('Part1:', len([a for a in board.values() if a >= 2]))

for (x1,y1),(x2,y2) in lines:
    if x1!=x2 and y1!=y2:
        p1,p2 = sorted([(x1,y1),(x2,y2)])
        cur = p1
        if p1[1] < p2[1]:
            while cur != (p2[0]+1,p2[1]+1):
                board[cur] += 1
                cur = cur[0]+1,cur[1]+1
        else:
            while cur != (p2[0]+1,p2[1]-1):
                board[cur] += 1
                cur = cur[0]+1,cur[1]-1

print('Part2:', len([a for a in board.values() if a >= 2]))