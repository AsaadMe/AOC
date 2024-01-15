import numpy as np

with open('input') as file:
    nums ,*boards = file.read().split('\n\n')
    nums = map(int, nums.split(','))
    boards = [line.splitlines() for line in boards]
    for b in range(len(boards)):
        for i in range(len(boards[b])):
            boards[b][i] = [int(a) for a in boards[b][i].split()]
        boards[b] = np.array(boards[b])

check_boards = [np.zeros_like(b) for b in boards]

def check_bingo(chk_board):
    if any(chk_board.all(axis=0)) or any(chk_board.all(axis=1)):
        return True
    else:
        return False
    
def run():
    winners = {}
    for num in nums:
        for i, board in enumerate(boards):
            if num in board and i not in winners:
                check_boards[i][board == num] = 1
                if check_bingo(check_boards[i]):
                    winners[i] = num
                    if len(winners) == len(boards):
                        return winners
    
def solve(winners):
    sum1 = 0
    i = list(winners)[0]
    num = winners[i]
    for j in range(boards[0].shape[0]):
        for k in range(boards[0].shape[1]):
            if not check_boards[i][j,k]:
                sum1 += boards[i][j,k]
    print('Part1:', sum1 * num)

    sum2 = 0
    i = list(winners)[-1]
    num = winners[i]
    for j in range(boards[0].shape[0]):
        for k in range(boards[1].shape[1]):
            if not check_boards[i][j,k]:
                sum2 += boards[i][j,k]
    print('Part2:', sum2 * num)

solve(run())