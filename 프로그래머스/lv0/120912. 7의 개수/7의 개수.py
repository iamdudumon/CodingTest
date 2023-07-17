def solution(array):
    answer = 0

    for item in array:
        ch_item = str(item)
        for ch in ch_item:
            if ch == "7":
                answer += 1

    return answer