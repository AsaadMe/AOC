import json

data = json.load(open('input'))

def flatten(data):
    sumnums1, sumnums2 = 0,0
    for d in data:
        if isinstance(d, list):
            s1,s2 = flatten(d)
            sumnums1 += s1
            sumnums2 += s2
        elif isinstance(d, dict):
            if 'red' not in d.values():
                sumnums2 += flatten(d.values())[1]
            sumnums1 += flatten(d.values())[0]
        elif isinstance(d, int):
            sumnums1 += d
            sumnums2 += d
    return sumnums1, sumnums2

print('(Part1, Part2):', flatten(data))