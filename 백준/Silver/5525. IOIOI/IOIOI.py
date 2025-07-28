import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
ioi = input()
dp = [0] * M
answer = 0

for i in range(1, M - 1):
	if ioi[i] == 'O':
		if ioi[i - 1] == 'I' and ioi[i + 1] == 'I':
			if i > 2:
				dp[i] = dp[i - 2] + 1
			else:
				dp[i] = 1

		if dp[i] >= N:
			answer+=1
print(answer)
