orig_registors = {}

with open("input.txt") as file:
    regs, program = file.read().split("\n\n")
    for reg in regs.splitlines():
        reg = reg.split(":")
        orig_registors[reg[0][-1]] = int(reg[1])

    program = [int(p) for p in program.split(":")[1].split(",")]


def get_operand_combo(op: int, registors: dict):
    if op == 4:
        return registors["A"]
    elif op == 5:
        return registors["B"]
    elif op == 6:
        return registors["C"]
    elif op in [0, 1, 2, 3]:
        return op


def run(registors, program, part2=False):
    ip = 0
    output = []
    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        match opcode:
            case 0:
                registors["A"] = int(registors["A"] / (2 ** get_operand_combo(operand, registors)))
            case 1:
                registors["B"] = registors["B"] ^ operand
            case 2:
                registors["B"] = get_operand_combo(operand, registors) % 8
            case 3:
                if registors["A"]:
                    ip = operand
                    continue
            case 4:
                registors["B"] = registors["B"] ^ registors["C"]
            case 5:
                output.append(get_operand_combo(operand, registors) % 8)
                if part2 and output[len(output) - 1] != program[len(output) - 1]:
                    return output
            case 6:
                registors["B"] = int(registors["A"] / (2 ** get_operand_combo(operand, registors)))
            case 7:
                registors["C"] = int(registors["A"] / (2 ** get_operand_combo(operand, registors)))

        ip += 2

    return output


print("Part1: ", ",".join(map(str, run(orig_registors.copy(), program))))

i = 0
best = 0
while True:
    i += 1
    registors = orig_registors.copy()
    # registors["A"] = i
    # registors["A"] = i * 8**5 + 0o25052
    registors["A"] = i * 8**10 + 0o6274025052
    out = run(registors.copy(), program, part2=True)
    if out == program:
        print("Part2: ", registors["A"])
        break
    elif len(out) > best:
        # print(registors["A"], oct(registors["A"]), best, len(program))
        best = len(out)
