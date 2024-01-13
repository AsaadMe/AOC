
input = [int(a) for a in open('input').readlines()]
ans1 = 0
prev_line = input[0]
for line in input[1:]:
    line = line
    if line > prev_line:
        ans1 += 1
    prev_line = line

print('Part1:', ans1)

winind = 1
ans2 = 0
prev_sum = sum(input[:3])
while winind < len(input):
    if sum(input[winind:winind+3]) > prev_sum:
        ans2 += 1
    prev_sum = sum(input[winind:winind+3])
    winind += 1

print('Part2:', ans2)