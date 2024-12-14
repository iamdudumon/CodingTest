import sys

input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
modular = [0] * N
cnts = [0] * M
cnt = 0

for i in range(N):
	array[i] += array[i - 1] if i > 0 else 0
	modular[i] = array[i] % M
	if modular[i] == 0:
		cnt += 1

for m in modular:
	cnts[m] += 1

for c in cnts:
	if c == 0:
		continue
	cnt += c * (c - 1) // 2

print(cnt)