import sys

input = sys.stdin.readline

str1, str2 = input().rstrip(), input().rstrip()
len1, len2 = len(str1), len(str2)
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
	for ii in range(1, len2 + 1):
		if str1[i - 1] == str2[ii - 1]:
			dp[i][ii] = dp[i - 1][ii - 1] + 1
		else:
			dp[i][ii] = max(dp[i][ii - 1], dp[i - 1][ii])


i, ii = len1, len2
lcs = ""
while i and ii:
	if str1[i - 1] == str2[ii - 1]:
		i -= 1
		ii -= 1
		lcs += str1[i]
	else :
		if dp[i - 1][ii] < dp[i][ii - 1]:
			ii -= 1
		else:
			i -= 1

print(dp[-1][-1])
print(lcs[::-1])
