import re

not_beacon = set()
lines = []
with open('2022/input.txt', 'r') as file:
    for line in file:
        sensor, beacon = re.findall(r'x=(-?\d+), y=(-?\d+)', line)
        sensor = [int(s) for s in sensor]
        beacon = [int(s) for s in beacon]
        lines.append([sensor, beacon])

for sensor, beacon in lines:
    dx, dy = abs(sensor[0]-beacon[0]), abs(sensor[1]-beacon[1])
    y = 2000000
    i = sensor[0]
    while abs((i-sensor[0])/(dx+dy))+abs((y-sensor[1])/(dx+dy)) <= 1:
        not_beacon.add((i,y))
        not_beacon.add((-i+2*sensor[0],y))
        i += 1
    
    if tuple(beacon) in not_beacon:
        not_beacon.remove(tuple(beacon))


print('Part1:', len(not_beacon))

# all_outer_points = []
# for sensor, beacon in lines:
#     diss = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
#     ps = set()
#     for i in range(diss+2):
#         if (0 <= sensor[0]+diss+1-i <= 4000000) and (0 <= sensor[1]-i <= 4000000):
#             ps.add((sensor[0]+diss+1-i,sensor[1]-i))
#         if (0 <= sensor[0]-diss-1+i <= 4000000) and (0 <= sensor[1]-i <= 4000000):
#             ps.add((sensor[0]-diss-1+i,sensor[1]-i))
#         if (0 <= sensor[0]+diss+1-i <= 4000000) and (0 <= sensor[1]+i <= 4000000):
#             ps.add((sensor[0]+diss+1-i,sensor[1]+i))
#         if (0 <= sensor[0]-diss-1+i <= 4000000) and (0 <= sensor[1]+i <= 4000000):
#             ps.add((sensor[0]-diss-1+i,sensor[1]+i))
#     all_outer_points.append(ps)
#     print(len(ps))
#     # draw_board(ps)

# for a in all_outer_points:
#     for sensor, beacon in lines:
#         a.discard(tuple(sensor))
#         a.discard(tuple(beacon))

# fin = set()
# for a,b in combinations(all_outer_points, 2):
#     ans = a & b 
#     if len(ans) == 1:
#         ans = ans.pop()
#         fin.add(ans)

# dis = set()        
# for sen,beac in lines:
#     diss = abs(sen[0]-beac[0]) + abs(sen[1]-beac[1])
#     for ans in fin:
#         if abs((ans[0]-sen[0])/diss)+abs((ans[1]-sen[1])/diss) <= 1:
#             dis.add(ans)

# j = (fin - dis).pop()
# print(j[0]*4000000 + j[1])
            

radius = {tuple(sens):abs(sens[0]-beac[0])+abs(sens[1]-beac[1]) for sens,beac in lines}
scanners = radius.keys()
acoeffs, bcoeffs = set(), set()
for ((x,y), r) in radius.items():
    acoeffs.add(y-x+r+1)
    acoeffs.add(y-x-r-1)
    bcoeffs.add(x+y+r+1)
    bcoeffs.add(x+y-r-1)

for a in acoeffs:
    for b in bcoeffs:
        p = ((b-a)//2, (a+b)//2)
        if all(0 < c < 4000000 for c in p):
            if all(abs(p[0]-t[0])+abs(p[1]-t[1]) > radius[t] for t in scanners):
                print('Part2:', 4000000 * p[0] + p[1])