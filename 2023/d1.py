from string import digits
import re

with open('input.txt','r') as file:
    inp = [line.strip() for line in file]

def translate(line):
    tr_line = ''
    for i, c in enumerate(line):
        if c.isnumeric():
            tr_line += c
            continue
        
        for j, num in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            if line[i:].startswith(num):
                tr_line += str(j+1)
                break
    return tr_line

ans1 = 0    
ans2 = 0    
for line in inp:
    nums = [c for c in line if c in digits]
    ans1 += int(nums[0] + nums[-1])
    
    line = translate(line)
    l, r = re.search(r'\d', line).group(), re.search(r'\d(?!.*\d)', line).group()
    ans2 += int(l+r)
    
print('Part1:', ans1)
print('Part2:', ans2)