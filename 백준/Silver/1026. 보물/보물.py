n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

sum = 0
for idx in range(n):
    sum += A[idx] * B[idx]

print(sum)