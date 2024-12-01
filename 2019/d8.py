with open('2019/input.txt', 'r') as file:
    input = file.readline()

layers = []    
image_size = (25,6)
for i in range(0, len(input), image_size[0]*image_size[1]):
    layers.append(input[i:i+image_size[0]*image_size[1]])

fewest_zero_layer = sorted(layers, key=lambda layer: layer.count('0'))[0]
print('Part1:', fewest_zero_layer.count('1')*fewest_zero_layer.count('2'))        

final_image_inline = ''
for i in range(len(layers[0])):
    for layer in layers:
        if layer[i] != '2':
            final_image_inline += layer[i]
            break
        
print('Part2:\n')
for i in range(0, len(final_image_inline), image_size[0]):
    print(final_image_inline[i:i+image_size[0]].replace('0',' '))