from collections import defaultdict

with open('2019/input.txt','r') as file:
    program = [int(opc) for opc in file.readline().strip().split(',')]
    mem = defaultdict(int)
    for i,v in enumerate(program):
        mem[i] = v
        
def run_intcode(memory:defaultdict, i:int, rel_i:int, inputs:list) -> tuple:
    #return: program, pointer, rel_i, inputs, outputs, retstate
    
    modes = []
    def get_par(parnum):
        mode = modes[parnum-1]
        if mode == 1:
            return memory[i+parnum]
        elif mode == 0:
            return memory[memory[i+parnum]]
        elif mode == 2:
            return memory[rel_i+memory[i+parnum]]
    
    def save(parnum, num):
        mode = modes[parnum-1]
        if mode == 0:
            memory[memory[i+parnum]] = num
        elif mode == 2:
            memory[rel_i+memory[i+parnum]] = num
            
    outputs = []   
    while True:
        instruct = str(memory[i]).rjust(5,'0')
        opcode = int(instruct[-2:])
        p3mode, p2mode, p1mode = map(int, instruct[:3])
        modes = [p1mode, p2mode, p3mode]
        if opcode == 99:
            i += 1
            return memory, i, rel_i, inputs, outputs, 'finish'
        elif opcode == 1:
            par1 = get_par(1)
            par2 = get_par(2)
            save(3, par1 + par2)
            i += 4
        elif opcode == 2:
            par1 = get_par(1)
            par2 = get_par(2)
            save(3, par1 * par2)
            i += 4
        elif opcode == 3:
            if not inputs:
                inputs.append(0)
            save(1, inputs.pop(0))
            i += 2
        elif opcode == 4:
            par1 = get_par(1)
            outputs.append(par1)
            i += 2
            return memory, i, rel_i, inputs, outputs, 'pause'
        elif opcode == 5:
            par1 = get_par(1)
            par2 = get_par(2)
            if par1:
                i = par2
            else:
                i += 3      
        elif opcode == 6:
            par1 = get_par(1)
            par2 = get_par(2)
            if not par1:
                i = par2
            else:
                i += 3
        elif opcode == 7:
            par1 = get_par(1)
            par2 = get_par(2)
            if par1 < par2:
                save(3, 1)
            else:
                save(3, 0)
            i += 4
        elif opcode == 8:
            par1 = get_par(1)
            par2 = get_par(2)
            if par1 == par2:
                save(3, 1)
            else:
                save(3, 0)
            i += 4
        elif opcode == 9:
            par1 = get_par(1)
            rel_i += par1 
            i += 2
        else:
            print('Wrong OP-Code!')
            break
        
    return -1

def part1(mem):
    board = defaultdict(int)
    pos = (0,0)
    all_dirs = ['N','E','S','W']
    direction = 'N'
    i, rel_i = 0, 0
    retstate = None
    while retstate != 'finish':
        
        inputs = [board[pos]]
        mem, i, rel_i, inputs, outputs, retstate = run_intcode(mem, i, rel_i, inputs)
        
        if retstate == 'finish':
            break
        
        board[pos] = outputs[0]
        mem, i, rel_i, inputs, outputs, retstate = run_intcode(mem, i, rel_i, inputs)
        
        if outputs[0] == 0:
            rot = -1
        elif outputs[0] == 1:
            rot = 1
            
        if direction == 'N':
            pos = (pos[0]+rot, pos[1])
        elif direction == 'E':
            pos = (pos[0], pos[1]-rot)
        elif direction == 'S':
            pos = (pos[0]-rot, pos[1])
        elif direction == 'W':
            pos = (pos[0], pos[1]+rot)
            
        direction = all_dirs[(all_dirs.index(direction)+rot)%4]        
                
    print('Part1:', len(board))
    
def part2(mem):
    board = defaultdict(int)
    pos = (0,0)
    board[pos] = 1
    all_dirs = ['N','E','S','W']
    direction = 'N'
    i, rel_i = 0, 0
    retstate = None
    while retstate != 'finish':
        
        inputs = [board[pos]]
        mem, i, rel_i, inputs, outputs, retstate = run_intcode(mem, i, rel_i, inputs)
        
        if retstate == 'finish':
            break
        
        board[pos] = outputs[0]
        mem, i, rel_i, inputs, outputs, retstate = run_intcode(mem, i, rel_i, inputs)
        
        if outputs[0] == 0:
            rot = -1
        elif outputs[0] == 1:
            rot = 1
            
        if direction == 'N':
            pos = (pos[0]+rot, pos[1])
        elif direction == 'E':
            pos = (pos[0], pos[1]-rot)
        elif direction == 'S':
            pos = (pos[0]-rot, pos[1])
        elif direction == 'W':
            pos = (pos[0], pos[1]+rot)
            
        direction = all_dirs[(all_dirs.index(direction)+rot)%4]        
                
    min_x, *_, max_x = sorted([p[0] for p in board])
    min_y, *_, max_y = sorted([p[1] for p in board])
    
    print('Part2:')
    for i in range(max_x, min_x-1, -1):
        for j in range(max_y, min_y-1, -1):
            if board[(i,j)]:
                print('#', end='')
            else:
                print(' ', end='')
        print('\n', end='')
    
part1(mem)
part2(mem)