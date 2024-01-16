pos = [int(a) for a in open('input').readline().split(',')]

min_dist1 = float('inf')
min_dist2 = float('inf')
for center in range(min(pos),max(pos)):
    dist1 = 0
    dist2 = 0
    for p in pos:
        dist1 += abs(center-p)
        dist2 += int(abs(center-p)*(abs(center-p)+1)/2)
    if dist1 < min_dist1:
        min_dist1 = dist1
    if dist2 < min_dist2:
        min_dist2 = dist2

print('Part1:', min_dist1)
print('Part2:', min_dist2)