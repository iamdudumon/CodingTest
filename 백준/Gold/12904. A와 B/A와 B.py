import sys
input = sys.stdin.readline

a = list(input())[:-1]
b = list(input())[:-1]

target_size = len(a)

while(target_size != len(b)):
    if b[len(b) - 1] == 'A':
        b.pop()
    else:
        b.pop()
        b = b[::-1]

print(1 if a == b else 0)