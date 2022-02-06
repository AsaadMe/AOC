cor_count_p1 = 0
cor_count_p2 = 0
for passw in range(278384,824796):
    passw = str(passw)
    if sorted(passw) == list(passw):
        for d in range(10):
            d = str(d)
            if passw.count(d) >= 2:
                cor_count_p1 += 1
                break

for passw in range(278384,824796):
    passw = str(passw)
    if sorted(passw) == list(passw):
        for d in range(10):
            d = str(d)
            if passw.count(d) == 2:
                cor_count_p2 += 1
                break
                        
print('Part1:', cor_count_p1)
print('Part2:', cor_count_p2)