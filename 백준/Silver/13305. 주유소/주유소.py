import sys

input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = 0
i = 0
while i < n - 1:
    cur_cost = cost[i]
    more_cost = 0
    for j in range(i + 1, n):
        if cur_cost < cost[j]:
            more_cost+=1
    for j in range(more_cost + 1):
        min_cost += (cur_cost * distance[i + j])
    i += (more_cost + 1)

print(min_cost)