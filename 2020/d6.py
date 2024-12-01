from string import ascii_lowercase

with open('2020/input', 'r') as file:
    groups = file.read().split('\n\n')

all_answers = []    
for group in groups:
    answers = set(ascii_lowercase)
    for line in group.splitlines():
        answers &= set(line.strip())
            
    all_answers.append(answers)        
    
print(sum([len(a) for a in all_answers]))