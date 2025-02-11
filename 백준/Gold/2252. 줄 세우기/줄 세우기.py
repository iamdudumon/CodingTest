import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [(set(), set()) for _ in range(N)]
for _ in range(M):
	a, b = map(int, input().split())
	graph[a - 1][0].add(b - 1)	# 진출
	graph[b - 1][1].add(a - 1)	# 진입
table = [len(graph[i][1]) for i in range(N)]
que = deque()

for i in range(len(table)):
	if table[i] == 0:
		que.appendleft(i)

while que:
	node = que.pop()
	for v in graph[node][0]:
		table[v] -= 1
		if table[v] == 0:
			que.appendleft(v)
	print(node + 1, end=" ")
