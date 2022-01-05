from itertools import combinations 

with open('2020/input.txt','r') as file:
    input = [int(a.strip()) for a in file.readlines()]
        
for i in range(26, len(input)):
    combs = combinations(input[i-26:i], 2)
    combs = [a+b for a,b in combs]
    if input[i] not in combs:
        invalid_indes = i
        invalid_num = input[i]
        print('Invalid:', invalid_indes, invalid_num)
        break

br_flag = False
for i in range(len(input)):
    j = 2
    while j != invalid_indes:       
        if sum(input[i:j]) == invalid_num:
            w_sets = input[i:j]
            print("Sets:", w_sets)
            print('Weakness Num:', sorted(w_sets)[0] + sorted(w_sets)[-1])
            br_flag = True
            break
        else:
            j += 1
            continue
    
    if br_flag:
        break