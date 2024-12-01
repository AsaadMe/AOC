import re

nicecount1 = 0
nicecount2 = 0
for line in open('input'):
    line = line.strip()
    if (re.match(r'.*[aeiou].*[aeiou].*[aeiou]', line) and
        re.search(r'(.)\1', line) and
        not re.search(r'ab|cd|pq|xy', line)):
        nicecount1 += 1

    if (re.search(r'(..).*\1', line) and
        re.search(r'(.).\1', line)):
        nicecount2 += 1

print("Part1:", nicecount1)
print("Part2:", nicecount2)