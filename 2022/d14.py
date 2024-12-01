from copy import deepcopy

def draw_board(board):
    ground_y = max([a[1] for a in board])
    for i in range(ground_y+1):
        for j in range(min([a[0] for a in board]),max([a[0] for a in board])+1):
            print(board.get((j,i),'.'), end='')
        print()


with open('2022/input.txt', 'r') as file:
    board = {}
    for line in file:
        line = line.strip().split('->')
        for i in range(len(line)-1):
            m1, m2 = line[i], line[i+1]
            m1 = int(m1.split(',')[0]),int(m1.split(',')[1])
            m2 = int(m2.split(',')[0]),int(m2.split(',')[1])
            if m1[0] == m2[0]:
                s = sorted([m1[1],m2[1]])
                for j in range(s[0], s[1]+1):
                    board[(m1[0],j)] = '#'
            elif m1[1] == m2[1]:
                s = sorted([m1[0],m2[0]])
                for j in range(s[0], s[1]+1):
                    board[(j,m1[1])] = '#'

def part1(board):
    ground_y = max([a[1] for a in board])
    end_flag = False
    while not end_flag:
        cur_point = (500,0)
        
        while True:
            if (next_p := (cur_point[0],cur_point[1]+1)) not in board:
                cur_point = next_p
            elif (next_p := (cur_point[0]-1,cur_point[1]+1)) not in board:
                cur_point = next_p
            elif (next_p := (cur_point[0]+1,cur_point[1]+1)) not in board:
                cur_point = next_p
            else:
                if cur_point[1] < ground_y:
                    board[cur_point] = 'O'
                    break

            if cur_point[1] >= ground_y:
                end_flag = True
                break

    # draw_board(board)            
    print('Part1:', sum([1 for a in board.values() if a == 'O']))

def part2(board):
    ground_y = max([a[1] for a in board]) + 2
    end_flag = False
    while not end_flag:
        cur_point = (500,-1)
        
        while True:
            if ((next_p := (cur_point[0],cur_point[1]+1)) not in board
            and next_p[1] < ground_y):
                cur_point = next_p
            elif ((next_p := (cur_point[0]-1,cur_point[1]+1)) not in board
            and next_p[1] < ground_y) :
                cur_point = next_p
            elif ((next_p := (cur_point[0]+1,cur_point[1]+1)) not in board
                and next_p[1] < ground_y):
                cur_point = next_p
            else:
                board[cur_point] = 'O'
                break

            if board.get((500,0)) == 'O':
                end_flag = True
                break

    # draw_board(board)
    print('Part2:', sum([1 for a in board.values() if a == 'O']))

part1(deepcopy(board))
part2(deepcopy(board))
