from itertools import cycle, product

walls = set()
curpos = ()
walk_map = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

with open("input.txt") as file:
    for x, line in enumerate(file):
        for y, char in enumerate(line):
            if char == "#":
                walls.add((x, y))
            elif char == "^":
                curpos = (x, y)

    max_x = x
    max_y = y


def part1(curpos):
    visited = set()
    walk_cycle = cycle(walk_map.keys())
    cur_dir = next(walk_cycle)
    while 0 <= curpos[0] <= max_x and 0 <= curpos[1] <= max_y:
        visited.add(curpos)
        next_pos = (walk_map[cur_dir][0] + curpos[0], walk_map[cur_dir][1] + curpos[1])
        if next_pos not in walls:
            curpos = next_pos
        else:
            cur_dir = next(walk_cycle)

    print("Part1: ", len(visited))


def part2(curpos):
    orig_curpos = curpos
    stucks = 0
    for x, y in product(range(max_x + 1), range(max_y + 1)):
        curpos = orig_curpos
        if (x, y) not in walls and (x, y) != curpos:
            walls.add((x, y))
            visited = set()
            walk_cycle = cycle(walk_map.keys())
            cur_dir = next(walk_cycle)
            while 0 <= curpos[0] <= max_x and 0 <= curpos[1] <= max_y:
                if (curpos, cur_dir) in visited:
                    stucks += 1
                    break
                visited.add((curpos, cur_dir))
                next_pos = (
                    walk_map[cur_dir][0] + curpos[0],
                    walk_map[cur_dir][1] + curpos[1],
                )
                if next_pos not in walls:
                    curpos = next_pos
                else:
                    cur_dir = next(walk_cycle)

            walls.remove((x, y))

    print("Part2: ", stucks)


part1(curpos)
part2(curpos)
