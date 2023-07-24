n = int(input())

for _ in range(n):
    str= input()
    str = [ch for ch in str]

    flag = True
    start = len(str) - 1
    stop = 0
    pair = [0, 0]

    while start > 0:
        for idx in range(start, stop -1 , -1):
            if str[start] > str[idx]:
                pair[0] = idx
                pair[1] = start
                stop = idx + 1
                flag = False
                break

        start -= 1

    if not flag:
        str[pair[0]], str[pair[1]] = str[pair[1]], str[pair[0]]
        str[pair[0] + 1:len(str)] = sorted(str[pair[0] + 1:len(str)])
    
    restult = "".join(str)
    print(restult)