def solution(lottos, win_nums):
    answer = []
    count_0 = 0
    count = 0

    for num in lottos:
        if num == 0:
            count_0 += 1
        if num in win_nums:
            count += 1

    count_0 += count

    if count_0 <= 1:
        answer.append(6)
    else:
        answer.append(7 - count_0)

    if count <= 1:
        answer.append(6)
    else:
        answer.append(7 - count)

    

    return answer