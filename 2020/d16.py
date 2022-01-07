from collections import defaultdict

with open('2020/input.txt', 'r') as file:
    input = file.read()
    
rules, myticket, neartickets = input.split('\n\n')
rules = rules.splitlines()
neartickets =  neartickets.splitlines()[1:]
myticket = myticket.splitlines()[1].split(',')

all_rules = {}
for rule in rules:
    rule_name, rule_ranges = rule.split(':')
    lrange, rrange = rule_ranges.split('or')
    l1,r1 = list(map(int, lrange.split('-')))
    lrange = range(l1,r1+1)
    l2,r2 = list(map(int, rrange.split('-')))
    rrange = range(l2,r2+1)
    all_rules[rule_name] = [lrange, rrange]

invalid_ticks = []
invalid_ticks_ind = set()
for ind, tick in enumerate(neartickets):
    nums = [int(a) for a in tick.split(',')]
    for num in nums:
        fl = 0
        for rgs in all_rules.values():
            for rg in rgs:
                if num not in rg:
                    fl += 1
        if fl == len(all_rules)*2:
            invalid_ticks.append(num)
            invalid_ticks_ind.add(ind)

neartickets = [a for i,a in enumerate(neartickets) if i not in invalid_ticks_ind]
 
on_cols = [[] for _ in range(len(all_rules))]
for tick in neartickets:    
    tick = [int(a) for a in tick.split(',')]
    for i,n in enumerate(tick):
        on_cols[i].append(n)

true_tags = defaultdict(list)
for runame, ruranges in all_rules.items():       
    for i, nums in enumerate(on_cols):
        fl = 0
        for num in nums:
            if (num in ruranges[0]) or (num in ruranges[1]):
                fl += 1
            else:
                break
        if fl == len(neartickets):
            true_tags[runame].append(i)
            
            
final_poses = {}
while len(final_poses) != len(on_cols):
    ne_tags = {}
    for rname, rinds in true_tags.items():
        if len(rinds) == 1:
            final_poses[rname] = rinds[0] 
            for n, r in true_tags.items():
                ne_tags[n] = list(set(r) - set(rinds))
            break
    true_tags = ne_tags

# print(final_poses)   

ans = 1
for name in final_poses:
    if 'departure' in name:
        ans *= int(myticket[final_poses[name]])
        
print(ans)