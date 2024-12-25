locks = []
keys = []

with open("input.txt") as file:
    inp = map(str.splitlines, file.read().split("\n\n"))
    for schema in inp:
        if "." not in schema[0]:
            locks.append(schema)
        else:
            keys.append(schema)


def get_heights(schema):
    heights = [-1] * len(schema[0])
    for col in range(len(schema[0])):
        for row in range(len(schema)):
            if schema[row][col] == "#":
                heights[col] += 1

    return heights


locks_heights = [get_heights(lock) for lock in locks]
keys_heights = [get_heights(key) for key in keys]

ans = 0
for lock in locks_heights:
    for key in keys_heights:
        heights_sum = [sum(z) for z in zip(lock, key)]
        if all([a < len(locks[0]) - 1 for a in heights_sum]):
            ans += 1

print("Final Answer: ", ans)
