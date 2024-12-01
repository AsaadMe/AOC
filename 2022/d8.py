import numpy as np
from math import prod

with open('2022/input.txt', 'r') as file:
    input = [list(map(int, a.strip())) for a in file.readlines()]
    arr = np.array(input)
    
    vis_trees = sum(arr.shape)*2-4
    
    for i in range(1, arr.shape[0]-1):
        for j in range(1, arr.shape[1]-1):
            if (arr[i,j] > arr[i,j+1:].max() or
                arr[i,j] > arr[i,:j].max() or
                arr[i,j] > arr[:i,j].max() or
                arr[i,j] > arr[i+1:,j].max()):
                vis_trees += 1
    
    all_trees_score = []
    arr = np.pad(arr, 1, constant_values=10)
    for i in range(1, arr.shape[0]-1):
        for j in range(1, arr.shape[1]-1):
            score = [0,0,0,0]
            for tree in arr[i,j+1:]:
                if tree == 10:
                    break
                if tree < arr[i,j]:
                    score[0] += 1
                elif tree >= arr[i,j]:
                    score[0] += 1
                    break
                
            for tree in np.flip(arr[i,:j]):
                if tree == 10:
                    break
                if tree < arr[i,j]:
                    score[1] += 1
                elif tree >= arr[i,j]:
                    score[1] += 1
                    break
            for tree in np.flip(arr[:i,j]):
                if tree == 10:
                    break
                if tree < arr[i,j]:
                    score[2] += 1
                elif tree >= arr[i,j]:
                    score[2] += 1
                    break
            for tree in arr[i+1:,j]:
                if tree == 10:
                    break
                if tree < arr[i,j]:
                    score[3] += 1
                elif tree >= arr[i,j]:
                    score[3] += 1
                    break
            all_trees_score.append(prod(score))
            
    print('Part1:', vis_trees)
    print('Part2:', max(all_trees_score))