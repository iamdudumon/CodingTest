from collections import deque

def move(n, i):
    if i == 0:
        return n + 1
    elif i == 1:
        return n - 1
    else:
        return n * 2

def bfs(n):
    deq = deque()
    deq.append(n)
    visited[n] = 0
    if n == k:
        return visited[n]

    while deq:
        posision = deq.popleft()

        for idx in range(3):
            temp = move(posision, idx)

            if temp == k:
                return visited[posision] + 1
            if not visited.__contains__(temp) and temp >= 0 and temp <= 100000:
                deq.append(temp)
                visited[temp] = visited[posision] + 1
        

n, k = map(int, input().split())
visited = dict()
print(bfs(n))
