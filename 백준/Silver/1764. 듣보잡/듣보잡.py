import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
no_see = set([input() for _ in range(n)])
no_hear = set([input() for _ in range(m)])
no_see_hear = list()

for see in no_see:
    if see in no_hear:
        no_see_hear.append(see)
no_see_hear.sort()
print(f"{len(no_see_hear)}\n")
for s_h in no_see_hear:
    print(s_h)