from functools import cache

with open("input.txt") as file:
    patterns, designs = file.read().split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.splitlines()


@cache
def check(design: str):
    if not design:
        return 1

    score = 0
    for pattern in patterns:
        if pattern in design:
            # replaceds = []
            # ind = design.find(pattern)
            # replaceds.append(design[:ind])
            # replaceds.append(design[ind + len(pattern) :])

            # check_sum = 0
            # for replaced in replaceds:
            #     if replaced != design and check(replaced):
            #         check_sum += 1
            # if check_sum == 2:
            #     return True
            if design.startswith(pattern):
                score += check(design[len(pattern) :])

    return score


print("Part1: ", sum([1 for design in designs if check(design)]))
print("Part2: ", sum([check(design) for design in designs]))
