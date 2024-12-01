import re

monkeys = {}
with open('2022/input.txt','r') as file:
    for line in file:
        monk, job = map(str.strip, line.split(':'))
        if job.isnumeric():
            monkeys[monk] = int(job)
        else:
            l, op, r = re.search(r'(\w+) (.) (\w+)', job).groups()
            monkeys[monk] = (l, op, r)

def yell(monk, t=None):
    job = monkeys[monk]
    if isinstance(job, int):
        return job
    else:
        match job[1]:
            case '=': return yell(job[0]) if t=='left' else yell(job[2])
            case '+': return yell(job[0]) + yell(job[2])
            case '-': return yell(job[0]) - yell(job[2])
            case '*': return yell(job[0]) * yell(job[2])
            case '/': return yell(job[0]) / yell(job[2])
    
print('Part1:', int(yell('root')))

monkeys['root'] = (monkeys['root'][0], '=', monkeys['root'][2])
rg = (0, int(1e20)) # A Guess
mid = sum(rg) // 2
monkeys['humn'] = mid

while True: # Binary Search
    target = yell('root', 'right')
    a = yell('root', 'left')
    
    if a == target:
        print('Part2:', monkeys['humn'])
        break
    
    elif a < target:
        rg = (rg[0], mid)
        mid = sum(rg) // 2
        monkeys['humn'] = mid
        
    elif a > target:
        rg = (mid, rg[1])
        mid = sum(rg) // 2
        monkeys['humn'] = mid