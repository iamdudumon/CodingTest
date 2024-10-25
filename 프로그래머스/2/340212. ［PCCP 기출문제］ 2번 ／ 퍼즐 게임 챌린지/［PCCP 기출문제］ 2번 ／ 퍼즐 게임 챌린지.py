def solve_puzzle(level, diffs, times, limit):
	time_prev = 0

	for i in range(len(diffs)):
		if limit <= 0:
			break

		if level >= diffs[i]:
			limit -= times[i]
		else :
			diff = diffs[i] - level
			limit -= diff * (time_prev + times[i]) + times[i]
		time_prev = times[i]

	return limit

def binary_search(low, high, diffs, times, limit):
	while low <= high - 1:
		mid = (low + high) // 2
		result = solve_puzzle(mid, diffs, times, limit)

		if result == 0:
			return mid
		elif result < 0:
			low = mid + 1
		else:
			high = mid
	return low


def solution(diffs, times, limit):
	low, high = min(diffs), max(diffs)
	return binary_search(low, high, diffs, times, limit)
