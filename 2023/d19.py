with open('input.txt', 'r') as file:
    rules, parts = map(str.splitlines, file.read().split('\n\n'))
    rules = {rule.split('{')[0]:rule.split('{')[1][:-1] for rule in rules}
    parts = [{cat.split('=')[0]:int(cat.split('=')[1]) for cat in part[1:-1].split(',')} for part in parts]
    

def is_accepted(part):
    workflow = ['in']
    while workflow:
        
        id = workflow.pop()
        if id == 'R':
            return False
        elif id == 'A':
            return True
        
        rule = rules[id]
        
        steps = rule.split(',')
        for step in steps:
            if ':' in step:
                cond, goto = step.split(':')
                if '>' in cond:
                    if part[cond[0]] > int(cond[2:]):
                        workflow.append(goto)
                        break
                if '<' in cond:
                    if part[cond[0]] < int(cond[2:]):
                        workflow.append(goto)
                        break
            else:
                workflow.append(step)
                
ans1 = 0                
for part in parts:
    if is_accepted(part):
        ans1 += sum(part.values())
        
print('Part1: ', ans1)