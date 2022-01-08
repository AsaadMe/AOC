import functools

with open('2020/input.txt','r') as file:
    all_adapters = sorted([int(a) for a in file.readlines()])
    device_adaptor = max(all_adapters) + 3
    
def part1():
    jolt = 0
    diffs = []
    while jolt+3 != device_adaptor:
        
        next_adapt = min([j for j in range(jolt+1, jolt+4) if j in all_adapters])
        diffs.append(next_adapt-jolt)
        jolt = next_adapt
        
    diffs.append(3)
    print(diffs.count(1)*diffs.count(3))
    
def part2():
    all_adapters.insert(0,0)
    all_adapters.append(device_adaptor)
    
    @functools.cache
    def find_path_to_end(i):
        if i==len(all_adapters)-1:
            return 1
        ans = 0
        for j in range(i+1, len(all_adapters)):
            if all_adapters[j]-all_adapters[i]<=3:
                ans += find_path_to_end(j)
        return ans
    
    print(find_path_to_end(0))

part1()    
part2()