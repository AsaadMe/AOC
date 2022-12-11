from math import prod

with open('2022/input.txt', 'r') as file:
    monk_inst = file.read().split('\n\n')
    
    monk_list = []
    
    def oper_func(monk):
        return lambda x: eval(monk[1].split('=')[1].strip().replace('old', str(x)))
    
    def test_func(monk):
        r = int(monk[2].split('by')[-1])
        m1 = int(monk[3].split('monkey')[-1])
        m2 = int(monk[4].split('monkey')[-1])
        return lambda x: m1 if x % r == 0 else m2
    
    univ_mod = 1 #P2
    for monk in monk_inst:
        monk = monk.splitlines()[1:]
        univ_mod *= int(monk[2].split('by')[-1]) #P2
        items = [int(a) for a in monk[0].strip().split(':')[1].strip().split(',')]
        monk_list.append({'items':items, 'oper':oper_func(monk), 'test':test_func(monk), 'inspect_count':0})
    
    ### (PART 1) ###
    # for _ in range(20):
    #     for monk in monk_list:
    #         for _ in range(len(monk['items'])):
    #             monk['inspect_count'] += 1
    #             monk_item = monk['items'].pop(0)
    #             new = int(monk['oper'](monk_item) / 3)
    #             next_monk = monk['test'](new)
    #             monk_list[next_monk]['items'].append(new)
                
    # print('Part1:', prod(sorted([m['inspect_count'] for m in monk_list], reverse=True)[:2]))
    
    ### (PART 2) ###            
    for _ in range(10000):
        for monk in monk_list:
            for _ in range(len(monk['items'])):
                monk['inspect_count'] += 1
                monk_item = monk['items'].pop(0)
                new = monk['oper'](monk_item) % univ_mod
                next_monk = monk['test'](new)
                monk_list[next_monk]['items'].append(new)
                
    print('Part2:', prod(sorted([m['inspect_count'] for m in monk_list], reverse=True)[:2]))
        