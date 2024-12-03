import re


def part1(inp):
    insts = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp)

    ans1 = 0
    for inst in insts:
        ans1 += int(inst[0]) * int(inst[1])

    print("Part1: ", ans1)


def part2_just_for_convenient(inp):
    ans2 = 0
    subcom = ""
    fnum, snum = "", ""
    do_flag = True
    while inp:
        char = inp[0]
        inp = inp[1:]
        if char == "m" and subcom == "":
            subcom += "m"
        elif char == "u" and subcom == "m":
            subcom += "u"
        elif char == "l" and subcom == "mu":
            subcom += "l"
        elif char == "(" and subcom == "mul":
            subcom += "("
        elif char.isnumeric() and subcom == "mul(":
            fnum += char
        elif char == "," and subcom == "mul(":
            subcom += ","
        elif char.isnumeric() and subcom == "mul(,":
            snum += char
        elif char == ")" and subcom == "mul(," and do_flag:
            ans2 += int(fnum) * int(snum)
            fnum, snum = "", ""
            subcom = ""

        elif char == "d" and subcom == "":
            subcom += "d"
        elif char == "o" and subcom == "d":
            subcom += "o"
        elif char == "(" and subcom == "do":
            subcom += "("
        elif char == ")" and subcom == "do(":
            do_flag = True
            subcom = ""

        elif char == "d" and subcom == "":
            subcom += "d"
        elif char == "o" and subcom == "d":
            subcom += "o"
        elif char == "n" and subcom == "do":
            subcom += "n"
        elif char == "'" and subcom == "don":
            subcom += "'"
        elif char == "t" and subcom == "don'":
            subcom += "t"
        elif char == "(" and subcom == "don't":
            subcom += "("
        elif char == ")" and subcom == "don't(":
            do_flag = False
            subcom = ""

        else:
            subcom = ""
            fnum, snum = "", ""

    print("Part2 (convenient): ", ans2)


def part2(inp):
    ans2 = 0
    do_flag = True
    insts = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", inp)
    for inst in insts:
        if inst == "do()":
            do_flag = True
        elif inst == "don't()":
            do_flag = False
        elif do_flag:
            fnum, snum = map(
                int, inst.removeprefix("mul(").removesuffix(")").split(",")
            )
            ans2 += fnum * snum

    print("Part2: ", ans2)


with open("input.txt") as file:
    inp = file.read().strip()

part1(inp)
# part2_just_for_convenient(inp)
part2(inp)
