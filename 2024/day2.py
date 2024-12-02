with open("input.txt") as file:
    inp = [list(map(int, a.strip().split())) for a in file.readlines()]


def issafe(report: list):
    if not (sorted(report) == report or sorted(report, reverse=True) == report):
        return False

    for i in range(1, len(report)):
        if not (0 < abs(report[i] - report[i - 1]) <= 3):
            return False

    return True


def get_all_pot_reports(report: list):
    acc_reports = [report.copy() for _ in range(len(report))]
    for i in range(len(acc_reports)):
        del acc_reports[i][i]

    return acc_reports


ans1 = 0
ans2 = 0
for line in inp:
    if issafe(line):
        ans1 += 1
        ans2 += 1
    else:
        if any([issafe(report) for report in get_all_pot_reports(line)]):
            ans2 += 1

print("Part1: ", ans1)
print("Part2: ", ans2)
