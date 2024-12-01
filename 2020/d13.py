with open('2020/input.txt','r') as file:
    mins, bus_ids = file.readlines()
    mins = int(mins)
    bus_ids = [int(a) if a != 'x' else a for a in bus_ids.strip().split(',')]
    

def part1():
    ids = [a for a in bus_ids if a != 'x']
    curmin = mins
    while True:
        for id in ids:
            if curmin % id == 0:
                return (curmin-mins) * id
            
        curmin += 1

def part2():
    data = [(i, int(bus_id)) for i, bus_id in enumerate(bus_ids) if bus_id != 'x']
    jump = data[0][1]
    time_stamp = 0
    for delta, bus_id in data[1:]:
        while (time_stamp + delta) % bus_id != 0:
            time_stamp += jump
        jump *= bus_id
    return time_stamp

print('Part1:', part1())
print('Part2:', part2())
