n, m = map(int, input().split())

answer_set = set()
answer = 0

for _ in range(n):
    str = input()
    answer_set.add(str)

for _ in range(m):
    str = input()
    if str in answer_set:
        answer += 1

print(answer)