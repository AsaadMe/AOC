with open('input') as file:
    inst = file.readline()

print('Part1:', inst.count('(')-inst.count(')'))

level = 0
for ind, char in enumerate(inst, 1):
    match char:
        case '(': level += 1
        case ')': level -= 1
    if level == -1:
        print('Part2:', ind)
        break