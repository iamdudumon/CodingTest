def solution(answers):
    answer = []

    p_1 = 0

    p_2 = 0
    math_2 = [2, 1, 2, 3, 2, 4, 2, 5]

    p_3 = 0
    math_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    i = 0
    for ans in answers:
        # 1번 수포자
        if i % 5 + 1 == ans:
            p_1 += 1
        # 2번 수포자
        if math_2[i % len(math_2)] == ans:
            p_2 += 1
        # 3번 수포자
        if math_3[i % len(math_3)] == ans:
            p_3 += 1
        
        i += 1

    # 배열의 최대 값을 찾고 배열의 최대 값과 같은 지 확인하는 방법
    p = [p_1, p_2, p_3]
    for i in range(len(p)):
        if p[i] == max(p):
            answer.append(i + 1)
    


    return answer
