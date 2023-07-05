def solution(babbling):
    answer = 0

    speak = ["aya", "ye", "woo", "ma"]

    for str in babbling:
        str_copy = str
        count = 0
        for tmp in speak:
            if tmp in str_copy:
                str_copy = str_copy.replace(tmp, " ")
                count = count + 1
        if str_copy ==  " " * count :
            answer = answer + 1

    return answer