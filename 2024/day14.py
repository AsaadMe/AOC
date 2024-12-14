from collections import Counter
from math import prod

import numpy as np
from PIL import Image

max_x = 101
max_y = 103

robots = []
for line in open("input.txt"):
    p, v = [a[2:].split(",") for a in line.strip().split()]

    robots.append((tuple([int(a) for a in p]), tuple([int(a) for a in v])))


def walk(robot):
    cur_pos, velo = robot
    next_pos = (cur_pos[0] + velo[0]) % max_x, (cur_pos[1] + velo[1]) % max_y

    return next_pos, velo


def part1(robots):
    seconds = 100
    for robot_ind in range(len(robots)):
        for _ in range(seconds):
            robots[robot_ind] = walk(robots[robot_ind])

    c = Counter([p for p, _ in robots])
    quadrants = [0, 0, 0, 0]
    for p, val in c.items():
        if p[0] < max_x // 2 and p[1] < max_y // 2:
            quadrants[0] += val
        elif p[0] < max_x // 2 and p[1] > max_y // 2:
            quadrants[1] += val
        elif p[0] > max_x // 2 and p[1] < max_y // 2:
            quadrants[2] += val
        elif p[0] > max_x // 2 and p[1] > max_y // 2:
            quadrants[3] += val

    print("Part1: ", prod(quadrants))


def part2(robots):
    seconds = 10000
    for sec in range(seconds):
        plot = np.zeros((max_y, max_x), dtype=np.uint8)
        for robot_ind in range(len(robots)):
            robots[robot_ind] = walk(robots[robot_ind])

        for (y, x), _ in robots:
            plot[x, y] = 255

        image = Image.fromarray(plot, mode="L")
        image.save(f"images/output_{sec}.jpg")


part1(robots.copy())
part2(robots.copy())  # manually checking the images
