def solution(s):
    answer = []
    str_dict = {}

    i = 0
    for ch in s:
        if ch in str_dict:
            answer.append(i - str_dict[ch])
        else:
            answer.append(-1)
        str_dict[ch] = i
        i += 1

    return answer