import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visitors = [int(i) for i in input().split()]

max_vis = sum(visitors[:x])
sum_vis = max_vis
cnt = 1

for i, num in enumerate(visitors):
    if i <= x - 1:
        continue
    sum_vis = sum_vis + num - visitors[i - x]
    if max_vis == sum_vis:
        cnt+=1
    if max_vis < sum_vis:
        max_vis = sum_vis
        cnt = 1
if max_vis == 0:
    print("SAD")
    sys.exit()
print(f"{max_vis}\n{cnt}")