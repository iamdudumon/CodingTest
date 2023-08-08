import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vip = set()
for _ in range(m):
    vip.add(int(input()))

dp = [1] * 41
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, n - m + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    
size = 0
sum = 1
for i in range(n):
    if i+1 in vip:
        sum *= dp[size]
        size = 0
    elif i == n - 1:
        sum *= dp[size + 1]
    else:
        size += 1

print(sum)

