import sys

input = sys.stdin.readline

N, K = map(int, input().split())

items = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, K + 1):  # 배낭 무게
    for ii in range(1, N + 1): # item 순서
        W, V = items[ii - 1]    # 물건의 무게, 가치
        if W > i:
            dp[ii][i] = dp[ii - 1][i]
            continue
        dp[ii][i] = max(dp[ii - 1][i], V + dp[ii - 1][i - W])

print(dp[N][K])