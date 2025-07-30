import sys

input = sys.stdin.readline

n = int(input())
podos = [int(input()) for _ in range(n)]
dp = [0] * n

dp[0] = podos[0]
if n >= 2:
    dp[1] = podos[0] + podos[1] 
if n >= 3:
    dp[2] = max(podos[2] + podos[0], podos[2] + podos[1], podos[0] + podos[1])

if n >= 4:
    for i in range(3, n):
        dp[i] = max(podos[i] + dp[i - 2], \
                    podos[i] + podos[i - 1] + dp[i - 3], \
                    podos[i - 1] + podos[i - 2] + dp[i - 4] if i >= 4 else 0)

print(max(dp))
