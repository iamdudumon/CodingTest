import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[1] * (n + 1) for _ in range(n + 1)]

for i in range(3, n + 1):
	for ii in range(2, i):
		dp[i][ii] = dp[i - 1][ii - 1] + dp[i - 1][ii]

print(dp[n][k]) 