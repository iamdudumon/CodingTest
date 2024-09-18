T = int(input())

mv = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(pos, num):
	row, col = pos

	if len(num) == 7:
		numbers.add(num)
		return

	global mv
	for m in mv:
		next = (row + m[0], col + m[1])
		if 0 <= next[0] < 4 and 0 <= next[1] < 4:
			dfs(next, num + graph[row][col])



for test_case in range(1, T + 1):
	graph = [ list(input().split()) for _ in range(4)]
	numbers = set()

	for row in range(4):
		for col in range(4):
			dfs((row, col), "")
	print(f"#{test_case} {len(numbers)}")
