### NOT WORKING ###

import numpy as np

with open('2019/inputtest.txt', 'r') as file:
    board = np.array([list(line.strip()) for line in file.readlines()])


def get_visable_points(board, point):
    visp_count = 0
    for w in range(max(board.shape)):
        if w == 0:
            y = point[1] + 1
            x = point[0]
            while y < board.shape[1]:
                if board[x,y] == '#':
                    visp_count += 1
                    break
                y += 1
                
            y = point[1] - 1
            x = point[0]
            while y >= 0:
                if board[x,y] == '#':
                    visp_count += 1
                    break
                y -= 1
        elif w == 1:
            y = point[1] + 1
            while y <= board.shape[1]:
                x = y + point[0]
                if 0 <= x < board.shape[0] and board[x,y] == '#':
                    visp_count += 1
                    break
                y += 1
                
            y = point[1] - 1
            while y >= 0:
                x = y + point[0]
                if 0 <= x < board.shape[0] and board[x,y] == '#':
                    visp_count += 1
                    break
                y -= 1
                
            y = point[1] + 1
            while y <= board.shape[1]:
                x = -y + point[0]
                if 0 <= x < board.shape[0] and board[x,y] == '#':
                    visp_count += 1
                    break
                y += 1
                
            y = point[1] - 1
            while y >= 0:
                x = -y + point[0]
                if 0 <= x < board.shape[0] and board[x,y] == '#':
                    visp_count += 1
                    break
                y -= 1
        else:
            y = point[1] + 1
            while y < board.shape[1]:
                x = w * y + point[0]
                if 0 <= x < board.shape[0] and board[x,y] == '#':
                    visp_count += 1
                    break
                y += 1
                
            y = point[1] - 1
            while y >= 0:
                x = w * y + point[0]
                if 0 <= x < board.shape[0] and board[x,y] == '#':
                    visp_count += 1
                    break
                y -= 1
                
            y = point[1] + 1
            while y < board.shape[1]:
                if y % w == 0:
                    x = int(1/w * y + point[0])
                    if 0 <= x < board.shape[0] and board[x,y] == '#':
                        visp_count += 1
                        break
                y += 1
                
            y = point[1] - 1
            while y >= 0:
                if y % w == 0:
                    x = int(1/w * y + point[0])
                    if 0 <= x < board.shape[0] and board[x,y] == '#':
                        visp_count += 1
                        break
                y -= 1
                
            y = point[1] + 1
            while y < board.shape[1]:
                x = w * -y + point[0]
                if 0 <= x < board.shape[0] and board[x,y] == '#':
                    visp_count += 1
                    break
                y += 1
                
            y = point[1] - 1
            while y >= 0:
                x = w * -y + point[0]
                if 0 <= x < board.shape[0] and board[x,y] == '#':
                    visp_count += 1
                    break
                y -= 1
                
            y = point[1] + 1
            while y < board.shape[1]:
                if y % w == 0:
                    x = int(1/w * -y + point[0])
                    if 0 <= x < board.shape[0] and board[x,y] == '#':
                        visp_count += 1
                        break
                y += 1
                
            y = point[1] - 1
            while y >= 0:
                if y % w == 0:
                    x = int(1/w * -y + point[0])
                    if 0 <= x < board.shape[0] and board[x,y] == '#':
                        visp_count += 1
                        break
                y -= 1
                
    return visp_count

print(board)
print(get_visable_points(board, (2,4)))