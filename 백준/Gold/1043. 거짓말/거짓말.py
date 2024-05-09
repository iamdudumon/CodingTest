import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trues = set(list(map(int, input().split()))[1:])
if len(trues) == 0:
    print(m)
    sys.exit()

partys = [set() for _ in range(n+1)]
members = []
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    members.append(party)
    for p in party:
        for i in party:
            if p != i:
                partys[p].add(i)

while True:
    cp = trues.copy()
    for t in trues:
        for p in partys[t]:
            cp.add(p)
    if cp == trues:
        break
    trues = cp

cnt = len(members)
for mem in members:
    for m in mem:
        if m in trues:
            cnt-=1
            break
print(cnt)