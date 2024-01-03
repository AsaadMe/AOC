import re

ans = 0
for line in open('input'):
    line = line.strip()
    t = line
    len1 = len(line)
    line = re.sub(r'\\x[0-9a-f]{2}', '!', line)
    line = re.sub(r'\\"', '"', line)
    line = re.sub(r'\\\\', '!', line)
    ans += len1 - (len(line) - 2)

ans2 = 0
for line in open('input'):
    line = line.strip()
    line = re.sub(r'\\', '\\\\\\\\', line)
    line = re.sub(r'"', '\\"', line)
    line = '"' + line + '"'
    ans2 += len(line)

print("Part1:", ans)
print("Part2:", ans2 - sum([len(a.strip()) for a in open('input')]))