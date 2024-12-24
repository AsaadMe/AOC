with open("input.txt") as file:
    valued_wires, system = map(str.splitlines, file.read().split("\n\n"))
    valued_wires = {a.split(":")[0]: int(a.split(":")[1]) for a in valued_wires}

    all_x = sorted([(a, b) for a, b in valued_wires.items() if a.startswith("x")], key=lambda x: x[0], reverse=True)
    all_y = sorted([(a, b) for a, b in valued_wires.items() if a.startswith("y")], key=lambda x: x[0], reverse=True)

    x = int(f"0b{''.join([str(a[1]) for a in all_x])}", 2)
    y = int(f"0b{''.join([str(a[1]) for a in all_y])}", 2)

    system = [(*(a.split("->")[0].split()), a.split("->")[1].strip()) for a in system]


def simulate(system, valued_wires):
    while [a for a in system if a[-1].startswith("z") and a[-1] not in valued_wires]:
        for row in system:
            a, op, b, out = row
            if out not in valued_wires and (a in valued_wires) and (b in valued_wires):
                match op:
                    case "AND":
                        valued_wires[out] = valued_wires[a] & valued_wires[b]
                    case "OR":
                        valued_wires[out] = valued_wires[a] | valued_wires[b]
                    case "XOR":
                        valued_wires[out] = valued_wires[a] ^ valued_wires[b]

    all_z = sorted([(a, b) for a, b in valued_wires.items() if a.startswith("z")], key=lambda x: x[0], reverse=True)

    return int(f"0b{''.join([str(a[1]) for a in all_z])}", 2)


print("Part1: ", simulate(system, valued_wires.copy()))
