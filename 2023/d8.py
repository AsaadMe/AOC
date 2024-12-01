from math import lcm
from itertools import cycle

with open('input.txt','r') as file:
    insts, rules = file.read().split('\n\n')
    rules = rules.splitlines()

rules_map = {}    
for rule in rules:
    k, v = map(str.strip, rule.split('='))
    v = v.replace('(','').replace(')','')
    rules_map[k] = (v.split(',')[0], v.split(',')[1].strip())
    
def part1():
    cur_node = 'AAA'
    exit_node = 'ZZZ'

    for step, inst in enumerate(cycle(insts), 1):
        if inst == 'R':
            cur_node = rules_map[cur_node][1]
        elif inst == 'L':
            cur_node = rules_map[cur_node][0]
            
        if cur_node == exit_node:
            break
        
    print('Part1: ', step)

def part2():
    cur_nodes = []
    for rule in rules_map:
        if rule.endswith('A'):
            cur_nodes.append(rule)

    lcms = []
    for i in range(len(cur_nodes)):
        for step, inst in enumerate(cycle(insts), 1):
            if inst == 'R':
                    cur_nodes[i] = rules_map[cur_nodes[i]][1]
            if inst == 'L':
                    cur_nodes[i] = rules_map[cur_nodes[i]][0]
                        
            if cur_nodes[i].endswith('Z'):
                lcms.append(step)
                break
        
    print('Part2: ', lcm(*lcms))
    
part1()
part2()