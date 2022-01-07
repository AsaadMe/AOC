import re

with open('2020/input.txt','r') as file:
    input = file.readlines()
    
def evinpp1(line):
    while se := re.search(f'\d+[+*]\d+', line):
        line = line.replace(line[se.span()[0]:se.span()[1]], str(eval(se.group())), 1)
    return line.replace('(','').replace(')','')

def evinpp2(line):
    while se := re.search(f'\d+\+\d+', line):
        line = line.replace(line[se.span()[0]:se.span()[1]], str(eval(se.group())), 1)
    line = eval(line)
    return str(line)

def part1():
    all_ans = []
    for line in input:
        
        line = line.strip().replace(' ','')
        
        while se := re.search(r'\([^()]+\)', line):
            line = line.replace(line[se.span()[0]:se.span()[1]], evinpp1(se.group()), 1)
        line = evinpp1(line)
        all_ans.append(int(line))
        
    print('part1:', sum(all_ans))   
    
def part2():
    all_ans = []
    for line in input:
        
        line = line.strip().replace(' ','')
        
        while se := re.search(r'\([^()]+\)', line):
            line = line.replace(line[se.span()[0]:se.span()[1]], evinpp2(se.group()), 1)
        line = evinpp2(line)
        all_ans.append(int(line))

    print('part2:', sum(all_ans)) 

part1()    
part2()