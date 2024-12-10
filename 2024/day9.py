with open("input.txt") as file:
    inp = file.readline()

blocks1 = []
blocks2 = []

for i in range(len(inp)):
    if i % 2 == 0:
        block_id = i // 2
        blocks2.append((int(block_id), int(inp[i])))
        for _ in range(int(inp[i])):
            blocks1.append(block_id)
    else:
        if int(inp[i]) != 0:
            blocks2.append((".", int(inp[i])))
        for _ in range(int(inp[i])):
            blocks1.append(".")


def move_block(blocks: list):
    new_blocks = blocks.copy()
    first_empty_block = blocks.index(".")
    for i in range(len(blocks) - 1, -1, -1):
        if blocks[i] != ".":
            to_move_id = blocks[i]
            new_blocks[i] = "."
            break

    new_blocks[first_empty_block] = to_move_id
    return new_blocks


def part1(blocks):
    nblocks = blocks.copy()
    empty_blocks = blocks.count(".")
    for _ in range(empty_blocks):
        nblocks = move_block(nblocks)

    ans1 = 0
    for i in range(len(blocks) - empty_blocks):
        ans1 += i * int(nblocks[i])

    print("Part1: ", ans1)


def join_two_empties(blocks: list):
    next_blocks = blocks.copy()
    for i in range(len(blocks) - 1):
        if blocks[i][0] == blocks[i + 1][0] == ".":
            next_blocks[i] = (".", blocks[i][1] + blocks[i + 1][1])
            del next_blocks[i + 1]
            return next_blocks
    return next_blocks


def part2(blocks: list):
    last_block = blocks[-1][0]

    while last_block != 0:
        for index, (id, _) in enumerate(blocks):
            if id == last_block:
                blockind = index

        new_block = blocks.copy()
        if blocks[blockind][0] != ".":
            for empind in range(len(blocks)):
                if (
                    blocks[empind][0] == "."
                    and blocks[blockind][1] * len(str(blocks[blockind][0])) <= blocks[empind][1]
                    and empind < blockind
                ):
                    new_block[empind], new_block[blockind] = (
                        new_block[blockind],
                        new_block[empind],
                    )

                    if (diff := blocks[empind][1] - blocks[blockind][1] * len(str(blocks[blockind][0]))) != 0:
                        new_block.insert(empind + 1, (".", diff))
                        new_block[blockind + 1] = (
                            ".",
                            new_block[blockind + 1][1] - diff,
                        )

                    while new_block != join_two_empties(new_block):
                        new_block = join_two_empties(new_block)

                    blocks = new_block
                    break

        last_block -= 1

    blocks_str = []
    for block in blocks:
        for _ in range(block[1]):
            blocks_str.append(str(block[0]))

    print("".join(blocks_str))
    ans2 = 0
    for i in range(len(blocks_str)):
        if blocks_str[i] != ".":
            ans2 += i * int(blocks_str[i])

    print("Part2: ", ans2)


part1(blocks1)
part2(blocks2)
