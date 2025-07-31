import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(M)]
dp = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]

deq = deque()
deq.append((0, 0))

while deq:
	pos = deq.popleft()

	for m in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
		next = (pos[0] + m[0], pos[1] + m[1])
		if (0 <= next[0] < M) and (0 <= next[1] < N) and visited[next[0]][next[1]] == 0:
			if matrix[next[0]][next[1]]:
				dp[next[0]][next[1]] = dp[pos[0]][pos[1]] + 1
				deq.append(next)
			else:
				dp[next[0]][next[1]] = dp[pos[0]][pos[1]]
				deq.appendleft(next)

			visited[next[0]][next[1]] = 1

print(dp[M - 1][N - 1])