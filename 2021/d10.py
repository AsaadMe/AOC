ans1 = 0
incompletes = []
for line in open('input').readlines():
    incomplete_flg = True
    line = line.strip()
    ocmap = {'(':')','[':']','<':'>','{':'}'}
    points = {')':3, ']':57, '>':25137 ,'}':1197}
    stack = []
    for char in line:
        if stack and char == ocmap[stack[-1]]:
            stack.pop()
        elif char in ocmap:
            stack.append(char)
        else:
            ans1 += points[char]
            incomplete_flg = False
            break
    if incomplete_flg:
        incompletes.append(stack)

print('Part1:', ans1)

points = {'[':2, '{':3, '<':4, '(':1}
scores = []
for stack in incompletes:
    ans2 = 0
    while stack:
        ans2 = ans2*5 + points[stack.pop()] 
    scores.append(ans2) 

print('Part2:', sorted(scores)[len(scores)//2])