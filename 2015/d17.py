from itertools import combinations

ans = []
containers = [int(a) for a in open('input').readlines()]

for i in range(len(containers)):
    for comb in combinations(containers,i):
        if sum(comb) == 150:
            ans.append(len(comb))

print('Part1: ', len(ans))
print('Part2: ', len([a for a in ans if a==min(ans)]))