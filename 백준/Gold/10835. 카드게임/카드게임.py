import sys

input = sys.stdin.readline

N = int(input())
l_cards = [0] + list(map(int, input().split()))
r_cards = [0] + list(map(int, input().split()))
dp = [[-1] * (N + 1) for _ in range(N + 1)]

def solve(i, ii):
	if i > N or ii > N:
		return 0
	if dp[i][ii] != -1:
		return dp[i][ii]
	if r_cards[i] < l_cards[ii]:
		dp[i][ii] = max(solve(i + 1, ii) + r_cards[i], solve(i, ii + 1),  solve(i + 1, ii + 1))
	else:
		dp[i][ii] = max(solve(i, ii + 1), solve(i + 1, ii + 1))
	return dp[i][ii]

print(solve(0, 0))