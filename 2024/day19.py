from functools import cache

with open("input.txt") as file:
    patterns, designs = file.read().split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.splitlines()


@cache
def check(design: str):
    if not design:
        return True

    for pattern in patterns:
        if pattern in design:
            replaceds = []
            ind = design.find(pattern)
            replaceds.append(design[:ind])
            replaceds.append(design[ind + len(pattern) :])

            check_sum = 0
            for replaced in replaceds:
                if replaced != design and check(replaced):
                    check_sum += 1
            if check_sum == 2:
                return True

    return False


print("Part1: ", sum([check(design) for design in designs]))
