with open('2022/input.txt', 'r') as file:
    elfs_pack = file.read().split('\n\n')
    elfs_cal = []
    for pack in elfs_pack:
        pack = map(int,pack.split())
        elfs_cal.append(sum(pack))
    
    print(f"Part1: {max(elfs_cal)}")
    print(f"Part2: {sum(sorted(elfs_cal, reverse=True)[:3])}")