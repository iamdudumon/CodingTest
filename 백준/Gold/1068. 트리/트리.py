import sys

input = sys.stdin.readline

def dfs(n):
	if n in tree:
		for key in tree[n]:
			dfs(key)
	array[n] = -1

N = int(input())
array = list(map(int, input().split()))
M = int(input())
tree = dict()
root = 0

for i in range(len(array)):
	if array[i] == -1:
		root = i
		if i == M:
			print(0)
			exit()
		continue
	if array[i] not in tree:
		tree[array[i]] = []
	tree[array[i]].append(i)

dfs(M)
s = set(array)
cnt = 0
for i in range(N):
	if i == root or array[i] != -1:
		cnt += 1

for i in range(N):
	if i in s:
		cnt -= 1
	
print(cnt)