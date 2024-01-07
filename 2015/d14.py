import re

animals = []
for line in open('input'):
    v, g, r = map(int, re.findall(r'\d+', line))

    # v,g,r,passed_dist,remain_time,remain_rest,score
    animals.append([v,g,r,0,g,r,0])

def run_race(animals, time):
    for _ in range(time):
        # Part1:
        for animal in animals:
            v,g,r,dist,rem_time,rem_rest,score = animal
            if rem_time != 0 and rem_rest != 0:
                dist += v
                rem_time -= 1
            elif rem_time == 0 and rem_rest != 0:
                rem_rest -=1
            elif rem_rest == 0:
                rem_time = g-1
                rem_rest = r
                dist += v

            animal[:] = [v,g,r,dist,rem_time,rem_rest,score]

        # Part2:
        max_dist = max([a[3] for a in animals])
        for animal in animals:
            animal[-1] += 1 if animal[3] == max_dist else 0

duration = 2503
run_race(animals, duration)
print('Part1:', max([a[3] for a in animals]))
print('Part2:', max([a[-1] for a in animals]))