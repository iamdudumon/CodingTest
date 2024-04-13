from sys import stdin, stdout

input = stdin.readline
write = stdout.write

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = nums[1]

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + nums[i]
for _ in range(m):
    i, j = map(int, input().split())
    write(str(dp[j] - dp[i - 1]) + '\n') 