from collections import Counter

with open('2020/input', 'r') as file:
    input = file.readlines()
    
def part1():
    ans = 0   
    for line in input:
        line = line.split()
        lower_bound, higher_band = map(int, line[0].split('-'))
        the_char = line[1][0]
        password = line[2]
        
        c = Counter(password)
        if lower_bound <= c[the_char] <= higher_band:
            ans += 1
    return ans
    
def part2():
    ans = 0   
    for line in input:
        line = line.split()
        first_ind, second_ind = [int(a)-1 for a in line[0].split('-')]
        the_char = line[1][0]
        password = line[2]
        
        if ((password[first_ind] == the_char and password[second_ind] != the_char) or 
            (password[first_ind] != the_char and password[second_ind] == the_char)):
            ans += 1       
    return ans
    
print(part2())
    