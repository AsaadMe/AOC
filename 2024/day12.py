from itertools import combinations

garden = {}

with open("input.txt") as file:
    for x, line in enumerate(file):
        for y, char in enumerate(line.strip()):
            garden[(x, y)] = char


visited = set()
regions = []
moves = {(0, 1): "r", (0, -1): "l", (1, 0): "u", (-1, 0): "d"}

for x, y in garden:
    if (x, y) not in visited:
        q = [(x, y)]
        region = set()
        region.add((x, y))
        perimeter = []

        while q:
            i, j = q.pop()
            visited.add((i, j))

            for movi, movj in moves:
                nextij = i + movi, j + movj

                if garden.get(nextij, "") != garden[(i, j)]:
                    perimeter.append(((i, j), moves[(movi, movj)]))

                if (
                    nextij in garden
                    and garden[nextij] == garden[(i, j)]
                    and nextij not in region
                ):
                    q.append(nextij)
                    region.add(nextij)

        sides = len(perimeter)
        for (p1, dir1), (p2, dir2) in combinations(perimeter, 2):
            if (
                dir1 == dir2
                and p1 != p2
                and p1 in [(p2[0] + movi, p2[1] + movj) for movi, movj in moves]
            ):
                sides -= 1

        regions.append(
            {
                "char": garden[(x, y)],
                "poses": region,
                "perimeter_count": len(perimeter),
                "perimeter_sides": sides,
                "area": len(region),
            }
        )

print("Part1: ", sum(region["area"] * region["perimeter_count"] for region in regions))

print("Part2: ", sum(region["area"] * region["perimeter_sides"] for region in regions))
