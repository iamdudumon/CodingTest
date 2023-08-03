import sys
import copy
from collections import deque

input = sys.stdin.readline

def comb(list, idx, end, n = 3):
    if len(list) == n:
        wall.append(list)
        return
    if idx == end:
        return
    else:
        comb(list, idx + 1, end)
        comb(list + [idx], idx + 1, end)

def bfs(origin, wall):
    origin_copy = copy.deepcopy(origin)
    for item in wall:
        temp = save[item]
        origin_copy[temp[0]][temp[1]] = 1
    
    count = 0
    for virus_position in virus:
        deq = deque()
        deq.append(virus_position)

        while deq:
            position = deq.popleft()
            for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                add_position = [position[0] + move[0], position[1] + move[1]]
                if add_position[0] < n and add_position[0] > -1 and add_position[1] < m and add_position[1] > -1:
                    value = origin_copy[add_position[0]][add_position[1]]
                    if value == 0:    # save area
                        origin_copy[add_position[0]][add_position[1]] = 2 
                        deq.append(add_position)
                        count += 1
                        if count > min_count:
                            return n*m
    return count

    



n, m = map(int, input().split())

graph = []
save = []
virus = []
wall = []
min_count = n * m

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 0:
            save.append([i, j])
        elif line[j] == 2:
            virus.append([i, j])
    graph.append(line)

# for idx in range(n):
#     print(*graph[idx])

comb([], 0, len(save))

for item in wall:
    count = bfs(graph, item)
    if min_count > count:
        min_count = count

print(len(save) - (3 + min_count))
