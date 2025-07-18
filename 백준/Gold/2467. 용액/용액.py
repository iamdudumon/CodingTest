import sys

input = sys.stdin.readline

N = int(input())
liqs = list(map(int, input().split()))
answer = [2000000001, [-1, -1]]

def binary(liqs, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        std = liqs[key] + liqs[mid]

        if answer[0] > abs(std):
            answer[0] = abs(std)
            answer[1][0] = liqs[key]
            answer[1][1] = liqs[mid]
        
        if std > 0:
            high = mid - 1
        elif std < 0:
            low = mid + 1
        else:
            break
        

for i in range(N - 1):
    binary(liqs, i, i + 1, N - 1)

print(*answer[1])