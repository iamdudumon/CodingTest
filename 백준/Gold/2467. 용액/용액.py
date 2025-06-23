import sys
import heapq

input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))

def binary(std, low, high, heap) :
	if low > high:
		return 

	mid = (low + high) // 2
	temp = std + solutions[mid]
	heapq.heappush(heap, (abs(temp), mid))

	if std + solutions[mid] < 0:
		binary(std, mid + 1, high, heap)
	elif std + solutions[mid] > 0:
		binary(std, low, mid - 1, heap)


min_so = 2000000001
answer = (0, 0)

for i in range(N - 1):
	heap = []
	binary(solutions[i], i + 1, N - 1, heap)

	# print(heap)
	pop = heapq.heappop(heap)
	if min_so > pop[0]:
		min_so = pop[0]
		answer = (i, pop[1])

print(solutions[answer[0]], solutions[answer[1]])