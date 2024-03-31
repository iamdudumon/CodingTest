import sys

input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_cost = cost[0]
total_cost = 0
for i in range(n - 1):
    if min_cost > cost[i]:
        min_cost = cost[i]
    total_cost += (distance[i] * min_cost)

print(total_cost)