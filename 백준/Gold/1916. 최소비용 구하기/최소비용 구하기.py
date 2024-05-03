import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().rstrip().split())
    graph[start].append((end, cost))
start, end = map(int, input().rstrip().split())
table = [1e9] * (n + 1)
table[start] = 0
heap = []
heapq.heappush(heap, [0, start])

while heap:
    cost, node = heapq.heappop(heap)
    if table[node] < cost:
        continue

    for i, c in graph[node]:
        if table[i] > cost + c:
            table[i] = cost + c
            heapq.heappush(heap, [table[i], i])

print(table[end])