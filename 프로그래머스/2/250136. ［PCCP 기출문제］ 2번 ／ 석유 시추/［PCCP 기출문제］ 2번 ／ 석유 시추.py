from collections import deque

def solution(land):
	n, m = len(land), len(land[0])
	answer = [0] * m

	def bfs(st):
		if land[st[0]][st[1]] == 0:
			return

		deq = deque()
		deq.append(st)
		visited = set()
		cnt = 0

		while deq:
			pos = deq.popleft()
			if land[pos[0]][pos[1]] == 0:
				continue 
			land[pos[0]][pos[1]] = 0
			visited.add(pos[1])
			cnt += 1

			for mv in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
				nxt = (pos[0] + mv[0], pos[1] + mv[1])
				if 0 <= nxt[0] < n and 0 <= nxt[1] < m and land[nxt[0]][nxt[1]] == 1:
					deq.append(nxt)

		for col in visited:
				answer[col] += cnt

	for i in range(n):
		for ii in range(m):
			bfs((i, ii))
	
	return max(answer) 