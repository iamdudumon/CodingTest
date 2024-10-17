import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int,  input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]

def dfs(pos):
	if dp[pos[0]][pos[1]] != -1:
		return dp[pos[0]][pos[1]]

	if pos == (N - 1, M - 1):
		return 1

	sum = 0
	for m in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
		next = (pos[0] + m[0], pos[1] + m[1])
		if 0 <= next[0] < N and 0 <= next[1] < M:
			if matrix[next[0]][next[1]] >= matrix[pos[0]][pos[1]]:
				continue
			
			sum += dfs(next)
	dp[pos[0]][pos[1]] = sum
	return dp[pos[0]][pos[1]]

print(dfs((0, 0)))