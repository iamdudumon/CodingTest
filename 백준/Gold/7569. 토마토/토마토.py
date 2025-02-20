import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
mv = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

tomato_cnt = 0
tomatos = []
not_tomato_cnt = 0

for i in range(H):
	for ii in range(N):
		for iii in range(M):
			if matrix[i][ii][iii] == 1:
				tomatos.append((i, ii, iii))
				tomato_cnt += 1
			if matrix[i][ii][iii] == -1:
				not_tomato_cnt += 1

next_tomatos = []
answer = 0
while tomato_cnt < M * N * H - not_tomato_cnt:
	for tomato in tomatos:
		for m in mv:
			next = (tomato[0] + m[0], tomato[1] + m[1], tomato[2] + m[2])
			if 0 <= next[0] < H and 0 <= next[1] < N and 0 <= next[2] < M:
				if matrix[next[0]][next[1]][next[2]] == 0:
					tomato_cnt += 1
					matrix[next[0]][next[1]][next[2]] = 1
					next_tomatos.append(next)
	answer += 1
	tomatos.clear()
	if not next_tomatos:
		answer = -1
		break
	tomatos = next_tomatos
	next_tomatos = []

print(answer)