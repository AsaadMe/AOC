from collections import Counter

with open('input.txt','r') as file:
    inp = file.read().splitlines()
    
hands = {l.split()[0]:{'bid':int(l.split()[1]), 'type':None} for l in inp}

def get_type(hand):
    c = Counter(hand)
    if max(c.values()) == 5:
        type = 7
    elif max(c.values()) == 4:
        type = 6
    elif len(c) == 2 and sum(c.values()) == 5:
        type = 5
    elif max(c.values()) == 3:
        type = 4
    elif c.most_common()[0][1] == c.most_common()[1][1] == 2:
        type = 3
    elif max(c.values()) == 2:
        type = 2
    else:
        type = 1
    return type

for hand in hands:
    hands[hand]['type'] = get_type(hand)
    
card_ranks = {'A':12, 'K':11, 'Q':10, 'J':9, 'T':8, '9':7, '8':6, '7':5, '6':4, '5':3, '4':2, '3':1, '2':0}       
sorted_hands = sorted(hands, key=lambda x: (hands[x]['type'], [card_ranks[a] for a in x]))

ans1 = 0
for w, h in enumerate(sorted_hands,1):
    ans1 += w*hands[h]['bid']
    
print('Part1: ', ans1)

card_ranks = {'A':12, 'K':11, 'Q':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1, 'J':0}
for hand in hands:
    c = Counter(hand)
    if c.most_common()[0][0] != 'J' :
        new = hand.replace('J', c.most_common()[0][0])
    elif (c.most_common()[0][0] == 'J') and (len(c.most_common()) > 1):
        new = hand.replace('J', c.most_common()[1][0])
    else:
        new = hand.replace('J', '2')
    
    hands[hand]['type'] = get_type(new)

sorted_hands = sorted(hands, key=lambda x: (hands[x]['type'], [card_ranks[a] for a in x]))

ans2 = 0
for w, h in enumerate(sorted_hands,1):
    ans2 += w*hands[h]['bid']
    
print('Part2: ', ans2)