freqs = {}

with open("input.txt") as file:
    for x, line in enumerate(file):
        for y, char in enumerate(line.strip()):
            if char != ".":
                freqs[(x, y)] = char

max_x = x
max_y = y


def part1():
    antinodes = set()
    for point1, val1 in freqs.items():
        for point2, val2 in freqs.items():
            if val1 == val2 and point1 != point2:
                diff = (point1[0] - point2[0], point1[1] - point2[1])

                anti1 = (point1[0] + diff[0], point1[1] + diff[1])
                if 0 <= anti1[0] <= max_x and 0 <= anti1[1] <= max_y:
                    antinodes.add(anti1)
                anti2 = (point2[0] - diff[0], point2[1] - diff[1])
                if 0 <= anti2[0] <= max_x and 0 <= anti2[1] <= max_y:
                    antinodes.add(anti2)

    print("Part1: ", len(antinodes))


def part2():
    antinodes = set()
    for point1, val1 in freqs.items():
        for point2, val2 in freqs.items():
            if val1 == val2 and point1 != point2:
                diff = (point1[0] - point2[0], point1[1] - point2[1])

                anti1 = (point1[0] + diff[0], point1[1] + diff[1])
                while 0 <= anti1[0] <= max_x and 0 <= anti1[1] <= max_y:
                    antinodes.add(anti1)
                    anti1 = (anti1[0] + diff[0], anti1[1] + diff[1])

                anti2 = (point2[0] - diff[0], point2[1] - diff[1])
                while 0 <= anti2[0] <= max_x and 0 <= anti2[1] <= max_y:
                    antinodes.add(anti2)
                    anti2 = (anti2[0] - diff[0], anti2[1] - diff[1])

    antinodes = antinodes | freqs.keys()
    print("Part2: ", len(antinodes))


part1()
part2()
