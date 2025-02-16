import sys
sys.setrecursionlimit(10**6)

sys = sys.stdin.readline

def find(set, x):
	if set[x] != x:
		set[x] = find(set, set[x])
		return set[x]
	return x

def union(set, x,  y):
	x, y = find(set, x), find(set, y)
	set[max(x, y)] = min(x, y)

n, m = map(int, input().split())
root = [i for i in range(n + 1)]
for _ in range(m):
	c, a, b = map(int, input().split())
	if c == 0:
		union(root, a, b)
	if c == 1:
		if find(root, a) == find(root, b):
			print("YES")
		else:
			print("NO")