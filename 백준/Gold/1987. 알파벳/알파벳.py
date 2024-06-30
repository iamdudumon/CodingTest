import sys
import copy

input = sys.stdin.readline

def dfs(pos, cc):
	al = board[pos[0]][pos[1]]
	al_set[ord(al) - 65] = 1
	visited[pos[0]][pos[1]] = 1

	for mv in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
		next_pos = (pos[0] + mv[0], pos[1] + mv[1])
		if (0 <= next_pos[0] < R) and (0 <= next_pos[1] < C):
			if visited[next_pos[0]][next_pos[1]] == 1:
				continue
			if al_set[ord(board[next_pos[0]][next_pos[1]]) - 65] == 0:
				dfs(next_pos, cc + 1)
	global cnt
	cnt = max(cnt, cc)
	al_set[ord(al) - 65] = 0
	visited[pos[0]][pos[1]] = 0

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

cnt = 0
pos = (0, 0)
al_set = [0] * 26
visited = [[0] * C for _ in range(R)]
dfs(pos, 1)
print(cnt)