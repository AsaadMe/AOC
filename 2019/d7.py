import itertools

with open('2019/input.txt','r') as file:
    program = [int(opc) for opc in file.readline().strip().split(',')]

def run_intcode(memory, i:int, inputs:list) -> tuple:  # return: program, pointer, inputs, outputs, retstate 
    def get_par(mode, parnum):
        if mode:
            return memory[i+parnum]
        else:
            return memory[memory[i+parnum]]
        
    outputs = []   
    while True:
        instruct = str(memory[i]).rjust(5,'0')
        opcode = int(instruct[-2:])
        p3mode, p2mode, p1mode = map(int, instruct[:3])
        if opcode == 99:
            i += 1
            return memory, i, inputs, outputs, 'finish'
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
            if not inputs:
                inputs.append(0)
            memory[memory[i+1]] = inputs.pop(0)
            i += 2
        elif opcode == 4:
            par1 = get_par(p1mode, 1)
            outputs.append(par1)
            i += 2
            return memory, i, inputs, outputs, 'pause'
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
        
    return -1

def part1():
    thruster_sig = 0
    for phase_settings in itertools.permutations([0,1,2,3,4], 5):
        nextin = [0]
        for i in [0,1,2,3,4]:
            _, _, _, nextin, _ = run_intcode(program, 0, [phase_settings[i], *nextin])

        if nextin[0] > thruster_sig:
            thruster_sig = nextin[0]
            
    print('Part1:', thruster_sig)

def part2():
    thruster_sig = 0
    for phase_settings in itertools.permutations([5,6,7,8,9], 5):
        amps = []  # program, pointer, inputs
        for _ in range(5):
            amps.append([program.copy(), 0, []])
            
        for ind, phase in enumerate(phase_settings):
            amps[ind][2].append(phase)
        amps[0][2].append(0)

        for i in itertools.cycle([0,1,2,3,4]):
            nextprogram, ip, inputs, outputs, state = run_intcode(*amps[i])

            if state == 'finish':
                if inputs[0] > thruster_sig:
                    thruster_sig = inputs[0]
                break
            
            amps[i] = [nextprogram, ip, inputs]
            next_amp = (i+1) % 5
            amps[next_amp][2].extend(outputs)

    print('Part2:', thruster_sig)
    
part1()
part2()