with open('2020/input.txt', 'r') as file:
    input = file.readlines()

def part1():
    
    def maskit(mask, val):
        new_val = list(val)
        for i in range(36):
            if mask[i] != 'X':
                new_val[i] = mask[i]
        return ''.join(new_val)

    memory = {}
    for line in input:
        line = line.strip()
        if 'mask' in line:
            mask = line.split(' = ')[1]
                
        else:
            line = line.split(' = ')
            addr = line[0][4:-1]
            val = bin(int(line[1]))[2:].rjust(36,'0')
            memory[addr] = int(maskit(mask, val), 2)
            
    print('part1:', sum(memory.values()))
        
def part2():
    
    def maskit(mask, mem_addr):
        new_addr = list(mem_addr)
        for i in range(36):
            if mask[i] == 'X':
                new_addr[i] = 'X'
            elif mask[i] == '1':
                new_addr[i] = '1'
                
        return ''.join(new_addr)
    
    def get_all_possible_addrs(mem_addr):
        all_addrs = [mem_addr]

        while 'X' in all_addrs[-1]:
            addr = all_addrs.pop()
            all_addrs.insert(0, addr.replace('X','1',1))
            all_addrs.insert(0, addr.replace('X','0',1))

        return [int(x,2) for x in all_addrs]
    
    memory = {}
    for line in input:
        line = line.strip()
        if 'mask' in line:
            mask = line.split(' = ')[1]
                
        else:
            line = line.split(' = ')
            addr = line[0][4:-1]
            addr_bin = bin(int(addr))[2:].rjust(36,'0')
            val = int(line[1])
            masked_addr = maskit(mask, addr_bin)
            all_new_addrs = get_all_possible_addrs(masked_addr)
            for addr in all_new_addrs:
                memory[addr] = val
                
    print('part2:', sum(memory.values()))

part1()    
part2()