with open('2022/input.txt', 'r') as file:
    
    def get_val(cyclemap, cycle):
        for i in range(cycle, 0, -1):
            if i in cyclemap:
                return cyclemap[i]
              
    cur_cycle = 1
    cur_xval = 1
    xval_cycle = {1:1}
    for inst in file:
        inst = inst.strip()
        if inst == 'noop':
            cur_cycle += 1
        else:
            num = int(inst.split()[1])
            cur_xval += num
            cur_cycle += 2
            xval_cycle[cur_cycle] = cur_xval
    
    ans1 = 0
    for c in [20, 60, 100, 140, 180, 220]:
        ans1 += get_val(xval_cycle, c) * c
    print('Part1:', ans1, '\n')
    
    screen = []
    for r in range(1, 7):
        row = ''
        for c in range(40 * (r-1), 40 * r):
            middle_sprite = get_val(xval_cycle, c+1)
            if c%40 in [middle_sprite-1, middle_sprite, middle_sprite+1]:
                row += '#'
            else:
                row += '.'
        screen.append(row)
    
    print('Part2:')    
    for row in screen:
        print(row)