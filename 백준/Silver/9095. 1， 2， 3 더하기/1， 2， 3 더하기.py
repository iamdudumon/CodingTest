from sys import stdin, stdout

input = stdin.readline
print = stdout.write

t = int(input())                                                                       
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

# n=4 -> 4-3 4-3 4-1
max_n = 0
for _ in range(t):
    n = int(input())
    if max_n > n:
        print(str(dp[n]) + "\n")
        continue
    max_n = n
    for i in range(4, n + 1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(str(dp[n]) + "\n")