import itertools
import math
from copy import deepcopy

with open('2019/input.txt', 'r') as file:
    moons = [[int(a[2:]) for a in l.strip()[1:-1].split(', ')] for l in file.readlines()]
    moons = [{'pos':m, 'vel':[0,0,0]} for m in moons]    
    init_states = deepcopy(moons)
    
def p1_step():
    for m1, m2 in itertools.combinations(moons, 2):
        for i in range(3):
            if m1['pos'][i] > m2['pos'][i]:
                m1['vel'][i] -= 1
                m2['vel'][i] += 1
            elif m1['pos'][i] < m2['pos'][i]:
                m1['vel'][i] += 1
                m2['vel'][i] -= 1
                
    for m in moons:
        for i in range(3):
            m['pos'][i] += m['vel'][i]
            
def part1():           
    for _ in range(1000):            
        p1_step()

    ans = 0
    for m in moons:
        ans += sum(map(abs, m['pos'])) * sum(map(abs, m['vel']))
        
    print('Part1:', ans)

def part2():
    
    cyc_ans = [0,0,0]
    for i in range(3):
        moons = deepcopy(init_states)
        c = 0
        while not cyc_ans[i]:
            for m1, m2 in itertools.combinations(moons, 2):
                if m1['pos'][i] > m2['pos'][i]:
                    m1['vel'][i] -= 1
                    m2['vel'][i] += 1
                elif m1['pos'][i] < m2['pos'][i]:
                    m1['vel'][i] += 1
                    m2['vel'][i] -= 1
                    
            for m in moons:
                m['pos'][i] += m['vel'][i]
                
            c += 1
            if ([m['pos'][i] for m in moons] == [m['pos'][i] for m in init_states] and
                [m['vel'][i] for m in moons] == [0,0,0,0]):
                cyc_ans[i] = c

    print('Part2:', math.lcm(*cyc_ans))

part1()    
part2()