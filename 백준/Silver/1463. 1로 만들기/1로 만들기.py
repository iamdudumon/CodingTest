n = int(input())

x = []
x.append(0)
x.append(0)
x.append(1)
x.append(1)

for idx in range(4, n + 1):
    if idx % 6 == 0:
        x.append(min(x[idx//3], x[idx//2], x[idx-1]) + 1)
    elif idx % 3 == 0:
        x.append(min(x[idx//3], x[idx-1]) + 1)
    elif idx % 2 == 0:
        x.append(min(x[idx//2], x[idx-1]) + 1)
    else:
        x.append(x[idx-1] + 1)

print(x[n])