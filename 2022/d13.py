import json

with open('2022/input.txt', 'r') as file:
    pairs = [[json.loads(b) for b in a.splitlines()] for a in file.read().split('\n\n')]

def check(left, right):
    match left, right:
        case [int(), int()]:
            return left-right
        case [list(), list()]:
            for l,r in zip(left, right):
                if ch := check(l,r):
                    return ch
            return len(left) - len(right)
        case [int(), list()]:
            return check([left], right)
        case [list(), int()]:
            return check(left, [right])
    

ans1 = 0
for i, (pair1, pair2) in enumerate(pairs, 1):
    if check(pair1, pair2) < 0:
        ans1 += i
        
print('Part1:', ans1)

with open('2022/input.txt', 'r') as file:
    packets = [json.loads(a) for a in file.readlines() if a !='\n']
    packets.extend([[[2]],[[6]]])

a = sum(check(p, [[2]]) <= 0 for p in packets)
b = sum(check(p, [[6]]) <= 0 for p in packets)
print('Part2:', a * b)

