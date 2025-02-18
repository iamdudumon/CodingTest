import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [(set(), set()) for _ in range(N + 1)] # (진입, 진출)
costs = [0 for _ in range(N + 1)]
table = [0  for _ in range(N + 1)]
for i in range(N):
	works = list(map(int, input().split()))
	costs[i + 1] = works[0]
	for n in works[2:]:
		graph[i + 1][0].add(n)	# 진입
		graph[n][1].add(i + 1)	# 진출
		table[i + 1] += 1

dp = [0  for _ in range(N + 1)]
que = deque()
for i in range(1, len(table)):
	if table[i] == 0:
		que.append(i)

dp = [0  for _ in range(N + 1)]
while que:
	node = que.popleft()
	for n in graph[node][1]:
		table[n] -= 1
		dp[n] = max(dp[n], dp[node] + costs[node])
		if table[n] == 0:
			que.append(n)

res = 0
for i in range(1, N + 1):
	res = max(res, dp[i] + costs[i])
print(res)
