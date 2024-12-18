import sys

sys.setrecursionlimit(5000)

board = {}
start_pos = None
end_pos = None
start_dir = "E"
dir_map = {"E": (0, 1), "S": (1, 0), "W": (0, -1), "N": (-1, 0)}

with open("input.txt") as file:
    for x, line in enumerate(file):
        for y, char in enumerate(line.strip()):
            if char == "S":
                start_pos = (x, y)

            if char == "E":
                end_pos = (x, y)

            board[(x, y)] = char


def dfs(cur_pos, cur_dir, visited):
    visited = frozenset(visited | {cur_pos})
    if cur_pos == end_pos:
        return 0

    scores = []
    for dir, dirpos in dir_map.items():
        next_pos = (cur_pos[0] + dirpos[0], cur_pos[1] + dirpos[1])
        if next_pos not in visited and next_pos in board and board[next_pos] != "#":
            score = dfs(next_pos, dir, visited.copy())
            if score is not None:
                if dir == cur_dir:
                    scores.append(1 + score)

                elif (dir_map[cur_dir][0] + dirpos[0], dir_map[cur_dir][1] + dirpos[1]) == (0, 0):
                    scores.append(2001 + score)

                else:
                    scores.append(1001 + score)

    return min(scores) if scores else None


print("Part1: ", dfs(start_pos, start_dir, frozenset()))
