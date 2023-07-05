def solution(A, B):
    answer = 0
    if A == B:
        return answer
    
    for _ in range(len(A)):
        answer += 1
        temp_A = A[len(A) - 1]
        for i in range(len(A) - 1):
            ch = A[i]
            temp_A += ch
        
        A = temp_A
        if A == B:
            return answer


    return -1