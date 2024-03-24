import sys
input = sys.stdin.readline

m = int(input())
s_set = set()

for _ in range(m):
    command = input().split()
    if len(command) == 2:
        command[1] = int(command[1])
    if command[0] == "add":
        if command[1] not in s_set:
            s_set.add(command[1])
    elif command[0] == "remove":
        if command[1] in s_set:
            s_set.remove(command[1])
    elif command[0] == "check":
        if command[1] in s_set:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if command[1] in s_set:
            s_set.remove(command[1])
        else:
             s_set.add(command[1])
    elif command[0] == "all":
        s_set = set([i for i in range(1, 21)])
    elif command[0] == "empty":
        s_set = set()