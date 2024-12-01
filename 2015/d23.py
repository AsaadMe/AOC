with open('input') as file:
    input = file.readlines()
    input = [a.strip().split(' ', 1) for a in input]

def run(regs):
    index = 0
    while index < len(input):
        match input[index]:
            case ['inc', ('a'|'b') as reg]:
                regs[reg] += 1
                index += 1
            case ['hlf', ('a'|'b') as reg]:
                regs[reg] /= 2
                index += 1
            case ['tpl', ('a'|'b') as reg]:
                regs[reg] *= 3
                index += 1
            case ['jmp', offset]:
                index += int(offset)
            case ['jie', others]:
                reg, offset = others.split(', ')
                if regs[reg] % 2 == 0:
                    index += int(offset)
                else:
                    index += 1
            case ['jio', others]:
                reg, offset = others.split(', ')
                if regs[reg] == 1:
                    index += int(offset)
                else:
                    index += 1

    return regs

print('Part1:', run({'a':0,'b':0})['b'])
print('Part2:', run({'a':1,'b':0})['b'])