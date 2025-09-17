import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dd = {}
maxx, minn = 0, 256

for i in range(N):
	for ii in range(M):
		maxx = max(maxx, matrix[i][ii])
		minn = min(minn, matrix[i][ii])
		if matrix[i][ii] in dd:
			dd[matrix[i][ii]]+=1
		else:
			dd[matrix[i][ii]] = 1

sorted_dd = sorted(dd.items(), key=lambda x : -x[0])
answer = [N * M * 256 * 2 + 1, -1]

for i in range(minn, maxx + 1):
	temp = 0
	b = B
	flag = False
	for k, v in sorted_dd:
		if k == i:
			continue
		elif i < k:
			temp+=2 * (k - i) * v
			b+=(k - i) * v
		else:
			if b < ((i - k) * v):
				flag = True
				break
			temp+=(i - k) * v
			b-=(i - k) * v
	if flag:
		continue

	if answer[0] >= temp:
		answer[0] = temp
		answer[1] = i

print(*answer)