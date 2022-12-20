# Using LinkedList (Stupid idea!)

class Num:
    def __init__(self, val:int, prev_num=None, next_num=None) -> None:
        self.val = val
        self.prev_num = prev_num
        self.next_num = next_num
    
    def __repr__(self) -> str:
        return f'<Num>: ({self.val}, {self.prev_num.val}, {self.next_num.val})'    
        
with open('2022/input.txt', 'r') as file:
    l1 = [int(a) for a in file]
    l2 = [a*811589153 for a in l1]
    ind_0 = l1.index(0)
    
    seq1 = [Num(a) for a in l1]
    for i in range(len(seq1)-1):
        seq1[i].prev_num = seq1[i-1]
        seq1[i].next_num = seq1[i+1]
    seq1[-1].prev_num = seq1[-2]
    seq1[-1].next_num = seq1[0]
    
    seq2 = [Num(a) for a in l2]
    for i in range(len(seq2)-1):
        seq2[i].prev_num = seq2[i-1]
        seq2[i].next_num = seq2[i+1]
    seq2[-1].prev_num = seq2[-2]
    seq2[-1].next_num = seq2[0]

def mix(seq):        
    for n in seq:
        shift = n.val % (len(seq)-1)
        if shift > 0:
            prev = n.next_num
            for _ in range(shift-1):
                prev = prev.next_num
            next = prev.next_num
            tn = n.next_num
            tp = n.prev_num
            n.prev_num = prev
            n.next_num = next
            prev.next_num = n
            next.prev_num = n
            tp.next_num = tn
            tn.prev_num = tp
            
        elif shift < 0:
            next = n.prev_num
            for _ in range(abs(shift)-1):
                next = next.prev_num
            prev = next.prev_num
            tn = n.next_num
            tp = n.prev_num
            n.prev_num = prev
            n.next_num  = next
            prev.next_num = n
            next.prev_num = n
            tp.next_num = tn
            tn.prev_num = tp
            
    return seq


seq = mix(seq1)
ans1 = 0
for t in [1000,2000,3000]:
    p = seq[ind_0]        
    for _ in range(t):
        p = p.next_num
    ans1 += p.val   
print('Part1:', ans1)
        

for _ in range(10):
    seq = mix(seq2)   
ans1 = 0
for t in [1000,2000,3000]:
    p = seq[ind_0]        
    for _ in range(t):
        p = p.next_num
    ans1 += p.val  
print('Part2:', ans1)