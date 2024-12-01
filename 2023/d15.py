from collections import defaultdict

with open('input.txt', 'r') as file:
    inp = file.readline().split(',')

def get_hash(input):
    shash = 0
    for ch in input:
        shash = ((shash+ord(ch))*17)%256
    return shash

all_hash = []
for seq in inp:
    all_hash.append(get_hash(seq))

print('Part1: ', sum(all_hash))

boxes = [defaultdict(str) for _ in range(256)]
for seq in inp:
    if '-' in seq:
        box_name = seq[:-1]
        box = get_hash(box_name)
        boxes[box].pop(box_name, None)
        
    elif '=' in seq:
        box_name,lens = seq.split('=')
        box = get_hash(box_name)
        boxes[box][box_name] = lens

focus_powers = 0        
for id, box in enumerate(boxes,1):
    for slot, lens in enumerate(box.values(),1):
        focus_powers += id * slot * int(lens)
        
print('Part2: ', focus_powers)