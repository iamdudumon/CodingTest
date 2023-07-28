n, l  = input().split()

if len(n) != len(l):
    print(0)
else:
    idx = 0
    count = 0
    while idx < len(l):
        if n[idx] == l[idx]:
            if n[idx] == '8':
                count += 1
            idx += 1
        else:
            break

    print(count)