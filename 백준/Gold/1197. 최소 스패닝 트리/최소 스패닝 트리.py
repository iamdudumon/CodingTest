import sys
import heapq
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

heap = []
V, E = map(int, input().split())
root = [i for i in range(V + 1)]

def find(x):
	if root[x] != x:
		root[x] = find(root[x])
		return root[x]
	return x

def union(x, y):
	x, y = find(x), find(y)
	root[max(x, y)] = min(x, y)

for _ in range(E):
	a, b, c = map(int, input().split())
	heapq.heappush(heap, (c, (a, b)))

cnt = 0
res = 0
while cnt < V - 1:
	c, (a, b) = heapq.heappop(heap)
	if find(a) != find(b):
		union(a, b)
		res += c
		cnt += 1

print(res)