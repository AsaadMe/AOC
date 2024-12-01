with open('2022/input.txt', 'r') as file:
    ans1 = 0
    ans2 = 0
    for line in file:
        pair1, pair2 = line.strip().split(',')
        pair1_start, pair1_end = map(int, pair1.split('-'))
        pair2_start, pair2_end = map(int, pair2.split('-'))
        p1_set = set(range(pair1_start, pair1_end+1))
        p2_set = set(range(pair2_start, pair2_end+1))
        diff = p1_set & p2_set
        if diff in [p1_set, p2_set]:
            ans1 += 1
        if diff:
            ans2 += 1
            
    print('Part1:', ans1)
    print('Part2:', ans2)
    
    