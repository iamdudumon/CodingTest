import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
maxtrix = [list(map(int, input().split())) for _ in range(N)]
xys= [list(map(int, input().split())) for _ in range(M)]
row_maxtrix = copy.deepcopy(maxtrix)

# 1. 무식하게 다 구하기
# for xy in xys:
#     x1, y1, x2, y2 = xy
#     total = 0
#     for i in range(x1 - 1, x2):
#         for j in range(y1 - 1, y2):
#             total += maxtrix[j][i]
#     print(total)

# 2. 행, 열끼리 미리 다 누적시키기
for i in range(N):
    for j in range(1, N):
        row_maxtrix[j][i] += row_maxtrix[j - 1][i]

for i in range(N):
    for j in range(1, N):
        row_maxtrix[i][j] += row_maxtrix[i][j - 1]
    
for xy in xys:
    x1, y1, x2, y2 = xy
    total = row_maxtrix[x2 - 1][y2 - 1]
    if y1 > 1:
        total -= row_maxtrix[x2 - 1][y1 - 2]
    if x1 > 1:
        total -= row_maxtrix[x1 - 2][y2 - 1]
    if x1 > 1 and y1 > 1:
        total += row_maxtrix[x1 - 2][y1 - 2]
    print(total)