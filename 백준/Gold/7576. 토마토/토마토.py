import sys
from collections import deque 
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
deq = deque()
count = 0
answer = 0
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(m):
        if line[j] == 1:
            deq.append((i, j))
        elif line[j] == 0:
            count += 1

while deq:
    pos = deq.popleft()
    for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        a_pos = (pos[0] + move[0], pos[1] + move[1])
        if 0 <= a_pos[0] < n and 0 <= a_pos[1] < m and graph[a_pos[0]][a_pos[1]] == 0:
            graph[a_pos[0]][a_pos[1]] = graph[pos[0]][pos[1]] + 1
            deq.append(a_pos)
            
            count -= 1
            if count == 0:
                answer = graph[a_pos[0]][a_pos[1]] - 1
                deq.clear()
                break

if count == 0:
    print(answer)
else:
    print(-1)