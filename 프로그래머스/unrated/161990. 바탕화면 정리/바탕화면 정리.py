def solution(wallpaper):
    # List comprehension
    answer = []
    wallpaper = [[0 if item == '.' else 1 for item in row]  for row in wallpaper]

   
    lux = len(wallpaper[0])
    rdx = 0
    state = False
    # luy, lux 계산
    for idx, row in enumerate(wallpaper):
        # luy
        if max(row) == 1 and not state:
            luy = idx
            state = True
        # lux
        for i, r in enumerate(row):
            if r == 1 and lux > i:
                lux = i


        # if max(row) == 1 and not state:
        #     luy = idx
    # rdy, rdx 계산 
    state = False 
    for idx in range(len(wallpaper) - 1, -1, -1):
        row = wallpaper[idx]
        # rdy
        if max(row) == 1 and not state:
            rdy = idx + 1
            state = True

        # rdx
        for i in range(len(row) - 1, -1, -1):
            if row[i] == 1 and rdx < i:
                rdx = i


    answer.append(luy)
    answer.append(lux)
    answer.append(rdy)
    answer.append(rdx + 1)

    return answer