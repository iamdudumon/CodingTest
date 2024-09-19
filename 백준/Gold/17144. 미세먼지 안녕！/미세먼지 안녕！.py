import sys
import copy

input = sys.stdin.readline

mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def spread(r, c, temp, matrix):
	cnt = 0
	for m in mv:
		next = (r + m[0], c + m[1])
		if 0 <= next[0] < R and 0 <= next[1] < C and next not in air_clean:
			temp[next[0]][next[1]] += matrix[r][c] // 5
			cnt += 1

	matrix[r][c] -= cnt * (matrix[r][c] // 5)

def add_matrix(mat1, mat2, R, C):
	for r in range(R):
		for c in range(C):
			mat1[r][c] += mat2[r][c]

def spread_dust(matrix, R, C):
	temp = [[0] * C for _ in range(R)]

	for r in range(R):
		for c in range(C):
			if matrix[r][c] <= 0:
				continue
			spread(r, c, temp, matrix)

	add_matrix(matrix, temp ,R, C)

def make_air_clean_dir(n):
	dir = []
	if n == 1:
		for _ in range(C - 1):
			dir.append((0, 1))
		for _ in range(air_clean[0][0]):
			dir.append((-1, 0))
		for _ in range(C - 1):
			dir.append((0, -1))
		for _ in range(air_clean[0][0]):
			dir.append((1, 0))
	if n == 2:
		for _ in range(C - 1):
			dir.append((0, 1))
		for _ in range(R - air_clean[1][0] - 1):
			dir.append((1, 0))
		for _ in range(C - 1):
			dir.append((0, -1))
		for _ in range(R - air_clean[1][0] - 1):
			dir.append((-1, 0))
	return dir

def exec_air_clean(n):
	dir = make_air_clean_dir(n)
	temp = copy.deepcopy(matrix)
	r, c = air_clean[n - 1]
    
	for i, m in enumerate(dir):
		r, c = (r + m[0], c + m[1])

		next = (r + dir[i + 1][0], c + dir[i + 1][1])
		if next == air_clean[n - 1]:
			break
		matrix[next[0]][next[1]] = temp[r][c]
	matrix[air_clean[n - 1][0]][air_clean[n - 2][1] + 1] = 0


R, C, T = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

air_clean = []

for r in range(R):
	for c in range(C):
		if matrix[r][c] == -1:
			air_clean.append((r,c))

for _ in range(T):
	spread_dust(matrix, R, C)

	exec_air_clean(1)
	exec_air_clean(2)

sum = 0
for r in range(R):
	for c in range(C):
		if matrix[r][c] > 0:
			sum += matrix[r][c]
print(sum)