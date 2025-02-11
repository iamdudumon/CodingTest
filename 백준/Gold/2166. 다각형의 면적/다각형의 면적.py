import sys

input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

sum1 = 0
sum2 = 0

for i in range(N):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % N]

    sum1 += x1 * y2
    sum2 += y1 * x2

print(round(abs(sum2 - sum1) / 2, 2))