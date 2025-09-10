import sys

sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def soluation(n, graph):
	visited = [0] * n
	cnt = 0

	def dfs(v, visited):
		nonlocal cnt
		visited[v] = 1
		vv = graph[v]

		if visited[vv] == 0:
			dfs(vv, visited)
		elif visited[vv] == 1: # is cycle -> team
			t = vv
			while True:
				t = graph[t]
				cnt+=1
				if t == vv:
					break

		visited[v] = 2

	for i in range(n):
		if visited[i] == 0:
			dfs(i, visited)
	
	print(n - cnt)

T = int(input())
for _ in range(T):
	n = int(input())
	students = list(map(int, input().split()))
	graph = [0] * n

	for i in range(n):
		graph[i] = students[i] - 1
	
	soluation(n, graph)