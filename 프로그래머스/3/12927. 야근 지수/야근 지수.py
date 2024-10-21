import heapq

def solution(n, works):
	answer = 0

	heap = []
	for w in works:
		heapq.heappush(heap, -w)

	while n:
		w = -heapq.heappop(heap)
		if len(heap) == 0:
			if n <= w:
				heapq.heappush(heap, -(w - n))
				n = 0
			break

		pre = -heap[0]
		if w != pre:
			if n < (w - pre + 1):
				heapq.heappush(heap, -(w - n))
				n = 0
                
			else:
				if pre > 1:
					heapq.heappush(heap, -(pre - 1))
				n -= (w - pre + 1)

		else:
			heapq.heappush(heap, -(w - 1))
			n -= 1

	for w in heap:
		answer += w * w

	return answer