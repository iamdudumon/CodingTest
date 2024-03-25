import sys

input = sys.stdin.readline
print = sys.stdout.write

p = int(input())
for _ in range(1, p + 1):
    student = list(map(int, input().split()))
    sort_s = [0, student[1]]
    cnt = 0
    for i in range(1, 20):
        j = i
        while True:
            if sort_s[j] <= student[i + 1]:
                sort_s.insert(j + 1, student[i + 1])
                break
            j-=1
            cnt+=1
    print(f"{student[0]} {cnt}\n")