import sys

input = sys.stdin.readline

N = int(input())
liqs = list(map(int, input().split()))
liqs = sorted(liqs)
answer = [3000000001, [-1, -1, -1]]

for i in range(N - 1):
    start, end = i + 1, N - 1

    while start < end:
        std = liqs[i] + liqs[start] + liqs[end]

        if answer[0] > abs(std):
            answer[0] = abs(std)
            answer[1] = [liqs[i], liqs[start], liqs[end]]

        if std > 0:
            end-=1
        elif std < 0:
            start+=1
        else:
            break

print(*sorted(answer[1]))