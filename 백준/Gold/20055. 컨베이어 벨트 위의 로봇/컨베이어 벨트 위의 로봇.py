import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
robots = [False] * N

start = 0
stage = 0
while True:
    stage+=1

    start = (start - 1) % (2 * N)
    robots = [False] + robots[:-1]
    robots[-1] = False

    for i in range(N - 2, -1, -1):
        next = (start + 1 + i) % (2 * N)
        if robots[i] and A[next] and not robots[i + 1]:
            robots[i] = False
            robots[i + 1] = True
            A[next]-=1
            if A[next] == 0:
                K-=1

    if A[start]:
        A[start]-=1
        if A[start] == 0:
            K-=1
        robots[0] = True

    if K <= 0:
        break

print(stage)