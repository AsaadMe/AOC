import re

with open('2022/input.txt', 'r') as file:
    input = [a.strip() for a in file]

def SNAFU_to_dec(snafu:str) -> int:
    dec = 0
    snafu = re.sub(r'(.)(?!$)', r'\1,', snafu).replace('-','-1').replace('=','-2').split(',')
    for i,c in enumerate(snafu,1):
        r = len(snafu)-i
        dec += (5**r) * int(c)
    return dec

def dec_to_SNAFU(dec:int) -> str:
    snafu = ''
    while dec > 0:
        dec, rem = (dec+2) // 5, (dec+2) % 5
        snafu += '=-012'[rem]
    return snafu[::-1]
    

s = sum([SNAFU_to_dec(a) for a in input])
ans = dec_to_SNAFU(s)
print(ans)
