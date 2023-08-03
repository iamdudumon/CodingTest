import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def bfs(origin, wall):
    origin_copy = copy.deepcopy(origin)     # 깊은 복사
    for item in wall:       # 3개의 벽 설치
        temp = save[item]
        origin_copy[temp[0]][temp[1]] = 1
    
    count = 0
    for virus_position in virus:    # 각 바이러스 위치에서 시작
        deq = deque()
        deq.append(virus_position)

        while deq:
            position = deq.popleft()
            for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:     # 상하, 좌우
                add_position = [position[0] + move[0], position[1] + move[1]] # 움직인 위치
        
                if add_position[0] < n and add_position[0] > -1 and add_position[1] < m and add_position[1] > -1:   # 움직인 위치가 규격을 벗어나면  X
                    value = origin_copy[add_position[0]][add_position[1]]
                    if value == 0:    # save area
                        origin_copy[add_position[0]][add_position[1]] = 2 
                        deq.append(add_position)
                        count += 1
                        if count >= min_count:      # 최소값을 넘기면 굳이 더 진행 안 하고 return
                            return count
                else:   # 범위를 벗어나면 다음 방향으로 이동
                    continue

    return count



n, m = map(int, input().split())

graph = []
save = []
virus = []
min_count = n * m

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 0:
            save.append([i, j])
        elif line[j] == 2:
            virus.append([i, j])
    graph.append(line)

wall = list(combinations([i for i in range(len(save))], 3))

for item in wall:           # 벽의 조합 수만큼 반복
    count = bfs(graph, item)
    if min_count > count:
        min_count = count

print(len(save) - (3 + min_count))  # 원래 세이프 공간 - (설치학 벽 3개 + 추가적으로 퍼진 바이러스 수)
