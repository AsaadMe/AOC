### NOT COMPLETE ###

with open('2019/inputtest.txt', 'r') as file:
    data = []
    for line in file:
        left, right = line.split('=>')
        left = map(str.strip, left.split(','))
        right = map(str.strip, right.split(','))
        data.append(())