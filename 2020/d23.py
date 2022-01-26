global_input = '418976235'

def part1():
    input = [int(a) for a in global_input]
    cur_cup = input[0]

    def move(cups:list[int], cur_cup:int):
        picks = []
        cur_cup_index = cups.index(cur_cup)

        for _ in range(3):
            if cur_cup != cups[-1]:
                picks.append(cups.pop(cur_cup_index+1))
            else:
                picks.append(cups.pop(0))

        dest_cup = cur_cup - 1
        while dest_cup in picks or dest_cup == 0:        
            dest_cup -= 1
            if dest_cup < min(cups):
                dest_cup = max(cups)
                break
            
        cur_cup_index = cups.index(cur_cup)    
        dest_cup_index = cups.index(dest_cup)

        cups = cups[0:dest_cup_index+1] + picks + cups[dest_cup_index+1:]
        
        cur_cup_index = cups.index(cur_cup)
        if cur_cup != cups[-1]:
            next_cur_cup = cups[cur_cup_index+1]
        else:
            next_cur_cup = cups[0]
        
        return cups, next_cur_cup
            
    for _ in range(100):        
        input, cur_cup = move(input, cur_cup)

    ans = ''
    while input:
        if input.index(1) != len(input)-1:
            ans += str(input.pop(input.index(1)+1))
        else:
            ans += str(input.pop(0))
    ans = ans[:-1]        
    print('Part1:', ans)
    
def part2():
    class Cup:
        def __init__(self, label=None, next=None):
            self.label = label
            self.next = next
        
        def __repr__(self) -> str:
            return f'<{self.label}, {self.next.label}>'
         
    all_cups = [Cup(int(l)) for l in global_input]
    for i,c in enumerate(all_cups[:-1]):
        c.next = all_cups[i+1]
    
    all_cups.extend([Cup(l) for l in range(10,1000001)])
    for i,c in enumerate(all_cups[8:-1]):
        c.next = all_cups[i+8+1]
        
    all_cups[-1].next = all_cups[0]
    
    all_cups = sorted(all_cups, key=lambda cup: cup.label)
    
    def move(all_cups, cur_cup):
        picks = [cur_cup.next, cur_cup.next.next, cur_cup.next.next.next]

        dest_cup_l = cur_cup.label - 1
        while dest_cup_l in [n.label for n in picks] or dest_cup_l == 0:        
            dest_cup_l -= 1
            if dest_cup_l < 1:
                dest_cup_l = 1000000
                break
                
        dest_cup_index = dest_cup_l - 1

        cur_cup.next = picks[-1].next
        picks[-1].next = all_cups[dest_cup_index].next
        all_cups[dest_cup_index].next = picks[0]
        
        return cur_cup.next
    
    cur_cup = all_cups[int(global_input[0])-1]
    for _ in range(10000000):        
        cur_cup = move(all_cups, cur_cup)
        
    print('Part2:', all_cups[0].next.label * all_cups[0].next.next.label)
 
part1()    
part2()