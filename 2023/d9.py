with open('input.txt', 'r') as file:
    inp = file.read().splitlines()

inp = [list(map(int,a.split())) for a in inp]

def get_predict1(line):
    hier = [line]
    while any(last := hier[-1]):
        step = []
        for i in range(1,len(last)):
            step.append(last[i]-last[i-1])
            
        hier.append(step)

    val = 0
    for step in list(reversed(hier))[1:]:
        val += step[-1]
        
    return val

def get_predict2(line):
    hier = [line]
    while any(last := hier[-1]):
        step = []
        for i in range(1,len(last)):
            step.append(last[i]-last[i-1])
            
        hier.append(step)

    val = 0
    for step in list(reversed(hier))[1:]:
        val = step[0] - val
        
    return val

ans1 = 0
ans2 = 0
for line in inp:
    ans1 += get_predict1(line)
    ans2 += get_predict2(line)

print('Part1: ', ans1)
print('Part2: ', ans2)