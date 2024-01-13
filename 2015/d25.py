row,col = 3010,3019
nth = sum(range(row+col-1)) + col

code = 20151125
for i in range(nth-1):
    code = code * 252533 % 33554393

print('Part1:', code)