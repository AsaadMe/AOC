with open('2020/input', 'r') as file:
    input = file.readlines()

sit_ids = []   
for sit in input:
    if sit := sit.strip():
        sit = sit.replace('F','0').replace('B','1').replace('R','1').replace('L','0')
        sit_row = int(sit[:7], 2)
        sit_col = int(sit[-3:], 2)
        sit_id = sit_row*8 + sit_col
        sit_ids.append(sit_id)
    
print('max:', max(sit_ids))

for i in range(min(sit_ids), max(sit_ids)+1):
    if (i not in sit_ids) and (i-1 in sit_ids) and (i+1 in sit_ids):
        print('my sit id:', i)
        