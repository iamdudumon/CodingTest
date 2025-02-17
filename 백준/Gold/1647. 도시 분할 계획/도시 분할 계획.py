import sys
import heapq

input = sys.stdin.readline

def find(set, x):
	if set[x] != x:
		set[x] = find(set, set[x])
	return set[x]

def union(set, x, y):
	x, y = find(set, x), find(set, y)
	set[max(x, y)] = min(x, y)

N, M = map(int, input().split())
root = [i for i in range(N + 1)]
heap = []
for _ in range(M):
	a, b, c = map(int, input().split())
	heapq.heappush(heap, (c, (a, b)))

cnt = 0
cost = 0
while cnt < N - 2:
	c, (a, b) = heapq.heappop(heap)
	if find(root, a) != find(root, b):
		union(root, a, b)
		cost += c
		cnt += 1

print(cost)