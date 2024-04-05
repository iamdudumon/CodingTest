n, row, col = map(int, input().split())
n = 2**n
count = -1
while n > 1:
    if row < n//2 and col < n//2:
        n//=2
        continue
    if row < n//2 and col < n:
        n//=2
        count+=n**2 * 1
        col-=n
        continue
    if row < n and col < n//2:
        n//=2
        count+=n**2 * 2
        row-=n
        continue
    if row < n and col < n:
        n//=2
        count+=n**2 * 3
        row-=n
        col-=n
        continue

for mv in ((0, 0), (0, 1), (1, 0), (1, 1)):
        count+=1
        if mv[0] == row and mv[1] == col:
            print(count)
            break