import sys
import heapq

input = sys.stdin.readline

heap = []
answer = 0
N = int(input())
for _ in range(N):
	heapq.heappush(heap, int(input()))

while heap:
	n1 = heapq.heappop(heap)
	if not heap:
		break
	n2 = heapq.heappop(heap)
	answer += (n1 + n2)
	heapq.heappush(heap, n1 + n2)

print(answer)