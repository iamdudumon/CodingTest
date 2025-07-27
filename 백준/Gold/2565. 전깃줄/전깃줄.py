import sys

N = int(input())
lines = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
dp = [1] * N

for i in range(1, len(lines)):
	for ii in range(i):
		if lines[i][1] > lines[ii][1]:
			dp[i] = max(dp[i], dp[ii] + 1)

print(N - max(dp))