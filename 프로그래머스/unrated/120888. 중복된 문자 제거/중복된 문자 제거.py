def solution(my_string):
    answer = ''
    str_set = set()
    
    for ch in list(my_string):
        if not ch in str_set:
            answer += ch
        str_set.add(ch)
    return answer