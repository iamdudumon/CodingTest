import sys

input = sys.stdin.readline

n, k = map(int, input().split())
medals = []
for i in range(n):
    medals.append(list(map(int, input().split())))
    if medals[i][0] == k:
        std_con = medals[i]
#medals = [list(map(int, input().split())) for _ in range(n)]
#std_con = medals[k + 1]
#print(std_con)
rank = 0
for i in range(n):
    cmp_con = medals[i]
    if cmp_con[0] == k:
        continue
    for j in range(1, 4):
        if cmp_con[j] > std_con[j]:
            rank+=1
            break
        if cmp_con[j] < std_con[j]:
            break
print(rank + 1)