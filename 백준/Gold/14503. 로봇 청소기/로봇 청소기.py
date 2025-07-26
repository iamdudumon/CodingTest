import sys

input = sys.stdin.readline

def move(d):
	if d == 0:
		return (-1, 0)
	if d == 1:
		return (0, 1)
	if d == 2:
		return (1, 0)
	if d == 3:
		return (0, -1)

def is_move(pos, N, M):
	if (0 <= pos[0] < N and 0 <= pos[1] < M) and \
		(matrix[pos[0]][pos[1]] == 0 or matrix[pos[0]][pos[1]] == -1):
		return True
	return False

def is_clean(pos, N, M):
	if (0 <= pos[0] < N and 0 <= pos[1] < M) and \
		(matrix[pos[0]][pos[1]] == 0):
		return True
	return False

def loop(matrix, r, c, d, N, M):
	count = 0

	while True:
		if matrix[r][c] == 0:
			count+=1
			matrix[r][c] = -1
			continue
		
		# 4칸 중 청소되지 않은 빈 칸이 있는 경우
		if matrix[r + 1][c] == 0 or matrix[r - 1][c] == 0 or \
			matrix[r][c +1] == 0 or matrix[r][c - 1] == 0:
			d = (d - 1) % 4
			m = move(d)
			front = (r + m[0], c + m[1])
			if is_clean(front, N, M):	# front가 청소 가능하냐?
				if matrix[front[0]][front[1]] == 0:
					r += m[0]
					c += m[1]

		else:   # 4칸 중 청소되지 않은 빈 칸이 없는 경우
			m = move(d)
			back = (r - m[0], c - m[1])
			if is_move(back, N, M):   # back이 이동 가능하냐?
				r -= m[0]
				c -= m[1]
			else:
				break

	return count

N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

print(loop(matrix, r, c, d, N, M))