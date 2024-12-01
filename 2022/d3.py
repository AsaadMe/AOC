with open('2022/input.txt', 'r') as file:
    ans = 0
    for sack in file:
        sack = sack.strip()
        lsack, rsack = sack[:len(sack)//2], sack[len(sack)//2:]
        err = (set(lsack) & set(rsack)).pop()

        if err.islower():
            ans += ord(err) - 96
        else:
            ans += ord(err) - 38
            
    print('Part1:', ans)

with open('2022/input.txt', 'r') as file:   
    ans = 0 
    groups = list(zip(*[file] * 3))
    for group in groups:
        group = [a.strip() for a in group]
        err = (set(group[0]) & set(group[1]) & set(group[2])).pop()
        if err.islower():
            ans += ord(err) - 96
        else:
            ans += ord(err) - 38
            
    print('Part2:', ans)