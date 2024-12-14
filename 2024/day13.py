with open("input.txt") as file:
    inp = file.read().split("\n\n")

machines = []
for machine in inp:
    machine = machine.splitlines()
    button_a = [int(a.split("+")[1]) for a in machine[0].strip().removeprefix("Button A: ").split(",")]
    button_b = [int(a.split("+")[1]) for a in machine[1].strip().removeprefix("Button B: ").split(",")]
    prize = [int(a.split("=")[1]) for a in machine[2].strip().removeprefix("Prize: ").split(",")]

    machines.append({"A": button_a, "B": button_b, "Prize": prize})


def get_min_token1(machine: dict):
    button_a = machine["A"]
    button_b = machine["B"]
    prize = machine["Prize"]

    for a in range(100):
        for b in range(100):
            if (a * button_a[0] + b * button_b[0], a * button_a[1] + b * button_b[1]) == tuple(prize):
                return 3 * a + b
    return 0


def get_min_token2(machine: dict):
    button_a = machine["A"]
    button_b = machine["B"]
    prize = machine["Prize"]

    b = (prize[1] * button_a[0] - prize[0] * button_a[1]) // (button_b[1] * button_a[0] - button_b[0] * button_a[1])
    a = (prize[0] - b * button_b[0]) // button_a[0]

    if (a * button_a[0] + b * button_b[0], a * button_a[1] + b * button_b[1]) == tuple(prize):
        return 3 * a + b

    return 0


print("Part1: ", sum([get_min_token1(m) for m in machines]))

for m in machines:
    m["Prize"][0] += 10000000000000
    m["Prize"][1] += 10000000000000


print("Part2: ", sum([get_min_token2(m) for m in machines]))
