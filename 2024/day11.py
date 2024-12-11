from functools import cache

with open("input.txt") as file:
    inp = file.readline()

stones = list(map(int, inp.split()))


def part1(stones):
    blinks = 25

    for _ in range(blinks):
        next_stones = []
        for stone in stones:
            if stone == 0:
                next_stones.append(1)
            elif (l := len(str(stone))) % 2 == 0:
                mid = l // 2
                next_stones.append(int(str(stone)[:mid]))
                next_stones.append(int(str(stone)[mid:]))
            else:
                next_stones.append(stone * 2024)

        stones = next_stones

    print("Part1: ", len(stones))


def part2(stones):
    @cache
    def get_len(stone, blink):
        if blink == 0:
            return 1
        if stone == 0:
            return get_len(1, blink - 1)

        if len(str(stone)) % 2 != 0:
            return get_len(stone * 2024, blink - 1)

        else:
            mid = len(str(stone)) // 2
            return get_len(int(str(stone)[:mid]), blink - 1) + get_len(
                int(str(stone)[mid:]), blink - 1
            )

    print("Part2: ", sum([get_len(stone, 75) for stone in stones]))


part1(stones)
part2(stones)
