input = [int(a) for a in '418976235']
cur_cup = input[0]

def move(cups:list[int], cur_cup:int):
    picks = []
    cur_cup_index = cups.index(cur_cup)

    for _ in range(3):
        if cur_cup != cups[-1]:
            picks.append(cups.pop(cur_cup_index+1))
        else:
            picks.append(cups.pop(0))

    dest_cup = cur_cup - 1
    while dest_cup in picks or dest_cup == 0:        
        dest_cup -= 1
        if dest_cup < min(cups):
            dest_cup = max(cups)
            break
        
    cur_cup_index = cups.index(cur_cup)    
    dest_cup_index = cups.index(dest_cup)

    cups = cups[0:dest_cup_index+1] + picks + cups[dest_cup_index+1:]
    
    cur_cup_index = cups.index(cur_cup)
    if cur_cup != cups[-1]:
        next_cur_cup = cups[cur_cup_index+1]
    else:
        next_cur_cup = cups[0]
    
    return cups, next_cur_cup
        
for _ in range(100):        
    input, cur_cup = move(input, cur_cup)

ans = ''
while input:
    if input.index(1) != len(input)-1:
        ans += str(input.pop(input.index(1)+1))
    else:
        ans += str(input.pop(0))
ans = ans[:-1]        
print(ans)