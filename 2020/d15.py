numbers = [0,14,6,20,1,4]

def find_latest(num_list, num):
    for i in range(len(num_list)-2,-1,-1):
        if num_list[i] == num:
            return i
        
def part1():
    for step in range(2020-len(numbers)):
        print(step)
        cur_number = numbers[-1]
        if numbers.count(cur_number) == 1:
            next_number = 0
        else:
            latest_ind = find_latest(numbers, cur_number)
            next_number = len(numbers)-1 - latest_ind
            
        numbers.append(next_number)
        
    print(numbers[-1])
    
def part2():
    steps = 30000000
    last, c = numbers[-1], {n: i+1 for i, n in enumerate(numbers)}
    for i in range(len(numbers), steps):
        c[last], last = i, i - c.get(last, i)
    print(last)
    
part2()