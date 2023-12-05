from itertools import batched, chain

with open('input.txt','r') as file:
    inp = file.read().split('\n\n')
    

seeds1 = inp[0].split(':')[1].split()
seeds2 = []
for p in batched(inp[0].split(':')[1].split(),2):
    s,e = map(int,p)
    seeds2.append((sd for sd in range(s,s+e)))
    
seeds2 = chain(*seeds2)

inpm = [inp[1].split(':')[1].strip().splitlines(),
inp[2].split(':')[1].strip().splitlines(),
inp[3].split(':')[1].strip().splitlines(),
inp[4].split(':')[1].strip().splitlines(),
inp[5].split(':')[1].strip().splitlines(),
inp[6].split(':')[1].strip().splitlines(),
inp[7].split(':')[1].strip().splitlines()]

def find_loc(seeds):
    locs = []
    for seed in seeds:
        seed = int(seed)
        for step in inpm:
            nxt = None
            for line in step:
                dst,src,rng = map(int, line.split())
                if src+rng-1 >= seed >= src:
                    nxt = seed - src + dst
                    break
                
            if not nxt:
                nxt = seed
            seed = nxt      
        locs.append(seed)
        
    print('Part1: ', min(locs))
    
find_loc(seeds1)
find_loc(seeds2)