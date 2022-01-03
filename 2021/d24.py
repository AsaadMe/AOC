from math import floor
import functools
import itertools

with open("input", 'r') as file:
    input = file.readlines()

instructs = []
for i in range(0, 14):
    instructs.append(tuple(itertools.islice(input,i*18,i*18+18)))

@functools.cache
def run_alu(command, *args, **avar):
    
    if command == 'inp':
        avar[args[0]] = int(avar['bignum'])
        
    elif command == 'add':
        try:
            avar[args[0]] += int(args[1])
        except ValueError:
            avar[args[0]] += avar[args[1]]
            
    elif command == 'mul':
        try:
            avar[args[0]] *= int(args[1])
        except ValueError:
            avar[args[0]] *= avar[args[1]]
            
    elif command == 'div':
        try:
            avar[args[0]] = floor(avar[args[0]]/int(args[1]))
        except ValueError:
            avar[args[0]] = floor(avar[args[0]]/avar[args[1]])
            
    elif command == 'mod':
        try:
            avar[args[0]] %= int(args[1])
        except ValueError:
            avar[args[0]] %= avar[args[1]]
            
    elif command == 'eql':
        try:
            if avar[args[0]] == int(args[1]):
                avar[args[0]] = 1
            else:
                avar[args[0]] = 0
        except ValueError:
            if avar[args[0]] == avar[args[1]]:
                avar[args[0]] = 1
            else:
                avar[args[0]] = 0
    return avar

@functools.cache
def run_instruct(instruct, **avar):
    for line in instruct:
        command, *args = line.strip().split()
        avar = run_alu(command, *args, **avar)
    return avar    
        
def check_valid(num):
    avar = {'x':0, 'w':0, 'y':0, 'z':0, 'bignum':'0'}

    for i, ins in enumerate(instructs):
        avar['bignum'] = str(num)[i]
        avar = run_instruct(tuple(ins), **avar)
        # print(i, avar)
        
    if avar['z'] == 0:
        return True
    else:
        return False
        
# all_14_digits_number = range(99999999999999, 11111111111111, -1)
# for num in all_14_digits_number: # without any zeros
#     if '0' not in str(num):
#         # print(num)
#         if check_valid(num):
#             print("found solution:", num)
# 51316214181141
# if check_valid(96979989692495):
#     print("found solution")

for w in range(1,10):
    for z in range(0, 100000):
        avar = {'x':0, 'w':0, 'y':0, 'z':z, 'bignum':str(w)}
        ans = run_instruct(instructs[12], **avar)
        
        if ans['z'] in range(6,15):
            print('found it:', avar)