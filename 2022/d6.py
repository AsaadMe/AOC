def find_ind(input, dist_chars):
    for i in range(dist_chars, len(input)):
        if len(set(input[i-dist_chars:i])) == dist_chars:
            return i

with open('2022/input.txt', 'r') as file:
    message = file.readline()
    print('Part1:', find_ind(message, 4))
    print('Part2:', find_ind(message, 14))