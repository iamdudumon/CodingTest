from sys import stdin, stdout

input = stdin.readline
write = stdout.write

n = int(input())
xi = list(map(int, input().split()))
xi_map = {x : i for i, x in enumerate(sorted(set(xi)))}
answer = [str(xi_map[x]) for x in xi]
write(" ".join(answer))