import sys

input = sys.stdin.readline

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

dp = tri.copy()

for i in range(1, n):
    pre_len = tri[i - 1] # == i
    for j in range(len(tri[i])):
        if j == 0:
            dp[i][j] +=  dp[i - 1][j]
        elif j == i:
            dp[i][j] +=  dp[i - 1][j - 1]
        else:
            dp[i][j] +=  max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n - 1]))