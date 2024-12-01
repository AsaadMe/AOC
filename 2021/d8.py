def part1():
    ans = 0
    for line in open('input').readlines():
        out = line.strip().split(' | ')[1].split()
        ans += len([seg for seg in out if len(seg) in (2,4,3,7)])
    print('Part1:', ans)


def part2():
    ans = 0
    nums = {}
    segs = {}
    for line in open('input').readlines():
        pats, out = map(str.split, line.strip().split(' | '))
        nums['1'] = [p for p in pats if len(p)==2][0]
        nums['4'] = [p for p in pats if len(p)==4][0]
        nums['7'] = [p for p in pats if len(p)==3][0]
        nums['8'] = [p for p in pats if len(p)==7][0]

        segs['a'] =  ''.join(set(nums['7']) - set(nums['1']))
        segs['cf'] = nums['1']
        segs['bd'] = ''.join(set(nums['4']) - set(nums['1']))
        segs['eg'] = ''.join(set(nums['8']) - set(segs['a']) - set(segs['bd']) - set(segs['cf']))
        nums['6'] = ''.join([p for p in pats if len(set(segs['a']+segs['bd']+segs['eg']) - set(p))==0 and p!=nums['8']][0])
        segs['f'] = ''.join(set(nums['6']) - set(segs['a']+segs['bd']+segs['eg']))
        segs['c'] = ''.join(set(segs['cf']) - set(segs['f']))
        nums['0'] = ''.join([p for p in pats if len(set(segs['a']+segs['cf']+segs['eg']) - set(p))==0 and p!=nums['8']][0])
        segs['b'] = ''.join(set(nums['0']) - set(segs['a']) - set(segs['cf']) - set(segs['eg']))
        segs['d'] = ''.join(set(nums['4']) - set(segs['b']) - set(segs['cf']))
        nums['9'] = ''.join([p for p in pats if len(set(segs['a']+segs['cf']+segs['bd']) - set(p))==0 and p!=nums['8']][0])
        segs['g'] = ''.join(set(nums['9']) - set(segs['a']) - set(segs['cf']) - set(segs['bd']))
        nums['5'] = ''.join(segs['a'] + segs['b'] + segs['d'] + segs['f'] + segs['g'])
        segs['e'] = ''.join(set(nums['8']) - set(segs['bd']) - set(segs['cf']) - set(segs['a']) - set(segs['g']))
        nums['2'] = segs['eg'] + segs['a'] + segs['c'] + segs['d']
        nums['3'] = segs['cf'] + segs['a'] + segs['d'] + segs['g']
        
        mapping = {}
        outnum = ''
        for k,v in nums.items():
            mapping[''.join(sorted(v))] = int(k)

        for n in out:
            outnum += str(mapping[''.join(sorted(n))])

        ans += int(outnum)

    print('Part2:', ans)

part1()
part2()