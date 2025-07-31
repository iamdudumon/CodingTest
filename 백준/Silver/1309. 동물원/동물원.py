import copy

N = int(input())

dp = [1, 1, 1]

for i in range(1, N):
    pre_dp = copy.deepcopy(dp)
    dp[0] = pre_dp[1] + pre_dp[2]
    dp[1] = pre_dp[0] + pre_dp[2]
    dp[2] = pre_dp[0] + pre_dp[1] + pre_dp[2]

print(sum(dp) % 9901)