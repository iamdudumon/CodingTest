import sys
import copy

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
dp = [0] * 21
dp[numbers[0]] = 1

for i in range(1, N - 1):
	pre_dp = copy.deepcopy(dp)
	dp = [0] * 21

	for ii in range(21):
		if pre_dp[ii]:
			minus = ii - numbers[i]
			if minus >= 0:
				dp[minus]+=pre_dp[ii]

			plus = ii + numbers[i]
			if plus <= 20:
				dp[plus]+=pre_dp[ii]

print(dp[numbers[-1]])