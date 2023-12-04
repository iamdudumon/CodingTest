# 치킨 배달
import sys
input = sys.stdin.readline
from itertools import combinations

def distanc(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

N, M = map(int, input().split())
chickens = []
houses = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 2:
            chickens.append((i, j))
        elif row[j] == 1:        
            houses.append((i,j))

# print(*graph)

combi = list(combinations(chickens, M))
answer = N*N*N
for chicken_combi in combi:
    temp1 = 0
    for house in houses:
        temp2 = N*N
        for chicken in chicken_combi:
            if(temp2 > distanc(chicken, house)):
                temp2 = distanc(chicken, house)
        temp1 += temp2
    if answer > temp1:
        answer = temp1

print(answer)

   