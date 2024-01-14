inp = [l.strip() for l in open('input')]

def find_commons_bits(inp):
    most_commons = {}
    for i in range(len(inp[0])):
        zero,one = 0,0
        for line in inp:
            if line[i] == '0':
                zero += 1
            else:
                one += 1

        if zero > one:
            most_commons[i] = '0'

        else:
            most_commons[i] = '1'
    return most_commons

commons = find_commons_bits(inp)
gamma = '0b'+''.join(commons.values())
eps = '0b'+''.join(['1' if el=='0' else '0' for el in commons.values()])

print('Part1:', int(gamma,2)*int(eps,2))

inp1 = inp.copy()
i = 0
while len(inp1) > 1:
    nxt = []
    for n in inp1:
        commons = find_commons_bits(inp1)
        if n[i] == commons[i]:
            nxt.append(n)
    i += 1
    inp1 = nxt

inp2 = inp.copy()
i = 0
while len(inp2) > 1:
    nxt = []
    for n in inp2:
        commons = find_commons_bits(inp2)
        if n[i] != commons[i]:
            nxt.append(n)
    i += 1
    inp2 = nxt

print('Part2:', int('0b'+inp1[0],2)*int('0b'+inp2[0],2))