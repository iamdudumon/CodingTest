import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [1000000] * 100001
visited[N] = 0

def move(n, i):
    if i == 0:
        return n * 2
    elif i == 1:
        return n - 1
    else:
        return n + 1

def bfs(N):
	deq = deque()
	deq.append((N, 0))

	while deq:
		num, time = deq.popleft()
		if num == K:
			return visited[num]
        
		for i in range(3):
			next = move(num, i)
			if 0 <= next <= 100000 and visited[next] == 1000000:
				if i == 0:
						visited[next] = min(visited[next], time)
						deq.appendleft((next, visited[next]))
				else:
						visited[next] = min(visited[next], time + 1)
						deq.append((next, visited[next]))

print(bfs(N))