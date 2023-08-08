import sys
from collections import deque 
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
start = []
count = 0
time_dic = dict()
for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(m):
        if line[j] == 1:
            start.append((i, j))
        elif line[j] == 0:
            count += 1

deq = deque()
for item in start:
    deq.append(item)
    time_dic[item] = 0
answer = 0

while deq:
    pos = deq.popleft()
    for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        a_pos = (pos[0] + move[0], pos[1] + move[1])
        if a_pos[0] >= n or a_pos[0] < 0 or a_pos[1] >= m or a_pos[1] < 0:
            continue
        if graph[a_pos[0]][a_pos[1]] == -1 or graph[a_pos[0]][a_pos[1]] == 1:
            continue
        
        graph[a_pos[0]][a_pos[1]] = 1
        deq.append(a_pos)
        
        count -= 1
        if count == 0:
            answer = time_dic[pos] + 1
            break
        else:
            time_dic[a_pos] = time_dic[pos] + 1

if count == 0:
    print(answer)
else:
    print(-1)