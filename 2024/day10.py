board = {}

with open("input.txt") as file:
    for x, line in enumerate(file):
        for y, height in enumerate(line.strip()):
            if height != ".":
                board[(x, y)] = int(height)

max_x = x
max_y = y

trailheads = [p for p, h in board.items() if h == 0]
ends = [p for p, h in board.items() if h == 9]

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

scores1 = [{p: False for p in ends} for _ in trailheads]
scores2 = [{p: 0 for p in ends} for _ in trailheads]
for head_id, head in enumerate(trailheads):
    routes = [head]
    while routes:
        curpos = routes.pop()

        if curpos in ends:
            scores1[head_id][curpos] = True
            scores2[head_id][curpos] += 1
            continue

        for move in moves:
            nextpos = curpos[0] + move[0], curpos[1] + move[1]
            if board.get(nextpos) == board.get(curpos) + 1:
                routes.append(nextpos)

ans1 = 0
for headscore in scores1:
    ans1 += sum(headscore.values())
print("Part1: ", ans1)

ans2 = 0
for headscore in scores2:
    ans2 += sum(headscore.values())
print("Part2: ", ans2)
