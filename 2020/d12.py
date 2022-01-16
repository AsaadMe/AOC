with open('2020/input.txt','r') as file:
    input = file.readlines()


def part1():    
    directions = {0:(1,0),1:(0,1),2:(-1,0),3:(0,-1)} # N,E,S,W
    cur_pos = (0,0) # N,E
    cur_direct_i = 1 # E
    for line in input:
        inst, val = line[0], int(line[1:])
        if inst == 'N':
            cur_pos = cur_pos[0]+val, cur_pos[1]
        elif inst == 'S':
            cur_pos = cur_pos[0]-val, cur_pos[1]
        elif inst == 'E':
            cur_pos = cur_pos[0], cur_pos[1]+val
        elif inst == 'W':
            cur_pos = cur_pos[0], cur_pos[1]-val
        elif inst == 'L':
            i_ch = val // 90
            cur_direct_i = (cur_direct_i-i_ch) % 4
        elif inst == 'R':
            i_ch = val // 90
            cur_direct_i = (cur_direct_i+i_ch) % 4
        elif inst == 'F':
            direction = directions[cur_direct_i]
            cur_pos = cur_pos[0]+val*direction[0],cur_pos[1]+val*direction[1]

    print(abs(cur_pos[0]) + abs(cur_pos[1]))
    
def part2():
    cur_pos = (0,0) # N,E
    waypoint = (1,10)
    
    for line in input:
        inst, val = line[0], int(line[1:])
        if inst == 'N':
            waypoint = waypoint[0]+val, waypoint[1]
        elif inst == 'S':
            waypoint = waypoint[0]-val, waypoint[1]
        elif inst == 'E':
            waypoint = waypoint[0], waypoint[1]+val
        elif inst == 'W':
            waypoint = waypoint[0], waypoint[1]-val
        elif inst == 'L':
            i_ch = val // 90
            for _ in range(i_ch):
                waypoint = waypoint[1], -waypoint[0]
        elif inst == 'R':
            i_ch = val // 90
            for _ in range(i_ch):
                waypoint = -waypoint[1], waypoint[0]
        elif inst == 'F':
            move = waypoint[0]*val, waypoint[1]*val
            cur_pos = cur_pos[0]+move[0], cur_pos[1]+move[1]

    print(abs(cur_pos[0]) + abs(cur_pos[1]))
    
part1()
part2()