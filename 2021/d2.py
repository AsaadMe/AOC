depth = 0
pos = 0
for line in open('input').readlines():
    match line.split():
        case ['up', num]:
            depth += int(num)
        case ['down', num]:
            depth -= int(num)
        case ['forward', num]:
            pos += int(num)

print('Part1:', depth*pos)

aim = 0
depth = 0
pos = 0
for line in open('input').readlines():
    match line.split():
        case ['up', num]:
            aim -= int(num)
        case ['down', num]:
            aim += int(num)
        case ['forward', num]:
            pos += int(num)
            depth += aim*int(num)

print('Part2:', depth*pos)