def get_input():
    with open('2020/input.txt','r') as file:
        pl1, pl2 = file.read().split('\n\n')
        pl1 = [int(a.strip()) for a in pl1.splitlines()[1:]]
        pl2 = [int(a.strip()) for a in pl2.splitlines()[1:]]
    return pl1, pl2
    
def part1():
    pl1, pl2 = get_input()
    while all([len(pl1), len(pl2)]):
        front_card1 = pl1.pop(0)
        front_card2 = pl2.pop(0)
        
        if front_card1 > front_card2:
            pl1.extend([front_card1, front_card2])
        else:
            pl2.extend([front_card2, front_card1])
    
    ans = 0
    winner = pl1 if pl1 else pl2
    for i, card in enumerate(reversed(winner)):
         ans += (i+1)*card
         
    print('Part1:', ans)


def part2():
    def play_game(p1, p2):
        seen1, seen2 = set(), set()

        while len(p1) > 0 and len(p2) > 0:
            s1 = ",".join([str(c) for c in p1])
            s2 = ",".join([str(c) for c in p2])
            if s1 in seen1 or s2 in seen2:
                return "p1", p1
            
            seen1.add(s1)
            seen2.add(s2)

            a, b = p1.pop(0), p2.pop(0)
            if a <= len(p1) and b <= len(p2):
                winner, _ = play_game(p1.copy()[:a], p2.copy()[:b])
            else:
                if a > b:
                    winner = "p1"
                else:
                    winner = "p2"
            
            if winner == "p1":
                p1 += [a,b]
            else:
                p2 += [b,a]

        if len(p1) > 0:
            return "p1", p1
        else:
            return "p2", p2

    pl1, pl2 = get_input()
    _, winner = play_game(pl1.copy(), pl2.copy())
    ans = 0
    for i, card in enumerate(reversed(winner)):
         ans += (i+1)*card
         
    print('Part2:', ans)
    
part1()
part2()