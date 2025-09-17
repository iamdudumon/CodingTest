import sys

input = sys.stdin.readline

N = int(input())
l = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
	day = l[i][0]
	if (i + day) > N:
		dp[i] = dp[i + 1]
		continue
	dp[i] = max(dp[i + 1], l[i][1] + dp[i + day])

print(dp[0])