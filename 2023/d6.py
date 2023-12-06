from math import prod

with open('input.txt','r') as file:
    inp = file.read().splitlines()
    time_dist = list(zip(map(int,inp[0].split()[1:]), map(int,inp[1].split()[1:])))

possible_ways = []    
for time, dist in time_dist:
    pos = 0
    for t in range(1,time):
        if t*(time-t) > dist:
           pos += 1
    possible_ways.append(pos) 
            
print('Part1: ', prod(possible_ways))


time,dist = [int(''.join(a.split()[1:]).replace(' ','')) for a in inp]
possible_ways = []
pos = 0
for t in range(1,time):
        if t*(time-t) > dist:
           pos += 1
possible_ways.append(pos)

print('Part2: ', prod(possible_ways))