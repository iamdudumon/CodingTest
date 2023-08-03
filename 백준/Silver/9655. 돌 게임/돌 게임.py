# dp 이용
n = int(input())

dp = [0] * 1001  # dp[n] 은 n 개의 돌을 가지고 게임할 때 진행할 게임 횟수
dp[0] = 0
dp[1] = 1
dp[2] = 2

for idx in range(3, n + 1):
    dp[idx] = min(dp[idx - 1], dp[idx - 3]) + 1

if not dp[n] % 2 == 0:
    print("SK")
else:
    print("CY")
