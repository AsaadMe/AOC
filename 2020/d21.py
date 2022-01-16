## NOT CORRECT ##

from copy import deepcopy
import itertools

with open('2020/input.txt','r') as file:
    input = file.readlines()
    input_ch = []
    for line in input:
        ings, alergs = line.split('(')
        ings = ings.split()
        alergs = alergs.strip().replace(',','')[9:-1].split()
        input_ch.append((ings, alergs))
    
while 1:
    tmp_input = deepcopy(input_ch)
    for f1,f2 in itertools.combinations(input_ch, 2):
        changed = False
        ing1, aler1 = f1
        ing2, aler2 = f2
        
        if (len(set(aler1) & set(aler2)), len(set(ing1) & set(ing2))) == (1,1):
            ing_com = list(set(ing1) & set(ing2))[0]
            aler_com = list(set(aler1) & set(aler2))[0]
            for i,a in tmp_input:
                if ing_com in i:
                    i.remove(ing_com)
                    changed = True
                if aler_com in a:
                    a.remove(aler_com)
                    changed = True
                if len(i) == len(a) == 1:
                    ir = i.pop()
                    ar = a.pop()
                    for i2,a2 in tmp_input:
                        if ir in i2:
                            i2.remove(ir)
                        if ar in a2:
                            a2.remove(ar) 
                    changed = True
            if changed:
                break
            
    if input_ch == tmp_input: 
        break
                 
    input_ch = tmp_input
            
ans = 0 
for i in tmp_input:
    ans += len(i[0])
    
print(ans)