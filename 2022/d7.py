from collections import defaultdict

with open('2022/input.txt', 'r') as file:
    curr_dir = []
    dir_size = defaultdict(list)
    for line in file:
        line = line.strip().split()
        match line:
            case ['$', 'cd', '/']:
                curr_dir.append('/')
            case ['$', 'cd', '..']:
                curr_dir.pop()
            case ['$', 'cd', next_dir]:
                curr_dir.append(next_dir)
            case [size, *rest] if size.isnumeric():
                for i in range(2,len(curr_dir)+1):
                    full_path = '/'.join(curr_dir[:i])[1:]
                    dir_size[full_path].append(int(size))
                dir_size['/'].append(int(size))
                
    ans1 = 0
    for l in dir_size.values():
        s = sum(l)
        if s <= 100000:
            ans1 += s
                        
    print('Part1:', ans1)
    
    unused = 70000000 - sum(dir_size['/'])
    need = 30000000 - unused
    
    sorted_dirs = sorted(dir_size.values(), key=lambda vals: sum(vals))
    for val in sorted_dirs:
        if sum(val) >= need:
            print('Part2:', sum(val))
            break
    