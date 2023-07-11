def solution(order):
    answer = 0
    list_369 = ["3", "6", "9"]

    order = str(order)

    for ch in order:
        if ch in list_369:
            answer += 1

    return answer