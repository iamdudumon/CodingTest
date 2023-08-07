import sys
from collections import deque


def bfs(start):
    deq = deque()
    deq.append(start)
    graph[start[0]][start[1]] = 0

    while deq:
        position = deq.popleft()
        for mv in move:  
            ap = (position[0] + mv[0], position[1] + mv[1])
            if ap[0] >= n or ap[1] >= m or ap[0] < 0 or ap[1] < 0 or ap not in not_visited or graph[ap[0]][ap[1]] == 0:
                continue

            # temp = []
            # for mvo in move:
            #     tp = [ap[0] + mvo[0], ap[1] + mvo[1]]
            #     print(tp)
            #     if tp[0] >= n or tp[1] >= m or tp[0] < 0 or tp[1] < 0:
            #         temp.append(1000000)
            #     else:
            #         temp.append(graph[tp[0]][tp[1]])

            graph[ap[0]][ap[1]] = graph[position[0]][position[1]] + 1
            not_visited.remove(ap)
            deq.append(ap)

                

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
move = ((1, 0), (-1, 0), (0, 1), (0, -1))

not_visited = set()
start = [0, 0]

for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
    for j in range(m):
        if line[j] == 2:
            start = (i , j)
        
        not_visited.add((i, j))

bfs(start)

for item in not_visited:
    if not item == start and not graph[item[0]][item[1]] == 0:
        graph[item[0]][item[1]] = -1

for i in range(n):
    print(*graph[i])