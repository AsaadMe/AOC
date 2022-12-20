import re
from functools import cache

valves = {}
with open('2022/input.txt', 'r') as file:
    for line in file:
        lvalve, rate, rvalves = re.findall(r"Valve (\w+).*=(\d+).*valves?(.*)$", line)[0]
        rvalves = [a.strip() for a in rvalves.split(',')]
        valves[lvalve] = {'next_valves':rvalves, 'rate':int(rate)}
        
@cache        
def max_flow(cur_valve, opened, min_left):
    if min_left <= 0:
        return 0
    
    most_press = 0
    if cur_valve not in opened:
        r = valves[cur_valve]['rate']
        press = r * (min_left-1)
        nxt_opened = opened + (cur_valve,)
        for dest in valves[cur_valve]['next_valves']:
            if r != 0:
                most_press = max(most_press, press + max_flow(dest, nxt_opened, min_left-2))
            else:
                most_press = max(most_press, max_flow(dest, opened, min_left-1))
                
    return most_press
        
print('Part1:', max_flow('AA', (), 30))