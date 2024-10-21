import heapq

def solution(scoville, K):
	answer = 0

	heapq.heapify(scoville)

	while True:
		if scoville[0] >= K:
			break
		answer += 1
		fst = heapq.heappop(scoville)
		if len(scoville) == 0:
			answer = -1
			break
		scd = heapq.heappop(scoville)

		heapq.heappush(scoville, fst + 2 * scd)

	return answer