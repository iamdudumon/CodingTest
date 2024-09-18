from collections import deque

T = int(input())

for test_case in range(1, T + 1):
	N = int(input())
	grade_list = list(map(int, input().split()))
	grade_set = set()

	possible_sum = set()
	possible_sum.add(0)

	for grade in grade_list:
		temp = set()
		for sum in possible_sum:
			temp.add(sum + grade)
		possible_sum.update(temp)
	print(f"#{test_case} {len(possible_sum)}")
