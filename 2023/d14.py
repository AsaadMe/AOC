import numpy as np

with open('input.txt','r') as file:
    board = np.array([list(line.strip()) for line in file])

def get_load(board):
    ans = 0
    for j in range(board.shape[1]):
        score = board.shape[0]
        for i in range(board.shape[0]):
            if board[i,j] == '#':
                score = board.shape[0]-i-1
            elif board[i,j] == 'O':
                ans += score
                score -= 1
    return ans            


def tilt_up(board):
    nxt = np.copy(board)
    nxt[board=='O'] = '.'
    for j in range(board.shape[1]):
        pos = 0
        for i in range(board.shape[0]):
            if board[i,j] == '#':
                pos = i+1
            elif board[i,j] == 'O':
                nxt[pos,j] = 'O'
                pos += 1
                
    return nxt
     
print('Part1: ', get_load(board))

all_board = []
for i in range(1000000000):
    board = tilt_up(board)
    board = np.rot90(board, -1)
    board = tilt_up(board)
    board = np.rot90(board)
    board = np.rot90(board,2)
    board = tilt_up(board)
    board = np.rot90(board,-2)
    board = np.rot90(board)
    board = tilt_up(board)
    board = np.rot90(board,-1)
    
    if board.tobytes() not in all_board:
        all_board.append(board.tobytes())
    else:
        ind = len(all_board)-1-all_board[::-1].index(board.tobytes())
        p = i - ind
        final_board = np.frombuffer(all_board[((1000000000-i) % p)],dtype='<U1').reshape(board.shape)
        print('Part2: ', get_load(final_board))
        break

