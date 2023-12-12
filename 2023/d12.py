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