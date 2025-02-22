import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
n1 = len(str1)
n2 = len(str2)
dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

answer = 0
for i in range(1, n1 + 1):
	for ii in range(1, n2 + 1):
		if str1[i - 1] == str2[ii - 1]:
			dp[i][ii] = dp[i - 1][ii - 1] + 1
			answer = max(answer, dp[i][ii])

print(answer)