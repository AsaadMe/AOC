def part1():
    
    with open('2022/input.txt', 'r') as file:
        
        head = [0,0] # x(hor), y(ver)
        tail = [0,0]
        tail_visited = {(0,0)}
        
        for inst in file:
            direction, val = inst.strip().split()
            val = int(val)
            
            if direction == 'R':
                for _ in range(val):
                    if (head[1]-tail[1] != 0) and (head[0]-tail[0] == 1):
                        tail[1] += head[1]-tail[1]
                    if head[0]-tail[0] == 1:
                        tail[0] += 1
                        
                    head[0] += 1
                    tail_visited.add(tuple(tail))
                    
            elif direction == 'U':
                for _ in range(val):
                    if (head[0]-tail[0] != 0) and (head[1]-tail[1] == 1):
                        tail[0] += head[0]-tail[0]
                    if head[1]-tail[1] == 1:
                        tail[1] += 1
                        
                    head[1] += 1
                    tail_visited.add(tuple(tail))
                    
            elif direction == 'D':
                for _ in range(val):
                    if (head[1]-tail[1] == -1) and (head[0]-tail[0] != 0):
                        tail[0] += head[0]-tail[0]
                    if head[1]-tail[1] == -1:
                        tail[1] -= 1
                        
                    head[1] -= 1
                    tail_visited.add(tuple(tail))
                    
            elif direction == 'L':
                for _ in range(val):
                    if (head[1]-tail[1] != 0) and (head[0]-tail[0] == -1):
                        tail[1] += head[1]-tail[1]
                    if head[0]-tail[0] == -1:
                        tail[0] -= 1
                        
                    head[0] -= 1
                    tail_visited.add(tuple(tail))

    print('Part1:', len(tail_visited))
    
def part2():
    with open('2022/input.txt', 'r') as file:
        rope = [[0,0] for _ in range(10)]
        
        def sign(x):
            if x > 0: return 1
            if x < 0: return -1
            if x == 0: return 0

        ans = set()
        for inst in file:
            direction, val = inst.strip().split()
            val = int(val)
            ans.add(tuple(rope[-1]))
            for _ in range(val):
                dx, dy = {"U":(0,1),"D":(0,-1),"R":(1,0),"L":(-1,0)}[direction]
                rope[0][0] += dx
                rope[0][1] += dy
                for i in range(1,10):
                    hx,hy = rope[i-1]
                    tx,ty = rope[i]
                    dx = tx-hx
                    dy = ty-hy
                    if dx == 0 or dy == 0:
                        if abs(dx) >= 2:
                            rope[i][0] -= sign(dx)
                        if abs(dy) >= 2:
                            rope[i][1] -= sign(dy)
                    elif (abs(dx),abs(dy)) != (1,1):
                        rope[i][0] -= sign(dx)
                        rope[i][1] -= sign(dy)
                ans.add(tuple(rope[-1]))
    print('Part2:', len(ans))
    
    
part1()
part2()