import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
	N, K = map(int, input().split())
	graph = [list() for _ in range(N + 1)]
	costs = [0 for _ in range(N + 1)]
	table = [0  for _ in range(N + 1)]
	costs = [0] + list(map(int, input().split()))
	for _ in range(K):
		a, b = map(int, input().split())
		graph[a].append(b)
		table[b] += 1
	W = int(input())

	dp = [0  for _ in range(N + 1)]
	que = deque()
	for i in range(1, len(table)):
		if table[i] == 0:
			que.append(i)

	while que:
		node = que.popleft()
		for n in graph[node]:
			table[n] -= 1
			dp[n] = max(dp[n], dp[node] + costs[node])
			if table[n] == 0:
				que.append(n)

	print(dp[W] + costs[W])
