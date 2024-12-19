corrupted = {}

bytes_count = 1024
for line in open("input.txt").readlines()[:bytes_count]:
    corrupted[tuple(map(int, line.strip().split(",")))] = "#"

max_x = 70
max_y = 70

start = (0, 0)
end = (max_x, max_y)


def bfs(corrupted):
    q = []
    visited = set()
    q.append((start, 0))

    while q:
        cur_pos, step = q.pop(0)
        if cur_pos in visited:
            continue

        visited.add(cur_pos)
        if cur_pos == end:
            return step

        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nposx = cur_pos[0] + x
            nposy = cur_pos[1] + y
            if 0 <= nposx <= max_x and 0 <= nposy <= max_y and (nposx, nposy) not in corrupted:
                q.append(((nposx, nposy), step + 1))


print("Part1: ", bfs(corrupted))

corrupted = {}

for line in open("input.txt").readlines():
    corrupted[tuple(map(int, line.strip().split(",")))] = "#"

    if not bfs(corrupted):
        print("Part2: ", line.strip())
        break
