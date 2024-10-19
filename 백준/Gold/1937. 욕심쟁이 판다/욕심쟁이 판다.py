import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]

def dfs(pos):
	if dp[pos[0]][pos[1]] != -1:
		return dp[pos[0]][pos[1]]

	way = 0
	for m in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		nxt = (pos[0] + m[0], pos[1] + m[1])
		if 0 <= nxt[0] < N and 0 <= nxt[1] < N:
			if matrix[nxt[0]][nxt[1]] <= matrix[pos[0]][pos[1]]:
				continue
			
			way = max(way, dfs(nxt))
			dp[pos[0]][pos[1]] = way
	
	dp[pos[0]][pos[1]] += 1
	return dp[pos[0]][pos[1]]

for i in range(N):
	for ii in range(N):
		dfs((i, ii))

print(max(map(max, dp)) + 1)