from collections import deque

def solution(ingredient):
    answer = 0
    deq = deque()
    
    hamburger = [1,2,3,1]
    for item in ingredient:
        deq.append(item)
        if len(deq) >= 4:
            if [deq[-4], deq[-3], deq[-2], deq[-1]] == hamburger:
                answer += 1
                for _ in range(4):
                    deq.pop()
                    

    
    return answer