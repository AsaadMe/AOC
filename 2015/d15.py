import re
from math import prod

foods = []
for line in open('input'):
    foods.append(tuple(map(int, re.findall(r'-?\d+', line))))

ans1 = 0
ans2 = 0
for i in range(100):
    for j in range(100-i):
        for k in range(100-j-i):
            h = 100-k-j-i
            s1 = i*foods[0][0] + j*foods[1][0] + k*foods[2][0] + h*foods[3][0]
            s2 = i*foods[0][1] + j*foods[1][1] + k*foods[2][1] + h*foods[3][1]
            s3 = i*foods[0][2] + j*foods[1][2] + k*foods[2][2] + h*foods[3][2]
            s4 = i*foods[0][3] + j*foods[1][3] + k*foods[2][3] + h*foods[3][3]
            val = prod([a if a>0 else 0 for a in (s1,s2,s3,s4)])
            if val > ans1:
                ans1 = val
            total_cal = i*foods[0][4] + j*foods[1][4] + k*foods[2][4] + h*foods[3][4]
            if total_cal == 500:
                if val > ans2:
                    ans2 = val

print('Part1:', ans1)
print('Part2:', ans2)