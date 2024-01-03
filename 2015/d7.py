signals = dict()
insts = []
done = []

for line in open('input'):
    line = line.strip()
    inst, sig = line.split(' -> ')
    inst = [int(a) if a.isnumeric() else a for a in inst.split()]
    insts.append((inst,sig))
    done.append(False)

while not all(done):
    for i, flag in enumerate(done):
        if not flag:
            inst, sig = insts[i]

            match inst:
                case [signum]:
                    if isinstance(signum, int):
                        signals[sig] = signum
                        done[i] = True
                    elif signum in signals:
                        signals[sig] = signals[signum]
                        done[i] = True
                case [s1, 'AND'|'OR' as op, s2]:
                    if s1 == 1: # AHHHHHHH
                        if s2 in signals:
                            done[i] = True
                            match op:
                                case 'AND':
                                    signals[sig] = s1 & signals[s2]
                                case 'OR':
                                    signals[sig] = s1 | signals[s2]

                    elif s1 in signals and s2 in signals:
                        done[i] = True
                        match op:
                            case 'AND':
                                signals[sig] = signals[s1] & signals[s2]
                            case 'OR':
                                signals[sig] = signals[s1] | signals[s2]
                case [s1, 'LSHIFT'|'RSHIFT' as op, bit]:
                    if s1 in signals:
                        done[i] = True
                        match op:
                            case 'LSHIFT':
                                signals[sig] = signals[s1] << bit
                            case 'RSHIFT':
                                signals[sig] = signals[s1] >> bit
                case ['NOT', s1]:
                    if s1 in signals:
                        done[i] = True
                        signals[sig] = ~signals[s1]

print("ANS:", signals['a'])

#Part2: Change (x) -> b in input file to this input and run again.