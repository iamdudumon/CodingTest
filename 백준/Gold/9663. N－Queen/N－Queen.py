import sys

input = sys.stdin.readline

n = int(input())
q_pos = [0] * n
cq = set()


def check_queen(queen_idx, row):
    if row in cq:
        return False

    for i in range(0, queen_idx):
        k = queen_idx - i
        if row > q_pos[i]:
            if row == q_pos[i] + k:
                return False
        else:
            if row == q_pos[i] - k:
                return False
    return True


def n_queen(queen_idx):
    if queen_idx == n:
        global cnt
        cnt += 1
        return

    for i in range(0, n):
        if check_queen(queen_idx, i):
            q_pos[queen_idx] = i
            cq.add(i)
            n_queen(queen_idx + 1)
            cq.remove(i)
            q_pos[queen_idx] = 0
    return False

cnt = 0
n_queen(0)
print(cnt)