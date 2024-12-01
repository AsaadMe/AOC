cubes = set()
free_sides = 0
with open('2022/input.txt','r') as file:
    for line in file:
        line = tuple([int(a) for a in line.strip().split(',')])
        free_sides += 6
        for cube in cubes:
            if sum(abs(a-b) for a,b in zip(line,cube)) == 1:
                free_sides -= 2
        cubes.add(line)
        
print('Part1:', free_sides)

min_x = min(x for x,y,z in cubes)
max_x = max(x for x,y,z in cubes)
min_y = min(y for x,y,z in cubes)
max_y = max(y for x,y,z in cubes)
min_z = min(z for x,y,z in cubes)
max_z = max(z for x,y,z in cubes)

x_range = range(min_x-1, max_x+2)
y_range = range(min_y-1, max_y+2)
z_range = range(min_z-1, max_z+2)
outside = {(min_x-1, min_y-1, min_z-1)}
check = [(min_x-1, min_y-1, min_z-1)]

sides = lambda x,y,z: ({(x-1, y, z), (x+1, y, z),
            (x, y-1, z), (x, y+1, z),
            (x, y, z-1), (x, y, z+1)})

while check:
        x, y, z = check.pop()
        if x not in x_range or y not in y_range or z not in z_range:
            continue
        newly_found = sides(x, y, z) - outside - cubes
        outside.update(newly_found)
        check.extend(newly_found)

answer = sum(len((sides(x, y, z) & outside) - cubes)
                for x, y, z in cubes)

print('Part2:', answer)