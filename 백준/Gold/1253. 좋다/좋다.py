import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

def binary_search(array, key, excp):
	start, end = 0, N - 1

	while start <= end:
		mid = (start + end) // 2

		if array[mid] < key:
			start = mid + 1
		elif array[mid] > key:
			end = mid - 1
		else:
			if mid in excp:
				if ((mid -1 >= 0 and mid - 1 not in excp) and array[mid - 1] == key) or \
					((mid + 1 < N and mid + 1 not in excp) and array[mid + 1] == key):
					return True
				else:
					return False

			return True
		
	return False

cnt = 0
for i in range(N):
	for ii in range(N):
		if i == ii:
			continue
		if binary_search(numbers, numbers[i] - numbers[ii], [ii, i]):
			cnt+=1
			break

print(cnt)