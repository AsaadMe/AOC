from itertools import product
from math import prod

inp = []
with open("input.txt") as file:
    for line in file:
        test_val, nums = line.strip().split(":")
        nums = [int(a) for a in nums.split()]
        inp.append((int(test_val), nums))


def solve(part):
    ops = {"+": sum, "*": prod}
    if part == 2:
        ops["||"] = lambda l: int(str(l[0]) + str(l[1]))

    ans = 0
    for test_val, nums in inp:
        for state in product(ops.keys(), repeat=len(nums) - 1):
            eq = nums[0]
            for i, op in enumerate(state):
                eq = ops[op]([eq, nums[i + 1]])

            if eq == test_val:
                ans += test_val
                break

    print(f"Part{part}: ", ans)


solve(part=1)
solve(part=2)
