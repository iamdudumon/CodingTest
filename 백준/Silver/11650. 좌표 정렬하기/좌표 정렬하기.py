import sys
from operator import itemgetter

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
xy.sort(key=itemgetter(0,1))

for coor in xy:
    print(f"{coor[0]} {coor[1]}\n")