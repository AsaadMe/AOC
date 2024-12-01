with open('2020/input.txt','r') as file:
    input = file.readlines()
    
def part1():
    i = 0
    accumulator = 0
    seen_structs = set()
    while i not in seen_structs:
        seen_structs.add(i)
        struct, arg = input[i].strip().split()
        arg = int(arg)
        
        if struct == 'acc':
            accumulator += arg
        elif struct == 'jmp':
            i += arg
            continue
        
        i += 1
        
    return accumulator


def part2():
    def check(input):
        i = 0
        accumulator = 0
        seen_structs = set()
        while (i not in seen_structs) and (0 <= i <= len(input)-1):
            seen_structs.add(i)
            struct, arg = input[i].strip().split()
            arg = int(arg)
            
            if struct == 'acc':
                accumulator += arg
            elif struct == 'jmp':
                i += arg
                continue
            
            if i == len(input)-2:   # last instruction is jmp +1 :))
                return accumulator
            
            i += 1
    
    for ind, ins in enumerate(input):
        new_input = input.copy()
        if 'nop' in ins:
            new_input[ind] = new_input[ind].replace('nop', 'jmp')
        elif 'jmp' in ins:
            new_input[ind] = new_input[ind].replace('jmp', 'nop')
    
        
        if ans := check(new_input):
            return ans


print(part1())
print(part2())