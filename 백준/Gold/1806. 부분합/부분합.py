import sys

input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))
answer = 100001
sum = 0

i = 0
ii = 0
for i in range(N):
	while ii < N:
		sum += array[ii]
		if sum >= S:
			answer = min(answer, ii - i + 1)
			if sum > S:
				sum -= array[ii]
			else:
				ii += 1
			break
		else :
			ii += 1
	sum -= array[i]

print(answer if answer != 100001 else 0)