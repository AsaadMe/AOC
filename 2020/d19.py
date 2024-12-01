with open('2020/input.txt','r') as file:
    input = file.read()
    rules, input = input.split('\n\n')
    all_rules = {int(rule.split(': ')[0]):rule.split(': ')[1].replace('"','') for rule in rules.splitlines()}
    input = input.splitlines()

def check(rul_ind, line):
    
    rules = all_rules[rul_ind].split('|')
    rules = [a.strip() for a in rules]
    
    if rules[0].isalpha():
        if line[0] == rules[0]:
            return True, line[1:]
        else:
            return False, line
    lch = []
    le_line = line
    for rule in rules[0].split(' '):
        ch, le_line = check(int(rule), le_line)
        lch.append(ch)  
          
    if all(lch):
        return True, le_line
    
    rch = []
    ri_line = line    
    if len(rules) != 1:
        for rule in rules[1].split(' '):
            ch, ri_line = check(int(rule), ri_line)
            rch.append(ch)
    else:
        return False, le_line
    
    if all(rch):
        return True, ri_line       
    
    return False, ri_line

ans = 0 
for line in input:
    flg, rem = check(0, line)
    if flg and rem == '':
        ans += 1
        
print(ans) 