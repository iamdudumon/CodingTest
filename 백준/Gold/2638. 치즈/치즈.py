import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().split()) for _ in range(N)]

chizees = set()

for r in range(N):
	for c in range(M):
		if matrix[r][c] == "1":
			chizees.add((r, c))

def is_space(r, c, visited):
	visited.add((r, c))
	for m in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
		next = (r + m[0], c + m[1])
		if next in visited:
			continue
		if not (0 <= next[0] < N) or not (0 <= next[1] < M):
			return True
		if matrix[next[0]][next[1]] == "0":
			if is_space(next[0], next[1], visited):
				return True
	return False

def is_melt(r, c):
	cnt = 0
	for m in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
		next = (r + m[0], c + m[1])
		if 0 <= next[0] < N and 0 <= next[1] < M and matrix[next[0]][next[1]] == "0":
			if is_space(next[0], next[1], set()):
				cnt += 1
               
	return cnt >= 2

cnt = 0
while True:
	temp = []
	for chizee in chizees:   
		if is_melt(chizee[0], chizee[1]):
			temp.append(chizee)
			
	for t in temp:
		chizees.remove(t)
		matrix[t[0]][t[1]] = "0"
	cnt += 1
	
	if len(chizees) == 0:
		break 
print(cnt)