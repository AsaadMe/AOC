from collections import Counter

with open("input.txt") as file:
    inp = file.readlines()
    fcol, scol = [], []

    for line in inp:
        f, s = map(int, line.strip().split())
        fcol.append(f)
        scol.append(s)

ans1 = 0
for pair in zip(sorted(fcol), sorted(scol)):
    ans1 += abs(pair[0] - pair[1])

print("Part1: ", ans1)

ans2 = 0
c = Counter(scol)
for num in fcol:
    ans2 += num * c.get(num, 0)

print("Part2: ", ans2)
