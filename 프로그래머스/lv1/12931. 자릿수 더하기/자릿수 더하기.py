def solution(n):
    answer = 0
    
    n_str = str(n)
    for ch in n_str:
        answer += int(ch)

    return answer