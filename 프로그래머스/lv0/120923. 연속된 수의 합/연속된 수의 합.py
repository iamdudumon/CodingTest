def solution(num, total):
    answer = []

    if num % 2 == 0:
        average = total // num
        start = average - (num // 2 - 1)
    else:
        average = total / num
        start = int(average - num // 2)

    print(start)
    for i in range(start, start + num):
        answer.append(i)

    return answer