import sys

input = sys.stdin.readline

N = int(input())
l = [tuple(map(int, input().split())) for _ in range(N)]

def communicate(t, s):
	if t >= N:
		return s
	if (t + l[t][0]) > N:
		return communicate(t + 1, s)

	return max(communicate(t + 1, s), communicate(t + l[t][0], s + l[t][1]))

print(communicate(0, 0))