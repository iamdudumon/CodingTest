import sys
from collections import deque

input = sys.stdin.readline

def move(pos, d):
	return (pos[0] + d[0], pos[1] + d[1])

def is_move(pos, N, matrix):
	if (0 <= pos[0] < N and 0 <= pos[1] < N) and \
		(matrix[pos[0]][pos[1]] != 1):
		return True
	return False

def curv(d, C):
	if d == (1, 0):
		if C == 'L':
			return (0, 1)
		if C == 'D':
			return (0, -1)
	if d == (-1, 0):
		if C == 'L':
			return (0, -1)
		if C == 'D':
			return (0, 1)
	if d == (0, 1):
		if C == 'L':
			return (-1, 0)
		if C == 'D':
			return (1, 0)
	if d == (0, -1):
		if C == 'L':
			return (1, 0)
		if C == 'D':
			return (-1, 0)

def loop(matrix, N, curvs):
	time = 0
	d = (0, 1)
	snake = deque()
	snake.append((0, 0))
	cc = 0

	while True:
		time +=1
		next = move(snake[-1], d)
		if not is_move(next, N, matrix):
			break
		snake.append(next)

		if matrix[snake[-1][0]][snake[-1][1]] != -1: # not 사과
			tail = snake.popleft()
			matrix[tail[0]][tail[1]] = 0
		
		matrix[snake[-1][0]][snake[-1][1]] = 1

		if cc < len(curvs) and curvs[cc][0] == time:
			d = curv(d, curvs[cc][1])
			cc+=1
			

	return time

N = int(input())
K = int(input())
matrix = [[0] * N for _ in range(N)]
for _ in range(K):
	r, c = map(int, input().split())
	matrix[r - 1][c - 1] = -1

L = int(input())
curvs = []
for _ in range(L):
	temp = input().split()
	curvs.append(tuple((int(temp[0]), temp[1])))

print(loop(matrix, N, curvs))