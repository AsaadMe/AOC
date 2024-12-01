pkey1 = 8987316
pkey2 = 14681524

def find_loop_size(pkey):
    subnum = 7
    i = 1
    num = 1
    while True:
        num *= subnum
        num = num % 20201227
        if num == pkey:
            return i
        i += 1

def find_encryption_key(pubkey, otherlsize):
    subnum = pubkey
    num = 1
    for _ in range(otherlsize):
        num *= subnum
        num = num % 20201227
    return num
   
lsize2 = find_loop_size(pkey2)

enc = find_encryption_key(pkey1, lsize2)
print('Part1:', enc)