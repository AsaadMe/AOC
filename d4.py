from string import digits
import re

with open('2020/input', 'r') as file:
    input = file.read().strip()

passports = []    
for passport in input.split('\n\n'):
    pas = {}
    for line in passport.splitlines():
        for t in line.split():
            k,v = t.split(':')
            pas[k] = v
        
    passports.append(pas)            

validity_check = {'byr':lambda x: 1 if 1920 <= int(x) <= 2002 else 0,
                  'iyr':lambda x: 1 if 2010 <= int(x) <= 2020 else 0,
                  'eyr':lambda x: 1 if 2020 <= int(x) <= 2030 else 0,
                  'hgt':lambda x: 1 if (x.endswith('cm') and 150 <= int(x[:-2]) <= 193) or (x.endswith('in') and 59 <= int(x[:-2]) <= 76) else 0,
                  'hcl':lambda x: 1 if re.match(r'^#[0-9a-f]{6}$', x) else 0,
                  'ecl':lambda x: 1 if x in 'amb blu brn gry grn hzl oth' else 0,
                  'pid':lambda x: 1 if len(x) == 9 and any([a in digits for a in x]) else 0}
ans = 0                
for ps in passports:
    chf = 0
    for k,v in ps.items():
        if k != 'cid':
            if validity_check[k](v):
                chf += 1
    if chf == 7:
        ans += 1
        
print(ans)
    