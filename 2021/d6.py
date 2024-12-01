def part1():
    fishes = map(int, open('input').readline().split(','))

    days = 80
    for _ in range(days):
        nfishes = []
        for fish in fishes:
            if fish == 0:
                nfishes.append(6)
                nfishes.append(8)
            else:
                nfishes.append(fish-1)

        fishes = nfishes

    print('Part1:', len(fishes))


def part2():
    fishes = {a:0 for a in range(9)}
    for n in map(int,open('input').readline().split(',')):
        fishes[n] += 1

    days = 256
    for _ in range(days):
        nfishes = {a:0 for a in range(9)}
        for fish,val in fishes.items():
            if fish == 0:
               nfishes[6] += val
               nfishes[8] += val
            else:
               nfishes[fish-1] += val

        fishes = nfishes

    print('Part2:', sum(fishes.values()))

part1()
part2()