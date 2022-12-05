from copy import deepcopy

with open('2022/input.txt', 'r') as file:
    input = file.read()
    
    draw, insts = input.split('\n\n')
    draw = draw.splitlines()
    insts = insts.splitlines()
    
    last_line = draw[-1]
    draw = draw[:-1]
    all_containers = []

    for col_i in range(1, len(last_line), 4):
        col_containers = []
        for container in draw:
            if container[col_i] != ' ':
                col_containers.append(container[col_i])
        all_containers.append(col_containers)
    
    all_containers_p1 = deepcopy(all_containers)
    all_containers_p2 = deepcopy(all_containers)  
     
    for inst in insts:
        inst = inst.split()
        n_cont = int(inst[1])
        src = int(inst[3])-1
        dst = int(inst[5])-1
        
        to_move = []
        for i in range(n_cont):
            to_move.append(all_containers_p1[src].pop(0))
        
        for c in to_move:
            all_containers_p1[dst].insert(0, c)
        
        to_move = all_containers_p2[src][:n_cont]
        del all_containers_p2[src][:n_cont]
        
        all_containers_p2[dst] = to_move + all_containers_p2[dst]
            
    print('Part1:', ''.join([a[0] for a in all_containers_p1]))
    print('Part2:', ''.join([a[0] for a in all_containers_p2]))   