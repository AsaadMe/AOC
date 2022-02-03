with open('2019/input.txt','r') as file:
    program = [int(opc) for opc in file.readline().strip().split(',')]

def run_intcode(memory):
    i = 0    
    while True:
        if memory[i] == 99:
            i += 1
            break
        elif memory[i] == 1:
            memory[memory[i+3]] = memory[memory[i+1]] + memory[memory[i+2]]
            i += 4
        elif memory[i] == 2:
            memory[memory[i+3]] = memory[memory[i+1]] * memory[memory[i+2]]
            i += 4
        else:
            print('Wrong OP-Code!')
            break
        
    return memory

def part1():
    memory = program.copy()
    memory[1] = 12
    memory[2] = 2
         
    print('Part1:', run_intcode(memory)[0])

def part2():
    for noun in range(100):
        for verb in range(100):
                memory = program.copy()
                memory[1] = noun
                memory[2] = verb
                if run_intcode(memory)[0] == 19690720:
                    print('Part2:', 100 * noun + verb)
part1()
part2()