def part1():
    with open("2022/input.txt", 'r') as game:
        final_score = 0
        for round in game:
            match round.strip().split():
                case ['A', 'X']:
                    final_score += 1 + 3
                case ['A', 'Y']:
                    final_score += 2 + 6
                case ['A', 'Z']:
                    final_score += 3 + 0
                    
                case ['B', 'X']:
                    final_score += 1 + 0
                case ['B', 'Y']:
                    final_score += 2 + 3
                case ['B', 'Z']:
                    final_score += 3 + 6
                    
                case ['C', 'X']:
                    final_score += 1 + 6
                case ['C', 'Y']:
                    final_score += 2 + 0
                case ['C', 'Z']:
                    final_score += 3 + 3
            
        print('Part1:', final_score)
        
def part2():
    with open("2022/input.txt", 'r') as game:
        final_score = 0
        for round in game:
            match round.strip().split():
                case ['A', 'X']:
                    final_score += 3 + 0
                case ['A', 'Y']:
                    final_score += 1 + 3
                case ['A', 'Z']:
                    final_score += 2 + 6
                    
                case ['B', 'X']:
                    final_score += 1 + 0
                case ['B', 'Y']:
                    final_score += 2 + 3
                case ['B', 'Z']:
                    final_score += 3 + 6
                    
                case ['C', 'X']:
                    final_score += 2 + 0
                case ['C', 'Y']:
                    final_score += 3 + 3
                case ['C', 'Z']:
                    final_score += 1 + 6
            
        print('Part2:', final_score)
        
part1()
part2()