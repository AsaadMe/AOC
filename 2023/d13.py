import numpy as np

with open('input.txt','r') as file:
    input = file.read().split('\n\n')
    patterns = []
    for pattern in input:
        patterns.append(np.array([list(a) for a in pattern.splitlines()]))

def vertical_chk(pattern, alt=0):
    if not alt:
        for i in range(1,pattern.shape[1]-1):
            if np.array_equal(np.fliplr(pattern[:,i:]), pattern[:,i:]) and (pattern.shape[1]-i)%2==0:
                return int((pattern.shape[1]-i)/2+i)
            if np.array_equal(np.fliplr(pattern[:,:-i]), pattern[:,:-i]) and (i+1)%2==0:
                return int((pattern.shape[1]-i)/2)
        return 0
    else:
        for i in range(1,pattern.shape[1]-1):
            if (len([a for a in (np.fliplr(pattern[:,i:]) == pattern[:,i:]).ravel() if not a]) == 2) and (pattern.shape[1]-i)%2==0:
                return int((pattern.shape[1]-i)/2+i)    
            if (len([a for a in (np.fliplr(pattern[:,:-i]) == pattern[:,:-i]).ravel() if not a]) == 2) and (i+1)%2==0:
                return int((pattern.shape[1]-i)/2)
        return 0           
                
def horizontal_chk(pattern,alt=0):
    if not alt:
        for i in range(1,pattern.shape[0]-1):
            if np.array_equal(np.flipud(pattern[i:,:]), pattern[i:,:]) and (pattern.shape[1]-i)%2==0:
                return int((pattern.shape[0]-i)/2+i)
            if np.array_equal(np.flipud(pattern[:-i,:]), pattern[:-i,:]) and (i+1)%2==0:
                return int((pattern.shape[0]-i)/2)
        return 0
    else:
        for i in range(1,pattern.shape[0]-1):
            if (len([a for a in (np.flipud(pattern[i:,:]) == pattern[i:,:]).ravel() if not a]) == 2) and (pattern.shape[1]-i)%2==0:
                return int((pattern.shape[0]-i)/2+i)
            if (len([a for a in (np.flipud(pattern[:-i,:]) == pattern[:-i,:]).ravel() if not a]) == 2) and (i+1)%2==0:
                return int((pattern.shape[0]-i)/2)
        return 0
    
    
ans1 = []
for pattern in patterns:
    ans1.append(vertical_chk(pattern))
    ans1.append(horizontal_chk(pattern)*100)
    
print('Part1: ', sum(ans1))

ans2 = []
for pattern in patterns:
    ans2.append(vertical_chk(pattern, alt=1))
    ans2.append(horizontal_chk(pattern, alt=1)*100)
    
print('Part2: ', sum(ans2))