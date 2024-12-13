import sys

input = sys.stdin.readline

N = int(input())
array = [0] + list(map(int, input().split()))
for i in range(2, N + 1):
	array[i] += array[i - 1]

M = int(input())
for _ in range(M):
	i, j = map(int, input().split())
	print(array[j] - array[i - 1])