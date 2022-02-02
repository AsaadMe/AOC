import math
import re

with open('2019/input.txt','r') as file:
    masses = [int(a.strip()) for a in file.readlines()]
    
def get_fuel(mass):
    return math.floor(mass / 3) - 2

def part1():
    ans = 0
    for mass in masses:
        ans += get_fuel(mass)
        
    print('Part1:', ans)

def rec_get_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + rec_get_fuel(fuel)

def part2():
    ans = 0
    for mass in masses:
        ans += rec_get_fuel(mass)
        
    print('Part2:', ans)
            
part1()
part2()