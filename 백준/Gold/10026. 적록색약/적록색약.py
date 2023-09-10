import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(pos, rgb):
    for mv in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        pos_add = (pos[0] + mv[0], pos[1] + mv[1])
        if pos_add[0] >= n or pos_add[0] < 0 or pos_add[1] >= n or pos_add[1] <0 or pos_add in visited or graph[pos_add[0]][pos_add[1]] != rgb:
            continue
        
        visited.add(pos_add)
        dfs(pos_add, rgb)
        

n = int(input())
graph = []
visited = set()

for i in range(n):
    line = input()
    temp = []
    for j, ch in enumerate(line):
        temp.append(ch)
    graph.append(temp)

count1 = 0 
count2 = 0

for i in range(n):
    for j in range(n):
        if (i, j) in visited:
            continue
        dfs((i, j), graph[i][j])
        count1 += 1

visited.clear()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if (i, j) in visited:
            continue
        dfs((i, j), graph[i][j])
        count2 += 1

print(count1, count2)