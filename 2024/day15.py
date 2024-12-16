board = {}
with open("input.txt") as file:
    mp, insts = file.read().split("\n\n")
    mp = mp.splitlines()
    insts = insts.strip()

for x, line in enumerate(mp):
    for y, char in enumerate(line.strip()):
        if char == "@":
            cur_pos = (x, y)
        if char != ".":
            board[(x, y)] = char

max_x = x
max_y = y


def draw_board(board: dict, max_x, max_y):
    for x in range(max_x + 1):
        line = ""
        for y in range(max_y + 1):
            line += board.get((x, y), ".")
        print(line)
    print()


def walk(board, cur_pos, inst):
    if inst == ">":
        nx, ny = cur_pos[0], cur_pos[1] + 1
        if (nx, ny) not in board:
            del board[cur_pos]
            cur_pos = (nx, ny)
            board[cur_pos] = "@"
        elif board[(nx, ny)] == "O":
            can_move = False
            to_move = [cur_pos, (nx, ny)]
            for ny in range(cur_pos[1] + 2, max_y + 1):
                if board.get((nx, ny)) == "O":
                    to_move.append((nx, ny))
                elif (nx, ny) not in board:
                    can_move = True
                    break
                else:
                    break
            if can_move:
                for prevp in to_move[::-1]:
                    nextp = prevp[0], prevp[1] + 1
                    board[nextp] = board[prevp]
                    del board[prevp]
                cur_pos = nextp

    elif inst == "<":
        nx, ny = cur_pos[0], cur_pos[1] - 1
        if (nx, ny) not in board:
            del board[cur_pos]
            cur_pos = (nx, ny)
            board[cur_pos] = "@"
        elif board[(nx, ny)] == "O":
            can_move = False
            to_move = [cur_pos, (nx, ny)]
            for ny in range(cur_pos[1] - 2, -1, -1):
                if board.get((nx, ny)) == "O":
                    to_move.append((nx, ny))
                elif (nx, ny) not in board:
                    can_move = True
                    break
                else:
                    break
            if can_move:
                for prevp in to_move[::-1]:
                    nextp = prevp[0], prevp[1] - 1
                    board[nextp] = board[prevp]
                    del board[prevp]
                cur_pos = nextp

    elif inst == "^":
        nx, ny = cur_pos[0] - 1, cur_pos[1]
        if (nx, ny) not in board:
            del board[cur_pos]
            cur_pos = (nx, ny)
            board[cur_pos] = "@"
        elif board[(nx, ny)] == "O":
            can_move = False
            to_move = [cur_pos, (nx, ny)]
            for nx in range(cur_pos[0] - 2, -1, -1):
                if board.get((nx, ny)) == "O":
                    to_move.append((nx, ny))
                elif (nx, ny) not in board:
                    can_move = True
                    break
                else:
                    break
            if can_move:
                for prevp in to_move[::-1]:
                    nextp = prevp[0] - 1, prevp[1]
                    board[nextp] = board[prevp]
                    del board[prevp]
                cur_pos = nextp

    elif inst == "v":
        nx, ny = cur_pos[0] + 1, cur_pos[1]
        if (nx, ny) not in board:
            del board[cur_pos]
            cur_pos = (nx, ny)
            board[cur_pos] = "@"
        elif board[(nx, ny)] == "O":
            can_move = False
            to_move = [cur_pos, (nx, ny)]
            for nx in range(cur_pos[0] + 2, max_x + 1):
                if board.get((nx, ny)) == "O":
                    to_move.append((nx, ny))
                elif (nx, ny) not in board:
                    can_move = True
                    break
                else:
                    break
            if can_move:
                for prevp in to_move[::-1]:
                    nextp = prevp[0] + 1, prevp[1]
                    board[nextp] = board[prevp]
                    del board[prevp]
                cur_pos = nextp

    return board, cur_pos


for inst in insts:
    board, cur_pos = walk(board, cur_pos, inst)
    # draw_board(board, max_x, max_y)

ans1 = 0
for p, ch in board.items():
    if ch == "O":
        ans1 += 100 * p[0] + p[1]

print("Part1: ", ans1)
