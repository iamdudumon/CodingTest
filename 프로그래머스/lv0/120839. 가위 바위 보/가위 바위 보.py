def solution(rsp):
    answer = ''

    for ch in rsp:
        if ch == '2':
            answer += '0'
        elif ch == '0':
            answer += '5'
        else:
            answer += '2' 

    return answer