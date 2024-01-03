on_lights = set()
all_lights = [[0 for _ in range(1000)] for _ in range(1000)]

for line in open('input'):
    line = line.strip()
    zline = line.replace('turn off','').replace('turn on','').replace('toggle','')
    p1,p2 = zline.split(' through ')
    i1,j1 = map(int, p1.split(','))
    i2,j2 = map(int, p2.split(','))
    
    if 'on' in line:
        for i in range(i1,i2+1):
            for j in range(j1,j2+1):
                on_lights.add((i,j))
                all_lights[i][j] += 1

    elif 'off' in line:
        for i in range(i1,i2+1):
            for j in range(j1,j2+1):
                on_lights.discard((i,j))
                if all_lights[i][j] > 0:
                    all_lights[i][j] -= 1

    elif 'toggle' in line:
        for i in range(i1,i2+1):
            for j in range(j1,j2+1):
                if (i,j) in on_lights:
                    on_lights.discard((i,j))
                else:
                    on_lights.add((i,j))

                all_lights[i][j] += 2

print("Part1:", len(on_lights))
print("Part2:", sum([sum(l) for l in all_lights]))