from itertools import cycle

pos = (0,0)
visited = set()
visited.add(pos)
dir_map = {'<':(0,-1),'>':(0,1),'^':(-1,0),'v':(1,0)}
for dir in open('input').read():
    pos = (pos[0]+dir_map[dir][0],pos[1]+dir_map[dir][1])
    visited.add(pos)

print("Part1:", len(visited))

poses = [(0,0),(0,0)]
visited = set()
visited.add((0,0))
santanum = cycle([0,1])
for dir in open('input').read():
    santa = next(santanum)
    poses[santa] = (poses[santa][0]+dir_map[dir][0],poses[santa][1]+dir_map[dir][1])
    visited.add(poses[santa])

print("Part2:", len(visited))
