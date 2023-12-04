with open('input.txt','r') as file:
    inp = [l for l in file.read().splitlines()]

matches = []

ans1 = 0    
for card in inp:
    winning_cards = card.split(':')[1].split('|')[0].strip().split()
    my_cards = card.split(':')[1].split('|')[1].strip().split()
    
    match_nums = len(set(my_cards) & set(winning_cards))
    if match_nums:
        ans1 += pow(2, match_nums-1)
        matches.append(match_nums)
    else:
        matches.append(0)
    
print('Part1: ',ans1)


ans2 = 0
cards_stack = list(range(1,len(inp)+1))
while cards_stack:
    cur_card = cards_stack.pop()
    ans2 += 1
    if matches[cur_card-1]:
        cards_stack.extend([cur_card+a for a in range(1,matches[cur_card-1]+1)])
    
print('Part2: ', ans2)