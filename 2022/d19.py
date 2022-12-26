# Must Optimize

import re
import functools
from copy import deepcopy

with open('2022/input.txt','r') as file:
    blprint = file.readline()
    nums = [int(a) for a in re.findall(r'\d+', blprint)[1:]]
    
inventory = {'ore':0, 'clay':0, 'obsidian':0, 'geode':0,
             'ore_bot':1, 'clay_bot':0, 'obsidian_bot':0, 'geode_bot':0}

rules = {'ore_bot':{'ore':nums[0]}, 'clay_bot':{'ore':nums[1]},
         'obsidian_bot':{'ore':nums[2], 'clay':nums[3]},
         'geode_bot':{'ore':nums[4], 'obsidian':nums[5]},
         'nobot':{'ore':0}}

@functools.cache
def max_geode(inv, min_left):
    inv = dict(inv)
    if min_left == 0:
        return inv['geode']
    
    best = 0
    min_left -= 1
    
    
    for bot in ['ore_bot', 'clay_bot', 'obsidian_bot', 'geode_bot', 'nobot']:
        if all(inv[k] >= v for k,v in rules[bot].items()):
            nxt_inv = deepcopy(inv)
            nxt_inv['ore'] -= rules[bot].get('ore',0)
            nxt_inv['clay'] -= rules[bot].get('clay',0)
            nxt_inv['obsidian'] -= rules[bot].get('obsidian',0)
            
            nxt_inv['ore'] += nxt_inv['ore_bot']
            nxt_inv['clay'] += nxt_inv['clay_bot']
            nxt_inv['obsidian'] += nxt_inv['obsidian_bot']
            nxt_inv['geode'] += nxt_inv['geode_bot']
            
            if bot != 'nobot':
                nxt_inv[bot] += 1 
            nxt_inv = tuple(sorted(nxt_inv.items()))
            
            best = max(best, max_geode(nxt_inv, min_left))
            
    return best

inventory = tuple(sorted(inventory.items()))   
print(max_geode(inventory, 24))