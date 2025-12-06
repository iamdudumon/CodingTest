import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
shark = [(0, 0), 2, 0]
for i in range(N):
	for ii in range(N):
		if matrix[i][ii] == 9:
			shark[0] = (i, ii)
			matrix[i][ii] = 0

def find_close_point(shark):
	shark_pos = shark[0]
	shark_size = shark[1]
	deq = deque()
	deq.append((shark_pos, 0))
	visited = [[False] * N for _ in range(N)]
	visited[shark_pos[0]][shark_pos[1]] = True
	close_pos_lst = []
	min_d = N * N

	while deq:
		pos, d = deq.popleft()
		if min_d < d:
			continue
		if 1 <= matrix[pos[0]][pos[1]] < shark_size:
			close_pos_lst.append((pos, d))
			min_d = d
			continue

		for m in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
			nxt = (pos[0] + m[0], pos[1] + m[1])
			if nxt[0] < 0 or nxt[0] >= N or nxt[1] < 0 or nxt[1] >= N:
				continue
			if visited[nxt[0]][nxt[1]] == True:
				continue
			if matrix[nxt[0]][nxt[1]] <= shark_size:
				deq.append((nxt, d + 1))
				visited[nxt[0]][nxt[1]] = True
	if len(close_pos_lst) == 0:
		return (shark_pos, 0)
	close_pos_lst.sort(key=lambda x: (x[1], x[0][0], x[0][1]))
	return close_pos_lst[0]

answer = 0
while True:
	# print(shark)
	nxt_shark = find_close_point(shark)
	if shark[0][0] == nxt_shark[0][0] and shark[0][1] == nxt_shark[0][1]:
		break
	matrix[nxt_shark[0][0]][nxt_shark[0][1]] = 0
	shark[0] = nxt_shark[0]
	shark[2] += 1
	if shark[1] == shark[2]:
		shark[1] += 1
		shark[2] = 0
	answer += nxt_shark[1]

print(answer)