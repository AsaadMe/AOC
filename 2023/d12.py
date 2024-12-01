from functools import cache
import re

with open('input.txt','r') as file:
    inp = file.read().splitlines()
    
    
ans1 = 0    
for line in inp:
    arr, chk = line.split()
    stack = [(arr,0)]
    while stack:
        cur_arr, i = stack.pop()
        
        if '?' not in cur_arr:
            if [len(a) for a in re.findall(r'#+', cur_arr)] == [int(a) for a in chk.split(',')]:
                ans1 += 1
                
        elif cur_arr[i] == '?':
            stack.append((cur_arr[:i]+'.'+cur_arr[i+1:],i+1))
            stack.append((cur_arr[:i]+'#'+cur_arr[i+1:],i+1))
        else:
            stack.append((cur_arr,i+1))
           
print('Part1: ', ans1)


# Part2: rewrite part1 in recursive function and then use DP with cache.

@cache
def solve(arr, chk, in_group=0):
    if not arr:
        return not chk and not in_group
    num_sols = 0
    possible = '.#' if arr[0] == "?" else arr[0]
    for c in possible:
        if c == "#":
            num_sols += solve(arr[1:], chk, in_group + 1)
        else:
            if in_group:
                if chk and chk[0] == in_group:
                    num_sols += solve(arr[1:], chk[1:])
            else:
                num_sols += solve(arr[1:], chk)
    return num_sols

ans = 0
for line in inp:
    arr, chk = line.split()
    arr = '?'.join([arr]*5)
    chk = [int(a) for a in chk.split(',')]*5
    ans += solve(arr+'.', tuple(chk))
    
print('Part2: ', ans)