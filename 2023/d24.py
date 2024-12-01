from itertools import combinations

def matrix_minor(m, i, j):
	return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

def matrix_det(m):
	if len(m) == 2:
		return m[0][0] * m[1][1] - m[0][1] * m[1][0]

	determinant = 0
	for c in range(len(m)):
		determinant += ((-1)**c) * m[0][c] * matrix_det(matrix_minor(m, 0, c))

	return determinant

# Adapted from: https://stackoverflow.com/a/20677983/3889449
def intersection_2d_forward(a, va, b, vb):
	a1 = (a[0] + va[0], a[1] + va[1])
	b1 = (b[0] + vb[0], b[1] + vb[1])
	dx = (a[0] - a1[0], b[0] - b1[0])
	dy = (a[1] - a1[1], b[1] - b1[1])

	div = matrix_det((dx, dy))
	if div == 0:
		return None, None

	d = (matrix_det((a, a1)), matrix_det((b, b1)))

	x = matrix_det((d, dx)) / div
	if (x > a[0]) != (va[0] > 0) or (x > b[0]) != (vb[0] > 0):
		return None, None

	y = matrix_det((d, dy)) / div
	if (y > a[1]) != (va[1] > 0) or (y > b[1]) != (vb[1] > 0):
		return None, None

	return x, y





with open('input.txt','r') as file:
	fin = file.read().splitlines()

hailstones = []
total = 0

for line in fin:
    p, v = line.split('@')
    p = tuple(map(int, p.split(',')))
    v = tuple(map(int, v.split(',')))
    hailstones.append((p, v))

for a, b in combinations(hailstones, 2):
	x, y = intersection_2d_forward(*a, *b)
	if x is None:
		continue

	xok = 200000000000000 <= x <= 400000000000000
	yok = 200000000000000 <= y <= 400000000000000
	total += xok and yok

print('Part 1:', total)
