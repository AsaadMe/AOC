with open("input.txt") as file:
    all_strs = [a.strip() for a in file.readlines()]
    inp = [list(a) for a in all_strs]

to_search = "XMAS"

for i in range(len(inp[0])):
    all_strs.append("".join([row[i] for row in inp]))


for i in range(len(inp)):
    x = i
    y = 0
    substr1 = ""
    while x >= 0 and y < len(inp[i]):
        substr1 += inp[x][y]
        x -= 1
        y += 1

    x = i
    y = 0
    substr2 = ""
    while x < len(inp) and y < len(inp[i]):
        substr2 += inp[x][y]
        x += 1
        y += 1

    if len(substr1) >= 4:
        all_strs.append(substr1)

    if len(substr2) >= 4:
        all_strs.append(substr2)

for i in range(1, len(inp)):
    x = i
    y = len(inp) - 1
    substr1 = ""
    while x < len(inp[i]) and y >= 0:
        substr1 += inp[x][y]
        x += 1
        y -= 1

    x = i - 1
    y = len(inp) - 1
    substr2 = ""
    while x >= 0 and y >= 0:
        substr2 += inp[x][y]
        x -= 1
        y -= 1

    if len(substr1) >= 4:
        all_strs.append(substr1[::-1])

    if len(substr2) >= 4:
        all_strs.append(substr2[::-1])

ans1 = 0
for possible in all_strs:
    ans1 += possible.count(to_search)
    ans1 += possible.count(to_search[::-1])

print("Part1: ", ans1)


to_search = ["M.S.A.M.S", "M.M.A.S.S", "S.S.A.M.M", "S.M.A.S.M"]
to_search = [list(a) for a in to_search]

rows = len(inp)
cols = len(inp[0])
windows = []

for i in range(rows - 2):
    for j in range(cols - 2):
        window = [
            [inp[i][j], inp[i][j + 1], inp[i][j + 2]],
            [inp[i + 1][j], inp[i + 1][j + 1], inp[i + 1][j + 2]],
            [inp[i + 2][j], inp[i + 2][j + 1], inp[i + 2][j + 2]],
        ]
        windows.append(window)

ans2 = 0
not_importants = [(0, 1), (1, 0), (1, 2), (2, 1)]
for window in windows:
    for x, y in not_importants:
        window[x][y] = "."
    if [item for row in window for item in row] in to_search:
        ans2 += 1

print("Part2: ", ans2)
