from string import ascii_lowercase
from itertools import batched
import re

password = open('input').readline()

all_pos = []
for i in range(30):
    cand = list(batched(ascii_lowercase[i:],3))
    if cand: cand = cand[0]
    if len(cand) == 3:
        all_pos.append(''.join(cand))

def next_pass(password):
    password = list(password)
    while True:
        carry = 1
        while carry:
            for i in range(len(password)):
                ch = password[len(password)-i-1]
                ch = chr(ord(ch)+1)
                if ch == '{':
                    password[len(password)-i-1] = 'a'
                    carry = 1
                else:
                    password[len(password)-i-1] = ch
                    carry = 0
                    break
                    
        str_pass = ''.join(password)
        if ('i' not in str_pass or
            'o' not in str_pass or
            'l' not in str_pass):
            for p in all_pos:
                if p in str_pass:
                    if len(set(re.findall(r'(\w)\1',str_pass))) >= 2:
                        return str_pass

p1 = next_pass(password)              
print('Part1:', p1)
print('Part2:', next_pass(p1))