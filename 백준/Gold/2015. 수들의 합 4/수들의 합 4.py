import sys

input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0
sum = list(map(int, input().split()))
sum_map = dict()

for i in range(N):
	sum[i] += sum[i - 1] if i > 0 else 0
	if (sum[i] == K):
		cnt += 1

for i in range(N):
	if sum[i] - K in sum_map:
		cnt += sum_map[sum[i] - K]

	if sum[i] in sum_map:
		sum_map[sum[i]] += 1
	else:
		sum_map[sum[i]] = 1

print(cnt)