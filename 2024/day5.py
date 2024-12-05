from collections import defaultdict

with open("input.txt") as file:
    rules, inp = map(str.splitlines, file.read().split("\n\n"))

rules_map = defaultdict(list)
for rule in rules:
    l, r = map(int, rule.split("|"))
    rules_map[l].append(r)


def rule_accepted(rule):
    for fnum in rule:
        for snum in rules_map[fnum]:
            if snum in rule and rule.index(fnum) > rule.index(snum):
                return False

    return True


def correct_rule(rule):
    rule_changed = False
    while not rule_accepted(rule):
        for ifnum in range(len(rule)):
            for snum in rules_map[rule[ifnum]]:
                if snum in rule and ifnum > rule.index(snum):
                    rule[ifnum], rule[rule.index(snum)] = (
                        rule[rule.index(snum)],
                        rule[ifnum],
                    )
                    rule_changed = True
                    break
            if rule_changed:
                break
        rule_changed = False

    return rule


ans1 = 0
for line in inp:
    line = [int(a) for a in line.split(",")]
    if rule_accepted(line):
        ans1 += line[len(line) // 2]

print("Part1: ", ans1)


ans2 = 0
for line in inp:
    line = [int(a) for a in line.split(",")]
    if not rule_accepted(line):
        rule = correct_rule(line)
        ans2 += rule[len(rule) // 2]

print("Part2: ", ans2)
