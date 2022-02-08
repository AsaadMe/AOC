with open('2019/input.txt','r') as file:
    program = [int(opc) for opc in file.readline().strip().split(',')]

def run_intcode(memory, input=0):
    def get_par(mode, parnum):
        if mode:
            return memory[i+parnum]
        else:
            return memory[memory[i+parnum]]
        
    i = 0
    outputs = []   
    while True:
        instruct = str(memory[i]).rjust(5,'0')
        opcode = int(instruct[-2:])
        p3mode, p2mode, p1mode = map(int, instruct[:3])
        if opcode == 99:
            i += 1
            break
        elif opcode == 1:
            par1 = get_par(p1mode, 1)
            par2 = get_par(p2mode, 2)
            memory[memory[i+3]] = par1 + par2
            i += 4
        elif opcode == 2:
            par1 = get_par(p1mode, 1)
            par2 = get_par(p2mode, 2)
            memory[memory[i+3]] = par1 * par2
            i += 4
        elif opcode == 3:
            memory[memory[i+1]] = input
            i += 2
        elif opcode == 4:
            par1 = get_par(p1mode, 1)
            outputs.append(par1)
            i += 2
        elif opcode == 5:
            par1 = get_par(p1mode, 1)
            par2 = get_par(p2mode, 2)
            if par1:
                i = par2
            else:
                i += 3      
        elif opcode == 6:
            par1 = get_par(p1mode, 1)
            par2 = get_par(p2mode, 2)
            if not par1:
                i = par2
            else:
                i += 3
        elif opcode == 7:
            par1 = get_par(p1mode, 1)
            par2 = get_par(p2mode, 2)
            if par1 < par2:
                memory[memory[i+3]] = 1
            else:
                memory[memory[i+3]] = 0
            i += 4
        elif opcode == 8:
            par1 = get_par(p1mode, 1)
            par2 = get_par(p2mode, 2)
            if par1 == par2:
                memory[memory[i+3]] = 1
            else:
                memory[memory[i+3]] = 0
            i += 4
        else:
            print('Wrong OP-Code!')
            break
        
    return memory, outputs


print('Part1:', run_intcode(program.copy(), input=1)[1])
print('Part2:', run_intcode(program.copy(), input=5)[1])