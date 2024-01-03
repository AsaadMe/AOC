from hashlib import md5

inp = "bgvyzdsv"

for i in range(1000000000):
    if md5((inp+str(i)).encode()).hexdigest().startswith('0'*5):
        print('Part1:', i)
        break

for i in range(1000000000):
    if md5((inp+str(i)).encode()).hexdigest().startswith('0'*6):
        print('Part2:', i)
        break