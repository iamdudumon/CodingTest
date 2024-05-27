from sys import stdin
import copy

input = stdin.readline

n = int(input())
line = list(map(int, input().split()))

dp_max = copy.deepcopy(line)
dp_min = copy.deepcopy(line)
dp_max_pre = copy.deepcopy(line)
dp_min_pre = copy.deepcopy(line)

for i in range(1, n):
    line = list(map(int, input().split()))

    dp_max[0] = max(dp_max_pre[0], dp_max_pre[1]) + line[0]
    dp_max[1] = max(dp_max_pre[0], dp_max_pre[1], dp_max_pre[2]) + line[1] 
    dp_max[2] = max(dp_max_pre[2], dp_max_pre[1]) + line[2]

    dp_min[0] = min(dp_min_pre[0], dp_min_pre[1]) + line[0] 
    dp_min[1] = min(dp_min_pre[0], dp_min_pre[1], dp_min_pre[2]) + line[1] 
    dp_min[2] = min(dp_min_pre[2], dp_min_pre[1]) + line[2]

    dp_max_pre = [dp_max[0], dp_max[1], dp_max[2]]
    dp_min_pre = [dp_min[0], dp_min[1], dp_min[2]]

print(max(dp_max), min(dp_min))