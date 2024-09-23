import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(100001)

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

def bfs(N, K):
	deq = deque()
	deq.append((N, 0))

	while deq:
		num, time = deq.popleft()

		if num == K:
			return visited[num]

		for i in range(3):
			next = move(num, i)
			if 0 <= next <= 100000 and visited[next] == 1000000:
				if visited[next] > time + 1:
					visited[next] = time + 1
				visited[next] = min(visited[next], time + 1)
				deq.append((next, visited[next]))

def get_cnt(K):
	result = visited[K]
	cnt = 0

	for i in [K - 1, K + 1, int(K / 2)] if K % 2 == 0 and K != 0 else [K - 1, K + 1]:
		if i < 0 or i >= 100001:
			continue
		if visited[i] == 0:
			cnt += 1
			continue
		if visited[i] == result - 1:
			cnt += get_cnt(i)
	return cnt

bfs(N, K)
print(visited[K])
cntt = get_cnt(K)
print(cntt if cntt else 1)