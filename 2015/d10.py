def conv(inp):
    return str(len(inp))+inp[0]

def split(inp):
  groups = []
  current_ch, current_count = inp[0], 1
  for char in inp[1:]:
    if char == current_ch:
      current_count += 1
    else:
      groups.append(current_ch * current_count)
      current_ch, current_count = char, 1
  groups.append(current_ch * current_count)
  return groups

cur_str = open('input').readline()
for _ in range(40):
    nxt_str = ''
    for group in split(cur_str):
       nxt_str += conv(group)
    cur_str = nxt_str

print('Part1:', len(cur_str))

def p2(cur_str):
    out = ''
    last_ch = cur_str[0]
    count = 1
    for c in cur_str[1:]:
        if c != last_ch:
            out += str(count) + last_ch
            last_ch = c
            count = 1
        else:
            count += 1
    out += str(count) + last_ch
    return out

cur_str = open('input').readline()
for i in range(50):
    cur_str = p2(cur_str)
    
print('Part2:', len(cur_str))