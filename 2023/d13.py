import numpy as np

with open('2023/input.txt','r') as file:
    input = file.read().split('\n\n')
    patterns = []
    for pattern in input:
        patterns.append(np.array([list(a) for a in pattern.splitlines()]))

def vertical_chk(pattern):
    for i in range(1,pattern.shape[1]-1):
        if np.array_equal(np.fliplr(pattern[:,i:]), pattern[:,i:]) and (pattern.shape[1]-i)%2==0:
            return int((pattern.shape[1]-i)/2+i)
        if np.array_equal(np.fliplr(pattern[:,:-i]), pattern[:,:-i]) and (i+1)%2==0:
            return int((pattern.shape[1]-i)/2)
    return 0
    
def horizontal_chk(pattern):
    for i in range(1,pattern.shape[0]-1):
        if np.array_equal(np.flipud(pattern[i:,:]), pattern[i:,:]) and (pattern.shape[1]-i)%2==0:
            return int((pattern.shape[0]-i)/2+i)
        if np.array_equal(np.flipud(pattern[:-i,:]), pattern[:-i,:]) and (i+1)%2==0:
            return int((pattern.shape[0]-i)/2)
    return 0
    
ans = []
for pattern in patterns:
    ans.append(vertical_chk(pattern))
    ans.append(horizontal_chk(pattern)*100)
    
print(sum(ans))

        
        