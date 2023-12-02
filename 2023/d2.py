import math
import re

rule = {'red':12 , 'green':13 , 'blue':14}
impos = []
with open('input.txt','r') as file:
    for game in file:
        id = re.search(r'\b\d+(?=:)', game).group()
        groups = game.split(':')[1].split(';')
        for group in groups:
            for draw in group.strip().split(','):
                draw = draw.split()
                if int(draw[0]) > rule[draw[1]]:
                    impos.append(int(id))
                    break

ans1 = int(id)*(int(id)+1)/2 - sum(set(impos))
print("Part1: ", ans1)
            
            
ans2 = 0            
with open('input.txt','r') as file:
    for game in file:
        least_color = {'red':0 , 'green':0 , 'blue':0}
        id = re.search(r'\b\d+(?=:)', game).group()
        groups = game.split(':')[1].split(';')
        for group in groups:
            for draw in group.strip().split(','):
                draw = draw.split()
                if int(draw[0]) > least_color[draw[1]]:
                    least_color[draw[1]] = int(draw[0])
        
        ans2 += math.prod(least_color.values())
        
print('Part2: ', ans2)        