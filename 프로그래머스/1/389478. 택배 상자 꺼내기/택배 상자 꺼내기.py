def solution(n, w, num):
    answer = 0
    
    while num <= n:
        p = (num - 1) // w
        q = (num - 1) % w + 1
        
        k = (w - q) * 2 + 1
        num += k
        # print(p, q)
        # print(num)
        answer += 1
    
    return answer